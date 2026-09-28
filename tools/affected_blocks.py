#!/usr/bin/env python3
"""Which blocks must be regenerated when a given set of files changes.

check-schema-drift.yml regenerates all 92 blocks on every pull request
(~11 min), because a source edit that lands without its artifact is
invisible. But a block's resolved output can only move if the block itself
changed or something it $refs did, so most of that sweep is spent proving
that 88 untouched blocks are still current.

This computes the reverse-$ref closure of a change set: the blocks whose
artifacts the change can actually move. Measured 2026-09-28 for
xasProperties/xasFacility -- 4 blocks, 4.5 s, against ~11 min for --all.

The saving is NOT uniform, and the shape of the graph is the reason. Edits
to peripheral blocks are cheap (xasFacility 4% of --all, cdifCodelist 13%);
edits to hubs are not (skosConcept 65%, identifier 63%, and ddicdiDataTypes
has 22 direct dependents). This buys a fast common case, not a fast worst
case.

WHY THIS IS SOUND, AND HOW IT WOULD STOP BEING SOUND
----------------------------------------------------
A block's resolved output depends only on its own $ref closure. Two places
in resolve_schema.py decide that, and both were checked on 2026-09-28:

  * inline_low_use_defs() counts uses via count_def_refs(schema) against a
    single in-memory schema. There is no register-wide use count, so how
    often the rest of the repo $refs a def never enters the result.
  * _is_type_library() is evaluated on the ROOT schema_path only (twice, at
    resolve_schema.py:1396 and :1413) and never per dependency, so a
    dependency's bblock.json cannot move a dependent's bytes.

If either grows cross-schema state, this tool silently under-reports and a
pull request goes green over real drift -- a rule that stops working looks
exactly like a rule that passes. That is why `main` keeps the
unconditional --all: the backstop is the thing that would notice, and it
must not be traded away for this.

Two further guards, rather than assumptions:

  * The graph is built with resolve_schema's own loader and the result is
    intersected with its own find_all_resolvable_schemas(), so "which
    blocks exist" and "which blocks --all would write" cannot drift from
    the resolver.
  * A URL $ref would make the output depend on the network rather than on
    the tree. There are none today; if one appears this reports ALL instead
    of reasoning about it.

Anything under tools/ reports ALL: cheap, because tool edits are rare, and
correct without having to model what a tool change does.

Usage:
    python tools/affected_blocks.py --base origin/main
    python tools/affected_blocks.py --changed _sources/a/schema.yaml ...
    python tools/affected_blocks.py --self-test
    python tools/affected_blocks.py --drift-test
"""

import argparse
import ast
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import resolve_schema as rs
import yaml

REPO_ROOT = rs.REPO_ROOT
ALL = "ALL"

WORKFLOW = ".github/workflows/check-schema-drift.yml"

# The tools that can move a generated schema: the ones the drift workflow
# actually runs, plus anything they import from tools/. Nothing else under
# tools/ qualifies, and the distinction matters -- an earlier version treated
# every tools/ change as a full sweep, which made a change to
# audit_ig_consistency.py (which cannot write a schema at all) regenerate all
# 92 blocks. Most pull requests here touch some tool, so that rule collapsed
# straight back to the full run it was meant to avoid.
#
# Declared here but DERIVED in the self-test from the workflow and the import
# graph, so adding a tool to the workflow without adding it here fails the
# test rather than quietly shrinking what triggers a sweep.
RESOLUTION_TOOLS = frozenset({
    "tools/resolve_schema.py",
    "tools/regenerate_schema_json.py",
    "tools/affected_blocks.py",
})

# requirements.txt is in here because the YAML parser is an input to every
# resolved schema, even though a version bump changing the output would be a
# surprise.
GLOBAL_PATHS = frozenset({WORKFLOW, "requirements.txt"})


def _derive_resolution_tools():
    """What RESOLUTION_TOOLS should be, read off the workflow and imports."""
    text = (REPO_ROOT / WORKFLOW).read_text(encoding="utf-8")
    local = {p.stem for p in (REPO_ROOT / "tools").glob("*.py")}
    seen, stack = set(), re.findall(r"python (tools/[A-Za-z0-9_]+\.py)", text)
    while stack:
        rel = stack.pop()
        if rel in seen:
            continue
        seen.add(rel)
        path = REPO_ROOT / rel
        if not path.exists():
            continue
        for node in ast.walk(ast.parse(path.read_text(encoding="utf-8"))):
            if isinstance(node, ast.Import):
                names = [a.name for a in node.names]
            elif isinstance(node, ast.ImportFrom) and node.module:
                names = [node.module]
            else:
                continue
            stack.extend(f"tools/{n}.py" for n in names if n in local)
    return seen


def _collect_refs(node, base_dir, files, urls):
    """Every external $ref in *node*, resolved against *base_dir*."""
    if isinstance(node, dict):
        ref = node.get("$ref")
        if isinstance(ref, str) and ref and not ref.startswith("#"):
            target = ref.split("#")[0]
            if target.startswith(("http://", "https://")):
                urls.append(ref)
            elif target:
                files.add((base_dir / target).resolve())
        for value in node.values():
            _collect_refs(value, base_dir, files, urls)
    elif isinstance(node, list):
        for item in node:
            _collect_refs(item, base_dir, files, urls)


def build_forward_graph(sources_dir=None):
    """schema.yaml -> the set of schema.yaml files it $refs.

    Returns (graph, url_refs). A non-existent target is dropped here and
    caught by the resolver instead, which refuses to write anything when a
    $ref does not resolve.
    """
    sources_dir = sources_dir or rs.SOURCES_DIR
    graph, urls = {}, []
    for schema_path in sorted(Path(sources_dir).rglob("schema.yaml")):
        schema = rs.load_schema_file(schema_path)
        if not isinstance(schema, dict):
            continue
        files = set()
        _collect_refs(schema, schema_path.parent, files, urls)
        graph[schema_path.resolve()] = {f for f in files if f.exists()}
    return graph, urls


def build_reverse_graph(forward):
    reverse = {}
    for source, targets in forward.items():
        for target in targets:
            reverse.setdefault(target, set()).add(source)
    return reverse


def closure(seeds, reverse):
    """*seeds* plus every block that transitively $refs one of them.

    Iterative and visited-guarded, so a $ref cycle terminates.
    """
    seen, stack = set(), list(seeds)
    while stack:
        node = stack.pop()
        if node in seen:
            continue
        seen.add(node)
        stack.extend(reverse.get(node, ()))
    return seen


def classify(changed, sources_dir=None):
    """Split changed paths into propagating seeds, self-only blocks, global.

    A changed schema.yaml propagates to dependents. A changed artifact or
    bblock.json affects that block alone -- artifacts are outputs, not
    inputs, so nothing downstream reads them.
    """
    sources_dir = Path(sources_dir or rs.SOURCES_DIR).resolve()
    # Relative paths are repo-relative, so they resolve against whatever
    # contains _sources -- REPO_ROOT normally, a temp tree under test.
    root = sources_dir.parent
    seeds, self_only = set(), set()
    for raw in changed:
        rel = str(raw).replace("\\", "/").lstrip("./")
        if rel in GLOBAL_PATHS or rel in RESOLUTION_TOOLS:
            return set(), set(), f"{rel} can affect any block"
        path = (root / rel).resolve()
        try:
            path.relative_to(sources_dir)
        except ValueError:
            continue  # outside _sources: cannot reach a generated schema
        if path.name == "schema.yaml":
            if not path.exists():
                return set(), set(), f"{rel} was deleted; dependents unknown"
            seeds.add(path)
        else:
            sibling = path.parent / "schema.yaml"
            if sibling.exists():
                self_only.add(sibling.resolve())
    return seeds, self_only, None


def affected(changed, sources_dir=None):
    """(blocks_to_regenerate, reason_for_all). Exactly one is meaningful."""
    forward, urls = build_forward_graph(sources_dir)
    if urls:
        return ALL, f"a source declares a URL $ref ({urls[0]})"
    seeds, self_only, reason = classify(changed, sources_dir)
    if reason:
        return ALL, reason
    if not seeds and not self_only:
        return [], None
    hit = closure(seeds, build_reverse_graph(forward)) | self_only
    # Match --all's target set exactly: a block with no external $ref and no
    # existing resolvedSchema.json is not one --all writes, so it is not one
    # this may claim either. Traversal still passes THROUGH such a block.
    if sources_dir is None:
        writable = {p.resolve() for p in rs.find_all_resolvable_schemas()}
        hit &= writable
    return sorted(hit), None


def changed_against(base):
    """Paths that differ from *base*, via the merge base."""
    out = subprocess.run(
        ["git", "diff", "--name-only", f"{base}...HEAD"],
        cwd=REPO_ROOT, capture_output=True, text=True, check=True,
    )
    return [line for line in out.stdout.splitlines() if line.strip()]


# ---------------------------------------------------------------------------
# Self-test
# ---------------------------------------------------------------------------

def _write(path, text):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def _synthetic(tmp):
    """A chain, a cycle, and an isolated block."""
    src = tmp / "_sources"
    _write(src / "a/schema.yaml", "type: object\n")
    _write(src / "b/schema.yaml", "allOf:\n- $ref: ../a/schema.yaml\n")
    _write(src / "c/schema.yaml", "allOf:\n- $ref: ../b/schema.yaml\n")
    _write(src / "cyc1/schema.yaml", "allOf:\n- $ref: ../cyc2/schema.yaml\n")
    _write(src / "cyc2/schema.yaml", "allOf:\n- $ref: ../cyc1/schema.yaml\n")
    _write(src / "lonely/schema.yaml", "type: string\n")
    return src


def _check(results, name, got, want):
    ok = got == want
    results.append((name, ok))
    print(f"  {'PASS' if ok else 'FAIL'}  {name}")
    if not ok:
        print(f"        got  {got}")
        print(f"        want {want}")


def _names(paths):
    return sorted(p.parent.name for p in paths)


def self_test():
    print("affected_blocks self-test")
    results = []

    with tempfile.TemporaryDirectory() as td:
        src = _synthetic(Path(td))

        # Multi-hop. A closure that walked only DIRECT dependents would
        # return [a, b] here and look perfectly healthy.
        got, _ = affected(["_sources/a/schema.yaml"], sources_dir=src)
        _check(results, "transitive: editing a reaches b and c",
               _names(got), ["a", "b", "c"])

        # Direction. The walk must go up to dependents, never down into
        # dependencies -- editing c cannot change a or b.
        got, _ = affected(["_sources/c/schema.yaml"], sources_dir=src)
        _check(results, "direction: editing c reaches only c", _names(got), ["c"])

        got, _ = affected(["_sources/cyc1/schema.yaml"], sources_dir=src)
        _check(results, "cycle terminates", _names(got), ["cyc1", "cyc2"])

        got, _ = affected(["_sources/lonely/schema.yaml"], sources_dir=src)
        _check(results, "isolated block reaches only itself", _names(got),
               ["lonely"])

        # An artifact is an output. Nothing downstream reads it, so a change
        # to a's artifact must not drag in b and c.
        got, _ = affected(["_sources/a/resolvedSchema.json"], sources_dir=src)
        _check(results, "artifact edit does not propagate", _names(got), ["a"])

        got, _ = affected(["tools/resolve_schema.py"], sources_dir=src)
        _check(results, "resolution tool reports ALL", got, ALL)

        # A tool the drift workflow never runs cannot move an artifact. This
        # is the case that made the first version useless: treating every
        # tools/ change as a sweep meant most pull requests here got one.
        got, _ = affected(["tools/audit_ig_consistency.py",
                           "_sources/a/schema.yaml"], sources_dir=src)
        _check(results, "non-resolution tool does not force a sweep",
               _names(got), ["a", "b", "c"])

        got, _ = affected(["README.md"], sources_dir=src)
        _check(results, "unrelated file affects nothing", got, [])

        got, _ = affected(["build/anything.json"], sources_dir=src)
        _check(results, "build/ output affects nothing", got, [])

    # The declared tool set against the workflow it is supposed to describe.
    # Without this, adding a tool to the workflow silently stops triggering a
    # sweep for changes to it.
    _check(results, "RESOLUTION_TOOLS matches the workflow and import graph",
           sorted(RESOLUTION_TOOLS), sorted(_derive_resolution_tools()))

    # The real graph. Hard-coded, because the point is to notice if the
    # builder stops seeing real edges.
    got, _ = affected(["_sources/xasProperties/xasFacility/schema.yaml"])
    _check(results, "real repo: xasFacility closure is the known 3-hop chain",
           _names(got),
           ["xasCore", "xasDocument", "xasFacility", "xasGeneratedBy"])

    passed = sum(1 for _, ok in results if ok)
    print(f"\n{passed}/{len(results)} checks passed")
    return passed == len(results)


def drift_test():
    """Seed drift in a DEPENDENT and prove an incremental run catches it.

    This guards the failure that matters: if the closure comes back too
    small, the pull request regenerates the edited block, finds it current,
    and reports success while a dependent's committed artifact still
    describes the old source. That is indistinguishable from a real pass, so
    it has to be provoked deliberately.

    Runs entirely in a copy of the tree. The marker is a property NAME --
    strip_metadata_keys() drops $id, x-jsonld-* and nulls but keeps
    properties, so the name survives into every dependent's artifact.
    """
    print("affected_blocks drift test (seeded drift in a dependent)")
    marker = "xas:driftProbeMarker"
    edited = "_sources/xasProperties/xasFacility/schema.yaml"
    # xasFacility -> xasGeneratedBy -> xasCore -> xasDocument
    dependents = [
        "_sources/xasProperties/xasGeneratedBy",
        "_sources/xasProperties/xasCore",
        "_sources/profiles/cdifCompositeProfile/xasDocument",
    ]
    outside = "_sources/schemaorgProperties/spatialExtent"

    with tempfile.TemporaryDirectory() as td:
        tmp = Path(td)
        print("  copying tree...")
        shutil.copytree(REPO_ROOT / "_sources", tmp / "_sources")
        shutil.copytree(REPO_ROOT / "tools", tmp / "tools")

        outside_before = (tmp / outside / "resolvedSchema.json").read_bytes()

        target = tmp / edited
        schema = yaml.safe_load(target.read_text(encoding="utf-8"))
        # Land it beside the block's own properties, not in $defs, so it has
        # to travel through the same merge every real edit does.
        for branch in schema["allOf"]:
            if isinstance(branch, dict) and "properties" in branch:
                branch["properties"][marker] = {"type": "string"}
                break
        else:
            print("  FAIL  no properties branch to perturb")
            return False
        target.write_text(yaml.safe_dump(schema, sort_keys=False),
                          encoding="utf-8")

        blocks, reason = affected([edited], sources_dir=tmp / "_sources")
        if reason:
            print(f"  FAIL  expected a closure, got ALL ({reason})")
            return False
        print(f"  closure: {_names(blocks)}")

        for schema_path in blocks:
            run = subprocess.run(
                [sys.executable, str(tmp / "tools" / "resolve_schema.py"),
                 "--file", str(schema_path)],
                capture_output=True, text=True,
            )
            if run.returncode != 0:
                print(f"  FAIL  resolve failed for {schema_path}")
                print(run.stderr[-800:])
                return False

        ok = True
        for dep in dependents:
            artifact = tmp / dep / "resolvedSchema.json"
            text = artifact.read_text(encoding="utf-8") if artifact.exists() else ""
            if marker in text:
                print(f"  PASS  drift reached {Path(dep).name}")
            else:
                print(f"  FAIL  drift did NOT reach {Path(dep).name} -- an "
                      "incremental run would report success over real drift")
                ok = False

        # Without this the test would also pass if the closure were "every
        # block", which would defeat the point of computing one.
        if (tmp / outside / "resolvedSchema.json").read_bytes() == outside_before:
            print(f"  PASS  {Path(outside).name} (outside closure) untouched")
        else:
            print(f"  FAIL  {Path(outside).name} was regenerated but is not "
                  "in the closure")
            ok = False
        return ok


def main():
    parser = argparse.ArgumentParser(
        description="Blocks whose generated schemas a change set can move.")
    parser.add_argument("--changed", nargs="*", default=None,
                        help="Repo-relative changed paths")
    parser.add_argument("--base",
                        help="Git ref to diff against (e.g. origin/main)")
    parser.add_argument("--self-test", action="store_true",
                        help="Prove each rule still fires")
    parser.add_argument("--drift-test", action="store_true",
                        help="Seed drift in a dependent and prove it is caught")
    args = parser.parse_args()

    if args.self_test or args.drift_test:
        ok = True
        if args.self_test:
            ok = self_test() and ok
        if args.drift_test:
            print()
            ok = drift_test() and ok
        sys.exit(0 if ok else 1)

    if args.base:
        changed = changed_against(args.base)
    elif args.changed is not None:
        changed = args.changed
    else:
        parser.error("Specify --changed, --base, --self-test or --drift-test")

    blocks, reason = affected(changed)
    if blocks == ALL:
        print(f"# ALL: {reason}", file=sys.stderr)
        print(ALL)
        return
    print(f"# {len(changed)} changed file(s) -> {len(blocks)} block(s) "
          "to regenerate", file=sys.stderr)
    for schema_path in blocks:
        print(schema_path.relative_to(REPO_ROOT).as_posix())


if __name__ == "__main__":
    main()
