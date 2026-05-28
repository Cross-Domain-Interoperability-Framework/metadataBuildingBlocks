
# CDIF Codelist (Schema)

`cdif.bbr.metadata.profiles.cdifProfile.cdifCodelist` *v0.1*

A controlled-vocabulary codelist as a skos:ConceptScheme constrained for CDIF use: resolvable @id, schema:identifier and schema:dateModified, schema:license or schema:conditionsOfAccess, and skos:hasTopConcept whose items are CdifCodelistConcept (each requiring @id, skos:inScheme, skos:prefLabel, skos:notation; hierarchy expressed via paired skos:narrower/skos:broader). Referenced by CDIFCodelistProfile and by cdifEnumerationDomain (cdif:references).

[*Status*](http://www.opengis.net/def/status): Under development

## Description

# CDIF Codelist

A controlled-vocabulary **codelist** modeled as a `skos:ConceptScheme` constrained for CDIF use.

The scheme carries a resolvable `@id`, CDIF metadata (`schema:identifier`, `schema:dateModified`, `schema:license` or `schema:conditionsOfAccess`), and identifies its top concepts via `skos:hasTopConcept`. Each member concept is a `CdifCodelistConcept`:

- **Required:** `@id`, `skos:inScheme`, `skos:prefLabel`, `skos:notation`
- **Optional:** `skos:definition` and any other SKOS properties (JSON-LD is open-world)
- **Hierarchy:** where it exists, both `skos:narrower` (for JSON tree traversal) and `skos:broader` (for upward navigation) must be explicit; an inline narrower concept must declare `skos:broader` back to its parent.

CDIF `schema:` metadata properties take precedence over the equivalent `dcterms:` properties from the base `skos:ConceptScheme`.

## Consumers

- **`CDIFCodelistProfile`** — the codelist profile composes this building block.
- **`cdifEnumerationDomain`** — references a codelist (by value or by `@id`) via `cdif:references` to define the allowed values of an enumerated value domain.

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
type: object
title: CDIF Codelist
description: A controlled-vocabulary codelist implemented as a skos:ConceptScheme
  constrained for CDIF use. The scheme must have a resolvable @id and identify its
  top concepts via skos:hasTopConcept; each concept (CdifCodelistConcept) must have
  a resolvable @id, skos:inScheme, skos:prefLabel, and skos:notation. Hierarchical
  concepts must declare both skos:narrower (for JSON tree traversal) and skos:broader
  (for upward navigation) where hierarchy exists. CDIF metadata properties (schema:identifier,
  schema:dateModified, schema:license or schema:conditionsOfAccess) take precedence
  over the equivalent dcterms properties from the base skos:ConceptScheme.
properties:
  '@context':
    description: JSON-LD context (an object) declaring the skos namespace prefix and
      any additional prefixes used in concept URIs.
    type: object
    properties:
      skos:
        const: http://www.w3.org/2004/02/skos/core#
    required:
    - skos
  '@id':
    type: string
    description: URI identifier for this concept scheme.
  '@type':
    type: array
    items:
      type: string
    contains:
      const: skos:ConceptScheme
    minItems: 1
  schema:identifier:
    description: Primary identifier for the codelist. May be a string URI or a structured
      PropertyValue.
    anyOf:
    - type: string
    - type: object
      properties:
        '@type':
          type: array
          items:
            type: string
          contains:
            const: schema:PropertyValue
        schema:propertyID:
          type: string
          x-jsonld-id: http://schema.org/propertyID
        schema:value:
          type: string
          x-jsonld-id: http://schema.org/value
        schema:url:
          type: string
          x-jsonld-id: http://schema.org/url
    x-jsonld-id: http://schema.org/identifier
  schema:dateModified:
    type: string
    description: ISO 8601 date when the codelist was last modified.
    x-jsonld-id: http://schema.org/dateModified
  schema:url:
    type: string
    format: uri
    description: Web location of a page describing the codelist.
    default: missing
    x-jsonld-id: http://schema.org/url
  schema:license:
    description: License for the codelist.
    type: array
    items:
      anyOf:
      - type: string
      - type: object
        properties:
          '@id':
            type: string
    x-jsonld-id: http://schema.org/license
  schema:conditionsOfAccess:
    description: Text statement of access conditions for the codelist.
    type: array
    items:
      type: string
    x-jsonld-id: http://schema.org/conditionsOfAccess
  skos:prefLabel:
    description: Preferred lexical label for the concept scheme. A single string,
      a single language-tagged value, or an array of language-tagged values. Each
      language should appear at most once.
    type: string
    x-jsonld-id: http://www.w3.org/2004/02/skos/core#prefLabel
  skos:definition:
    description: Formal explanation of the meaning or purpose of this concept scheme.
    type: string
    x-jsonld-id: http://www.w3.org/2004/02/skos/core#definition
  skos:note:
    description: General note about the concept scheme.
    type: string
    x-jsonld-id: http://www.w3.org/2004/02/skos/core#note
  skos:hasTopConcept:
    description: Top-level concepts that have no skos:broader in this scheme. Required
      for hierarchical codelists.
    type: array
    minItems: 1
    items:
      $ref: '#/$defs/CdifCodelistConcept'
    x-jsonld-id: http://www.w3.org/2004/02/skos/core#hasTopConcept
  schema:subjectOf:
    type: array
    items:
      type: object
      properties:
        '@id':
          type: object
          properties:
            '@id':
              const: https://w3id.org/cdif/codelist/1.0
    x-jsonld-id: http://schema.org/subjectOf
anyOf:
- required:
  - schema:license
- required:
  - schema:conditionsOfAccess
required:
- '@id'
- skos:prefLabel
- schema:identifier
- schema:dateModified
- skos:hasTopConcept
$defs:
  CdifCodelistConcept:
    description: A SKOS Concept constrained for CDIF codelist use. Must have a resolvable
      @id, skos:inScheme, skos:notation, and skos:prefLabel. Becasue JSON-LD is an
      open-world implementation, any other skos properties may be included.
    type: object
    properties:
      '@id':
        type: string
        description: Globally unique, resolvable URI for this concept.
      skos:inScheme:
        description: The concept scheme this concept belongs to. Required for CDIF
          codelist concepts.
        type: array
        items:
          type: object
          properties:
            '@id':
              type: string
          required:
          - '@id'
        x-jsonld-id: http://www.w3.org/2004/02/skos/core#inScheme
      skos:prefLabel:
        description: Preferred lexical label for this concept. A single string, a
          single language-tagged value, or an array of language-tagged values. Each
          language should appear at most once.
        type: string
        x-jsonld-id: http://www.w3.org/2004/02/skos/core#prefLabel
      skos:notation:
        description: Classification code for this concept within a scheme.
        type: string
        x-jsonld-id: http://www.w3.org/2004/02/skos/core#notation
      skos:definition:
        description: Formal definition of this concept. Optional for CDIF codelist
          concepts. A plain string.
        type: string
        x-jsonld-id: http://www.w3.org/2004/02/skos/core#definition
      skos:narrower:
        description: Narrower (child) concepts. If present, each inline concept must
          also declare skos:broader pointing back to the parent concept. Both skos:narrower
          and skos:broader must be explicit in CDIF codelists.
        type: array
        items:
          anyOf:
          - type: object
            properties:
              '@id':
                type: string
            required:
            - '@id'
          - allOf:
            - $ref: '#/$defs/CdifCodelistConcept'
            - required:
              - skos:broader
        x-jsonld-id: http://www.w3.org/2004/02/skos/core#narrower
      skos:broader:
        description: Broader (parent) concepts. Required on any concept that appears
          as a skos:narrower value of another concept. CDIF requires both directions
          to be explicit for hierarchy traversal.
        type: array
        items:
          type: object
          properties:
            '@id':
              type: string
          required:
          - '@id'
        x-jsonld-id: http://www.w3.org/2004/02/skos/core#broader
    required:
    - '@id'
    - skos:inScheme
    - skos:prefLabel
    - skos:notation
x-jsonld-prefixes:
  skos: http://www.w3.org/2004/02/skos/core#
  dcterms: http://purl.org/dc/terms/
  schema: http://schema.org/

```

Links to the schema:

* YAML version: [schema.yaml](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/profiles/cdifProfile/cdifCodelist/schema.json)
* JSON version: [schema.json](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/profiles/cdifProfile/cdifCodelist/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "skos": "http://www.w3.org/2004/02/skos/core#",
    "dcterms": "http://purl.org/dc/terms/",
    "schema": "http://schema.org/",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/profiles/cdifProfile/cdifCodelist/context.jsonld)

## Sources

* [SKOS Reference](https://www.w3.org/TR/skos-reference/)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/Cross-Domain-Interoperability-Framework/metadataBuildingBlocks](https://github.com/Cross-Domain-Interoperability-Framework/metadataBuildingBlocks)
* Path: `_sources/profiles/cdifProfile/cdifCodelist`

