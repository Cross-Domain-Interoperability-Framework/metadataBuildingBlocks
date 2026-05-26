## CDIF Core Metadata Properties

Defines the core properties for any CDIF metadata record, implementing the schema.org-based [Cross Domain Interoperability Framework](https://cross-domain-interoperability-framework.github.io/cdifbook/metadata/schemaorgimplementation.html#implementation-of-metadata-content-items) (CDIF) metadata model.

### Required properties
- `@id`, `@type`, `@context` (JSON-LD structural)
- `schema:name` -- descriptive name for the resource
- `schema:identifier` -- primary identifier (string or PropertyValue)
- `schema:dateModified` -- last update date (ISO 8601)
- `schema:license` or `schema:conditionsOfAccess` -- access/use terms
- `schema:url` or `schema:distribution` -- how to obtain the resource
- `schema:subjectOf` -- metadata catalog record with `dcterms:conformsTo`

### Optional core properties
- `schema:description` -- summary text
- `schema:additionalType` -- non-schema.org type identifiers
- `schema:sameAs` -- alternate identifiers
- `schema:version` -- version number/string
- `schema:inLanguage` -- content language
- `schema:datePublished` -- publication date
- `schema:relatedLink` -- typed links to related resources
- `schema:publishingPrinciples` -- maintenance/persistence policies
- `schema:keywords` -- subject keywords (strings or DefinedTerms)
- `schema:creator` -- authors (ordered `@list`)
- `schema:contributor` -- other contributing parties (with roles via agentInRole)
- `schema:publisher` -- publishing party
- `schema:provider` -- distribution provider
- `schema:funding` -- funding sources
- `prov:wasGeneratedBy` -- provenance: how the resource was created
- `prov:wasDerivedFrom` -- provenance: source datasets
