## Spatial Extent properties

Defines a set of properties for use describing the spatial extent of a resource for the schema.org implementation of the [Cross Domain Interoperability Framework](https://cross-domain-interoperability-framework.github.io/cdifbook/metadata/schemaorgimplementation.html#implementation-of-metadata-content-items) (CDIF) discovery profile. Based on [ESIP science on schema.org recommendations](https://github.com/ESIPFed/science-on-schema.org/blob/main/guides/Dataset.md#spatial-coverage), with [option from Ocean Info Hub](https://book.oceaninfohub.org/thematics/spatial/README.html#simple-geosparql-wkt).

### Defined properties

- **@type** — must be schema:Place
- **schema:name** — place names or DefinedTerms with place name and URI
- **schema:geo** — point location (schema:GeoCoordinates with latitude/longitude), bounding box (schema:GeoShape with box), or curvilinear trace (schema:GeoShape with line)
- **geosparql:hasGeometry** — geographic extent using WKT geometry (geosparql:asWKT with optional coordinate reference system)

### Dependencies

- [definedTerm](../definedTerm/) — controlled vocabulary term for place names
