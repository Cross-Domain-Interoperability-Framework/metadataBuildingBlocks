# CDIF LocatorMapping

Locates a variable's value(s) within a **structured** (hierarchical) dataset such as
XML or JSON, via a locator expression (XPath, JSONPath, JSON Pointer, etc.). DDI-CDI
`LocatorMapping`.

- `cdi:locator` (required) — the locator expression
- `cdif:formats_InstanceVariable` — reference to the `schema:variableMeasured` variable this locates

Used as the item type for `cdif:hasPhysicalMapping` on a distribution typed
`cdi:StructuredDataSet`, where a column index / text mapping does not apply.
