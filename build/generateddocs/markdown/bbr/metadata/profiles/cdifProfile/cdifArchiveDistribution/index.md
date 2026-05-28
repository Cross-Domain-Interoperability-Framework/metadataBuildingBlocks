
# CDIF Archive Distribution (Schema)

`cdif.bbr.metadata.profiles.cdifProfile.cdifArchiveDistribution` *v0.1*

Profile module for archive distributions. Adds schema:hasPart support to schema:distribution items that wrap a single download (e.g. a ZIP), describing each component file inside. Requires that the metadata record declare conformance to https://w3id.org/cdif/manifest/1.0; requires schema:hasPart on any DataDownload whose schema:encodingFormat includes application/zip. Defines the archivePartArray and archivePartItem shapes used by component-file metadata. (Merged from the previous cdifArchive building block, which only published these $defs.)

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
    "https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/profiles/cdifProfile/cdifArchiveDistribution/context.jsonld",
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
    "https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/profiles/cdifProfile/cdifArchiveDistribution/context.jsonld",
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
description: "Profile module for archive distributions. Marks the catalog record as
  conformant to the CDIF manifest spec (https://w3id.org/cdif/manifest/1.0) and lets
  schema:distribution items carry schema:hasPart describing the component files inside
  an archive (ZIP, etc.). The base schema:distribution anyOf [DataDownload, WebAPI]
  contributed by cdifCore is preserved \u2014 this BB only adds property constraints,
  no new anyOf branch. (Merged from the previous cdifProfile/cdifArchive BB, which
  held only the $defs for ArchivePart; everything now lives here.)"
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
      allOf:
      - properties:
          schema:hasPart:
            $ref: '#/$defs/archivePartArray'
            description: For archive-style distributions (e.g. ZIP files containing
              multiple component files), describes the component files. Each component
              is typed as schema:MediaObject and may include CDIF data description
              extensions (cdifTabularData, cdifDataCube) to describe its internal
              structure.
      - if:
          properties:
            schema:encodingFormat:
              type: array
              contains:
                const: application/zip
          required:
          - schema:encodingFormat
        then:
          required:
          - schema:hasPart
$defs:
  archivePartArray:
    type: array
    description: Array describing the files contained in the archive. Each item represents
      a component file that is part of the archive and is not independently accessible.
    items:
      $ref: '#/$defs/archivePartItem'
  archivePartItem:
    allOf:
    - type: object
      properties:
        '@id':
          type: string
          description: Identifier for this file, typically a hash-based anchor (e.g.
            '#abc123'). Used for cross-references from schema:about in metadata sidecar
            files.
        '@type':
          type: array
          description: Must include schema:MediaObject. Must NOT include schema:DataDownload
            since this file is not independently accessible. May include additional
            types for categorization.
          items:
            type: string
          contains:
            const: schema:MediaObject
          not:
            contains:
              const: schema:DataDownload
          minItems: 1
        schema:name:
          type: string
          description: Filename of the component file within the archive.
        schema:description:
          type: string
          description: Description of the file content. May include checksum information.
        schema:encodingFormat:
          type: array
          description: MIME type(s) for this file.
          items:
            type: string
        schema:size:
          type: object
          description: File size as a QuantitativeValue.
          properties:
            '@type':
              type: array
              items:
                type: string
              contains:
                const: schema:QuantitativeValue
              minItems: 1
            schema:value:
              type: number
              description: Numeric size value.
            schema:unitText:
              type: string
              description: Unit of measure for size (e.g. 'byte').
        schema:about:
          type: array
          description: For metadata sidecar files, references the data file this metadata
            describes.
          items:
            type: object
            properties:
              '@id':
                type: string
                description: Reference to the @id of the data file described by this
                  sidecar.
        spdx:checksum:
          type: object
          description: Checksum for integrity verification of this component file.
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
      required:
      - '@type'
      - schema:name
      - schema:encodingFormat
    - anyOf:
      - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifDataType/cdifDataCube/schema.yaml
      - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifDataType/cdifTabularData/schema.yaml
      - {}

```

Links to the schema:

* YAML version: [schema.yaml](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/profiles/cdifProfile/cdifArchiveDistribution/schema.json)
* JSON version: [schema.json](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/profiles/cdifProfile/cdifArchiveDistribution/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "cdif": "https://cdif.org/0.1/",
    "schema": "http://schema.org/",
    "ada": "https://ada.astromat.org/metadata/",
    "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/profiles/cdifProfile/cdifArchiveDistribution/context.jsonld)

## Sources

* [schema.org DataDownload](https://schema.org/DataDownload)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/Cross-Domain-Interoperability-Framework/metadataBuildingBlocks](https://github.com/Cross-Domain-Interoperability-Framework/metadataBuildingBlocks)
* Path: `_sources/profiles/cdifProfile/cdifArchiveDistribution`

