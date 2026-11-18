#!/usr/bin/env python3
"""Audit each building block's description.md against its CURRENT schema.

VERSION: 1.0

A description.md is prose, not a generated artifact, so nothing has ever checked it against the
schema it describes. The failure it hides is the one that cost time on cdifValueDomain
(2026-11-18): its Notes section said "This BB does not yet expose a description pointer; add
cdif:isDescribedBy if/when needed" while the schema had carried cdi:isDescribedBy since October,
and its property table omitted that property entirely. A reader following the doc would have
concluded the capability was absent.

WHAT A FINDING MEANS. As with audit_ig_consistency.py: a mismatch says the prose and the schema
disagree, NOT which of them is wrong. A `table-omission` can mean the doc is behind OR that the
schema grew a property nobody wanted. Triage each one; do not sweep.

CHECKS
  unknown-in-block   a `prefix:name` token in the prose appears nowhere in this block's own files
                     (schema.yaml, resolvedSchema.json, rules.shacl, context.jsonld) but does
                     exist elsewhere in _sources -- usually a property described in the wrong
                     block, or one that moved.
  unknown-in-repo    the token appears nowhere in _sources at all -- a typo, or a term that was
                     renamed or retired out from under the prose.
  table-omission     the block's description.md HAS a property table, and a root-level schema
                     property is missing from it. Only raised for table-bearing files: a prose
                     description claims no completeness, so silence there is not a defect.
  table-phantom      the table lists a property the schema does not define at root level.
  dead-link          a relative markdown link resolves to nothing on disk. Checked
                     CASE-SENSITIVELY -- Path.exists() lies on Windows, and a link whose case is
                     wrong resolves locally and 404s on the published Pages site.
  archived-target    a link resolves, or a block name is mentioned, that now lives under archive/
                     while the prose presents it as current.
  stale-absence      a sentence asserting something is absent ("does not yet", "not supported",
                     "if/when needed") names a token the schema DOES define.

Usage:
    python tools/audit_bb_descriptions.py                  # table to stdout
    python tools/audit_bb_descriptions.py -o findings.json # machine-readable
    python tools/audit_bb_descriptions.py -b cdifValueDomain
    python tools/audit_bb_descriptions.py --check dead-link
    python tools/audit_bb_descriptions.py --self-test      # prove every check still fires
    python tools/audit_bb_descriptions.py --strict          # exit 1 if any finding
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
from pathlib import Path

TOOLS_DIR = Path(__file__).resolve().parent
REPO_ROOT = TOOLS_DIR.parent
SOURCES = REPO_ROOT / "_sources"
ARCHIVE = REPO_ROOT / "archive"

# Files that make up a block's own declared vocabulary.
BLOCK_FILES = ("schema.yaml", "resolvedSchema.json", "rules.shacl", "context.jsonld")

# A CURIE-shaped token: prefix:localName. Deliberately permissive on the local part so that
# nxs:base_classes/NXsource.html and cdif:has_PrimaryKey both match.
TOKEN_RE = re.compile(r"\b([A-Za-z][A-Za-z0-9]{1,15}):([A-Za-z_][A-Za-z0-9_./-]*)")
BACKTICKED_RE = re.compile(r"`([^`\n]{1,120})`")

# Prefixes that are URI schemes or prose, never CDIF vocabulary.
NON_VOCAB_PREFIXES = {
    "http", "https", "ftp", "urn", "mailto", "doi", "file", "git", "ssh",
    "e", "i", "eg", "ie", "cf", "see", "note", "NOTE", "TODO", "python", "bash",
}

# Phrases that assert absence. Matched per sentence.
ABSENCE_RE = re.compile(
    r"(does not yet|do not yet|not yet (?:expose|support|implement|available|wired|done)"
    r"|if/when needed|if and when needed|is not supported|are not supported"
    r"|does not expose|do not expose|no longer exists|has no |have no |is absent)",
    re.I,
)

# Wording that already tells the reader a term or block is no longer current. Requiring the
# literal word "archive" was too strict: webAPI's description says "Absorbed the former
# cdifDataType/cdifReference block on 2026-09-23", which says it plainly enough.
RETIREMENT_RE = re.compile(
    r"(archiv|former|absorb|retir|supersed|merged into|no longer|used to|previously|"
    r"prior to|was a|renamed)",
    re.I,
)

MD_LINK_RE = re.compile(r"\[[^\]]*\]\(([^)\s]+)\)")

# Set by main() / self_test(). table-omission is advisory; see audit_block for why.
INCLUDE_OMISSIONS = False

CHECK_NAMES = (
    "unknown-in-block",
    "unknown-in-repo",
    "table-omission",
    "table-phantom",
    "dead-link",
    "archived-target",
    "stale-absence",
)


# ---------------------------------------------------------------------------
# helpers
# ---------------------------------------------------------------------------

def read_text(path: Path) -> str:
    """UTF-8 always. A bare open() takes the platform default, which is cp1252 on Windows and
    raises UnicodeDecodeError on bytes two niaidDataset examples actually carry -- the trap
    recorded in CLAUDE.md, where the failure counted as an *error* and slipped past '0 failed'."""
    try:
        return path.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError):
        return ""


def tokens_in(text: str) -> set[str]:
    out = set()
    for m in TOKEN_RE.finditer(text):
        prefix, local = m.group(1), m.group(2)
        if prefix in NON_VOCAB_PREFIXES:
            continue
        out.add(f"{prefix}:{local}")
    return out


def backticked_tokens(text: str) -> dict[str, int]:
    """CURIE tokens appearing inside backticks, mapped to the 1-based line they first appear on.

    Only backticked tokens are considered. Prose that merely says the word 'identifier' is not a
    claim about a property; `schema:identifier` is.
    """
    out: dict[str, int] = {}
    for lineno, line in enumerate(text.splitlines(), start=1):
        for span in BACKTICKED_RE.findall(line):
            for tok in tokens_in(span):
                out.setdefault(tok, lineno)
    return out


def exists_case_sensitive(path: Path) -> bool:
    """True only if every path component matches the on-disk spelling exactly.

    Windows resolves a mis-cased path happily; Linux Pages serving does not. CLAUDE.md records
    the generator overwriting a differently-cased tracked file while reporting 'unchanged'.
    Walks to the filesystem anchor rather than a passed-in root, so it works on a scratch copy
    outside the repo (which is what the self-test audits).
    """
    try:
        node = path.resolve()
    except OSError:
        return False
    if not os.path.exists(node):
        return False
    for _ in range(64):
        parent = node.parent
        if parent == node:
            return True
        try:
            if node.name not in os.listdir(parent):
                return False
        except OSError:
            return False
        node = parent
    return True


APPLICATORS = ("allOf", "anyOf", "oneOf", "if", "then", "else", "items", "contains",
               "prefixItems", "additionalItems")


def deref(node, root, seen=None):
    """Follow an internal `#/$defs/...` $ref. External refs are left alone.

    resolve_schema.py resolves EXTERNAL refs into $defs and leaves the internal ones, so a
    schema here is full of {"$ref": "#/$defs/Identifier"} with no `type` and no `properties`.
    A walker that does not deref them reads this block's root as EMPTY -- cdifValueDomain's root
    is a bare oneOf of two $defs -- and then reports every table row as a phantom. That is the
    mistake generate_property_tree2.py made (CLAUDE.md), surfacing as plausible wrong counts.
    """
    seen = seen or set()
    for _ in range(16):
        if not isinstance(node, dict):
            return node
        ref = node.get("$ref")
        if not isinstance(ref, str) or not ref.startswith("#/"):
            return node
        if ref in seen:
            return {}
        seen.add(ref)
        target = root
        for part in ref.lstrip("#/").split("/"):
            if not isinstance(target, dict) or part not in target:
                return {}
            target = target[part]
        node = target
    return node


def collect_root_properties(schema, root=None, depth: int = 0, budget: int = 12) -> set[str]:
    """Property names reachable at the ROOT level of a schema, applicators and internal $refs
    included.

    A profile can declare properties outside `properties` -- cdifDataStructure declares only
    ['@context'] there and puts every structure term under its root if/then/else. A walker that
    reads `schema['properties']` alone loses the whole slice without a trace (CLAUDE.md). The
    dataset-level properties sit five applicators down, hence a budget well above the obvious 6.
    """
    root = schema if root is None else root
    out: set[str] = set()
    if depth > budget or not isinstance(schema, (dict, list)):
        return out
    if isinstance(schema, list):
        for item in schema:
            out |= collect_root_properties(item, root, depth + 1, budget)
        return out
    schema = deref(schema, root)
    if not isinstance(schema, dict):
        return out
    props = schema.get("properties")
    if isinstance(props, dict):
        out |= {k for k in props if not k.startswith("$")}
    for key in APPLICATORS:
        if key in schema:
            out |= collect_root_properties(schema[key], root, depth + 1, budget)
    return out


def all_property_names(node, depth: int = 0) -> set[str]:
    """Every property key anywhere in the document, $defs included. No $ref needed: this walks
    the raw tree, so a property defined only inside a $defs still counts as 'this block
    defines it'. Used to tell a table row describing a sub-object from a genuine phantom.
    """
    out: set[str] = set()
    if depth > 24:
        return out
    if isinstance(node, list):
        for item in node:
            out |= all_property_names(item, depth + 1)
        return out
    if not isinstance(node, dict):
        return out
    for key, value in node.items():
        if key == "properties" and isinstance(value, dict):
            out |= {k for k in value if not k.startswith("$")}
        out |= all_property_names(value, depth + 1)
    return out


PROPERTY_HEADERS = ("property", "properties", "property name", "field", "key")


def table_properties(text: str) -> dict[str, int]:
    """First-column tokens of the rows belonging to a PROPERTY table only.

    Scanning the first column of every table in the file was wrong: cdifBioschemasProperties
    leads with a `| Class | Description | ... |` table, so its five class names were reported
    as properties the schema fails to define. A table's rows only make property claims when
    that table's own first column is the property column, so the scan now starts at such a
    header and stops when the table ends.
    """
    out: dict[str, int] = {}
    in_table = False
    for lineno, line in enumerate(text.splitlines(), start=1):
        s = line.strip()
        if not s.startswith("|"):
            in_table = False
            continue
        if set(s) <= set("|- :"):
            continue  # the header underline
        cells = [c.strip() for c in s.strip("|").split("|")]
        if not cells:
            continue
        if cells[0].strip().lower() in PROPERTY_HEADERS:
            in_table = True
            continue
        if not in_table:
            continue
        for span in BACKTICKED_RE.findall(cells[0]):
            span = span.strip()
            if span.startswith("@"):
                out.setdefault(span, lineno)
            else:
                for tok in tokens_in(span):
                    out.setdefault(tok, lineno)
    return out


def has_property_table(text: str) -> bool:
    """A table whose FIRST column is the property column.

    Matching any header that merely contains 'propert' was far too loose, and the false
    positives all looked like real findings: niaidDataset's prefix table has a 'Used for'
    column and a 'NIAID properties' column, so 13 rows of its *prefix* and *block* tables were
    reported as omitted properties, and cdifBioschemasProperties' `| Class | ... |` table had
    its five class names reported as phantom properties. A table only claims to enumerate a
    block's properties when that is what its first column holds.
    """
    lines = text.splitlines()
    for i, line in enumerate(lines):
        s = line.strip()
        if not s.startswith("|") or i + 1 >= len(lines):
            continue
        if not set(lines[i + 1].strip()) <= set("|- :"):
            continue
        first = s.strip("|").split("|")[0].strip().lower()
        if first in ("property", "properties", "property name", "field", "key"):
            return True
    return False


def paragraph_at(text: str, lineno: int) -> str:
    """The blank-line-delimited paragraph containing a 1-based line number."""
    lines = text.splitlines()
    if not (1 <= lineno <= len(lines)):
        return ""
    start = lineno - 1
    while start > 0 and lines[start - 1].strip():
        start -= 1
    end = lineno - 1
    while end + 1 < len(lines) and lines[end + 1].strip():
        end += 1
    return "\n".join(lines[start:end + 1])


def sentences(text: str):
    """(line number, sentence) pairs. Crude split; enough to localise an absence claim."""
    for lineno, line in enumerate(text.splitlines(), start=1):
        for part in re.split(r"(?<=[.;:])\s+", line):
            if part.strip():
                yield lineno, part.strip()


def load_schema(path: Path):
    try:
        import yaml
    except ImportError:
        print("PyYAML required: pip install -r requirements.txt", file=sys.stderr)
        raise SystemExit(2)
    try:
        return yaml.safe_load(read_text(path)) or {}
    except Exception:
        return {}


# ---------------------------------------------------------------------------
# audit
# ---------------------------------------------------------------------------

def discover_blocks(sources: Path) -> list[Path]:
    return sorted({p.parent for p in sources.rglob("schema.yaml")
                   if (p.parent / "bblock.json").exists()})


def archived_names(archive: Path) -> set[str]:
    if not archive.is_dir():
        return set()
    return {p.parent.name for p in archive.rglob("schema.yaml")}


def audit_block(bb: Path, repo_tokens: set[str], archived: set[str],
                sources_names: set[str], archive_tokens: set[str] | None = None) -> list[dict]:
    findings: list[dict] = []
    desc = bb / "description.md"
    try:
        rel = str(bb.relative_to(REPO_ROOT)).replace(os.sep, "/")
    except ValueError:
        rel = bb.name  # a scratch copy outside the repo (self-test)
    if not desc.exists():
        return findings
    text = read_text(desc)
    if not text.strip():
        return findings

    archive_tokens = archive_tokens or set()
    lines = text.splitlines()

    own = set()
    for name in BLOCK_FILES:
        f = bb / name
        if f.exists():
            own |= tokens_in(read_text(f))

    # Property KEYS as the schema spells them. tokens_in() only matches prefix:name, so `@type`
    # and `@id` could never land in `own` and every table row naming them read as a phantom.
    schema_doc = load_schema(bb / "schema.yaml")
    own_props = all_property_names(schema_doc)
    own |= {p for p in own_props if ":" in p}

    def add(check, detail, line, token=""):
        findings.append({"check": check, "block": rel, "token": token,
                         "line": line, "detail": detail, "fix": ""})

    def line_text(n: int) -> str:
        return lines[n - 1] if 1 <= n <= len(lines) else ""

    # -- token checks -------------------------------------------------------
    for tok, line in sorted(backticked_tokens(text).items()):
        if tok in own:
            continue
        if tok in repo_tokens:
            add("unknown-in-block", f"`{tok}` is not declared anywhere in this block's own "
                                    f"files, but exists elsewhere in _sources", line, tok)
        elif tok in archive_tokens:
            # Naming an archived term is legitimate when the prose says it is archived -- the
            # canonical DDI-CDI spellings are worth documenting as the thing CDIF diverged from.
            if not RETIREMENT_RE.search(line_text(line)):
                add("archived-target", f"`{tok}` exists only under archive/; the line does not "
                                       f"say so", line, tok)
        else:
            add("unknown-in-repo", f"`{tok}` appears nowhere in _sources or archive/", line, tok)

    # -- table checks -------------------------------------------------------
    if has_property_table(text):
        root = collect_root_properties(schema_doc)
        listed = table_properties(text)
        # OFF BY DEFAULT. A property table here is usually SELECTIVE, not exhaustive --
        # niaidDataset's documents the portal's additions, niaidCreativeWork's the four nde:
        # terms -- so treating one as a complete enumeration reported 23 non-defects, and a
        # check that mostly cries wolf is one nobody reads. No reliable signal distinguishes
        # "this table is the block's shape" from "these are the extras", so the caller asks.
        if INCLUDE_OMISSIONS:
            for prop in sorted(root):
                if prop not in listed:
                    add("table-omission", f"schema declares `{prop}` at root level; the "
                                          f"property table does not list it", 0, prop)
        for prop, line in sorted(listed.items()):
            if prop in root or prop in own_props:
                continue  # root, or defined deeper in the schema (a $defs sub-table)
            add("table-phantom", f"property table lists `{prop}`, which the schema does "
                                 f"not define", line, prop)

    # -- link checks --------------------------------------------------------
    for lineno, line in enumerate(text.splitlines(), start=1):
        for target in MD_LINK_RE.findall(line):
            if target.startswith(("http://", "https://", "#", "mailto:")):
                continue
            clean = target.split("#", 1)[0].split("?", 1)[0]
            if not clean:
                continue
            resolved = (desc.parent / clean)
            if not exists_case_sensitive(resolved):
                add("dead-link", f"link target `{target}` does not exist "
                                 f"(case-sensitive check)", lineno)
            elif "/archive/" in resolved.resolve().as_posix() and "archive" not in line.lower():
                add("archived-target", f"link target `{target}` is under archive/ but the text "
                                       f"does not say so", lineno)

    # -- archived block mentioned as current --------------------------------
    for name in sorted(archived - sources_names):
        if len(name) < 6:
            continue
        for lineno, line in enumerate(text.splitlines(), start=1):
            # Judged on the whole PARAGRAPH, not the line: a migration note names the retired
            # block mid-list and says it is retired a sentence or two later, which is clear to a
            # reader and was being reported anyway.
            if re.search(rf"\b{re.escape(name)}\b", line) and not RETIREMENT_RE.search(
                    paragraph_at(text, lineno)):
                add("archived-target", f"mentions `{name}`, which now lives only under "
                                       f"archive/, without saying so", lineno, name)
                break

    # -- stale absence claims ----------------------------------------------
    for lineno, sent in sentences(text):
        if not ABSENCE_RE.search(sent):
            continue
        for span in BACKTICKED_RE.findall(sent):
            for tok in tokens_in(span):
                if tok in own:
                    add("stale-absence", f"asserts absence while the schema defines `{tok}`: "
                                         f"\"{sent[:140]}\"", lineno, tok)
                    break

    return findings


def build_context() -> dict:
    """The repo-wide sets every block is judged against. Built once."""
    repo_tokens: set[str] = set()
    for bb in discover_blocks(SOURCES):
        for name in BLOCK_FILES:
            f = bb / name
            if f.exists():
                repo_tokens |= tokens_in(read_text(f))
    archive_tokens: set[str] = set()
    if ARCHIVE.is_dir():
        for pattern in BLOCK_FILES:
            for f in ARCHIVE.rglob(pattern):
                archive_tokens |= tokens_in(read_text(f))
    return {
        "repo_tokens": repo_tokens,
        "archive_tokens": archive_tokens - repo_tokens,
        "archived": archived_names(ARCHIVE),
        "sources_names": {bb.name for bb in discover_blocks(SOURCES)},
    }


def run(blocks: list[Path], ctx: dict | None = None) -> list[dict]:
    ctx = ctx or build_context()
    out: list[dict] = []
    for bb in blocks:
        out.extend(audit_block(bb, ctx["repo_tokens"], ctx["archived"],
                               ctx["sources_names"], ctx["archive_tokens"]))
    return out


# ---------------------------------------------------------------------------
# self-test
# ---------------------------------------------------------------------------

def self_test() -> int:
    """Seed each defect into a scratch copy of a real block and assert its check fires.

    A green audit is the default state of a check that has stopped working -- the failure mode
    CLAUDE.md calls out five ways over. This asserts presence on a seeded defect AND absence on
    the clean original.
    """
    import shutil
    import tempfile

    src = SOURCES / "cdifDataType" / "cdifValueDomain"
    if not src.exists():
        print("self-test needs _sources/cdifDataType/cdifValueDomain", file=sys.stderr)
        return 2

    ctx = build_context()

    # The unknown-in-block seed has to be a token that exists SOMEWHERE in _sources but not in
    # this block's own files. Picked by measurement, not by guess: a hand-picked skos: term
    # failed because cdifValueDomain reaches skosConcept through cdifEnumerationDomain ->
    # cdifCodelist, so its resolvedSchema.json already carries those tokens.
    own = set()
    for name in BLOCK_FILES:
        f = src / name
        if f.exists():
            own |= tokens_in(read_text(f))
    own |= {p for p in all_property_names(load_schema(src / "schema.yaml")) if ":" in p}
    elsewhere = sorted(ctx["repo_tokens"] - own)
    if not elsewhere:
        print("self-test cannot run: no token exists outside this block", file=sys.stderr)
        return 2
    foreign = elsewhere[len(elsewhere) // 2]

    archive_only = sorted(ctx["archive_tokens"] - own)
    if not archive_only:
        print("self-test cannot seed archived-target: no archive-only token", file=sys.stderr)
        return 2
    archived_tok = archive_only[len(archive_only) // 2]

    def drop_a_table_row(text: str) -> str:
        """Delete the row documenting cdi:isDescribedBy -- the exact defect that prompted this
        tool. table-omission cannot be seeded by appending; it needs something taken away."""
        kept = [ln for ln in text.splitlines()
                if not (ln.strip().startswith("|") and "cdi:isDescribedBy" in ln)]
        return "\n".join(kept) + "\n"

    cases = [
        ("unknown-in-block", lambda t: t + f"\n\nSee `{foreign}` for details.\n"),
        ("unknown-in-repo", lambda t: t + "\n\nSee `cdif:thisWasNeverAThing` for details.\n"),
        ("dead-link", lambda t: t + "\n\n- [gone](../noSuchBlockHere/)\n"),
        ("stale-absence", lambda t: t + "\n\n- Does not yet expose `cdif:displayLabel`.\n"),
        ("table-phantom", lambda t: t + "\n\n| Property | Type |\n|---|---|\n"
                                        "| `cdif:notARealProperty` | string |\n"),
        ("table-omission", drop_a_table_row),
        # Seeded through the archive-only TOKEN, not a relative archive/ link: the scratch copy
        # lives outside the repo, so such a link is genuinely dead and raises dead-link instead.
        ("archived-target", lambda t: t + f"\n\nThe canonical spelling is `{archived_tok}`.\n"),
    ]

    failures = 0
    with tempfile.TemporaryDirectory() as td:
        for check, transform in cases:
            work = Path(td) / check
            shutil.copytree(src, work)
            # keep bblock.json so discovery still treats it as a block
            desc = work / "description.md"
            desc.write_text(transform(read_text(src / "description.md")),
                            encoding="utf-8", newline="\n")
            got = audit_block(work, ctx["repo_tokens"], ctx["archived"],
                              ctx["sources_names"], ctx["archive_tokens"])
            names = {f["check"] for f in got}
            if check in names:
                print(f"  PASS  {check:<18} fired on seeded defect")
            else:
                print(f"  FAIL  {check:<18} did NOT fire; raised {sorted(names) or 'nothing'}")
                failures += 1

    # and the clean original must not raise the seeded checks spuriously
    clean = {f["check"] for f in audit_block(src, ctx["repo_tokens"], ctx["archived"], ctx["sources_names"], ctx["archive_tokens"])}
    spurious = clean & {c for c, _ in cases}
    if spurious:
        print(f"  WARN  clean block already raises {sorted(spurious)} -- "
              f"the PASS results above may be false")
    else:
        print(f"  PASS  {'clean block':<18} raises none of the seeded checks")

    print()
    print(f"self-test: {len(cases) - failures}/{len(cases)} checks fire")
    return 1 if failures else 0


# ---------------------------------------------------------------------------
# main
# ---------------------------------------------------------------------------

def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("-b", "--block", help="substring filter on block path")
    ap.add_argument("-c", "--check", action="append", choices=CHECK_NAMES,
                    help="limit to these checks (repeatable)")
    ap.add_argument("-o", "--output", help="write findings as JSON")
    ap.add_argument("--include-omissions", action="store_true",
                    help="also report table-omission (advisory: these tables are usually "
                         "selective, not exhaustive)")
    ap.add_argument("--strict", action="store_true", help="exit 1 if any finding")
    ap.add_argument("--self-test", action="store_true", help="prove each check fires")
    args = ap.parse_args()

    global INCLUDE_OMISSIONS
    INCLUDE_OMISSIONS = args.include_omissions

    if args.self_test:
        INCLUDE_OMISSIONS = True  # the seeded case needs it
        return self_test()

    blocks = discover_blocks(SOURCES)
    if args.block:
        blocks = [b for b in blocks if args.block.lower() in str(b).lower()]
        if not blocks:
            print(f"no block matching {args.block!r}", file=sys.stderr)
            return 2

    findings = run(blocks)
    if args.check:
        findings = [f for f in findings if f["check"] in args.check]

    by_check: dict[str, list[dict]] = {}
    for f in findings:
        by_check.setdefault(f["check"], []).append(f)

    for check in CHECK_NAMES:
        rows = by_check.get(check)
        if not rows:
            continue
        print(f"\n{'=' * 78}\n{check}  ({len(rows)})\n{'=' * 78}")
        for f in sorted(rows, key=lambda r: (r["block"], r["line"])):
            loc = f"{f['block']}/description.md"
            if f["line"]:
                loc += f":{f['line']}"
            print(f"  {loc}")
            print(f"      {f['detail']}")

    print(f"\n{'=' * 78}")
    print(f"{len(findings)} finding(s) across {len(blocks)} block(s) "
          f"({len({f['block'] for f in findings})} block(s) affected)")
    counts = ", ".join(f"{c}={len(by_check[c])}" for c in CHECK_NAMES if c in by_check)
    print(counts or "clean")
    print("=" * 78)
    print("A finding means the prose and the schema DISAGREE, not which one is wrong.")

    if args.output:
        Path(args.output).write_text(
            json.dumps(findings, indent=2, ensure_ascii=False), encoding="utf-8", newline="\n")
        print(f"wrote {args.output}")

    return 1 if (args.strict and findings) else 0


if __name__ == "__main__":
    sys.exit(main())
