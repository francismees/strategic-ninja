#!/usr/bin/env python3
"""Run the deterministic fixtures in evals/fixtures/.

Standard library only. Each analytics fixture stores raw input, an independently
established expected output (hand derivation recorded in the fixture), the calculation
convention, tolerance, the edge-case expectation and the expected failure behaviour.
Records fixtures check schema validation, ID resolution, staleness propagation and
storyline evidence links.

Usage:
  python3 scripts/run_fixtures.py                 # run all, print summary
  python3 scripts/run_fixtures.py --verbose       # show every check
  python3 scripts/run_fixtures.py --write evals/results/deterministic-latest.json

These checks establish arithmetic and structural correctness only. They do not
establish causality, source truth or strategic validity.
"""

import argparse
import datetime
import glob
import json
import os
import subprocess
import sys
import tempfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ANALYTICS = os.path.join(ROOT, "scripts", "commercial_analysis.py")
RECORDS = os.path.join(ROOT, "scripts", "records.py")


def get_path(data, dotted):
    current = data
    for part in dotted.split("."):
        if isinstance(current, list):
            current = current[int(part)]
        elif isinstance(current, dict):
            if part not in current:
                raise KeyError(dotted)
            current = current[part]
        else:
            raise KeyError(dotted)
    return current


def values_match(actual, expected, tolerance):
    if isinstance(expected, (int, float)) and not isinstance(expected, bool) and isinstance(actual, (int, float)) and not isinstance(actual, bool):
        return abs(actual - expected) <= tolerance
    return actual == expected


def run_command(cmd):
    proc = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    try:
        payload = json.loads(proc.stdout) if proc.stdout.strip() else {}
    except ValueError:
        payload = {"status": "unparseable", "raw": proc.stdout[:2000]}
    return proc.returncode, payload, proc.stderr


def check_process_stderr(returncode, stderr, checks):
    """Fail only on evidence of an unexpected subprocess failure, not benign warnings."""
    text = stderr.strip()
    if not text:
        return
    if returncode not in (0, 2) or "Traceback (most recent call last):" in text:
        checks.append(("no uncaught exception", False, text[-500:]))


def check_common(fixture, payload, returncode, checks):
    status = payload.get("status")
    expected_status = fixture["expected_status"]
    checks.append(("status == {}".format(expected_status), status == expected_status, status))
    if expected_status == "error":
        checks.append(("exit code 2", returncode == 2, returncode))
        code = fixture.get("expected_error_code")
        if code:
            checks.append(("error code {}".format(code), payload.get("code") == code, payload.get("code")))
        for text in fixture.get("expected_message_contains", []):
            checks.append(("message contains '{}'".format(text), text.lower() in payload.get("message", "").lower(), payload.get("message")))
    tolerance = fixture.get("tolerance", 1e-9)
    for path, expected in fixture.get("expected", {}).items():
        try:
            actual = get_path(payload, path)
            ok = values_match(actual, expected, tolerance)
        except (KeyError, IndexError, ValueError):
            actual, ok = "<missing>", False
        checks.append(("{} == {}".format(path, expected), ok, actual))
    for text in fixture.get("expected_flags_contain", []):
        flags = payload.get("flags", [])
        checks.append(("flag contains '{}'".format(text), any(text.lower() in f.lower() for f in flags), flags))
    for text in fixture.get("expected_warnings_contain", []):
        warnings = payload.get("warnings", [])
        checks.append(("warning contains '{}'".format(text), any(text.lower() in w.lower() for w in warnings), warnings))
    if fixture.get("expect_reconciles") and status == "ok":
        rec = payload.get("reconciliation")
        if rec is None and isinstance(payload.get("results"), dict):
            recs = [seg.get("reconciliation") for seg in payload["results"].values() if isinstance(seg, dict) and "reconciliation" in seg]
            ok = bool(recs) and all(r["reconciles"] and abs(r["residual"]) <= r["tolerance"] for r in recs)
            checks.append(("all segment bridges reconcile within tolerance", ok, recs))
        else:
            ok = bool(rec) and rec["reconciles"] and abs(rec["residual"]) <= rec["tolerance"]
            checks.append(("bridge reconciles within declared tolerance", ok, rec))


def run_analytics(fixture, tmpdir):
    paths = {}
    for key, name in (("input_csv", "input"), ("right_csv", "right")):
        if key in fixture:
            path = os.path.join(tmpdir, "{}_{}.csv".format(fixture["id"], name))
            with open(path, "w", encoding="utf-8") as handle:
                handle.write(fixture[key])
            paths[name] = path
    args = [a.format(**paths) for a in fixture["args"]]
    returncode, payload, stderr = run_command([sys.executable, ANALYTICS, fixture["recipe"]] + args)
    checks = []
    check_process_stderr(returncode, stderr, checks)
    check_common(fixture, payload, returncode, checks)
    return checks


def run_records(fixture, tmpdir):
    paths = {"root": ROOT}
    for key in ("records", "outline"):
        if key in fixture:
            path = os.path.join(tmpdir, "{}_{}.json".format(fixture["id"], key))
            with open(path, "w", encoding="utf-8") as handle:
                json.dump(fixture[key], handle)
            paths[key] = path
    args = [a.format(**paths) for a in fixture["args"]]
    returncode, payload, stderr = run_command([sys.executable, RECORDS, fixture["command"]] + args)
    checks = []
    check_process_stderr(returncode, stderr, checks)
    check_common(fixture, payload, returncode, checks)
    error_codes = {e.get("code") for e in payload.get("errors", [])}
    warning_codes = {w.get("code") for w in payload.get("warnings", [])}
    for code in fixture.get("expected_error_codes", []):
        checks.append(("error {} reported".format(code), code in error_codes, sorted(error_codes)))
    for code in fixture.get("expected_warning_codes", []):
        checks.append(("warning {} reported".format(code), code in warning_codes, sorted(warning_codes)))
    if "expected_no_errors" in fixture:
        checks.append(("no errors", not payload.get("errors"), payload.get("errors")))
    if "expected_flagged" in fixture:
        flagged = sorted(payload.get("flagged", []))
        checks.append(("flagged == {}".format(sorted(fixture["expected_flagged"])), flagged == sorted(fixture["expected_flagged"]), flagged))
    return checks


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--verbose", action="store_true")
    parser.add_argument("--write", help="write a JSON results file (path relative to the skill root or absolute)")
    parser.add_argument("--only", help="run fixtures whose id contains this text")
    args = parser.parse_args()

    files = sorted(glob.glob(os.path.join(ROOT, "evals", "fixtures", "*", "*.json")))
    results = []
    with tempfile.TemporaryDirectory() as tmpdir:
        for path in files:
            with open(path, encoding="utf-8") as handle:
                fixture = json.load(handle)
            if args.only and args.only not in fixture["id"]:
                continue
            runner = run_analytics if fixture["kind"] == "analytics" else run_records
            try:
                checks = runner(fixture, tmpdir)
            except Exception as error:  # report, never hide
                checks = [("fixture executed", False, repr(error))]
            passed = all(ok for _, ok, _ in checks)
            results.append({
                "id": fixture["id"],
                "file": os.path.relpath(path, ROOT),
                "kind": fixture["kind"],
                "result": "PASSED" if passed else "FAILED",
                "checks": [{"check": name, "ok": ok, "actual": actual if not ok or args.verbose else None} for name, ok, actual in checks],
            })
            marker = "PASS" if passed else "FAIL"
            print("[{}] {} ({} checks)".format(marker, fixture["id"], len(checks)))
            for name, ok, actual in checks:
                if args.verbose or not ok:
                    print("    {} {}{}".format("ok  " if ok else "FAIL", name, "" if ok else "  -> actual: {}".format(json.dumps(actual)[:400])))

    passed = sum(1 for r in results if r["result"] == "PASSED")
    print("\n{} of {} fixtures passed.".format(passed, len(results)))
    if args.write:
        out = args.write if os.path.isabs(args.write) else os.path.join(ROOT, args.write)
        os.makedirs(os.path.dirname(out), exist_ok=True)
        with open(out, "w", encoding="utf-8") as handle:
            json.dump({
                "run_at": datetime.datetime.now(datetime.timezone.utc).replace(microsecond=0).isoformat(),
                "python": sys.version.split()[0],
                "passed": passed,
                "total": len(results),
                "scope_note": "Deterministic checks establish arithmetic and structural correctness only; not causality, source truth or strategic validity.",
                "results": results,
            }, handle, indent=2)
        print("Results written to {}".format(os.path.relpath(out, ROOT)))
    return 0 if passed == len(results) else 1


if __name__ == "__main__":
    sys.exit(main())
