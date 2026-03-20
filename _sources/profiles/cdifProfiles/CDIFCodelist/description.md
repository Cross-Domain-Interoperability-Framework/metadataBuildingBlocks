## CDIF Codelist Profile

A CDIF profile for controlled vocabulary codelists implemented as SKOS ConceptSchemes.

### ConceptScheme requirements
- Must have a globally unique, resolvable `@id` URI
- Must have at least one `skos:prefLabel`
- Must declare top concepts via `skos:hasTopConcept`

### Concept requirements (beyond base SKOS)
- Must have a globally unique, resolvable `@id` URI
- Must have `skos:inScheme` linking to the containing ConceptScheme
- Must have at least one `skos:prefLabel` (at most one per language)
- Must have at least one `skos:definition`
- Must declare `skos:broader` if the concept is not a top concept in a hierarchical scheme
- `skos:notation` is optional but must be unique within the scheme if used
- `skos:altLabel`, `skos:narrower`, and other SKOS properties are optional

### Validation
- JSON Schema validates structure and required properties
- SHACL shapes validate RDF constraints including `sh:uniqueLang` on `skos:prefLabel` and `sh:class skos:ConceptScheme` on `skos:inScheme` targets

This profile aligns with the approach described in ['Modelling of Eurostat's Statistical Classifications in ShowVoc'](https://cros.ec.europa.eu/book-page/modeling-eurostats-statistical-classifications-showvoc).
