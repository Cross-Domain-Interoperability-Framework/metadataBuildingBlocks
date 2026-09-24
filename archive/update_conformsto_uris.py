#!/usr/bin/env python3
"""One-time utility: update dcterms:conformsTo in example files to use
canonical w3id BB URIs.

For files with an existing schema:subjectOf / dcterms:conformsTo block,
replaces the conformsTo array with the single canonical w3id URI.

For ECRR profile examples (which lack schema:subjectOf), injects a
CatalogRecord block with conformsTo referencing both the ECRR profile's
w3id URI and the cdifCore BB.
"""

import json
import os
import sys
from collections import OrderedDict
from pathlib import Path

SOURCES_DIR = Path(__file__).resolve().parent.parent / "_sources"

W3ID_BASE = "https://w3id.org/cdif/bbr/metadata"
CDIF_MANDATORY_URI = f"{W3ID_BASE}/cdifProperties/cdifCore"

# BB-level directories whose example files are full metadata instances
# (not snippets) and should get their conformsTo updated.
BB_LEVEL_DIRS = {
    "cdifProperties/cdifCore",
    "DDEproperties/ddeRequired",
    "xasProperties/xasOptional",
    "xasProperties/xasRequired",
}


def compute_w3id_uri(rel_dir: str) -> str:
    """Compute the w3id URI from a directory path relative to _sources/."""
    # Normalise separators
    rel_dir = rel_dir.replace("\\", "/").strip("/")
    return f"{W3ID_BASE}/{rel_dir}"


def detect_indent(file_path: Path) -> int:
    """Detect whether a JSON file uses 2-space or 4-space indent."""
    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            stripped = line.lstrip()
            if stripped and stripped != line:
                indent = len(line) - len(stripped)
                if indent > 0:
                    return indent
    return 4  # default


def update_existing_conformsto(data: dict, w3id_uri: str) -> bool:
    """Update conformsTo in an existing schema:subjectOf block.
    Returns True if a change was made."""
    subject_of = data.get("schema:subjectOf")
    if subject_of is None:
        return False

    # subjectOf could be a list or a single object
    targets = [subject_of] if isinstance(subject_of, dict) else subject_of
    changed = False
    for target in targets:
        if isinstance(target, dict) and "dcterms:conformsTo" in target:
            target["dcterms:conformsTo"] = [{"@id": w3id_uri}]
            changed = True
    return changed


def inject_ecrr_subject_of(data: dict, w3id_uri: str) -> dict:
    """Inject a schema:subjectOf CatalogRecord block into an ECRR example.
    If schema:subjectOf already exists (without conformsTo), converts to
    an array containing both the existing value and the new CatalogRecord.
    Returns the modified data dict with key ordering preserved."""
    catalog_record = OrderedDict([
        ("@type", ["schema:CreativeWork"]),
        ("schema:additionalType", ["dcat:CatalogRecord"]),
        ("dcterms:conformsTo", [
            {"@id": CDIF_MANDATORY_URI},
            {"@id": w3id_uri},
        ]),
        ("schema:sdDatePublished", "2026-03-03"),
    ])

    existing = data.get("schema:subjectOf")
    if existing is not None:
        # Check if existing subjectOf already has a CatalogRecord with conformsTo
        items = existing if isinstance(existing, list) else [existing]
        for item in items:
            if isinstance(item, dict) and "dcterms:conformsTo" in item:
                # Already has conformsTo — update it (idempotent)
                item["dcterms:conformsTo"] = [
                    {"@id": CDIF_MANDATORY_URI},
                    {"@id": w3id_uri},
                ]
                return data
        # Existing subjectOf without conformsTo — wrap both in an array
        if isinstance(existing, list):
            data["schema:subjectOf"] = existing + [catalog_record]
        else:
            data["schema:subjectOf"] = [existing, catalog_record]
        return data

    # Insert schema:subjectOf after schema:url if present, else at end.
    # Rebuild the ordered dict to control key position.
    new_data = OrderedDict()
    inserted = False
    for key, value in data.items():
        new_data[key] = value
        if key == "schema:url" and not inserted:
            new_data["schema:subjectOf"] = catalog_record
            inserted = True
    if not inserted:
        # Try after schema:license
        new_data2 = OrderedDict()
        for key, value in new_data.items():
            new_data2[key] = value
            if key == "schema:license" and not inserted:
                new_data2["schema:subjectOf"] = catalog_record
                inserted = True
        if inserted:
            new_data = new_data2
        else:
            new_data["schema:subjectOf"] = catalog_record
    return new_data


def ensure_context_has_keys(data: dict, is_ecrr: bool) -> None:
    """Ensure @context includes dcterms and dcat prefixes needed for
    conformsTo / CatalogRecord."""
    ctx = data.get("@context")
    if ctx is None:
        return

    # ECRR files use array-style @context: ["https://schema.org/", {...}]
    if isinstance(ctx, list):
        # Find the dict element (second item typically)
        for item in ctx:
            if isinstance(item, dict):
                if "dcterms" not in item:
                    item["dcterms"] = "http://purl.org/dc/terms/"
                if "dcat" not in item:
                    item["dcat"] = "http://www.w3.org/ns/dcat#"
                return
        # No dict found — append one
        ctx.append({
            "dcterms": "http://purl.org/dc/terms/",
            "dcat": "http://www.w3.org/ns/dcat#",
        })
    elif isinstance(ctx, dict):
        if "dcterms" not in ctx:
            ctx["dcterms"] = "http://purl.org/dc/terms/"
        if "dcat" not in ctx:
            ctx["dcat"] = "http://www.w3.org/ns/dcat#"


def process_file(file_path: Path, rel_dir: str, is_ecrr: bool) -> str:
    """Process a single example file. Returns a status message."""
    w3id_uri = compute_w3id_uri(rel_dir)
    indent = detect_indent(file_path)

    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f, object_pairs_hook=OrderedDict)

    if is_ecrr:
        # ECRR: inject subjectOf CatalogRecord
        ensure_context_has_keys(data, is_ecrr=True)
        data = inject_ecrr_subject_of(data, w3id_uri)
        action = "injected subjectOf"
    else:
        # Non-ECRR: update existing conformsTo
        if update_existing_conformsto(data, w3id_uri):
            action = "updated conformsTo"
        else:
            return f"  SKIP (no conformsTo found): {file_path.name}"

    with open(file_path, "w", encoding="utf-8", newline="\n") as f:
        json.dump(data, f, indent=indent, ensure_ascii=False)
        f.write("\n")

    return f"  {action} -> {w3id_uri}: {file_path.name}"


def main():
    updated = 0
    skipped = 0
    errors = 0

    print("Scanning _sources/ for in-scope example files...\n")

    for dirpath, _dirnames, filenames in os.walk(SOURCES_DIR):
        example_files = [f for f in filenames if f.startswith("example") and f.endswith(".json")]
        if not example_files:
            continue

        dir_path = Path(dirpath)
        rel_dir = dir_path.relative_to(SOURCES_DIR).as_posix()

        # Determine if this directory is in scope
        is_profile = rel_dir.startswith("profiles/")
        is_bb_level = rel_dir in BB_LEVEL_DIRS

        if not is_profile and not is_bb_level:
            continue

        is_ecrr = rel_dir.startswith("profiles/ecrrProfiles/")

        for fname in sorted(example_files):
            file_path = dir_path / fname
            try:
                msg = process_file(file_path, rel_dir, is_ecrr)
                print(msg)
                if "SKIP" in msg:
                    skipped += 1
                else:
                    updated += 1
            except Exception as e:
                print(f"  ERROR processing {file_path}: {e}")
                errors += 1

    print(f"\nDone: {updated} updated, {skipped} skipped, {errors} errors")
    return 0 if errors == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
