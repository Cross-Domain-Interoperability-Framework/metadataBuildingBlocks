#!/usr/bin/env python3
"""Generate a custom validation report from bblocks-postprocess report.json.

Replaces the binary PASS/FAIL with granular labels:
- "JSON Schema Fail" if JSON Schema validation fails
- "SHACL: 2 Info, 1 Warning, 1 Violation" for SHACL issues
- "Passed" if everything passes

Usage:
    python tools/generate_custom_report.py [--input build/tests/report.json] [--output build/tests/report.html]
"""

import argparse
import html
import json
import os
import re
from collections import Counter
from datetime import datetime, timezone


def parse_shacl_severities(graph_turtle: str) -> Counter:
    """Extract SHACL severity counts from a Turtle-serialized ValidationReport."""
    return Counter(re.findall(r"sh:resultSeverity\s+sh:(\w+)", graph_turtle))


def classify_item(item: dict) -> dict:
    """Classify a test item's results into JSON Schema and SHACL components.

    Returns dict with:
      - json_schema_pass: bool
      - json_schema_error: str or None (first error message)
      - shacl_severities: Counter({'Violation': n, 'Warning': n, 'Info': n})
      - shacl_pass: bool (True if no SHACL results at all or all conform)
      - overall_pass: bool
      - require_fail: bool
    """
    require_fail = item.get("source", {}).get("requireFail", False)
    json_schema_pass = True
    json_schema_error = None
    shacl_severities = Counter()
    shacl_has_nonconforming = False

    for section in item.get("sections", []):
        if section["name"] == "JSON_SCHEMA":
            for entry in section.get("entries", []):
                if entry.get("isError"):
                    json_schema_pass = False
                    if json_schema_error is None:
                        json_schema_error = entry.get("message", "")
        elif section["name"] == "SHACL":
            for entry in section.get("entries", []):
                graph = entry.get("graph", "")
                if graph:
                    sevs = parse_shacl_severities(graph)
                    shacl_severities += sevs
                    if "sh:conforms false" in graph:
                        shacl_has_nonconforming = True

    shacl_pass = not shacl_has_nonconforming

    # For require-fail items, the OGC pipeline inverts the result
    if require_fail:
        overall_pass = item.get("result", False)
    else:
        overall_pass = json_schema_pass and shacl_pass

    return {
        "json_schema_pass": json_schema_pass,
        "json_schema_error": json_schema_error,
        "shacl_severities": shacl_severities,
        "shacl_pass": shacl_pass,
        "overall_pass": overall_pass,
        "require_fail": require_fail,
    }


def format_shacl_badge(severities: Counter) -> str:
    """Format SHACL severity counts as a human-readable string."""
    if not severities:
        return ""
    parts = []
    for sev in ("Violation", "Warning", "Info"):
        count = severities.get(sev, 0)
        if count > 0:
            parts.append(f"{count} {sev}")
    return "SHACL: " + ", ".join(parts)


def severity_badge_class(severities: Counter) -> str:
    """Return Bootstrap badge class based on highest SHACL severity."""
    if severities.get("Violation", 0) > 0:
        return "text-bg-danger"
    if severities.get("Warning", 0) > 0:
        return "text-bg-warning"
    if severities.get("Info", 0) > 0:
        return "text-bg-info"
    return "text-bg-success"


def item_badge_html(classification: dict) -> str:
    """Generate HTML badge(s) for a test item."""
    if classification["require_fail"]:
        if classification["overall_pass"]:
            return '<span class="badge text-bg-success me-1">Passed (expected fail)</span>'
        else:
            return '<span class="badge text-bg-danger me-1">Failed (expected fail did not fail)</span>'

    badges = []

    if not classification["json_schema_pass"]:
        badges.append('<span class="badge text-bg-danger me-1">JSON Schema Fail</span>')

    sevs = classification["shacl_severities"]
    if sevs:
        label = format_shacl_badge(sevs)
        css = severity_badge_class(sevs)
        badges.append(f'<span class="badge {css} me-1">{html.escape(label)}</span>')

    if not badges:
        badges.append('<span class="badge text-bg-success me-1">Passed</span>')

    return "\n".join(badges)


def bblock_summary(items: list, classifications: list) -> dict:
    """Compute building-block-level summary from classified items."""
    total = len(items)
    # For bblock-level, only count non-requireFail items for the custom status
    example_items = [c for c in classifications if not c["require_fail"]]
    require_fail_items = [c for c in classifications if c["require_fail"]]

    all_json_pass = all(c["json_schema_pass"] for c in example_items) if example_items else True
    all_shacl_pass = all(c["shacl_pass"] for c in example_items) if example_items else True
    require_fail_ok = all(c["overall_pass"] for c in require_fail_items)

    # Aggregate SHACL severities across non-requireFail items
    agg_severities = Counter()
    for c in example_items:
        agg_severities += c["shacl_severities"]

    passed_count = sum(1 for c in classifications if c["overall_pass"])
    failed_count = total - passed_count

    return {
        "total": total,
        "passed": passed_count,
        "failed": failed_count,
        "all_json_pass": all_json_pass,
        "all_shacl_pass": all_shacl_pass,
        "require_fail_ok": require_fail_ok,
        "agg_severities": agg_severities,
    }


def bblock_badge_html(summary: dict) -> str:
    """Generate the building-block-level badge."""
    badges = []

    if not summary["all_json_pass"]:
        badges.append('<span class="badge text-bg-danger me-1">JSON Schema Fail</span>')

    sevs = summary["agg_severities"]
    if sevs:
        label = format_shacl_badge(sevs)
        css = severity_badge_class(sevs)
        badges.append(f'<span class="badge {css} me-1">{html.escape(label)}</span>')

    if not summary["require_fail_ok"]:
        badges.append('<span class="badge text-bg-danger me-1">Expected-fail test issue</span>')

    if not badges:
        pct = (summary["passed"] / summary["total"] * 100) if summary["total"] else 100
        badges.append(f'<span class="badge text-bg-success me-1">Passed ({pct:.0f}% passed)</span>')

    return "\n".join(badges)


def render_entry_message(entry: dict) -> str:
    """Render a single validation entry as HTML."""
    msg = html.escape(entry.get("message", ""))
    is_error = entry.get("isError", False)
    css_class = "text-danger" if is_error else ""
    return f'<div class="font-monospace entry-message {css_class}">{msg}</div>'


def generate_report(data: dict) -> str:
    """Generate the full HTML report from report.json data."""
    summary = data.get("summary", {})
    bblocks = data.get("bblocks", {})
    generated = data.get("generated", datetime.now(timezone.utc).isoformat())

    # Classify all items
    bb_data = []
    total_pass = 0
    total_bb = 0
    for bid, bb in sorted(bblocks.items()):
        items = bb.get("items", [])
        classifications = [classify_item(item) for item in items]
        bb_summary = bblock_summary(items, classifications)

        # A bblock passes if all examples pass JSON Schema AND no SHACL violations
        # (warnings/info don't count as failures at bblock level)
        bb_passes = (
            bb_summary["all_json_pass"]
            and bb_summary["require_fail_ok"]
            and bb_summary["agg_severities"].get("Violation", 0) == 0
        )
        total_bb += 1
        if bb_passes:
            total_pass += 1

        bb_data.append({
            "id": bid,
            "title": bb.get("bblockName", bid),
            "items": items,
            "classifications": classifications,
            "summary": bb_summary,
            "passes": bb_passes,
        })

    pct = (total_pass / total_bb * 100) if total_bb else 100
    pct_class = "text-success" if total_pass == total_bb else "text-danger"

    # Build HTML
    lines = []
    lines.append("""<!doctype html>
<html>
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Building Blocks validation report</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.1/font/bootstrap-icons.css">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet"
          integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN" crossorigin="anonymous">
    <style>
        .entry-message { white-space: pre-wrap; font-size: 80%; line-height: 1.1; }
        *[data-bs-toggle] .caret { display: inline-block; transform: rotate(90deg); transition: transform 0.25s; }
        *[data-bs-toggle].collapsed .caret { transform: rotate(0deg); }
        .highlighted { animation: highlight-border 3500ms ease-out; }
        .highlighted h2 button { animation: highlight 3500ms ease-out; }
        @keyframes highlight {
            0% { background: #ffff90; }
            100% { background: var(--bs-accordion-active-bg); }
        }
        @keyframes highlight-border {
            0% { border-color: red; border-width: 2px; }
            100% { border-color: var(--bs-accordion-border-color); border-width: var(--bs-accordion-border-width); }
        }
        .anchor { color: black; opacity: 0; text-decoration: none; margin-left: 0.5em; margin-right: 0.5em; }
        .anchor-container:hover .anchor { opacity: 60%; }
        .anchor-container:hover .anchor:hover { opacity: 100%; }
    </style>
</head>
<body>
    <div class="container">
        <h1 class="title">Building blocks validation report</h1>""")
    lines.append(f'        <small class="datetime">Generated at {html.escape(generated)}</small>')
    lines.append(f'        <p class="summary fw-semibold {pct_class}">')
    lines.append(f"            Number of passing building blocks: {total_pass} / {total_bb} ({pct:.2f}%)")
    lines.append("        </p>")
    lines.append("""        <p class="small text-muted">
            Pass criteria: JSON Schema passes and no SHACL Violations.
            SHACL Warnings and Info are reported but do not cause failure.
        </p>""")
    lines.append('        <div class="text-end small" id="expand-collapse">')
    lines.append('            <a href="#" class="expand-all">Expand all</a>')
    lines.append('            <a href="#" class="collapse-all">Collapse all</a>')
    lines.append("        </div>")
    lines.append('        <div class="accordion mt-2" id="bblock-reports">')

    uid_counter = 0

    for bb in bb_data:
        bid = bb["id"]
        bid_escaped = bid.replace(".", r"\.")
        bb_badge = bblock_badge_html(bb["summary"])

        lines.append(f'            <div class="accordion-item bblock-report" data-bblock-id="{html.escape(bid)}" id="bblock-{html.escape(bid)}">')
        lines.append('                <h2 class="accordion-header bblock-title anchor-container">')
        lines.append(f'                    <button class="accordion-button collapsed" type="button"')
        lines.append(f'                        data-bs-toggle="collapse"')
        lines.append(f'                        data-bs-target="#bblock-collapse-{bid_escaped}">')
        lines.append(f'                        <div class="flex-fill">')
        lines.append(f"                            {html.escape(bb['title'])}")
        lines.append(f'                            <small class="ms-2 bblock-id">{html.escape(bid)}</small>')
        lines.append(f'                            <a class="anchor" href="#bblock-{html.escape(bid)}">¶</a>')
        lines.append(f"                        </div>")
        lines.append(f"                        {bb_badge}")
        lines.append(f"                    </button>")
        lines.append(f"                </h2>")
        lines.append(f'                <div class="accordion-collapse collapse" id="bblock-collapse-{html.escape(bid)}">')
        lines.append(f'                    <div class="accordion-body">')

        s = bb["summary"]
        s_class = "text-success" if s["passed"] == s["total"] else "text-danger"
        lines.append(f'                        <p class="summary fw-semibold {s_class}">')
        lines.append(f'                            Test passed: {s["passed"]} / {s["total"]}')
        lines.append(f"                        </p>")

        for idx, (item, classification) in enumerate(zip(bb["items"], bb["classifications"])):
            uid_counter += 1
            uid = f"uid-{uid_counter}"
            src = item.get("source", {})
            filename = src.get("filename", "")
            # Make links relative to build/tests/ where report.html lives
            link_path = filename
            if link_path.startswith("build/tests/"):
                link_path = link_path[len("build/tests/"):]
            display_name = os.path.basename(filename) if filename else f"item {idx+1}"
            src_type = src.get("type", "EXAMPLE")
            require_fail = src.get("requireFail", False)
            item_badges = item_badge_html(classification)

            item_css = "require-fail" if require_fail else ""
            lines.append(f'                        <div class="card mb-2 validation-item {item_css}" id="item-{html.escape(bid)}-{idx+1}">')
            lines.append(f'                            <div class="card-body">')
            lines.append(f'                                <div class="card-title mb-0 anchor-container">')
            lines.append(f'                                    <button type="button" class="btn btn-sm btn-primary collapsed"')
            lines.append(f'                                            data-bs-toggle="collapse" data-bs-target="#{uid}"')
            lines.append(f'                                            style="--bs-btn-padding-y: .25rem; --bs-btn-padding-x: .5rem; --bs-btn-font-size: .75rem;">')
            lines.append(f'                                        <i class="bi bi-caret-right-fill caret"></i>')
            lines.append(f"                                        Details")
            lines.append(f"                                    </button>")
            if filename:
                lines.append(f'                                    <a href="{html.escape(link_path)}" target="_blank">{html.escape(display_name)}</a>')
            lines.append(f'                                    <span class="badge bg-secondary {src_type.lower()}">{html.escape(src_type.replace("_", " ").title())}</span>')
            if require_fail:
                lines.append(f'                                    <span class="badge text-bg-info">Requires fail</span>')
            lines.append(f'                                    <a class="anchor" href="#item-{html.escape(bid)}-{idx+1}">¶</a>')
            lines.append(f'                                    <div class="float-end">')
            lines.append(f"                                        {item_badges}")
            lines.append(f"                                    </div>")
            lines.append(f"                                </div>")

            # Detail section
            lines.append(f'                                <div class="card-text mt-2 validation-text collapse" id="{uid}">')
            lines.append(f'                                    <div class="validation-text-inner">')

            for section in item.get("sections", []):
                sec_name = section.get("name", "")
                sec_title = section.get("title", sec_name)
                lines.append(f'                                        <div class="font-monospace subsection-title mt-2">{html.escape(sec_title)}</div>')
                for entry in section.get("entries", []):
                    lines.append(f"                                        {render_entry_message(entry)}")

            lines.append(f"                                    </div>")
            lines.append(f"                                </div>")
            lines.append(f"                            </div>")
            lines.append(f"                        </div>")

        lines.append(f"                    </div>")
        lines.append(f"                </div>")
        lines.append(f"            </div>")

    lines.append("        </div>")
    lines.append("    </div>")

    # JavaScript for expand/collapse and anchor navigation
    lines.append("""
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js"
            integrity="sha384-C6RzsynM9kWDrMNeT87bh95OGNyZPhcTNXj1NW7RuBCsyN/o0jlpcV8Qyq46cDfL"
            crossorigin="anonymous"></script>
    <script>
        document.querySelector('.expand-all')?.addEventListener('click', e => {
            e.preventDefault();
            document.querySelectorAll('.accordion-collapse').forEach(el => {
                new bootstrap.Collapse(el, {toggle: false}).show();
            });
        });
        document.querySelector('.collapse-all')?.addEventListener('click', e => {
            e.preventDefault();
            document.querySelectorAll('.accordion-collapse').forEach(el => {
                new bootstrap.Collapse(el, {toggle: false}).hide();
            });
        });
        if (location.hash) {
            const target = document.querySelector(location.hash);
            if (target) {
                const accordion = target.querySelector('.accordion-collapse') || target.closest('.accordion-collapse');
                if (accordion) new bootstrap.Collapse(accordion, {toggle: false}).show();
                target.classList.add('highlighted');
                target.scrollIntoView({behavior: 'smooth'});
            }
        }
        document.querySelectorAll('.anchor').forEach(a => {
            a.addEventListener('click', e => {
                e.preventDefault();
                navigator.clipboard?.writeText(a.href);
                history.replaceState(null, '', a.getAttribute('href'));
            });
        });
    </script>
</body>
</html>""")

    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="Generate custom validation report from report.json")
    parser.add_argument("--input", "-i", default="build/tests/report.json",
                        help="Path to report.json (default: build/tests/report.json)")
    parser.add_argument("--output", "-o", default="build/tests/report.html",
                        help="Path to output report.html (default: build/tests/report.html)")
    args = parser.parse_args()

    with open(args.input, encoding="utf-8") as f:
        data = json.load(f)

    report_html = generate_report(data)

    os.makedirs(os.path.dirname(args.output) or ".", exist_ok=True)
    with open(args.output, "w", encoding="utf-8") as f:
        f.write(report_html)

    print(f"Custom report written to {args.output}")


if __name__ == "__main__":
    main()
