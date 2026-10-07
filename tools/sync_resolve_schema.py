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
# geochemBuildingBlocks moved from usgin to amds-ldeo on 2026-08-19 and the old repository was
# archived. This list was not updated, so every sync since then wrote to the archived clone and
# reported success: the live repository never received them. That is how the canonical
# find_self_referential_defs guard -- which catches a $defs entry whose body $refs itself, a
# RecursionError at the consumer rather than a failure here -- reached none of the targets.
# dde and ecrr are still on usgin remotes and stay as they are.
TARGETS = [
    ("../../usgin/ddeBuildingBlocks", "tools"),
    ("../../usgin/ecrrBuildingBlocks", "tools"),
    ("../../amds-ldeo/geochemBuildingBlocks", "tools"),
]


def file_hash(path: Path) -> str:
    """Hash the file's CONTENT, normalizing CRLF, so a line-ending difference is not drift.

    Hashed raw bytes until 2026-10-07. On Windows `core.autocrlf=true` overrides the repos' own
    `* text=auto eol=lf`, so a target's working copy holds CRLF while this one holds LF and an
    IDENTICAL file hashes differently: the run printed DIFF and `--apply` rewrote a correct file,
    whole-file, every time git happened to touch it. Measured that day on ddeBuildingBlocks --
    reported DIFF, 0 differing content lines, and the rewrite had to be reverted by hand.

    The cost of the old behaviour was not just noise: a DIFF that is always present is a DIFF
    nobody reads, which is how a real divergence would have gone unnoticed.
    """
    return hashlib.md5(path.read_bytes().replace(b"\r\n", b"\n")).hexdigest()


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
