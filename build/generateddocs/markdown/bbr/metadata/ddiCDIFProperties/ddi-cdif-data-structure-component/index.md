
# DDI-CDI Data Structure Component (Schema)

`cdif.bbr.metadata.ddiCDIFProperties.ddi-cdif-data-structure-component` *v0.1*

Role given to a represented variable in the context of a long or wide data structure to identify the units associated to data points, and in dimensional and key value data structures to provide identifying fields for the instance values.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

DDI-CDI DataStructureComponent assigns a represented variable a role within a data structure (identifying units, holding observed values, qualifying observations, or standing in for variable identifiers). Polymorphic root over six concrete subclasses: `cdi:IdentifierComponent`, `cdi:MeasureComponent`, `cdi:AttributeComponent`, `cdi:DimensionComponent`, `cdi:VariableValueComponent`, and `cdi:VariableDescriptorComponent`.

Most variants associate the component with a `ddicdiRepresentedVariable` via `cdi:isDefinedBy` (or, for `VariableDescriptorComponent`, a `ddicdiPresentationalVariable`); `DimensionComponent` adds `cdi:isStructuredBy` pointing at a `ddicdiValueDomain`, and `AttributeComponent` carries `cdi:qualifies` linking to other components it describes. All variants support `cdi:semantic` (paired controlled-vocabulary roles) and `cdi:specialization` for harmonization context. Together with `ddicdiDataStructure`, this BB defines the column/dimension/measure roles consumed by physical datasets.

## Examples

### Minimal DataStructureComponent (MeasureComponent)
A bare MeasureComponent with just @type, @id, and the SHACL-recommended
cdi:isDefinedBy @id-ref to a RepresentedVariable. The other component
subtypes (IdentifierComponent, AttributeComponent, DimensionComponent,
VariableValueComponent, VariableDescriptorComponent) follow the same
minimal shape.
#### json
```json
{
  "@context": {
    "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
    "ex": "https://example.org/"
  },
  "@type": ["cdi:MeasureComponent"],
  "@id": "ex:component/temperature",
  "cdi:isDefinedBy": { "@id": "ex:rep-var/temperature" }
}

```

#### jsonld
```jsonld
{
  "@context": [
    {
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/"
    },
    "https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiCDIFProperties/ddi-cdif-data-structure-component/context.jsonld",
    {
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "ex": "https://example.org/"
    }
  ],
  "@type": [
    "cdi:MeasureComponent"
  ],
  "@id": "ex:component/temperature",
  "cdi:isDefinedBy": {
    "@id": "ex:rep-var/temperature"
  }
}
```

#### ttl
```ttl
@prefix cdi: <http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/> .

<https://example.org/component/temperature> a cdi:MeasureComponent ;
    cdi:isDefinedBy <https://example.org/rep-var/temperature> .


```


### Complete DataStructureComponent (MeasureComponent)
Fully-described MeasureComponent exercising cdi:identifier, cdi:name,
cdi:isDefinedBy, and cdi:semantic (PairedControlledVocabularyEntry
with purpose and use entries linked to QUDT).
#### json
```json
{
  "@context": {
    "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
    "ex": "https://example.org/"
  },
  "@type": ["cdi:MeasureComponent"],
  "@id": "ex:component/temperature",
  "cdi:identifier": {
    "@type": ["cdi:Identifier"],
    "cdi:uri": "https://example.org/component/temperature"
  },
  "cdi:name": [
    {
      "@type": ["cdi:ObjectName"],
      "cdi:name": "temperature"
    }
  ],
  "cdi:isDefinedBy": { "@id": "ex:rep-var/temperature" },
  "cdi:semantic": [
    {
      "@type": ["cdi:PairedControlledVocabularyEntry"],
      "cdi:purposeEntry": {
        "@type": ["cdi:ControlledVocabularyEntry"],
        "cdi:entryValue": ["temperature"],
        "cdi:vocabulary": {
          "@type": ["cdif:Reference"],
          "cdi:uri": "https://qudt.org/vocab/quantitykind/Temperature"
        }
      },
      "cdi:useEntry": {
        "@type": ["cdi:ControlledVocabularyEntry"],
        "cdi:entryValue": ["measurement"]
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
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/"
    },
    "https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiCDIFProperties/ddi-cdif-data-structure-component/context.jsonld",
    {
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "ex": "https://example.org/"
    }
  ],
  "@type": [
    "cdi:MeasureComponent"
  ],
  "@id": "ex:component/temperature",
  "cdi:identifier": {
    "@type": [
      "cdi:Identifier"
    ],
    "cdi:uri": "https://example.org/component/temperature"
  },
  "cdi:name": [
    {
      "@type": [
        "cdi:ObjectName"
      ],
      "cdi:name": "temperature"
    }
  ],
  "cdi:isDefinedBy": {
    "@id": "ex:rep-var/temperature"
  },
  "cdi:semantic": [
    {
      "@type": [
        "cdi:PairedControlledVocabularyEntry"
      ],
      "cdi:purposeEntry": {
        "@type": [
          "cdi:ControlledVocabularyEntry"
        ],
        "cdi:entryValue": [
          "temperature"
        ],
        "cdi:vocabulary": {
          "@type": [
            "cdif:Reference"
          ],
          "cdi:uri": "https://qudt.org/vocab/quantitykind/Temperature"
        }
      },
      "cdi:useEntry": {
        "@type": [
          "cdi:ControlledVocabularyEntry"
        ],
        "cdi:entryValue": [
          "measurement"
        ]
      }
    }
  ]
}
```

#### ttl
```ttl
@prefix cdi: <http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/> .

<https://example.org/component/temperature> a cdi:MeasureComponent ;
    cdi:identifier [ a cdi:Identifier ;
            cdi:uri "https://example.org/component/temperature" ] ;
    cdi:isDefinedBy <https://example.org/rep-var/temperature> ;
    cdi:name [ a cdi:ObjectName ;
            cdi:name "temperature" ] ;
    cdi:semantic [ a cdi:PairedControlledVocabularyEntry ;
            cdi:purposeEntry [ a cdi:ControlledVocabularyEntry ;
                    cdi:entryValue "temperature" ;
                    cdi:vocabulary [ a <cdif:Reference> ;
                            cdi:uri "https://qudt.org/vocab/quantitykind/Temperature" ] ] ;
            cdi:useEntry [ a cdi:ControlledVocabularyEntry ;
                    cdi:entryValue "measurement" ] ] .


```

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
      cdi:isDefinedBy:
        anyOf:
        - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiCDIFProperties/ddi-cdif-represented-variable/schema.yaml
        - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiCDIFProperties/ddi-cdif-data-types/schema.yaml#/$defs/id-reference
    required:
    - '@type'
    - cdi:isDefinedBy
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
          $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiCDIFProperties/ddi-cdif-data-types/schema.yaml#/$defs/ObjectName
        minItems: 1
        description: Human understandable name (liguistic signifier, word, phrase,
          or mnemonic). May follow ISO/IEC 11179-5 naming principles, and have context
          provided to specify usage.
      cdi:identifier:
        $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiCDIFProperties/ddi-cdif-data-types/schema.yaml#/$defs/Identifier
        description: Identifier for objects requiring short- or long-lasting referencing
          and management.
      cdi:isDefinedBy:
        anyOf:
        - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiCDIFProperties/ddi-cdif-represented-variable/schema.yaml
        - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiCDIFProperties/ddi-cdif-data-types/schema.yaml#/$defs/id-reference
      cdi:semantic:
        type: array
        items:
          $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiCDIFProperties/ddi-cdif-data-types/schema.yaml#/$defs/PairedControlledVocabularyEntry
        minItems: 1
        description: Qualifies the purpose or use expressed as a paired external controlled
          vocabulary.
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
          - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiCDIFProperties/ddi-cdif-data-types/schema.yaml#/$defs/id-reference
        minItems: 1
      cdi:identifier:
        $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiCDIFProperties/ddi-cdif-data-types/schema.yaml#/$defs/Identifier
        description: Identifier for objects requiring short- or long-lasting referencing
          and management.
      cdi:isDefinedBy:
        anyOf:
        - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiCDIFProperties/ddi-cdif-represented-variable/schema.yaml
        - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiCDIFProperties/ddi-cdif-data-types/schema.yaml#/$defs/id-reference
      cdi:semantic:
        type: array
        items:
          $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiCDIFProperties/ddi-cdif-data-types/schema.yaml#/$defs/PairedControlledVocabularyEntry
        minItems: 1
        description: Qualifies the purpose or use expressed as a paired external controlled
          vocabulary.
    required:
    - '@type'
  DimensionComponent:
    type: object
    description: 'Role given to a represented variable in the context of a dimensional
      data structure to identify the universes associated with data points. The variable
      acts as a field in the compound identifier (the key structure) to disambiguate
      the cells in the multi-dimensional "cube".  AG: references to the variables
      which are the components of a compound identifier, in which each variable is
      a single field - an axis - in a coordinate system addressing a location in a
      matrix. These variables are often categorical, but also commonly include time.
      Unlike other Components, they may be ordered using instances of cdi:ComponentPosition.'
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
      cdi:isDefinedBy:
        anyOf:
        - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiCDIFProperties/ddi-cdif-represented-variable/schema.yaml
        - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiCDIFProperties/ddi-cdif-data-types/schema.yaml#/$defs/id-reference
    required:
    - '@type'
    - cdi:isDefinedBy
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
        $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiCDIFProperties/ddi-cdif-data-types/schema.yaml#/$defs/Identifier
        description: Identifier for objects requiring short- or long-lasting referencing
          and management.
      cdi:isDefinedBy:
        anyOf:
        - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiCDIFProperties/ddi-cdif-represented-variable/schema.yaml
        - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiCDIFProperties/ddi-cdif-data-types/schema.yaml#/$defs/id-reference
      cdi:semantic:
        type: array
        items:
          $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiCDIFProperties/ddi-cdif-data-types/schema.yaml#/$defs/PairedControlledVocabularyEntry
        minItems: 1
        description: Qualifies the purpose or use expressed as a paired external controlled
          vocabulary.
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
        - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiCDIFProperties/ddi-cdif-presentational-variable/schema.yaml
        - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiCDIFProperties/ddi-cdif-data-types/schema.yaml#/$defs/id-reference
      cdi:refersTo:
        anyOf:
        - $ref: '#/$defs/VariableValueComponent'
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
        $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiCDIFProperties/ddi-cdif-data-types/schema.yaml#/$defs/Identifier
        description: Identifier for objects requiring short- or long-lasting referencing
          and management.
      cdi:isDefinedBy:
        anyOf:
        - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiCDIFProperties/ddi-cdif-represented-variable/schema.yaml
        - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiCDIFProperties/ddi-cdif-data-types/schema.yaml#/$defs/id-reference
      cdi:semantic:
        type: array
        items:
          $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiCDIFProperties/ddi-cdif-data-types/schema.yaml#/$defs/PairedControlledVocabularyEntry
        minItems: 1
        description: Qualifies the purpose or use expressed as a paired external controlled
          vocabulary.
    required:
    - '@type'
x-jsonld-prefixes:
  cdi: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/

```

Links to the schema:

* YAML version: [schema.yaml](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiCDIFProperties/ddi-cdif-data-structure-component/schema.json)
* JSON version: [schema.json](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiCDIFProperties/ddi-cdif-data-structure-component/schema.yaml)


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
[context.jsonld](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiCDIFProperties/ddi-cdif-data-structure-component/context.jsonld)

## Sources

* [DDI-CDI 1.0 Specification](https://ddialliance.org/Specification/DDI-CDI/1.0/)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/Cross-Domain-Interoperability-Framework/metadataBuildingBlocks](https://github.com/Cross-Domain-Interoperability-Framework/metadataBuildingBlocks)
* Path: `_sources/ddiCDIFProperties/ddi-cdif-data-structure-component`

