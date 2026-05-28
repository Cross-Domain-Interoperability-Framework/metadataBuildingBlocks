#!/usr/bin/env python3
"""
Standalone SHACL validation for a target building block or profile (prototype).

This is intentionally SEPARATE from tools/validate_examples.py (which stays the
fast, JSON-Schema-only default gate). It:
  1. resolves a target BB/profile directory,
  2. gathers that target's rules.shacl PLUS every transitively-composed BB's
     rules.shacl (by following $ref links between schema.yaml files),
  3. expands the target's example*.json from JSON-LD to RDF,
  4. runs pyshacl against the combined shapes graph,
  5. reports results grouped by severity.

Report-only by default (always exits 0) so it can be wired in as a non-fatal
"warnings" check. Pass --strict to exit non-zero when any sh:Violation is found.

Requires: pyshacl (pulls in rdflib, which provides the JSON-LD parser).
    pip install pyshacl

Usage:
    python tools/validate_shacl.py CDIFDataStructureProfile
    python tools/validate_shacl.py CDIFDataStructureProfile --verbose
    python tools/validate_shacl.py _sources/profiles/cdifCompositeProfile/DataDescriptionWithStructure --strict
"""

import argparse
import json
import sys
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
SOURCES = REPO_ROOT / "_sources"


def find_target_dir(target: str) -> Path:
    """Resolve a target given as a path or a BB/profile name."""
    p = Path(target)
    if p.is_dir() and (p / "schema.yaml").exists():
        return p.resolve()
    matches = [
        d for d in SOURCES.rglob(target)
        if d.is_dir() and (d / "schema.yaml").exists()
    ]
    if not matches:
        matches = [
            d for d in SOURCES.rglob("*")
            if d.is_dir() and d.name.lower() == target.lower()
            and (d / "schema.yaml").exists()
        ]
    if len(matches) == 1:
        return matches[0].resolve()
    if not matches:
        sys.exit(f"No building block / profile directory found for '{target}'.")
    sys.exit("Ambiguous target; candidates:\n  " + "\n  ".join(str(m) for m in matches))


def _iter_refs(node):
    if isinstance(node, dict):
        for k, v in node.items():
            if k == "$ref" and isinstance(v, str):
                yield v
            else:
                yield from _iter_refs(v)
    elif isinstance(node, list):
        for item in node:
            yield from _iter_refs(item)


def gather_schema_files(start_schema: Path) -> set:
    """BFS over $ref links to other schema.yaml files (fragments stripped)."""
    seen = set()
    stack = [start_schema.resolve()]
    while stack:
        cur = stack.pop()
        if cur in seen or not cur.exists():
            continue
        seen.add(cur)
        try:
            doc = yaml.safe_load(cur.read_text(encoding="utf-8"))
        except Exception:
            continue
        for ref in _iter_refs(doc):
            ref_path = ref.split("#", 1)[0]
            if not ref_path or not ref_path.endswith(".yaml"):
                continue
            target = (cur.parent / ref_path).resolve()
            if target.exists():
                stack.append(target)
    return seen


def gather_rule_files(schema_files) -> list:
    """rules.shacl (with actual shapes) for each schema.yaml's directory."""
    rules = []
    for sf in sorted(schema_files):
        rf = sf.parent / "rules.shacl"
        if rf.exists() and "sh:NodeShape" in rf.read_text(encoding="utf-8"):
            rules.append(rf)
    return rules


def merge_shapes_dedup(rule_files, profile_name):
    """Merge the rule files into one shapes graph, deduping shapes that are
    defined in more than one source. A naive union yields e.g. a PropertyShape
    with two sh:path (shared named shapes such as cdifd:rightsProperty use a
    blank-node `sh:path [ sh:alternativePath (...) ]`, and each parse mints a
    distinct blank node), which pyshacl rejects with a ShapeLoadError.

    For each *named* shape defined in more than one file, one definition wins
    and the losers' concise bounded descriptions are removed before union.
    Blank-node-rooted (anonymous) shapes and all references TO a shape are
    preserved (only the losing named shape's own subgraph is dropped).

    Precedence for a duplicated named shape: the profile's own rules.shacl wins
    (it intentionally overrides base shapes like CDIFCatalogRecordShape /
    CDIFDatasetMandatoryShape); otherwise the BB whose directory name appears in
    the shape's local name wins (e.g. definedTerm owns CDIFDefinedTermShape);
    else fall back to sorted directory name.
    """
    import rdflib
    from rdflib import RDF
    SH = rdflib.Namespace("http://www.w3.org/ns/shacl#")
    parsed = []
    for rf in rule_files:
        g = rdflib.Graph()
        g.parse(str(rf), format="turtle")
        parsed.append((rf, g))

    def priority(rf, local):
        name = rf.parent.name
        if name == profile_name:
            return (0, name)
        if name.lower() in local.lower():
            return (1, name)
        return (2, name)

    # collect named shapes -> candidate (rf, graph) definitions
    shape_defs = {}
    for rf, g in parsed:
        for typ in (SH.NodeShape, SH.PropertyShape):
            for s in g.subjects(RDF.type, typ):
                if isinstance(s, rdflib.BNode):
                    continue
                shape_defs.setdefault(s, []).append((rf, g))

    # pick the single winning file for each duplicated named shape
    winner = {}
    for s, cands in shape_defs.items():
        local = str(s).split("#")[-1].split("/")[-1]
        rf, _g = min(cands, key=lambda c: priority(c[0], local))
        winner[s] = rf

    out = rdflib.Graph()
    for rf, g in parsed:
        # Remove the concise bounded description of every named shape this file
        # does NOT win, so only the winner contributes that shape's definition
        # (and its blank-node path). Anonymous shapes and references survive.
        for s, w in winner.items():
            if w is not rf and (s, None, None) in g:
                for tr in list(g.cbd(s)):
                    g.remove(tr)
        out += g

    for prefix, ns in (
        ("rdf", rdflib.RDF), ("rdfs", rdflib.RDFS), ("sh", SH), ("xsd", rdflib.XSD),
        ("schema", "http://schema.org/"), ("dcterms", "http://purl.org/dc/terms/"),
        ("cdi", "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/"),
        ("cdif", "https://cdif.org/0.1/"),
        ("cdifd", "https://cdif.org/validation/0.1/shacl#"),
        ("skos", "http://www.w3.org/2004/02/skos/core#"),
        ("dqv", "http://www.w3.org/ns/dqv#"), ("spdx", "http://spdx.org/rdf/terms#"),
        ("csvw", "http://www.w3.org/ns/csvw#"), ("prov", "http://www.w3.org/ns/prov#"),
        ("time", "http://www.w3.org/2006/time#"), ("dcat", "http://www.w3.org/ns/dcat#"),
        ("geosparql", "http://www.opengis.net/ont/geosparql#"),
    ):
        out.bind(prefix, ns, replace=True)
    return out


def load_example_graph(example_path: Path, context_jsonld: Path):
    """Expand a JSON-LD example to an RDF graph; inject context.jsonld if absent."""
    import rdflib
    data = json.loads(example_path.read_text(encoding="utf-8"))
    if "@context" not in data and context_jsonld and context_jsonld.exists():
        ctx = json.loads(context_jsonld.read_text(encoding="utf-8")).get("@context")
        if ctx is not None:
            data = {"@context": ctx, **data}
    g = rdflib.Graph()
    g.parse(data=json.dumps(data), format="json-ld")
    return g


def extract_results(report_graph):
    import rdflib
    SH = rdflib.Namespace("http://www.w3.org/ns/shacl#")
    out = []
    for r in report_graph.subjects(rdflib.RDF.type, SH.ValidationResult):
        sev = report_graph.value(r, SH.resultSeverity)
        out.append({
            "severity": sev.split("#")[-1] if sev else "Violation",
            "focus": str(report_graph.value(r, SH.focusNode) or ""),
            "path": str(report_graph.value(r, SH.resultPath) or ""),
            "message": str(report_graph.value(r, SH.resultMessage) or ""),
            "shape": str(report_graph.value(r, SH.sourceShape) or ""),
        })
    return out


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("target", help="BB/profile name or directory path")
    ap.add_argument("--verbose", "-v", action="store_true",
                    help="List every result (default: violations + summary)")
    ap.add_argument("--strict", action="store_true",
                    help="Exit non-zero if any sh:Violation is found")
    ap.add_argument("--emit-shapes", metavar="FILE",
                    help="Write the merged+deduped shapes graph (the $ref-graph "
                         "rule bundle) to FILE as Turtle, then exit. Use to "
                         "(re)generate a release profile's *Rules.shacl.")
    args = ap.parse_args()

    try:
        import pyshacl  # noqa: F401
        import rdflib   # noqa: F401
    except ImportError:
        sys.exit("pyshacl/rdflib not installed. Run: pip install pyshacl")
    import pyshacl

    target_dir = find_target_dir(args.target)
    schema_files = gather_schema_files(target_dir / "schema.yaml")
    rule_files = gather_rule_files(schema_files)

    if args.emit_shapes:
        merged = merge_shapes_dedup(rule_files, target_dir.name)
        merged.serialize(destination=args.emit_shapes, format="turtle")
        print(f"Wrote {len(merged)} triples from {len(rule_files)} rules.shacl "
              f"to {args.emit_shapes}")
        return

    examples = sorted(target_dir.glob("example*.json"))
    context_jsonld = target_dir / "context.jsonld"

    print(f"Target:        {target_dir.relative_to(REPO_ROOT)}")
    print(f"Schema deps:   {len(schema_files)} schema.yaml files")
    print(f"Rule files:    {len(rule_files)} rules.shacl with shapes")
    print(f"Examples:      {len(examples)}")
    if args.verbose:
        for rf in rule_files:
            print(f"  rule: {rf.relative_to(REPO_ROOT)}")
    if not examples:
        print("No example*.json found in target directory.")
        return 0

    shapes_graph = merge_shapes_dedup(rule_files, target_dir.name)

    total = {"Violation": 0, "Warning": 0, "Info": 0}
    any_violation = False

    for ex in examples:
        rel = ex.relative_to(REPO_ROOT)
        try:
            data_graph = load_example_graph(ex, context_jsonld)
            _, report_graph, _ = pyshacl.validate(
                data_graph, shacl_graph=shapes_graph,
                advanced=True, inference="none", allow_warnings=True,
            )
        except Exception as ex_err:
            print(f"\nERROR {rel}: {type(ex_err).__name__}: {str(ex_err)[:200]}")
            continue

        results = extract_results(report_graph)
        counts = {"Violation": 0, "Warning": 0, "Info": 0}
        for r in results:
            counts[r["severity"]] = counts.get(r["severity"], 0) + 1
        for k in total:
            total[k] += counts.get(k, 0)
        if counts["Violation"]:
            any_violation = True

        status = "OK" if not results else \
            f'{counts["Violation"]}V {counts["Warning"]}W {counts["Info"]}I'
        print(f"\n{rel}: {status}")
        show = results if args.verbose else [r for r in results if r["severity"] == "Violation"]
        for r in show:
            loc = r["focus"] + (f"  ({r['path']})" if r["path"] else "")
            print(f"  [{r['severity']}] {loc}")
            print(f"      {r['message'][:240]}")

    print(f"\n{'='*60}")
    print(f"Totals: {total['Violation']} violations, "
          f"{total['Warning']} warnings, {total['Info']} info "
          f"across {len(examples)} examples")
    print(f"{'='*60}")

    return 1 if (args.strict and any_violation) else 0


if __name__ == "__main__":
    sys.exit(main())
