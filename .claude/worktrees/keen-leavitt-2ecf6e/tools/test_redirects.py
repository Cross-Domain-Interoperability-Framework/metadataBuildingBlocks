#!/usr/bin/env python3
"""Test w3id.org/cdif redirect rules by parsing .htaccess and curling each URL.

Parses the .htaccess file to extract:
  - Environment variables (base URLs)
  - RewriteCond/RewriteRule pairs

Then constructs concrete test URLs and can:
  1. Show expected redirects (dry-run, default)
  2. Retrieve expected redirect targets to verify they exist (--follow)
  3. Test live w3id.org redirects (--live)
  4. Test live redirects AND follow them (--live --follow)

Usage:
    python tools/test_redirects.py path/to/.htaccess                # dry-run
    python tools/test_redirects.py path/to/.htaccess --follow       # verify targets exist
    python tools/test_redirects.py path/to/.htaccess --live         # test w3id.org redirects
    python tools/test_redirects.py path/to/.htaccess --live --follow  # test + verify targets
"""

import argparse
import re
import subprocess
import sys
from dataclasses import dataclass, field
from pathlib import Path


W3ID_BASE = "https://w3id.org/cdif"

# Sample values for capture groups in regex patterns.
# Each key is a category/family name that appears in .htaccess patterns.
SAMPLE_CAPTURE_VALUES = {
    # Two-segment BB: bbr/metadata/{category}/{name}
    "cdifProperties": ["cdifOptional", "cdifCore"],
    "xasProperties": ["xasRequired", "xasOptional"],
    "schemaorgProperties": ["definedTerm"],
    # Three-segment profiles: bbr/metadata/profiles/{family}/{name}
    "cdifProfiles": ["CDIFDiscoveryProfile", "CDIFcompleteProfile"],
    # Domain-specific (matched by dedicated rules, not generic patterns)
    "adaProfiles": ["adaICPMS"],
    "DDEProfiles": ["DDEDiscovery"],
    "ecrrProfiles": ["ECRRDataset"],
    "adaProperties": ["collection"],
    "DDEproperties": ["ddeOptional"],
    "ecrrProperties": ["ecrrBase"],
}

# Accept header values to display names
ACCEPT_LABELS = {
    "application/schema+json": "schema+json",
    "application/yaml": "yaml",
    "text/turtle": "turtle",
    "application/ld+json": "ld+json",
    "application/json": "json",
    "text/html": "html",
}


@dataclass
class EnvVars:
    """Environment variables parsed from SetEnvIf directives."""
    vars: dict = field(default_factory=dict)

    def substitute(self, s: str) -> str:
        """Replace %{ENV:VAR} with the actual value."""
        def replacer(m):
            name = m.group(1)
            return self.vars.get(name, m.group(0))
        return re.sub(r'%\{ENV:(\w+)\}', replacer, s)


@dataclass
class RewriteRule:
    """A single RewriteCond/RewriteRule pair."""
    pattern: str           # regex pattern from RewriteRule
    target: str            # target URL template (with env refs)
    accept_cond: str = ""  # Accept header condition (empty = no condition)
    line_num: int = 0


def parse_htaccess(path: Path) -> tuple[EnvVars, list[RewriteRule]]:
    """Parse .htaccess and return env vars and rewrite rules."""
    env = EnvVars()
    rules = []

    lines = path.read_text(encoding="utf-8").splitlines()
    pending_conds = []

    for i, line in enumerate(lines, 1):
        stripped = line.strip()

        # Skip comments and blanks
        if not stripped or stripped.startswith("#"):
            pending_conds = []
            continue

        # SetEnvIf Request_URI ^.*$ VAR=value
        m = re.match(r'SetEnvIf\s+Request_URI\s+\S+\s+(\w+)=(.*)', stripped)
        if m:
            env.vars[m.group(1)] = m.group(2)
            continue

        # RewriteCond
        m = re.match(r'RewriteCond\s+%\{HTTP_ACCEPT\}\s+(.*?)(?:\s+\[(.*)\])?$', stripped)
        if m:
            cond_pattern = m.group(1)
            # Unescape Apache regex escapes for display
            cond_pattern = cond_pattern.replace("\\+", "+").replace("\\*", "*")
            flags = m.group(2) or ""
            pending_conds.append((cond_pattern, flags))
            continue

        # Other RewriteCond (user-agent, etc.) — track but don't extract accept
        if stripped.startswith("RewriteCond"):
            pending_conds.append(("", ""))
            continue

        # RewriteRule
        m = re.match(r'RewriteRule\s+(\S+)\s+(\S+)\s+\[([^\]]*)\]', stripped)
        if m:
            pattern = m.group(1)
            target = m.group(2)
            flags = m.group(3)

            if "R=" not in flags and "R," not in flags:
                pending_conds = []
                continue

            # Determine accept condition from pending conds
            accept = ""
            if pending_conds:
                # Take the first non-empty accept condition
                for cond_pat, cond_flags in pending_conds:
                    if cond_pat and "HTTP_ACCEPT" not in cond_pat:
                        # This was from a non-accept RewriteCond line we captured
                        pass
                    if cond_pat:
                        accept = cond_pat
                        break

            rules.append(RewriteRule(
                pattern=pattern,
                target=target,
                accept_cond=accept,
                line_num=i,
            ))
            pending_conds = []
            continue

        # Non-matching lines reset pending conds
        if not stripped.startswith("Rewrite"):
            pending_conds = []

    return env, rules


def instantiate_pattern(pattern: str) -> list[str]:
    """Convert a regex pattern into concrete URL paths.

    For literal patterns (no capture groups), returns the path as-is.
    For patterns with ([^/]+) capture groups, substitutes sample values.
    """
    # Unescape Apache regex (e.g., \. -> .)
    clean = pattern.replace(r"\.",".")

    # Remove anchors
    clean = clean.lstrip("^").rstrip("$")

    # Remove optional trailing slash
    clean = re.sub(r'\?$', '', clean)
    clean = clean.rstrip("/")

    # Check for capture groups
    groups = re.findall(r'\([^)]+\)', clean)
    if not groups:
        return [clean]

    # Try to fill capture groups with sample values
    results = []
    if len(groups) == 1:
        # Single capture group — find matching samples from the path prefix
        prefix = clean.split("(")[0].rstrip("/")
        for category, names in SAMPLE_CAPTURE_VALUES.items():
            if category in prefix:
                for name in names:
                    path = re.sub(r'\([^)]+\)', name, clean, count=1)
                    results.append(path)
                break
        if not results:
            # Fallback: use first available sample
            path = re.sub(r'\([^)]+\)', "testItem", clean, count=1)
            results.append(path)
    elif len(groups) == 2:
        # Two capture groups — e.g., profiles/{family}/{name} or {category}/{name}
        prefix = clean.split("(")[0].rstrip("/")
        # For generic two-segment rules (bbr/metadata/cat/name), pick a few combos
        if "profiles" in prefix:
            for family, names in SAMPLE_CAPTURE_VALUES.items():
                if "Profiles" in family or "profiles" in family.lower():
                    if family in ("adaProfiles", "DDEProfiles", "ecrrProfiles"):
                        continue  # these have dedicated rules
                    for name in names:
                        path = clean
                        path = re.sub(r'\([^)]+\)', family, path, count=1)
                        path = re.sub(r'\([^)]+\)', name, path, count=1)
                        results.append(path)
        else:
            # Generic two-segment: use cdifProperties and xasProperties samples
            for cat in ("cdifProperties", "xasProperties"):
                for name in SAMPLE_CAPTURE_VALUES.get(cat, [])[:1]:
                    path = clean
                    path = re.sub(r'\([^)]+\)', cat, path, count=1)
                    path = re.sub(r'\([^)]+\)', name, path, count=1)
                    results.append(path)

    return results if results else [clean]


def accept_to_header(accept_cond: str) -> str:
    """Convert an Apache accept condition pattern to an Accept header value."""
    # Remove regex escapes
    clean = accept_cond.replace("\\+", "+").replace("\\*", "*")
    return clean


@dataclass
class TestCase:
    """A single test to run."""
    url: str
    accept: str       # Accept header value ("" = no header / browser default)
    expected: str      # expected redirect target
    category: str      # descriptive category
    htaccess_line: int


def build_test_cases(env: EnvVars, rules: list[RewriteRule]) -> list[TestCase]:
    """Build concrete test cases from parsed rules."""
    cases = []
    seen = set()

    for rule in rules:
        paths = instantiate_pattern(rule.pattern)
        target_template = env.substitute(rule.target)

        for path in paths:
            url = f"{W3ID_BASE}/{path}"
            accept = accept_to_header(rule.accept_cond)

            # Resolve capture group backreferences ($1, $2) in target
            # by re-matching the original pattern against the concrete path
            try:
                m = re.match(rule.pattern, path)
                if m:
                    expected = target_template
                    for i, g in enumerate(m.groups(), 1):
                        expected = expected.replace(f"${i}", g)
                else:
                    expected = target_template
            except re.error:
                expected = target_template

            # Categorize
            if path.startswith("bbr/metadata/profiles/"):
                cat = "Profile BB"
            elif path.startswith("bbr/metadata/"):
                if "/schema" in path or "/resolved" in path or "/shacl" in path or "/context" in path:
                    cat = "BB sub-path"
                else:
                    cat = "BB conneg"
            elif re.match(r'\w+/1\.\d/', path) or re.match(r'\w+/1\.\d$', path):
                if "/schema" in path or "/resolved" in path or "/shacl" in path or "/context" in path:
                    cat = "Conformance sub-path"
                else:
                    cat = "Conformance conneg"
            elif path == "" or path == "/":
                cat = "Base redirect"
            else:
                cat = "Other"

            key = (url, accept)
            if key not in seen:
                seen.add(key)
                cases.append(TestCase(
                    url=url,
                    accept=accept,
                    expected=expected,
                    category=cat,
                    htaccess_line=rule.line_num,
                ))

    return cases


def test_redirect(url: str, accept: str) -> tuple[int, str]:
    """Send a request to w3id.org and return (status_code, location_header).

    Does NOT follow redirects — just captures the initial 303/302 response.
    """
    cmd = [
        "curl", "-sI",
        "-o", "/dev/null",
        "-w", "%{http_code} %{redirect_url}",
        "--max-time", "10",
    ]
    if accept:
        cmd.extend(["-H", f"Accept: {accept}"])
    cmd.append(url)

    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=15)
        parts = result.stdout.strip().split(" ", 1)
        code = int(parts[0]) if parts[0].isdigit() else 0
        location = parts[1] if len(parts) > 1 else ""
        return code, location
    except (subprocess.TimeoutExpired, Exception) as e:
        return 0, f"ERROR: {e}"


def follow_url(url: str) -> tuple[int, str]:
    """Follow a redirect target URL and return (final_status_code, content_type).

    Follows all redirects (GitHub Pages may issue its own redirects) and
    returns the final HTTP status code and Content-Type header.
    """
    cmd = [
        "curl", "-s",
        "-o", "/dev/null",
        "-L",                    # follow redirects
        "-w", "%{http_code} %{content_type}",
        "--max-time", "15",
    ]
    cmd.append(url)

    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=20)
        parts = result.stdout.strip().split(" ", 1)
        code = int(parts[0]) if parts[0].isdigit() else 0
        content_type = parts[1].strip() if len(parts) > 1 else ""
        return code, content_type
    except (subprocess.TimeoutExpired, Exception) as e:
        return 0, f"ERROR: {e}"


def is_bblock_viewer_url(url: str) -> bool:
    """Return True if URL is a bblocks-viewer SPA route.

    These return 404 to curl but work in browsers because GitHub Pages
    serves 404.html (a copy of index.html) which contains the SPA
    JavaScript that handles client-side routing.
    """
    return "/bblock/" in url


def format_accept(accept: str) -> str:
    """Short display label for an Accept header."""
    if not accept:
        return "(default)"
    return ACCEPT_LABELS.get(accept, accept)


def run_tests(cases: list[TestCase], live: bool, follow: bool, outfile) -> None:
    """Run all test cases and write results."""
    def out(s=""):
        print(s, file=outfile)
        if outfile != sys.stdout:
            print(s)

    out("CDIF w3id.org Redirect Test Results")
    out("=" * 70)
    if not live and not follow:
        out("MODE: dry-run (showing expected redirects only)")
        out("  Use --follow to verify redirect targets exist on GitHub Pages")
        out("  Use --live to test redirects against w3id.org")
        out("  Use --live --follow to do both")
    elif follow and not live:
        out("MODE: follow (verifying expected redirect targets exist)")
    elif live and follow:
        out("MODE: live + follow (testing w3id.org redirects and verifying targets)")
    else:
        out("MODE: live (testing w3id.org redirects only)")
    out(f"Total test cases: {len(cases)}")
    out()

    current_cat = ""
    pass_count = 0
    fail_count = 0
    skip_count = 0
    follow_ok = 0
    follow_fail = 0

    for idx, case in enumerate(cases, 1):
        if case.category != current_cat:
            current_cat = case.category
            out(f"\n--- {current_cat} ---")

        accept_label = format_accept(case.accept)
        short_url = case.url.replace(W3ID_BASE, "w3id:cdif")

        if not live and not follow:
            # Dry-run: just show expected
            skip_count += 1
            out(f"  [----] {short_url}")
            out(f"           Accept: {accept_label}")
            out(f"           Expect: {case.expected}")
            out(f"           (.htaccess line {case.htaccess_line})")
            continue

        if live:
            # Live: test the redirect against w3id.org
            if idx % 10 == 0:
                print(f"  Testing {idx}/{len(cases)}...", file=sys.stderr)

            redir_code, location = test_redirect(case.url, case.accept)

            # Determine redirect pass/fail
            if redir_code in (302, 303) and location == case.expected:
                redir_status = "PASS"
                pass_count += 1
            elif redir_code in (302, 303):
                redir_status = "REDIR-MISMATCH"
                fail_count += 1
            elif redir_code == 0:
                redir_status = "ERR"
                fail_count += 1
            else:
                redir_status = f"{redir_code}"
                fail_count += 1

            out(f"  [{redir_status:>5}] {short_url}")
            out(f"           Accept:   {accept_label}")
            out(f"           Redirect: {redir_code} -> {location}")
            if location != case.expected:
                out(f"           Expected: {case.expected}")

            # Follow the actual redirect target
            if follow and location and redir_code in (302, 303):
                final_code, content_type = follow_url(location)

                if final_code == 200:
                    follow_label = "OK"
                    follow_ok += 1
                elif final_code == 404 and is_bblock_viewer_url(location):
                    follow_label = "OK (SPA viewer — 404 expected via curl, works in browser)"
                    follow_ok += 1
                elif final_code == 404:
                    follow_label = "NOT FOUND"
                    follow_fail += 1
                elif final_code == 0:
                    follow_label = "ERR"
                    follow_fail += 1
                else:
                    follow_label = str(final_code)
                    if final_code >= 400:
                        follow_fail += 1
                    else:
                        follow_ok += 1

                out(f"           Target:   {final_code} {follow_label}  Content-Type: {content_type}")

        elif follow:
            # Follow-only (no --live): retrieve the expected target URL directly
            if idx % 10 == 0:
                print(f"  Checking target {idx}/{len(cases)}...", file=sys.stderr)

            final_code, content_type = follow_url(case.expected)

            if final_code == 200:
                follow_label = "OK"
                follow_ok += 1
            elif final_code == 404 and is_bblock_viewer_url(case.expected):
                follow_label = "OK (SPA viewer — 404 expected via curl, works in browser)"
                follow_ok += 1
            elif final_code == 404:
                follow_label = "NOT FOUND"
                follow_fail += 1
            elif final_code == 0:
                follow_label = "ERR"
                follow_fail += 1
            else:
                follow_label = str(final_code)
                if final_code >= 400:
                    follow_fail += 1
                else:
                    follow_ok += 1

            status_icon = " OK " if final_code == 200 else f"{final_code:>4}"
            if final_code == 404 and is_bblock_viewer_url(case.expected):
                status_icon = " SPA"
            out(f"  [{status_icon}] {short_url}")
            out(f"           Accept:   {accept_label}")
            out(f"           Target:   {case.expected}")
            out(f"           Response: {final_code} {follow_label}  Content-Type: {content_type}")

    # Summary
    out(f"\n{'=' * 70}")
    if not live and not follow:
        out(f"Dry run: {skip_count} test cases generated")
        out("Run with --follow to verify redirect targets exist on GitHub Pages")
        out("Run with --live to test redirects against w3id.org")
    elif follow and not live:
        follow_total = follow_ok + follow_fail
        out(f"Target verification: {follow_ok}/{follow_total} reachable, {follow_fail} not found/error")
    elif live and not follow:
        total = pass_count + fail_count
        out(f"Redirect results: {pass_count}/{total} passed, {fail_count} failed")
    else:
        total = pass_count + fail_count
        out(f"Redirect results: {pass_count}/{total} passed, {fail_count} failed")
        follow_total = follow_ok + follow_fail
        out(f"Target results:   {follow_ok}/{follow_total} reachable, {follow_fail} not found/error")


def main():
    parser = argparse.ArgumentParser(
        description="Test w3id.org/cdif redirect rules from .htaccess",
    )
    parser.add_argument(
        "htaccess",
        type=Path,
        help="Path to the .htaccess file to parse",
    )
    parser.add_argument(
        "-o", "--output",
        type=str,
        default="redirectTest.txt",
        help="Output file for results (default: redirectTest.txt)",
    )
    parser.add_argument(
        "--live",
        action="store_true",
        help="Test redirects against live w3id.org",
    )
    parser.add_argument(
        "--follow",
        action="store_true",
        help="Retrieve expected redirect targets and report their HTTP status and "
             "Content-Type. Without --live, tests targets computed locally from "
             ".htaccess (pre-push validation). With --live, follows actual "
             "w3id.org redirects.",
    )
    parser.add_argument(
        "--stdout",
        action="store_true",
        help="Print to stdout only, don't write file",
    )
    args = parser.parse_args()

    if not args.htaccess.exists():
        print(f"ERROR: .htaccess not found: {args.htaccess}", file=sys.stderr)
        sys.exit(1)

    print(f"Parsing {args.htaccess}...", file=sys.stderr)
    env, rules = parse_htaccess(args.htaccess)

    print(f"Found {len(env.vars)} env vars, {len(rules)} rewrite rules", file=sys.stderr)
    for name, val in env.vars.items():
        print(f"  {name} = {val}", file=sys.stderr)

    cases = build_test_cases(env, rules)
    print(f"Generated {len(cases)} test cases", file=sys.stderr)

    if args.live:
        print("Testing against live w3id.org...", file=sys.stderr)
        if args.follow:
            print("Will also follow redirect targets.", file=sys.stderr)

    if args.stdout:
        run_tests(cases, args.live, args.follow, sys.stdout)
    else:
        with open(args.output, "w", encoding="utf-8") as f:
            run_tests(cases, args.live, args.follow, f)
        print(f"\nResults written to {args.output}", file=sys.stderr)


if __name__ == "__main__":
    main()
