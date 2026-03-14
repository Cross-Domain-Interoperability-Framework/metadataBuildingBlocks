
# CDIF PhysicalMapping bulding block (Schema)

`cdif.bbr.metadata.cdifProperties.cdifPhysicalMapping` *v0.1*

metadata to document the physical serialization of variables in a data structure. Defines properties: cdi:index, cdi:format, cdi:physicalDataType, cdi:length, cdi:nullSequence, cdi:defaultValue, cdi:scale, cdi:decimalPositions, cdi:minimumLength, cdi:maximumLength, cdi:isRequired, cdi:formats_InstanceVariable.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

# Data structure description

Describes tabular/structured data files. Typed as `cdi:PhysicalDataSet` and `ada:tabularData`. Supports DDI-CDI WideDataStructure for column layout description, spatial registration, and various analytical technique-specific component types, hierarchical datastructures like JSON, and multidimensional data array structures serialized in data cube format like hdf5 or netCDF.

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: Physical Mapping Type
description: Defines implementation-specific properties for the representation of
  a variable in a dataset. Aligned with CDIF 2026 schema using DDI-CDI flat per-column
  mapping structure.
type: object
properties:
  cdi:index:
    type: integer
    minimum: 0
    description: Non-negative integer that orders the fields in the data structure
      (column number).
  cdi:format:
    type: string
    description: A format for number expressed as a string, or date format like YYYY/MM
      or MM-DD-YY.
  cdi:physicalDataType:
    type: string
  cdi:length:
    type: integer
    description: The column width if the tabular text is fixed width.
  cdi:nullSequence:
    type: string
    description: The value of this property becomes the null annotation for the described
      column.
  cdi:defaultValue:
    type: string
    description: A default string indicating the value to substitute for an empty
      string.
  cdi:scale:
    type: integer
  cdi:decimalPositions:
    type: integer
  cdi:minimumLength:
    type: integer
  cdi:maximumLength:
    type: integer
  cdi:isRequired:
    type: boolean
    default: false
  cdi:formats_InstanceVariable:
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

* YAML version: [schema.yaml](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifProperties/cdifPhysicalMapping/schema.json)
* JSON version: [schema.json](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifProperties/cdifPhysicalMapping/schema.yaml)


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
[context.jsonld](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifProperties/cdifPhysicalMapping/context.jsonld)

## Sources

* [ADA Metadata Schema v3](https://github.com/amds-ldeo/metadata)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/Cross-Domain-Interoperability-Framework/metadataBuildingBlocks](https://github.com/Cross-Domain-Interoperability-Framework/metadataBuildingBlocks)
* Path: `_sources/cdifProperties/cdifPhysicalMapping`

