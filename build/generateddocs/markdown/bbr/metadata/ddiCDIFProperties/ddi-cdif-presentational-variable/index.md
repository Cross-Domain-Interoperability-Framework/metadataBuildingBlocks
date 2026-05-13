
# DDI-CDI Presentational Variable (Schema)

`cdif.bbr.metadata.ddiCDIFProperties.ddi-cdif-presentational-variable` *v0.1*

Variable that records values of multiple variables in the context of a data structure. Variable playing the role of a variable value component.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

DDI-CDI PresentationalVariable describes variables that play a presentational role in a data structure — variables that record values of multiple variables, or that identify which variable a value belongs to. Polymorphic root over `cdi:ReferenceVariable` (carries the values of multiple substantive variables, structured by a `ReferenceValueDomain`) and `cdi:DescriptorVariable` (provides codes that identify which variable each value represents).

Both variants carry `cdi:takesValuesFrom` (pointing at a local presentational value domain), `cdi:has_PhysicalSegmentLayout`, and `cdi:has_ValueMapping`, mirroring the physical-realization properties of `ddicdiInstanceVariable`. They are referenced from `ddicdiDataStructureComponent` (`VariableDescriptorComponent.cdi:isDefinedBy`) and are the variable-level counterparts to the variable-value/variable-descriptor components used in long and key-value data structures.

## Examples

### Minimal ReferenceVariable
Bare ReferenceVariable — the BB root is anyOf of ReferenceVariable or
DescriptorVariable; only @type is required.
#### json
```json
{
  "@context": {
    "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
    "ex": "https://example.org/"
  },
  "@type": ["cdi:ReferenceVariable"],
  "@id": "ex:ref-var/measurement-value"
}

```

#### jsonld
```jsonld
{
  "@context": [
    {
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/"
    },
    "https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiCDIFProperties/ddi-cdif-presentational-variable/context.jsonld",
    {
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "ex": "https://example.org/"
    }
  ],
  "@type": [
    "cdi:ReferenceVariable"
  ],
  "@id": "ex:ref-var/measurement-value"
}
```

#### ttl
```ttl
@prefix cdi: <http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/> .

<https://example.org/ref-var/measurement-value> a cdi:ReferenceVariable .


```


### Complete ReferenceVariable
Long-data ReferenceVariable exercising every schema property:
cdi:descriptiveText, cdi:simpleUnitOfMeasure / cdi:describedUnitOfMeasure,
cdi:physicalDataType / cdi:hasIntendedDataType, cdi:platformType,
cdi:source, cdi:variableFunction, the four substantive/sentinel value/
concept domain references, cdi:takesValuesFrom (ReferenceValueDomain),
cdi:has_PhysicalSegmentLayout, and cdi:has_ValueMapping.
#### json
```json
{
  "@context": {
    "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
    "ex": "https://example.org/"
  },
  "@type": ["cdi:ReferenceVariable"],
  "@id": "ex:ref-var/measurement-value",
  "cdi:descriptiveText": {
    "@type": ["cdi:InternationalString"],
    "cdi:languageSpecificString": [
      {
        "@type": ["cdi:LanguageString"],
        "cdi:content": "Long-data-format reference variable holding the actual measured value.",
        "cdi:language": "en"
      }
    ]
  },
  "cdi:simpleUnitOfMeasure": "varies",
  "cdi:physicalDataType": {
    "@type": ["cdi:ControlledVocabularyEntry"],
    "cdi:entryValue": ["xsd:string"]
  },
  "cdi:hasIntendedDataType": {
    "@type": ["cdi:ControlledVocabularyEntry"],
    "cdi:entryValue": ["xsd:decimal"]
  },
  "cdi:platformType": {
    "@type": ["cdi:ControlledVocabularyEntry"],
    "cdi:entryValue": ["SAS"]
  },
  "cdi:describedUnitOfMeasure": {
    "@type": ["cdi:ControlledVocabularyEntry"],
    "cdi:entryValue": ["mixed"],
    "cdi:vocabulary": {
      "@type": ["cdi:Reference"],
      "cdi:uri": "https://qudt.org/vocab/unit"
    }
  },
  "cdi:source": {
    "@type": ["cdi:Reference"],
    "cdi:uri": "https://example.org/provenance/measurement-value"
  },
  "cdi:variableFunction": [
    {
      "@type": ["cdi:ControlledVocabularyEntry"],
      "cdi:entryValue": ["measurement"]
    }
  ],
  "cdi:takesSubstantiveValuesFrom": { "@id": "ex:value-domain/decimal" },
  "cdi:takesSentinelValuesFrom": [
    { "@id": "ex:value-domain/missing-codes" }
  ],
  "cdi:takesSubstantiveConceptsFrom": { "@id": "ex:concept-domain/measurement" },
  "cdi:takesSentinelConceptsFrom": { "@id": "ex:concept-domain/missing" },
  "cdi:takesValuesFrom": { "@id": "ex:ref-value-domain/decimal" },
  "cdi:has_PhysicalSegmentLayout": [
    { "@id": "ex:layout/observations.csv" }
  ],
  "cdi:has_ValueMapping": { "@id": "ex:value-mapping/measurement-value" }
}

```

#### jsonld
```jsonld
{
  "@context": [
    {
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/"
    },
    "https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiCDIFProperties/ddi-cdif-presentational-variable/context.jsonld",
    {
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "ex": "https://example.org/"
    }
  ],
  "@type": [
    "cdi:ReferenceVariable"
  ],
  "@id": "ex:ref-var/measurement-value",
  "cdi:descriptiveText": {
    "@type": [
      "cdi:InternationalString"
    ],
    "cdi:languageSpecificString": [
      {
        "@type": [
          "cdi:LanguageString"
        ],
        "cdi:content": "Long-data-format reference variable holding the actual measured value.",
        "cdi:language": "en"
      }
    ]
  },
  "cdi:simpleUnitOfMeasure": "varies",
  "cdi:physicalDataType": {
    "@type": [
      "cdi:ControlledVocabularyEntry"
    ],
    "cdi:entryValue": [
      "xsd:string"
    ]
  },
  "cdi:hasIntendedDataType": {
    "@type": [
      "cdi:ControlledVocabularyEntry"
    ],
    "cdi:entryValue": [
      "xsd:decimal"
    ]
  },
  "cdi:platformType": {
    "@type": [
      "cdi:ControlledVocabularyEntry"
    ],
    "cdi:entryValue": [
      "SAS"
    ]
  },
  "cdi:describedUnitOfMeasure": {
    "@type": [
      "cdi:ControlledVocabularyEntry"
    ],
    "cdi:entryValue": [
      "mixed"
    ],
    "cdi:vocabulary": {
      "@type": [
        "cdi:Reference"
      ],
      "cdi:uri": "https://qudt.org/vocab/unit"
    }
  },
  "cdi:source": {
    "@type": [
      "cdi:Reference"
    ],
    "cdi:uri": "https://example.org/provenance/measurement-value"
  },
  "cdi:variableFunction": [
    {
      "@type": [
        "cdi:ControlledVocabularyEntry"
      ],
      "cdi:entryValue": [
        "measurement"
      ]
    }
  ],
  "cdi:takesSubstantiveValuesFrom": {
    "@id": "ex:value-domain/decimal"
  },
  "cdi:takesSentinelValuesFrom": [
    {
      "@id": "ex:value-domain/missing-codes"
    }
  ],
  "cdi:takesSubstantiveConceptsFrom": {
    "@id": "ex:concept-domain/measurement"
  },
  "cdi:takesSentinelConceptsFrom": {
    "@id": "ex:concept-domain/missing"
  },
  "cdi:takesValuesFrom": {
    "@id": "ex:ref-value-domain/decimal"
  },
  "cdi:has_PhysicalSegmentLayout": [
    {
      "@id": "ex:layout/observations.csv"
    }
  ],
  "cdi:has_ValueMapping": {
    "@id": "ex:value-mapping/measurement-value"
  }
}
```

#### ttl
```ttl
@prefix cdi: <http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/> .

<https://example.org/ref-var/measurement-value> a cdi:ReferenceVariable ;
    cdi:describedUnitOfMeasure [ a cdi:ControlledVocabularyEntry ;
            cdi:entryValue "mixed" ;
            cdi:vocabulary [ a cdi:Reference ;
                    cdi:uri "https://qudt.org/vocab/unit" ] ] ;
    cdi:descriptiveText [ a cdi:InternationalString ;
            cdi:languageSpecificString [ a cdi:LanguageString ;
                    cdi:content "Long-data-format reference variable holding the actual measured value." ;
                    cdi:language "en" ] ] ;
    cdi:hasIntendedDataType [ a cdi:ControlledVocabularyEntry ;
            cdi:entryValue "xsd:decimal" ] ;
    cdi:has_PhysicalSegmentLayout <https://example.org/layout/observations.csv> ;
    cdi:has_ValueMapping <https://example.org/value-mapping/measurement-value> ;
    cdi:physicalDataType [ a cdi:ControlledVocabularyEntry ;
            cdi:entryValue "xsd:string" ] ;
    cdi:platformType [ a cdi:ControlledVocabularyEntry ;
            cdi:entryValue "SAS" ] ;
    cdi:simpleUnitOfMeasure "varies" ;
    cdi:source [ a cdi:Reference ;
            cdi:uri "https://example.org/provenance/measurement-value" ] ;
    cdi:takesSentinelConceptsFrom <https://example.org/concept-domain/missing> ;
    cdi:takesSentinelValuesFrom <https://example.org/value-domain/missing-codes> ;
    cdi:takesSubstantiveConceptsFrom <https://example.org/concept-domain/measurement> ;
    cdi:takesSubstantiveValuesFrom <https://example.org/value-domain/decimal> ;
    cdi:takesValuesFrom <https://example.org/ref-value-domain/decimal> ;
    cdi:variableFunction [ a cdi:ControlledVocabularyEntry ;
            cdi:entryValue "measurement" ] .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: DDI-CDI Presentational Variable
description: Variable that records values of multiple variables in the context of
  a data structure. Variable playing the role of a variable value component.
anyOf:
- $ref: '#/$defs/ReferenceVariable'
- $ref: '#/$defs/DescriptorVariable'
$defs:
  ReferenceVariable:
    type: object
    description: Variable that records values of multiple variables in the context
      of a data structure. Variable playing the role of a variable value component.
    properties:
      '@type':
        type: array
        items:
          type: string
        contains:
          const: cdi:ReferenceVariable
        minItems: 1
      '@id':
        type: string
        description: Identifier for this ReferenceVariable node
      cdi:takesValuesFrom:
        anyOf:
        - $ref: '#/$defs/ReferenceValueDomain'
        - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiCDIFProperties/ddi-cdif-data-types/schema.yaml#/$defs/id-reference
      cdi:has_PhysicalSegmentLayout:
        type: array
        items:
          anyOf:
          - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiCDIFProperties/ddi-cdif-physical-segment-layout/schema.yaml
          - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiCDIFProperties/ddi-cdif-data-types/schema.yaml#/$defs/id-reference
        minItems: 1
      cdi:has_ValueMapping:
        anyOf:
        - $ref: '#/$defs/ValueMapping'
        - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiCDIFProperties/ddi-cdif-data-types/schema.yaml#/$defs/id-reference
      cdi:physicalDataType:
        $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiCDIFProperties/ddi-cdif-data-types/schema.yaml#/$defs/ControlledVocabularyEntry
        description: The data type of this variable. Supports the optional use of
          an external controlled vocabulary.
      cdi:platformType:
        $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiCDIFProperties/ddi-cdif-data-types/schema.yaml#/$defs/ControlledVocabularyEntry
        description: Describes the application or technical system context in which
          the variable has been realized. Typically a statistical processing package
          or other processing environment.
      cdi:source:
        $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiCDIFProperties/ddi-cdif-data-types/schema.yaml#/$defs/Reference
        description: Reference capturing provenance information.
      cdi:variableFunction:
        type: array
        items:
          $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiCDIFProperties/ddi-cdif-data-types/schema.yaml#/$defs/ControlledVocabularyEntry
        minItems: 1
        description: Immutable characteristic of the variable such as geographic designator,
          weight, temporal designation, etc.
      cdi:describedUnitOfMeasure:
        $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiCDIFProperties/ddi-cdif-data-types/schema.yaml#/$defs/ControlledVocabularyEntry
        description: The unit in which the data values are measured (kg, pound, euro),
          expressed as a value from a controlled system of entries (i.e., QDT). Supports
          the provision of an identifier for the entry in the authoritative source
          (a URI, etc.), and the specific vocabulary.
      cdi:hasIntendedDataType:
        $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiCDIFProperties/ddi-cdif-data-types/schema.yaml#/$defs/ControlledVocabularyEntry
        description: The data type intended to be used by this variable. Supports
          the optional use of an external controlled vocabulary.
      cdi:takesSentinelValuesFrom:
        type: array
        items:
          anyOf:
          - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiCDIFProperties/ddi-cdif-value-domain/schema.yaml
          - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiCDIFProperties/ddi-cdif-data-types/schema.yaml#/$defs/id-reference
        minItems: 1
      cdi:takesSubstantiveValuesFrom:
        anyOf:
        - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiCDIFProperties/ddi-cdif-value-domain/schema.yaml
        - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiCDIFProperties/ddi-cdif-data-types/schema.yaml#/$defs/id-reference
      cdi:simpleUnitOfMeasure:
        type: string
        description: The unit in which the data values are measured (kg, pound, euro),
          expressed as a simple string, in cases where no additional information is
          available (in the legacy system) or needed (as in the case of broad agreement
          within the community of use [i.e., ISO country codes, currencies, etc. in
          SDMX])
      cdi:descriptiveText:
        $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiCDIFProperties/ddi-cdif-data-types/schema.yaml#/$defs/InternationalString
        description: A short natural language account of the characteristics of the
          object.
      cdi:takesSentinelConceptsFrom:
        anyOf:
        - $ref: '#/$defs/SentinelConceptualDomain'
        - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiCDIFProperties/ddi-cdif-data-types/schema.yaml#/$defs/id-reference
      cdi:takesSubstantiveConceptsFrom:
        anyOf:
        - $ref: '#/$defs/SubstantiveConceptualDomain'
        - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiCDIFProperties/ddi-cdif-data-types/schema.yaml#/$defs/id-reference
      cdi:measures:
        anyOf:
        - $ref: '#/$defs/UnitType'
        - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiCDIFProperties/ddi-cdif-data-types/schema.yaml#/$defs/id-reference
      cdi:unitOfMeasureKind:
        $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiCDIFProperties/ddi-cdif-data-types/schema.yaml#/$defs/ControlledVocabularyEntry
        description: Kind of unit of measure, so that it may be prone to translation
          to equivalent UOMs. Example values include "acceleration," "temperature,"
          "salinity", etc. This description exists at the conceptual level, indicating
          a limitation on the type of representations which may be used for the variable
          as it is made more concrete.
      cdi:definition:
        $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiCDIFProperties/ddi-cdif-data-types/schema.yaml#/$defs/InternationalString
        description: Natural language statement conveying the meaning of a concept,
          differentiating it from other concepts. Supports the use of multiple languages
          and structured text. 'externalDefinition' can't be used if 'definition'
          is used.
      cdi:displayLabel:
        type: array
        items:
          $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiCDIFProperties/ddi-cdif-data-types/schema.yaml#/$defs/LabelForDisplay
        minItems: 1
        description: A human-readable display label for the object. Supports the use
          of multiple languages. Repeat for labels with different content, for example,
          labels with differing length limitations.
      cdi:externalDefinition:
        $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiCDIFProperties/ddi-cdif-data-types/schema.yaml#/$defs/Reference
        description: A reference to an external definition of a concept (that is,
          a concept which is described outside the content of the DDI-CDI metadata
          description). An example is a SKOS concept. The definition property is assumed
          to duplicate the external one referenced if externalDefinition is used.
          Other corresponding properties are assumed to be included unchanged if used.
      cdi:identifier:
        $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiCDIFProperties/ddi-cdif-data-types/schema.yaml#/$defs/Identifier
        description: Identifier for objects requiring short- or long-lasting referencing
          and management.
      cdi:name:
        type: array
        items:
          $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiCDIFProperties/ddi-cdif-data-types/schema.yaml#/$defs/ObjectName
        minItems: 1
        description: Human understandable name (linguistic signifier, word, phrase,
          or mnemonic). May follow ISO/IEC 11179-5 naming principles, and have context
          provided to specify usage.
      cdi:uses:
        type: array
        items:
          anyOf:
          - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/skosProperties/skosConcept/schema.yaml
          - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiCDIFProperties/ddi-cdif-data-types/schema.yaml#/$defs/id-reference
        minItems: 1
    required:
    - '@type'
  DescriptorVariable:
    type: object
    description: Variable that provides codes for variable identification in the context
      of a data structure. Descriptor Variables hold values which reference the logical
      variables in the data set, indicating which one the associated value in the
      corresponding Reference Variable is a measure/value for. Descriptor Variables
      are presentational variables found only in Long Data Sets.
    properties:
      '@type':
        type: array
        items:
          type: string
        contains:
          const: cdi:DescriptorVariable
        minItems: 1
      '@id':
        type: string
        description: Identifier for this DescriptorVariable node
      cdi:takesSubstantiveValuesFrom:
        description: a link to an instance of cdi:DescriptorValueDomain, which in
          turn provides information about logical variables to which each enumerated
          value corresponds, using the cdi:Descriptor class.
        anyOf:
        - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiCDIFProperties/ddi-cdif-value-domain/schema.yaml#/$defs/DescriptorValueDomain
        - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiCDIFProperties/ddi-cdif-data-types/schema.yaml#/$defs/id-reference
      cdi:name:
        type: array
        items:
          $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiCDIFProperties/ddi-cdif-data-types/schema.yaml#/$defs/ObjectName
        minItems: 1
        description: Human understandable name (linguistic signifier, word, phrase,
          or mnemonic). May follow ISO/IEC 11179-5 naming principles, and have context
          provided to specify usage.
      cdi:uses:
        type: array
        items:
          anyOf:
          - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/skosProperties/skosConcept/schema.yaml
          - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiCDIFProperties/ddi-cdif-data-types/schema.yaml#/$defs/id-reference
        minItems: 1
    required:
    - '@type'
    - cdi:name
    - cdi:takesSubstantiveValuesFrom
  ConceptSystem:
    type: object
    description: Set of concepts structured by the relations among them [GSIM 1.1].
    properties:
      '@type':
        type: array
        items:
          type: string
        contains:
          const: cdi:ConceptSystem
        minItems: 1
      '@id':
        type: string
        description: Identifier for this ConceptSystem node
      cdi:allowsDuplicates:
        type: boolean
        description: "If value is False, the members are unique within the collection
          - if True, there may be duplicates. (Note that a mathematical \u201Cbag\u201D
          permits duplicates and is unordered - a \u201Cset\u201D does not have duplicates
          and may be ordered.)"
      cdi:externalDefinition:
        $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiCDIFProperties/ddi-cdif-data-types/schema.yaml#/$defs/Reference
        description: A reference to an external definition of a concept (that is,
          a concept which is described outside the content of the DDI-CDI metadata
          description). An example is a SKOS concept. The definition property is assumed
          to duplicate the external one referenced if externalDefinition is used.
          Other corresponding properties are assumed to be included unchanged if used.
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
      cdi:isDefinedBy:
        type: array
        items:
          anyOf:
          - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/skosProperties/skosConcept/schema.yaml
          - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiCDIFProperties/ddi-cdif-data-types/schema.yaml#/$defs/id-reference
        minItems: 1
      cdi:has:
        type: array
        items:
          anyOf:
          - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/skosProperties/skosConcept/schema.yaml
          - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiCDIFProperties/ddi-cdif-data-types/schema.yaml#/$defs/id-reference
        minItems: 1
      cdi:purpose:
        $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiCDIFProperties/ddi-cdif-data-types/schema.yaml#/$defs/InternationalString
        description: Intent or reason for the object/the description of the object.
    required:
    - '@type'
  DataPoint:
    type: object
    description: Container for an instance value.
    properties:
      '@type':
        type: array
        items:
          type: string
        contains:
          const: cdi:DataPoint
        minItems: 1
      '@id':
        type: string
        description: Identifier for this DataPoint node
      cdi:identifier:
        $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiCDIFProperties/ddi-cdif-data-types/schema.yaml#/$defs/Identifier
        description: Identifier for objects requiring short- or long-lasting referencing
          and management.
      cdi:correspondsTo:
        type: array
        items:
          anyOf:
          - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiCDIFProperties/ddi-cdif-data-structure-component/schema.yaml
          - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiCDIFProperties/ddi-cdif-data-types/schema.yaml#/$defs/id-reference
        minItems: 1
      cdi:isDescribedBy:
        anyOf:
        - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifProperties/cdifInstanceVariable/schema.yaml
        - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiCDIFProperties/ddi-cdif-data-types/schema.yaml#/$defs/id-reference
    required:
    - '@type'
  PhysicalSegmentLocation:
    type: object
    description: Location of a data point in a physical segment.
    properties:
      '@type':
        type: array
        items:
          type: string
        contains:
          const: cdi:PhysicalSegmentLocation
        minItems: 1
      '@id':
        type: string
        description: Identifier for this PhysicalSegmentLocation node
      cdi:identifier:
        $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiCDIFProperties/ddi-cdif-data-types/schema.yaml#/$defs/Identifier
        description: Identifier for objects requiring short- or long-lasting referencing
          and management.
    required:
    - '@type'
  ReferenceValueDomain:
    type: object
    description: Set of permissible values for a variable playing the role of a variable
      value component.
    properties:
      '@type':
        type: array
        items:
          type: string
        contains:
          const: cdi:ReferenceValueDomain
        minItems: 1
      '@id':
        type: string
        description: Identifier for this ReferenceValueDomain node
      cdi:displayLabel:
        type: array
        items:
          $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiCDIFProperties/ddi-cdif-data-types/schema.yaml#/$defs/LabelForDisplay
        minItems: 1
        description: A human-readable display label for the object. Supports the use
          of multiple languages. Repeat for labels with different content, for example,
          labels with differing length limitations.
      cdi:identifier:
        $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiCDIFProperties/ddi-cdif-data-types/schema.yaml#/$defs/Identifier
        description: Identifier for objects requiring short- or long-lasting referencing
          and management.
      cdi:recommendedDataType:
        type: array
        items:
          $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiCDIFProperties/ddi-cdif-data-types/schema.yaml#/$defs/ControlledVocabularyEntry
        minItems: 1
        description: The data types that are recommended for use with this domain.
    required:
    - '@type'
  SentinelConceptualDomain:
    type: object
    description: Conceptual domain of sentinel concepts.
    properties:
      '@type':
        type: array
        items:
          type: string
        contains:
          const: cdi:SentinelConceptualDomain
        minItems: 1
      '@id':
        type: string
        description: Identifier for this SentinelConceptualDomain node
      cdi:displayLabel:
        type: array
        items:
          $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiCDIFProperties/ddi-cdif-data-types/schema.yaml#/$defs/LabelForDisplay
        minItems: 1
        description: A human-readable display label for the object. Supports the use
          of multiple languages. Repeat for labels with different content, for example,
          labels with differing length limitations.
      cdi:identifier:
        $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiCDIFProperties/ddi-cdif-data-types/schema.yaml#/$defs/Identifier
        description: Identifier for objects requiring short- or long-lasting referencing
          and management.
      cdi:isDescribedBy:
        anyOf:
        - $ref: '#/$defs/ValueAndConceptDescription'
        - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiCDIFProperties/ddi-cdif-data-types/schema.yaml#/$defs/id-reference
      cdi:takesConceptsFrom:
        anyOf:
        - $ref: '#/$defs/ConceptSystem'
        - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiCDIFProperties/ddi-cdif-data-types/schema.yaml#/$defs/id-reference
    required:
    - '@type'
  SubstantiveConceptualDomain:
    type: object
    description: Conceptual domain of substantive concepts.
    properties:
      '@type':
        type: array
        items:
          type: string
        contains:
          const: cdi:SubstantiveConceptualDomain
        minItems: 1
      '@id':
        type: string
        description: Identifier for this SubstantiveConceptualDomain node
      cdi:displayLabel:
        type: array
        items:
          $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiCDIFProperties/ddi-cdif-data-types/schema.yaml#/$defs/LabelForDisplay
        minItems: 1
        description: A human-readable display label for the object. Supports the use
          of multiple languages. Repeat for labels with different content, for example,
          labels with differing length limitations.
      cdi:identifier:
        $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiCDIFProperties/ddi-cdif-data-types/schema.yaml#/$defs/Identifier
        description: Identifier for objects requiring short- or long-lasting referencing
          and management.
      cdi:isDescribedBy:
        anyOf:
        - $ref: '#/$defs/ValueAndConceptDescription'
        - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiCDIFProperties/ddi-cdif-data-types/schema.yaml#/$defs/id-reference
      cdi:takesConceptsFrom:
        anyOf:
        - $ref: '#/$defs/ConceptSystem'
        - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiCDIFProperties/ddi-cdif-data-types/schema.yaml#/$defs/id-reference
    required:
    - '@type'
  TypedString:
    type: object
    description: TypedString combines a type with content defined as a simple string.
      May be used wherever a simple string needs to support a type definition to clarify
      its content.
    properties:
      '@type':
        type: array
        items:
          type: string
        contains:
          const: cdi:TypedString
        minItems: 1
      cdi:content:
        type: string
        description: Content of the property expressed as a simple string.
      cdi:typeOfContent:
        $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiCDIFProperties/ddi-cdif-data-types/schema.yaml#/$defs/ControlledVocabularyEntry
        description: Optional use of a controlled vocabulary to specifically type
          the associated content.
  UnitType:
    type: object
    description: Unit type is a type or class of objects of interest (units).
    properties:
      '@type':
        type: array
        items:
          type: string
        contains:
          const: cdi:UnitType
        minItems: 1
      '@id':
        type: string
        description: Identifier for this UnitType node
      cdi:descriptiveText:
        $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiCDIFProperties/ddi-cdif-data-types/schema.yaml#/$defs/InternationalString
        description: A short natural language account of the characteristics of the
          object.
      cdi:definition:
        $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiCDIFProperties/ddi-cdif-data-types/schema.yaml#/$defs/InternationalString
        description: Natural language statement conveying the meaning of a concept,
          differentiating it from other concepts. Supports the use of multiple languages
          and structured text. 'externalDefinition' can't be used if 'definition'
          is used.
      cdi:displayLabel:
        type: array
        items:
          $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiCDIFProperties/ddi-cdif-data-types/schema.yaml#/$defs/LabelForDisplay
        minItems: 1
        description: A human-readable display label for the object. Supports the use
          of multiple languages. Repeat for labels with different content, for example,
          labels with differing length limitations.
      cdi:externalDefinition:
        $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiCDIFProperties/ddi-cdif-data-types/schema.yaml#/$defs/Reference
        description: A reference to an external definition of a concept (that is,
          a concept which is described outside the content of the DDI-CDI metadata
          description). An example is a SKOS concept. The definition property is assumed
          to duplicate the external one referenced if externalDefinition is used.
          Other corresponding properties are assumed to be included unchanged if used.
      cdi:identifier:
        $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiCDIFProperties/ddi-cdif-data-types/schema.yaml#/$defs/Identifier
        description: Identifier for objects requiring short- or long-lasting referencing
          and management.
      cdi:name:
        type: array
        items:
          $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiCDIFProperties/ddi-cdif-data-types/schema.yaml#/$defs/ObjectName
        minItems: 1
        description: Human understandable name (linguistic signifier, word, phrase,
          or mnemonic). May follow ISO/IEC 11179-5 naming principles, and have context
          provided to specify usage.
      cdi:uses:
        type: array
        items:
          anyOf:
          - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/skosProperties/skosConcept/schema.yaml
          - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiCDIFProperties/ddi-cdif-data-types/schema.yaml#/$defs/id-reference
        minItems: 1
    required:
    - '@type'
  ValueAndConceptDescription:
    type: object
    description: Formal description of a set of values.
    properties:
      '@type':
        type: array
        items:
          type: string
        contains:
          const: cdi:ValueAndConceptDescription
        minItems: 1
      '@id':
        type: string
        description: Identifier for this ValueAndConceptDescription node
      cdi:classificationLevel:
        type: string
        enum:
        - Continuous
        - Interval
        - Nominal
        - Ordinal
        - Ratio
        description: Indicates the type of relationship, nominal, ordinal, interval,
          ratio, or continuous. Use where appropriate for the representation type.
      cdi:description:
        $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiCDIFProperties/ddi-cdif-data-types/schema.yaml#/$defs/InternationalString
        description: A formal description of the set of values in human-readable language.
      cdi:formatPattern:
        $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiCDIFProperties/ddi-cdif-data-types/schema.yaml#/$defs/ControlledVocabularyEntry
        description: 'A pattern for a number as described in Unicode Locale Data Markup
          Language (LDML) (http://www.unicode.org/reports/tr35/tr35.html) Part 3:
          Numbers (http://www.unicode.org/reports/tr35/tr35-numbers.html#Number_Format_Patterns)
          and Part 4. Dates (http://www.unicode.org/reports/tr35/tr35-dates.html#Date_Format_Patterns)
          . Examples would be #,##0.### to describe the pattern for a decimal number,
          or yyyy.MM.dd G ''at'' HH:mm:ss zzz for a datetime pattern.'
      cdi:identifier:
        $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiCDIFProperties/ddi-cdif-data-types/schema.yaml#/$defs/Identifier
        description: Identifier for objects requiring short- or long-lasting referencing
          and management.
      cdi:logicalExpression:
        $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiCDIFProperties/ddi-cdif-data-types/schema.yaml#/$defs/ControlledVocabularyEntry
        description: A logical expression where the values of "x" making the expression
          true are the members of the set of valid values. For example, "(all reals
          x such that x > 0)" describes the real numbers greater than 0.
      cdi:maximumValueExclusive:
        type: string
        description: 'A string denoting the maximum possible value (excluding this
          value). From the W3C Recommendation "Metadata Vocabulary for Tabular Data"
          (https://www.w3.org/TR/tabular-metadata/) 5.11.2: "maxExclusive: An atomic
          property that contains a single number or string that is the maximum valid
          value (exclusive). The value of this property becomes the maximum exclusive
          annotation for the described datatype. See Value Constraints in [tabular-data-model]
          for details."'
      cdi:maximumValueInclusive:
        type: string
        description: 'A string denoting the maximum possible value. From the W3C Recommendation
          "Metadata Vocabulary for Tabular Data" (https://www.w3.org/TR/tabular-metadata/)
          5.11.2: "maximum: An atomic property that contains a single number or string
          that is the maximum valid value (inclusive); equivalent to maxInclusive.
          The value of this property becomes the maximum annotation for the described
          datatype. See Value Constraints in [tabular-data-model] for details."'
      cdi:minimumValueExclusive:
        type: string
        description: 'A string denoting the minimum possible value (excluding this
          value). From the W3C Recommendation "Metadata Vocabulary for Tabular Data"
          (https://www.w3.org/TR/tabular-metadata/) 5.11.2: "minExclusive: An atomic
          property that contains a single number or string that is the minimum valid
          value (exclusive). The value of this property becomes the minimum exclusive
          annotation for the described datatype. See Value Constraints in [tabular-data-model]
          for details."'
      cdi:minimumValueInclusive:
        type: string
        description: 'A string denoting the minimum possible value. From the W3C Recommendation
          "Metadata Vocabulary for Tabular Data" (https://www.w3.org/TR/tabular-metadata/)
          5.11.2: "minimum: An atomic property that contains a single number or string
          that is the minimum valid value (inclusive); equivalent to minInclusive.
          The value of this property becomes the minimum annotation for the described
          datatype. See Value Constraints in [tabular-data-model] for details."'
      cdi:regularExpression:
        $ref: '#/$defs/TypedString'
        description: A regular expression where strings matching the expression belong
          to the set of valid values. Use typeOfContent to specify the syntax of the
          regularExpression found in content.
    required:
    - '@type'
  ValueMapping:
    type: object
    description: Physical characteristics for the value of an instance variable stored
      in a data point as part of a physical segment layout.
    properties:
      '@type':
        type: array
        items:
          type: string
        contains:
          const: cdi:ValueMapping
        minItems: 1
      '@id':
        type: string
        description: Identifier for this ValueMapping node
      cdi:decimalPositions:
        type: integer
        description: The number of decimal positions expressed as an integer. Used
          when the decimal position is implied (no decimal separator is present) See
          DDI 3.2 ManagedNumericRepresentation_decimalPositions
      cdi:defaultDecimalSeparator:
        type: string
        description: 'Default value is "." (period). The character separating the
          integer part from the fractional part of a decimal or real number. From
          the W3C Recommendation "Metadata Vocabulary for Tabular Data" (https://www.w3.org/TR/tabular-metadata/)
          6.4.2: "decimalChar: A string whose value is used to represent a decimal
          point within the number. If the supplied value is not a string, implementations
          MUST issue a warning and proceed as if the property had not been specified."'
      cdi:defaultDigitGroupSeparator:
        type: string
        description: 'Default value is null. A character separating groups of digits
          (for readability). In W3C part of the datatype format From https://www.w3.org/TR/tabular-metadata/
          tabular 6.4.2 groupChar: "A string whose value is used to group digits within
          the number. If the supplied value is not a string, implementations MUST
          issue a warning and proceed as if the property had not been specified."'
      cdi:defaultValue:
        type: string
        description: A default string indicating the value to substitute for an empty
          string. From https://www.w3.org/TR/tabular-metadata/ Inherited 5.7 "default
          - An atomic property holding a single string that is used to create a default
          value for the cell in cases where the original string value is an empty
          string. See Parsing Cells in [tabular-data-model] for more details. If not
          specified, the default for the default property is the empty string, "".
          The value of this property becomes the default annotation for the described
          column."
      cdi:format:
        $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiCDIFProperties/ddi-cdif-data-types/schema.yaml#/$defs/ControlledVocabularyEntry
        description: 'This defines the format of the physical representation of the
          value. From https://www.w3.org/TR/tabular-metadata/ 5.11.2 format: "An atomic
          property that contains either a single string or an object that defines
          the format of a value of this type, used when parsing a string value as
          described in Parsing Cells in [tabular-data-model]. The value of this property
          becomes the format annotation for the described datatype." See https://www.w3.org/TR/tabular-metadata/
          Tabular 6.4.2 "Formats for numeric datatypes" this may include decimalChar,
          groupChar, pattern "By default, numeric values must be in the formats defined
          in [xmlschema11-2]. It is not uncommon for numbers within tabular data to
          be formatted for human consumption, which may involve using commas for decimal
          points, grouping digits in the number using commas, or adding percent signs
          to the number." See https://www.w3.org/TR/tabular-metadata/ Tabular 6.4.
          Formats for Booleans " Boolean values may be represented in many ways aside
          from the standard 1 and 0 or true and false." See https://www.w3.org/TR/tabular-metadata/
          6.4.4. Formats for dates and times "By default, dates and times are assumed
          to be in the format defined in [xmlschema11-2]. However dates and times
          are commonly represented in tabular data in other formats." See https://www.w3.org/TR/tabular-metadata/
          6.4.5 Formats for durations "Durations MUST be formatted and interpreted
          as defined in [xmlschema11-2], using the [ISO8601] format -?PnYnMnDTnHnMnS.
          For example, the duration P1Y1D is used for a year and a day; the duration
          PT2H30M for 2 hours and 30 minutes." See https://www.w3.org/TR/tabular-metadata/
          6.4.6 Formats for other types "If the datatype base is not numeric, boolean,
          a date/time type, or a duration type, the datatype format annotation provides
          a regular expression for the string values, with syntax and processing defined
          by [ECMASCRIPT]. If the supplied value is not a valid regular expression,
          implementations MUST issue a warning and proceed as if no format had been
          provided." From DDI3.2 ManagedNumericRepresentation@format "A format for
          number expressed as a string." From DDI3.2 ManagedDateTimeRepresentation_DateFieldFormat
          "Describes the format of the date field, in formats such as YYYY/MM or MM-DD-YY,
          etc. If this element is omitted, then the format is assumed to be the XML
          Schema format corresponding to the type attribute value."'
      cdi:identifier:
        $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiCDIFProperties/ddi-cdif-data-types/schema.yaml#/$defs/Identifier
        description: Identifier for objects requiring short- or long-lasting referencing
          and management.
      cdi:isRequired:
        type: boolean
        description: 'If the value of this property is True indicates that a value
          is required for the referenced instance variable. From the W3C Recommendation
          "Metadata Vocabulary for Tabular Data" (https://www.w3.org/TR/tabular-metadata/)
          5.7 Inherited Properties: "required: A boolean atomic property taking a
          single value which indicates whether the cell value can be null. See Parsing
          Cells in [tabular-data-model] for more details. The default is false, which
          means cells can have null values. The value of this property becomes the
          required annotation for the described column."'
      cdi:length:
        type: integer
        description: 'The length in characters of the physical representation of the
          value. From the W3C Recommendation "Metadata Vocabulary for Tabular Data"
          (https://www.w3.org/TR/tabular-metadata/) 5.11.2 "length: A numeric atomic
          property that contains a single integer that is the exact length of the
          value. The value of this property becomes the length annotation for the
          described datatype. See Length Constraints in [tabular-data-model] for details."
          Corresponds to DDI2.5 var/location/width and DDI 3.2 PhysicalLocation/Width.'
      cdi:maximumLength:
        type: integer
        description: 'The largest possible value of the length of the physical representation
          of the value. From the W3C Recommendation "Metadata Vocabulary for Tabular
          Data" (https://www.w3.org/TR/tabular-metadata/) 5.11.2: "maxLength: A numeric
          atomic property that contains a single integer that is the maximum length
          of the value. The value of this property becomes the maximum length annotation
          for the described datatype. See Length Constraints in [tabular-data-model]
          for details."'
      cdi:minimumLength:
        type: integer
        description: 'The smallest possible value for the length of the physical representation
          of the value. From the W3C Recommendation "Metadata Vocabulary for Tabular
          Data" (https://www.w3.org/TR/tabular-metadata/) 5.11.2: "minLength: An atomic
          property that contains a single integer that is the minimum length of the
          value. The value of this property becomes the minimum length annotation
          for the described datatype. See Length Constraints in [tabular-data-model]
          for details."'
      cdi:nullSequence:
        type: string
        description: 'A string indicating a null value. From the W3C Recommendation
          "Metadata Vocabulary for Tabular Data" (https://www.w3.org/TR/tabular-metadata/)
          4.3: "null: the string or strings which cause the value of cells having
          string value matching any of these values to be null." From the same source,
          Inherited 5.7: "null: An atomic property giving the string or strings used
          for null values within the data. If the string value of the cell is equal
          to any one of these values, the cell value is null. See Parsing Cells in
          [tabular-data-model] for more details. If not specified, the default for
          the null property is the empty string ''''. The value of this property becomes
          the null annotation for the described column."'
      cdi:numberPattern:
        type: string
        description: "A pattern description of the format of a numeric value. In W3C
          part of the datatype format From https://www.w3.org/TR/tabular-metadata/
          tabular 6.4.2 pattern: \"A number format pattern as defined in [UAX35] http://www.unicode.org/reports/tr35/tr35-31/tr35-numbers.html#Number_Format_Patterns.
          Implementations MUST recognise number format patterns containing the symbols
          0, #, the specified decimalChar (or \".\" if unspecified), the specified
          groupChar (or \",\" if unspecified), E, +, % and \u2030. Implementations
          MAY additionally recognise number format patterns containing other special
          pattern characters defined in [UAX35]. If the supplied value is not a string,
          or if it contains an invalid number format pattern or uses special pattern
          characters that the implementation does not recognise, implementations MUST
          issue a warning and proceed as if the property had not been specified. If
          the datatype format annotation is a single string, this is interpreted in
          the same way as if it were an object with a pattern property whose value
          is that string. If the groupChar is specified, but no pattern is supplied,
          when parsing the string value of a cell against this format specification,
          implementations MUST recognise and parse numbers that consist of: an optional
          + or - sign, \u2026 Implementations MAY also recognise numeric values that
          are in any of the standard-decimal, standard-percent or standard-scientific
          formats listed in the Unicode Common Locale Data Repository. \u2026\""
      cdi:formats:
        type: array
        items:
          anyOf:
          - $ref: '#/$defs/DataPoint'
          - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiCDIFProperties/ddi-cdif-data-types/schema.yaml#/$defs/id-reference
        minItems: 1
      cdi:uses:
        anyOf:
        - $ref: '#/$defs/PhysicalSegmentLocation'
        - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiCDIFProperties/ddi-cdif-data-types/schema.yaml#/$defs/id-reference
      cdi:physicalDataType:
        $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiCDIFProperties/ddi-cdif-data-types/schema.yaml#/$defs/ControlledVocabularyEntry
        description: 'The base datatype of the physical representation. An integer
          InstanceVariable might, for example, be stored as a floating point number.
          From the W3C Recommendation "Metadata Vocabulary for Tabular Data" (https://www.w3.org/TR/tabular-metadata/)
          Inherited 5.7: "datatype: An atomic property that contains either a single
          string that is the main datatype of the values of the cell or a datatype
          description object. If the value of this property is a string, it MUST be
          the name of one of the built-in datatypes defined in section 5.11.1 Built-in
          Datatypes and this value is normalized to an object whose base property
          is the original string value. If it is an object then it describes a more
          specialized datatype. If a cell contains a sequence (i.e. the separator
          property is specified and not null) then this property specifies the datatype
          of each value within that sequence. See 5.11 Datatypes and Parsing Cells
          in [tabular-data-model] for more details. The normalized value of this property
          becomes the datatype annotation for the described column."'
      cdi:scale:
        type: integer
        description: The scale of the number expressed as an integer. A multiplier
          to be used in combination with the value to determine the measurement. (E.g.,
          a number expressed in 100's with a value of 5 and a scale of 100 would be
          500).
    required:
    - '@type'
x-jsonld-prefixes:
  cdi: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/

```

Links to the schema:

* YAML version: [schema.yaml](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiCDIFProperties/ddi-cdif-presentational-variable/schema.json)
* JSON version: [schema.json](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiCDIFProperties/ddi-cdif-presentational-variable/schema.yaml)


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
[context.jsonld](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiCDIFProperties/ddi-cdif-presentational-variable/context.jsonld)

## Sources

* [DDI-CDI 1.0 Specification](https://ddialliance.org/Specification/DDI-CDI/1.0/)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/Cross-Domain-Interoperability-Framework/metadataBuildingBlocks](https://github.com/Cross-Domain-Interoperability-Framework/metadataBuildingBlocks)
* Path: `_sources/ddiCDIFProperties/ddi-cdif-presentational-variable`

