
# DDI-CDI Presentational Variable (Schema)

`cdif.bbr.metadata.ddiProperties.ddicdiPresentationalVariable` *v0.1*

Variable that records values of multiple variables in the context of a data structure. Variable playing the role of a variable value component.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

DDI-CDI PresentationalVariable describes variables that play a presentational role in a data structure — variables that record values of multiple variables, or that identify which variable a value belongs to. Polymorphic root over `cdi:ReferenceVariable` (carries the values of multiple substantive variables, structured by a `ReferenceValueDomain`) and `cdi:DescriptorVariable` (provides codes that identify which variable each value represents).

Both variants carry `cdi:takesValuesFrom` (pointing at a local presentational value domain) plus the physical-level and conceptual-level properties mirrored from `ddicdiInstanceVariable`. As with InstanceVariable, the 2026-03 DDI-CDI model describes physical layout from the mapping side (`PhysicalMapping` → `formats`), so these variables no longer carry outward `has_PhysicalSegmentLayout` / `has_ValueMapping` links — see the `ddicdiPhysicalMapping` BB. They are referenced from `ddicdiDataStructureComponent` (`VariableDescriptorComponent.cdi:isDefinedBy`) and are the variable-level counterparts to the variable-value/variable-descriptor components used in long and key-value data structures.

## Examples

### Minimal ReferenceVariable
TODO: replace with a JSON-LD example.
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
        - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/id-reference
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/takesValuesFrom
      cdi:physicalDataType:
        $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/ControlledVocabularyEntry
        description: The data type of this variable. Supports the optional use of
          an external controlled vocabulary.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/physicalDataType
      cdi:platformType:
        $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/ControlledVocabularyEntry
        description: Describes the application or technical system context in which
          the variable has been realized. Typically a statistical processing package
          or other processing environment.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/platformType
      cdi:source:
        $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/Reference
        description: Reference capturing provenance information.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/source
      cdi:variableFunction:
        type: array
        items:
          $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/ControlledVocabularyEntry
        minItems: 1
        description: Immutable characteristic of the variable such as geographic designator,
          weight, temporal designation, etc.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/variableFunction
      cdi:describedUnitOfMeasure:
        $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/ControlledVocabularyEntry
        description: The unit in which the data values are measured (kg, pound, euro),
          expressed as a value from a controlled system of entries (i.e., QDT). Supports
          the provision of an identifier for the entry in the authoritative source
          (a URI, etc.), and the specific vocabulary.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/describedUnitOfMeasure
      cdi:hasIntendedDataType:
        $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/ControlledVocabularyEntry
        description: The data type intended to be used by this variable. Supports
          the optional use of an external controlled vocabulary.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/hasIntendedDataType
      cdi:takesSentinelValuesFrom:
        type: array
        items:
          anyOf:
          - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiValueDomain/schema.yaml
          - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/id-reference
        minItems: 1
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/takesSentinelValuesFrom
      cdi:takesSubstantiveValuesFrom:
        anyOf:
        - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiValueDomain/schema.yaml
        - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/id-reference
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/takesSubstantiveValuesFrom
      cdi:simpleUnitOfMeasure:
        type: string
        description: The unit in which the data values are measured (kg, pound, euro),
          expressed as a simple string, in cases where no additional information is
          available (in the legacy system) or needed (as in the case of broad agreement
          within the community of use [i.e., ISO country codes, currencies, etc. in
          SDMX])
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/simpleUnitOfMeasure
      cdi:descriptiveText:
        $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/InternationalString
        description: A short natural language account of the characteristics of the
          object.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/descriptiveText
      cdi:takesSentinelConceptsFrom:
        anyOf:
        - $ref: '#/$defs/SentinelConceptualDomain'
        - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/id-reference
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/takesSentinelConceptsFrom
      cdi:takesSubstantiveConceptsFrom:
        anyOf:
        - $ref: '#/$defs/SubstantiveConceptualDomain'
        - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/id-reference
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/takesSubstantiveConceptsFrom
      cdi:measures:
        anyOf:
        - $ref: '#/$defs/UnitType'
        - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/id-reference
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/measures
      cdi:unitOfMeasureKind:
        $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/ControlledVocabularyEntry
        description: Kind of unit of measure, so that it may be prone to translation
          to equivalent UOMs. Example values include "acceleration," "temperature,"
          "salinity", etc. This description exists at the conceptual level, indicating
          a limitation on the type of representations which may be used for the variable
          as it is made more concrete.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/unitOfMeasureKind
      cdi:definition:
        $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/InternationalString
        description: Natural language statement conveying the meaning of a concept,
          differentiating it from other concepts. Supports the use of multiple languages
          and structured text. 'externalDefinition' can't be used if 'definition'
          is used.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/definition
      cdi:displayLabel:
        type: array
        items:
          $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/LabelForDisplay
        minItems: 1
        description: A human-readable display label for the object. Supports the use
          of multiple languages. Repeat for labels with different content, for example,
          labels with differing length limitations.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/displayLabel
      cdi:externalDefinition:
        $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/Reference
        description: A reference to an external definition of a concept (that is,
          a concept which is described outside the content of the DDI-CDI metadata
          description). An example is a SKOS concept. The definition property is assumed
          to duplicate the external one referenced if externalDefinition is used.
          Other corresponding properties are assumed to be included unchanged if used.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/externalDefinition
      cdi:identifier:
        $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/Identifier
        description: Identifier for objects requiring short- or long-lasting referencing
          and management.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/identifier
      cdi:name:
        type: array
        items:
          $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/ObjectName
        minItems: 1
        description: Human understandable name (linguistic signifier, word, phrase,
          or mnemonic). May follow ISO/IEC 11179-5 naming principles, and have context
          provided to specify usage.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/name
      cdi:uses:
        type: array
        items:
          anyOf:
          - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/skosProperties/skosConcept/schema.yaml
          - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/id-reference
        minItems: 1
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/uses
    required:
    - '@type'
  DescriptorVariable:
    type: object
    description: Variable that provides codes for variable identification in the context
      of a data structure. Variable playing the role of a variable descriptor component.
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
        anyOf:
        - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiValueDomain/schema.yaml
        - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/id-reference
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/takesSubstantiveValuesFrom
      cdi:physicalDataType:
        $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/ControlledVocabularyEntry
        description: The data type of this variable. Supports the optional use of
          an external controlled vocabulary.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/physicalDataType
      cdi:platformType:
        $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/ControlledVocabularyEntry
        description: Describes the application or technical system context in which
          the variable has been realized. Typically a statistical processing package
          or other processing environment.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/platformType
      cdi:source:
        $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/Reference
        description: Reference capturing provenance information.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/source
      cdi:variableFunction:
        type: array
        items:
          $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/ControlledVocabularyEntry
        minItems: 1
        description: Immutable characteristic of the variable such as geographic designator,
          weight, temporal designation, etc.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/variableFunction
      cdi:describedUnitOfMeasure:
        $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/ControlledVocabularyEntry
        description: The unit in which the data values are measured (kg, pound, euro),
          expressed as a value from a controlled system of entries (i.e., QDT). Supports
          the provision of an identifier for the entry in the authoritative source
          (a URI, etc.), and the specific vocabulary.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/describedUnitOfMeasure
      cdi:hasIntendedDataType:
        $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/ControlledVocabularyEntry
        description: The data type intended to be used by this variable. Supports
          the optional use of an external controlled vocabulary.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/hasIntendedDataType
      cdi:takesSentinelValuesFrom:
        type: array
        items:
          anyOf:
          - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiValueDomain/schema.yaml
          - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/id-reference
        minItems: 1
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/takesSentinelValuesFrom
      cdi:simpleUnitOfMeasure:
        type: string
        description: The unit in which the data values are measured (kg, pound, euro),
          expressed as a simple string, in cases where no additional information is
          available (in the legacy system) or needed (as in the case of broad agreement
          within the community of use [i.e., ISO country codes, currencies, etc. in
          SDMX])
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/simpleUnitOfMeasure
      cdi:descriptiveText:
        $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/InternationalString
        description: A short natural language account of the characteristics of the
          object.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/descriptiveText
      cdi:takesSentinelConceptsFrom:
        anyOf:
        - $ref: '#/$defs/SentinelConceptualDomain'
        - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/id-reference
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/takesSentinelConceptsFrom
      cdi:takesSubstantiveConceptsFrom:
        anyOf:
        - $ref: '#/$defs/SubstantiveConceptualDomain'
        - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/id-reference
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/takesSubstantiveConceptsFrom
      cdi:measures:
        anyOf:
        - $ref: '#/$defs/UnitType'
        - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/id-reference
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/measures
      cdi:unitOfMeasureKind:
        $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/ControlledVocabularyEntry
        description: Kind of unit of measure, so that it may be prone to translation
          to equivalent UOMs. Example values include "acceleration," "temperature,"
          "salinity", etc. This description exists at the conceptual level, indicating
          a limitation on the type of representations which may be used for the variable
          as it is made more concrete.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/unitOfMeasureKind
      cdi:definition:
        $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/InternationalString
        description: Natural language statement conveying the meaning of a concept,
          differentiating it from other concepts. Supports the use of multiple languages
          and structured text. 'externalDefinition' can't be used if 'definition'
          is used.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/definition
      cdi:displayLabel:
        type: array
        items:
          $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/LabelForDisplay
        minItems: 1
        description: A human-readable display label for the object. Supports the use
          of multiple languages. Repeat for labels with different content, for example,
          labels with differing length limitations.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/displayLabel
      cdi:externalDefinition:
        $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/Reference
        description: A reference to an external definition of a concept (that is,
          a concept which is described outside the content of the DDI-CDI metadata
          description). An example is a SKOS concept. The definition property is assumed
          to duplicate the external one referenced if externalDefinition is used.
          Other corresponding properties are assumed to be included unchanged if used.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/externalDefinition
      cdi:identifier:
        $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/Identifier
        description: Identifier for objects requiring short- or long-lasting referencing
          and management.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/identifier
      cdi:name:
        type: array
        items:
          $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/ObjectName
        minItems: 1
        description: Human understandable name (linguistic signifier, word, phrase,
          or mnemonic). May follow ISO/IEC 11179-5 naming principles, and have context
          provided to specify usage.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/name
      cdi:uses:
        type: array
        items:
          anyOf:
          - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/skosProperties/skosConcept/schema.yaml
          - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/id-reference
        minItems: 1
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/uses
    required:
    - '@type'
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
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/allowsDuplicates
      cdi:externalDefinition:
        $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/Reference
        description: A reference to an external definition of a concept (that is,
          a concept which is described outside the content of the DDI-CDI metadata
          description). An example is a SKOS concept. The definition property is assumed
          to duplicate the external one referenced if externalDefinition is used.
          Other corresponding properties are assumed to be included unchanged if used.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/externalDefinition
      cdi:identifier:
        $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/Identifier
        description: Identifier for objects requiring short- or long-lasting referencing
          and management.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/identifier
      cdi:name:
        type: array
        items:
          $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/ObjectName
        minItems: 1
        description: Human understandable name (liguistic signifier, word, phrase,
          or mnemonic). May follow ISO/IEC 11179-5 naming principles, and have context
          provided to specify usage.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/name
      cdi:isDefinedBy:
        type: array
        items:
          anyOf:
          - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/skosProperties/skosConcept/schema.yaml
          - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/id-reference
        minItems: 1
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/isDefinedBy
      cdi:has:
        type: array
        items:
          anyOf:
          - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/skosProperties/skosConcept/schema.yaml
          - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/id-reference
        minItems: 1
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/has
      cdi:purpose:
        $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/InternationalString
        description: Intent or reason for the object/the description of the object.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/purpose
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
          $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/LabelForDisplay
        minItems: 1
        description: A human-readable display label for the object. Supports the use
          of multiple languages. Repeat for labels with different content, for example,
          labels with differing length limitations.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/displayLabel
      cdi:identifier:
        $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/Identifier
        description: Identifier for objects requiring short- or long-lasting referencing
          and management.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/identifier
      cdi:recommendedDataType:
        type: array
        items:
          $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/ControlledVocabularyEntry
        minItems: 1
        description: The data types that are recommended for use with this domain.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/recommendedDataType
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
          $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/LabelForDisplay
        minItems: 1
        description: A human-readable display label for the object. Supports the use
          of multiple languages. Repeat for labels with different content, for example,
          labels with differing length limitations.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/displayLabel
      cdi:identifier:
        $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/Identifier
        description: Identifier for objects requiring short- or long-lasting referencing
          and management.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/identifier
      cdi:isDescribedBy:
        anyOf:
        - $ref: '#/$defs/ValueAndConceptDescription'
        - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/id-reference
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/isDescribedBy
      cdi:takesConceptsFrom:
        anyOf:
        - $ref: '#/$defs/ConceptSystem'
        - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/id-reference
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/takesConceptsFrom
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
          $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/LabelForDisplay
        minItems: 1
        description: A human-readable display label for the object. Supports the use
          of multiple languages. Repeat for labels with different content, for example,
          labels with differing length limitations.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/displayLabel
      cdi:identifier:
        $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/Identifier
        description: Identifier for objects requiring short- or long-lasting referencing
          and management.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/identifier
      cdi:isDescribedBy:
        anyOf:
        - $ref: '#/$defs/ValueAndConceptDescription'
        - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/id-reference
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/isDescribedBy
      cdi:takesConceptsFrom:
        anyOf:
        - $ref: '#/$defs/ConceptSystem'
        - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/id-reference
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/takesConceptsFrom
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
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/content
      cdi:typeOfContent:
        $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/ControlledVocabularyEntry
        description: Optional use of a controlled vocabulary to specifically type
          the associated content.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/typeOfContent
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
        $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/InternationalString
        description: A short natural language account of the characteristics of the
          object.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/descriptiveText
      cdi:definition:
        $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/InternationalString
        description: Natural language statement conveying the meaning of a concept,
          differentiating it from other concepts. Supports the use of multiple languages
          and structured text. 'externalDefinition' can't be used if 'definition'
          is used.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/definition
      cdi:displayLabel:
        type: array
        items:
          $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/LabelForDisplay
        minItems: 1
        description: A human-readable display label for the object. Supports the use
          of multiple languages. Repeat for labels with different content, for example,
          labels with differing length limitations.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/displayLabel
      cdi:externalDefinition:
        $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/Reference
        description: A reference to an external definition of a concept (that is,
          a concept which is described outside the content of the DDI-CDI metadata
          description). An example is a SKOS concept. The definition property is assumed
          to duplicate the external one referenced if externalDefinition is used.
          Other corresponding properties are assumed to be included unchanged if used.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/externalDefinition
      cdi:identifier:
        $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/Identifier
        description: Identifier for objects requiring short- or long-lasting referencing
          and management.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/identifier
      cdi:name:
        type: array
        items:
          $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/ObjectName
        minItems: 1
        description: Human understandable name (linguistic signifier, word, phrase,
          or mnemonic). May follow ISO/IEC 11179-5 naming principles, and have context
          provided to specify usage.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/name
      cdi:uses:
        type: array
        items:
          anyOf:
          - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/skosProperties/skosConcept/schema.yaml
          - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/id-reference
        minItems: 1
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/uses
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
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/classificationLevel
      cdi:description:
        $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/InternationalString
        description: A formal description of the set of values in human-readable language.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/description
      cdi:formatPattern:
        $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/ControlledVocabularyEntry
        description: 'A pattern for a number as described in Unicode Locale Data Markup
          Language (LDML) (http://www.unicode.org/reports/tr35/tr35.html) Part 3:
          Numbers (http://www.unicode.org/reports/tr35/tr35-numbers.html#Number_Format_Patterns)
          and Part 4. Dates (http://www.unicode.org/reports/tr35/tr35-dates.html#Date_Format_Patterns)
          . Examples would be #,##0.### to describe the pattern for a decimal number,
          or yyyy.MM.dd G ''at'' HH:mm:ss zzz for a datetime pattern.'
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/formatPattern
      cdi:identifier:
        $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/Identifier
        description: Identifier for objects requiring short- or long-lasting referencing
          and management.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/identifier
      cdi:logicalExpression:
        $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/ControlledVocabularyEntry
        description: A logical expression where the values of "x" making the expression
          true are the members of the set of valid values. For example, "(all reals
          x such that x > 0)" describes the real numbers greater than 0.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/logicalExpression
      cdi:maximumValueExclusive:
        type: string
        description: 'A string denoting the maximum possible value (excluding this
          value). From the W3C Recommendation "Metadata Vocabulary for Tabular Data"
          (https://www.w3.org/TR/tabular-metadata/) 5.11.2: "maxExclusive: An atomic
          property that contains a single number or string that is the maximum valid
          value (exclusive). The value of this property becomes the maximum exclusive
          annotation for the described datatype. See Value Constraints in [tabular-data-model]
          for details."'
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/maximumValueExclusive
      cdi:maximumValueInclusive:
        type: string
        description: 'A string denoting the maximum possible value. From the W3C Recommendation
          "Metadata Vocabulary for Tabular Data" (https://www.w3.org/TR/tabular-metadata/)
          5.11.2: "maximum: An atomic property that contains a single number or string
          that is the maximum valid value (inclusive); equivalent to maxInclusive.
          The value of this property becomes the maximum annotation for the described
          datatype. See Value Constraints in [tabular-data-model] for details."'
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/maximumValueInclusive
      cdi:minimumValueExclusive:
        type: string
        description: 'A string denoting the minimum possible value (excluding this
          value). From the W3C Recommendation "Metadata Vocabulary for Tabular Data"
          (https://www.w3.org/TR/tabular-metadata/) 5.11.2: "minExclusive: An atomic
          property that contains a single number or string that is the minimum valid
          value (exclusive). The value of this property becomes the minimum exclusive
          annotation for the described datatype. See Value Constraints in [tabular-data-model]
          for details."'
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/minimumValueExclusive
      cdi:minimumValueInclusive:
        type: string
        description: 'A string denoting the minimum possible value. From the W3C Recommendation
          "Metadata Vocabulary for Tabular Data" (https://www.w3.org/TR/tabular-metadata/)
          5.11.2: "minimum: An atomic property that contains a single number or string
          that is the minimum valid value (inclusive); equivalent to minInclusive.
          The value of this property becomes the minimum annotation for the described
          datatype. See Value Constraints in [tabular-data-model] for details."'
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/minimumValueInclusive
      cdi:regularExpression:
        $ref: '#/$defs/TypedString'
        description: A regular expression where strings matching the expression belong
          to the set of valid values. Use typeOfContent to specify the syntax of the
          regularExpression found in content.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/regularExpression
    required:
    - '@type'
x-jsonld-prefixes:
  cdi: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/

```

Links to the schema:

* YAML version: [schema.yaml](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiPresentationalVariable/schema.json)
* JSON version: [schema.json](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiPresentationalVariable/schema.yaml)


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
[context.jsonld](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiPresentationalVariable/context.jsonld)

## Sources

* [DDI-CDI 1.0 Specification](https://ddialliance.org/Specification/DDI-CDI/1.0/)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/Cross-Domain-Interoperability-Framework/metadataBuildingBlocks](https://github.com/Cross-Domain-Interoperability-Framework/metadataBuildingBlocks)
* Path: `_sources/ddiProperties/ddicdiPresentationalVariable`

