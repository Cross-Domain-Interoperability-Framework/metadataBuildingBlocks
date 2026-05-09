## CDIF Complete Metadata Profile

Profile assembling building blocks for the full schema.org implementation of the [Cross Domain Interoperability Framework](https://cross-domain-interoperability-framework.github.io/cdifbook/metadata/schemaorgimplementation.html#implementation-of-metadata-content-items) (CDIF). Composes cdifCore with discovery, data description, archive distribution, and provenance extensions.

### Composition

- **cdifCore** -- required and optional core metadata properties applicable to any resource
- **Discovery properties** -- measurement technique, variables measured, spatial/temporal coverage, quality measurements
- **Extended provenance** (`cdifProvActivity`) -- full provenance activities with instruments, agents, temporal bounds, methodology, action chaining, and domain-specific extension properties
- **Data description extensions** -- distribution items may include CDIF data description properties:
  - `cdifTabularData` -- for delimited or fixed-width tabular text files (CSV, TSV), with CSVW properties and physical column mappings
  - `cdifDataCube` -- for multi-dimensional structured datasets (NetCDF, HDF5), with locator-based physical mappings
- **Archive distribution** (`cdifArchiveDistribution`) -- for archive files (ZIP, tar.gz) containing multiple component files described via `schema:hasPart`, each typed as `schema:MediaObject` with optional data description extensions
- **WebAPI distribution** -- for API-based data access with `schema:potentialAction` describing query endpoints and result data descriptions

### Distribution types

Each `schema:distribution` item must match one of:

1. **Single-file DataDownload** -- a directly accessible file with optional tabular/dataCube data description
2. **Archive DataDownload** -- an archive file with `schema:hasPart` listing component files
3. **WebAPI** -- an API endpoint with `schema:potentialAction` describing available queries and their result format

### Conformance

Metadata conforming to this profile declares conformance to: `cdif/core/1.0/`, `cdif/discovery/1.0/`, `cdif/data_description/1.0/`, `cdif/manifest/1.0/`, and `cdif/provenance/1.0/`.
