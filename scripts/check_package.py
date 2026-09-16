#!/usr/bin/env python3
"""Deterministic package checks for the strategic-ninja skill, and archive building.

Standard library only (Python 3.8+).

Checks
  frontmatter   SKILL.md frontmatter follows the Agent Skills specification (name format and
                length, matches folder, description 1-1024 chars without angle brackets,
                compatibility <= 500 chars, only fields accepted for Claude app upload)
  size          SKILL.md under 500 lines; estimated tokens reported against the ~5,000 guide
  links         every relative Markdown link in every .md file resolves
  routing       every module in references/, workflows/, markets/, templates/, integrations/
                is linked directly from SKILL.md
  reachability  every packaged file is reachable by links from SKILL.md or README.md
  hygiene       no empty folders, caches, .DS_Store or compiled files; every JSON file parses
  privacy       no e-mail addresses outside an allow-list
  records       example records, storyline outlines, the blank template and the Tanzania
                observations validate (scripts/records.py rules)
  scripts       all Python scripts compile

Usage
  python3 scripts/check_package.py                 # run checks
  python3 scripts/check_package.py --run-fixtures  # also run deterministic fixtures
  python3 scripts/check_package.py --zip ../dist/strategic-ninja.zip
  python3 scripts/check_package.py --json results.json

These checks prove structure and arithmetic plumbing, not source truth, insight quality or strategic fit.
"""

import argparse
import datetime
import json
import os
import py_compile
import re
import subprocess
import sys
import tempfile
import zipfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.dont_write_bytecode = True
sys.path.insert(0, os.path.join(ROOT, "scripts"))
import records as records_lib  # noqa: E402

ALLOWED_UPLOAD_KEYS = {"name", "description", "license", "allowed-tools", "metadata", "compatibility"}
JUNK_NAMES = {".DS_Store", "__pycache__", "Thumbs.db"}
JUNK_SUFFIXES = (".pyc", ".pyo")
EMAIL_ALLOW = {"noreply@anthropic.com"}
LINK_RE = re.compile(r"(?<!!)\[[^\]]*\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)")
EMAIL_RE = re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}")
ROUTED_DIRS = ("references", "workflows", "markets", "templates", "integrations")


class Results:
    def __init__(self):
        self.items = []

    def add(self, check, status, detail):
        self.items.append({"check": check, "status": status, "detail": detail})

    @property
    def errors(self):
        return [i for i in self.items if i["status"] == "ERROR"]


def parse_frontmatter(text):
    if not text.startswith("---\n"):
        return None, "SKILL.md does not start with '---'"
    end = text.find("\n---", 4)
    if end == -1:
        return None, "frontmatter is not closed"
    block = text[4:end]
    data, current_map = {}, None
    for raw in block.splitlines():
        if not raw.strip():
            continue
        if raw.startswith("  ") and current_map is not None:
            key, _, value = raw.strip().partition(":")
            data[current_map][key.strip()] = value.strip().strip('"').strip("'")
            continue
        key, _, value = raw.partition(":")
        key, value = key.strip(), value.strip()
        if value == "":
            data[key] = {}
            current_map = key
        else:
            data[key] = value.strip('"').strip("'")
            current_map = None
    return data, None


def package_files():
    out = []
    for base, dirs, files in os.walk(ROOT):
        dirs[:] = [d for d in dirs if d not in JUNK_NAMES and not d.startswith(".git")]
        for name in files:
            out.append(os.path.relpath(os.path.join(base, name), ROOT))
    return sorted(out)


def check_frontmatter(res):
    text = open(os.path.join(ROOT, "SKILL.md"), encoding="utf-8").read()
    fm, problem = parse_frontmatter(text)
    if problem:
        res.add("frontmatter", "ERROR", problem)
        return
    folder = os.path.basename(ROOT)
    name, desc = fm.get("name", ""), fm.get("description", "")
    issues = []
    if not re.fullmatch(r"[a-z0-9]+(-[a-z0-9]+)*", name or ""):
        issues.append("name must be lowercase letters, digits and single hyphens")
    if len(name) > 64:
        issues.append("name longer than 64 characters")
    if name != folder:
        issues.append("name '{}' does not match folder '{}'".format(name, folder))
    if not 1 <= len(desc) <= 1024:
        issues.append("description length {} outside 1-1024".format(len(desc)))
    if "<" in desc or ">" in desc:
        issues.append("description contains angle brackets")
    if "compatibility" in fm and len(fm["compatibility"]) > 500:
        issues.append("compatibility longer than 500 characters")
    extra = set(fm) - ALLOWED_UPLOAD_KEYS
    if extra:
        issues.append("fields not accepted for app upload: {}".format(sorted(extra)))
    if isinstance(fm.get("metadata"), dict) and not all(isinstance(v, str) for v in fm["metadata"].values()):
        issues.append("metadata values must be strings")
    if issues:
        res.add("frontmatter", "ERROR", "; ".join(issues))
    else:
        res.add("frontmatter", "PASS", "name '{}' ({} chars); description {} chars; fields {}".format(name, len(name), len(desc), sorted(fm)))


def check_size(res):
    text = open(os.path.join(ROOT, "SKILL.md"), encoding="utf-8").read()
    lines = text.count("\n") + 1
    words = len(re.findall(r"\S+", text))
    est_tokens = int(max(len(text) / 4.0, words * 1.33))
    status = "ERROR" if lines >= 500 else ("WARN" if est_tokens > 5000 else "PASS")
    res.add("size", status, "SKILL.md {} lines, {} words, about {} tokens (estimate: max of chars/4 and words x 1.33; guide: under 500 lines and about 5,000 tokens)".format(lines, words, est_tokens))


def md_links(path):
    text = open(os.path.join(ROOT, path), encoding="utf-8").read()
    text = re.sub(r"```.*?```", "", text, flags=re.S)
    links = []
    for target in LINK_RE.findall(text):
        if re.match(r"^[a-z]+:", target) or target.startswith("#"):
            continue
        links.append(target.split("#", 1)[0])
    return links


def resolve(from_file, target):
    full = os.path.normpath(os.path.join(ROOT, os.path.dirname(from_file), target))
    return full


def check_links(res, files):
    broken = []
    for f in files:
        if not f.endswith(".md"):
            continue
        for target in md_links(f):
            if not os.path.exists(resolve(f, target)):
                broken.append("{} -> {}".format(f, target))
    res.add("links", "ERROR" if broken else "PASS", broken if broken else "all relative Markdown links resolve")


def check_routing(res):
    linked = {os.path.relpath(resolve("SKILL.md", t), ROOT) for t in md_links("SKILL.md")}
    missing = []
    for d in ROUTED_DIRS:
        for name in sorted(os.listdir(os.path.join(ROOT, d))):
            rel = os.path.join(d, name)
            if os.path.isfile(os.path.join(ROOT, rel)) and rel not in linked:
                missing.append(rel)
    res.add("routing", "ERROR" if missing else "PASS", missing if missing else "every module in {} is linked directly from SKILL.md".format(", ".join(ROUTED_DIRS)))


def check_reachability(res, files):
    seen, frontier = set(), ["SKILL.md", "README.md"]
    while frontier:
        f = frontier.pop()
        if f in seen or not os.path.exists(os.path.join(ROOT, f)):
            continue
        seen.add(f)
        if os.path.isdir(os.path.join(ROOT, f)):
            readme = os.path.join(f, "README.md")
            if os.path.exists(os.path.join(ROOT, readme)):
                frontier.append(readme)
            continue
        if f.endswith(".md"):
            for target in md_links(f):
                full = resolve(f, target)
                if full.startswith(ROOT) and os.path.exists(full):
                    frontier.append(os.path.relpath(full, ROOT))
    # files inside a linked directory count as reachable through that directory
    linked_dirs = {s for s in seen if os.path.isdir(os.path.join(ROOT, s))}
    unreachable = [f for f in files if f not in seen and not any(f.startswith(d.rstrip("/") + "/") for d in linked_dirs)]
    res.add("reachability", "WARN" if unreachable else "PASS", unreachable if unreachable else "all {} files reachable from SKILL.md or README.md".format(len(files)))


def check_hygiene(res, files):
    problems = []
    for base, dirs, names in os.walk(ROOT):
        rel = os.path.relpath(base, ROOT)
        if any(part in JUNK_NAMES for part in rel.split(os.sep)):
            problems.append("junk folder: " + rel)
            continue
        if not dirs and not names:
            problems.append("empty folder: " + rel)
        for n in names:
            if n in JUNK_NAMES or n.endswith(JUNK_SUFFIXES):
                problems.append("junk file: " + os.path.join(rel, n))
    bad_json = []
    for f in files:
        if f.endswith(".json"):
            try:
                json.load(open(os.path.join(ROOT, f), encoding="utf-8"))
            except ValueError as error:
                bad_json.append("{}: {}".format(f, error))
    status = "ERROR" if bad_json else ("WARN" if problems else "PASS")
    res.add("hygiene", status, (problems + bad_json) if (problems or bad_json) else "no empty folders, caches or junk; all JSON parses")


def check_privacy(res, files):
    found = []
    for f in files:
        if f.endswith((".md", ".json", ".csv", ".py", ".txt")):
            for match in EMAIL_RE.findall(open(os.path.join(ROOT, f), encoding="utf-8", errors="ignore").read()):
                if match.lower() not in EMAIL_ALLOW:
                    found.append("{}: {}".format(f, match))
    res.add("privacy", "WARN" if found else "PASS", found if found else "no e-mail addresses found")


def check_records(res, files):
    problems, summary = [], []
    for f in files:
        base = os.path.basename(f)
        path = os.path.join(ROOT, f)
        if base in ("records.json", "engagement-records.json") and not f.startswith("evals/"):
            report = records_lib.Report()
            data = json.load(open(path, encoding="utf-8"))
            records_lib.schema_validate(data, records_lib.RECORD_SCHEMA, report)
            records_lib.validate_records(data, report)
            summary.append("{}: {} errors, {} warnings".format(f, len(report.errors), len(report.warnings)))
            if report.errors:
                problems.append("{}: {}".format(f, report.errors[:5]))
    for f in files:
        if f.endswith("outline.json") and not os.path.basename(f).startswith("original-"):
            records_file = os.path.join(os.path.dirname(f), "records.json")
            args = argparse.Namespace(outline=os.path.join(ROOT, f), records=os.path.join(ROOT, records_file))
            result, code = records_lib.cmd_outline(args)
            summary.append("{}: {}".format(f, result["status"]))
            if code != 0:
                problems.append("{}: {}".format(f, result["errors"][:5]))
    obs_path = os.path.join(ROOT, "markets", "tanzania-observations.json")
    if os.path.exists(obs_path):
        schema = json.load(open(records_lib.RECORD_SCHEMA, encoding="utf-8"))
        obs = json.load(open(obs_path, encoding="utf-8"))
        report = records_lib.Report()
        ids = {s["id"] for s in obs.get("sources", [])} | {c["id"] for c in obs.get("claims", [])}
        for s in obs.get("sources", []):
            records_lib.subset_validate(s, schema["$defs"]["source"], schema, s.get("id", "source"), report)
        for c in obs.get("claims", []):
            records_lib.subset_validate(c, schema["$defs"]["claim"], schema, c.get("id", "claim"), report)
            for ref in c["basis"].get("sources", []) + c["basis"].get("records", []):
                if ref not in ids:
                    report.error("UNRESOLVED_REFERENCE", c["id"], ref)
        summary.append("markets/tanzania-observations.json: {} errors".format(len(report.errors)))
        if report.errors:
            problems.append("tanzania-observations: {}".format(report.errors[:5]))
    res.add("records", "ERROR" if problems else "PASS", problems if problems else summary)


def check_scripts(res):
    bad = []
    with tempfile.TemporaryDirectory() as tmp:
        for name in sorted(os.listdir(os.path.join(ROOT, "scripts"))):
            if name.endswith(".py"):
                try:
                    py_compile.compile(os.path.join(ROOT, "scripts", name), cfile=os.path.join(tmp, name + "c"), doraise=True)
                except py_compile.PyCompileError as error:
                    bad.append(str(error))
    res.add("scripts", "ERROR" if bad else "PASS", bad if bad else "all scripts compile on Python {}".format(sys.version.split()[0]))


def run_fixtures(res):
    proc = subprocess.run([sys.executable, os.path.join(ROOT, "scripts", "run_fixtures.py")], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, universal_newlines=True)
    last = [l for l in proc.stdout.splitlines() if "fixtures passed" in l]
    res.add("fixtures", "PASS" if proc.returncode == 0 else "ERROR", last[-1] if last else proc.stdout[-500:])


def build_zip(path, files):
    path = os.path.abspath(path)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    folder = os.path.basename(ROOT)
    with zipfile.ZipFile(path, "w", zipfile.ZIP_DEFLATED) as archive:
        for f in files:
            archive.write(os.path.join(ROOT, f), os.path.join(folder, f))
    return path


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--run-fixtures", action="store_true")
    parser.add_argument("--zip", help="write an archive with the skill folder at its root")
    parser.add_argument("--json", help="write results as JSON to this path")
    args = parser.parse_args()
    files = [f for f in package_files() if os.path.basename(f) not in JUNK_NAMES and not f.endswith(JUNK_SUFFIXES)]
    res = Results()
    check_frontmatter(res)
    check_size(res)
    check_links(res, files)
    check_routing(res)
    check_reachability(res, files)
    check_hygiene(res, files)
    check_privacy(res, files)
    check_records(res, files)
    check_scripts(res)
    if args.run_fixtures:
        run_fixtures(res)
    for item in res.items:
        detail = item["detail"]
        if isinstance(detail, list):
            detail = "\n      " + "\n      ".join(str(d) for d in detail)
        print("[{}] {}: {}".format(item["status"], item["check"], detail))
    if args.zip:
        if res.errors:
            print("Not building archive: errors present.")
        else:
            out = build_zip(args.zip, files)
            print("Archive written: {} ({} files, {:.0f} KB)".format(out, len(files), os.path.getsize(out) / 1024))
    if args.json:
        with open(args.json, "w", encoding="utf-8") as handle:
            json.dump({"run_at": datetime.datetime.now(datetime.timezone.utc).replace(microsecond=0).isoformat(), "python": sys.version.split()[0], "files": len(files), "results": res.items}, handle, indent=2)
    print("\n{} checks, {} errors, {} warnings.".format(len(res.items), len(res.errors), sum(1 for i in res.items if i["status"] == "WARN")))
    return 1 if res.errors else 0


if __name__ == "__main__":
    sys.exit(main())
