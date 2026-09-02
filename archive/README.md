# Archived building blocks

Building blocks retained for reference but **not** part of any active profile or the
`_sources` build tree.

## profiles/cdifCompositeProfile/XASdata

Archived 2026-07-24. Superseded by the six-profile
[`xasDocument`](../_sources/profiles/cdifCompositeProfile/xasDocument/) composite
(conformance URI `https://w3id.org/cdif/xasDocument/1.0`). The two composites
differed only in whether `cdifDataStructure` was included:

- `XASdata` (5 profiles): core + discovery + dataDescription + xasCore + xasOptional
- `xasDocument` (6 profiles): the above + **cdifDataStructure**

An XAS document profile without a byte-level structural mapping (`cdi:isStructuredBy`
+ `cdif:hasPhysicalMapping` on the distribution) can no longer be described as
"conformant to CDIF for XAS"; `xasDocument` requires that mapping. The unique
content that lived under `XASdata/` — the `CHANGES-from-UKDS.md` transformation log,
the `README.md`, the `assets/` diagram, the `tests/` negative-case fixtures, and the
three example instances — was migrated into `xasDocument/` before the move.

## xasXdiTabularTextDataset

Archived 2026-07. It was an orphan — referenced by no schema in `_sources` (the XASdata
profile composes `xasCore`/`xasOptional`, whose `schema:distribution` uses the generic
`dataDownload` block, not this one). It also modeled the tabular data structure with the
DDI-CDI `cdi:` DataStructure vocabulary (`cdi:WideDataStructure` / `cdi:has_DataStructureComponent`
/ `cdi:haslength`) rather than the CDIF `cdif:hasPhysicalMapping` convention used by
`cdifDataType/cdifTabularData`. If XAS needs an XDI-specific tabular block, it should be
reworked to `cdif:hasPhysicalMapping` and wired into the profile before being restored.

## ddiProperties/ddicdiDataStructure, ddiProperties/ddicdiRepresentedVariable (examples only)

Archived 2026-09-02. **The building blocks themselves are still active** — both are
`$ref`d by `ddicdiKeyValueStructure`, `ddicdiPhysicalDataSet`, `ddicdiLogicalRecord` and
`ddicdiDataStructureComponent`. Only their `example*.json` files moved here.

These five files came in as synthetic fixtures (`ec4973e0a`, "Add synthetic examples
exercising every schema option") and were never adopted: unlike every other
`ddiProperties` block, neither `examples.yaml` references them — both still read
`TODO: replace with a JSON-LD example.` — and nothing else in the repo does either. They
were carried along by schema-change sweeps without being reconciled, and all five failed
`validate_examples.py`.

Retiring them takes the JSON Schema gate to **142 passed / 0 failed**. Both blocks are now
without an example, which the `examples.yaml` TODOs already anticipated; anything restored
here must be made to validate and wired into `examples.yaml`.

`_sources/ddiProperties/ddicdiInstanceVariable/exampleDdicdiInstanceVariable.json` is
unreferenced in the same way but **was left in place** — it validates, so it is unwired
rather than broken.
