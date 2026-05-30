#!/usr/bin/env python3
"""Sync mBB-generated artifacts to release repos' reviewRevision202606 branches.

For each (release_repo, mbb_source) pair:
  - Copy mbb_source/resolvedSchema.json -> release_repo/<StructuredSchema>
  - Run validate_shacl --emit-shapes mbb_source -> release_repo/<Rules.shacl>
  - For each mbb_source/example*.json, copy -> release_repo/examples/<name>

Does NOT touch: implementation guides, frame.jsonld, FrameAndValidate.py,
README, LICENSE, AGENTS.md, or release-only examples.

Usage:
    python tools/sync_release_repos.py                # dry-run (default)
    python tools/sync_release_repos.py --apply        # actually copy
    python tools/sync_release_repos.py --apply --repo profile-core   # one repo
"""
import argparse
import shutil
import subprocess
import sys
from pathlib import Path

MBB_ROOT = Path(__file__).resolve().parent.parent
CDIF_ROOT = MBB_ROOT.parent

# (release_repo_name, mbb_source_relpath, structured_schema_filename, shacl_filename)
REPOS = [
    ("doc-corediscovery", "_sources/profiles/cdifCompositeProfile/CoreDiscovery",
     "CDIFDiscoveryDocStructuredSchema.json", "discoveryDocRules.shacl"),
    ("doc-discoverydatadescription", "_sources/profiles/cdifCompositeProfile/DiscoveryDataDescription",
     "CDIFDataDescriptionProfileStructuredSchema.json", "dataDescriptionRules.shacl"),
    ("doc-discoverydatadescriptionstructure", "_sources/profiles/cdifCompositeProfile/DiscoveryDataDescriptionStructure",
     "CDIFDiscoveryDataDescriptionStructureProfileStructuredSchema.json",
     "discoveryDataDescriptionStructureRules.shacl"),
    ("profile-codelist", "_sources/profiles/cdifProfile/cdifCodelist",
     "CDIFCodelistProfileStructuredSchema.json", "rules.shacl"),
    ("profile-conceptscheme", "_sources/profiles/cdifProfile/cdifConceptScheme",
     "cdifConceptSchemeStructuredSchema.json", "conceptSchemeRules.shacl"),
    ("profile-core", "_sources/profiles/cdifProfile/cdifCore",
     "cdifCoreStructuredSchema.json", "coreRules.shacl"),
    ("profile-datadescription", "_sources/profiles/cdifProfile/cdifDataDescription",
     "cdifDataDescriptionStructuredSchema.json", "dataDescriptionRules.shacl"),
    ("profile-discovery", "_sources/profiles/cdifProfile/cdifDiscovery",
     "cdifDiscoveryStructuredSchema.json", "discoveryRules.shacl"),
    # Newly-populated repos (had no schema/SHACL/examples before 2026-05-30):
    ("profile-datastructure", "_sources/profiles/cdifProfile/cdifDataStructure",
     "cdifDataStructureStructuredSchema.json", "dataStructureRules.shacl"),
    ("profile-manifest", "_sources/profiles/cdifProfile/cdifManifest",
     "cdifManifestStructuredSchema.json", "manifestRules.shacl"),
    ("profile-provenance", "_sources/profiles/cdifProfile/cdifProvenance",
     "cdifProvenanceStructuredSchema.json", "provenanceRules.shacl"),
]


def file_differs(src: Path, dst: Path) -> bool:
    if not dst.exists():
        return True
    return src.read_bytes() != dst.read_bytes()


def sync_repo(repo: str, src_rel: str, schema_name: str, shacl_name: str, apply: bool) -> dict:
    src = MBB_ROOT / src_rel
    release = CDIF_ROOT / repo
    examples_dir = release / "examples"

    result = {"repo": repo, "schema": "—", "shacl": "—", "examples": []}

    # 1. Schema
    mbb_schema = src / "resolvedSchema.json"
    rel_schema = release / schema_name
    if not mbb_schema.exists():
        result["schema"] = f"SKIP: {mbb_schema} not found"
    elif file_differs(mbb_schema, rel_schema):
        if apply:
            shutil.copy2(mbb_schema, rel_schema)
        result["schema"] = "WOULD COPY" if not apply else "copied"
    else:
        result["schema"] = "identical"

    # 2. SHACL via validate_shacl --emit-shapes
    tmp_shacl = release / (shacl_name + ".tmp")
    rel_shacl = release / shacl_name
    cmd = [sys.executable, str(MBB_ROOT / "tools" / "validate_shacl.py"),
           str(src), "--emit-shapes", str(tmp_shacl)]
    proc = subprocess.run(cmd, capture_output=True, text=True, cwd=MBB_ROOT)
    if proc.returncode != 0 or not tmp_shacl.exists():
        result["shacl"] = f"FAIL: {proc.stderr.strip()[:120]}"
    else:
        if file_differs(tmp_shacl, rel_shacl):
            if apply:
                shutil.move(str(tmp_shacl), str(rel_shacl))
                result["shacl"] = "emitted+copied"
            else:
                result["shacl"] = "WOULD COPY"
                tmp_shacl.unlink()
        else:
            result["shacl"] = "identical"
            tmp_shacl.unlink()

    # 3. Examples (mBB example*.json -> release/examples/)
    examples_dir.mkdir(exist_ok=True)
    for ex in sorted(src.glob("example*.json")):
        target = examples_dir / ex.name
        if file_differs(ex, target):
            action = "new" if not target.exists() else "overwrite"
            if apply:
                shutil.copy2(ex, target)
            result["examples"].append(f"{ex.name} ({action}{' WOULD' if not apply else ''})")

    return result


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--apply", action="store_true", help="Actually copy files (default: dry-run)")
    ap.add_argument("--repo", help="Only process this one release repo")
    args = ap.parse_args()

    repos = REPOS if not args.repo else [r for r in REPOS if r[0] == args.repo]
    if args.repo and not repos:
        print(f"Unknown repo: {args.repo}", file=sys.stderr)
        sys.exit(1)

    print(f"Mode: {'APPLY' if args.apply else 'DRY-RUN'}")
    print()
    for repo, src_rel, schema, shacl in repos:
        r = sync_repo(repo, src_rel, schema, shacl, args.apply)
        print(f"=== {r['repo']} ===")
        print(f"  schema:   {r['schema']}")
        print(f"  shacl:    {r['shacl']}")
        if r["examples"]:
            print(f"  examples: {len(r['examples'])}")
            for ex in r["examples"]:
                print(f"    - {ex}")
        else:
            print(f"  examples: all identical or none in mBB source")
        print()


if __name__ == "__main__":
    main()
