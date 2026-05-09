
# CDIF Long Data Structure (Schema)

`cdif.bbr.metadata.cdifProperties.cdifLongData` *v0.1*

metadata to document long (narrow) data structure where each row is a single observation with a descriptor column identifying the variable and a reference column holding the value. Defines properties: @type, cdi:hasPhysicalMapping, cdi:arrayBase, csvw:delimiter, csvw:header, csvw:headerRowCount, csvw:commentPrefix, csvw:skipBlankRows, csvw:skipInitialSpace, csvw:skipRows, csvw:lineTerminators, csvw:quoteChar, cdi:isDelimited, cdi:isFixedWidth, cdi:escapeCharacter. Uses building blocks: cdifPhysicalMapping (cdifProperties).

[*Status*](http://www.opengis.net/def/status): Under development

## Description

# Long Data Structure

Describes data in **long (narrow) format**, where each row represents a single observation. A descriptor column identifies which variable the row measures, and a reference column holds the actual value. This contrasts with wide format (one row per entity with each variable in its own column) and data cube format (multi-dimensional arrays).

Uses DDI-CDI `LongStructureDataSet` type. The descriptor and reference variable roles are expressed via `cdi:role` on `cdi:InstanceVariable` entries in `schema:variableMeasured`, using the values `DescriptorComponent` and `ReferenceValueComponent`.

Optional CSVW and DDI-CDI physical properties may be provided when the long data is serialized as delimited text.

## Examples

### Example Long Data Structure
Example long (narrow) data structure with delimiter and header settings.
#### json
```json
{
    "@context": {
        "schema": "http://schema.org/",
        "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
        "csvw": "http://www.w3.org/ns/csvw#",
        "ex": "https://example.org/"
    },
    "@type": ["cdi:LongStructureDataSet"],
    "cdi:hasPhysicalMapping": [
        {
            "cdi:index": 0,
            "cdi:physicalDataType": "String",
            "cdi:formats_InstanceVariable": {
                "@id": "ex:var-descriptor"
            }
        },
        {
            "cdi:index": 1,
            "cdi:physicalDataType": "Numeric",
            "cdi:formats_InstanceVariable": {
                "@id": "ex:var-value"
            }
        }
    ],
    "csvw:delimiter": ",",
    "csvw:header": true,
    "csvw:headerRowCount": 1,
    "cdi:isDelimited": true
}

```

#### jsonld
```jsonld
{
  "@context": [
    {
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "csvw": "http://www.w3.org/ns/csvw#"
    },
    "https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifProperties/cdifLongData/context.jsonld",
    {
      "schema": "http://schema.org/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "csvw": "http://www.w3.org/ns/csvw#",
      "ex": "https://example.org/"
    }
  ],
  "@type": [
    "cdi:LongStructureDataSet"
  ],
  "cdi:hasPhysicalMapping": [
    {
      "cdi:index": 0,
      "cdi:physicalDataType": "String",
      "cdi:formats_InstanceVariable": {
        "@id": "ex:var-descriptor"
      }
    },
    {
      "cdi:index": 1,
      "cdi:physicalDataType": "Numeric",
      "cdi:formats_InstanceVariable": {
        "@id": "ex:var-value"
      }
    }
  ],
  "csvw:delimiter": ",",
  "csvw:header": true,
  "csvw:headerRowCount": 1,
  "cdi:isDelimited": true
}
```

#### ttl
```ttl
@prefix cdi: <http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/> .
@prefix csvw: <http://www.w3.org/ns/csvw#> .
@prefix ex: <https://example.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

[] a cdi:LongStructureDataSet ;
    cdi:hasPhysicalMapping [ cdi:formats_InstanceVariable ex:var-descriptor ;
            cdi:index 0 ;
            cdi:physicalDataType "String" ],
        [ cdi:formats_InstanceVariable ex:var-value ;
            cdi:index 1 ;
            cdi:physicalDataType "Numeric" ] ;
    cdi:isDelimited true ;
    csvw:delimiter "," ;
    csvw:header true ;
    csvw:headerRowCount 1 .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
type: object
title: Long Data Structure Type
description: Long (narrow) data structure using DDI-CDI. Typed as cdi:LongStructureDataSet.
  In long format each row represents a single observation, with a descriptor column
  identifying which variable is measured and a reference column holding the value.
  The descriptor and reference roles are expressed via cdi:role on InstanceVariables
  in schema:variableMeasured (DescriptorComponent and ReferenceValueComponent).
properties:
  '@type':
    type: array
    items:
      type: string
    allOf:
    - contains:
        const: cdi:LongStructureDataSet
  cdi:hasPhysicalMapping:
    type: array
    description: Links variables to their physical representation in this dataset.
    items:
      $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifProperties/cdifPhysicalMapping/schema.yaml
  cdi:arrayBase:
    type: integer
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
  csvw:commentPrefix:
    type: string
    description: An atomic property that sets the comment prefix flag to the single
      provided value, which MUST be a string. The default is '#'.
  csvw:skipBlankRows:
    type: boolean
    default: false
  csvw:skipInitialSpace:
    type: boolean
    default: true
  csvw:skipRows:
    type: integer
    description: The number of rows to skip at the beginning of the file, before a
      header row or tabular data.
    default: 0
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
  cdi:isDelimited:
    type: boolean
    description: Indicates whether the data uses a delimiter to separate fields.
  cdi:isFixedWidth:
    type: boolean
    description: Indicates whether the data uses fixed-width fields.
  cdi:escapeCharacter:
    type: string
    description: The character used to escape special characters in the data. From
      DDI-CDI PhysicalSegmentLayout.escapeCharacter.
required:
- '@type'
x-jsonld-prefixes:
  schema: http://schema.org/
  cdi: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/

```

Links to the schema:

* YAML version: [schema.yaml](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifProperties/cdifLongData/schema.json)
* JSON version: [schema.json](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifProperties/cdifLongData/schema.yaml)


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
[context.jsonld](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifProperties/cdifLongData/context.jsonld)

## Sources

* [DDI-CDI 1.0 Specification](https://ddialliance.org/Specification/DDI-CDI/1.0/)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/Cross-Domain-Interoperability-Framework/metadataBuildingBlocks](https://github.com/Cross-Domain-Interoperability-Framework/metadataBuildingBlocks)
* Path: `_sources/cdifProperties/cdifLongData`

