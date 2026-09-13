"""Prove the viewer's SHACL block is honest.

The cases that matter are the ones where an implementation shows a clean result
it did not earn: a remote @context that could not be fetched, a host the SSRF
guard refused, a record declaring no profile at all. Each of those yields an
unexpanded or unchecked graph, zero violations, and a page that looks exactly
like a valid record unless the code says otherwise.

Also pins severity handling: pyshacl's text summary labels every result
"Constraint Violation" whatever its severity, so severity must be read from the
report graph. A sh:Warning rendered as a failure would make the advisory
conformance rules unusable.

    python tools/test_viewer_validation.py     # exits 1 on any failure
"""
import importlib.util
import json
import pathlib
import sys

spec = importlib.util.spec_from_file_location("R", "tools/cdif_record_to_html.py")
R = importlib.util.module_from_spec(spec)
spec.loader.exec_module(R)

modules = R.load_modules([pathlib.Path("_sources/profiles/cdifProfile"),
                          pathlib.Path("_sources/xasProperties")])
base = json.loads(pathlib.Path(
    "_sources/profiles/cdifProfile/cdifCore/exampleCdifCore.json"
).read_text(encoding="utf-8"))


def selected_for(record):
    return [modules[u] for u in R.declared_conformance(record) if u in modules]


def run(label, record, allow_fetch, expect):
    findings, reason = R.shacl_findings(record, selected_for(record),
                                        allow_fetch=allow_fetch)
    html = R.render_validation(findings, reason)
    if expect == "skipped":
        ok = reason is not None and "Not validated" in html
        got = "skipped: %s" % (reason or "")[:70]
    elif expect == "violation":
        ok = reason is None and any(f.severity == "Violation" for f in findings)
        got = "reason=%r severities=%s" % (reason, sorted({f.severity for f in findings}))
    elif expect == "clean":
        ok = reason is None and not findings
        got = "reason=%r findings=%d" % (reason, len(findings))
    else:
        ok, got = False, "unknown expectation"
    # A skipped check must never be styled as the clean one.
    if expect == "skipped" and "validation clean" in html:
        ok, got = False, "styled as CLEAN while skipped"
    print("  %-6s %-52s %s" % ("PASS" if ok else "**FAIL**", label, got))
    return ok


results = []

# 1. A record whose @context is remote, with fetching off. rdflib would happily
#    fetch it; the point is that we do not, and do not pretend to have checked.
remote = json.loads(json.dumps(base))
remote["@context"] = "https://example.org/context.jsonld"
results.append(run("remote @context, fetching off -> not validated",
                   remote, False, "skipped"))

# 2. Same, fetching on, but the host is private. The SSRF guard must refuse it
#    and the result must still be "not validated", not "clean".
private = json.loads(json.dumps(base))
private["@context"] = "http://127.0.0.1:9/context.jsonld"
results.append(run("private-host @context, fetching on -> refused",
                   private, True, "skipped"))

# 3. A record that breaks a hard rule must report a Violation.
#    Keep conformsTo intact -- removing it leaves no profile to validate
#    against, which is a different (also correct) outcome.
broken = json.loads(json.dumps(base))
broken.pop("schema:name", None)
results.append(run("required property removed -> Violation", broken, False,
                   "violation"))

# 4. A record declaring nothing recognised is not silently "clean".
unknown = json.loads(json.dumps(base))
unknown["schema:subjectOf"] = {"@type": ["schema:Dataset"]}
findings, reason = R.shacl_findings(unknown, selected_for(unknown), allow_fetch=False)
ok = reason is not None
print("  %-6s %-52s %s" % ("PASS" if ok else "**FAIL**",
                           "no recognised profile -> not validated",
                           "reason=%s" % (reason or "")[:50]))
results.append(ok)

# 5. Severity must come from the report graph, not the text summary: pyshacl
#    labels every result "Constraint Violation" regardless of severity.
findings, reason = R.shacl_findings(base, selected_for(base), allow_fetch=False)
ok = reason is None and findings and all(f.severity in ("Violation", "Warning", "Info")
                                         for f in findings)
sevs = sorted({f.severity for f in findings})
print("  %-6s %-52s %s" % ("PASS" if ok else "**FAIL**",
                           "severities read from the report graph", sevs))
results.append(ok)

print("\n  %d/%d passed" % (sum(results), len(results)))
sys.exit(0 if all(results) else 1)
