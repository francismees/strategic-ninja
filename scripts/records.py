#!/usr/bin/env python3
"""Engagement records: validation, staleness propagation, rendering and storyline checks.

Standard library only (Python 3.8+). Uses the `jsonschema` package for schema checks when
it is installed; otherwise a built-in validator for the subset of JSON Schema used by
schemas/records.schema.json and schemas/outline.schema.json.

Commands
  validate  --records FILE                 schema + semantic rules (IDs, link types, claim-type
                                           requirements, traceability, unknowns, review flags)
  impact    --records FILE --changed ID    list every downstream record that depends on ID;
            [--set field=value] [--reason TEXT] [--author user|analyst] [--date YYYY-MM-DD]
            [--apply] [--output FILE]      with --apply, add review flags and a change-log entry
  render    --records FILE [--output FILE] readable Markdown registers with derived dependents
  outline   --outline FILE --records FILE  storyline contract: structure, evidence IDs resolve,
                                           evidence-bearing sections cite evidence, uncertainty is
                                           shown where linked evidence is uncertain, and the
                                           recommendation is not stated more strongly than recorded

Exit codes: 0 valid/ok, 2 invalid/error, 1 unexpected failure.
These checks are structural. They cannot establish source truth, insight quality or strategic fit.
"""

import argparse
import datetime
import json
import os
import re
import sys
from importlib.metadata import version as package_version

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RECORD_SCHEMA = os.path.join(ROOT, "schemas", "records.schema.json")
OUTLINE_SCHEMA = os.path.join(ROOT, "schemas", "outline.schema.json")

COLLECTIONS = {
    "sources": ("SRC",),
    "claims": ("CLM",),
    "hypotheses": ("HYP", "ASM"),
    "insights": ("INS",),
    "options": ("OPT",),
    "actions": ("ACT",),
    "metrics": ("MET",),
    "learnings": ("LRN",),
    "defects": ("DEF",),
    "changes": ("CHG",),
}
EVIDENCE_PREFIXES = {"SRC", "CLM", "HYP", "ASM", "INS"}
UNCERTAIN_CONFIDENCE = {"low", "unknown"}
DATE_RE = re.compile(r"^\d{4}(-\d{2}(-\d{2})?)?$")
UNKNOWN_RE = re.compile(r"^\s*unknown\b", re.IGNORECASE)
UNKNOWN_OK_RE = re.compile(r"^\s*unknown\s*:\s*\S.{2,}", re.IGNORECASE)


class Report:
    def __init__(self):
        self.errors = []
        self.warnings = []

    def error(self, code, record, message):
        self.errors.append({"code": code, "record": record, "message": message})

    def warn(self, code, record, message):
        self.warnings.append({"code": code, "record": record, "message": message})


def prefix(identifier):
    return identifier.split("-", 1)[0] if isinstance(identifier, str) and "-" in identifier else None


def load_json(path):
    with open(path, encoding="utf-8") as handle:
        return json.load(handle)


# ---------------------------------------------------------------------------
# Schema validation
# ---------------------------------------------------------------------------

TYPE_CHECKS = {
    "string": lambda v: isinstance(v, str),
    "number": lambda v: isinstance(v, (int, float)) and not isinstance(v, bool),
    "integer": lambda v: isinstance(v, int) and not isinstance(v, bool),
    "boolean": lambda v: isinstance(v, bool),
    "object": lambda v: isinstance(v, dict),
    "array": lambda v: isinstance(v, list),
    "null": lambda v: v is None,
}


def subset_validate(instance, schema, root, path, report):
    if "$ref" in schema:
        ref = schema["$ref"]
        if not ref.startswith("#/"):
            raise ValueError("Only local $ref supported: " + ref)
        target = root
        for part in ref[2:].split("/"):
            target = target[part]
        subset_validate(instance, target, root, path, report)
        return
    expected = schema.get("type")
    if expected:
        types = expected if isinstance(expected, list) else [expected]
        if not any(TYPE_CHECKS[t](instance) for t in types):
            report.error("SCHEMA", path or "$", "expected type {} but found {}".format("/".join(types), type(instance).__name__))
            return
    if "enum" in schema and instance not in schema["enum"]:
        report.error("SCHEMA", path or "$", "value {!r} not in {}".format(instance, schema["enum"]))
    if isinstance(instance, str):
        if "minLength" in schema and len(instance) < schema["minLength"]:
            report.error("SCHEMA", path or "$", "string shorter than {}".format(schema["minLength"]))
        if "pattern" in schema and not re.search(schema["pattern"], instance):
            report.error("SCHEMA", path or "$", "value {!r} does not match {}".format(instance, schema["pattern"]))
    if isinstance(instance, list):
        if "minItems" in schema and len(instance) < schema["minItems"]:
            report.error("SCHEMA", path or "$", "array has fewer than {} items".format(schema["minItems"]))
        if "items" in schema:
            for index, item in enumerate(instance):
                subset_validate(item, schema["items"], root, "{}[{}]".format(path, index), report)
    if isinstance(instance, dict):
        for key in schema.get("required", []):
            if key not in instance:
                report.error("SCHEMA", path or "$", "missing required field '{}'".format(key))
        properties = schema.get("properties", {})
        for key, value in instance.items():
            if key in properties:
                subset_validate(value, properties[key], root, "{}.{}".format(path, key) if path else key, report)
            elif schema.get("additionalProperties") is False:
                report.error("SCHEMA", path or "$", "unexpected field '{}'".format(key))


def schema_validate(instance, schema_path, report):
    schema = load_json(schema_path)
    try:
        import jsonschema  # optional
        validator = jsonschema.Draft202012Validator(schema)
        for error in sorted(validator.iter_errors(instance), key=lambda e: list(e.path)):
            report.error("SCHEMA", ".".join(str(p) for p in error.path) or "$", error.message)
        return "jsonschema " + package_version("jsonschema")
    except ImportError:
        subset_validate(instance, schema, schema, "", report)
        return "builtin-subset"


# ---------------------------------------------------------------------------
# Record graph helpers
# ---------------------------------------------------------------------------

def index_records(data):
    index = {}
    for collection in COLLECTIONS:
        for record in data.get(collection, []) or []:
            if isinstance(record, dict) and "id" in record:
                index.setdefault(record["id"], []).append((collection, record))
    return index


def dependencies(collection, record):
    """Return list of (field, id) that this record depends on."""
    deps = []
    def add(field, values):
        for value in values or []:
            deps.append((field, value))
    if collection == "sources":
        add("lineage.derived_from", record.get("lineage", {}).get("derived_from"))
    elif collection == "claims":
        add("basis.sources", record.get("basis", {}).get("sources"))
        add("basis.records", record.get("basis", {}).get("records"))
    elif collection == "hypotheses":
        add("basis_records", record.get("basis_records"))
        add("depends_on", record.get("depends_on"))
    elif collection == "insights":
        add("evidence", record.get("evidence"))
    elif collection == "options":
        add("supporting_records", record.get("supporting_records"))
        add("assumptions", record.get("assumptions"))
    elif collection == "actions":
        if record.get("decision_link"):
            deps.append(("decision_link", record["decision_link"]))
    elif collection == "metrics":
        add("actions", record.get("actions"))
    elif collection == "learnings":
        add("evidence_from", record.get("evidence_from"))
    return deps


def other_references(collection, record):
    refs = []
    if collection == "claims":
        refs += [("contradicts", r) for r in record.get("contradicts", []) or []]
        if record.get("superseded_by"):
            refs.append(("superseded_by", record["superseded_by"]))
    if collection == "actions":
        refs += [("metrics", r) for r in record.get("metrics", []) or []]
    if collection == "learnings":
        refs += [("affected_records", r) for r in record.get("affected_records", []) or []]
    if collection == "defects":
        refs += [("affected_records", r) for r in record.get("affected_records", []) or []]
    if collection == "changes":
        refs.append(("record_id", record.get("record_id")))
        refs += [("flagged", r) for r in record.get("flagged", []) or []]
    return refs


ALLOWED_LINKS = {
    ("sources", "lineage.derived_from"): {"SRC"},
    ("claims", "basis.sources"): {"SRC"},
    ("claims", "basis.records"): {"SRC", "CLM", "HYP", "ASM", "INS"},
    ("claims", "contradicts"): {"CLM"},
    ("claims", "superseded_by"): {"CLM"},
    ("hypotheses", "basis_records"): EVIDENCE_PREFIXES,
    ("hypotheses", "depends_on"): EVIDENCE_PREFIXES,
    ("insights", "evidence"): {"SRC", "CLM", "HYP", "ASM"},
    ("options", "supporting_records"): EVIDENCE_PREFIXES,
    ("options", "assumptions"): {"HYP", "ASM"},
    ("actions", "decision_link"): {"OPT"},
    ("actions", "metrics"): {"MET"},
    ("metrics", "actions"): {"ACT"},
    ("learnings", "evidence_from"): {"MET", "ACT", "CLM", "SRC"},
}


def reverse_graph(data):
    graph = {}
    for collection in COLLECTIONS:
        for record in data.get(collection, []) or []:
            for field, dep in dependencies(collection, record):
                graph.setdefault(dep, []).append((record["id"], field))
    return graph


def downstream(data, changed):
    graph = reverse_graph(data)
    seen, order, frontier, paths = set(), [], [changed], {changed: [changed]}
    while frontier:
        current = frontier.pop(0)
        for dependent, field in graph.get(current, []):
            if dependent not in seen and dependent != changed:
                seen.add(dependent)
                order.append(dependent)
                paths[dependent] = paths[current] + [dependent]
                frontier.append(dependent)
    return order, paths


# ---------------------------------------------------------------------------
# validate
# ---------------------------------------------------------------------------

def check_strings_for_unknown(obj, record_id, path, report):
    if isinstance(obj, str):
        if UNKNOWN_RE.match(obj) and not UNKNOWN_OK_RE.match(obj):
            report.warn("UNKNOWN_WITHOUT_REASON", record_id, "{} is 'unknown' without a reason; write 'unknown: <reason>'".format(path))
    elif isinstance(obj, dict):
        for key, value in obj.items():
            if key in ("level", "status", "current_support", "verification_status", "origin"):
                continue  # enum values such as confidence level 'unknown' are legitimate
            check_strings_for_unknown(value, record_id, "{}.{}".format(path, key), report)
    elif isinstance(obj, list):
        for i, value in enumerate(obj):
            check_strings_for_unknown(value, record_id, "{}[{}]".format(path, i), report)


def validate_records(data, report):
    index = index_records(data)
    for identifier, entries in index.items():
        if len(entries) > 1:
            report.error("DUPLICATE_ID", identifier, "ID used by {} records".format(len(entries)))
    for collection, prefixes in COLLECTIONS.items():
        for record in data.get(collection, []) or []:
            rid = record.get("id")
            if prefix(rid) not in prefixes:
                report.error("WRONG_COLLECTION", rid, "ID prefix does not belong in '{}'".format(collection))
            refs = dependencies(collection, record) + other_references(collection, record)
            for field, target in refs:
                if target is None:
                    continue
                if target not in index:
                    report.error("UNRESOLVED_REFERENCE", rid, "{} refers to {} which does not exist".format(field, target))
                    continue
                allowed = ALLOWED_LINKS.get((collection, field))
                if allowed and prefix(target) not in allowed:
                    code = "RECOMMENDATION_AS_EVIDENCE" if prefix(target) in ("OPT", "ACT") else "INVALID_LINK_TYPE"
                    report.error(code, rid, "{} may not point to {} ({})".format(field, target, "recommendations and actions are not evidence" if code == "RECOMMENDATION_AS_EVIDENCE" else "allowed: " + ", ".join(sorted(allowed))))
            check_strings_for_unknown({k: v for k, v in record.items() if k != "id"}, rid, collection, report)
            for flag in record.get("review_flags", []) or []:
                if not flag.get("resolved"):
                    report.warn("OPEN_REVIEW_FLAG", rid, "unresolved review flag: {} ({})".format(flag.get("reason"), flag.get("changed_record")))
            for field in ("recorded", "last_verified", "access_date", "date"):
                value = record.get(field)
                if isinstance(value, str) and not DATE_RE.match(value) and not UNKNOWN_OK_RE.match(value):
                    report.warn("DATE_FORMAT", rid, "{} '{}' is not YYYY, YYYY-MM or YYYY-MM-DD".format(field, value))

    records = {rid: entries[0][1] for rid, entries in index.items()}
    kinds = {rid: entries[0][0] for rid, entries in index.items()}

    for h in data.get("hypotheses", []) or []:
        expected_prefix = "HYP" if h.get("kind") == "hypothesis" else "ASM"
        if prefix(h.get("id")) != expected_prefix:
            report.error("KIND_PREFIX_MISMATCH", h.get("id"), "kind '{}' should use prefix {}".format(h.get("kind"), expected_prefix))

    for c in data.get("claims", []) or []:
        rid, basis = c.get("id"), c.get("basis", {})
        ctype, status = c.get("type"), c.get("verification_status")
        if ctype == "observed" and not basis.get("sources"):
            report.error("OBSERVED_WITHOUT_SOURCE", rid, "observed/reported claims need at least one source")
        if ctype == "computed" and not basis.get("calculation"):
            report.error("COMPUTED_WITHOUT_CALCULATION", rid, "computed findings need the calculation or script command")
        if ctype == "inference" and (not basis.get("reasoning") or not (basis.get("sources") or basis.get("records"))):
            report.error("INFERENCE_WITHOUT_BASIS", rid, "inferences need explicit reasoning and at least one dependency")
        if ctype == "estimate" and (not basis.get("method") or not basis.get("uncertainty")):
            report.error("ESTIMATE_WITHOUT_METHOD", rid, "estimates need a method and an uncertainty statement")
        if status == "verified" and ctype == "observed":
            source_locators = [records[s].get("locator", "") for s in basis.get("sources", []) if s in records]
            if not basis.get("locator") and not any(l and not UNKNOWN_RE.match(l) for l in source_locators):
                report.error("VERIFIED_WITHOUT_LOCATOR", rid, "verified claims need a specific locator in the claim or its source")
        if status == "reproduced" and ctype != "computed":
            report.error("REPRODUCED_NOT_COMPUTED", rid, "only computed findings can be 'reproduced'")
        if status == "superseded" and not c.get("superseded_by"):
            report.error("SUPERSEDED_WITHOUT_SUCCESSOR", rid, "superseded claims must name superseded_by")
        if c.get("verbatim") and (not (c.get("respondent_id") or basis.get("sources")) or not c.get("translation_status")):
            report.error("VERBATIM_WITHOUT_PROVENANCE", rid, "verbatim quotes need a respondent or source ID and a translation status")
        if status == "contested" and not c.get("contradicts"):
            report.warn("CONTESTED_WITHOUT_LINK", rid, "contested claims should link the conflicting claim(s) via 'contradicts'")

    for i in data.get("insights", []) or []:
        rid = i.get("id")
        evidence = i.get("evidence", [])
        if i.get("status") == "defensible":
            if not evidence:
                report.error("INSIGHT_WITHOUT_EVIDENCE", rid, "defensible insights need evidence")
            elif all(prefix(e) in ("HYP", "ASM") for e in evidence):
                report.error("INSIGHT_ON_HYPOTHESES_ONLY", rid, "an insight resting only on hypotheses/assumptions is a mechanism hypothesis, not a defensible insight")
            if i.get("confidence", {}).get("level") == "unknown":
                report.warn("DEFENSIBLE_WITH_UNKNOWN_CONFIDENCE", rid, "confidence not assessed for a defensible insight")

    selected_options = []
    for o in data.get("options", []) or []:
        rid, rtype, status = o.get("id"), o.get("recommendation_type"), o.get("status")
        if status == "selected":
            selected_options.append(o)
        if status in ("selected", "proposed") and rtype in ("supported", "conditional") and not o.get("supporting_records"):
            report.error("UNTRACEABLE_RECOMMENDATION", rid, "recommendation has no supporting records")
        if rtype == "conditional" and not (o.get("assumptions") or o.get("conditions")):
            report.error("CONDITIONAL_WITHOUT_CONDITIONS", rid, "conditional recommendations must state assumptions or conditions")
        if rtype == "research_first" and not o.get("conditions"):
            report.error("RESEARCH_FIRST_WITHOUT_TEST", rid, "research-first recommendations must state the discriminating test in conditions")
        if status == "selected" and not o.get("non_choices"):
            report.warn("NO_NON_CHOICES", rid, "selected option states no non-choices")
        for a in o.get("assumptions", []) or []:
            h = records.get(a)
            if not h:
                continue
            if h.get("status") == "refuted" or h.get("current_support") == "refuted":
                if status in ("selected", "proposed", "deferred"):
                    report.error("OPTION_RELIES_ON_REFUTED", rid, "relies on refuted {}".format(a))
                elif status == "status_quo":
                    report.warn("STATUS_QUO_RELIES_ON_REFUTED", rid, "status quo relies on refuted {}".format(a))
            elif rtype == "supported" and h.get("current_support") in ("untested", "mixed", "unsupported"):
                report.warn("SUPPORTED_WITH_UNTESTED_ASSUMPTION", rid, "{} is {}; consider a conditional recommendation".format(a, h.get("current_support")))
        if status == "selected" and rtype == "supported":
            for s in o.get("supporting_records", []) or []:
                r = records.get(s)
                if r and kinds.get(s) == "claims" and r.get("market_applicability", {}).get("status") in ("regional_proxy", "global_hypothesis", "unknown"):
                    report.warn("PROXY_EVIDENCE_IN_SUPPORTED_RECOMMENDATION", rid, "{} is {} evidence for the target market".format(s, r["market_applicability"]["status"]))

    options_by_id = {o.get("id"): o for o in data.get("options", []) or []}
    metrics_by_id = {m.get("id"): m for m in data.get("metrics", []) or []}
    for a in data.get("actions", []) or []:
        rid = a.get("id")
        linked = options_by_id.get(a.get("decision_link"))
        if linked and linked.get("status") == "rejected" and a.get("status") != "stopped":
            report.error("ACTION_ON_REJECTED_OPTION", rid, "action is linked to rejected option {}".format(linked.get("id")))
        if not a.get("metrics"):
            report.warn("ACTION_WITHOUT_METRIC", rid, "no metric defined")
        else:
            levels = {metrics_by_id[m].get("level") for m in a["metrics"] if m in metrics_by_id}
            if levels and levels <= {"exposure_output"}:
                report.warn("EXPOSURE_ONLY_MEASUREMENT", rid, "only exposure/output metrics; add behavioural or business measures")
        for m in a.get("metrics", []) or []:
            if m in metrics_by_id and rid not in (metrics_by_id[m].get("actions") or []):
                report.warn("ONE_WAY_METRIC_LINK", rid, "{} does not list this action".format(m))
    if data.get("actions"):
        for o in selected_options:
            if not any(a.get("decision_link") == o.get("id") for a in data["actions"]):
                report.warn("SELECTED_OPTION_WITHOUT_ACTIONS", o.get("id"), "selected option has no linked actions")

    for d in data.get("defects", []) or []:
        if d.get("verdict") == "FAIL" and d.get("status") == "open":
            for target in d.get("affected_records", []) or []:
                o = options_by_id.get(target)
                if o and o.get("status") == "selected" and o.get("recommendation_type") == "supported":
                    report.error("OPEN_FAIL_ON_SUPPORTED_RECOMMENDATION", target, "open FAIL {} affects a recommendation presented as supported".format(d.get("id")))

    return {collection: len(data.get(collection, []) or []) for collection in COLLECTIONS}


def cmd_validate(args):
    data = load_json(args.records)
    report = Report()
    validator = schema_validate(data, RECORD_SCHEMA, report)
    counts = None
    if isinstance(data, dict):
        counts = validate_records(data, report)
    return {
        "command": "validate",
        "status": "invalid" if report.errors else "valid",
        "schema_validator": validator,
        "counts": counts,
        "errors": report.errors,
        "warnings": report.warnings,
        "scope_note": "Structural checks only; they do not establish source truth, insight quality or strategic fit.",
    }, (2 if report.errors else 0)


# ---------------------------------------------------------------------------
# impact
# ---------------------------------------------------------------------------

def parse_value(text):
    try:
        return json.loads(text)
    except ValueError:
        return text


def cmd_impact(args):
    data = load_json(args.records)
    index = index_records(data)
    if args.changed not in index:
        return {"command": "impact", "status": "error", "code": "UNKNOWN_RECORD", "message": "{} not found".format(args.changed)}, 2
    collection, record = index[args.changed][0]
    flagged, paths = downstream(data, args.changed)
    date = args.date or datetime.date.today().isoformat()
    change_entry = None
    if args.set:
        if "=" not in args.set:
            return {"command": "impact", "status": "error", "code": "BAD_SET", "message": "--set must be field=value"}, 2
        field, raw = args.set.split("=", 1)
        previous = record.get(field)
        new = parse_value(raw)
        if isinstance(previous, (dict, list)) or isinstance(new, (dict, list)):
            return {"command": "impact", "status": "error", "code": "BAD_SET", "message": "--set supports top-level scalar fields only"}, 2
    else:
        field, previous, new = "(content)", None, None
    if args.apply:
        if not args.reason:
            return {"command": "impact", "status": "error", "code": "REASON_REQUIRED", "message": "--apply needs --reason"}, 2
        if args.set:
            record[field] = new
        for rid in flagged:
            target_collection, target = index[rid][0]
            if target_collection in ("learnings", "defects", "changes"):
                continue
            target.setdefault("review_flags", []).append({"changed_record": args.changed, "reason": args.reason, "date": date, "resolved": False})
        existing = [c.get("id", "") for c in data.get("changes", [])]
        number = 1
        while "CHG-{:03d}".format(number) in existing:
            number += 1
        change_entry = {"id": "CHG-{:03d}".format(number), "date": date, "record_id": args.changed, "field": field, "previous": previous, "new": new, "reason": args.reason, "author": args.author, "flagged": flagged}
        data.setdefault("changes", []).append(change_entry)
        out = args.output or args.records
        with open(out, "w", encoding="utf-8") as handle:
            json.dump(data, handle, indent=2, ensure_ascii=False)
            handle.write("\n")
    by_type = {}
    for rid in flagged:
        by_type.setdefault(index[rid][0][0], []).append(rid)
    return {
        "command": "impact",
        "status": "ok",
        "changed": args.changed,
        "changed_collection": collection,
        "flagged": flagged,
        "flagged_by_collection": by_type,
        "paths": {rid: " -> ".join(paths[rid]) for rid in flagged},
        "applied": bool(args.apply),
        "change_entry": change_entry,
        "note": "Flagged records must be reviewed before being presented as current; a flag does not mean they are wrong.",
    }, 0


# ---------------------------------------------------------------------------
# render
# ---------------------------------------------------------------------------

def md_escape(value):
    if value is None:
        return ""
    if isinstance(value, list):
        value = "; ".join(str(v) for v in value)
    elif isinstance(value, dict):
        value = ", ".join("{}: {}".format(k, v) for k, v in value.items())
    return str(value).replace("|", "\\|").replace("\n", " ")


def table(headers, rows):
    lines = ["| " + " | ".join(headers) + " |", "|" + "---|" * len(headers)]
    for row in rows:
        lines.append("| " + " | ".join(md_escape(v) for v in row) + " |")
    return lines


def cmd_render(args):
    data = load_json(args.records)
    graph = reverse_graph(data)
    dependents = lambda rid: sorted({d for d, _ in graph.get(rid, [])})
    e = data.get("engagement", {})
    lines = ["# Engagement records: {}".format(e.get("id", "")), ""]
    if e.get("synthetic"):
        lines += ["> **Synthetic teaching fixture — not real client data.**", ""]
    for label, key in (("Decision", "decision"), ("Decision-maker", "decision_maker"), ("Audience", "audience"), ("Client / brand / category / market", None), ("Horizon", "horizon"), ("Outcome", "outcome"), ("Success metric", "success_metric"), ("Baseline", "baseline"), ("Scope", "scope"), ("Mode / depth", None)):
        if key:
            lines.append("- **{}:** {}".format(label, md_escape(e.get(key))))
        elif label.startswith("Client"):
            lines.append("- **{}:** {} / {} / {} / {}".format(label, e.get("client"), e.get("brand"), e.get("category"), e.get("market")))
        else:
            lines.append("- **{}:** {} / {}".format(label, e.get("mode"), e.get("depth")))
    if e.get("constraints"):
        lines.append("- **Constraints:** " + md_escape(e["constraints"]))
    if e.get("unresolved_questions"):
        lines.append("- **Unresolved questions:** " + md_escape(e["unresolved_questions"]))
    sections = [
        ("Sources", "sources", ["ID", "Title", "Publisher", "Locator", "Data period", "Geography", "Method", "Lineage", "Limitations"],
         lambda r: [r["id"], r["title"], r["publisher_owner"], r["locator"], r["data_period"], r["geography"], r["method"], "{} {}".format(r["lineage"]["origin"], r["lineage"]["derived_from"] or ""), r["limitations"]]),
        ("Claims and findings", "claims", ["ID", "Statement", "Type", "Basis", "Confidence", "Market applicability", "Verification", "Used by"],
         lambda r: [r["id"], r["statement"], r["type"], (r["basis"].get("sources") or []) + (r["basis"].get("records") or []), "{} — {}".format(r["confidence"]["level"], r["confidence"]["reason"]), "{} ({})".format(r["market_applicability"]["status"], r["market_applicability"]["scope"]), r["verification_status"], dependents(r["id"])]),
        ("Hypotheses and assumptions", "hypotheses", ["ID", "Kind", "Proposition", "Confirming signal", "Falsifier", "Support", "Status", "Decision impact", "Validation step", "Used by"],
         lambda r: [r["id"], r["kind"], r["proposition"], r["confirming_signal"], r["falsifier"], r["current_support"], r["status"], r["decision_impact"], r["validation_step"], dependents(r["id"])]),
        ("Insights", "insights", ["ID", "Explanation", "Observation", "Contrast", "Mechanism", "Tension", "Alternatives", "Confidence", "Status", "Implication"],
         lambda r: [r["id"], r["explanation"], r["observation"], r["contrast"], r["mechanism"], r.get("tension") or "—", r["alternatives"], r["confidence"]["level"], r["status"], r["implication"]]),
        ("Options and decisions", "options", ["ID", "Title", "Status", "Recommendation type", "Decision state", "Mechanism", "Assumptions", "Non-choices", "Reversal triggers"],
         lambda r: [r["id"], r["title"], r["status"], r["recommendation_type"], r["decision_state"], "{}: {}".format(", ".join(r["mechanism"]["levers"]), r["mechanism"]["explanation"]), r["assumptions"], r["non_choices"], r["reversal_triggers"]]),
        ("Actions", "actions", ["ID", "Decision", "Action", "Intended change", "Owner role", "Timing", "Resource basis", "Metrics", "Reversal trigger", "Status"],
         lambda r: [r["id"], r["decision_link"], r["description"], r["intended_change"], r["owner_role"], r["timing"], r["resource_basis"], r["metrics"], r["reversal_trigger"], r["status"]]),
        ("Metrics", "metrics", ["ID", "Definition", "Level", "Leading/lagging", "Baseline", "Target rationale", "Source", "Cadence", "Decision rule"],
         lambda r: [r["id"], r["definition"], r["level"], r["timing_role"], r["baseline"], r["target_rationale"], r["data_source"], r["cadence"], r["decision_rule"]]),
        ("Learnings", "learnings", ["ID", "From", "Observed result", "Interpretation", "Enters as", "Affected", "Status"],
         lambda r: [r["id"], r["evidence_from"], r["observed_result"], r["interpretation"], r["enters_as"], r["affected_records"], r["status"]]),
        ("Red-team defects", "defects", ["ID", "Claim/section", "Gate", "Verdict", "Defect", "Evidence", "Consequence", "Fix", "Retest", "Status"],
         lambda r: [r["id"], r["claim_or_section"], r["gate"], r["verdict"], r["defect"], r["evidence_or_missing_evidence"], r["strategic_consequence"], r["required_fix"], r["retest_condition"], r["status"]]),
        ("Change log", "changes", ["ID", "Date", "Record", "Field", "Previous", "New", "Reason", "Flagged"],
         lambda r: [r["id"], r["date"], r["record_id"], r["field"], r["previous"], r["new"], r["reason"], r["flagged"]]),
    ]
    for title, key, headers, row in sections:
        items = data.get(key) or []
        if not items:
            continue
        lines += ["", "## " + title, ""]
        lines += table(headers, [row(r) for r in items])
    if data.get("gate_results"):
        lines += ["", "## Gate verdicts", ""] + table(["Gate", "Verdict", "Reason", "Defects"], [[g["gate"], g["verdict"], g["reason"], g.get("defects")] for g in data["gate_results"]])
    open_flags = [(r["id"], f) for c in COLLECTIONS for r in data.get(c, []) or [] for f in r.get("review_flags", []) or [] if not f.get("resolved")]
    if open_flags:
        lines += ["", "## Open review flags", ""] + table(["Record", "Changed record", "Reason", "Date"], [[rid, f["changed_record"], f["reason"], f["date"]] for rid, f in open_flags])
    text = "\n".join(lines) + "\n"
    if args.output:
        with open(args.output, "w", encoding="utf-8") as handle:
            handle.write(text)
        return {"command": "render", "status": "ok", "output": args.output}, 0
    return text, 0


# ---------------------------------------------------------------------------
# outline
# ---------------------------------------------------------------------------

EVIDENCE_ROLES = {"diagnosis", "evidence", "insight", "recommendation", "alternatives", "economics", "risk", "measurement"}
STRENGTH = {"supported": 3, "conditional": 2, "research_first": 1, "not_recommended": 0}


def uncertain_reasons(rid, collection, record):
    reasons = []
    level = (record.get("confidence") or {}).get("level")
    if level in UNCERTAIN_CONFIDENCE:
        reasons.append("{} confidence is {}".format(rid, level))
    if collection == "claims" and record.get("verification_status") in ("unverified", "contested"):
        reasons.append("{} is {}".format(rid, record["verification_status"]))
    if collection == "claims" and record.get("type") == "estimate":
        reasons.append("{} is an estimate".format(rid))
    if collection == "claims" and (record.get("market_applicability") or {}).get("status") in ("regional_proxy", "global_hypothesis", "unknown"):
        reasons.append("{} is {} for the target market".format(rid, record["market_applicability"]["status"]))
    if collection == "hypotheses" and record.get("status") in ("open", "accepted_for_planning", "weakened"):
        reasons.append("{} is an untested or planning {}".format(rid, record.get("kind")))
    if collection == "insights" and record.get("status") == "mechanism_hypothesis":
        reasons.append("{} is a mechanism hypothesis".format(rid))
    if collection == "options" and record.get("recommendation_type") in ("conditional", "research_first"):
        reasons.append("{} is a {} recommendation".format(rid, record["recommendation_type"]))
    if any(not f.get("resolved") for f in record.get("review_flags", []) or []):
        reasons.append("{} has an open review flag".format(rid))
    return reasons


def cmd_outline(args):
    outline = load_json(args.outline)
    data = load_json(args.records)
    report = Report()
    validator = schema_validate(outline, OUTLINE_SCHEMA, report)
    index = index_records(data)
    if report.errors:
        return {"command": "outline", "status": "invalid", "schema_validator": validator, "errors": report.errors, "warnings": report.warnings}, 2
    seen = set()
    for section in outline.get("sections", []):
        sid, role = section["id"], section["role"]
        if sid in seen:
            report.error("DUPLICATE_SECTION_ID", sid, "section ID repeated")
        seen.add(sid)
        evidence = section.get("evidence_ids", [])
        if role in EVIDENCE_ROLES and not evidence:
            report.error("ASSERTION_WITHOUT_EVIDENCE", sid, "'{}' sections must cite evidence or decision records".format(role))
        reasons = []
        for rid in evidence:
            if rid not in index:
                report.error("UNRESOLVED_EVIDENCE", sid, "{} not found in records".format(rid))
                continue
            collection, record = index[rid][0]
            if prefix(rid) in ("OPT", "ACT", "MET") and role in ("diagnosis", "evidence", "insight"):
                report.error("RECOMMENDATION_CITED_AS_EVIDENCE", sid, "{} is a decision/action record, not evidence for a {} assertion".format(rid, role))
            reasons += uncertain_reasons(rid, collection, record)
            if collection in ("sources", "claims") and not section.get("source_locators"):
                report.warn("MISSING_LOCATORS", sid, "cites {} without source locators for the exhibit".format(rid))
            if any(not f.get("resolved") for f in record.get("review_flags", []) or []):
                report.warn("STALE_EVIDENCE", sid, "{} has an unresolved review flag".format(rid))
            if collection == "options" and role == "recommendation":
                stated = outline.get("recommendation_type")
                recorded = record.get("recommendation_type")
                if stated and recorded and STRENGTH.get(stated, 0) > STRENGTH.get(recorded, 0):
                    report.error("RECOMMENDATION_STRENGTH_MISMATCH", sid, "storyline states a {} recommendation but {} is recorded as {}".format(stated, rid, recorded))
        if reasons and not (section.get("uncertainty") or "").strip():
            report.error("UNCERTAINTY_NOT_SHOWN", sid, "linked evidence is uncertain ({}) but the section states no uncertainty".format("; ".join(sorted(set(reasons)))))
    if not any(s["role"] == "ask" for s in outline.get("sections", [])):
        report.warn("NO_ASK_SECTION", outline.get("title"), "storyline has no explicit decision/ask section")
    return {
        "command": "outline",
        "status": "invalid" if report.errors else "valid",
        "schema_validator": validator,
        "sections": len(outline.get("sections", [])),
        "errors": report.errors,
        "warnings": report.warnings,
        "scope_note": "Checks structure and evidence links. Whether each slide's evidence actually supports its assertion, and whether the sequence forms a coherent argument, requires judgement.",
    }, (2 if report.errors else 0)


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = parser.add_subparsers(dest="command")
    p = sub.add_parser("validate")
    p.add_argument("--records", required=True)
    p.set_defaults(func=cmd_validate)
    p = sub.add_parser("impact")
    p.add_argument("--records", required=True)
    p.add_argument("--changed", required=True)
    p.add_argument("--set")
    p.add_argument("--reason")
    p.add_argument("--author", choices=["user", "analyst", "script"], default="analyst")
    p.add_argument("--date")
    p.add_argument("--apply", action="store_true")
    p.add_argument("--output")
    p.set_defaults(func=cmd_impact)
    p = sub.add_parser("render")
    p.add_argument("--records", required=True)
    p.add_argument("--output")
    p.set_defaults(func=cmd_render)
    p = sub.add_parser("outline")
    p.add_argument("--outline", required=True)
    p.add_argument("--records", required=True)
    p.set_defaults(func=cmd_outline)
    args = parser.parse_args(argv)
    if not getattr(args, "func", None):
        parser.print_help()
        return 1
    try:
        result, code = args.func(args)
    except FileNotFoundError as error:
        result, code = {"command": args.command, "status": "error", "code": "FILE_NOT_FOUND", "message": str(error)}, 2
    except ValueError as error:
        result, code = {"command": args.command, "status": "error", "code": "INVALID_JSON", "message": str(error)}, 2
    print(result if isinstance(result, str) else json.dumps(result, indent=2, ensure_ascii=False))
    return code


if __name__ == "__main__":
    sys.exit(main())
