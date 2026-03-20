
# SKOS Collection (Schema)

`cdif.bbr.metadata.skosProperties.skosCollection` *v0.1*

JSON Schema for SKOS Collection and OrderedCollection in JSON-LD form. Collection groups concepts via skos:member; OrderedCollection preserves ordering via JSON-LD @list. References skosConcept building block for concept items and LanguageTaggedValue.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

## SKOS Collection

JSON Schema for [SKOS Collection](https://www.w3.org/TR/skos-reference/#collections) and [OrderedCollection](https://www.w3.org/TR/skos-reference/#collections) in JSON-LD form.

### Collection

An unordered grouping of concepts. Must have `@type` including `skos:Collection`, a `skos:prefLabel`, and at least one `skos:member`. Members can be inline concept objects, `@id` references, or nested collections.

### OrderedCollection

A subclass of Collection where member ordering is meaningful. Must have `@type` including `skos:OrderedCollection`, a `skos:prefLabel`, and `skos:memberList` using the JSON-LD `@list` construct.

Both types reference the `skosConcept` building block for concept items and `LanguageTaggedValue` for multilingual labels.

## Examples

### SKOS Collection example
Solid Earth Disciplines collection grouping geology, geophysics,
and geochemistry concepts.
#### json
```json
{
  "@context": {
    "skos": "http://www.w3.org/2004/02/skos/core#",
    "ex": "https://example.org/vocab/"
  },
  "@id": "ex:solid-earth-disciplines",
  "@type": ["skos:Collection"],
  "skos:prefLabel": [
    {"@value": "Solid Earth Disciplines", "@language": "en"}
  ],
  "skos:definition": "A grouping of Earth science concepts focused on solid Earth processes.",
  "skos:member": [
    {
      "@id": "ex:geology",
      "@type": ["skos:Concept"],
      "skos:prefLabel": "Geology",
      "skos:notation": ["01"],
      "skos:inScheme": {"@id": "ex:earth-science-topics"}
    },
    {
      "@id": "ex:geophysics",
      "@type": ["skos:Concept"],
      "skos:prefLabel": "Geophysics",
      "skos:notation": ["03"],
      "skos:inScheme": {"@id": "ex:earth-science-topics"}
    },
    {"@id": "ex:geochemistry"}
  ]
}

```

#### jsonld
```jsonld
{
  "@context": [
    {
      "skos": "http://www.w3.org/2004/02/skos/core#"
    },
    "https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/skosProperties/skosCollection/context.jsonld",
    {
      "skos": "http://www.w3.org/2004/02/skos/core#",
      "ex": "https://example.org/vocab/"
    }
  ],
  "@id": "ex:solid-earth-disciplines",
  "@type": [
    "skos:Collection"
  ],
  "skos:prefLabel": [
    {
      "@value": "Solid Earth Disciplines",
      "@language": "en"
    }
  ],
  "skos:definition": "A grouping of Earth science concepts focused on solid Earth processes.",
  "skos:member": [
    {
      "@id": "ex:geology",
      "@type": [
        "skos:Concept"
      ],
      "skos:prefLabel": "Geology",
      "skos:notation": [
        "01"
      ],
      "skos:inScheme": {
        "@id": "ex:earth-science-topics"
      }
    },
    {
      "@id": "ex:geophysics",
      "@type": [
        "skos:Concept"
      ],
      "skos:prefLabel": "Geophysics",
      "skos:notation": [
        "03"
      ],
      "skos:inScheme": {
        "@id": "ex:earth-science-topics"
      }
    },
    {
      "@id": "ex:geochemistry"
    }
  ]
}
```

#### ttl
```ttl
@prefix ex: <https://example.org/vocab/> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .

ex:solid-earth-disciplines a skos:Collection ;
    skos:definition "A grouping of Earth science concepts focused on solid Earth processes." ;
    skos:member ex:geochemistry,
        ex:geology,
        ex:geophysics ;
    skos:prefLabel "Solid Earth Disciplines"@en .

ex:geology a skos:Concept ;
    skos:inScheme ex:earth-science-topics ;
    skos:notation "01" ;
    skos:prefLabel "Geology" .

ex:geophysics a skos:Concept ;
    skos:inScheme ex:earth-science-topics ;
    skos:notation "03" ;
    skos:prefLabel "Geophysics" .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: SKOS Collection
description: JSON Schema for SKOS Collection and OrderedCollection in JSON-LD form.
  A Collection is a meaningful grouping of concepts; an OrderedCollection preserves
  member ordering via the JSON-LD @list construct. Based on the W3C SKOS Reference
  (https://www.w3.org/TR/skos-reference/).
anyOf:
- $ref: '#/$defs/Collection'
- $ref: '#/$defs/OrderedCollection'
$defs:
  Collection:
    type: object
    description: A SKOS Collection -- a meaningful grouping of concepts. Disjoint
      with Concept and ConceptScheme.
    properties:
      '@context':
        description: JSON-LD context declaring the skos namespace prefix.
        anyOf:
        - type: object
          properties:
            skos:
              const: http://www.w3.org/2004/02/skos/core#
          required:
          - skos
        - type: array
          items:
            anyOf:
            - type: string
            - type: object
          contains:
            type: object
            properties:
              skos:
                const: http://www.w3.org/2004/02/skos/core#
            required:
            - skos
      '@id':
        type: string
        description: URI identifier for this collection.
      '@type':
        type: array
        items:
          type: string
        contains:
          const: skos:Collection
        minItems: 1
      skos:prefLabel:
        description: Preferred lexical label for this collection.
        anyOf:
        - type: string
        - type: array
          items:
            $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/skosProperties/skosConcept/schema.yaml#/$defs/LanguageTaggedValue
      skos:altLabel:
        description: Alternative lexical labels.
        anyOf:
        - type: string
        - type: array
          items:
            anyOf:
            - type: string
            - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/skosProperties/skosConcept/schema.yaml#/$defs/LanguageTaggedValue
      skos:notation:
        description: Classification code for this collection.
        anyOf:
        - type: string
        - type: array
          items:
            type: string
      skos:definition:
        description: Formal explanation of the purpose of this collection.
        anyOf:
        - type: string
        - type: array
          items:
            anyOf:
            - type: string
            - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/skosProperties/skosConcept/schema.yaml#/$defs/LanguageTaggedValue
      skos:note:
        description: General note about this collection.
        anyOf:
        - type: string
        - type: array
          items:
            anyOf:
            - type: string
            - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/skosProperties/skosConcept/schema.yaml#/$defs/LanguageTaggedValue
      skos:member:
        description: Members of this collection (concepts or nested collections, inline
          or by @id reference).
        type: array
        minItems: 1
        items:
          anyOf:
          - type: object
            properties:
              '@id':
                type: string
            required:
            - '@id'
          - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/skosProperties/skosConcept/schema.yaml
          - $ref: '#/$defs/Collection'
    required:
    - '@type'
    - skos:prefLabel
    - skos:member
  OrderedCollection:
    type: object
    description: A SKOS OrderedCollection -- concepts where both grouping and ordering
      are meaningful. Subclass of Collection. Uses JSON-LD @list for the member list.
    properties:
      '@context':
        description: JSON-LD context declaring the skos namespace prefix.
        anyOf:
        - type: object
          properties:
            skos:
              const: http://www.w3.org/2004/02/skos/core#
          required:
          - skos
        - type: array
          items:
            anyOf:
            - type: string
            - type: object
          contains:
            type: object
            properties:
              skos:
                const: http://www.w3.org/2004/02/skos/core#
            required:
            - skos
      '@id':
        type: string
        description: URI identifier for this ordered collection.
      '@type':
        type: array
        items:
          type: string
        contains:
          const: skos:OrderedCollection
        minItems: 1
      skos:prefLabel:
        description: Preferred lexical label for this ordered collection.
        anyOf:
        - type: string
        - type: array
          items:
            $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/skosProperties/skosConcept/schema.yaml#/$defs/LanguageTaggedValue
      skos:altLabel:
        description: Alternative lexical labels.
        anyOf:
        - type: string
        - type: array
          items:
            anyOf:
            - type: string
            - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/skosProperties/skosConcept/schema.yaml#/$defs/LanguageTaggedValue
      skos:notation:
        description: Classification code for this ordered collection.
        anyOf:
        - type: string
        - type: array
          items:
            type: string
      skos:memberList:
        description: Ordered list of members using JSON-LD @list construct.
        type: object
        properties:
          '@list':
            type: array
            minItems: 1
            items:
              anyOf:
              - type: object
                properties:
                  '@id':
                    type: string
                required:
                - '@id'
              - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/skosProperties/skosConcept/schema.yaml
    required:
    - '@type'
    - skos:prefLabel
    - skos:memberList
x-jsonld-prefixes:
  skos: http://www.w3.org/2004/02/skos/core#

```

Links to the schema:

* YAML version: [schema.yaml](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/skosProperties/skosCollection/schema.json)
* JSON version: [schema.json](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/skosProperties/skosCollection/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "skos": "http://www.w3.org/2004/02/skos/core#",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/skosProperties/skosCollection/context.jsonld)

## Sources

* [W3C SKOS Reference](https://www.w3.org/TR/skos-reference/)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/Cross-Domain-Interoperability-Framework/metadataBuildingBlocks](https://github.com/Cross-Domain-Interoperability-Framework/metadataBuildingBlocks)
* Path: `_sources/skosProperties/skosCollection`

