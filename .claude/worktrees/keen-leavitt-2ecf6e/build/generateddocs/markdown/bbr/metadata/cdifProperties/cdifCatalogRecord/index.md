
# CDIF Catalog Record (Schema)

`cdif.bbr.metadata.cdifProperties.cdifCatalogRecord` *v0.2*

properties for a CDIF metadata-about-metadata catalog record node, typed as dcat:CatalogRecord. Defines properties: @type, schema:additionalType, @id, schema:about, dcterms:conformsTo, schema:maintainer, schema:sdDatePublished, schema:includedInDataCatalog. Uses building blocks: identifier (schemaorgProperties), person (schemaorgProperties), organization (schemaorgProperties).

[*Status*](http://www.opengis.net/def/status): Under development

## Description

## CDIF Catalog Record properties

Defines properties for a metadata-about-metadata catalog record node in the schema.org implementation of the [Cross Domain Interoperability Framework](https://cross-domain-interoperability-framework.github.io/cdifbook/metadata/schemaorgimplementation.html#implementation-of-metadata-content-items) (CDIF) discovery profile. The record is typed as both `schema:Dataset` and `dcat:CatalogRecord` (via `schema:additionalType`).

## Examples

### Example CDIF catalog record (metadata about metadata).
Example instance of properties for a catalog record describing information about the metadata record itself, typed as dcat:CatalogRecord.
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "ex": "https://example.org/",
    "xsd": "http://www.w3.org/2001/XMLSchema#",
    "dcterms": "http://purl.org/dc/terms/",
    "dcat": "http://www.w3.org/ns/dcat#"
  },
  "@type": [
    "schema:Dataset"
  ],
  "schema:additionalType": [
    "dcat:CatalogRecord"
  ],
  "@id": "ex:URIforMetadata3575",
  "schema:about": {
    "@id": "ex:URIforNode2246"
  },
  "dcterms:conformsTo": [
    {
      "@id": "https://w3id.org/cdif/core/1.0"
    }
  ],
  "schema:maintainer": {
    "@id": "https://orcid.org/3333-4442-9456-9347",
    "@type": [
      "schema:Person"
    ],
    "schema:name": "Goodge, Alice",
    "schema:alternateName": "Metadata curator",
    "schema:affiliation": {
      "@id": "https://ror.org/04jpmwt24",
      "@type": [
        "schema:Organization"
      ],
      "schema:additionalType": [
        "schema:Consortium"
      ],
      "schema:name": "Big Wildlife Consortium",
      "schema:alternateName": "BWC",
      "schema:description": "Description of organizatioan BWC",
      "schema:identifier": {
        "@type": [
          "schema:PropertyValue"
        ],
        "schema:propertyID": "https://registry.identifiers.org/registry/ror",
        "schema:url": "https://ror.org/04jpmwt24"
      },
      "schema:sameAs": [
        "ISNI 0000 0000 9427 2533",
        "Wikidata Q4904147"
      ]
    },
    "schema:contactPoint": {
      "@type": [
        "schema:ContactPoint"
      ],
      "schema:email": "goodgea@bwc.org"
    },
    "schema:identifier": {
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": "https://registry.identifiers.org/registry/orcid",
      "schema:url": "https://orcid.org/3333-4442-9456-9347"
    }
  },
  "schema:sdDatePublished": "2025-10-24",
  "schema:includedInDataCatalog": {
    "@id": "https://ror.org/04sfkyrt24",
    "@type": [
      "schema:DataCatalog"
    ],
    "schema:name": "Global Wildlife Aggregator",
    "schema:url": "http://example.com/wildlifecatalog",
    "schema:identifier": {
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": "https://registry.identifiers.org/registry/ror",
      "schema:value": "04sfkyrt24",
      "schema:url": "https://ror.org/04sfkyrt24"
    }
  }
}

```

#### jsonld
```jsonld
{
  "@context": [
    {
      "schema": "http://schema.org/",
      "dcat": "http://www.w3.org/ns/dcat#",
      "dcterms": "http://purl.org/dc/terms/"
    },
    "https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifProperties/cdifCatalogRecord/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ex": "https://example.org/",
      "xsd": "http://www.w3.org/2001/XMLSchema#",
      "dcterms": "http://purl.org/dc/terms/",
      "dcat": "http://www.w3.org/ns/dcat#"
    }
  ],
  "@type": [
    "schema:Dataset"
  ],
  "schema:additionalType": [
    "dcat:CatalogRecord"
  ],
  "@id": "ex:URIforMetadata3575",
  "schema:about": {
    "@id": "ex:URIforNode2246"
  },
  "dcterms:conformsTo": [
    {
      "@id": "https://w3id.org/cdif/core/1.0"
    }
  ],
  "schema:maintainer": {
    "@id": "https://orcid.org/3333-4442-9456-9347",
    "@type": [
      "schema:Person"
    ],
    "schema:name": "Goodge, Alice",
    "schema:alternateName": "Metadata curator",
    "schema:affiliation": {
      "@id": "https://ror.org/04jpmwt24",
      "@type": [
        "schema:Organization"
      ],
      "schema:additionalType": [
        "schema:Consortium"
      ],
      "schema:name": "Big Wildlife Consortium",
      "schema:alternateName": "BWC",
      "schema:description": "Description of organizatioan BWC",
      "schema:identifier": {
        "@type": [
          "schema:PropertyValue"
        ],
        "schema:propertyID": "https://registry.identifiers.org/registry/ror",
        "schema:url": "https://ror.org/04jpmwt24"
      },
      "schema:sameAs": [
        "ISNI 0000 0000 9427 2533",
        "Wikidata Q4904147"
      ]
    },
    "schema:contactPoint": {
      "@type": [
        "schema:ContactPoint"
      ],
      "schema:email": "goodgea@bwc.org"
    },
    "schema:identifier": {
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": "https://registry.identifiers.org/registry/orcid",
      "schema:url": "https://orcid.org/3333-4442-9456-9347"
    }
  },
  "schema:sdDatePublished": "2025-10-24",
  "schema:includedInDataCatalog": {
    "@id": "https://ror.org/04sfkyrt24",
    "@type": [
      "schema:DataCatalog"
    ],
    "schema:name": "Global Wildlife Aggregator",
    "schema:url": "http://example.com/wildlifecatalog",
    "schema:identifier": {
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": "https://registry.identifiers.org/registry/ror",
      "schema:value": "04sfkyrt24",
      "schema:url": "https://ror.org/04sfkyrt24"
    }
  }
}
```

#### ttl
```ttl
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix ex: <https://example.org/> .
@prefix schema1: <http://schema.org/> .

ex:URIforMetadata3575 a schema1:Dataset ;
    dcterms:conformsTo <https://w3id.org/cdif/core/1.0> ;
    schema1:about ex:URIforNode2246 ;
    schema1:additionalType "dcat:CatalogRecord" ;
    schema1:includedInDataCatalog <https://ror.org/04sfkyrt24> ;
    schema1:maintainer <https://orcid.org/3333-4442-9456-9347> ;
    schema1:sdDatePublished "2025-10-24" .

<https://orcid.org/3333-4442-9456-9347> a schema1:Person ;
    schema1:affiliation <https://ror.org/04jpmwt24> ;
    schema1:alternateName "Metadata curator" ;
    schema1:contactPoint [ a schema1:ContactPoint ;
            schema1:email "goodgea@bwc.org" ] ;
    schema1:identifier [ a schema1:PropertyValue ;
            schema1:propertyID "https://registry.identifiers.org/registry/orcid" ;
            schema1:url "https://orcid.org/3333-4442-9456-9347" ] ;
    schema1:name "Goodge, Alice" .

<https://ror.org/04jpmwt24> a schema1:Organization ;
    schema1:additionalType "schema:Consortium" ;
    schema1:alternateName "BWC" ;
    schema1:description "Description of organizatioan BWC" ;
    schema1:identifier [ a schema1:PropertyValue ;
            schema1:propertyID "https://registry.identifiers.org/registry/ror" ;
            schema1:url "https://ror.org/04jpmwt24" ] ;
    schema1:name "Big Wildlife Consortium" ;
    schema1:sameAs "ISNI 0000 0000 9427 2533",
        "Wikidata Q4904147" .

<https://ror.org/04sfkyrt24> a schema1:DataCatalog ;
    schema1:identifier [ a schema1:PropertyValue ;
            schema1:propertyID "https://registry.identifiers.org/registry/ror" ;
            schema1:url "https://ror.org/04sfkyrt24" ;
            schema1:value "04sfkyrt24" ] ;
    schema1:name "Global Wildlife Aggregator" ;
    schema1:url "http://example.com/wildlifecatalog" .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
type: object
description: see https://github.com/Cross-Domain-Interoperability-Framework/Discovery/issues/13
  for discussion on how to make assertion about the sample registration and metadata
  distinct from statements about the physical object
properties:
  '@type':
    type: array
    items:
      type: string
    contains:
      const: schema:Dataset
    minItems: 1
  schema:additionalType:
    type: array
    description: additional type assertions for the catalog record node. dcat:CatalogRecord
      is required.
    items:
      type: string
    contains:
      const: dcat:CatalogRecord
    minItems: 1
  '@id':
    type: string
    description: identifier for the metadata record
  schema:about:
    type: object
    properties:
      '@id':
        type: string
        description: this must be the @id value of the node containing the resource
          description metadata
  dcterms:conformsTo:
    type: array
    items:
      type: object
      properties:
        '@id':
          type: string
          description: uri for specifications that this metadata record conforms to
    minItems: 1
    description: uri for specifications that this metadata record conforms to. Minimimally
      should specify uri for CDIF discovery profile.
  schema:maintainer:
    description: Identification of the agent that maintains the metadata, with contact
      information. Should include person name and affiliation, or position name and
      affiliation, or just organization name. e-mail address is preferred contact
      information.
    anyOf:
    - $ref: '#/$defs/Person'
    - $ref: '#/$defs/Organization'
  schema:sdDatePublished:
    description: date of most recent update to the metadata content
    type: string
    format: date
  schema:includedInDataCatalog:
    type: object
    description: identify the source for the origin the metadata record.
    properties:
      '@id':
        type: string
        description: identifier for the graph node.
      '@type':
        default: schema:DataCatalog
        type: array
        items:
          type: string
        contains:
          const: schema:DataCatalog
        minItems: 1
      schema:name:
        type: string
      schema:url:
        type: string
        format: uri
        description: locator to access a landing page for the collection or catalog
      schema:identifier:
        $ref: '#/$defs/Identifier'
        description: identifier for the collection or catalog; use identifier_type
          to provide information on identifier scheme and context for identifier
required:
- schema:about
- dcterms:conformsTo
- schema:additionalType
- '@type'
- '@id'
$defs:
  Identifier:
    $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/identifier/schema.yaml
  Person:
    $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/person/schema.yaml
  Organization:
    $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/organization/schema.yaml
x-jsonld-prefixes:
  schema: http://schema.org/
  ex: https://example.org/
  xsd: http://www.w3.org/2001/XMLSchema#
  dcterms: http://purl.org/dc/terms/
  dcat: http://www.w3.org/ns/dcat#

```

Links to the schema:

* YAML version: [schema.yaml](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifProperties/cdifCatalogRecord/schema.json)
* JSON version: [schema.json](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifProperties/cdifCatalogRecord/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "schema": "http://schema.org/",
    "ex": "https://example.org/",
    "xsd": "http://www.w3.org/2001/XMLSchema#",
    "dcterms": "http://purl.org/dc/terms/",
    "dcat": "http://www.w3.org/ns/dcat#",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifProperties/cdifCatalogRecord/context.jsonld)

## Sources

* [CDIF book](https://cross-domain-interoperability-framework.github.io/cdifbook/metadata/schemaorgimplementation.html#schema-org-implementation-of-cdif-metadata)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/Cross-Domain-Interoperability-Framework/metadataBuildingBlocks](https://github.com/Cross-Domain-Interoperability-Framework/metadataBuildingBlocks)
* Path: `_sources/cdifProperties/cdifCatalogRecord`

