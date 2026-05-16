
# CDIF Archive Distribution (Schema)

`cdif.bbr.metadata.cdifProperties.cdifArchiveDistribution` *v0.1*

Adds archive distribution (cdifArchive) as a valid schema:distribution item type. cdifOptional already provides DataDownload and WebAPI; this building block extends distribution with the cdifArchive option for archive files containing component files described via schema:hasPart.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

## CDIF Archive Distribution

Adds archive distribution as a valid `schema:distribution` item type. The `cdifOptional` building block already defines `schema:distribution` with DataDownload and WebAPI options; this building block extends that with the [cdifArchive](../cdifArchive/) option.

### Dependencies

- [cdifArchive](../cdifArchive/) - archive item schema (DataDownload with hasPart component files)

## Examples

### Minimal CDIF Archive Distribution
Bare schema:Dataset with one archive distribution exercising
cdifArchive at the smallest valid shape.
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "dcterms": "http://purl.org/dc/terms/",
    "ex": "https://example.org/"
  },
  "@type": ["schema:Dataset"],
  "@id": "ex:dataset/minimal-archived",
  "schema:name": "Minimal archived dataset",
  "schema:subjectOf": {
    "dcterms:conformsTo": [
      { "@id": "https://w3id.org/cdif/manifest/1.0" }
    ]
  },
  "schema:distribution": [
    {
      "@type": ["schema:DataDownload"],
      "schema:name": "Bundle",
      "schema:contentUrl": "https://example.org/data/bundle.zip",
      "schema:encodingFormat": ["application/zip"],
      "schema:hasPart": [
        {
          "@id": "#part-1",
          "@type": ["schema:MediaObject"],
          "schema:name": "data.csv",
          "schema:encodingFormat": ["text/csv"]
        }
      ]
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
    "https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifProperties/cdifArchiveDistribution/context.jsonld",
    {
      "schema": "http://schema.org/",
      "dcterms": "http://purl.org/dc/terms/",
      "ex": "https://example.org/"
    }
  ],
  "@type": [
    "schema:Dataset"
  ],
  "@id": "ex:dataset/minimal-archived",
  "schema:name": "Minimal archived dataset",
  "schema:subjectOf": {
    "dcterms:conformsTo": [
      {
        "@id": "https://w3id.org/cdif/manifest/1.0"
      }
    ]
  },
  "schema:distribution": [
    {
      "@type": [
        "schema:DataDownload"
      ],
      "schema:name": "Bundle",
      "schema:contentUrl": "https://example.org/data/bundle.zip",
      "schema:encodingFormat": [
        "application/zip"
      ],
      "schema:hasPart": [
        {
          "@id": "#part-1",
          "@type": [
            "schema:MediaObject"
          ],
          "schema:name": "data.csv",
          "schema:encodingFormat": [
            "text/csv"
          ]
        }
      ]
    }
  ]
}
```

#### ttl
```ttl
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix schema1: <http://schema.org/> .

<https://example.org/dataset/minimal-archived> a schema1:Dataset ;
    schema1:distribution [ a schema1:DataDownload ;
            schema1:contentUrl "https://example.org/data/bundle.zip" ;
            schema1:encodingFormat "application/zip" ;
            schema1:hasPart <file:///github/workspace/#part-1> ;
            schema1:name "Bundle" ] ;
    schema1:name "Minimal archived dataset" ;
    schema1:subjectOf [ dcterms:conformsTo <https://w3id.org/cdif/manifest/1.0> ] .

<file:///github/workspace/#part-1> a schema1:MediaObject ;
    schema1:encodingFormat "text/csv" ;
    schema1:name "data.csv" .


```


### Complete CDIF Archive Distribution
Geochemistry-package Dataset with full schema:subjectOf CatalogRecord,
SPDX checksum on the archive distribution, and a full hasPart manifest.
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "dcterms": "http://purl.org/dc/terms/",
    "dcat": "http://www.w3.org/ns/dcat#",
    "spdx": "http://spdx.org/rdf/terms#",
    "ex": "https://example.org/"
  },
  "@id": "ex:dataset_archive_001",
  "@type": [
    "schema:Dataset"
  ],
  "schema:name": "Geochemical Analysis Results Package",
  "schema:identifier": "https://doi.org/10.1234/geochem-archive-2025",
  "schema:url": "https://example.org/datasets/geochem-archive-2025",
  "schema:dateModified": "2025-08-01",
  "schema:license": [
    "https://creativecommons.org/licenses/by/4.0/"
  ],
  "schema:subjectOf": {
    "@type": [
      "schema:Dataset"
    ],
    "schema:additionalType": [
      "dcat:CatalogRecord"
    ],
    "@id": "ex:metadata_archive_001",
    "schema:about": {
      "@id": "ex:dataset_archive_001"
    },
    "dcterms:conformsTo": [
      {
        "@id": "https://w3id.org/cdif/manifest/1.0"
      }
    ]
  },
  "schema:distribution": [
    {
      "@type": [
        "schema:DataDownload"
      ],
      "schema:name": "Geochemistry results archive",
      "schema:contentUrl": "https://example.org/downloads/geochem-results-2025.zip",
      "schema:encodingFormat": [
        "application/zip"
      ],
      "dcterms:conformsTo": [
        {
          "@id": "https://w3id.org/cdif/manifest/1.0"
        }
      ],
      "schema:hasPart": [
        {
          "@id": "#data-csv",
          "@type": [
            "schema:MediaObject"
          ],
          "schema:name": "results.csv",
          "schema:description": "Tabular geochemical analysis results",
          "schema:encodingFormat": [
            "text/csv"
          ],
          "schema:size": {
            "@type": [
              "schema:QuantitativeValue"
            ],
            "schema:value": 245000,
            "schema:unitText": "byte"
          },
          "spdx:checksum": {
            "@type": [
              "spdx:Checksum"
            ],
            "spdx:algorithm": "sha256",
            "spdx:checksumValue": "a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4e5f6a1b2"
          }
        },
        {
          "@id": "#metadata-json",
          "@type": [
            "schema:MediaObject"
          ],
          "schema:name": "metadata.json",
          "schema:description": "Metadata sidecar for the results file",
          "schema:encodingFormat": [
            "application/json"
          ],
          "schema:about": [
            {
              "@id": "#data-csv"
            }
          ]
        }
      ]
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
      "dcterms": "http://purl.org/dc/terms/",
      "dcat": "http://www.w3.org/ns/dcat#",
      "spdx": "http://spdx.org/rdf/terms#"
    },
    "https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifProperties/cdifArchiveDistribution/context.jsonld",
    {
      "schema": "http://schema.org/",
      "dcterms": "http://purl.org/dc/terms/",
      "dcat": "http://www.w3.org/ns/dcat#",
      "spdx": "http://spdx.org/rdf/terms#",
      "ex": "https://example.org/"
    }
  ],
  "@id": "ex:dataset_archive_001",
  "@type": [
    "schema:Dataset"
  ],
  "schema:name": "Geochemical Analysis Results Package",
  "schema:identifier": "https://doi.org/10.1234/geochem-archive-2025",
  "schema:url": "https://example.org/datasets/geochem-archive-2025",
  "schema:dateModified": "2025-08-01",
  "schema:license": [
    "https://creativecommons.org/licenses/by/4.0/"
  ],
  "schema:subjectOf": {
    "@type": [
      "schema:Dataset"
    ],
    "schema:additionalType": [
      "dcat:CatalogRecord"
    ],
    "@id": "ex:metadata_archive_001",
    "schema:about": {
      "@id": "ex:dataset_archive_001"
    },
    "dcterms:conformsTo": [
      {
        "@id": "https://w3id.org/cdif/manifest/1.0"
      }
    ]
  },
  "schema:distribution": [
    {
      "@type": [
        "schema:DataDownload"
      ],
      "schema:name": "Geochemistry results archive",
      "schema:contentUrl": "https://example.org/downloads/geochem-results-2025.zip",
      "schema:encodingFormat": [
        "application/zip"
      ],
      "dcterms:conformsTo": [
        {
          "@id": "https://w3id.org/cdif/manifest/1.0"
        }
      ],
      "schema:hasPart": [
        {
          "@id": "#data-csv",
          "@type": [
            "schema:MediaObject"
          ],
          "schema:name": "results.csv",
          "schema:description": "Tabular geochemical analysis results",
          "schema:encodingFormat": [
            "text/csv"
          ],
          "schema:size": {
            "@type": [
              "schema:QuantitativeValue"
            ],
            "schema:value": 245000,
            "schema:unitText": "byte"
          },
          "spdx:checksum": {
            "@type": [
              "spdx:Checksum"
            ],
            "spdx:algorithm": "sha256",
            "spdx:checksumValue": "a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4e5f6a1b2"
          }
        },
        {
          "@id": "#metadata-json",
          "@type": [
            "schema:MediaObject"
          ],
          "schema:name": "metadata.json",
          "schema:description": "Metadata sidecar for the results file",
          "schema:encodingFormat": [
            "application/json"
          ],
          "schema:about": [
            {
              "@id": "#data-csv"
            }
          ]
        }
      ]
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
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<file:///github/workspace/#metadata-json> a schema1:MediaObject ;
    schema1:about <file:///github/workspace/#data-csv> ;
    schema1:description "Metadata sidecar for the results file" ;
    schema1:encodingFormat "application/json" ;
    schema1:name "metadata.json" .

ex:dataset_archive_001 a schema1:Dataset ;
    schema1:dateModified "2025-08-01" ;
    schema1:distribution [ a schema1:DataDownload ;
            dcterms:conformsTo <https://w3id.org/cdif/manifest/1.0> ;
            schema1:contentUrl "https://example.org/downloads/geochem-results-2025.zip" ;
            schema1:encodingFormat "application/zip" ;
            schema1:hasPart <file:///github/workspace/#data-csv>,
                <file:///github/workspace/#metadata-json> ;
            schema1:name "Geochemistry results archive" ] ;
    schema1:identifier "https://doi.org/10.1234/geochem-archive-2025" ;
    schema1:license "https://creativecommons.org/licenses/by/4.0/" ;
    schema1:name "Geochemical Analysis Results Package" ;
    schema1:subjectOf ex:metadata_archive_001 ;
    schema1:url "https://example.org/datasets/geochem-archive-2025" .

ex:metadata_archive_001 a schema1:Dataset ;
    dcterms:conformsTo <https://w3id.org/cdif/manifest/1.0> ;
    schema1:about ex:dataset_archive_001 ;
    schema1:additionalType "dcat:CatalogRecord" .

<file:///github/workspace/#data-csv> a schema1:MediaObject ;
    schema1:description "Tabular geochemical analysis results" ;
    schema1:encodingFormat "text/csv" ;
    schema1:name "results.csv" ;
    schema1:size [ a schema1:QuantitativeValue ;
            schema1:unitText "byte" ;
            schema1:value 245000 ] ;
    spdx:checksum [ a spdx:Checksum ;
            spdx:algorithm "sha256" ;
            spdx:checksumValue "a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4e5f6a1b2" ] .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: CDIF Archive Distribution
description: "Wrapper BB. Marks the catalog record as conformant to the CDIF manifest
  spec (https://w3id.org/cdif/manifest/1.0) and lets schema:distribution items carry
  schema:hasPart describing component files of an archive (ZIP, etc.). The base schema:distribution
  anyOf [DataDownload, WebAPI] contributed by cdifCore is preserved \u2014 this BB
  only adds an optional property patch, no new anyOf branch (which would conflict
  with the resolver's complete-schema-replace heuristic)."
type: object
properties:
  schema:subjectOf:
    properties:
      dcterms:conformsTo:
        type: array
        items:
          type: object
          properties:
            '@id':
              type: string
              description: uri for specifications that this metadata record conforms
                to
        minItems: 1
        contains:
          type: object
          properties:
            '@id':
              const: https://w3id.org/cdif/manifest/1.0
  schema:distribution:
    items:
      properties:
        schema:hasPart:
          $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifProperties/cdifArchive/schema.yaml#/$defs/archivePartArray
          description: For archive-style distributions (e.g. ZIP files containing
            multiple component files), describes the component files. Each component
            is typed as schema:MediaObject and may include CDIF data description extensions
            (cdifTabularData, cdifDataCube) to describe its internal structure.

```

Links to the schema:

* YAML version: [schema.yaml](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifProperties/cdifArchiveDistribution/schema.json)
* JSON version: [schema.json](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifProperties/cdifArchiveDistribution/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "schema": "http://schema.org/",
    "spdx": "http://spdx.org/rdf/terms#",
    "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
    "csvw": "http://www.w3.org/ns/csvw#",
    "ada": "https://ada.astromat.org/metadata/",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifProperties/cdifArchiveDistribution/context.jsonld)

## Sources

* [schema.org DataDownload](https://schema.org/DataDownload)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/Cross-Domain-Interoperability-Framework/metadataBuildingBlocks](https://github.com/Cross-Domain-Interoperability-Framework/metadataBuildingBlocks)
* Path: `_sources/cdifProperties/cdifArchiveDistribution`

