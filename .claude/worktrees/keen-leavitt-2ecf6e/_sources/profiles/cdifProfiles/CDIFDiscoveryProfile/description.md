## CDIF Discovery Metadata Profile

Profile for the schema.org implementation of the [Cross Domain Interoperability Framework](https://cross-domain-interoperability-framework.github.io/cdifbook/metadata/schemaorgimplementation.html#implementation-of-metadata-content-items) (CDIF) discovery profile. Composes cdifCore with discovery-oriented properties for dataset search, indexing, and cataloguing.

### Composition

- **cdifCore** — all required and optional core metadata properties (name, identifier, dateModified, license/conditionsOfAccess, url/distribution, creator, publisher, keywords, subjectOf with conformsTo)
- **Discovery properties** (defined in this profile):
  - `schema:measurementTechnique` — technique, technology, or methodology used for measurement (string or DefinedTerm array)
  - `schema:variableMeasured` — what the dataset measures (VariableMeasured or StatisticalVariable array)
  - `schema:spatialCoverage` — geographic extent (SpatialExtent array, supporting GeoCoordinates, GeoShape with bounding box, and named places)
  - `schema:temporalCoverage` — temporal extent (TemporalExtent array, supporting ISO 8601 intervals and structured time:ProperInterval)
  - `dqv:hasQualityMeasurement` — quality measurements (QualityMeasure array, W3C DQV)
- **Additional context prefixes**: `geosparql`, `dqv`, `cdi` (added to the cdifCore required `schema`, `dcterms`, `dcat`, `prov`)

### Conformance

Metadata conforming to this profile declares conformance to both `https://w3id.org/cdif/core/1.0` and `https://w3id.org/cdif/discovery/1.0` via `dcterms:conformsTo` in the `schema:subjectOf` catalog record.

### SHACL validation

The Discovery profile inherits cdifCore SHACL shapes and adds:

**Violation-level** (from cdifCore):
- `@id` must be an IRI
- `schema:name`, `schema:identifier`, `schema:dateModified` required
- `schema:license` or `schema:conditionsOfAccess` required
- `schema:url` or `schema:distribution` required
- CatalogRecord must have `dcterms:conformsTo`, `schema:about`, `dcat:CatalogRecord` additionalType

**Warning-level** (from cdifCore):
- `schema:description`, `schema:creator`, `schema:keywords` recommended
- Keywords must not contain commas (individual keywords should be array items)

**Info-level** (Discovery profile):
- `schema:datePublished`, `schema:sameAs`, `schema:contributor`, `schema:provider`
- Distribution should be DataDownload or WebAPI
- `schema:citation` discouraged (maxCount 0) — use `schema:relatedLink` or `dcterms:bibliographicCitation` instead

**Building block shapes** validate nested types:
- DataDownload requires `schema:contentUrl`
- Person/Organization require name or identifier
- DefinedTerm requires name, identifier, or termCode
- SpatialExtent Place must have geo or name
- Action/EntryPoint requires target with urlTemplate

### Examples

- `exampleCDIFDiscoveryMinimal.json` — minimal valid Discovery record (required properties only)
- `exampleCDIFDiscovery.json` — typical Discovery record with recommended properties
- `exampleCDIFDiscoveryComplete.json` — comprehensive record exercising all Discovery properties

Additional validated examples (26+) from diverse sources (GeoCodes, NCEI NOAA, Copernicus CDS, Harvard Dataverse, Borealis, PANGAEA, ODIS, ESIP) are in the [Discovery repository](https://github.com/Cross-Domain-Interoperability-Framework/Discovery/tree/main/examples).

### Comparison with ESIP Science on Schema.org

See [CDIF-Discovery-vs-SOSO-comparison.md](https://github.com/Cross-Domain-Interoperability-Framework/Discovery/blob/main/CDIF-Discovery-vs-SOSO-comparison.md) for a detailed property-by-property comparison with the ESIP Science on Schema.org (SOSO) v1.3 Dataset guide and SHACL shapes.
