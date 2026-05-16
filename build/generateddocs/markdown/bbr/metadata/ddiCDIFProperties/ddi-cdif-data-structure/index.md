
# DDI-CDI Data Structure (Schema)

`cdif.bbr.metadata.ddiCDIFProperties.ddi-cdif-data-structure` *v0.1*

Data organization based on reusable data structure components.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

DDI-CDI DataStructure describes how a dataset is organized in terms of reusable data structure components. Polymorphic root over `cdi:DataStructure`, `cdi:DimensionalDataStructure`, `cdi:LongDataStructure`, and `cdi:WideDataStructure` — one variant per logical layout supported by DDI-CDI.

Each variant carries `cdi:has_DataStructureComponent` (referencing the `ddicdiDataStructureComponent` BB), `cdi:has_ComponentPosition` for ordering, optional `cdi:has_PrimaryKey` and `cdi:has_ForeignKey` for referential structure, and a `cdi:specialization` slot for harmonization-related roles (time, geography, etc.). `DimensionalDataStructure` additionally references reusable `cdi:DimensionGroup` collections via `cdi:uses`. The BB is referenced from `ddicdiPhysicalDataSet` (`cdi:isStructuredBy`) and is the structural anchor for tabular, dimensional, and long/wide layouts in the CDIF Data Description profile.

## Examples

### Minimal DataStructure
TODO: replace with a JSON-LD example.
## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: DDI-CDI Data Structure
description: Data organization based on reusable data structure components.
anyOf:
- $ref: '#/$defs/DataStructure'
- $ref: '#/$defs/DimensionalDataStructure'
- $ref: '#/$defs/LongDataStructure'
- $ref: '#/$defs/WideDataStructure'
$defs:
  DataStructure:
    type: object
    description: Data organization based on reusable data structure components.
    properties:
      '@type':
        type: array
        items:
          type: string
        contains:
          const: cdi:DataStructure
        minItems: 1
      '@id':
        type: string
        description: Identifier for this DataStructure node
      cdi:has_ForeignKey:
        type: array
        items:
          anyOf:
          - $ref: '#/$defs/ForeignKey'
          - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiCDIFProperties/ddi-cdif-data-types/schema.yaml#/$defs/id-reference
        minItems: 1
      cdi:has_DataStructureComponent:
        type: array
        items:
          anyOf:
          - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiCDIFProperties/ddi-cdif-data-structure-component/schema.yaml
          - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiCDIFProperties/ddi-cdif-data-types/schema.yaml#/$defs/id-reference
        minItems: 1
      cdi:has_PrimaryKey:
        anyOf:
        - $ref: '#/$defs/PrimaryKey'
        - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiCDIFProperties/ddi-cdif-data-types/schema.yaml#/$defs/id-reference
      cdi:identifier:
        $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiCDIFProperties/ddi-cdif-data-types/schema.yaml#/$defs/Identifier
        description: Identifier for objects requiring short- or long-lasting referencing
          and management.
      cdi:semantic:
        type: array
        items:
          $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiCDIFProperties/ddi-cdif-data-types/schema.yaml#/$defs/PairedControlledVocabularyEntry
        minItems: 1
        description: Qualifies the purpose or use expressed as a paired external controlled
          vocabulary.
    required:
    - '@type'
  DimensionalDataStructure:
    type: object
    description: Structure of a dimensional data set (organized collection of multidimensional
      data). It is described by dimension, measure and attribute components.
    properties:
      '@type':
        type: array
        items:
          type: string
        contains:
          const: cdi:DimensionalDataStructure
        minItems: 1
      '@id':
        type: string
        description: Identifier for this DimensionalDataStructure node
      cdi:has_DataStructureComponent:
        type: array
        items:
          anyOf:
          - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiCDIFProperties/ddi-cdif-data-structure-component/schema.yaml
          - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiCDIFProperties/ddi-cdif-data-types/schema.yaml#/$defs/id-reference
        minItems: 1
      cdi:has_PrimaryKey:
        anyOf:
        - $ref: '#/$defs/PrimaryKey'
        - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiCDIFProperties/ddi-cdif-data-types/schema.yaml#/$defs/id-reference
    required:
    - '@type'
    - cdi:has_DataStructureComponent
    - cdi:has_PrimaryKey
  LongDataStructure:
    type: object
    description: Structure of a long dataset (organized collection of long data).
      It is described by identifier, measure, attribute, variable descriptor and variable
      value components.
    properties:
      '@type':
        type: array
        items:
          type: string
        contains:
          const: cdi:LongDataStructure
        minItems: 1
      '@id':
        type: string
        description: Identifier for this LongDataStructure node
      cdi:has_DataStructureComponent:
        type: array
        items:
          anyOf:
          - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiCDIFProperties/ddi-cdif-data-structure-component/schema.yaml
          - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiCDIFProperties/ddi-cdif-data-types/schema.yaml#/$defs/id-reference
        minItems: 1
      cdi:has_PrimaryKey:
        anyOf:
        - $ref: '#/$defs/PrimaryKey'
        - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiCDIFProperties/ddi-cdif-data-types/schema.yaml#/$defs/id-reference
    required:
    - '@type'
  WideDataStructure:
    type: object
    description: Structure of a wide dataset (organized collection of wide data).
      It is described by identifier, measure and attribute components.
    properties:
      '@type':
        type: array
        items:
          type: string
        contains:
          const: cdi:WideDataStructure
        minItems: 1
      '@id':
        type: string
        description: Identifier for this WideDataStructure node
      cdi:has_DataStructureComponent:
        type: array
        items:
          anyOf:
          - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiCDIFProperties/ddi-cdif-data-structure-component/schema.yaml
          - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiCDIFProperties/ddi-cdif-data-types/schema.yaml#/$defs/id-reference
        minItems: 1
      cdi:has_PrimaryKey:
        anyOf:
        - $ref: '#/$defs/PrimaryKey'
        - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiCDIFProperties/ddi-cdif-data-types/schema.yaml#/$defs/id-reference
    required:
    - '@type'
    - cdi:has_DataStructureComponent
  ComponentPosition:
    type: object
    description: Indexes the components in a data structure using integers with a
      position indicated by incrementing upward from 0 or 1.
    properties:
      '@type':
        type: array
        items:
          type: string
        contains:
          const: cdi:ComponentPosition
        minItems: 1
      '@id':
        type: string
        description: Identifier for this ComponentPosition node
      cdi:indexes:
        anyOf:
        - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiCDIFProperties/ddi-cdif-data-structure-component/schema.yaml
        - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiCDIFProperties/ddi-cdif-data-types/schema.yaml#/$defs/id-reference
      cdi:value:
        type: integer
        description: Index value of the member in an ordered array.
    required:
    - '@type'
    - cdi:indexes
    - cdi:value
  DimensionGroup:
    type: object
    description: Collection of dimensions that can be reused across multiple dimensional
      structures.
    properties:
      '@type':
        type: array
        items:
          type: string
        contains:
          const: cdi:DimensionGroup
        minItems: 1
      '@id':
        type: string
        description: Identifier for this DimensionGroup node
      cdi:identifier:
        $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiCDIFProperties/ddi-cdif-data-types/schema.yaml#/$defs/Identifier
        description: Identifier for objects requiring short- or long-lasting referencing
          and management.
      cdi:name:
        type: array
        items:
          $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiCDIFProperties/ddi-cdif-data-types/schema.yaml#/$defs/ObjectName
        minItems: 1
        description: Human understandable name (liguistic signifier, word, phrase,
          or mnemonic). May follow ISO/IEC 11179-5 naming principles, and have context
          provided to specify usage.
      cdi:has:
        type: array
        items:
          anyOf:
          - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiCDIFProperties/ddi-cdif-data-structure-component/schema.yaml
          - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiCDIFProperties/ddi-cdif-data-types/schema.yaml#/$defs/id-reference
        minItems: 1
    required:
    - '@type'
  ForeignKey:
    type: object
    description: Role of a set of data structure components for content referencing
      purposes
    properties:
      '@type':
        type: array
        items:
          type: string
        contains:
          const: cdi:ForeignKey
        minItems: 1
      '@id':
        type: string
        description: Identifier for this ForeignKey node
      cdi:identifier:
        $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiCDIFProperties/ddi-cdif-data-types/schema.yaml#/$defs/Identifier
        description: Identifier for objects requiring short- or long-lasting referencing
          and management.
      cdi:isComposedOf:
        type: array
        items:
          anyOf:
          - $ref: '#/$defs/ForeignKeyComponent'
          - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiCDIFProperties/ddi-cdif-data-types/schema.yaml#/$defs/id-reference
        minItems: 1
    required:
    - '@type'
  ForeignKeyComponent:
    type: object
    description: Role of a data structure component for content referencing purposes
    properties:
      '@type':
        type: array
        items:
          type: string
        contains:
          const: cdi:ForeignKeyComponent
        minItems: 1
      '@id':
        type: string
        description: Identifier for this ForeignKeyComponent node
      cdi:identifier:
        $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiCDIFProperties/ddi-cdif-data-types/schema.yaml#/$defs/Identifier
        description: Identifier for objects requiring short- or long-lasting referencing
          and management.
      cdi:references:
        anyOf:
        - $ref: '#/$defs/PrimaryKeyComponent'
        - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiCDIFProperties/ddi-cdif-data-types/schema.yaml#/$defs/id-reference
      cdi:correspondsTo:
        anyOf:
        - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiCDIFProperties/ddi-cdif-data-structure-component/schema.yaml
        - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiCDIFProperties/ddi-cdif-data-types/schema.yaml#/$defs/id-reference
    required:
    - '@type'
  PrimaryKey:
    type: object
    description: Role of a set of data structure components that uniquely identify
      data instance
    properties:
      '@type':
        type: array
        items:
          type: string
        contains:
          const: cdif:PrimaryKey
        minItems: 1
      '@id':
        type: string
        description: Identifier for this PrimaryKey node
      cdif:isComposedOf:
        type: array
        items:
          type: object
          description: Indexes the components in a data structure using integers with
            a position indicated by incrementing upward from 0 or 1.
          properties:
            '@type':
              type: array
              items:
                type: string
              contains:
                const: cdi:ComponentPosition
              minItems: 1
            '@id':
              type: string
              description: Identifier for this ComponentPosition node
            cdi:indexes:
              anyOf:
              - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiCDIFProperties/ddi-cdif-data-structure-component/schema.yaml
              - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiCDIFProperties/ddi-cdif-data-types/schema.yaml#/$defs/id-reference
            cdi:value:
              type: integer
              description: Index value of the member in an ordered array.
          required:
          - '@type'
          - cdi:indexes
          - cdi:value
        minItems: 1
    required:
    - '@type'
  PrimaryKeyComponent:
    type: object
    description: Role of a data structure component for content identification purposes
    properties:
      '@type':
        type: array
        items:
          type: string
        contains:
          const: cdi:PrimaryKeyComponent
        minItems: 1
      '@id':
        type: string
        description: Identifier for this PrimaryKeyComponent node
      cdi:identifier:
        $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiCDIFProperties/ddi-cdif-data-types/schema.yaml#/$defs/Identifier
        description: Identifier for objects requiring short- or long-lasting referencing
          and management.
      cdi:correspondsTo:
        anyOf:
        - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiCDIFProperties/ddi-cdif-data-structure-component/schema.yaml
        - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiCDIFProperties/ddi-cdif-data-types/schema.yaml#/$defs/id-reference
    required:
    - '@type'
x-jsonld-prefixes:
  cdi: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/

```

Links to the schema:

* YAML version: [schema.yaml](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiCDIFProperties/ddi-cdif-data-structure/schema.json)
* JSON version: [schema.json](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiCDIFProperties/ddi-cdif-data-structure/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
    "skos": "http://www.w3.org/2004/02/skos/core#",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiCDIFProperties/ddi-cdif-data-structure/context.jsonld)

## Sources

* [DDI-CDI 1.0 Specification](https://ddialliance.org/Specification/DDI-CDI/1.0/)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/Cross-Domain-Interoperability-Framework/metadataBuildingBlocks](https://github.com/Cross-Domain-Interoperability-Framework/metadataBuildingBlocks)
* Path: `_sources/ddiCDIFProperties/ddi-cdif-data-structure`

