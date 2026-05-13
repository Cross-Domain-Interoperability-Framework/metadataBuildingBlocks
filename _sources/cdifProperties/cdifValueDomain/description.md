# CDIF Value Domain

A **CDIF Value Domain** describes the set of values a variable may take — either *substantive* (subject-matter values of interest) or *sentinel* (processing or missing-value codes like SAS `.R`, SPSS `999`, "not applicable", etc.).

This is a CDIF profile of the DDI-CDI `ValueDomain` family. A single node is **one of**:

- `cdif:SubstantiveValueDomain` — the real values a variable measures.
- `cdif:SentinelValueDomain` — codes that flag missing, refused, not-applicable, or otherwise non-substantive observations.

The schema discriminates the two via `@type` (a `oneOf` over the two `$defs`).

## Structure

Each subclass carries the same shape:

| Property | Type | Notes |
|---|---|---|
| `@type` | array | Must contain `cdif:SubstantiveValueDomain` or `cdif:SentinelValueDomain` |
| `@id` | string | Optional IRI for the domain node |
| `cdif:takesValuesFrom` | anyOf | Inline [cdifEnumerationDomain](../cdifEnumerationDomain/) or `{@id}` reference |
| `cdif:displayLabel` | string | Short human-readable label (multilingual via repeat) |
| `cdif:recommendedDataType` | array | One or more `xsd:` type tokens (e.g. `xsd:decimal`, `xsd:date`) drawn from the enum in `$defs/xsdDataType` |

`@type` is required, plus **at least one of** `cdif:takesValuesFrom` or `cdif:recommendedDataType` — a value domain that pins neither an enumeration nor a recommended data type is not informative.

## Relationship to other BBs

- **[cdifEnumerationDomain](../cdifEnumerationDomain/)** — `cdif:takesValuesFrom` refs this BB when the value set is a controlled vocabulary, codelist, or classification.
- **[cdifInstanceVariable](../cdifInstanceVariable/)** — references a CDIF Value Domain to describe permissible values for the variable.
- **[ddicdiValueDomain](../../ddiProperties/ddicdiValueDomain/)** — the native DDI-CDI version (covers ValueAndConceptDescription, conceptual domain pointers, platformType). This CDIF profile is intentionally slimmer.

## Notes

- Where DDI-CDI uses `cdi:ValueAndConceptDescription` for value/concept description, CDIF uses `skos:Concept` (via [skosConcept](../../skosProperties/skosConcept/)) as the general pattern. This BB does not yet expose a description pointer; add `cdif:isDescribedBy` → `skosConcept` if/when needed.
- The `xsdDataType` enum is the same fixed list used elsewhere in CDIF for advertising recommended XML Schema datatypes.
