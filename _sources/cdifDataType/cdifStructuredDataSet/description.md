# CDIF StructuredDataSet

Dataset-level marker for a **structured** (hierarchical) dataset such as XML or JSON. A
subclass of DDI-CDI `PhysicalDataSet`; in CDIF it is carried on a `schema:DataDownload`
distribution dual-typed `cdi:StructuredDataSet`.

This building block is an **attribute mixin** (no `@type` of its own). It has no
tabular-layout attributes; instead, each measured variable is located in the document
with a [`cdifLocatorMapping`](../cdifLocatorMapping/) value of `cdif:hasPhysicalMapping`
(an `XPath`/`JSONPath`-style locator), rather than a column index or text mapping.

`cdif:encoding` records the serialization (e.g., `application/json`, `application/xml`) — `cdif:`
because the DDI-CDI `ControlledVocabularyEntry` type is simplified here to a plain charset string.
