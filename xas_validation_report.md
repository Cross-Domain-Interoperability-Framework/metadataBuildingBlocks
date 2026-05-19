# Validation report: CODATA XAS JSON-LD vs CDIFDataDescriptionProfile

Source: https://raw.githubusercontent.com/codata/cdi-xas/refs/heads/main/resources/Fe_c3d.001-nx-testschemaorg-cdi-v2-1.jsonLD

## Preprocessing

- JSON-LD framing applied (target @type: schema:Dataset). Original doc uses `@graph` with 7 nodes; framing produced a Dataset-rooted tree.
- For SHACL, the doc's `@context` mapping `schema: https://schema.org/` was normalized to `http://schema.org/` so shapes targeting `http://schema.org/Dataset` would actually fire. Without this rewrite SHACL would vacuously report Conforms=True (zero shapes match).

## JSON Schema validation: 25 errors

Categorized:

### Missing required field (11)
- `(root)`: 'schema:dateModified' is a required property
- `schema:subjectOf`: 'schema:additionalType' is a required property
- `schema:variableMeasured/0`: '@type' is a required property
- `schema:variableMeasured/0`: '@type' is a required property
- `schema:variableMeasured/0`: 'schema:name' is a required property
- `schema:variableMeasured/1`: '@type' is a required property
- `schema:variableMeasured/1`: '@type' is a required property
- `schema:variableMeasured/1`: 'schema:name' is a required property
- `schema:variableMeasured/3`: '@type' is a required property
- `schema:variableMeasured/3`: '@type' is a required property
- `schema:variableMeasured/3`: 'schema:name' is a required property

### Scalar where array required (7)
- `prov:wasGeneratedBy`: {'@id': '_:b0', '@type': ['schema:Event', 'nx:analysisEvent'], 'schema:additionalProperty': {'@id': '_:b1', '@type': 'schema:PropertyValue', 'schema:propertyID': 'nx:edge_energy', 'schema:unitText': '???', 'schema:value'
- `schema:contributor`: {'@id': '_:b10', '@type': 'schema:Role', 'schema:contributor': {'@id': 'https://ror.org/aps', '@type': 'schema:Organization', 'schema:identifier': 'https://ror.org/aps', 'schema:name': 'APS'}, 'schema:roleName': 'Facilit
- `schema:distribution`: {'@id': '_:b11', '@type': ['schema:DataDownload', 'PhysicalDataSet'], 'allowsDuplicates': False, 'has': {'@id': '_:b12', '@type': 'PhysicalRecordSegment', 'has': {'@id': '_:b13', '@type': 'PhysicalSegmentLayout', 'format
- `schema:license`: 'To be FAIR must include license/usage constraint information' is not of type 'array'
- `schema:measurementTechnique`: {'@id': '_:b28', '@type': 'schema:DefinedTerm', 'schema:identifier': 'https://w3id.org/geochem/1.0/analyticalmethod/xrayabsorptionspectrometry', 'schema:inDefinedTermSet': 'https://w3id.org/geochem/1.0/analyticalmethod/m
- `schema:variableMeasured/2/schema:alternateName`: 'fluorescence intensity' is not of type 'array'
- `schema:variableMeasured/2/schema:propertyID`: 'nx:fluorescenceIntensityConcept' is not of type 'array'

### Other (2)
- `schema:keywords/0`: {'@id': '_:b26', '@type': 'schema:DefinedTerm', 'schema:identifier': 'https://xas.org/vocab/absorptionedge/k', 'schema:inDefinedTermSet': 'https://xas.org/vocab/absorptionedge', 's
- `schema:keywords/1`: {'@id': '_:b27', '@type': 'schema:DefinedTerm', 'schema:identifier': 'URI for iron (CCPAC?)', 'schema:inDefinedTermSet': 'URI for element vocabualry', 'schema:name': 'Iron', 'schem

### @type must be an array (CDIF requires arrays even for single types) (1)
- `schema:subjectOf/@type`: 'schema:Dataset' is not of type 'array'

### @type array missing required type constant (4)
- `schema:subjectOf/dcterms:conformsTo`: [{'@id': 'http://example.org/base/CDIF_basic_1.0'}, {'@id': 'nx:nxxasCDIF'}] does not contain items matching the given schema
- `schema:subjectOf/dcterms:conformsTo`: [{'@id': 'http://example.org/base/CDIF_basic_1.0'}, {'@id': 'nx:nxxasCDIF'}] does not contain items matching the given schema
- `schema:subjectOf/dcterms:conformsTo`: [{'@id': 'http://example.org/base/CDIF_basic_1.0'}, {'@id': 'nx:nxxasCDIF'}] does not contain items matching the given schema
- `schema:variableMeasured/2/@type`: ['InstanceVariable', 'schema:PropertyValue'] does not contain items matching the given schema

## SHACL validation (advanced/SPARQL targets enabled): Conforms = False

```
Validation Report
Conforms: False
Results (4):
Constraint Violation in MinCountConstraintComponent (http://www.w3.org/ns/shacl#MinCountConstraintComponent):
	Severity: sh:Violation
	Source Shape: cdifd:dateModifiedProperty
	Focus Node: nx:fe_c3d.001
	Result Path: schema1:dateModified
	Message: Date of most recent update to resource content is required, using ISO8601 format with at least a year and a month.
Constraint Violation in MinCountConstraintComponent (http://www.w3.org/ns/shacl#MinCountConstraintComponent):
	Severity: sh:Violation
	Source Shape: cdifd:nameProperty
	Focus Node: nx:metadata.fe_c3d.001
	Result Path: schema1:name
	Message: a name for the person must be provided, and have a length of at least 3 characters.
Constraint Violation in MinCountConstraintComponent (http://www.w3.org/ns/shacl#MinCountConstraintComponent):
	Severity: sh:Violation
	Source Shape: cdifd:resourceIdentifierProperty
	Focus Node: nx:metadata.fe_c3d.001
	Result Path: schema1:identifier
	Message: An identifier for the documented resource must be provided
Constraint Violation in MinCountConstraintComponent (http://www.w3.org/ns/shacl#MinCountConstraintComponent):
	Severity: sh:Violation
	Source Shape: cdifd:rightsProperty
	Focus Node: nx:metadata.fe_c3d.001
	Result Path: [ sh:alternativePath ( schema1:license schema1:conditionsOfAccess ) ]
	Message: To meet the requirements for FAIR data, information about licenses or other security, usage, or access limitations must be described
```

## Headline takeaways

- The doc is not conformant to CDIFDataDescriptionProfile. Mostly a profile mismatch — it was written to a different (NXxas/DDI-CDI flavored) shape.
- Top issues that would unblock most of the JSON Schema errors:
  - Use `"@type": [...]` (array form) consistently. The doc has many scalar `@type` values; CDIF schemas require arrays.
  - Wrap singletons like `schema:license`, `schema:contributor`, `schema:distribution`, `schema:measurementTechnique` in arrays.
  - `schema:alternateName`, `schema:propertyID` inside `schema:variableMeasured`: must be arrays.
  - `schema:subjectOf.dcterms:conformsTo`: entries need to be objects shaped per CDIF Reference (with `schema:url`, `@type` containing `dcat:Relationship`), not bare `@id` strings.
  - `schema:subjectOf` requires `schema:additionalType` (e.g. `dcat:CatalogRecord`).
- SHACL caught 4 missing-field violations on top of the JSON Schema findings:
  - `nx:fe_c3d.001` missing `schema:dateModified`.
  - The metadata record `nx:metadata.fe_c3d.001` missing `schema:name`, `schema:identifier`, and license/access info.
- Namespace note: the doc uses `https://schema.org/` (with https). CDIF profile uses `http://schema.org/`. RDF treats these as different URIs, so any SHACL/SPARQL pass against the unnormalized doc would silently report no errors. Decide whether to switch the doc to `http://schema.org/` (matches CDIF examples) or update CDIF shapes to accept both. JSON Schema validation isn't affected by this because it matches on the literal JSON keys.
