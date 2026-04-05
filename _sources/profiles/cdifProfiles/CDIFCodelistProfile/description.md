## CDIF Codelist Profile

A CDIF profile for controlled vocabulary codelists implemented as SKOS ConceptSchemes.

### ConceptScheme requirements
- Must have a globally unique, resolvable `@id` URI
- Must have at least one `skos:prefLabel`
- Must declare top concepts via `skos:hasTopConcept`
- Must have `schema:identifier`, `schema:dateModified`, and either `schema:license` or `schema:conditionsOfAccess` (CDIF Core metadata properties take precedence over equivalent dcterms properties)

### Concept requirements (beyond base SKOS)
- Must have a globally unique, resolvable `@id` URI
- Must have `skos:inScheme` linking to the containing ConceptScheme
- Must have at least one `skos:prefLabel` (at most one per language)
- Must have at least one `skos:definition`
- `skos:notation` is optional but must be unique within the scheme if used
- `skos:altLabel` and other SKOS properties are optional

### Bidirectional hierarchy requirement

CDIF codelists require concept hierarchies to be expressed in **both directions** — `skos:narrower` and `skos:broader` must both be explicit:

- **`skos:narrower`** is needed because the JSON-LD tree structure is rooted at `skos:hasTopConcept`. Without `skos:narrower`, child concepts cannot be reached by traversing the JSON document tree from the root. This is the property used to build the inline hierarchy in the JSON serialization.

- **`skos:broader`** is needed for upward navigation and for building display trees in applications. Many SKOS consumers (vocabulary browsers, classification tools, thesaurus managers) expect `skos:broader` to be present and use it as the primary hierarchy traversal property.

Any concept that appears as a value of `skos:narrower` on another concept **must** also declare `skos:broader` pointing back to its parent. Top concepts (those listed in `skos:hasTopConcept`) should not have `skos:broader` within the scheme.

This constraint is enforced by:
- **JSON Schema**: inline concepts within `skos:narrower` require `skos:broader` (via `allOf` with `required`)
- **SHACL**: `narrowerImpliesBroaderShape` uses a SPARQL target to find concepts that are objects of `skos:narrower` and requires `skos:broader` with `minCount 1`

### Validation
- JSON Schema validates structure and required properties (including bidirectional hierarchy)
- SHACL shapes validate RDF constraints including `sh:uniqueLang` on `skos:prefLabel`, `sh:class skos:ConceptScheme` on `skos:inScheme` targets, and the `skos:narrower` implies `skos:broader` rule

This profile aligns with the approach described in ['Modelling of Eurostat's Statistical Classifications in ShowVoc'](https://cros.ec.europa.eu/book-page/modeling-eurostats-statistical-classifications-showvoc).
