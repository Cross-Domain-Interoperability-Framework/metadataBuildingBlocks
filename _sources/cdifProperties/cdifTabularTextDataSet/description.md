# CDIF TabularTextDataSet

Dataset-level physical layout of a delimited or fixed-width **text** dataset (CSV, TSV,
fixed-width). A subclass of DDI-CDI `PhysicalDataSet`; in CDIF it is carried on a
`schema:DataDownload` distribution dual-typed `cdi:TabularTextDataSet`.

This building block is an **attribute mixin** (no `@type` of its own) — the
`cdi:TabularTextDataSet` token lives on the distribution. The CDIF Data Description
profile merges these attributes onto a distribution via an `if @type contains
cdi:TabularTextDataSet then …` branch.

Defines the DDI-CDI `TabularTextDataSet` attributes (`cdi:delimiter`, `cdi:hasHeader`,
`cdi:headerRowCount`, `cdi:quoteCharacter`, `cdi:lineTerminator`, `cdi:isDelimited`,
`cdi:isFixedWidth`, `cdi:skipRows`, `cdi:trim`, etc.). Per-field physical mappings for a
tabular text dataset are [`cdifTextMapping`](../cdifTextMapping/) values of
`cdif:hasPhysicalMapping`.
