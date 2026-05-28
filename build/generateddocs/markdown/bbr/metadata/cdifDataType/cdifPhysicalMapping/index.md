
# CDIF PhysicalMapping bulding block (Schema)

`cdif.bbr.metadata.cdifDataType.cdifPhysicalMapping` *v0.1*

Base physical mapping: metadata to document the physical serialization of a variable in a data structure. Defines properties: cdif:index, cdif:format, cdif:physicalDataType, cdi:numberPattern, cdi:nullSequence, cdi:defaultValue, cdi:scale, cdi:decimalPositions, cdi:minimumLength, cdi:maximumLength, cdi:isRequired, cdif:formats_InstanceVariable. Text-format specifics (cdi:length and number separators) are in cdifTextMapping; structured-document location is in cdifLocatorMapping.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

# Data structure description

Describes tabular/structured data files. Typed as `cdi:PhysicalDataSet` and `ada:tabularData`. Supports DDI-CDI WideDataStructure for column layout description, spatial registration, and various analytical technique-specific component types, hierarchical datastructures like JSON, and multidimensional data array structures serialized in data cube format like hdf5 or netCDF.

## Examples

### Minimal Physical Mapping
Date column mapping with index, format, physical data type, null sequence,
isRequired flag, and a single formats_InstanceVariable reference.
#### json
```json
{
    "@context": {
        "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
        "ex": "https://example.org/"
    },
    "cdif:index": 0,
    "cdif:format": "YYYY-MM-DD",
    "cdif:physicalDataType": "Date",
    "cdi:nullSequence": "NA",
    "cdi:isRequired": true,
    "cdif:formats_InstanceVariable": {
        "@id": "ex:var-collection-date"
    }
}

```

#### jsonld
```jsonld
{
  "@context": [
    {
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/"
    },
    "https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifDataType/cdifPhysicalMapping/context.jsonld",
    {
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "ex": "https://example.org/"
    }
  ],
  "cdif:index": 0,
  "cdif:format": "YYYY-MM-DD",
  "cdif:physicalDataType": "Date",
  "cdi:nullSequence": "NA",
  "cdi:isRequired": true,
  "cdif:formats_InstanceVariable": {
    "@id": "ex:var-collection-date"
  }
}
```

#### ttl
```ttl
@prefix cdi: <http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/> .
@prefix ex: <https://example.org/> .
@prefix ns1: <cdif:> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

[] ns1:format "YYYY-MM-DD" ;
    ns1:formats_InstanceVariable ex:var-collection-date ;
    ns1:index 0 ;
    ns1:physicalDataType "Date" ;
    cdi:isRequired true ;
    cdi:nullSequence "NA" .


```


### Complete Physical Mapping
Numeric column mapping exercising every CSVW-aligned property: index,
format, physicalDataType, length (with min/max), scale, decimalPositions,
nullSequence, defaultValue, isRequired, and formats_InstanceVariable.
#### json
```json
{
  "@context": {
    "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
    "ex": "https://example.org/"
  },
  "cdif:index": 3,
  "cdif:format": "#,##0.00",
  "cdif:physicalDataType": "Numeric",
  "cdi:length": 12,
  "cdi:minimumLength": 1,
  "cdi:maximumLength": 12,
  "cdi:scale": 1,
  "cdi:decimalPositions": 2,
  "cdi:nullSequence": "NA",
  "cdi:defaultValue": "",
  "cdi:isRequired": true,
  "cdif:formats_InstanceVariable": {
    "@id": "ex:var-temperature"
  }
}

```

#### jsonld
```jsonld
{
  "@context": [
    {
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/"
    },
    "https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifDataType/cdifPhysicalMapping/context.jsonld",
    {
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "ex": "https://example.org/"
    }
  ],
  "cdif:index": 3,
  "cdif:format": "#,##0.00",
  "cdif:physicalDataType": "Numeric",
  "cdi:length": 12,
  "cdi:minimumLength": 1,
  "cdi:maximumLength": 12,
  "cdi:scale": 1,
  "cdi:decimalPositions": 2,
  "cdi:nullSequence": "NA",
  "cdi:defaultValue": "",
  "cdi:isRequired": true,
  "cdif:formats_InstanceVariable": {
    "@id": "ex:var-temperature"
  }
}
```

#### ttl
```ttl
@prefix cdi: <http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/> .
@prefix ex: <https://example.org/> .
@prefix ns1: <cdif:> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

[] ns1:format "#,##0.00" ;
    ns1:formats_InstanceVariable ex:var-temperature ;
    ns1:index 3 ;
    ns1:physicalDataType "Numeric" ;
    cdi:decimalPositions 2 ;
    cdi:defaultValue "" ;
    cdi:isRequired true ;
    cdi:length 12 ;
    cdi:maximumLength 12 ;
    cdi:minimumLength 1 ;
    cdi:nullSequence "NA" ;
    cdi:scale 1 .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: Physical Mapping Type
description: Defines implementation-specific properties for the representation of
  a variable in a dataset. Aligned with CDIF 2026 schema using DDI-CDI flat per-column
  mapping structure.
type: object
properties:
  cdif:index:
    type: integer
    minimum: 0
    description: Non-negative integer that orders the fields in the data structure
      (column number).
  cdif:format:
    type: string
    description: A format for number expressed as a string, or date format like YYYY/MM
      or MM-DD-YY.
  cdif:physicalDataType:
    type: string
  cdi:numberPattern:
    type: string
    description: Number format pattern for the field (PhysicalMapping.numberPattern).
      Text-format properties (column width, decimal/digit-group separators, display
      label) live on cdifTextMapping.
    x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/numberPattern
  cdi:nullSequence:
    type: string
    description: The value of this property becomes the null annotation for the described
      column.
    x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/nullSequence
  cdi:defaultValue:
    type: string
    description: A default string indicating the value to substitute for an empty
      string.
    x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/defaultValue
  cdi:scale:
    type: integer
    x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/scale
  cdi:decimalPositions:
    type: integer
    x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/decimalPositions
  cdi:minimumLength:
    type: integer
    x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/minimumLength
  cdi:maximumLength:
    type: integer
    x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/maximumLength
  cdi:isRequired:
    type: boolean
    default: false
    x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/isRequired
  cdif:formats_InstanceVariable:
    type: object
    description: Reference to a variable defined in schema:variableMeasured.
    properties:
      '@id':
        type: string
        description: This should be a reference to a variable defined in the schema:variableMeasured
          section.
x-jsonld-prefixes:
  schema: http://schema.org/
  ada: https://ada.astromat.org/metadata/
  cdi: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/

```

Links to the schema:

* YAML version: [schema.yaml](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifDataType/cdifPhysicalMapping/schema.json)
* JSON version: [schema.json](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifDataType/cdifPhysicalMapping/schema.yaml)


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
[context.jsonld](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifDataType/cdifPhysicalMapping/context.jsonld)

## Sources

* [ADA Metadata Schema v3](https://github.com/amds-ldeo/metadata)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/Cross-Domain-Interoperability-Framework/metadataBuildingBlocks](https://github.com/Cross-Domain-Interoperability-Framework/metadataBuildingBlocks)
* Path: `_sources/cdifDataType/cdifPhysicalMapping`

