# Archived building blocks

Building blocks retained for reference but **not** part of any active profile or the
`_sources` build tree.

## xasXdiTabularTextDataset

Archived 2026-07. It was an orphan — referenced by no schema in `_sources` (the XASdata
profile composes `xasCore`/`xasOptional`, whose `schema:distribution` uses the generic
`dataDownload` block, not this one). It also modeled the tabular data structure with the
DDI-CDI `cdi:` DataStructure vocabulary (`cdi:WideDataStructure` / `cdi:has_DataStructureComponent`
/ `cdi:haslength`) rather than the CDIF `cdif:hasPhysicalMapping` convention used by
`cdifDataType/cdifTabularData`. If XAS needs an XDI-specific tabular block, it should be
reworked to `cdif:hasPhysicalMapping` and wired into the profile before being restored.
