
# DDI-CDI Statistical Classification (Schema)

`cdif.bbr.metadata.ddiProperties.ddicdiStatisticalClassification` *v0.1*

Set of categories represented by classification items where the subset of immediate children categories for any given parent category are mutually exclusive and jointly exhaustive with respect to that parent.

[*Status*](http://www.opengis.net/def/status): Under development

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
  cdi:availableLanguage:
    type: array
    items:
      type: string
    minItems: 1
    description: A list of languages in which the Statistical Classification is available.
      Supports the indication of multiple languages within a single property. Supports
      use of codes defined by the RFC 1766.
  cdi:catalogDetails:
    $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/CatalogDetails
    description: 'Bundles the information useful for a data catalog entry.


      Examples would be creator, contributor, title, copyright, embargo, and license
      information


      A set of information useful for attribution, data discovery, and access. This
      is information that is tied to the identity of the object. If this information
      changes the version of the associated object changes.'
  cdi:changeFromBase:
    $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/InternationalString
    description: 'Describes the relationship between the variant and its base Statistical
      Classification, including regroupings, aggregations added and extensions. (Source:
      GSIM StatisticalClassification/Changes from base Statistical Classification).'
  cdi:copyright:
    type: array
    items:
      $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/InternationalString
    minItems: 1
    description: Copyright of the statistical classification.
  cdi:displayLabel:
    type: array
    items:
      $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/LabelForDisplay
    minItems: 1
    description: A human-readable display label for the object. Supports the use of
      multiple languages. Repeat for labels with different content, for example, labels
      with differing length limitations.
  cdi:isCurrent:
    type: boolean
    description: Indicates if the statistical classification is currently valid.
  cdi:isFloating:
    type: boolean
    description: 'Indicates if the Statistical Classification is a floating classification.
      In a floating statistical classification, a validity period should be defined
      for all classification Items which will allow the display of the item structure
      and content at different points of time. (Source: GSIM StatisticalClassification/Floating).'
  cdi:isMaintainedBy:
    type: array
    items:
      $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/id-reference
    minItems: 1
  cdi:isIndexedBy:
    type: array
    items:
      $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/id-reference
    minItems: 1
  cdi:isVariantOf:
    $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/id-reference
  cdi:isSuccessorOf:
    type: array
    items:
      $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/id-reference
    minItems: 1
  cdi:isPredecessorOf:
    type: array
    items:
      $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/id-reference
    minItems: 1
  cdi:has:
    type: array
    items:
      $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/id-reference
    minItems: 1
  cdi:purposeOfVariant:
    $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/InternationalString
    description: 'If the Statistical Classification is a variant, notes the specific
      purpose for which it was developed. (Source: GSIM StatisticalClassification/Purpose
      of variant).'
  cdi:rationale:
    $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/InternationalString
    description: Explanation of the reason(s) some decision was made or some object
      exists.
  cdi:releaseDate:
    $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/CombinedDate
    description: Date when the current version of the Statistical Classification was
      released.
  cdi:updateChanges:
    type: array
    items:
      $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/InternationalString
    minItems: 1
    description: Summary description of changes which have occurred since the most
      recent classification version or classification update came into force.
  cdi:usage:
    $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/InternationalString
    description: Explanation of the ways in which the object is employed.
  cdi:validDates:
    $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/DateRange
    description: 'The dates describing the validity period of the object. The date
      from which the object became valid must be defined if the map belongs to a "floating"
      construct. The date at which the object became invalid must be defined if the
      map belongs to a "floating" construct and is no longer valid. Per the Generic
      Statistical Information Model, Statistical Classification: "The date the statistical
      classification enters production use and the date on which the Statistical Classification
      was superseded by a successor version or otherwise ceased to be valid."'
  cdi:identifier:
    $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/Identifier
    description: Identifier for objects requiring short- or long-lasting referencing
      and management.
  cdi:name:
    type: array
    items:
      $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/ObjectName
    minItems: 1
    description: Human understandable name (liguistic signifier, word, phrase, or
      mnemonic). May follow ISO/IEC 11179-5 naming principles, and have context provided
      to specify usage.
  cdi:uses:
    $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/id-reference
  cdi:references:
    $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/id-reference
  cdi:isDefinedBy:
    type: array
    items:
      $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/id-reference
    minItems: 1
  cdi:purpose:
    $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/InternationalString
    description: Intent or reason for the object/the description of the object.
required:
- '@type'
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

