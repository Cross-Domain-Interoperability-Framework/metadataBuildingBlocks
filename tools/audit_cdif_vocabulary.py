#!/usr/bin/env python3
"""Inventory every `cdif:` term, so the namespace can be given definitions.

CDIF mints `cdif:` terms and defines none of them. Measured 2026-09-28:
`https://w3id.org/cdif/` returns 200 (it redirects to the book -- human HTML,
not a namespace document) while `https://w3id.org/cdif/Key` and
`https://w3id.org/cdif/has_PrimaryKey` return 404. The register holds 92
`itemClass: schema` + 1 `datatype`, no `model` block and no `ontology.ttl`, so
nothing anywhere says what these terms mean.

This produces the inventory that an ontology block would be written from:
every live `cdif:` term with its usage sites, inferred domain and range, and
whether a definition can be salvaged from existing prose.

Follows the `audit_ig_consistency.py` pattern deliberately. Each term carries
an empty `definition` field for a reviewer to fill, and re-running CARRIES
FILLED ONES FORWARD, matched on term name -- never on position, because terms
move in and out as schemas change.

    python tools/audit_cdif_vocabulary.py --self-test    # run FIRST
    python tools/audit_cdif_vocabulary.py -o cdif_ontology_register.json
    #   a reviewer writes into "definition"; re-run carries those forward

Domain is the nearest enclosing `@type` token, which is how these schemas say
"this is the class the property hangs off". `shacl_domains` is an INDEPENDENT
read from `sh:targetClass`. Neither is authoritative. Where they disagree that
disagreement is the finding -- it surfaced two real ones on 2026-09-28, noted
in the Findings section below.

Every applicator is walked (`allOf`/`anyOf`/`oneOf`/`if`/`then`/`else`/
`items`/`contains`/`additionalProperties`/`not`/`$defs`). A grep finds 52
apparent terms; 5 of those are prose in comments and descriptions, and the
walk is what tells them apart. If you add an applicator keyword to a schema
here, check this walker handles it -- the same hole made `contains` invisible
to `audit_ig_consistency.py` while it appeared in 76 files.

FINDINGS as of 2026-09-28 (47 live terms: 8 classes, 39 properties):
  * 8 properties have no description anywhere, so their definitions have to be
    written from scratch.
  * 7 are described differently at different sites, so the sites must be
    reconciled before one definition can be written.
  * Only 8 classes carry 39 properties, because most `cdif:` properties hang
    off `cdi:` classes. An ontology therefore cannot be self-contained: its
    `rdfs:domain` values point into the DDI-CDI namespace.
  * `cdif:isDefinedBy_Concept` is declared under `$defs/ConceptSystem` in
    cdifRepresentedVariable's schema but advised on `cdi:RepresentedVariable`
    by its SHACL -- and that property shape carries `sh:path`, `sh:severity`
    and `sh:message` with NO constraint component, so every value conforms and
    it can never produce a result. Its sibling `cdif:name` shape has
    `sh:minCount 1` and does fire.
  * `cdifOpenApi/schema.yaml:48` tells authors to "encode as a cdif:Reference",
    a class folded into `labeledLink` and archived on 2026-09-23.
"""

import argparse
import json
import re
import sys
from collections import defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import resolve_schema as rs

APPLICATORS = ("allOf", "anyOf", "oneOf", "if", "then", "else", "items",
               "contains", "additionalProperties", "not")
TERM = re.compile(r"^cdif:([A-Za-z_][A-Za-z0-9_]*)$")

# The classes the register held when this tool was written. Hard-coded so a
# walker that stops seeing real declarations fails the self-test instead of
# quietly reporting a smaller vocabulary.
KNOWN_CLASSES = [
    "cdif:EnumerationDomain", "cdif:ForeignKey", "cdif:Key",
    "cdif:LocatorMapping", "cdif:PhysicalMapping", "cdif:SentinelValueDomain",
    "cdif:SubstantiveValueDomain", "cdif:TextMapping",
]


def type_tokens(node):
    """The class tokens an `@type` subschema declares."""
    out = set()
    if not isinstance(node, dict):
        return out
    if isinstance(node.get("const"), str):
        out.add(node["const"])
    for value in node.get("enum") or []:
        if isinstance(value, str):
            out.add(value)
    for key in ("contains", "items"):
        out |= type_tokens(node.get(key))
    for key in ("allOf", "anyOf", "oneOf"):
        for branch in node.get(key) or []:
            out |= type_tokens(branch)
    return out


def describe_range(schema):
    """A short, readable range for *schema*."""
    if not isinstance(schema, dict):
        return "?"
    if "$ref" in schema:
        ref = schema["$ref"]
        if ref.startswith("#/$defs/"):
            return f"$defs/{ref.split('/')[-1]}"
        parts = [p for p in ref.split("#")[0].split("/") if p and p != ".."]
        return parts[-2] if len(parts) >= 2 else ref
    if "enum" in schema:
        return "enum"
    if "const" in schema:
        return f"const {schema['const']!r}"
    declared = schema.get("type")
    if declared == "array":
        return f"array of {describe_range(schema.get('items') or {})}"
    if declared:
        return declared if isinstance(declared, str) else "|".join(declared)
    for key in ("anyOf", "oneOf"):
        if key in schema:
            inner = {describe_range(b) for b in schema[key]
                     if isinstance(b, dict)}
            inner.discard("?")
            if inner:
                return " | ".join(sorted(inner))
    if "properties" in schema:
        return "object"
    return "?"


class Inventory:
    def __init__(self):
        self.props = defaultdict(
            lambda: {"sites": set(), "domains": set(), "ranges": set(),
                     "descriptions": [], "required_in": set()})
        self.classes = defaultdict(lambda: {"sites": set(), "properties": set()})

    def walk(self, node, rel, domain):
        if isinstance(node, list):
            for item in node:
                self.walk(item, rel, domain)
            return
        if not isinstance(node, dict):
            return

        here = domain
        properties = node.get("properties")
        if isinstance(properties, dict):
            declared = type_tokens(properties.get("@type"))
            minted = {t for t in declared if TERM.match(t)}
            for token in minted:
                self.classes[token]["sites"].add(rel)
            if minted:
                here = sorted(minted)[0]
            elif declared:
                here = sorted(declared)[0]

            required = set(node.get("required") or [])
            for key, sub in properties.items():
                if TERM.match(key):
                    self._record(key, sub, rel, here, key in required)
                self.walk(sub, rel, here)

        for key, value in node.items():
            if key == "properties":
                continue
            if isinstance(value, (dict, list)):
                self.walk(value, rel, here)

    def _record(self, term, schema, rel, domain, is_required):
        entry = self.props[term]
        entry["sites"].add(rel)
        entry["domains"].add(domain or f"(block {Path(rel).parent.name})")
        entry["ranges"].add(describe_range(schema))
        if is_required:
            entry["required_in"].add(domain or Path(rel).parent.name)
        if isinstance(schema, dict):
            description = schema.get("description")
            if isinstance(description, str) and description.strip():
                entry["descriptions"].append(" ".join(description.split())[:400])
        if domain and TERM.match(domain):
            self.classes[domain]["properties"].add(term)


def guide_definitions():
    """{term: [(repo, description)]} from the release-repo guides.

    The guides carry the definitions the schemas mostly do not: 23 terms have
    an unambiguous `**Description:**` there, including 4 that have no schema
    description at all. Reuses audit_ig_consistency's own reader, so "what is
    a property block" and "what is its Description" cannot drift from the tool
    that audits them.

    OPTIONAL BY DESIGN. CI clones only this repo, so an absent sibling
    checkout must mean "no guide definitions", never a failed run.
    """
    try:
        import audit_ig_consistency as aic
    except Exception as exc:                       # noqa: BLE001
        return {}, f"guides unavailable ({type(exc).__name__})"
    root = getattr(aic, "CDIF_ROOT", None)
    if not root or not Path(root).exists():
        return {}, "no sibling release repos"
    guides = sorted(Path(root).glob("*/*ImplementationGuide.md"))
    if not guides:
        return {}, "no implementation guides found"
    hits = defaultdict(list)
    for guide in guides:
        try:
            blocks = aic.read_guide(guide)
        except Exception:                          # noqa: BLE001
            continue                               # one bad guide is not fatal
        for block in blocks:
            name = block["name"]
            if not TERM.match(name):
                continue
            description = (block["fields"].get("description") or "").strip()
            if description:
                hits[name].append((guide.parent.name, description))
    return dict(hits), f"{len(guides)} guides"


def shacl_domains(sources_dir):
    """`sh:targetClass` per `cdif:` path -- an independent read on domain."""
    found = defaultdict(set)
    for path in sorted(Path(sources_dir).rglob("*.shacl")):
        if "archive" in path.parts:
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        for block in re.split(r"\n(?=\S)", text):
            target = re.search(r"sh:targetClass\s+(\S+)", block)
            if not target:
                continue
            for match in re.finditer(
                    r"sh:path\s+(cdif:[A-Za-z_][A-Za-z0-9_]*)", block):
                found[match.group(1)].add(target.group(1).rstrip(";,"))
    return found


def collect(sources_dir=None):
    sources_dir = Path(sources_dir or rs.SOURCES_DIR)
    inventory = Inventory()
    files = [p for p in sorted(sources_dir.rglob("schema.yaml"))
             if "archive" not in p.parts]
    for path in files:
        schema = rs.load_schema_file(path)
        if isinstance(schema, dict):
            try:
                rel = path.relative_to(rs.REPO_ROOT).as_posix()
            except ValueError:
                rel = path.as_posix()
            inventory.walk(schema, rel, None)
    return inventory, files, shacl_domains(sources_dir)


def _guide_fields(name, guides):
    """Guide definition for *name*: one, several, or none.

    A term described differently in two guides is NOT resolved here. Those
    differences are per-class phrasings ("name for the component" vs "string
    used to identify the variable in data"), and picking one silently would
    flatten a real distinction -- the mistake that collapsed three senses of
    schema:additionalType earlier in this work. They are surfaced for the
    reviewer instead.
    """
    hits = guides.get(name) or []
    distinct = sorted({d for _, d in hits})
    return {
        "guide_definition": distinct[0] if len(distinct) == 1 else None,
        "guide_variants": distinct if len(distinct) > 1 else [],
        "guide_sources": sorted({g for g, _ in hits}),
    }


def build_register(sources_dir=None, previous=None, guides=None):
    inventory, files, shacl = collect(sources_dir)
    previous = previous or {}
    guides = guides if guides is not None else {}
    register = {"classes": {}, "properties": {}}

    def settle(name, entry):
        """A reviewer's definition wins; else an unambiguous guide one."""
        if previous.get(name):
            entry["definition"] = previous[name]
            entry["definition_from"] = "reviewer"
        elif entry["guide_definition"]:
            entry["definition"] = entry["guide_definition"]
            entry["definition_from"] = "guide"
        else:
            entry["definition"] = ""
            entry["definition_from"] = ""
        return entry

    for name, info in sorted(inventory.classes.items()):
        entry = {
            "kind": "rdfs:Class",
            "properties": sorted(info["properties"]),
            "sites": sorted(info["sites"]),
            **_guide_fields(name, guides),
        }
        register["classes"][name] = settle(name, entry)

    for name, info in sorted(inventory.props.items()):
        variants = sorted(set(info["descriptions"]), key=len, reverse=True)
        entry = {
            "kind": "rdf:Property",
            "candidate_definition": variants[0] if variants else None,
            "description_variants": len(variants),
            "domains": sorted(info["domains"]),
            "shacl_domains": sorted(shacl.get(name, [])),
            "ranges": sorted(info["ranges"]),
            "required_in": sorted(info["required_in"]),
            "site_count": len(info["sites"]),
            "sites": sorted(info["sites"]),
            **_guide_fields(name, guides),
        }
        register["properties"][name] = settle(name, entry)
    return register, len(files)


def load_previous(path):
    """Definitions a reviewer has already written, keyed by term name."""
    if not path or not Path(path).exists():
        return {}
    existing = json.loads(Path(path).read_text(encoding="utf-8"))
    carried = {}
    for section in ("classes", "properties"):
        for name, entry in (existing.get(section) or {}).items():
            if entry.get("definition"):
                carried[name] = entry["definition"]
    return carried


def render_markdown(register):
    lines = []
    add = lines.append
    props = register["properties"]
    no_definition = sorted(n for n, i in props.items()
                           if not i["candidate_definition"])
    conflicting = sorted(n for n, i in props.items()
                         if i["description_variants"] > 1)

    add("# CDIF vocabulary inventory")
    add("")
    add(f"**{len(register['classes'])} classes, {len(props)} properties** — every "
        "`cdif:` term live in `_sources/` (`archive/` excluded). Extracted by "
        "walking every schema applicator, not by grep, so a term nested in an "
        "`allOf` branch is included and prose mentions are excluded.")
    add("")
    add("`domain` is the nearest enclosing `@type`; `shacl domain` is an "
        "independent read from `sh:targetClass`. Neither is authoritative — "
        "where they disagree, the disagreement is the finding.")
    add("")
    add("## Editorial gaps")
    add("")
    add(f"- **{len(no_definition)} properties carry no description anywhere**, so a "
        "definition must be written from scratch: "
        + ", ".join(f"`{n}`" for n in no_definition))
    add(f"- **{len(conflicting)} properties are described differently at different "
        "sites**, so the sites must be reconciled first: "
        + ", ".join(f"`{n}`" for n in conflicting))
    add("")
    add("## Classes")
    add("")
    add("| class | declared in | properties |")
    add("|---|---|---|")
    for name, info in sorted(register["classes"].items()):
        where = ", ".join(Path(s).parent.name for s in info["sites"])
        owned = ", ".join(f"`{p}`" for p in info["properties"]) or "—"
        add(f"| `{name}` | {where} | {owned} |")

    add("")
    add("## Properties")
    add("")
    add("| property | domain | shacl domain | range | required in | sites | definition |")
    add("|---|---|---|---|---|---|---|")
    for name, info in sorted(props.items()):
        domain = ", ".join(f"`{d}`" for d in info["domains"][:3])
        if len(info["domains"]) > 3:
            domain += f" +{len(info['domains']) - 3}"
        shacl = ", ".join(f"`{d}`" for d in info["shacl_domains"][:2]) or "—"
        ranges = ", ".join(f"`{r}`" for r in info["ranges"][:3])
        if len(info["ranges"]) > 3:
            ranges += f" +{len(info['ranges']) - 3}"
        required = ", ".join(info["required_in"][:2]) or "—"
        if not info["candidate_definition"]:
            state = "**none**"
        elif info["description_variants"] > 1:
            state = f"**{info['description_variants']} variants**"
        else:
            state = "candidate"
        add(f"| `{name}` | {domain or '—'} | {shacl} | {ranges or '—'} | "
            f"{required} | {info['site_count']} | {state} |")

    add("")
    add("## Candidate definitions")
    add("")
    add("The longest `description` found for each property. These are "
        "schema-authoring prose — written to tell an author what to put in a "
        "field, not to define a term — so they need rewriting, but they carry "
        "the intent.")
    add("")
    for name, info in sorted(props.items()):
        if info["candidate_definition"]:
            add(f"**`{name}`** — {info['candidate_definition']}")
            add("")
    return "\n".join(lines) + "\n"


# ---------------------------------------------------------------------------
# Self-test
# ---------------------------------------------------------------------------

def _check(results, name, got, want):
    ok = got == want
    results.append(ok)
    print(f"  {'PASS' if ok else 'FAIL'}  {name}")
    if not ok:
        print(f"        got  {got}")
        print(f"        want {want}")


def self_test():
    import tempfile
    import yaml

    print("audit_cdif_vocabulary self-test")
    results = []

    with tempfile.TemporaryDirectory() as td:
        src = Path(td) / "_sources"

        # One term behind each applicator. If the walk drops a keyword the
        # term vanishes and the vocabulary silently shrinks.
        nested = {
            "properties": {"@type": {"const": "cdif:Widget"}},
            "allOf": [{"properties": {"cdif:viaAllOf": {"type": "string"}}}],
            "anyOf": [{"properties": {"cdif:viaAnyOf": {"type": "string"}}}],
            "oneOf": [{"properties": {"cdif:viaOneOf": {"type": "string"}}}],
            "if": {"properties": {"cdif:viaIf": {"type": "string"}}},
            "then": {"properties": {"cdif:viaThen": {"type": "string"}}},
            "items": {"properties": {"cdif:viaItems": {"type": "string"}}},
            "contains": {"properties": {"cdif:viaContains": {"type": "string"}}},
            "$defs": {"X": {"properties": {"cdif:viaDefs": {"type": "string"}}}},
        }
        (src / "widget").mkdir(parents=True)
        (src / "widget/schema.yaml").write_text(
            yaml.safe_dump(nested), encoding="utf-8")

        # archive/ is retired and must not contribute terms.
        (src / "archive/old").mkdir(parents=True)
        (src / "archive/old/schema.yaml").write_text(
            yaml.safe_dump({"properties": {"cdif:retired": {"type": "string"}}}),
            encoding="utf-8")

        register, _ = build_register(sources_dir=src)
        found = sorted(register["properties"])
        _check(results, "every applicator is walked", found, [
            "cdif:viaAllOf", "cdif:viaAnyOf", "cdif:viaContains",
            "cdif:viaDefs", "cdif:viaIf", "cdif:viaItems", "cdif:viaOneOf",
            "cdif:viaThen",
        ])
        _check(results, "archive/ contributes nothing",
               "cdif:retired" in register["properties"], False)
        _check(results, "a cdif: @type const is recorded as a class",
               sorted(register["classes"]), ["cdif:Widget"])
        _check(results, "domain is the nearest enclosing @type",
               register["properties"]["cdif:viaAllOf"]["domains"],
               ["cdif:Widget"])

        # Prose must not become a term. This is what separates the 47 live
        # terms from a grep's 52.
        (src / "prose").mkdir()
        (src / "prose/schema.yaml").write_text(
            yaml.safe_dump({"description": "encode as a cdif:Reference please",
                            "properties": {"schema:name": {"type": "string"}}}),
            encoding="utf-8")
        register, _ = build_register(sources_dir=src)
        _check(results, "a term named only in prose is not collected",
               "cdif:Reference" in register["properties"]
               or "cdif:Reference" in register["classes"], False)

        # required, range, and description salvage
        (src / "shaped").mkdir()
        (src / "shaped/schema.yaml").write_text(yaml.safe_dump({
            "properties": {
                "@type": {"const": "cdif:Shaped"},
                "cdif:pinned": {"type": "array", "items": {"type": "string"},
                                "description": "A pinned value."},
            },
            "required": ["cdif:pinned"],
        }), encoding="utf-8")
        register, _ = build_register(sources_dir=src)
        pinned = register["properties"]["cdif:pinned"]
        _check(results, "range reads through an array", pinned["ranges"],
               ["array of string"])
        _check(results, "required is recorded", pinned["required_in"],
               ["cdif:Shaped"])
        _check(results, "a description becomes a candidate definition",
               pinned["candidate_definition"], "A pinned value.")

        # Carry-forward, matched on name. Write the register with one
        # definition filled, then rebuild and check it survived.
        out = Path(td) / "register.json"
        register["properties"]["cdif:pinned"]["definition"] = "MY DEFINITION"
        out.write_text(json.dumps(register), encoding="utf-8")
        rebuilt, _ = build_register(sources_dir=src,
                                    previous=load_previous(out))
        _check(results, "a written definition carries forward",
               rebuilt["properties"]["cdif:pinned"]["definition"],
               "MY DEFINITION")
        _check(results, "an unwritten definition stays empty",
               rebuilt["properties"]["cdif:viaAllOf"]["definition"], "")

        # Guide extraction. One agreeing term, one disagreeing.
        fake_guides = {
            "cdif:viaAllOf": [("profile-a", "One agreed definition."),
                              ("profile-b", "One agreed definition.")],
            "cdif:viaAnyOf": [("profile-a", "First sense."),
                              ("profile-b", "Second, different sense.")],
        }
        g, _ = build_register(sources_dir=src, guides=fake_guides)
        _check(results, "an agreed guide definition is adopted",
               g["properties"]["cdif:viaAllOf"]["definition"],
               "One agreed definition.")
        _check(results, "and is marked as coming from a guide",
               g["properties"]["cdif:viaAllOf"]["definition_from"], "guide")
        # Picking one of two senses silently is the failure to avoid.
        _check(results, "disagreeing guides do NOT settle a definition",
               g["properties"]["cdif:viaAnyOf"]["definition"], "")
        _check(results, "both senses are surfaced instead",
               g["properties"]["cdif:viaAnyOf"]["guide_variants"],
               ["First sense.", "Second, different sense."])
        # A reviewer outranks a guide.
        g2, _ = build_register(sources_dir=src, guides=fake_guides,
                               previous={"cdif:viaAllOf": "REVIEWER WINS"})
        _check(results, "a reviewer definition outranks a guide",
               (g2["properties"]["cdif:viaAllOf"]["definition"],
                g2["properties"]["cdif:viaAllOf"]["definition_from"]),
               ("REVIEWER WINS", "reviewer"))

    # Real repo anchor.
    register, scanned = build_register()
    _check(results, "real repo: the known classes are all still found",
           sorted(register["classes"]), KNOWN_CLASSES)
    _check(results, "real repo: scanned the whole register", scanned, 93)

    # Guides are optional: CI clones only this repo. A missing sibling
    # checkout must mean "no definitions", never a traceback -- so this
    # asserts the shape of the result, not that any guide was found.
    found, note = guide_definitions()
    _check(results, "guide lookup degrades instead of failing",
           (isinstance(found, dict), isinstance(note, str)), (True, True))
    if found:
        print(f"        ({note}, {len(found)} term(s) described)")
    else:
        print(f"        (no guides here: {note} — expected in CI)")

    passed = sum(1 for ok in results if ok)
    print(f"\n{passed}/{len(results)} checks passed")
    return passed == len(results)


def main():
    parser = argparse.ArgumentParser(
        description="Inventory every cdif: term for ontology authoring.")
    parser.add_argument("-o", "--output", type=Path,
                        help="Write the register JSON here (definitions in an "
                             "existing file at this path carry forward)")
    parser.add_argument("--md", type=Path,
                        help="Also write the readable table here")
    parser.add_argument("--self-test", action="store_true",
                        help="Prove each rule still fires")
    args = parser.parse_args()

    if args.self_test:
        sys.exit(0 if self_test() else 1)

    carried = load_previous(args.output)
    guides, guide_note = guide_definitions()
    register, scanned = build_register(previous=carried, guides=guides)
    props = register["properties"]
    everything = {**register["classes"], **props}
    no_definition = [n for n, i in props.items() if not i["candidate_definition"]]
    conflicting = [n for n, i in props.items() if i["description_variants"] > 1]
    settled = [n for n, i in everything.items() if i["definition"]]
    split = [n for n, i in everything.items() if i["guide_variants"]]
    unsettled = [n for n, i in everything.items()
                 if not i["definition"] and not i["guide_variants"]]

    print(f"scanned {scanned} schema.yaml (archive excluded)")
    print(f"{len(register['classes'])} classes, {len(props)} properties")
    print(f"  {len(no_definition)} with no description anywhere")
    print(f"  {len(conflicting)} described differently at different sites")
    print(f"guides: {guide_note}")
    print(f"  {len(settled)} term(s) now carry a definition")
    print(f"  {len(split)} left for a reviewer because the guides disagree: "
          + ", ".join(sorted(split)))
    print(f"  {len(unsettled)} with no definition from any source")
    if carried:
        still = sum(1 for n in carried
                    if n in props or n in register["classes"])
        print(f"carried forward {len(carried)} definition(s); "
              f"{len(carried) - still} no longer have a term")

    if args.output:
        args.output.write_text(
            json.dumps(register, indent=2, ensure_ascii=False) + "\n",
            encoding="utf-8")
        print(f"wrote {args.output}")
    if args.md:
        args.md.write_text(render_markdown(register), encoding="utf-8")
        print(f"wrote {args.md}")
    if not args.output and not args.md:
        print("\n(no -o/--md given; nothing written)")


if __name__ == "__main__":
    main()
