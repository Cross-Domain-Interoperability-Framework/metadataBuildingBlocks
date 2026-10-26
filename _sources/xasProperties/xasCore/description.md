## Required Fields for XAS data

Extends CDIF mandatory metadata with required XAS-specific properties. Same structure as xasOptional but adds `@type` constraints (requires `schema:Dataset`; `schema:Product` optional) and stricter cardinality requirements on instrument components and measurement techniques.

### Key requirements

- **@type** — must include `schema:Dataset`; `schema:Product` is optional (no root-level property depends on it)
- **schema:subjectOf** — XAS subject descriptors (element, edge)
- **prov:wasGeneratedBy** — required, with at least one activity. Any CDIF provenance activity may appear; at least one must be an `xas:analysisevent` (xasGeneratedBy) using XAS instruments with NXsource (type, probe) and NXmonochromator (type, d_spacing, reflection) components, plus sample object
- **schema:distribution** — requires at least one DataDownload typed as `cdi:PhysicalDataSet`, `cdi:TabularTextDataSet` or `cdi:StructuredDataSet`, conforming to the XDI specification or a NeXus application definition
- **schema:measurementTechnique** — required: DefinedTerms for XAS (PaNET, the schema's `default`) and measurement mode (NXxas)
- **schema:keywords** — no XAS requirement; base CDIF keywords apply. DefinedTerms for the absorption edge (XDI dictionary) and target element (SWEET) are recommended
