## CDIF Concept or Term

A shared union shape used wherever a CDIF property accepts a controlled-vocabulary value. The property's value can be:

1. **A SKOS concept referenced by URI** — an object carrying just an `@id` pointing at a `skos:Concept` in some published vocabulary.
2. **A `schema:DefinedTerm`** — the schema.org DefinedTerm shape inherited from the `schemaorgProperties/definedTerm` building block, used to inline name/identifier/termCode alongside a `inDefinedTermSet` pointer.
3. **An inline `cdif:Concept`** — the `cdifConcept` shape from the CDIF ConceptScheme profile, used to inline a complete concept definition (preferred label, alternate labels, definition, broader/narrower, etc.) directly in the metadata record.

### When to use

`$ref` this building block from any property that previously accepted the inlined `cdifConceptOrTerm` `anyOf` union. The intent is to consolidate that duplicated shape — every CDIF building block that needs a concept-or-term value should reference this single definition rather than redefining it locally.

### Migration note

Prior to 2026-06-05, this union appeared as a local `$defs.cdifConceptOrTerm` entry inside nine separate building-block schemas (`cdifInstanceVariable`, `cdifRepresentedVariable`, `cdifDataStructureComponent`, `cdifReference`, `cdifPhysicalMapping`, `cdifStatistics`, `cdifOpenApi`, `cdifCore`, `cdifDiscovery`). Each of those local `$defs` is now a single-line `$ref` delegation to this BB, so existing in-document `#/$defs/cdifConceptOrTerm` references continue to resolve unchanged.
