#!/usr/bin/env python3
"""One-shot path rewriter for the profile reorg.

Maps:
  cdifProperties/{cdifCore,cdifCodelist,cdifDataDescription,cdifDataStructure,
                  cdifArchive,cdifProvenance}/...
    -> profiles/cdifProfile/<same>/...
  cdifProperties/<other>/... -> cdifDataType/<other>/...
  profiles/cdifProfiles/CDIFDiscoveryProfile     -> profiles/cdifCompositeProfile/BasicDiscovery
  profiles/cdifProfiles/CDIFDataDescriptionProfile -> profiles/cdifCompositeProfile/BasicDataDescription
  profiles/cdifProfiles/CDIFDataStructureProfile -> profiles/cdifCompositeProfile/DataDescriptionWithStructure
  profiles/cdifProfiles/CDIFxasProfile           -> profiles/cdifCompositeProfile/XASdata
  profiles/cdifProfiles/CDIFcompleteProfile      -> profiles/cdifCompositeProfile/cdifComplete
  profiles/cdifProfiles/CDIFCodelistProfile      -> profiles/archive/CDIFCodelistProfile

Rewrites both:
  - Relative $ref values in schema.yaml / resolved schemas (recomputed for the
    source file's new location).
  - Absolute repo paths (e.g. "_sources/profiles/cdifProfiles/...") in any text.

Run from repo root.
"""
from pathlib import Path
import re
import sys

REPO = Path(__file__).resolve().parent.parent
SOURCES = REPO / "_sources"

MOVED_TO_PROFILE = {
    "cdifCore", "cdifCodelist", "cdifDataDescription",
    "cdifDataStructure", "cdifArchive", "cdifProvenance",
}
COMPOSITE_RENAMES = {
    "CDIFDiscoveryProfile": "BasicDiscovery",
    "CDIFDataDescriptionProfile": "BasicDataDescription",
    "CDIFDataStructureProfile": "DataDescriptionWithStructure",
    "CDIFxasProfile": "XASdata",
    "CDIFcompleteProfile": "cdifComplete",
}
ARCHIVED = {"CDIFCodelistProfile"}


def map_old_repo_path_to_new(old_rel: str) -> str | None:
    """Given an old _sources-relative path like
    'cdifProperties/cdifCore/schema.yaml' or
    'profiles/cdifProfiles/CDIFDiscoveryProfile/...', return the new
    _sources-relative path. None means no mapping applies.
    """
    # cdifProperties/<bb>/<rest>
    m = re.match(r"^cdifProperties/([^/]+)(/.*)?$", old_rel)
    if m:
        bb = m.group(1)
        rest = m.group(2) or ""
        if bb in MOVED_TO_PROFILE:
            return f"profiles/cdifProfile/{bb}{rest}"
        return f"cdifDataType/{bb}{rest}"
    # profiles/cdifProfiles/<composite>/<rest>
    m = re.match(r"^profiles/cdifProfiles/([^/]+)(/.*)?$", old_rel)
    if m:
        comp = m.group(1)
        rest = m.group(2) or ""
        if comp in COMPOSITE_RENAMES:
            return f"profiles/cdifCompositeProfile/{COMPOSITE_RENAMES[comp]}{rest}"
        if comp in ARCHIVED:
            return f"profiles/archive/{comp}{rest}"
    return None


def _segment_remap(old_rel_to_sources: str) -> str | None:
    """Try the structural remap; if no rule applies return None."""
    return map_old_repo_path_to_new(old_rel_to_sources)


def rewrite_relative_ref(ref: str, src_file: Path) -> str:
    """Find what the ref *meant* (resolve against either new or old src
    location), map to its new _sources-relative location, then emit a
    relative path from src_file's new location.
    """
    if "://" in ref or ref.startswith("#"):
        return ref
    path_part, _, frag = ref.partition("#")
    if not path_part:
        return ref

    # Candidate src directories: the new one (already moved), plus any old
    # location it was renamed from. For files at
    #   _sources/profiles/cdifProfile/<bb>/schema.yaml
    # the old location was
    #   _sources/cdifProperties/<bb>/schema.yaml
    # so resolving the ref against the OLD parent recovers the original
    # target. Same logic for composite renames and the archive move.
    try:
        rel = src_file.parent.relative_to(SOURCES).as_posix()
    except ValueError:
        return ref
    candidate_parents = [src_file.parent]
    # profiles/cdifProfile/<bb> -> cdifProperties/<bb>
    m = re.match(r"^profiles/cdifProfile/([^/]+)$", rel)
    if m:
        candidate_parents.append(SOURCES / "cdifProperties" / m.group(1))
    # cdifDataType/<bb> -> cdifProperties/<bb>
    m = re.match(r"^cdifDataType/([^/]+)$", rel)
    if m:
        candidate_parents.append(SOURCES / "cdifProperties" / m.group(1))
    # profiles/cdifCompositeProfile/<new> -> profiles/cdifProfiles/<old>
    m = re.match(r"^profiles/cdifCompositeProfile/([^/]+)$", rel)
    if m:
        new_name = m.group(1)
        for old, new in COMPOSITE_RENAMES.items():
            if new == new_name:
                candidate_parents.append(SOURCES / "profiles" / "cdifProfiles" / old)
                break
    # profiles/archive/<x> -> profiles/cdifProfiles/<x>
    m = re.match(r"^profiles/archive/([^/]+)$", rel)
    if m:
        candidate_parents.append(SOURCES / "profiles" / "cdifProfiles" / m.group(1))

    new_rel_to_sources = None
    src_moved = len(candidate_parents) > 1  # old location candidate added => src moved
    for cand in candidate_parents:
        target = (cand / path_part).resolve()
        try:
            old_rel = target.relative_to(SOURCES).as_posix()
        except ValueError:
            continue
        mapped = _segment_remap(old_rel)
        if mapped is not None:
            new_rel_to_sources = mapped
            break
        # If the ref points to a real un-renamed file on disk:
        #  - if src didn't move, keep the ref unchanged
        #  - if src moved, the relative ref is now wrong; recompute from new src
        if target.exists():
            if not src_moved:
                return ref
            new_rel_to_sources = old_rel
            break
    if new_rel_to_sources is None:
        return ref

    # Recompute relative from src_file's NEW location.
    try:
        depth = len(src_file.parent.relative_to(SOURCES).parts)
        new_rel = Path(*[".."] * depth, new_rel_to_sources).as_posix()
    except ValueError:
        new_rel = (SOURCES / new_rel_to_sources).as_posix()
    if frag:
        new_rel += f"#{frag}"
    return new_rel


REF_PATTERNS = [
    # YAML / JSON $ref values, possibly quoted. Require that "$ref" is NOT
    # preceded by a letter or colon — i.e. it is its own token, not part of
    # a longer property name like "oas:$ref".
    re.compile(r"""(?<![A-Za-z0-9:_])(\$ref\s*['"]?\s*:\s*['"]?)([^'"\s\]{}]+)"""),
]


def process_yaml_or_json(p: Path) -> bool:
    """Rewrite $ref values in YAML/JSON-ish text. Returns True if changed."""
    try:
        text = p.read_text(encoding="utf-8")
    except Exception:
        return False
    orig = text

    def sub_ref(m):
        prefix, ref = m.group(1), m.group(2)
        new_ref = rewrite_relative_ref(ref, p)
        return prefix + new_ref

    for pat in REF_PATTERNS:
        text = pat.sub(sub_ref, text)

    # Also rewrite any absolute repo paths anywhere in the text.
    # We match "_sources/<old>" / "/_sources/<old>" / "metadataBuildingBlocks/_sources/<old>".
    def sub_abs(m):
        old_rel = m.group(2)
        new_rel = map_old_repo_path_to_new(old_rel)
        if new_rel is None:
            return m.group(0)
        return m.group(1) + new_rel

    text = re.sub(
        r"(_sources/)((?:cdifProperties|profiles/cdifProfiles)/[A-Za-z0-9_\-./#]+)",
        sub_abs, text,
    )

    # Rewrite w3id.org bblock identifier URLs:
    #   .../cdif/bbr/metadata/cdifProperties/<bb>      -> profiles/cdifProfile/<bb>
    #                                                   or cdifDataType/<bb>
    #   .../cdif/bbr/metadata/profiles/cdifProfiles/<id> -> profiles/cdifCompositeProfile/<newId>
    # The identifier is the bblock id, which for composites used to drop the
    # trailing "Profile" (CDIFDiscoveryProfile -> CDIFDiscovery). New ids
    # match the new directory names exactly.
    ID_RENAMES = {
        "CDIFDiscovery": "BasicDiscovery",
        "CDIFDataDescription": "BasicDataDescription",
        "CDIFDataStructure": "DataDescriptionWithStructure",
        "CDIFxas": "XASdata",
        "CDIFcomplete": "cdifComplete",
        "CDIFCodelist": "CDIFCodelistProfile",  # archived
    }

    def sub_url_props(m):
        bb = m.group(2)
        if bb in MOVED_TO_PROFILE:
            return m.group(1) + f"profiles/cdifProfile/{bb}"
        return m.group(1) + f"cdifDataType/{bb}"

    def sub_url_composite(m):
        old_id = m.group(2)
        new_id = ID_RENAMES.get(old_id)
        if new_id is None:
            return m.group(0)
        if old_id == "CDIFCodelist":
            return m.group(1) + f"profiles/archive/{new_id}"
        return m.group(1) + f"profiles/cdifCompositeProfile/{new_id}"

    text = re.sub(
        r"(cdif/bbr/metadata/)cdifProperties/([A-Za-z][A-Za-z0-9_]*)",
        sub_url_props, text,
    )
    text = re.sub(
        r"(cdif/bbr/metadata/)profiles/cdifProfiles/([A-Za-z][A-Za-z0-9_]*)",
        sub_url_composite, text,
    )

    # Rewrite plain "(cdifProperties)" parenthetical mentions in bblock.json
    # abstracts: "cdifReference (cdifDataType)" -> "(cdifProfile)" if it's a
    # module BB, else "(cdifDataType)".
    def sub_paren(m):
        bb = m.group(1)
        if bb in MOVED_TO_PROFILE:
            return f"{bb} (cdifProfile)"
        return f"{bb} (cdifDataType)"

    text = re.sub(
        r"([a-zA-Z][a-zA-Z0-9]*) \(cdifProperties\)",
        sub_paren, text,
    )

    if text != orig:
        p.write_text(text, encoding="utf-8")
        return True
    return False


def main():
    targets = []
    for ext in ("*.yaml", "*.yml", "*.json", "*.jsonld", "*.md", "*.shacl"):
        targets.extend(SOURCES.rglob(ext))
    # Also rewrite root-level docs/configs that might pin paths.
    for ext in ("*.yaml", "*.yml", "*.md"):
        targets.extend((REPO / ".github" / "workflows").rglob(ext))
    targets.extend((REPO / "tools").rglob("*.py"))
    targets.append(REPO / "README.md")

    changed = []
    for p in targets:
        if not p.is_file():
            continue
        if "/build/" in p.as_posix() or "/_build/" in p.as_posix():
            continue
        if process_yaml_or_json(p):
            changed.append(p.relative_to(REPO).as_posix())

    print(f"Rewrote {len(changed)} files:")
    for c in changed:
        print(f"  {c}")


if __name__ == "__main__":
    main()
