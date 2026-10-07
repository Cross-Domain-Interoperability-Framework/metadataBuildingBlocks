
# CDIF Data Description (Schema)

`cdif.bbr.metadata.cdifDataType.cdifTabularData` *v0.1*

metadata to document physical data structure, mapping DDI/CDI instance variable to implementation  in a particualr serializtion. This extension plugs into the description of a particular file in a distribution, e.g. schema:DataDownload. Defines properties: @type, cdi:arrayBase, cdi:commentPrefix, cdi:delimiter, cdi:hasHeader, cdi:headerRowCount, cdi:isDelimited, cdi:isFixedWidth, cdi:lineTerminator, cdi:quoteCharacter, cdi:skipBlankRows, cdi:skipDataColumns, cdi:skipInitialSpace, cdi:skipRows, cdi:escapeCharacter, cdi:headerIsCaseSensitive, cdi:treatConsecutiveDelimitersAsOne, cdi:tableDirection, cdi:textDirection, cdi:trim, cdif:hasPhysicalMapping, countRows, countColumns. Uses building blocks: cdifPhysicalMapping (cdifDataType).

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
    "cdif": "https://w3id.org/cdif/",
    "ex": "https://example.org/"
  },
  "@type": [
    "cdi:TabularTextDataSet",
    "schema:Dataset"
  ],
  "cdi:isDelimited": true,
  "cdi:delimiter": ",",
  "cdi:hasHeader": true,
  "cdi:headerRowCount": 1,
  "cdi:commentPrefix": "#",
  "cdi:skipBlankRows": false,
  "cdi:skipInitialSpace": true,
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
      "schema": "http://schema.org/"
    },
    "https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifDataType/cdifTabularData/context.jsonld",
    {
      "schema": "http://schema.org/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "cdif": "https://w3id.org/cdif/",
      "ex": "https://example.org/"
    }
  ],
  "@type": [
    "cdi:TabularTextDataSet",
    "schema:Dataset"
  ],
  "cdi:isDelimited": true,
  "cdi:delimiter": ",",
  "cdi:hasHeader": true,
  "cdi:headerRowCount": 1,
  "cdi:commentPrefix": "#",
  "cdi:skipBlankRows": false,
  "cdi:skipInitialSpace": true,
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
@prefix cdif: <https://w3id.org/cdif/> .
@prefix ex: <https://example.org/> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

[] a cdi:TabularTextDataSet,
        schema1:Dataset ;
    cdi:commentPrefix "#" ;
    cdi:delimiter "," ;
    cdi:hasHeader true ;
    cdi:headerRowCount 1 ;
    cdi:isDelimited true ;
    cdi:skipBlankRows false ;
    cdi:skipInitialSpace true ;
    cdif:hasPhysicalMapping [ cdif:formats_InstanceVariable ex:var-station-id ;
            cdif:index 0 ;
            cdif:physicalDataType "String" ],
        [ cdif:format "float64" ;
            cdif:formats_InstanceVariable ex:var-temperature ;
            cdif:index 1 ;
            cdif:physicalDataType "Numeric" ] .


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
    "cdif": "https://w3id.org/cdif/",
    "ex": "https://example.org/"
  },
  "@type": [
    "cdi:TabularTextDataSet",
    "schema:Dataset"
  ],
  "cdi:isDelimited": true,
  "cdi:isFixedWidth": false,
  "cdi:arrayBase": 1,
  "cdi:delimiter": ",",
  "cdi:quoteCharacter": "\"",
  "cdi:escapeCharacter": "\"",
  "cdi:hasHeader": true,
  "cdi:headerRowCount": 1,
  "cdi:commentPrefix": "#",
  "cdi:lineTerminator": [
    "CRLF"
  ],
  "cdi:skipBlankRows": false,
  "cdi:skipDataColumns": 0,
  "cdi:skipInitialSpace": true,
  "cdi:skipRows": 0,
  "cdi:headerIsCaseSensitive": false,
  "cdi:treatConsecutiveDelimitersAsOne": false,
  "cdi:tableDirection": "Ltr",
  "cdi:textDirection": "Inherit",
  "cdi:trim": "Both",
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

#### jsonld
```jsonld
{
  "@context": [
    {
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "schema": "http://schema.org/"
    },
    "https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifDataType/cdifTabularData/context.jsonld",
    {
      "schema": "http://schema.org/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "cdif": "https://w3id.org/cdif/",
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
  "cdi:delimiter": ",",
  "cdi:quoteCharacter": "\"",
  "cdi:escapeCharacter": "\"",
  "cdi:hasHeader": true,
  "cdi:headerRowCount": 1,
  "cdi:commentPrefix": "#",
  "cdi:lineTerminator": [
    "CRLF"
  ],
  "cdi:skipBlankRows": false,
  "cdi:skipDataColumns": 0,
  "cdi:skipInitialSpace": true,
  "cdi:skipRows": 0,
  "cdi:headerIsCaseSensitive": false,
  "cdi:treatConsecutiveDelimitersAsOne": false,
  "cdi:tableDirection": "Ltr",
  "cdi:textDirection": "Inherit",
  "cdi:trim": "Both",
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
@prefix cdif: <https://w3id.org/cdif/> .
@prefix ex: <https://example.org/> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

[] a cdi:TabularTextDataSet,
        schema1:Dataset ;
    cdi:arrayBase 1 ;
    cdi:commentPrefix "#" ;
    cdi:delimiter "," ;
    cdi:escapeCharacter "\"" ;
    cdi:hasHeader true ;
    cdi:headerIsCaseSensitive false ;
    cdi:headerRowCount 1 ;
    cdi:isDelimited true ;
    cdi:isFixedWidth false ;
    cdi:lineTerminator "CRLF" ;
    cdi:quoteCharacter "\"" ;
    cdi:skipBlankRows false ;
    cdi:skipDataColumns 0 ;
    cdi:skipInitialSpace true ;
    cdi:skipRows 0 ;
    cdi:tableDirection "Ltr" ;
    cdi:textDirection "Inherit" ;
    cdi:treatConsecutiveDelimitersAsOne false ;
    cdi:trim "Both" ;
    cdif:hasPhysicalMapping [ cdi:nullSequence "NA" ;
            cdif:format "YYYY-MM-DD" ;
            cdif:formats_InstanceVariable ex:var-date ;
            cdif:index 1 ;
            cdif:physicalDataType "Date" ],
        [ cdi:decimalPositions 2 ;
            cdi:length 12 ;
            cdi:scale 1 ;
            cdif:format "#,##0.00" ;
            cdif:formats_InstanceVariable ex:var-temperature ;
            cdif:index 2 ;
            cdif:physicalDataType "Numeric" ],
        [ cdi:isRequired true ;
            cdi:length 16 ;
            cdif:formats_InstanceVariable ex:var-station-id ;
            cdif:index 0 ;
            cdif:physicalDataType "String" ] .


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
  cdi:commentPrefix:
    type: string
    description: Character(s) that mark a line as a comment.
    x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/commentPrefix
  cdi:delimiter:
    type: string
    description: Field delimiter (e.g., "," or tab).
    x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/delimiter
  cdi:hasHeader:
    type: boolean
    default: true
    x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/hasHeader
  cdi:headerRowCount:
    type: integer
    default: 1
    x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/headerRowCount
  cdi:isDelimited:
    type: boolean
    description: Schema constraint is that one of {'isDelimited','isFixedWidth'} must
      be present with a True value; the other one may be present or omitted, but if
      present must have a false value.
    x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/isDelimited
  cdi:isFixedWidth:
    type: boolean
    x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/isFixedWidth
  cdi:lineTerminator:
    type: array
    items:
      type: string
    description: Allowed line terminators, in order (default [CRLF, LF]).
    x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/lineTerminator
  cdi:quoteCharacter:
    type: string
    default: '"'
    x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/quoteCharacter
  cdi:skipBlankRows:
    type: boolean
    default: false
    x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/skipBlankRows
  cdi:skipDataColumns:
    type: integer
    default: 0
    x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/skipDataColumns
  cdi:skipInitialSpace:
    type: boolean
    default: true
    x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/skipInitialSpace
  cdi:skipRows:
    type: integer
    default: 0
    x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/skipRows
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
  cdi:tableDirection:
    type: string
    default: Auto
    enum:
    - Auto
    - Ltr
    - Rtl
    description: Direction in which columns are arranged in each row (DDI-CDI TabularTextDataSet.tableDirection,
      TableDirectionValues enumeration).
    x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/tableDirection
  cdi:textDirection:
    type: string
    enum:
    - Auto
    - Inherit
    - Ltr
    - Rtl
    description: Reading order of text within cells (DDI-CDI TabularTextDataSet.textDirection,
      TextDirectionValues enumeration).
    x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/textDirection
  cdi:trim:
    type: string
    enum:
    - Both
    - End
    - Neither
    - Start
    description: Which spaces to remove from a data value (DDI-CDI TabularTextDataSet.trim,
      TrimValues enumeration).
    x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/trim
  cdif:hasPhysicalMapping:
    type: array
    description: Links variables to their physical representation in this dataset.
    items:
      $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifDataType/cdifPhysicalMapping/schema.yaml
    x-jsonld-id: https://w3id.org/cdif/hasPhysicalMapping
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
  cdif: https://w3id.org/cdif/
  schema: http://schema.org/
  ada: https://ada.astromat.org/metadata/
  cdi: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/

```

Links to the schema:

* YAML version: [schema.yaml](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifDataType/cdifTabularData/schema.json)
* JSON version: [schema.json](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifDataType/cdifTabularData/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "cdif": "https://w3id.org/cdif/",
    "schema": "http://schema.org/",
    "ada": "https://ada.astromat.org/metadata/",
    "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
    "skos": "http://www.w3.org/2004/02/skos/core#",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifDataType/cdifTabularData/context.jsonld)

## Sources

* [ADA Metadata Schema v3](https://github.com/amds-ldeo/metadata)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/Cross-Domain-Interoperability-Framework/metadataBuildingBlocks](https://github.com/Cross-Domain-Interoperability-Framework/metadataBuildingBlocks)
* Path: `_sources/cdifDataType/cdifTabularData`

