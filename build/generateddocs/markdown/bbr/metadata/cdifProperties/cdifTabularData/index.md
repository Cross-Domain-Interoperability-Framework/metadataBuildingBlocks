
# CDIF Data Description (Schema)

`cdif.bbr.metadata.cdifProperties.cdifTabularData` *v0.1*

metadata to document physical data structure, mapping DDI/CDI instance variable to implementation  in a particualr serializtion. This extension plugs into the description of a particular file in a distribution, e.g. schema:DataDownload. Defines properties: @type, cdi:arrayBase, csvw:commentPrefix, csvw:delimiter, csvw:header, csvw:headerRowCount, cdi:isDelimited, cdi:isFixedWidth, csvw:lineTerminators, csvw:quoteChar, csvw:skipBlankRows, csvw:skipColumns, csvw:skipInitialSpace, csvw:skipRows, cdi:escapeCharacter, cdi:headerIsCaseSensitive, cdi:treatConsecutiveDelimitersAsOne, csvw:tableDirection, csvw:textDirection, csvw:trim, cdif:hasPhysicalMapping, countRows, countColumns. Uses building blocks: cdifPhysicalMapping (cdifProperties).

[*Status*](http://www.opengis.net/def/status): Under development

## Description

# Data structure description

Describes tabular/structured data files. Typed as `cdi:PhysicalDataSet` and `ada:tabularData`. Supports DDI-CDI WideDataStructure for column layout description, spatial registration, and various analytical technique-specific component types, hierarchical datastructures like JSON, and multidimensional data array structures serialized in data cube format like hdf5 or netCDF.

## Examples

### Minimal Tabular Data
Bare cdi:TabularTextDataSet + schema:Dataset typing with cdi:isDelimited
(the oneOf branch requires either isDelimited or isFixedWidth = true).
#### json
```json
{
    "@context": {
        "schema": "http://schema.org/",
        "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
        "csvw": "http://www.w3.org/ns/csvw#",
        "ex": "https://example.org/"
    },
    "@type": ["cdi:TabularTextDataSet", "schema:Dataset"],
    "cdi:isDelimited": true,
    "csvw:delimiter": ",",
    "csvw:header": true,
    "csvw:headerRowCount": 1,
    "csvw:commentPrefix": "#",
    "csvw:skipBlankRows": false,
    "csvw:skipInitialSpace": true,
    "countRows": 1500,
    "countColumns": 5,
    "cdif:hasPhysicalMapping": [
        {
            "cdif:index": 0,
            "cdif:physicalDataType": "String",
            "cdif:formats_InstanceVariable": {
                "@id": "ex:var-station-id"
            }
        },
        {
            "cdif:index": 1,
            "cdif:format": "float64",
            "cdif:physicalDataType": "Numeric",
            "cdif:formats_InstanceVariable": {
                "@id": "ex:var-temperature"
            }
        }
    ]
}

```

#### jsonld
```jsonld
{
  "@context": [
    {
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "csvw": "http://www.w3.org/ns/csvw#",
      "schema": "http://schema.org/"
    },
    "https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifProperties/cdifTabularData/context.jsonld",
    {
      "schema": "http://schema.org/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "csvw": "http://www.w3.org/ns/csvw#",
      "ex": "https://example.org/"
    }
  ],
  "@type": [
    "cdi:TabularTextDataSet",
    "schema:Dataset"
  ],
  "cdi:isDelimited": true,
  "csvw:delimiter": ",",
  "csvw:header": true,
  "csvw:headerRowCount": 1,
  "csvw:commentPrefix": "#",
  "csvw:skipBlankRows": false,
  "csvw:skipInitialSpace": true,
  "countRows": 1500,
  "countColumns": 5,
  "cdif:hasPhysicalMapping": [
    {
      "cdif:index": 0,
      "cdif:physicalDataType": "String",
      "cdif:formats_InstanceVariable": {
        "@id": "ex:var-station-id"
      }
    },
    {
      "cdif:index": 1,
      "cdif:format": "float64",
      "cdif:physicalDataType": "Numeric",
      "cdif:formats_InstanceVariable": {
        "@id": "ex:var-temperature"
      }
    }
  ]
}
```

#### ttl
```ttl
@prefix cdi: <http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/> .
@prefix csvw: <http://www.w3.org/ns/csvw#> .
@prefix ex: <https://example.org/> .
@prefix ns1: <cdif:> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

[] a cdi:TabularTextDataSet,
        schema1:Dataset ;
    ns1:hasPhysicalMapping [ ns1:formats_InstanceVariable ex:var-station-id ;
            ns1:index 0 ;
            ns1:physicalDataType "String" ],
        [ ns1:format "float64" ;
            ns1:formats_InstanceVariable ex:var-temperature ;
            ns1:index 1 ;
            ns1:physicalDataType "Numeric" ] ;
    cdi:isDelimited true ;
    csvw:commentPrefix "#" ;
    csvw:delimiter "," ;
    csvw:header true ;
    csvw:headerRowCount 1 ;
    csvw:skipBlankRows false ;
    csvw:skipInitialSpace true .


```


### Complete Tabular Data
Delimited tabular dataset exercising every CSVW dialect property
(delimiter, quote/escape, header, lineTerminators, skipBlankRows/
skipColumns/skipRows, table/text direction, trim), plus arrayBase,
headerIsCaseSensitive, treatConsecutiveDelimitersAsOne, countRows/Cols,
and three physical-mapping entries.
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
    "csvw": "http://www.w3.org/ns/csvw#",
    "ex": "https://example.org/"
  },
  "@type": ["cdi:TabularTextDataSet", "schema:Dataset"],
  "cdi:isDelimited": true,
  "cdi:isFixedWidth": false,
  "cdi:arrayBase": 1,
  "csvw:delimiter": ",",
  "csvw:quoteChar": "\"",
  "cdi:escapeCharacter": "\"",
  "csvw:header": true,
  "csvw:headerRowCount": 1,
  "csvw:commentPrefix": "#",
  "csvw:lineTerminators": "CRLF",
  "csvw:skipBlankRows": false,
  "csvw:skipColumns": 0,
  "csvw:skipInitialSpace": true,
  "csvw:skipRows": 0,
  "cdi:headerIsCaseSensitive": false,
  "cdi:treatConsecutiveDelimitersAsOne": false,
  "csvw:tableDirection": "Ltr",
  "csvw:textDirection": "Inherit",
  "csvw:trim": "true",
  "countRows": 1500,
  "countColumns": 3,
  "cdif:hasPhysicalMapping": [
    {
      "cdif:index": 0,
      "cdif:physicalDataType": "String",
      "cdi:length": 16,
      "cdi:isRequired": true,
      "cdif:formats_InstanceVariable": {"@id": "ex:var-station-id"}
    },
    {
      "cdif:index": 1,
      "cdif:format": "YYYY-MM-DD",
      "cdif:physicalDataType": "Date",
      "cdi:nullSequence": "NA",
      "cdif:formats_InstanceVariable": {"@id": "ex:var-date"}
    },
    {
      "cdif:index": 2,
      "cdif:format": "#,##0.00",
      "cdif:physicalDataType": "Numeric",
      "cdi:length": 12,
      "cdi:scale": 1,
      "cdi:decimalPositions": 2,
      "cdif:formats_InstanceVariable": {"@id": "ex:var-temperature"}
    }
  ]
}

```

#### jsonld
```jsonld
{
  "@context": [
    {
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "csvw": "http://www.w3.org/ns/csvw#",
      "schema": "http://schema.org/"
    },
    "https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifProperties/cdifTabularData/context.jsonld",
    {
      "schema": "http://schema.org/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "csvw": "http://www.w3.org/ns/csvw#",
      "ex": "https://example.org/"
    }
  ],
  "@type": [
    "cdi:TabularTextDataSet",
    "schema:Dataset"
  ],
  "cdi:isDelimited": true,
  "cdi:isFixedWidth": false,
  "cdi:arrayBase": 1,
  "csvw:delimiter": ",",
  "csvw:quoteChar": "\"",
  "cdi:escapeCharacter": "\"",
  "csvw:header": true,
  "csvw:headerRowCount": 1,
  "csvw:commentPrefix": "#",
  "csvw:lineTerminators": "CRLF",
  "csvw:skipBlankRows": false,
  "csvw:skipColumns": 0,
  "csvw:skipInitialSpace": true,
  "csvw:skipRows": 0,
  "cdi:headerIsCaseSensitive": false,
  "cdi:treatConsecutiveDelimitersAsOne": false,
  "csvw:tableDirection": "Ltr",
  "csvw:textDirection": "Inherit",
  "csvw:trim": "true",
  "countRows": 1500,
  "countColumns": 3,
  "cdif:hasPhysicalMapping": [
    {
      "cdif:index": 0,
      "cdif:physicalDataType": "String",
      "cdi:length": 16,
      "cdi:isRequired": true,
      "cdif:formats_InstanceVariable": {
        "@id": "ex:var-station-id"
      }
    },
    {
      "cdif:index": 1,
      "cdif:format": "YYYY-MM-DD",
      "cdif:physicalDataType": "Date",
      "cdi:nullSequence": "NA",
      "cdif:formats_InstanceVariable": {
        "@id": "ex:var-date"
      }
    },
    {
      "cdif:index": 2,
      "cdif:format": "#,##0.00",
      "cdif:physicalDataType": "Numeric",
      "cdi:length": 12,
      "cdi:scale": 1,
      "cdi:decimalPositions": 2,
      "cdif:formats_InstanceVariable": {
        "@id": "ex:var-temperature"
      }
    }
  ]
}
```

#### ttl
```ttl
@prefix cdi: <http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/> .
@prefix csvw: <http://www.w3.org/ns/csvw#> .
@prefix ex: <https://example.org/> .
@prefix ns1: <cdif:> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

[] a cdi:TabularTextDataSet,
        schema1:Dataset ;
    ns1:hasPhysicalMapping [ ns1:formats_InstanceVariable ex:var-station-id ;
            ns1:index 0 ;
            ns1:physicalDataType "String" ;
            cdi:isRequired true ;
            cdi:length 16 ],
        [ ns1:format "YYYY-MM-DD" ;
            ns1:formats_InstanceVariable ex:var-date ;
            ns1:index 1 ;
            ns1:physicalDataType "Date" ;
            cdi:nullSequence "NA" ],
        [ ns1:format "#,##0.00" ;
            ns1:formats_InstanceVariable ex:var-temperature ;
            ns1:index 2 ;
            ns1:physicalDataType "Numeric" ;
            cdi:decimalPositions 2 ;
            cdi:length 12 ;
            cdi:scale 1 ] ;
    cdi:arrayBase 1 ;
    cdi:escapeCharacter "\"" ;
    cdi:headerIsCaseSensitive false ;
    cdi:isDelimited true ;
    cdi:isFixedWidth false ;
    cdi:treatConsecutiveDelimitersAsOne false ;
    csvw:commentPrefix "#" ;
    csvw:delimiter "," ;
    csvw:header true ;
    csvw:headerRowCount 1 ;
    csvw:lineTerminators "CRLF" ;
    csvw:quoteChar "\"" ;
    csvw:skipBlankRows false ;
    csvw:skipColumns 0 ;
    csvw:skipInitialSpace true ;
    csvw:skipRows 0 ;
    csvw:tableDirection "Ltr" ;
    csvw:textDirection "Inherit" ;
    csvw:trim "true" .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
type: object
title: Tabular Data Type
description: Tabular data type aligned with CDIF 2026 schema using DDI-CDI and CSVW
  properties. Typed as cdi:TabularTextDataSet.
properties:
  '@type':
    type: array
    items:
      type: string
    minItems: 2
    allOf:
    - contains:
        const: cdi:TabularTextDataSet
  cdi:arrayBase:
    type: integer
    x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/arrayBase
  csvw:commentPrefix:
    type: string
    description: An atomic property that sets the comment prefix flag to the single
      provided value, which MUST be a string. The default is '#'.
  csvw:delimiter:
    type: string
    description: Sets the delimiter flag to the single provided value, which MUST
      be a string. The default is ','.
  csvw:header:
    type: boolean
    description: If true, sets the header row count flag to 1, and if false to 0,
      unless headerRowCount is provided, in which case the value provided for the
      header property is ignored. The default is true.
  csvw:headerRowCount:
    type: integer
    minimum: 0
    default: 1
    description: A numeric atomic property that sets the header row count flag to
      the single provided value, which MUST be a non-negative integer.
  cdi:isDelimited:
    type: boolean
    description: Schema constraint is that one of {'isDelimited','isFixedWidth'} must
      be present with a True value; the other one may be present or omitted, but if
      present must have a false value.
    x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/isDelimited
  cdi:isFixedWidth:
    type: boolean
    x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/isFixedWidth
  csvw:lineTerminators:
    type: string
    enum:
    - CRLF
    - LF
    - "\r\n"
    - '

      '
  csvw:quoteChar:
    type: string
    default: '"'
    description: Same as DDI-CDI quoteCharacter. The string that is used around escaped
      cells.
  csvw:skipBlankRows:
    type: boolean
    default: false
  csvw:skipColumns:
    type: integer
    default: 0
    description: The number of columns to skip at the beginning of each row.
  csvw:skipInitialSpace:
    type: boolean
    default: true
  csvw:skipRows:
    type: integer
    description: The number of rows to skip at the beginning of the file, before a
      header row or tabular data.
    default: 0
  cdi:escapeCharacter:
    type: string
    description: The character used to escape special characters in the data. From
      DDI-CDI PhysicalSegmentLayout.escapeCharacter.
    x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/escapeCharacter
  cdi:headerIsCaseSensitive:
    type: boolean
    default: false
    description: Whether column header names are case-sensitive. From DDI-CDI PhysicalSegmentLayout.headerIsCaseSensitive.
    x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/headerIsCaseSensitive
  cdi:treatConsecutiveDelimitersAsOne:
    type: boolean
    default: false
    description: Whether consecutive delimiters should be treated as a single delimiter.
      From DDI-CDI PhysicalSegmentLayout.treatConsecutiveDelimitersAsOne.
    x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/treatConsecutiveDelimitersAsOne
  csvw:tableDirection:
    type: string
    enum:
    - Ltr
    - Rtl
    default: Ltr
    description: Indicates the direction of the table layout (left-to-right or right-to-left).
      From DDI-CDI PhysicalSegmentLayout.tableDirection.
  csvw:textDirection:
    type: string
    enum:
    - Auto
    - Inherit
    - Ltr
    - Rtl
    default: Auto
    description: Indicates whether the text within cells should be displayed as left-to-right,
      right-to-left, according to content, or inherited from the table direction.
      From DDI-CDI PhysicalSegmentLayout.textDirection.
  csvw:trim:
    type: string
    enum:
    - 'true'
    - end
    - 'false'
    - start
    description: Indicates whether to trim whitespace around cells. 'true' corresponds
      to DDI-CDI 'both' value, 'false' corresponds to DDI-CDI 'neither' value.
  cdif:hasPhysicalMapping:
    type: array
    description: Links variables to their physical representation in this dataset.
    items:
      $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifProperties/cdifPhysicalMapping/schema.yaml
  countRows:
    type: integer
  countColumns:
    type: integer
oneOf:
- properties:
    cdi:isDelimited:
      const: true
      x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/isDelimited
    cdi:isFixedWidth:
      const: false
      x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/isFixedWidth
  required:
  - cdi:isDelimited
- properties:
    cdi:isDelimited:
      const: false
      x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/isDelimited
    cdi:isFixedWidth:
      const: true
      x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/isFixedWidth
  required:
  - cdi:isFixedWidth
required:
- '@type'
- cdif:hasPhysicalMapping
x-jsonld-prefixes:
  schema: http://schema.org/
  ada: https://ada.astromat.org/metadata/
  cdi: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/

```

Links to the schema:

* YAML version: [schema.yaml](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifProperties/cdifTabularData/schema.json)
* JSON version: [schema.json](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifProperties/cdifTabularData/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "schema": "http://schema.org/",
    "ada": "https://ada.astromat.org/metadata/",
    "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifProperties/cdifTabularData/context.jsonld)

## Sources

* [ADA Metadata Schema v3](https://github.com/amds-ldeo/metadata)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/Cross-Domain-Interoperability-Framework/metadataBuildingBlocks](https://github.com/Cross-Domain-Interoperability-Framework/metadataBuildingBlocks)
* Path: `_sources/cdifProperties/cdifTabularData`

