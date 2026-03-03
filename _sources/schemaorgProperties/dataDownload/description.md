## DataDownload properties

Defines a set of properties for use describing a DataDownload as a distribution for a resource. For use in the schema.org implementation of the [Cross Domain Interoperability Framework](https://cross-domain-interoperability-framework.github.io/cdifbook/metadata/schemaorgimplementation.html#implementation-of-metadata-content-items) (CDIF) discovery profile. The download is implicitly a single file that is accessible on the web via URL. CDIF integration profile will extend these to describe the data structure in the file.

### Defined properties

- **@id** — identifier for this download
- **@type** — must include schema:DataDownload
- **schema:name** — name of the download
- **schema:contentUrl** — URL to the downloadable content
- **schema:encodingFormat** — MIME type with extension indicating serialization scheme
- **spdx:checksum** — checksum value calculated from content representation (spdx:Checksum with algorithm and checksumValue)
- **schema:provider** — party who maintains this distribution option

### Dependencies

- [person](../person/) — person agent for provider
- [organization](../organization/) — organization agent for provider
