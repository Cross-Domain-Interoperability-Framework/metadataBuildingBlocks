## Required Fields for XAS data

Extends CDIF mandatory metadata with required XAS-specific properties. Same structure as xasOptional but adds `@type` constraints (schema:Dataset + schema:Product) and stricter cardinality requirements on instrument components, measurement techniques, and keywords.

### Key requirements

- **@type** — must include both `schema:Dataset` and `schema:Product`
- **schema:subjectOf** — XAS subject descriptors (element, edge)
- **prov:wasGeneratedBy** — cdifProvActivity activity requiring XAS instruments with NXsource (type, probe) and NXmonochromator (type, d_spacing, reflection) components, plus sample object
- **schema:distribution** — requires at least one DataDownload typed as `cdi:PhysicalDataset` conforming to the XDI specification
- **schema:measurementTechnique** — requires DefinedTerms for XAS (PaNET) and measurement mode (NXxas)
- **schema:keywords** — requires DefinedTerms from both the XDI dictionary (absorption edge) and SWEET ontology (target element)
