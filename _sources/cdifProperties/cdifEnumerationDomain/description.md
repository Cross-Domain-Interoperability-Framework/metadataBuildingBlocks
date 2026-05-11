# CDIF Enumeration Domain

A **CDIF Enumeration Domain** documents a codification vocabulary as an enumerated value domain — the set of permissible values a variable may take when those values are drawn from a controlled vocabulary, codelist, statistical classification, or SKOS concept scheme.

This is a CDIF profile of the DDI-CDI `EnumerationDomain` extension point. It is intentionally light at the root level (only `@type` is required) so that any codification — whether expressed as a SKOS `ConceptScheme`, a schema.org `DefinedTermSet`, or an `@id`-only reference to a domain defined elsewhere — can be advertised as a domain with the same shape. The detailed structure of the codification itself lives in the referenced BB (or external resource); this BB only carries the umbrella identity, naming, and intent properties.

## Structure

- `@type` must contain `"cdif:EnumerationDomain"`.
- `@id` — recommended URI for the domain itself.
- `cdi:identifier` — formal `schema:identifier` for the domain.
- `schema:name` — short human label.
- `schema:inDefinedTermSet` — anyOf an inline `skos:ConceptScheme`, an inline `schema:DefinedTermSet`, or an `@id`-only id-reference to a domain defined elsewhere.
- `cdi:purpose` — multilingual `InternationalString` describing intent/use.

## Relationship to other BBs

CDIF Enumeration Domain is the **abstract umbrella**; concrete codification BBs (e.g. the DDI-CDIF `CodeList` or `StatisticalClassification`) provide the actual content. Use this BB at points in the data-description graph where any codification will do; pin the specific codification BB when the value domain must be of a particular kind.
