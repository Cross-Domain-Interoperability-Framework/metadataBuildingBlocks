
# Defined Term Set (Schema)

`cdif.bbr.metadata.schemaorgProperties.definedTermSet` *v0.1*

Schema describing a controlled vocabulary or list of defined terms, based on schema.org/DefinedTermSet. Defines properties: @type, schema:name, schema:description, schema:identifier, schema:url, schema:hasDefinedTerm. Items in schema:hasDefinedTerm are individual schema:DefinedTerm objects (uses building block: definedTerm).

[*Status*](http://www.opengis.net/def/status): Under development

## Description

## DefinedTermSet properties

Defines a set of properties for use describing a schema.org DefinedTermSet for the schema.org implementation of the [Cross Domain Interoperability Framework](https://cross-domain-interoperability-framework.github.io/cdifbook/metadata/schemaorgimplementation.html#implementation-of-metadata-content-items) (CDIF) discovery profile.

A DefinedTermSet is a named container of schema:DefinedTerm objects — a controlled vocabulary, code list, or term collection. Each term in `schema:hasDefinedTerm` is validated against the DefinedTerm building block. The set itself must carry at least one identifier (any of `@id`, `schema:name`, or `schema:identifier`) so it can be referenced from `schema:inDefinedTermSet` or other links.

## Examples

### Defined Term Set example.
Minimal DefinedTermSet instance with two terms.
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "ex": "https://example.org/"
  },
  "@id": "ex:sampleMaterialTypes",
  "@type": ["schema:DefinedTermSet"],
  "schema:name": "Sample Material Types",
  "schema:description": "A minimal controlled vocabulary of geological sample material classifications.",
  "schema:hasDefinedTerm": [
    {
      "@type": ["schema:DefinedTerm"],
      "@id": "ex:rock",
      "schema:name": "Rock",
      "schema:termCode": "rock"
    },
    {
      "@type": ["schema:DefinedTerm"],
      "@id": "ex:soil",
      "schema:name": "Soil",
      "schema:termCode": "soil"
    }
  ]
}

```

#### jsonld
```jsonld
{
  "@context": [
    {
      "schema": "http://schema.org/"
    },
    "https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/definedTermSet/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ex": "https://example.org/"
    }
  ],
  "@id": "ex:sampleMaterialTypes",
  "@type": [
    "schema:DefinedTermSet"
  ],
  "schema:name": "Sample Material Types",
  "schema:description": "A minimal controlled vocabulary of geological sample material classifications.",
  "schema:hasDefinedTerm": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "@id": "ex:rock",
      "schema:name": "Rock",
      "schema:termCode": "rock"
    },
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "@id": "ex:soil",
      "schema:name": "Soil",
      "schema:termCode": "soil"
    }
  ]
}
```

#### ttl
```ttl
@prefix ex: <https://example.org/> .
@prefix schema1: <http://schema.org/> .

ex:sampleMaterialTypes a schema1:DefinedTermSet ;
    schema1:description "A minimal controlled vocabulary of geological sample material classifications." ;
    schema1:hasDefinedTerm ex:rock,
        ex:soil ;
    schema1:name "Sample Material Types" .

ex:rock a schema1:DefinedTerm ;
    schema1:name "Rock" ;
    schema1:termCode "rock" .

ex:soil a schema1:DefinedTerm ;
    schema1:name "Soil" ;
    schema1:termCode "soil" .


```


### Complete defined term set example.
DefinedTermSet exercising name, description, identifier, url, and a richer
list of schema:DefinedTerm entries each with their own @id, name, and termCode.
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "ex": "https://example.org/"
  },
  "@id": "ex:nercParameterCodes_P02",
  "@type": ["schema:DefinedTermSet"],
  "schema:name": "NERC Vocabulary Server P02 Parameter Codes",
  "schema:description": "Excerpt of the NERC Vocabulary Server P02 collection of climate and forecast standard names for marine and oceanographic measurements.",
  "schema:identifier": {
    "@type": ["schema:PropertyValue"],
    "schema:propertyID": "https://vocab.nerc.ac.uk/collection/P02/current/",
    "schema:value": "P02",
    "schema:url": "https://vocab.nerc.ac.uk/collection/P02/current/"
  },
  "schema:url": "https://vocab.nerc.ac.uk/collection/P02/current/",
  "schema:hasDefinedTerm": [
    {
      "@type": ["schema:DefinedTerm"],
      "@id": "https://vocab.nerc.ac.uk/collection/P02/current/MSDG/",
      "schema:name": "Marine Sediment Geochemistry",
      "schema:identifier": {
        "@type": ["schema:PropertyValue"],
        "schema:propertyID": "https://vocab.nerc.ac.uk/collection/P02/current/",
        "schema:value": "MSDG",
        "schema:url": "https://vocab.nerc.ac.uk/collection/P02/current/MSDG/"
      },
      "schema:inDefinedTermSet": "https://vocab.nerc.ac.uk/collection/P02/current/",
      "schema:termCode": "MSDG"
    },
    {
      "@type": ["schema:DefinedTerm"],
      "@id": "https://vocab.nerc.ac.uk/collection/P02/current/CHEM/",
      "schema:name": "Water-column chemistry",
      "schema:inDefinedTermSet": "https://vocab.nerc.ac.uk/collection/P02/current/",
      "schema:termCode": "CHEM"
    }
  ]
}

```

#### jsonld
```jsonld
{
  "@context": [
    {
      "schema": "http://schema.org/"
    },
    "https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/definedTermSet/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ex": "https://example.org/"
    }
  ],
  "@id": "ex:nercParameterCodes_P02",
  "@type": [
    "schema:DefinedTermSet"
  ],
  "schema:name": "NERC Vocabulary Server P02 Parameter Codes",
  "schema:description": "Excerpt of the NERC Vocabulary Server P02 collection of climate and forecast standard names for marine and oceanographic measurements.",
  "schema:identifier": {
    "@type": [
      "schema:PropertyValue"
    ],
    "schema:propertyID": "https://vocab.nerc.ac.uk/collection/P02/current/",
    "schema:value": "P02",
    "schema:url": "https://vocab.nerc.ac.uk/collection/P02/current/"
  },
  "schema:url": "https://vocab.nerc.ac.uk/collection/P02/current/",
  "schema:hasDefinedTerm": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "@id": "https://vocab.nerc.ac.uk/collection/P02/current/MSDG/",
      "schema:name": "Marine Sediment Geochemistry",
      "schema:identifier": {
        "@type": [
          "schema:PropertyValue"
        ],
        "schema:propertyID": "https://vocab.nerc.ac.uk/collection/P02/current/",
        "schema:value": "MSDG",
        "schema:url": "https://vocab.nerc.ac.uk/collection/P02/current/MSDG/"
      },
      "schema:inDefinedTermSet": "https://vocab.nerc.ac.uk/collection/P02/current/",
      "schema:termCode": "MSDG"
    },
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "@id": "https://vocab.nerc.ac.uk/collection/P02/current/CHEM/",
      "schema:name": "Water-column chemistry",
      "schema:inDefinedTermSet": "https://vocab.nerc.ac.uk/collection/P02/current/",
      "schema:termCode": "CHEM"
    }
  ]
}
```

#### ttl
```ttl
@prefix ex: <https://example.org/> .
@prefix schema1: <http://schema.org/> .

ex:nercParameterCodes_P02 a schema1:DefinedTermSet ;
    schema1:description "Excerpt of the NERC Vocabulary Server P02 collection of climate and forecast standard names for marine and oceanographic measurements." ;
    schema1:hasDefinedTerm <https://vocab.nerc.ac.uk/collection/P02/current/CHEM/>,
        <https://vocab.nerc.ac.uk/collection/P02/current/MSDG/> ;
    schema1:identifier [ a schema1:PropertyValue ;
            schema1:propertyID "https://vocab.nerc.ac.uk/collection/P02/current/" ;
            schema1:url "https://vocab.nerc.ac.uk/collection/P02/current/" ;
            schema1:value "P02" ] ;
    schema1:name "NERC Vocabulary Server P02 Parameter Codes" ;
    schema1:url "https://vocab.nerc.ac.uk/collection/P02/current/" .

<https://vocab.nerc.ac.uk/collection/P02/current/CHEM/> a schema1:DefinedTerm ;
    schema1:inDefinedTermSet "https://vocab.nerc.ac.uk/collection/P02/current/" ;
    schema1:name "Water-column chemistry" ;
    schema1:termCode "CHEM" .

<https://vocab.nerc.ac.uk/collection/P02/current/MSDG/> a schema1:DefinedTerm ;
    schema1:identifier [ a schema1:PropertyValue ;
            schema1:propertyID "https://vocab.nerc.ac.uk/collection/P02/current/" ;
            schema1:url "https://vocab.nerc.ac.uk/collection/P02/current/MSDG/" ;
            schema1:value "MSDG" ] ;
    schema1:inDefinedTermSet "https://vocab.nerc.ac.uk/collection/P02/current/" ;
    schema1:name "Marine Sediment Geochemistry" ;
    schema1:termCode "MSDG" .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
description: schema.org Defined Term Set schema. A controlled vocabulary or named
  list of schema:DefinedTerm objects.
type: object
properties:
  '@id':
    type: string
    description: Persistent identifier (URI) for this DefinedTermSet.
  '@type':
    type: array
    items:
      type: string
    contains:
      const: schema:DefinedTermSet
    minItems: 1
  schema:name:
    type: string
    description: Human-readable name (label) for the term set.
  schema:description:
    type: string
    description: Description of the scope and purpose of the term set.
  schema:identifier:
    description: Formal identifier for the term set, as a string or structured PropertyValue.
    anyOf:
    - type: string
    - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/identifier/schema.yaml
  schema:url:
    type: string
    format: uri
    description: URL where the term set is published.
  schema:hasDefinedTerm:
    type: array
    minItems: 1
    description: The terms that make up this set. Each item is a schema:DefinedTerm.
    items:
      $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/definedTerm/schema.yaml
allOf:
- required:
  - '@type'
  - schema:hasDefinedTerm
- anyOf:
  - required:
    - schema:name
  - required:
    - schema:identifier
  - required:
    - '@id'
x-jsonld-prefixes:
  schema: http://schema.org/

```

Links to the schema:

* YAML version: [schema.yaml](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/definedTermSet/schema.json)
* JSON version: [schema.json](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/definedTermSet/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "schema": "http://schema.org/",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/definedTermSet/context.jsonld)

## Sources

* [schema.org](https://schema.org/DefinedTermSet)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/Cross-Domain-Interoperability-Framework/metadataBuildingBlocks](https://github.com/Cross-Domain-Interoperability-Framework/metadataBuildingBlocks)
* Path: `_sources/schemaorgProperties/definedTermSet`

