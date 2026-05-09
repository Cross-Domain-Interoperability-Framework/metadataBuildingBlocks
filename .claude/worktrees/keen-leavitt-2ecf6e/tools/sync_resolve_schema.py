#!/usr/bin/env python3
"""
Sync shared tool scripts from the canonical copies in metadataBuildingBlocks/tools/
to all domain building block repositories.

Files synced:
  - resolve_schema.py
  - regenerate_schema_json.py

Usage:
    python tools/sync_resolve_schema.py          # dry-run (show what would be copied)
    python tools/sync_resolve_schema.py --apply  # actually copy the files

The script looks for sibling repos relative to this repo's parent directory.
Configure TARGETS and TOOLS below if your directory layout differs.
"""

import argparse
import hashlib
import shutil
import sys
from pathlib import Path

TOOLS_DIR = Path(__file__).resolve().parent
REPO_ROOT = TOOLS_DIR.parent  # metadataBuildingBlocks/

# Tools to sync (filename in tools/)
TOOLS = [
    "resolve_schema.py",
    "regenerate_schema_json.py",
]

# Target repos — paths relative to this repo root
TARGETS = [
    ("../../usgin/ddeBuildingBlocks", "tools"),
    ("../../usgin/ecrrBuildingBlocks", "tools"),
    ("../../usgin/geochemBuildingBlocks", "tools"),
]


def file_hash(path: Path) -> str:
    return hashlib.md5(path.read_bytes()).hexdigest()


def get_version(path: Path) -> str:
    for line in path.read_text().splitlines()[:6]:
        if "VERSION:" in line:
            return line.split("VERSION:")[-1].strip()
    return "unknown"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--apply", action="store_true", help="Actually copy files (default: dry-run)")
    args = parser.parse_args()

    any_diff = False

    for tool_name in TOOLS:
        canonical = TOOLS_DIR / tool_name
        if not canonical.exists():
            print(f"WARNING: Canonical {tool_name} not found, skipping", file=sys.stderr)
            continue

        canonical_hash = file_hash(canonical)
        version = get_version(canonical)

        print(f"{tool_name}  (version: {version}, hash: {canonical_hash[:12]})")

        for rel_path, tools_dir in TARGETS:
            target_dir = (REPO_ROOT / rel_path / tools_dir).resolve()
            repo_name = (REPO_ROOT / rel_path).resolve().name
            target = target_dir / tool_name

            if not target_dir.exists():
                print(f"  SKIP {repo_name}: {target_dir} not found")
                continue

            if target.exists():
                target_hash = file_hash(target)
                if target_hash == canonical_hash:
                    print(f"  OK   {repo_name}")
                    continue
                else:
                    any_diff = True
                    print(f"  DIFF {repo_name}")
            else:
                any_diff = True
                print(f"  NEW  {repo_name}")

            if args.apply:
                shutil.copy2(canonical, target)
                print(f"       -> copied")

        print()

    if any_diff and not args.apply:
        print("Run with --apply to copy canonical versions to all targets.")

    return 0


if __name__ == "__main__":
    sys.exit(main())
