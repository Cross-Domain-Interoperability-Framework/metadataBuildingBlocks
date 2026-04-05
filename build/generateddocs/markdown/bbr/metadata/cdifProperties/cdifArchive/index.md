
# CDIF Archive (Schema)

`cdif.bbr.metadata.cdifProperties.cdifArchive` *v0.1*

Schema for a DataDownload distribution that is an archive containing multiple component files described via schema:hasPart, with optional CDIF data description extensions. Defines properties: schema:hasPart. Uses building blocks: dataDownload (schemaorgProperties), cdifDataCube (cdifProperties), cdifTabularData (cdifProperties).

[*Status*](http://www.opengis.net/def/status): Under development

## Description

Defines the structure for a DataDownload distribution that is an archive file (e.g. ZIP, tar.gz) containing multiple component files. The archive itself is typed as `schema:DataDownload` with standard properties (name, contentUrl, encodingFormat, checksum). Component files within the archive are listed in `schema:hasPart` and typed as `schema:MediaObject` (not `schema:DataDownload`, since they are not independently accessible via URL).

Each hasPart item has:
- `@id` --identifier for cross-references (e.g. from metadata sidecar files via `schema:about`)
- `@type` --must include `schema:MediaObject`, must not include `schema:DataDownload`
- `schema:name` --filename within the archive
- `schema:encodingFormat` --MIME type(s)
- `schema:size` --file size as `schema:QuantitativeValue`
- `schema:description` --description of file content
- `schema:about` --references to related files (for metadata sidecars)
- `spdx:checksum` --integrity checksum

Component files may optionally include CDIF data description extensions to describe their internal data structure:
- `cdifTabularData` --for delimited or fixed-width tabular text files (CSV, TSV), with CSVW properties and physical column mappings
- `cdifDataCube` --for multi-dimensional structured datasets (NetCDF, HDF5), with locator-based physical mappings

## Examples

### Example CDIF archive distribution.
Example DataDownload distribution for a zip archive containing multiple
component files described via schema:hasPart, with optional CDIF data
description extensions (TabularTextDataSet, StructuredDataSet).
#### json
```json
{
  "@type": [
    "schema:DataDownload"
  ],
  "schema:name": "Geochemistry analysis data package",
  "schema:contentUrl": "https://example.org/data/geochem-package.zip",
  "schema:encodingFormat": [
    "application/zip"
  ],
  "dcterms:conformsTo": [
    {
      "@id": "https://www.iana.org/assignments/media-types/application/zip"
    }
  ],
  "schema:description": "This data product is distributed as a zip archive; contents of the archive are listed as parts. The component files are not individually accessible.",
  "spdx:checksum": {
    "@type": [
      "spdx:Checksum"
    ],
    "spdx:algorithm": "SHA256",
    "spdx:checksumValue": "a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4e5f6a1b2"
  },
  "schema:hasPart": [
    {
      "@type": [
        "schema:MediaObject"
      ],
      "@id": "#e0fee3cccca4292d76dcb5238224e677",
      "schema:name": "20260101_GEOCHEM_LAB_SAMPLE-001_results.csv",
      "schema:description": "Geochemistry analysis results in tabular format. sha256:f962af0b2e2f02752aa258a58cede1263f05c7a78e3b9d162da960368f7dc54b",
      "schema:encodingFormat": [
        "text/csv"
      ],
      "schema:size": {
        "@type": [
          "schema:QuantitativeValue"
        ],
        "schema:value": 10860,
        "schema:unitText": "byte"
      },
      "spdx:checksum": {
        "@type": [
          "spdx:Checksum"
        ],
        "spdx:algorithm": "SHA256",
        "spdx:checksumValue": "f962af0b2e2f02752aa258a58cede1263f05c7a78e3b9d162da960368f7dc54b"
      }
    },
    {
      "@type": [
        "schema:MediaObject",
        "cdi:TabularTextDataSet"
      ],
      "@id": "#7c6ef03f6b0e88dec54d9897f591deab",
      "schema:name": "20260101_GEOCHEM_LAB_SAMPLE-001_measurements.csv",
      "schema:description": "Measurement data with column structure described via CSVW and physical mappings.",
      "schema:encodingFormat": [
        "text/csv"
      ],
      "schema:size": {
        "@type": [
          "schema:QuantitativeValue"
        ],
        "schema:value": 6249,
        "schema:unitText": "byte"
      },
      "cdi:isDelimited": true,
      "csvw:delimiter": ",",
      "csvw:header": true,
      "csvw:headerRowCount": 1,
      "countRows": 144,
      "countColumns": 3,
      "cdi:hasPhysicalMapping": [
        {
          "cdi:index": 0,
          "cdi:format": "string",
          "cdi:physicalDataType": "string",
          "cdi:isRequired": true,
          "cdi:formats_InstanceVariable": {
            "@id": "#var-sample-id"
          }
        },
        {
          "cdi:index": 1,
          "cdi:format": "decimal",
          "cdi:physicalDataType": "float64",
          "cdi:nullSequence": "NA",
          "cdi:isRequired": true,
          "cdi:formats_InstanceVariable": {
            "@id": "#var-concentration"
          }
        },
        {
          "cdi:index": 2,
          "cdi:format": "decimal",
          "cdi:physicalDataType": "float64",
          "cdi:nullSequence": "NA",
          "cdi:isRequired": false,
          "cdi:formats_InstanceVariable": {
            "@id": "#var-uncertainty"
          }
        }
      ]
    },
    {
      "@type": [
        "schema:MediaObject",
        "cdi:StructuredDataSet"
      ],
      "@id": "#a6143a557a62f78ae39fcb80578b74a3",
      "schema:name": "20260101_GEOCHEM_LAB_SAMPLE-001_spectra.nc",
      "schema:description": "Spectral data cube with wavelength and intensity dimensions.",
      "schema:encodingFormat": [
        "application/x-netcdf"
      ],
      "schema:size": {
        "@type": [
          "schema:QuantitativeValue"
        ],
        "schema:value": 13743003,
        "schema:unitText": "byte"
      },
      "cdi:hasPhysicalMapping": [
        {
          "cdi:index": 0,
          "cdi:format": "decimal",
          "cdi:physicalDataType": "float32",
          "cdi:locator": "/spectra/wavelength",
          "cdi:isRequired": true,
          "cdi:formats_InstanceVariable": {
            "@id": "#var-wavelength"
          }
        },
        {
          "cdi:index": 1,
          "cdi:format": "decimal",
          "cdi:physicalDataType": "float32",
          "cdi:locator": "/spectra/intensity",
          "cdi:isRequired": true,
          "cdi:formats_InstanceVariable": {
            "@id": "#var-intensity"
          }
        }
      ]
    },
    {
      "@type": [
        "schema:MediaObject"
      ],
      "@id": "#3eaec0f86900d58d874bd7c18bedb156",
      "schema:name": "20260101_GEOCHEM_LAB_SAMPLE-001_method.pdf",
      "schema:description": "Method description document for the analysis.",
      "schema:encodingFormat": [
        "application/pdf"
      ],
      "schema:size": {
        "@type": [
          "schema:QuantitativeValue"
        ],
        "schema:value": 56062,
        "schema:unitText": "byte"
      }
    },
    {
      "@type": [
        "schema:MediaObject"
      ],
      "@id": "#d640488b65b53b6bcc1abcb66b3cde7e",
      "schema:name": "20260101_GEOCHEM_LAB_SAMPLE-001_results.yaml",
      "schema:description": "Metadata sidecar for the results CSV file.",
      "schema:encodingFormat": [
        "application/yaml"
      ],
      "schema:size": {
        "@type": [
          "schema:QuantitativeValue"
        ],
        "schema:value": 2281,
        "schema:unitText": "byte"
      },
      "schema:about": [
        {
          "@id": "#e0fee3cccca4292d76dcb5238224e677"
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
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "csvw": "http://www.w3.org/ns/csvw#",
      "spdx": "http://spdx.org/rdf/terms#",
      "dcterms": "http://purl.org/dc/terms/"
    },
    "https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifProperties/cdifArchive/context.jsonld"
  ],
  "@type": [
    "schema:DataDownload"
  ],
  "schema:name": "Geochemistry analysis data package",
  "schema:contentUrl": "https://example.org/data/geochem-package.zip",
  "schema:encodingFormat": [
    "application/zip"
  ],
  "dcterms:conformsTo": [
    {
      "@id": "https://www.iana.org/assignments/media-types/application/zip"
    }
  ],
  "schema:description": "This data product is distributed as a zip archive; contents of the archive are listed as parts. The component files are not individually accessible.",
  "spdx:checksum": {
    "@type": [
      "spdx:Checksum"
    ],
    "spdx:algorithm": "SHA256",
    "spdx:checksumValue": "a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4e5f6a1b2"
  },
  "schema:hasPart": [
    {
      "@type": [
        "schema:MediaObject"
      ],
      "@id": "#e0fee3cccca4292d76dcb5238224e677",
      "schema:name": "20260101_GEOCHEM_LAB_SAMPLE-001_results.csv",
      "schema:description": "Geochemistry analysis results in tabular format. sha256:f962af0b2e2f02752aa258a58cede1263f05c7a78e3b9d162da960368f7dc54b",
      "schema:encodingFormat": [
        "text/csv"
      ],
      "schema:size": {
        "@type": [
          "schema:QuantitativeValue"
        ],
        "schema:value": 10860,
        "schema:unitText": "byte"
      },
      "spdx:checksum": {
        "@type": [
          "spdx:Checksum"
        ],
        "spdx:algorithm": "SHA256",
        "spdx:checksumValue": "f962af0b2e2f02752aa258a58cede1263f05c7a78e3b9d162da960368f7dc54b"
      }
    },
    {
      "@type": [
        "schema:MediaObject",
        "cdi:TabularTextDataSet"
      ],
      "@id": "#7c6ef03f6b0e88dec54d9897f591deab",
      "schema:name": "20260101_GEOCHEM_LAB_SAMPLE-001_measurements.csv",
      "schema:description": "Measurement data with column structure described via CSVW and physical mappings.",
      "schema:encodingFormat": [
        "text/csv"
      ],
      "schema:size": {
        "@type": [
          "schema:QuantitativeValue"
        ],
        "schema:value": 6249,
        "schema:unitText": "byte"
      },
      "cdi:isDelimited": true,
      "csvw:delimiter": ",",
      "csvw:header": true,
      "csvw:headerRowCount": 1,
      "countRows": 144,
      "countColumns": 3,
      "cdi:hasPhysicalMapping": [
        {
          "cdi:index": 0,
          "cdi:format": "string",
          "cdi:physicalDataType": "string",
          "cdi:isRequired": true,
          "cdi:formats_InstanceVariable": {
            "@id": "#var-sample-id"
          }
        },
        {
          "cdi:index": 1,
          "cdi:format": "decimal",
          "cdi:physicalDataType": "float64",
          "cdi:nullSequence": "NA",
          "cdi:isRequired": true,
          "cdi:formats_InstanceVariable": {
            "@id": "#var-concentration"
          }
        },
        {
          "cdi:index": 2,
          "cdi:format": "decimal",
          "cdi:physicalDataType": "float64",
          "cdi:nullSequence": "NA",
          "cdi:isRequired": false,
          "cdi:formats_InstanceVariable": {
            "@id": "#var-uncertainty"
          }
        }
      ]
    },
    {
      "@type": [
        "schema:MediaObject",
        "cdi:StructuredDataSet"
      ],
      "@id": "#a6143a557a62f78ae39fcb80578b74a3",
      "schema:name": "20260101_GEOCHEM_LAB_SAMPLE-001_spectra.nc",
      "schema:description": "Spectral data cube with wavelength and intensity dimensions.",
      "schema:encodingFormat": [
        "application/x-netcdf"
      ],
      "schema:size": {
        "@type": [
          "schema:QuantitativeValue"
        ],
        "schema:value": 13743003,
        "schema:unitText": "byte"
      },
      "cdi:hasPhysicalMapping": [
        {
          "cdi:index": 0,
          "cdi:format": "decimal",
          "cdi:physicalDataType": "float32",
          "cdi:locator": "/spectra/wavelength",
          "cdi:isRequired": true,
          "cdi:formats_InstanceVariable": {
            "@id": "#var-wavelength"
          }
        },
        {
          "cdi:index": 1,
          "cdi:format": "decimal",
          "cdi:physicalDataType": "float32",
          "cdi:locator": "/spectra/intensity",
          "cdi:isRequired": true,
          "cdi:formats_InstanceVariable": {
            "@id": "#var-intensity"
          }
        }
      ]
    },
    {
      "@type": [
        "schema:MediaObject"
      ],
      "@id": "#3eaec0f86900d58d874bd7c18bedb156",
      "schema:name": "20260101_GEOCHEM_LAB_SAMPLE-001_method.pdf",
      "schema:description": "Method description document for the analysis.",
      "schema:encodingFormat": [
        "application/pdf"
      ],
      "schema:size": {
        "@type": [
          "schema:QuantitativeValue"
        ],
        "schema:value": 56062,
        "schema:unitText": "byte"
      }
    },
    {
      "@type": [
        "schema:MediaObject"
      ],
      "@id": "#d640488b65b53b6bcc1abcb66b3cde7e",
      "schema:name": "20260101_GEOCHEM_LAB_SAMPLE-001_results.yaml",
      "schema:description": "Metadata sidecar for the results CSV file.",
      "schema:encodingFormat": [
        "application/yaml"
      ],
      "schema:size": {
        "@type": [
          "schema:QuantitativeValue"
        ],
        "schema:value": 2281,
        "schema:unitText": "byte"
      },
      "schema:about": [
        {
          "@id": "#e0fee3cccca4292d76dcb5238224e677"
        }
      ]
    }
  ]
}
```

#### ttl
```ttl
@prefix cdi: <http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/> .
@prefix csvw: <http://www.w3.org/ns/csvw#> .
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix schema1: <http://schema.org/> .
@prefix spdx: <http://spdx.org/rdf/terms#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<file:///github/workspace/#3eaec0f86900d58d874bd7c18bedb156> a schema1:MediaObject ;
    schema1:description "Method description document for the analysis." ;
    schema1:encodingFormat "application/pdf" ;
    schema1:name "20260101_GEOCHEM_LAB_SAMPLE-001_method.pdf" ;
    schema1:size [ a schema1:QuantitativeValue ;
            schema1:unitText "byte" ;
            schema1:value 56062 ] .

<file:///github/workspace/#7c6ef03f6b0e88dec54d9897f591deab> a cdi:TabularTextDataSet,
        schema1:MediaObject ;
    cdi:hasPhysicalMapping [ cdi:format "decimal" ;
            cdi:formats_InstanceVariable <file:///github/workspace/#var-uncertainty> ;
            cdi:index 2 ;
            cdi:isRequired false ;
            cdi:nullSequence "NA" ;
            cdi:physicalDataType "float64" ],
        [ cdi:format "decimal" ;
            cdi:formats_InstanceVariable <file:///github/workspace/#var-concentration> ;
            cdi:index 1 ;
            cdi:isRequired true ;
            cdi:nullSequence "NA" ;
            cdi:physicalDataType "float64" ],
        [ cdi:format "string" ;
            cdi:formats_InstanceVariable <file:///github/workspace/#var-sample-id> ;
            cdi:index 0 ;
            cdi:isRequired true ;
            cdi:physicalDataType "string" ] ;
    cdi:isDelimited true ;
    schema1:description "Measurement data with column structure described via CSVW and physical mappings." ;
    schema1:encodingFormat "text/csv" ;
    schema1:name "20260101_GEOCHEM_LAB_SAMPLE-001_measurements.csv" ;
    schema1:size [ a schema1:QuantitativeValue ;
            schema1:unitText "byte" ;
            schema1:value 6249 ] ;
    csvw:delimiter "," ;
    csvw:header true ;
    csvw:headerRowCount 1 .

<file:///github/workspace/#a6143a557a62f78ae39fcb80578b74a3> a cdi:StructuredDataSet,
        schema1:MediaObject ;
    cdi:hasPhysicalMapping [ cdi:format "decimal" ;
            cdi:formats_InstanceVariable <file:///github/workspace/#var-wavelength> ;
            cdi:index 0 ;
            cdi:isRequired true ;
            cdi:locator "/spectra/wavelength" ;
            cdi:physicalDataType "float32" ],
        [ cdi:format "decimal" ;
            cdi:formats_InstanceVariable <file:///github/workspace/#var-intensity> ;
            cdi:index 1 ;
            cdi:isRequired true ;
            cdi:locator "/spectra/intensity" ;
            cdi:physicalDataType "float32" ] ;
    schema1:description "Spectral data cube with wavelength and intensity dimensions." ;
    schema1:encodingFormat "application/x-netcdf" ;
    schema1:name "20260101_GEOCHEM_LAB_SAMPLE-001_spectra.nc" ;
    schema1:size [ a schema1:QuantitativeValue ;
            schema1:unitText "byte" ;
            schema1:value 13743003 ] .

<file:///github/workspace/#d640488b65b53b6bcc1abcb66b3cde7e> a schema1:MediaObject ;
    schema1:about <file:///github/workspace/#e0fee3cccca4292d76dcb5238224e677> ;
    schema1:description "Metadata sidecar for the results CSV file." ;
    schema1:encodingFormat "application/yaml" ;
    schema1:name "20260101_GEOCHEM_LAB_SAMPLE-001_results.yaml" ;
    schema1:size [ a schema1:QuantitativeValue ;
            schema1:unitText "byte" ;
            schema1:value 2281 ] .

<file:///github/workspace/#e0fee3cccca4292d76dcb5238224e677> a schema1:MediaObject ;
    schema1:description "Geochemistry analysis results in tabular format. sha256:f962af0b2e2f02752aa258a58cede1263f05c7a78e3b9d162da960368f7dc54b" ;
    schema1:encodingFormat "text/csv" ;
    schema1:name "20260101_GEOCHEM_LAB_SAMPLE-001_results.csv" ;
    schema1:size [ a schema1:QuantitativeValue ;
            schema1:unitText "byte" ;
            schema1:value 10860 ] ;
    spdx:checksum [ a spdx:Checksum ;
            spdx:algorithm "SHA256" ;
            spdx:checksumValue "f962af0b2e2f02752aa258a58cede1263f05c7a78e3b9d162da960368f7dc54b" ] .

[] a schema1:DataDownload ;
    dcterms:conformsTo <https://www.iana.org/assignments/media-types/application/zip> ;
    schema1:contentUrl "https://example.org/data/geochem-package.zip" ;
    schema1:description "This data product is distributed as a zip archive; contents of the archive are listed as parts. The component files are not individually accessible." ;
    schema1:encodingFormat "application/zip" ;
    schema1:hasPart <file:///github/workspace/#3eaec0f86900d58d874bd7c18bedb156>,
        <file:///github/workspace/#7c6ef03f6b0e88dec54d9897f591deab>,
        <file:///github/workspace/#a6143a557a62f78ae39fcb80578b74a3>,
        <file:///github/workspace/#d640488b65b53b6bcc1abcb66b3cde7e>,
        <file:///github/workspace/#e0fee3cccca4292d76dcb5238224e677> ;
    schema1:name "Geochemistry analysis data package" ;
    spdx:checksum [ a spdx:Checksum ;
            spdx:algorithm "SHA256" ;
            spdx:checksumValue "a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4e5f6a1b2" ] .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: CDIF Archive Distribution
description: A DataDownload distribution that is an archive file (e.g. ZIP) containing
  multiple component files described in schema:hasPart. The archive itself is typed
  as schema:DataDownload; each component file is typed as schema:MediaObject (not
  DataDownload, since they are not independently accessible via URL). Components may
  optionally include CDIF data description extensions (cdifTabularData, cdifDataCube)
  to describe their internal data structure.
type: object
allOf:
- $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/dataDownload/schema.yaml
- type: object
  properties:
    schema:hasPart:
      type: array
      description: Array describing the files contained in the archive. Each item
        represents a component file that is part of the archive and is not independently
        accessible.
      items:
        allOf:
        - type: object
          properties:
            '@id':
              type: string
              description: Identifier for this file, typically a hash-based anchor
                (e.g. '#abc123'). Used for cross-references from schema:about in metadata
                sidecar files.
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
              description: For metadata sidecar files, references the data file this
                metadata describes.
              items:
                type: object
                properties:
                  '@id':
                    type: string
                    description: Reference to the @id of the data file described by
                      this sidecar.
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
          - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifProperties/cdifDataCube/schema.yaml
          - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifProperties/cdifTabularData/schema.yaml
          - {}
x-jsonld-prefixes:
  schema: http://schema.org/
  spdx: http://spdx.org/rdf/terms#
  cdi: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/
  csvw: http://www.w3.org/ns/csvw#

```

Links to the schema:

* YAML version: [schema.yaml](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifProperties/cdifArchive/schema.json)
* JSON version: [schema.json](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifProperties/cdifArchive/schema.yaml)


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
[context.jsonld](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifProperties/cdifArchive/context.jsonld)

## Sources

* [CDIF book](https://cross-domain-interoperability-framework.github.io/cdifbook/metadata/schemaorgimplementation.html#schema-org-implementation-of-cdif-metadata)
* [schema.org DataDownload](https://schema.org/DataDownload)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/Cross-Domain-Interoperability-Framework/metadataBuildingBlocks](https://github.com/Cross-Domain-Interoperability-Framework/metadataBuildingBlocks)
* Path: `_sources/cdifProperties/cdifArchive`

