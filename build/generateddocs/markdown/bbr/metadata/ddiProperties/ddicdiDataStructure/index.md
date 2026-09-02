
# DDI-CDI Data Structure (Schema)

`cdif.bbr.metadata.ddiProperties.ddicdiDataStructure` *v0.1*

Data organization based on reusable data structure components.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

DDI-CDI DataStructure describes how a dataset is organized in terms of reusable data structure components. Polymorphic root over `cdi:DataStructure`, `cdi:DimensionalDataStructure`, `cdi:LongDataStructure`, and `cdi:WideDataStructure` — one variant per logical layout supported by DDI-CDI.

Each variant carries `cdi:has_DataStructureComponent` (referencing the `ddicdiDataStructureComponent` BB), `cdi:has_ComponentPosition` for ordering, optional `cdi:has_PrimaryKey` and `cdi:has_ForeignKey` for referential structure, and a `cdi:specialization` slot for harmonization-related roles (time, geography, etc.). `DimensionalDataStructure` additionally references reusable `cdi:DimensionGroup` collections via `cdi:uses`. The BB is referenced from `ddicdiPhysicalDataSet` (`cdi:isStructuredBy`) and is the structural anchor for tabular, dimensional, and long/wide layouts in the CDIF Data Description profile.

## Examples

### Example DDI-CDI wide data structure.
A WideDataStructure for a daily air-temperature series, in which each
logical record is one row and each component is one column. Demonstrates
an IdentifierComponent and a MeasureComponent, each deferring its
semantics to a RepresentedVariable via cdi:isDefinedBy, and a PrimaryKey
whose PrimaryKeyComponent points at the identifier column.

Components declare a concrete subtype (cdi:IdentifierComponent,
cdi:MeasureComponent) rather than the abstract cdi:DataStructureComponent,
which the schema requires: the subtype states what role the column plays.
#### json
```json
{
  "@context": {
    "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
    "ex": "https://example.org/"
  },
  "@id": "ex:struct/dailyTemperature",
  "@type": [
    "cdi:WideDataStructure"
  ],
  "cdi:identifier": {
    "@type": [
      "cdi:Identifier"
    ],
    "cdi:ddiIdentifier": {
      "@type": [
        "cdi:InternationalRegistrationDataIdentifier"
      ],
      "cdi:dataIdentifier": "struct-daily-temperature",
      "cdi:registrationAuthorityIdentifier": "example.org",
      "cdi:versionIdentifier": "1"
    }
  },
  "cdi:has_DataStructureComponent": [
    {
      "@id": "ex:struct/dailyTemperature/comp/observationDate",
      "@type": [
        "cdi:IdentifierComponent"
      ],
      "cdi:isDefinedBy": {
        "@id": "ex:rv/observationDate"
      }
    },
    {
      "@id": "ex:struct/dailyTemperature/comp/airTemperature",
      "@type": [
        "cdi:MeasureComponent"
      ],
      "cdi:name": [
        {
          "@type": [
            "cdi:ObjectName"
          ],
          "cdi:name": "airTemperature"
        }
      ],
      "cdi:isDefinedBy": {
        "@id": "ex:rv/airTemperature"
      }
    }
  ],
  "cdi:has_PrimaryKey": {
    "@id": "ex:struct/dailyTemperature/pk",
    "@type": [
      "cdi:PrimaryKey"
    ],
    "cdi:has_PrimaryKeyComponent": [
      {
        "@id": "ex:struct/dailyTemperature/pk/comp1",
        "@type": [
          "cdi:PrimaryKeyComponent"
        ],
        "cdi:correspondsTo_DataStructureComponent": {
          "@id": "ex:struct/dailyTemperature/comp/observationDate"
        }
      }
    ]
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
    "https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataStructure/context.jsonld",
    {
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "ex": "https://example.org/"
    }
  ],
  "@id": "ex:struct/dailyTemperature",
  "@type": [
    "cdi:WideDataStructure"
  ],
  "cdi:identifier": {
    "@type": [
      "cdi:Identifier"
    ],
    "cdi:ddiIdentifier": {
      "@type": [
        "cdi:InternationalRegistrationDataIdentifier"
      ],
      "cdi:dataIdentifier": "struct-daily-temperature",
      "cdi:registrationAuthorityIdentifier": "example.org",
      "cdi:versionIdentifier": "1"
    }
  },
  "cdi:has_DataStructureComponent": [
    {
      "@id": "ex:struct/dailyTemperature/comp/observationDate",
      "@type": [
        "cdi:IdentifierComponent"
      ],
      "cdi:isDefinedBy": {
        "@id": "ex:rv/observationDate"
      }
    },
    {
      "@id": "ex:struct/dailyTemperature/comp/airTemperature",
      "@type": [
        "cdi:MeasureComponent"
      ],
      "cdi:name": [
        {
          "@type": [
            "cdi:ObjectName"
          ],
          "cdi:name": "airTemperature"
        }
      ],
      "cdi:isDefinedBy": {
        "@id": "ex:rv/airTemperature"
      }
    }
  ],
  "cdi:has_PrimaryKey": {
    "@id": "ex:struct/dailyTemperature/pk",
    "@type": [
      "cdi:PrimaryKey"
    ],
    "cdi:has_PrimaryKeyComponent": [
      {
        "@id": "ex:struct/dailyTemperature/pk/comp1",
        "@type": [
          "cdi:PrimaryKeyComponent"
        ],
        "cdi:correspondsTo_DataStructureComponent": {
          "@id": "ex:struct/dailyTemperature/comp/observationDate"
        }
      }
    ]
  }
}
```

#### ttl
```ttl
@prefix cdi: <http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/> .

<https://example.org/struct/dailyTemperature> a cdi:WideDataStructure ;
    cdi:has_DataStructureComponent <https://example.org/struct/dailyTemperature/comp/airTemperature>,
        <https://example.org/struct/dailyTemperature/comp/observationDate> ;
    cdi:has_PrimaryKey <https://example.org/struct/dailyTemperature/pk> ;
    cdi:identifier [ a cdi:Identifier ;
            cdi:ddiIdentifier [ a cdi:InternationalRegistrationDataIdentifier ;
                    cdi:dataIdentifier "struct-daily-temperature" ;
                    cdi:registrationAuthorityIdentifier "example.org" ;
                    cdi:versionIdentifier "1" ] ] .

<https://example.org/struct/dailyTemperature/comp/airTemperature> a cdi:MeasureComponent ;
    cdi:isDefinedBy <https://example.org/rv/airTemperature> ;
    cdi:name [ a cdi:ObjectName ;
            cdi:name "airTemperature" ] .

<https://example.org/struct/dailyTemperature/pk> a cdi:PrimaryKey ;
    cdi:has_PrimaryKeyComponent <https://example.org/struct/dailyTemperature/pk/comp1> .

<https://example.org/struct/dailyTemperature/pk/comp1> a cdi:PrimaryKeyComponent ;
    cdi:correspondsTo_DataStructureComponent <https://example.org/struct/dailyTemperature/comp/observationDate> .

<https://example.org/struct/dailyTemperature/comp/observationDate> a cdi:IdentifierComponent ;
    cdi:isDefinedBy <https://example.org/rv/observationDate> .


```

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
          - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/id-reference
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/has_ForeignKey
      cdi:has_DataStructureComponent:
        type: array
        items:
          anyOf:
          - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataStructureComponent/schema.yaml
          - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/id-reference
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/has_DataStructureComponent
      cdi:has_ComponentPosition:
        type: array
        items:
          anyOf:
          - $ref: '#/$defs/ComponentPosition'
          - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/id-reference
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/has_ComponentPosition
      cdi:has_PrimaryKey:
        anyOf:
        - $ref: '#/$defs/PrimaryKey'
        - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/id-reference
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/has_PrimaryKey
      cdi:identifier:
        $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/Identifier
        description: Identifier for objects requiring short- or long-lasting referencing
          and management.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/identifier
      cdi:semantic:
        type: array
        items:
          $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/PairedControlledVocabularyEntry
        description: Qualifies the purpose or use expressed as a paired external controlled
          vocabulary.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/semantic
      cdi:specialization:
        $ref: '#/$defs/SpecializationRole'
        description: The role played by the component for the data set for purposes
          of harmonization and integration, typically regarding geography, time, etc.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/specialization
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
      cdi:uses:
        type: array
        items:
          anyOf:
          - $ref: '#/$defs/DimensionGroup'
          - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/id-reference
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/uses
      cdi:has_ForeignKey:
        type: array
        items:
          anyOf:
          - $ref: '#/$defs/ForeignKey'
          - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/id-reference
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/has_ForeignKey
      cdi:has_DataStructureComponent:
        type: array
        items:
          anyOf:
          - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataStructureComponent/schema.yaml
          - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/id-reference
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/has_DataStructureComponent
      cdi:has_ComponentPosition:
        type: array
        items:
          anyOf:
          - $ref: '#/$defs/ComponentPosition'
          - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/id-reference
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/has_ComponentPosition
      cdi:has_PrimaryKey:
        anyOf:
        - $ref: '#/$defs/PrimaryKey'
        - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/id-reference
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/has_PrimaryKey
      cdi:identifier:
        $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/Identifier
        description: Identifier for objects requiring short- or long-lasting referencing
          and management.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/identifier
      cdi:semantic:
        type: array
        items:
          $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/PairedControlledVocabularyEntry
        description: Qualifies the purpose or use expressed as a paired external controlled
          vocabulary.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/semantic
      cdi:specialization:
        $ref: '#/$defs/SpecializationRole'
        description: The role played by the component for the data set for purposes
          of harmonization and integration, typically regarding geography, time, etc.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/specialization
    required:
    - '@type'
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
      cdi:has_ForeignKey:
        type: array
        items:
          anyOf:
          - $ref: '#/$defs/ForeignKey'
          - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/id-reference
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/has_ForeignKey
      cdi:has_DataStructureComponent:
        type: array
        items:
          anyOf:
          - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataStructureComponent/schema.yaml
          - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/id-reference
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/has_DataStructureComponent
      cdi:has_ComponentPosition:
        type: array
        items:
          anyOf:
          - $ref: '#/$defs/ComponentPosition'
          - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/id-reference
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/has_ComponentPosition
      cdi:has_PrimaryKey:
        anyOf:
        - $ref: '#/$defs/PrimaryKey'
        - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/id-reference
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/has_PrimaryKey
      cdi:identifier:
        $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/Identifier
        description: Identifier for objects requiring short- or long-lasting referencing
          and management.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/identifier
      cdi:semantic:
        type: array
        items:
          $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/PairedControlledVocabularyEntry
        description: Qualifies the purpose or use expressed as a paired external controlled
          vocabulary.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/semantic
      cdi:specialization:
        $ref: '#/$defs/SpecializationRole'
        description: The role played by the component for the data set for purposes
          of harmonization and integration, typically regarding geography, time, etc.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/specialization
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
      cdi:has_ForeignKey:
        type: array
        items:
          anyOf:
          - $ref: '#/$defs/ForeignKey'
          - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/id-reference
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/has_ForeignKey
      cdi:has_DataStructureComponent:
        type: array
        items:
          anyOf:
          - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataStructureComponent/schema.yaml
          - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/id-reference
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/has_DataStructureComponent
      cdi:has_ComponentPosition:
        type: array
        items:
          anyOf:
          - $ref: '#/$defs/ComponentPosition'
          - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/id-reference
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/has_ComponentPosition
      cdi:has_PrimaryKey:
        anyOf:
        - $ref: '#/$defs/PrimaryKey'
        - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/id-reference
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/has_PrimaryKey
      cdi:identifier:
        $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/Identifier
        description: Identifier for objects requiring short- or long-lasting referencing
          and management.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/identifier
      cdi:semantic:
        type: array
        items:
          $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/PairedControlledVocabularyEntry
        description: Qualifies the purpose or use expressed as a paired external controlled
          vocabulary.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/semantic
      cdi:specialization:
        $ref: '#/$defs/SpecializationRole'
        description: The role played by the component for the data set for purposes
          of harmonization and integration, typically regarding geography, time, etc.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/specialization
    required:
    - '@type'
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
      cdi:identifier:
        $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/Identifier
        description: Identifier for objects requiring short- or long-lasting referencing
          and management.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/identifier
      cdi:value:
        type: integer
        description: Index value of the member in an ordered array.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/value
      cdi:indexes:
        anyOf:
        - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataStructureComponent/schema.yaml
        - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/id-reference
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/indexes
    required:
    - '@type'
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
        $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/Identifier
        description: Identifier for objects requiring short- or long-lasting referencing
          and management.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/identifier
      cdi:name:
        type: array
        items:
          $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/ObjectName
        description: Human understandable name (linguistic signifier, word, phrase,
          or mnemonic). May follow ISO/IEC 11179-5 naming principles, and have context
          provided to specify usage.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/name
      cdi:has:
        type: array
        items:
          anyOf:
          - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataStructureComponent/schema.yaml
          - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/id-reference
        minItems: 1
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/has
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
        $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/Identifier
        description: Identifier for objects requiring short- or long-lasting referencing
          and management.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/identifier
      cdi:isComposedOf:
        type: array
        items:
          anyOf:
          - $ref: '#/$defs/ForeignKeyComponent'
          - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/id-reference
        minItems: 1
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/isComposedOf
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
        $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/Identifier
        description: Identifier for objects requiring short- or long-lasting referencing
          and management.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/identifier
      cdi:references:
        anyOf:
        - $ref: '#/$defs/PrimaryKeyComponent'
        - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/id-reference
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/references
      cdi:correspondsTo:
        anyOf:
        - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataStructureComponent/schema.yaml
        - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/id-reference
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/correspondsTo
    required:
    - '@type'
  PrimaryKey:
    type: object
    description: Role of a set of data structure components for content linkage purposes
    properties:
      '@type':
        type: array
        items:
          type: string
        contains:
          const: cdi:PrimaryKey
        minItems: 1
      '@id':
        type: string
        description: Identifier for this PrimaryKey node
      cdi:identifier:
        $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/Identifier
        description: Identifier for objects requiring short- or long-lasting referencing
          and management.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/identifier
      cdi:isComposedOf:
        type: array
        items:
          anyOf:
          - $ref: '#/$defs/PrimaryKeyComponent'
          - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/id-reference
        minItems: 1
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/isComposedOf
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
        $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/Identifier
        description: Identifier for objects requiring short- or long-lasting referencing
          and management.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/identifier
      cdi:correspondsTo:
        anyOf:
        - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataStructureComponent/schema.yaml
        - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/id-reference
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/correspondsTo
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

* YAML version: [schema.yaml](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataStructure/schema.json)
* JSON version: [schema.json](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataStructure/schema.yaml)


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
[context.jsonld](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataStructure/context.jsonld)

## Sources

* [DDI-CDI 1.0 Specification](https://ddialliance.org/Specification/DDI-CDI/1.0/)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/Cross-Domain-Interoperability-Framework/metadataBuildingBlocks](https://github.com/Cross-Domain-Interoperability-Framework/metadataBuildingBlocks)
* Path: `_sources/ddiProperties/ddicdiDataStructure`

