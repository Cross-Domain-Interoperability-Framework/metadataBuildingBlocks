## SKOS Collection

JSON Schema for [SKOS Collection](https://www.w3.org/TR/skos-reference/#collections) and [OrderedCollection](https://www.w3.org/TR/skos-reference/#collections) in JSON-LD form.

### Collection

An unordered grouping of concepts. Must have `@type` including `skos:Collection`, a `skos:prefLabel`, and at least one `skos:member`. Members can be inline concept objects, `@id` references, or nested collections.

### OrderedCollection

A subclass of Collection where member ordering is meaningful. Must have `@type` including `skos:OrderedCollection`, a `skos:prefLabel`, and `skos:memberList` using the JSON-LD `@list` construct.

Both types reference the `skosConcept` building block for concept items and `LanguageTaggedValue` for multilingual labels.
