## SKOS Concept

JSON Schema for validating a [SKOS Concept](https://www.w3.org/TR/skos-reference/#concepts) in native JSON-LD form.

A concept must have `@type` including `skos:Concept` and a `skos:prefLabel`. An `@id` or `skos:notation` is required for identification.

### Labels
- `skos:prefLabel` — preferred label (one per language)
- `skos:altLabel` — alternative labels (acronyms, abbreviations)
- `skos:hiddenLabel` — labels for search, not display

Labels can be simple strings or language-tagged JSON-LD value objects (`@value`/`@language`).

### Hierarchy and relations
- `skos:broader`, `skos:narrower` — hierarchical relations (inline concepts or `@id` references, recursive)
- `skos:related` — associative relations

### Cross-scheme mappings
- `skos:exactMatch`, `skos:closeMatch`, `skos:broadMatch`, `skos:narrowMatch`, `skos:relatedMatch` — `@id` references to concepts in other schemes

### Scheme membership
- `skos:inScheme` — concept scheme(s) this concept belongs to
- `skos:topConceptOf` — scheme(s) for which this is a top concept

### Documentary notes
- `skos:definition`, `skos:scopeNote`, `skos:note`, `skos:historyNote`, `skos:changeNote`, `skos:editorialNote`, `skos:example`
