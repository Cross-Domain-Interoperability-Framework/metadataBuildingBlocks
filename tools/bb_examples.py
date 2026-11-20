"""Where a building block's examples are -- one definition, three consumers.

``examples.yaml`` is what the OGC postprocessor publishes and validates, so it
is the authoritative list of a block's examples. The ``example*.json`` glob is
a fallback for the blocks that have no ``examples.yaml`` yet (12 of 86 on
2026-11-20).

Globbing alone silently skips any example whose filename does not start with
"example", and two in this repo are registered in an ``examples.yaml`` and
named otherwise: ``xasDocument/CDIF-XAS-Full.json`` and
``xasInstrument/alt_exampleXasInstrument.json``. CI validated both; the local
tools validated neither. That is how ``CDIF-XAS-Full.json`` came to bind
``cdif`` to ``https://cdif.org/profiles/`` -- against ``w3id.org`` in all 95
other declarations -- unnoticed until 2026-11-07.

This logic lived as three copies until 2026-11-20 -- ``find_example_schema_pairs``
in ``validate_examples.py``, ``gather_examples`` in ``validate_shacl.py``, and
three inline globs in ``audit_building_blocks.py`` -- and two had already
drifted: the first read ``examples.yaml``, the second did not. Hence one module.

Kept in ``sync_resolve_schema.py``'s TOOLS because ``validate_examples.py``
imports it at module level, so a domain repo that received that tool without
this one would fail at import. That is deliberate: the alternative is a lazy
import falling back to the glob, which would restore the blind spot silently.
"""
from pathlib import Path

import yaml


def examples_yaml_refs(block_dir: Path) -> list:
    """The .json snippet refs registered in ``block_dir/examples.yaml``, in file order.

    Returns paths that may NOT exist, so whether a dangling ref is an error is
    the caller's call. No caller treats it as one today -- ``gather_examples``
    drops it and no block has one (measured across all 86 on 2026-11-20) -- but
    reporting it needs the unfiltered list, which is why this is separate. A
    missing, unreadable or malformed ``examples.yaml``, or one whose top level is
    not a list, yields ``[]`` rather than raising.
    """
    path = block_dir / "examples.yaml"
    if not path.exists():
        return []
    try:
        entries = yaml.safe_load(path.read_text(encoding="utf-8")) or []
    except Exception:
        return []
    if not isinstance(entries, list):
        return []

    refs = []
    for entry in entries:
        if not isinstance(entry, dict):
            continue
        for snippet in entry.get("snippets", []) or []:
            ref = snippet.get("ref") if isinstance(snippet, dict) else None
            if isinstance(ref, str) and ref.endswith(".json"):
                refs.append(block_dir / ref)
    return refs


def gather_examples(block_dir: Path) -> list:
    """Every example of this block: ``examples.yaml`` refs UNION the ``example*.json`` glob.

    Existing files only, de-duplicated by resolved path and sorted so a report
    order does not depend on which source found a file first.

    Negative-test fixtures are deliberately excluded: they live in ``tests/``
    and are registered in ``tests.yaml``, so neither the non-recursive glob nor
    ``examples.yaml`` reaches them. They are meant to fail.
    """
    found = {}  # resolved path -> original Path; dedupes across both sources

    def add(path: Path):
        if path.exists() and path.suffix == ".json":
            found.setdefault(path.resolve(), path)

    for path in examples_yaml_refs(block_dir):
        add(path)
    for path in block_dir.glob("example*.json"):
        add(path)

    return sorted(found.values())
