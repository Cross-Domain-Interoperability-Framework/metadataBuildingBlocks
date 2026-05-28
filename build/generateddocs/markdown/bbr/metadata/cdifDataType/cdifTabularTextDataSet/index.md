
# CDIF TabularTextDataSet building block (Schema)

`cdif.bbr.metadata.cdifDataType.cdifTabularTextDataSet` *v0.1*

Dataset-level physical layout of a delimited or fixed-width text dataset (CSV, TSV, fixed-width). A subclass of cdi:PhysicalDataSet carried on a schema:DataDownload distribution dual-typed cdi:TabularTextDataSet. Defines cdi:delimiter, cdi:hasHeader, cdi:headerRowCount, cdi:quoteCharacter, cdi:lineTerminator, cdi:isDelimited, cdi:isFixedWidth, cdi:skipRows, cdi:trim, cdi:tableDirection, cdi:textDirection (enumerations modeled as string+enum, matching the canonical ddicdiPhysicalDataSet), and the other DDI-CDI TabularTextDataSet attributes. Per-field mappings are cdifTextMapping.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

# CDIF TabularTextDataSet

Dataset-level physical layout of a delimited or fixed-width **text** dataset (CSV, TSV,
fixed-width). A subclass of DDI-CDI `PhysicalDataSet`; in CDIF it is carried on a
`schema:DataDownload` distribution dual-typed `cdi:TabularTextDataSet`.

This building block is an **attribute mixin** (no `@type` of its own) — the
`cdi:TabularTextDataSet` token lives on the distribution. The CDIF Data Description
profile merges these attributes onto a distribution via an `if @type contains
cdi:TabularTextDataSet then …` branch.

Defines the DDI-CDI `TabularTextDataSet` attributes (`cdi:delimiter`, `cdi:hasHeader`,
`cdi:headerRowCount`, `cdi:quoteCharacter`, `cdi:lineTerminator`, `cdi:isDelimited`,
`cdi:isFixedWidth`, `cdi:skipRows`, `cdi:trim`, etc.). Per-field physical mappings for a
tabular text dataset are [`cdifTextMapping`](../cdifTextMapping/) values of
`cdif:hasPhysicalMapping`.

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: Tabular Text DataSet
description: Dataset-level physical layout properties of a delimited or fixed-width
  text dataset (CSV, TSV, fixed-width). A subclass of cdi:PhysicalDataSet, carried
  on a schema:DataDownload distribution dual-typed cdi:TabularTextDataSet. DDI-CDI
  TabularTextDataSet. This is an attribute mixin (no @type of its own); the @type
  token is carried by the distribution. Per-field mappings are cdifTextMapping (on
  cdif:hasPhysicalMapping).
type: object
properties:
  cdi:arrayBase:
    type: integer
    default: 1
    description: Index of the first element/column (TabularTextDataSet.arrayBase).
    x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/arrayBase
  cdi:commentPrefix:
    type: string
    description: Character(s) that mark a line as a comment.
    x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/commentPrefix
  cdi:delimiter:
    type: string
    description: Field delimiter (e.g., "," or tab).
    x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/delimiter
  cdi:escapeCharacter:
    type: string
    x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/escapeCharacter
  cdi:hasHeader:
    type: boolean
    default: true
    x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/hasHeader
  cdi:headerIsCaseSensitive:
    type: boolean
    default: false
    x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/headerIsCaseSensitive
  cdi:headerRowCount:
    type: integer
    default: 1
    x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/headerRowCount
  cdi:isDelimited:
    type: boolean
    default: true
    x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/isDelimited
  cdi:isFixedWidth:
    type: boolean
    default: false
    x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/isFixedWidth
  cdi:lineTerminator:
    type: array
    items:
      type: string
    description: Allowed line terminators, in order (default [CRLF, LF]).
    x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/lineTerminator
  cdi:nullSequence:
    type: string
    description: Value interpreted as null at the dataset level.
    x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/nullSequence
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
  cdi:treatConsecutiveDelimitersAsOne:
    type: boolean
    default: false
    x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/treatConsecutiveDelimitersAsOne
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
x-jsonld-prefixes:
  schema: http://schema.org/
  cdi: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/
  cdif: https://cdif.org/0.1/

```

Links to the schema:

* YAML version: [schema.yaml](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifDataType/cdifTabularTextDataSet/schema.json)
* JSON version: [schema.json](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifDataType/cdifTabularTextDataSet/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "schema": "http://schema.org/",
    "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
    "cdif": "https://cdif.org/0.1/",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifDataType/cdifTabularTextDataSet/context.jsonld)

## Sources

* [DDI-CDI 1.0 Specification](https://ddialliance.org/Specification/DDI-CDI/1.0/)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/Cross-Domain-Interoperability-Framework/metadataBuildingBlocks](https://github.com/Cross-Domain-Interoperability-Framework/metadataBuildingBlocks)
* Path: `_sources/cdifDataType/cdifTabularTextDataSet`

