## Optional Fields for XAS data

Extends CDIF mandatory metadata with optional XAS-specific properties. Composes cdifCore with cdifProvActivity-based provenance (via xasGeneratedBy pattern), XAS subject descriptors, data distribution with XDI conformance, measurement technique DefinedTerms, and element/edge keywords.

### Key properties

- **schema:subjectOf** — XAS subject descriptors (element, edge)
- **prov:wasGeneratedBy** — cdifProvActivity activity extended with XAS instrument wrappers (source, monochromator with d-spacing/reflection), sample object, and facility
- **schema:distribution** — data download with XDI specification conformance
- **schema:measurementTechnique** — DefinedTerms for XAS technique and measurement mode
- **schema:keywords** — DefinedTerms for absorption edge (XDI dictionary) and target element (SWEET ontology)
