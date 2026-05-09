
# DDI-CDI Data Structure Component (Schema)

`cdif.bbr.metadata.ddiProperties.ddicdiDataStructureComponent` *v0.1*

Role given to a represented variable in the context of a long or wide data structure to identify the units associated to data points, and in dimensional and key value data structures to provide identifying fields for the instance values.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

DDI-CDI DataStructureComponent assigns a represented variable a role within a data structure (identifying units, holding observed values, qualifying observations, or standing in for variable identifiers). Polymorphic root over six concrete subclasses: `cdi:IdentifierComponent`, `cdi:MeasureComponent`, `cdi:AttributeComponent`, `cdi:DimensionComponent`, `cdi:VariableValueComponent`, and `cdi:VariableDescriptorComponent`.

Most variants associate the component with a `ddicdiRepresentedVariable` via `cdi:isDefinedBy` (or, for `VariableDescriptorComponent`, a `ddicdiPresentationalVariable`); `DimensionComponent` adds `cdi:isStructuredBy` pointing at a `ddicdiValueDomain`, and `AttributeComponent` carries `cdi:qualifies` linking to other components it describes. All variants support `cdi:semantic` (paired controlled-vocabulary roles) and `cdi:specialization` for harmonization context. Together with `ddicdiDataStructure`, this BB defines the column/dimension/measure roles consumed by physical datasets.

## Examples

### Minimal IdentifierComponent
TODO: replace with a JSON-LD example.
## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: DDI-CDI Data Structure Component
description: Role given to a represented variable in the context of a long or wide
  data structure to identify the units associated to data points, and in dimensional
  and key value data structures to provide identifying fields for the instance values.
anyOf:
- $ref: '#/$defs/IdentifierComponent'
- $ref: '#/$defs/MeasureComponent'
- $ref: '#/$defs/AttributeComponent'
- $ref: '#/$defs/DimensionComponent'
- $ref: '#/$defs/VariableValueComponent'
- $ref: '#/$defs/VariableDescriptorComponent'
$defs:
  IdentifierComponent:
    type: object
    description: Role given to a represented variable in the context of a long or
      wide data structure to identify the units associated to data points, and in
      dimensional and key value data structures to provide identifying fields for
      the instance values.
    properties:
      '@type':
        type: array
        items:
          type: string
        contains:
          const: cdi:IdentifierComponent
        minItems: 1
      '@id':
        type: string
        description: Identifier for this IdentifierComponent node
      cdi:identifier:
        $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/Identifier
        description: Identifier for objects requiring short- or long-lasting referencing
          and management.
      cdi:isDefinedBy:
        anyOf:
        - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiRepresentedVariable/schema.yaml
        - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/id-reference
      cdi:semantic:
        type: array
        items:
          $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/PairedControlledVocabularyEntry
        minItems: 1
        description: Qualifies the purpose or use expressed as a paired external controlled
          vocabulary.
      cdi:specialization:
        $ref: '#/$defs/SpecializationRole'
        description: The role played by the component for the data set for purposes
          of harmonization and integration, typically regarding geography, time, etc.
    required:
    - '@type'
  MeasureComponent:
    type: object
    description: Role given to a represented variable in the context of a data structure
      to hold the observed/derived values.
    properties:
      '@type':
        type: array
        items:
          type: string
        contains:
          const: cdi:MeasureComponent
        minItems: 1
      '@id':
        type: string
        description: Identifier for this MeasureComponent node
      cdi:name:
        type: array
        items:
          $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/ObjectName
        minItems: 1
        description: Human understandable name (liguistic signifier, word, phrase,
          or mnemonic). May follow ISO/IEC 11179-5 naming principles, and have context
          provided to specify usage.
      cdi:identifier:
        $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/Identifier
        description: Identifier for objects requiring short- or long-lasting referencing
          and management.
      cdi:isDefinedBy:
        anyOf:
        - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiRepresentedVariable/schema.yaml
        - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/id-reference
      cdi:semantic:
        type: array
        items:
          $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/PairedControlledVocabularyEntry
        minItems: 1
        description: Qualifies the purpose or use expressed as a paired external controlled
          vocabulary.
      cdi:specialization:
        $ref: '#/$defs/SpecializationRole'
        description: The role played by the component for the data set for purposes
          of harmonization and integration, typically regarding geography, time, etc.
    required:
    - '@type'
  AttributeComponent:
    type: object
    description: Role given to a represented variable in the context of a data structure
      to qualify observations or provide other types of supplementary information.
    properties:
      '@type':
        type: array
        items:
          type: string
        contains:
          const: cdi:AttributeComponent
        minItems: 1
      '@id':
        type: string
        description: Identifier for this AttributeComponent node
      cdi:qualifies:
        type: array
        items:
          anyOf:
          - $ref: '#/$defs/DataStructureComponent'
          - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/id-reference
        minItems: 1
      cdi:identifier:
        $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/Identifier
        description: Identifier for objects requiring short- or long-lasting referencing
          and management.
      cdi:isDefinedBy:
        anyOf:
        - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiRepresentedVariable/schema.yaml
        - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/id-reference
      cdi:semantic:
        type: array
        items:
          $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/PairedControlledVocabularyEntry
        minItems: 1
        description: Qualifies the purpose or use expressed as a paired external controlled
          vocabulary.
      cdi:specialization:
        $ref: '#/$defs/SpecializationRole'
        description: The role played by the component for the data set for purposes
          of harmonization and integration, typically regarding geography, time, etc.
    required:
    - '@type'
  DimensionComponent:
    type: object
    description: Role given to a represented variable in the context of a dimensional
      data structure to identify the universes associated with data points. The variable
      acts as a field in the compound identifier (the key structure) to disambiguate
      the cells in the multi-dimensional "cube".
    properties:
      '@type':
        type: array
        items:
          type: string
        contains:
          const: cdi:DimensionComponent
        minItems: 1
      '@id':
        type: string
        description: Identifier for this DimensionComponent node
      cdi:categoricalAdditivity:
        type: boolean
        description: 'Indicates whether categories at a specific level can be combined
          to provide the value for their shared parent category. Value is True if
          categories can be added together (collapsed) to create higher-level categories.


          An example would be age categories. Five-year age categories can be collapsed
          into 10-year age categories.'
      cdi:isStructuredBy:
        anyOf:
        - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiValueDomain/schema.yaml
        - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/id-reference
      cdi:identifier:
        $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/Identifier
        description: Identifier for objects requiring short- or long-lasting referencing
          and management.
      cdi:isDefinedBy:
        anyOf:
        - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiRepresentedVariable/schema.yaml
        - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/id-reference
      cdi:semantic:
        type: array
        items:
          $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/PairedControlledVocabularyEntry
        minItems: 1
        description: Qualifies the purpose or use expressed as a paired external controlled
          vocabulary.
      cdi:specialization:
        $ref: '#/$defs/SpecializationRole'
        description: The role played by the component for the data set for purposes
          of harmonization and integration, typically regarding geography, time, etc.
    required:
    - '@type'
  VariableValueComponent:
    type: object
    description: Role given to a represented variable in the context of a data structure
      to record values of multiple variables.
    properties:
      '@type':
        type: array
        items:
          type: string
        contains:
          const: cdi:VariableValueComponent
        minItems: 1
      '@id':
        type: string
        description: Identifier for this VariableValueComponent node
      cdi:identifier:
        $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/Identifier
        description: Identifier for objects requiring short- or long-lasting referencing
          and management.
      cdi:isDefinedBy:
        anyOf:
        - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiRepresentedVariable/schema.yaml
        - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/id-reference
      cdi:semantic:
        type: array
        items:
          $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/PairedControlledVocabularyEntry
        minItems: 1
        description: Qualifies the purpose or use expressed as a paired external controlled
          vocabulary.
      cdi:specialization:
        $ref: '#/$defs/SpecializationRole'
        description: The role played by the component for the data set for purposes
          of harmonization and integration, typically regarding geography, time, etc.
    required:
    - '@type'
  VariableDescriptorComponent:
    type: object
    description: Role given to a represented variable in the context of a data structure
      to provide codes for variable identification.
    properties:
      '@type':
        type: array
        items:
          type: string
        contains:
          const: cdi:VariableDescriptorComponent
        minItems: 1
      '@id':
        type: string
        description: Identifier for this VariableDescriptorComponent node
      cdi:isDefinedBy:
        anyOf:
        - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiPresentationalVariable/schema.yaml
        - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/id-reference
      cdi:refersTo:
        anyOf:
        - $ref: '#/$defs/VariableValueComponent'
        - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/id-reference
      cdi:identifier:
        $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/Identifier
        description: Identifier for objects requiring short- or long-lasting referencing
          and management.
      cdi:semantic:
        type: array
        items:
          $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/PairedControlledVocabularyEntry
        minItems: 1
        description: Qualifies the purpose or use expressed as a paired external controlled
          vocabulary.
      cdi:specialization:
        $ref: '#/$defs/SpecializationRole'
        description: The role played by the component for the data set for purposes
          of harmonization and integration, typically regarding geography, time, etc.
    required:
    - '@type'
  DataStructureComponent:
    type: object
    description: Role given to a represented variable in the context of a data structure.
    properties:
      '@type':
        type: array
        items:
          type: string
        contains:
          const: cdi:DataStructureComponent
        minItems: 1
      '@id':
        type: string
        description: Identifier for this DataStructureComponent node
      cdi:identifier:
        $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/Identifier
        description: Identifier for objects requiring short- or long-lasting referencing
          and management.
      cdi:isDefinedBy:
        anyOf:
        - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiRepresentedVariable/schema.yaml
        - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/id-reference
      cdi:semantic:
        type: array
        items:
          $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/PairedControlledVocabularyEntry
        minItems: 1
        description: Qualifies the purpose or use expressed as a paired external controlled
          vocabulary.
      cdi:specialization:
        $ref: '#/$defs/SpecializationRole'
        description: The role played by the component for the data set for purposes
          of harmonization and integration, typically regarding geography, time, etc.
    required:
    - '@type'
  SpecializationRole:
    type: object
    description: Specific roles played by represented variables in terms of time,
      geography, and other concepts which are important for the harmonization and
      integration of data.
    properties:
      '@type':
        type: array
        items:
          type: string
        contains:
          const: cdi:SpecializationRole
        minItems: 1
x-jsonld-prefixes:
  cdi: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/

```

Links to the schema:

* YAML version: [schema.yaml](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataStructureComponent/schema.json)
* JSON version: [schema.json](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataStructureComponent/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
    "skos": "http://www.w3.org/2004/02/skos/core#",
    "schema": "http://schema.org/",
    "spdx": "http://spdx.org/rdf/terms#",
    "xas": "https://xas.org/dictionary/",
    "nxs": "http://purl.org/nexusformat/definitions/",
    "prov": "http://www.w3.org/ns/prov#",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataStructureComponent/context.jsonld)

## Sources

* [DDI-CDI 1.0 Specification](https://ddialliance.org/Specification/DDI-CDI/1.0/)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/Cross-Domain-Interoperability-Framework/metadataBuildingBlocks](https://github.com/Cross-Domain-Interoperability-Framework/metadataBuildingBlocks)
* Path: `_sources/ddiProperties/ddicdiDataStructureComponent`

