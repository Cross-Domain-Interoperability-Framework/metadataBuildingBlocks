## CDIF Discovery Metadata Profile

Profile for the schema.org implementation of the [Cross Domain Interoperability Framework](https://cross-domain-interoperability-framework.github.io/cdifbook/metadata/schemaorgimplementation.html#implementation-of-metadata-content-items) (CDIF) discovery profile. Composes cdifCore with discovery-oriented properties.

### Composition

- **cdifCore** -- all required and optional core metadata properties
- **Discovery properties** (defined inline):
  - `schema:measurementTechnique` -- technique used for measurement (string or DefinedTerm)
  - `schema:variableMeasured` -- what the dataset measures (VariableMeasured)
  - `schema:spatialCoverage` -- geographic extent (SpatialExtent)
  - `schema:temporalCoverage` -- temporal extent (TemporalExtent)
  - `dqv:hasQualityMeasurement` -- quality measurements (QualityMeasure)

### Conformance

Metadata conforming to this profile declares conformance to `cdif/core/1.0/` and `cdif/discovery/1.0/` via `dcterms:conformsTo` in the `schema:subjectOf` catalog record.
