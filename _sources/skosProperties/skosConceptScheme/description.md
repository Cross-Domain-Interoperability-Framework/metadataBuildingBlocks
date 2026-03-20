## SKOS Concept Scheme

JSON Schema for validating a [SKOS ConceptScheme](https://www.w3.org/TR/skos-reference/#schemes) in native JSON-LD form, based on the [W3C SKOS vocabulary](https://www.w3.org/2004/02/skos/core.rdf).

### Root object (skos:ConceptScheme)

The root object must have `@type` including `skos:ConceptScheme`, a `skos:prefLabel`, and at least one `skos:hasTopConcept`. An `@id` or `skos:notation` is required for identification.

Optional scheme-level properties include `skos:definition`, `skos:notation`, documentary notes (`skos:scopeNote`, `skos:historyNote`, `skos:changeNote`, `skos:editorialNote`, `skos:example`), and Dublin Core metadata (`dcterms:creator`, `dcterms:created`, `dcterms:modified`, `dcterms:license`).

### Nested concepts (skos:Concept)

Concepts within `skos:hasTopConcept` (and recursively in `skos:narrower`) must have `@type` including `skos:Concept` and a `skos:prefLabel`. Concepts support:

- **Labels**: `skos:prefLabel`, `skos:altLabel`, `skos:hiddenLabel` (strings or language-tagged values)
- **Notations**: `skos:notation` (classification codes)
- **Hierarchy**: `skos:broader`, `skos:narrower` (inline concepts or `@id` references)
- **Association**: `skos:related`
- **Mapping**: `skos:exactMatch`, `skos:closeMatch`, `skos:broadMatch`, `skos:narrowMatch`, `skos:relatedMatch` (cross-scheme `@id` references)
- **Scheme membership**: `skos:inScheme`, `skos:topConceptOf`
- **Notes**: all documentary note properties

### Collections

The schema also defines `skos:Collection` (unordered groupings with `skos:member`) and `skos:OrderedCollection` (ordered groupings with `skos:memberList` using the JSON-LD `@list` construct).

### Language-tagged values

Labels and notes can be simple strings or JSON-LD value objects with `@value` and `@language` for multilingual support.
