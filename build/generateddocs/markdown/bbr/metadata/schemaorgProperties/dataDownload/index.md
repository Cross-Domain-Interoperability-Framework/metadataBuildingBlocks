
# DataDownload (Schema)

`cdif.bbr.metadata.schemaorgProperties.dataDownload` *v0.1*

Schema defining properties of a DataDownload. Used as value to describe a distribution. Defines properties: @id, @type, schema:name, schema:contentUrl, schema:encodingFormat, spdx:checksum, schema:provider. Uses building blocks: person (schemaorgProperties), organization (schemaorgProperties).

[*Status*](http://www.opengis.net/def/status): Under development

## Description

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

## Examples

### Example data dowload description.
Defintion of properties to describe file-based distribution of a resource on the Web..
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "ex": "https://example.org/",
    "xsd": "http://www.w3.org/2001/XMLSchema#",
    "dcterms": "http://purl.org/dc/terms/"
  },
  "@type": [
    "schema:DataDownload"
  ],
  "schema:name": "Water levels in Beartooth reservoir, 1992-2020",
  "schema:contentUrl": "https://hounddata.org/354277.csv",
  "schema:encodingFormat": [
    "text/csv"
  ],
  "spdx:checksum": {
    "@type": [
      "spdx:Checksum"
    ],
    "spdx:algorithm": "MD5",
    "spdx:checksumValue": "d41d8cd98f00b204e9800998ecf8427e"
  },
  "schema:provider": [
    {
      "@id": "https://orcid.org/3333-4444-5565",
      "@type": [
        "schema:Person"
      ],
      "schema:name": "Severus Data",
      "schema:alternateName": "the datameister",
      "schema:affiliation": {
        "@id": "https://ror.org/347237",
        "@type": [
          "schema:Organization"
        ],
        "schema:additionalType": [
          "Data repository"
        ],
        "schema:name": "Houndstooth Data Repository",
        "schema:identifier": "https://ror.org/347237"
      },
      "schema:contactPoint": {
        "@type": [
          "schema:ContactPoint"
        ],
        "schema:email": "joe@email.org"
      },
      "schema:description": "Earth Science Data Custodian",
      "schema:identifier": {
        "@type": [
          "schema:PropertyValue"
        ],
        "schema:propertyID": "https://registry.identifiers.org/registry/orcid",
        "schema:value": "3333-4444-5565",
        "schema:url": "https://orcid.org/3333-4444-5565"
      }
    }
  ],
  "dcterms:conformsTo": [
    {
      "@id": "http://www.opengis.net/def/nil/OGC/0/missing"
    }
  ]
}

```

#### jsonld
```jsonld
{
  "@context": [
    {
      "schema": "http://schema.org/",
      "dcterms": "http://purl.org/dc/terms/"
    },
    "https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/dataDownload/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ex": "https://example.org/",
      "xsd": "http://www.w3.org/2001/XMLSchema#",
      "dcterms": "http://purl.org/dc/terms/"
    }
  ],
  "@type": [
    "schema:DataDownload"
  ],
  "schema:name": "Water levels in Beartooth reservoir, 1992-2020",
  "schema:contentUrl": "https://hounddata.org/354277.csv",
  "schema:encodingFormat": [
    "text/csv"
  ],
  "spdx:checksum": {
    "@type": [
      "spdx:Checksum"
    ],
    "spdx:algorithm": "MD5",
    "spdx:checksumValue": "d41d8cd98f00b204e9800998ecf8427e"
  },
  "schema:provider": [
    {
      "@id": "https://orcid.org/3333-4444-5565",
      "@type": [
        "schema:Person"
      ],
      "schema:name": "Severus Data",
      "schema:alternateName": "the datameister",
      "schema:affiliation": {
        "@id": "https://ror.org/347237",
        "@type": [
          "schema:Organization"
        ],
        "schema:additionalType": [
          "Data repository"
        ],
        "schema:name": "Houndstooth Data Repository",
        "schema:identifier": "https://ror.org/347237"
      },
      "schema:contactPoint": {
        "@type": [
          "schema:ContactPoint"
        ],
        "schema:email": "joe@email.org"
      },
      "schema:description": "Earth Science Data Custodian",
      "schema:identifier": {
        "@type": [
          "schema:PropertyValue"
        ],
        "schema:propertyID": "https://registry.identifiers.org/registry/orcid",
        "schema:value": "3333-4444-5565",
        "schema:url": "https://orcid.org/3333-4444-5565"
      }
    }
  ],
  "dcterms:conformsTo": [
    {
      "@id": "http://www.opengis.net/def/nil/OGC/0/missing"
    }
  ]
}
```

#### ttl
```ttl
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix ns1: <spdx:> .
@prefix schema1: <http://schema.org/> .

<https://orcid.org/3333-4444-5565> a schema1:Person ;
    schema1:affiliation <https://ror.org/347237> ;
    schema1:alternateName "the datameister" ;
    schema1:contactPoint [ a schema1:ContactPoint ;
            schema1:email "joe@email.org" ] ;
    schema1:description "Earth Science Data Custodian" ;
    schema1:identifier [ a schema1:PropertyValue ;
            schema1:propertyID "https://registry.identifiers.org/registry/orcid" ;
            schema1:url "https://orcid.org/3333-4444-5565" ;
            schema1:value "3333-4444-5565" ] ;
    schema1:name "Severus Data" .

<https://ror.org/347237> a schema1:Organization ;
    schema1:additionalType "Data repository" ;
    schema1:identifier "https://ror.org/347237" ;
    schema1:name "Houndstooth Data Repository" .

[] a schema1:DataDownload ;
    dcterms:conformsTo <http://www.opengis.net/def/nil/OGC/0/missing> ;
    schema1:contentUrl "https://hounddata.org/354277.csv" ;
    schema1:encodingFormat "text/csv" ;
    schema1:name "Water levels in Beartooth reservoir, 1992-2020" ;
    schema1:provider <https://orcid.org/3333-4444-5565> ;
    ns1:checksum [ a ns1:Checksum ;
            ns1:algorithm "MD5" ;
            ns1:checksumValue "d41d8cd98f00b204e9800998ecf8427e" ] .


```


### Complete data download example.
DataDownload instance exercising all properties: name, description, contentUrl,
encodingFormat (multiple), spdx:checksum (SHA256), provider (Person and Organization),
and dcterms:conformsTo (multiple).
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "ex": "https://example.org/",
    "spdx": "http://spdx.org/rdf/terms#",
    "dcterms": "http://purl.org/dc/terms/"
  },
  "@id": "ex:DataDownloadComplete_001",
  "@type": ["schema:DataDownload"],
  "schema:name": "Arctic Sea Ice Extent Monthly Averages 1979-2024",
  "schema:description": "CSV file containing monthly average Arctic sea ice extent values derived from satellite passive microwave observations. Columns include date, extent in million km², and anomaly from 1981-2010 mean.",
  "schema:contentUrl": "https://data.example.org/sea-ice/arctic-monthly-extent-1979-2024.csv",
  "schema:encodingFormat": ["text/csv", "application/zip"],
  "spdx:checksum": {
    "@type": ["spdx:Checksum"],
    "spdx:algorithm": "SHA256",
    "spdx:checksumValue": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"
  },
  "schema:provider": [
    {
      "@id": "https://orcid.org/0000-0002-5678-1234",
      "@type": ["schema:Person"],
      "schema:name": "Maria Icewatch",
      "schema:affiliation": {
        "@type": ["schema:Organization"],
        "schema:name": "National Snow and Ice Data Center",
        "schema:identifier": {
          "@type": ["schema:PropertyValue"],
          "schema:propertyID": "https://ror.org",
          "schema:value": "0559x5c32",
          "schema:url": "https://ror.org/0559x5c32"
        }
      },
      "schema:contactPoint": {
        "@type": ["schema:ContactPoint"],
        "schema:email": "data@nsidc.org"
      },
      "schema:identifier": {
        "@type": ["schema:PropertyValue"],
        "schema:propertyID": "https://orcid.org",
        "schema:value": "0000-0002-5678-1234",
        "schema:url": "https://orcid.org/0000-0002-5678-1234"
      }
    },
    {
      "@type": ["schema:Organization"],
      "schema:name": "National Snow and Ice Data Center",
      "schema:identifier": {
        "@type": ["schema:PropertyValue"],
        "schema:propertyID": "https://ror.org",
        "schema:value": "0559x5c32",
        "schema:url": "https://ror.org/0559x5c32"
      }
    }
  ],
  "dcterms:conformsTo": [
    {"@id": "https://www.ietf.org/rfc/rfc4180.txt"},
    {"@id": "https://www.w3.org/TR/tabular-data-primer/"}
  ]
}

```

#### jsonld
```jsonld
{
  "@context": [
    {
      "schema": "http://schema.org/",
      "dcterms": "http://purl.org/dc/terms/",
      "spdx": "http://spdx.org/rdf/terms#"
    },
    "https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/dataDownload/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ex": "https://example.org/",
      "spdx": "http://spdx.org/rdf/terms#",
      "dcterms": "http://purl.org/dc/terms/"
    }
  ],
  "@id": "ex:DataDownloadComplete_001",
  "@type": [
    "schema:DataDownload"
  ],
  "schema:name": "Arctic Sea Ice Extent Monthly Averages 1979-2024",
  "schema:description": "CSV file containing monthly average Arctic sea ice extent values derived from satellite passive microwave observations. Columns include date, extent in million km\u00b2, and anomaly from 1981-2010 mean.",
  "schema:contentUrl": "https://data.example.org/sea-ice/arctic-monthly-extent-1979-2024.csv",
  "schema:encodingFormat": [
    "text/csv",
    "application/zip"
  ],
  "spdx:checksum": {
    "@type": [
      "spdx:Checksum"
    ],
    "spdx:algorithm": "SHA256",
    "spdx:checksumValue": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"
  },
  "schema:provider": [
    {
      "@id": "https://orcid.org/0000-0002-5678-1234",
      "@type": [
        "schema:Person"
      ],
      "schema:name": "Maria Icewatch",
      "schema:affiliation": {
        "@type": [
          "schema:Organization"
        ],
        "schema:name": "National Snow and Ice Data Center",
        "schema:identifier": {
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": "https://ror.org",
          "schema:value": "0559x5c32",
          "schema:url": "https://ror.org/0559x5c32"
        }
      },
      "schema:contactPoint": {
        "@type": [
          "schema:ContactPoint"
        ],
        "schema:email": "data@nsidc.org"
      },
      "schema:identifier": {
        "@type": [
          "schema:PropertyValue"
        ],
        "schema:propertyID": "https://orcid.org",
        "schema:value": "0000-0002-5678-1234",
        "schema:url": "https://orcid.org/0000-0002-5678-1234"
      }
    },
    {
      "@type": [
        "schema:Organization"
      ],
      "schema:name": "National Snow and Ice Data Center",
      "schema:identifier": {
        "@type": [
          "schema:PropertyValue"
        ],
        "schema:propertyID": "https://ror.org",
        "schema:value": "0559x5c32",
        "schema:url": "https://ror.org/0559x5c32"
      }
    }
  ],
  "dcterms:conformsTo": [
    {
      "@id": "https://www.ietf.org/rfc/rfc4180.txt"
    },
    {
      "@id": "https://www.w3.org/TR/tabular-data-primer/"
    }
  ]
}
```

#### ttl
```ttl
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix ex: <https://example.org/> .
@prefix schema1: <http://schema.org/> .
@prefix spdx: <http://spdx.org/rdf/terms#> .

ex:DataDownloadComplete_001 a schema1:DataDownload ;
    dcterms:conformsTo <https://www.ietf.org/rfc/rfc4180.txt>,
        <https://www.w3.org/TR/tabular-data-primer/> ;
    schema1:contentUrl "https://data.example.org/sea-ice/arctic-monthly-extent-1979-2024.csv" ;
    schema1:description "CSV file containing monthly average Arctic sea ice extent values derived from satellite passive microwave observations. Columns include date, extent in million km², and anomaly from 1981-2010 mean." ;
    schema1:encodingFormat "application/zip",
        "text/csv" ;
    schema1:name "Arctic Sea Ice Extent Monthly Averages 1979-2024" ;
    schema1:provider [ a schema1:Organization ;
            schema1:identifier [ a schema1:PropertyValue ;
                    schema1:propertyID "https://ror.org" ;
                    schema1:url "https://ror.org/0559x5c32" ;
                    schema1:value "0559x5c32" ] ;
            schema1:name "National Snow and Ice Data Center" ],
        <https://orcid.org/0000-0002-5678-1234> ;
    spdx:checksum [ a spdx:Checksum ;
            spdx:algorithm "SHA256" ;
            spdx:checksumValue "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855" ] .

<https://orcid.org/0000-0002-5678-1234> a schema1:Person ;
    schema1:affiliation [ a schema1:Organization ;
            schema1:identifier [ a schema1:PropertyValue ;
                    schema1:propertyID "https://ror.org" ;
                    schema1:url "https://ror.org/0559x5c32" ;
                    schema1:value "0559x5c32" ] ;
            schema1:name "National Snow and Ice Data Center" ] ;
    schema1:contactPoint [ a schema1:ContactPoint ;
            schema1:email "data@nsidc.org" ] ;
    schema1:identifier [ a schema1:PropertyValue ;
            schema1:propertyID "https://orcid.org" ;
            schema1:url "https://orcid.org/0000-0002-5678-1234" ;
            schema1:value "0000-0002-5678-1234" ] ;
    schema1:name "Maria Icewatch" .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
description: schema to document file-based access to a resoruce via URL, based on
  schema.org/DataDownload
type: object
properties:
  '@id':
    type: string
  '@type':
    type: array
    description: implement as array because extensions might need to add additional
      types
    items:
      type: string
    contains:
      const: schema:DataDownload
    minItems: 1
  schema:name:
    type: string
  schema:description:
    type: string
    description: Description of this distribution, e.g. what format, access constraints,
      etc.
  schema:contentUrl:
    type: string
    format: uri
  schema:encodingFormat:
    type: array
    description: MIME type with extension; should indicate the serialization scheme
      in sufficient detail that machine can know how to parse.
    items:
      type: string
  spdx:checksum:
    type: object
    description: A string value calculated from the content of the resource representation,
      used to test if content has been modified. The checksum is a property of a particular
      distribution/DataDownload.
    properties:
      '@type':
        type: array
        items:
          type: string
        contains:
          const: spdx:Checksum
        minItems: 1
      spdx:algorithm:
        type: string
      spdx:checksumValue:
        type: string
    required:
    - '@type'
  dcterms:conformsTo:
    description: An identifier for a standard or specification that the distribution
      conforms to. Recommended to enable machine-actionable data access.
    type: array
    minItems: 1
    items:
      type: object
      properties:
        '@id':
          type: string
          description: uri for specification that this distribution conforms to
  schema:provider:
    type: array
    description: Party who maintains this particular distribution option for the dataset.
      Use this property if there are multiple distributions from different providers
    items:
      anyOf:
      - type: object
        properties:
          '@id':
            type: string
            description: a identifier for an agent defined in this metadata, or externally;
              must be dereferenceable
        required:
        - '@id'
      - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/person/schema.yaml
      - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/organization/schema.yaml
required:
- schema:contentUrl
- '@type'
x-jsonld-prefixes:
  schema: http://schema.org/

```

Links to the schema:

* YAML version: [schema.yaml](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/dataDownload/schema.json)
* JSON version: [schema.json](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/dataDownload/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "schema": "http://schema.org/",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/dataDownload/context.jsonld)

## Sources

* [schema.org](https://schema.org/DataDownload)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/Cross-Domain-Interoperability-Framework/metadataBuildingBlocks](https://github.com/Cross-Domain-Interoperability-Framework/metadataBuildingBlocks)
* Path: `_sources/schemaorgProperties/dataDownload`

