
# DDI-CDI Statistical Classification (Schema)

`cdif.bbr.metadata.ddiProperties.ddicdiStatisticalClassification` *v0.1*

Set of categories represented by classification items where the subset of immediate children categories for any given parent category are mutually exclusive and jointly exhaustive with respect to that parent.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

DDI-CDI StatisticalClassification models a set of categories represented by classification items in which the immediate children of any parent are mutually exclusive and jointly exhaustive. The root `cdi:StatisticalClassification` carries `cdi:isMaintainedBy` (referencing `ddicdiOrganization`), `cdi:isIndexedBy` (linking to one or more `ClassificationIndex` items), `cdi:isVariantOf` for variant relationships, and metadata properties such as `cdi:availableLanguage`, `cdi:changeFromBase`, `cdi:copyright`, `cdi:isCurrent`, and `cdi:isFloating`.

The hierarchy is expressed via `cdi:has_Level` and `cdi:has_ClassificationItem` (with `cdi:LevelStructure` and `Level` providing the nesting), and supporting types — `Code`, `Notation`, `Category`, `CategorySet`, `AuthorizationSource`, `ClassificationIndex`, and others — are defined locally in `$defs`. StatisticalClassification is the most fully-formed kind of `cdi:EnumerationDomain` available to `ddicdiValueDomain` for variables whose values come from an official classification scheme.

## Examples

### Minimal StatisticalClassification
TODO: replace with a JSON-LD example.
## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: DDI-CDI Statistical Classification
description: Set of categories represented by classification items where the subset
  of immediate children categories for any given parent category are mutually exclusive
  and jointly exhaustive with respect to that parent.
type: object
properties:
  '@type':
    type: array
    items:
      type: string
    contains:
      const: cdi:StatisticalClassification
    minItems: 1
  '@id':
    type: string
    description: Identifier for this StatisticalClassification node
  cdi:allowsDuplicates:
    type: boolean
    description: "If value is False, the members are unique within the collection
      - if True, there may be duplicates. (Note that a mathematical \u201Cbag\u201D
      permits duplicates and is unordered - a \u201Cset\u201D does not have duplicates
      and may be ordered.)"
    x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/allowsDuplicates
  cdi:availableLanguage:
    type: array
    items:
      type: string
    minItems: 1
    description: A list of languages in which the Statistical Classification is available.
      Supports the indication of multiple languages within a single property. Supports
      use of codes defined by the RFC 1766.
    x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/availableLanguage
  cdi:changeFromBase:
    $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/InternationalString
    description: 'Describes the relationship between the variant and its base Statistical
      Classification, including regroupings, aggregations added and extensions. (Source:
      GSIM StatisticalClassification/Changes from base Statistical Classification).'
    x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/changeFromBase
  cdi:copyright:
    type: array
    items:
      $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/InternationalString
    minItems: 1
    description: Copyright of the statistical classification.
    x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/copyright
  cdi:displayLabel:
    type: array
    items:
      $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/LabelForDisplay
    minItems: 1
    description: A human-readable display label for the object. Supports the use of
      multiple languages. Repeat for labels with different content, for example, labels
      with differing length limitations.
    x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/displayLabel
  cdi:isCurrent:
    type: boolean
    description: Indicates if the statistical classification is currently valid.
    x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/isCurrent
  cdi:isFloating:
    type: boolean
    description: 'Indicates if the Statistical Classification is a floating classification.
      In a floating statistical classification, a validity period should be defined
      for all classification Items which will allow the display of the item structure
      and content at different points of time. (Source: GSIM StatisticalClassification/Floating).'
    x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/isFloating
  cdi:isMaintainedBy:
    type: array
    items:
      anyOf:
      - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiOrganization/schema.yaml
      - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/id-reference
    minItems: 1
    x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/isMaintainedBy
  cdi:isIndexedBy:
    type: array
    items:
      anyOf:
      - $ref: '#/$defs/ClassificationIndex'
      - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/id-reference
    minItems: 1
    x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/isIndexedBy
  cdi:isVariantOf:
    anyOf:
    - $ref: '#/$defs/StatisticalClassification'
    - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/id-reference
    x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/isVariantOf
  cdi:isSuccessorOf:
    type: array
    items:
      anyOf:
      - $ref: '#/$defs/StatisticalClassification'
      - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/id-reference
    minItems: 1
    x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/isSuccessorOf
  cdi:isPredecessorOf:
    type: array
    items:
      anyOf:
      - $ref: '#/$defs/StatisticalClassification'
      - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/id-reference
    minItems: 1
    x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/isPredecessorOf
  cdi:has_ClassificationItemPosition:
    type: array
    items:
      anyOf:
      - $ref: '#/$defs/ClassificationItemPosition'
      - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/id-reference
    minItems: 1
    x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/has_ClassificationItemPosition
  cdi:has_ClassificationItem:
    type: array
    items:
      anyOf:
      - $ref: '#/$defs/ClassificationItem'
      - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/id-reference
    minItems: 1
    x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/has_ClassificationItem
  cdi:has_LevelStructure:
    anyOf:
    - $ref: '#/$defs/LevelStructure'
    - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/id-reference
    x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/has_LevelStructure
  cdi:purposeOfVariant:
    $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/InternationalString
    description: 'If the Statistical Classification is a variant, notes the specific
      purpose for which it was developed. (Source: GSIM StatisticalClassification/Purpose
      of variant).'
    x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/purposeOfVariant
  cdi:rationale:
    $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/InternationalString
    description: Explanation of the reason(s) some decision was made or some object
      exists.
    x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/rationale
  cdi:releaseDate:
    $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/CombinedDate
    description: Date when the current version of the Statistical Classification was
      released.
    x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/releaseDate
  cdi:updateChanges:
    type: array
    items:
      $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/InternationalString
    minItems: 1
    description: Summary description of changes which have occurred since the most
      recent classification version or classification update came into force.
    x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/updateChanges
  cdi:usage:
    $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/InternationalString
    description: Explanation of the ways in which the object is employed.
    x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/usage
  cdi:validDates:
    $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/DateRange
    description: 'The dates describing the validity period of the object. The date
      from which the object became valid must be defined if the map belongs to a "floating"
      construct. The date at which the object became invalid must be defined if the
      map belongs to a "floating" construct and is no longer valid. Per the Generic
      Statistical Information Model, Statistical Classification: "The date the statistical
      classification enters production use and the date on which the Statistical Classification
      was superseded by a successor version or otherwise ceased to be valid."'
    x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/validDates
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
    description: Human understandable name (liguistic signifier, word, phrase, or
      mnemonic). May follow ISO/IEC 11179-5 naming principles, and have context provided
      to specify usage.
    x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/name
  cdi:uses:
    anyOf:
    - $ref: '#/$defs/LevelStructure'
    - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/id-reference
    x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/uses
  cdi:references:
    anyOf:
    - $ref: '#/$defs/CategorySet'
    - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/id-reference
    x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/references
  cdi:isDefinedBy:
    type: array
    items:
      anyOf:
      - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/skosProperties/skosConcept/schema.yaml
      - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/id-reference
    minItems: 1
    x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/isDefinedBy
  cdi:purpose:
    $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/InternationalString
    description: Intent or reason for the object/the description of the object.
    x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/purpose
required:
- '@type'
$defs:
  StatisticalClassification:
    type: object
    description: Set of categories represented by classification items where the subset
      of immediate children categories for any given parent category are mutually
      exclusive and jointly exhaustive with respect to that parent.
    properties:
      '@type':
        type: array
        items:
          type: string
        contains:
          const: cdi:StatisticalClassification
        minItems: 1
      '@id':
        type: string
        description: Identifier for this StatisticalClassification node
      cdi:allowsDuplicates:
        type: boolean
        description: "If value is False, the members are unique within the collection
          - if True, there may be duplicates. (Note that a mathematical \u201Cbag\u201D
          permits duplicates and is unordered - a \u201Cset\u201D does not have duplicates
          and may be ordered.)"
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/allowsDuplicates
      cdi:availableLanguage:
        type: array
        items:
          type: string
        minItems: 1
        description: A list of languages in which the Statistical Classification is
          available. Supports the indication of multiple languages within a single
          property. Supports use of codes defined by the RFC 1766.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/availableLanguage
      cdi:changeFromBase:
        $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/InternationalString
        description: 'Describes the relationship between the variant and its base
          Statistical Classification, including regroupings, aggregations added and
          extensions. (Source: GSIM StatisticalClassification/Changes from base Statistical
          Classification).'
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/changeFromBase
      cdi:copyright:
        type: array
        items:
          $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/InternationalString
        minItems: 1
        description: Copyright of the statistical classification.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/copyright
      cdi:displayLabel:
        type: array
        items:
          $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/LabelForDisplay
        minItems: 1
        description: A human-readable display label for the object. Supports the use
          of multiple languages. Repeat for labels with different content, for example,
          labels with differing length limitations.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/displayLabel
      cdi:isCurrent:
        type: boolean
        description: Indicates if the statistical classification is currently valid.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/isCurrent
      cdi:isFloating:
        type: boolean
        description: 'Indicates if the Statistical Classification is a floating classification.
          In a floating statistical classification, a validity period should be defined
          for all classification Items which will allow the display of the item structure
          and content at different points of time. (Source: GSIM StatisticalClassification/Floating).'
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/isFloating
      cdi:isMaintainedBy:
        type: array
        items:
          anyOf:
          - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiOrganization/schema.yaml
          - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/id-reference
        minItems: 1
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/isMaintainedBy
      cdi:isIndexedBy:
        type: array
        items:
          anyOf:
          - $ref: '#/$defs/ClassificationIndex'
          - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/id-reference
        minItems: 1
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/isIndexedBy
      cdi:isVariantOf:
        anyOf:
        - $ref: '#/$defs/StatisticalClassification'
        - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/id-reference
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/isVariantOf
      cdi:isSuccessorOf:
        type: array
        items:
          anyOf:
          - $ref: '#/$defs/StatisticalClassification'
          - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/id-reference
        minItems: 1
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/isSuccessorOf
      cdi:isPredecessorOf:
        type: array
        items:
          anyOf:
          - $ref: '#/$defs/StatisticalClassification'
          - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/id-reference
        minItems: 1
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/isPredecessorOf
      cdi:has_ClassificationItemPosition:
        type: array
        items:
          anyOf:
          - $ref: '#/$defs/ClassificationItemPosition'
          - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/id-reference
        minItems: 1
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/has_ClassificationItemPosition
      cdi:has_ClassificationItem:
        type: array
        items:
          anyOf:
          - $ref: '#/$defs/ClassificationItem'
          - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/id-reference
        minItems: 1
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/has_ClassificationItem
      cdi:has_LevelStructure:
        anyOf:
        - $ref: '#/$defs/LevelStructure'
        - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/id-reference
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/has_LevelStructure
      cdi:purposeOfVariant:
        $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/InternationalString
        description: 'If the Statistical Classification is a variant, notes the specific
          purpose for which it was developed. (Source: GSIM StatisticalClassification/Purpose
          of variant).'
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/purposeOfVariant
      cdi:rationale:
        $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/InternationalString
        description: Explanation of the reason(s) some decision was made or some object
          exists.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/rationale
      cdi:releaseDate:
        $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/CombinedDate
        description: Date when the current version of the Statistical Classification
          was released.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/releaseDate
      cdi:updateChanges:
        type: array
        items:
          $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/InternationalString
        minItems: 1
        description: Summary description of changes which have occurred since the
          most recent classification version or classification update came into force.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/updateChanges
      cdi:usage:
        $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/InternationalString
        description: Explanation of the ways in which the object is employed.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/usage
      cdi:validDates:
        $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/DateRange
        description: 'The dates describing the validity period of the object. The
          date from which the object became valid must be defined if the map belongs
          to a "floating" construct. The date at which the object became invalid must
          be defined if the map belongs to a "floating" construct and is no longer
          valid. Per the Generic Statistical Information Model, Statistical Classification:
          "The date the statistical classification enters production use and the date
          on which the Statistical Classification was superseded by a successor version
          or otherwise ceased to be valid."'
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/validDates
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
      cdi:uses:
        anyOf:
        - $ref: '#/$defs/LevelStructure'
        - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/id-reference
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/uses
      cdi:references:
        anyOf:
        - $ref: '#/$defs/CategorySet'
        - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/id-reference
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/references
      cdi:isDefinedBy:
        type: array
        items:
          anyOf:
          - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/skosProperties/skosConcept/schema.yaml
          - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/id-reference
        minItems: 1
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/isDefinedBy
      cdi:purpose:
        $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/InternationalString
        description: Intent or reason for the object/the description of the object.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/purpose
    required:
    - '@type'
  AuthorizationSource:
    type: object
    description: Identifies the authorizing agency and allows for the full text of
      the authorization (law, regulation, or other form of authorization).
    properties:
      '@type':
        type: array
        items:
          type: string
        contains:
          const: cdi:AuthorizationSource
        minItems: 1
      '@id':
        type: string
        description: Identifier for this AuthorizationSource node
      cdi:authorizationDate:
        $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/CombinedDate
        description: Identifies the date of authorization.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/authorizationDate
      cdi:identifier:
        $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/Identifier
        description: Identifier for objects requiring short- or long-lasting referencing
          and management.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/identifier
      cdi:legalMandate:
        $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/InternationalString
        description: Provide a legal citation to a law authorizing the study/data
          collection. For example, a legal citation for a law authorizing a country's
          census.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/legalMandate
      cdi:has:
        type: array
        items:
          anyOf:
          - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiAgent/schema.yaml
          - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/id-reference
        minItems: 1
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/has
      cdi:purpose:
        $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/InternationalString
        description: Intent or reason for the object/the description of the object.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/purpose
      cdi:statementOfAuthorization:
        $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/InternationalString
        description: Text of the authorization (law, mandate, approved business case).
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/statementOfAuthorization
    required:
    - '@type'
  Category:
    type: object
    description: Concept whose role is to define and measure a characteristic.
    properties:
      '@type':
        type: array
        items:
          type: string
        contains:
          const: cdi:Category
        minItems: 1
      '@id':
        type: string
        description: Identifier for this Category node
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
  CategoryPosition:
    type: object
    description: Assigns a sequence number to a category within a list.
    properties:
      '@type':
        type: array
        items:
          type: string
        contains:
          const: cdi:CategoryPosition
        minItems: 1
      '@id':
        type: string
        description: Identifier for this CategoryPosition node
      cdi:identifier:
        $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/Identifier
        description: Identifier for objects requiring short- or long-lasting referencing
          and management.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/identifier
      cdi:indexes:
        anyOf:
        - $ref: '#/$defs/Category'
        - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/id-reference
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/indexes
      cdi:value:
        type: integer
        description: Index value of the member in an ordered array.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/value
    required:
    - '@type'
  CategorySet:
    type: object
    description: Concept system where the underlying concepts are categories.
    properties:
      '@type':
        type: array
        items:
          type: string
        contains:
          const: cdi:CategorySet
        minItems: 1
      '@id':
        type: string
        description: Identifier for this CategorySet node
      cdi:has_Category:
        type: array
        items:
          anyOf:
          - $ref: '#/$defs/Category'
          - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/id-reference
        minItems: 1
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/has_Category
      cdi:has_CategoryPosition:
        type: array
        items:
          anyOf:
          - $ref: '#/$defs/CategoryPosition'
          - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/id-reference
        minItems: 1
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/has_CategoryPosition
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
      cdi:purpose:
        $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/InternationalString
        description: Intent or reason for the object/the description of the object.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/purpose
    required:
    - '@type'
  ClassificationIndex:
    type: object
    description: Ordered list of classification index entries.
    properties:
      '@type':
        type: array
        items:
          type: string
        contains:
          const: cdi:ClassificationIndex
        minItems: 1
      '@id':
        type: string
        description: Identifier for this ClassificationIndex node
      cdi:allowsDuplicates:
        type: boolean
        description: "If value is False, the members are unique within the collection
          - if True, there may be duplicates. (Note that a mathematical \u201Cbag\u201D
          permits duplicates and is unordered - a \u201Cset\u201D does not have duplicates
          and may be ordered.)"
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/allowsDuplicates
      cdi:availableLanguage:
        type: array
        items:
          type: string
        minItems: 1
        description: A list of languages in which the Statistical Classification is
          available. If a Classification Index exists in several languages, the number
          of entries in each language may be different, as the number of terms describing
          any given phenomenon can change from one language to another. However, the
          same phenomena should be described in each language. Supports the indication
          of multiple languages within a single property. Supports use of codes defined
          by the RFC 1766.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/availableLanguage
      cdi:codingInstruction:
        type: array
        items:
          $ref: '#/$defs/CommandCode'
        minItems: 1
        description: Additional information which drives the coding process for all
          entries in a Classification Index.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/codingInstruction
      cdi:corrections:
        type: array
        items:
          $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/InternationalString
        minItems: 1
        description: Verbal summary description of corrections, which have occurred
          within the Classification Index. Corrections include changing the item code
          associated with a classification index entry.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/corrections
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
      cdi:isMaintainedBy:
        anyOf:
        - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiAgent/schema.yaml
        - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/id-reference
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/isMaintainedBy
      cdi:hasContact:
        type: array
        items:
          anyOf:
          - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiAgent/schema.yaml
          - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/id-reference
        minItems: 1
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/hasContact
      cdi:isDefinedBy:
        type: array
        items:
          anyOf:
          - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/skosProperties/skosConcept/schema.yaml
          - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/id-reference
        minItems: 1
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/isDefinedBy
      cdi:has_ClassificationIndexEntryPosition:
        type: array
        items:
          anyOf:
          - $ref: '#/$defs/ClassificationIndexEntryPosition'
          - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/id-reference
        minItems: 1
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/has_ClassificationIndexEntryPosition
      cdi:has_ClassificationIndexEntry:
        type: array
        items:
          anyOf:
          - $ref: '#/$defs/ClassificationIndexEntry'
          - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/id-reference
        minItems: 1
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/has_ClassificationIndexEntry
      cdi:purpose:
        $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/InternationalString
        description: Intent or reason for the object/the description of the object.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/purpose
      cdi:releaseDate:
        $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/CombinedDate
        description: Date when the current version of the classification index was
          released.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/releaseDate
    required:
    - '@type'
  ClassificationIndexEntry:
    type: object
    description: Word or a short phrase corresponding to a classification item in
      a statistical classification, together with the code of the corresponding classification
      item.
    properties:
      '@type':
        type: array
        items:
          type: string
        contains:
          const: cdi:ClassificationIndexEntry
        minItems: 1
      '@id':
        type: string
        description: Identifier for this ClassificationIndexEntry node
      cdi:codingInstruction:
        $ref: '#/$defs/CommandCode'
        description: Additional information which drives the coding process for the
          Index Entry. Required when coding is dependent upon one or many other factors.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/codingInstruction
      cdi:entry:
        $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/InternationalString
        description: Text describing the type of object/unit or object property.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/entry
      cdi:identifier:
        $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/Identifier
        description: Identifier for objects requiring short- or long-lasting referencing
          and management.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/identifier
      cdi:validDates:
        $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/DateRange
        description: The dates describing the validity period of the object. The date
          from which the object became valid must be defined if the map belongs to
          a "floating" construct. The date at which the object became invalid must
          be defined if the map belongs to a "floating" construct and is no longer
          valid.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/validDates
    required:
    - '@type'
  ClassificationIndexEntryPosition:
    type: object
    description: Member indicator for use with member type classification index entry.
    properties:
      '@type':
        type: array
        items:
          type: string
        contains:
          const: cdi:ClassificationIndexEntryPosition
        minItems: 1
      '@id':
        type: string
        description: Identifier for this ClassificationIndexEntryPosition node
      cdi:identifier:
        $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/Identifier
        description: Identifier for objects requiring short- or long-lasting referencing
          and management.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/identifier
      cdi:indexes:
        anyOf:
        - $ref: '#/$defs/ClassificationIndexEntry'
        - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/id-reference
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/indexes
      cdi:value:
        type: integer
        description: Index value of the member in an ordered array.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/value
    required:
    - '@type'
  ClassificationItem:
    type: object
    description: A space for a category within a statistical classification.
    properties:
      '@type':
        type: array
        items:
          type: string
        contains:
          const: cdi:ClassificationItem
        minItems: 1
      '@id':
        type: string
        description: Identifier for this ClassificationItem node
      cdi:changeFromPreviousVersion:
        $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/InternationalString
        description: Describes the changes, which the item has been subject to from
          the previous version to the actual statistical classification.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/changeFromPreviousVersion
      cdi:changeLog:
        $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/InternationalString
        description: Describes the changes, which the item has been subject to during
          the life time of the actual statistical classification.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/changeLog
      cdi:explanatoryNotes:
        type: array
        items:
          $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/InternationalString
        minItems: 1
        description: 'A classification item may be associated with explanatory notes,
          which further describe and clarify the contents of the category. Explanatory
          notes consist of: General note: Contains either additional information about
          the category, or a general description of the category, which is not structured
          according to the "includes", "includes also", "excludes" pattern. Includes:
          Specifies the contents of the category. Includes also: A list of borderline
          cases, which belong to the described category. Excludes: A list of borderline
          cases, which do not belong to the described category. Excluded cases may
          contain a reference to the classification items to which the excluded cases
          belong.'
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/explanatoryNotes
      cdi:futureNotes:
        type: array
        items:
          $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/InternationalString
        minItems: 1
        description: The future events describe an intended or implemented change
          (or a number of changes) related to an invalid item (e.g., these changes
          may have turned the now invalid item into one or several successor items).
          This allows for the possibility of following successors of the item in the
          future.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/futureNotes
      cdi:identifier:
        $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/Identifier
        description: Identifier for objects requiring short- or long-lasting referencing
          and management.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/identifier
      cdi:isGenerated:
        type: boolean
        description: Indicates whether or not the item has been generated to make
          the level to which it belongs complete.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/isGenerated
      cdi:isValid:
        type: boolean
        description: Indicates whether or not the item is currently valid. If updates
          are allowed in the Statistical Classification, an item may be restricted
          in its validity, i.e. it may become valid or invalid after the Statistical
          Classification has been released.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/isValid
      cdi:name:
        type: array
        items:
          $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/ObjectName
        minItems: 1
        description: Human understandable name (liguistic signifier, word, phrase,
          or mnemonic). May follow ISO/IEC 11179-5 naming principles, and have context
          provided to specify usage. A Classification Item has an official name as
          provided by the owner or maintenance unit. The name describes the content
          of the category. The name is unique within the Statistical Classification
          to which the item belongs, except for categories that are identical at more
          than one level in a hierarchical classification. Use the context attribute
          to differentiate official names or alternate names for the Classification
          Item.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/name
      cdi:excludes:
        type: array
        items:
          anyOf:
          - $ref: '#/$defs/ClassificationItem'
          - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/id-reference
        minItems: 1
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/excludes
      cdi:denotes:
        anyOf:
        - $ref: '#/$defs/Category'
        - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/id-reference
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/denotes
      cdi:uses:
        anyOf:
        - $ref: '#/$defs/Notation'
        - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/id-reference
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/uses
      cdi:hasRulingBy:
        type: array
        items:
          anyOf:
          - $ref: '#/$defs/AuthorizationSource'
          - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/id-reference
        minItems: 1
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/hasRulingBy
      cdi:validDates:
        $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/DateRange
        description: The dates describing the validity period of the object. The date
          from which the object became valid must be defined if the map belongs to
          a "floating" construct. The date at which the object became invalid must
          be defined if the map belongs to a "floating" construct and is no longer
          valid.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/validDates
    required:
    - '@type'
  ClassificationItemPosition:
    type: object
    description: Provides a classification item with an index conveying the order
      of the classification item within a sequence, expressed as an integer, progressing
      upward from 0 or 1.
    properties:
      '@type':
        type: array
        items:
          type: string
        contains:
          const: cdi:ClassificationItemPosition
        minItems: 1
      '@id':
        type: string
        description: Identifier for this ClassificationItemPosition node
      cdi:identifier:
        $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/Identifier
        description: Identifier for objects requiring short- or long-lasting referencing
          and management.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/identifier
      cdi:indexes:
        anyOf:
        - $ref: '#/$defs/ClassificationItem'
        - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/id-reference
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/indexes
      cdi:value:
        type: integer
        description: Index value of the member in an ordered array.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/value
    required:
    - '@type'
  Command:
    type: object
    description: 'Provides the following information on the command: The content of
      the command and the programming language used.'
    properties:
      '@type':
        type: array
        items:
          type: string
        contains:
          const: cdi:Command
        minItems: 1
      cdi:commandContent:
        $ref: '#/$defs/TypedString'
        description: Content of the command itself expressed in the language designated
          in programming language.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/commandContent
      cdi:programLanguage:
        $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/ControlledVocabularyEntry
        description: Designates the programming language used for the command. Supports
          the use of a controlled vocabulary.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/programLanguage
  CommandCode:
    type: object
    description: Contains information on the command used for processing data. Contains
      a description of the command which should clarify for the user the purpose and
      process of the command, an in-line provision of the command itself, and a reference
      to an external version of the command such as a coding script.
    properties:
      '@type':
        type: array
        items:
          type: string
        contains:
          const: cdi:CommandCode
        minItems: 1
      cdi:command:
        type: array
        items:
          $ref: '#/$defs/Command'
        minItems: 1
        description: This is an in-line provision of the command itself. It provides
          the programming language used as well as the command.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/command
      cdi:commandFile:
        type: array
        items:
          $ref: '#/$defs/CommandFile'
        minItems: 1
        description: Identifies and provides a link to an external copy of the command,
          for example, a SAS Command Code script. Designates the programming language
          of the command file as well as the URI for the file.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/commandFile
      cdi:description:
        $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/InternationalString
        description: A description of the purpose and use of the command code provided.
          Supports multiple languages.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/description
  CommandFile:
    type: object
    description: Identifies and provides a link to an external copy of the command,
      for example, a SAS Command Code script. Designates the programming language
      of the command file, a description of the location of the file , and a URN or
      URL for the command file.
    properties:
      '@type':
        type: array
        items:
          type: string
        contains:
          const: cdi:CommandFile
        minItems: 1
      cdi:location:
        $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/InternationalString
        description: A description of the location of the file. This may not be machine
          actionable. It supports a description expressed in multiple languages.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/location
      cdi:uri:
        type: string
        description: The URL or URN of the command file.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/uri
  Level:
    type: object
    description: Set of all classification items the same number of relationships
      from the root (or top) classification item.
    properties:
      '@type':
        type: array
        items:
          type: string
        contains:
          const: cdi:Level
        minItems: 1
      '@id':
        type: string
        description: Identifier for this Level node
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
      cdi:levelNumber:
        type: integer
        description: Provides an association between a level number and optional concept
          which defines it within an ordered array. Use is required.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/levelNumber
      cdi:isDefinedBy:
        anyOf:
        - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/skosProperties/skosConcept/schema.yaml
        - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/id-reference
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/isDefinedBy
      cdi:groups:
        type: array
        items:
          anyOf:
          - $ref: '#/$defs/ClassificationItem'
          - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/id-reference
        minItems: 1
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/groups
    required:
    - '@type'
  LevelStructure:
    type: object
    description: Nesting structure of a hierarchical collection.
    properties:
      '@type':
        type: array
        items:
          type: string
        contains:
          const: cdi:LevelStructure
        minItems: 1
      '@id':
        type: string
        description: Identifier for this LevelStructure node
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
      cdi:has:
        type: array
        items:
          anyOf:
          - $ref: '#/$defs/Level'
          - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/id-reference
        minItems: 1
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/has
      cdi:usage:
        $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/InternationalString
        description: Explanation of the ways in which the object is employed.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/usage
      cdi:validDateRange:
        $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/DateRange
        description: The period for which the level object is valid, expressed as
          a start and end date (supports both ISO-standard and non-ISO date formats).
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/validDateRange
    required:
    - '@type'
  Notation:
    type: object
    description: Representation of a category in the context of a code or a classification
      item, as opposed of the corresponding instance value which would appear when
      used in a dataset.
    properties:
      '@type':
        type: array
        items:
          type: string
        contains:
          const: cdi:Notation
        minItems: 1
      '@id':
        type: string
        description: Identifier for this Notation node
      cdi:content:
        $ref: '#/$defs/TypedString'
        description: The actual content of this value as a string.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/content
      cdi:identifier:
        $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/Identifier
        description: Identifier for objects requiring short- or long-lasting referencing
          and management.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/identifier
      cdi:represents:
        type: array
        items:
          anyOf:
          - $ref: '#/$defs/Category'
          - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/id-reference
        minItems: 1
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/represents
      cdi:whiteSpace:
        type: string
        enum:
        - Collapse
        - Preserve
        - Replace
        description: 'The usual setting "collapse" states that leading and trailing
          white space will be removed and multiple adjacent white spaces will be treated
          as a single white space. When setting to "replace" all occurrences of #x9
          (tab), #xA (line feed) and #xD (carriage return) are replaced with #x20
          (space) but leading and trailing spaces will be retained. If the existence
          of any of these white spaces is critical to the understanding of the content,
          change the value of this attribute to "preserve".'
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/whiteSpace
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
x-jsonld-prefixes:
  cdi: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/

```

Links to the schema:

* YAML version: [schema.yaml](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiStatisticalClassification/schema.json)
* JSON version: [schema.json](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiStatisticalClassification/schema.yaml)


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
[context.jsonld](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiStatisticalClassification/context.jsonld)

## Sources

* [DDI-CDI 1.0 Specification](https://ddialliance.org/Specification/DDI-CDI/1.0/)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/Cross-Domain-Interoperability-Framework/metadataBuildingBlocks](https://github.com/Cross-Domain-Interoperability-Framework/metadataBuildingBlocks)
* Path: `_sources/ddiProperties/ddicdiStatisticalClassification`

