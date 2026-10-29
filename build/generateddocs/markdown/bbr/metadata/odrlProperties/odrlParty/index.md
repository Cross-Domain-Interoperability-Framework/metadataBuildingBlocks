
# ODRL Party (Schema)

`cdif.bbr.metadata.odrlProperties.odrlParty` *v0.1*

W3C ODRL 2.2 Party (a person, organization or agent identified by IRI) or PartyCollection (a group of parties, identified by @id, or by odrl:source narrowed with odrl:refinement). A Party may be typed odrl:Party, schema:Person or schema:Organization (ODRL declares Party a subclass of these), and a schema.org-typed party is validated by the person or organization block. Used for the assigner and assignee of ODRL rules and policies. Uses building blocks: odrlConstraint (odrlProperties), person, organization (schemaorgProperties), objectReference (cdifDataType).

[*Status*](http://www.opengis.net/def/status): Under development

## Description

## ODRL Party

W3C ODRL 2.2 Party (a person, organization or agent identified by IRI) or PartyCollection (a group of parties, identified by @id, or by odrl:source narrowed with odrl:refinement). A Party may be typed odrl:Party, schema:Person or schema:Organization (ODRL declares Party a subclass of these), and a schema.org-typed party is validated by the person or organization block. Used for the assigner and assignee of ODRL rules and policies.

Generic W3C ODRL; CDIF-specific rules belong in profile blocks such as [odrlOffer](../odrlOffer/).

### Dependencies

- [person](../../schemaorgProperties/person/)
- [organization](../../schemaorgProperties/organization/)
- [odrlConstraint](../odrlConstraint/)
- [objectReference](../../cdifDataType/objectReference/)

## Examples

### ODRL refined PartyCollection
The registered users of a repository, refined to those located in the UK.
#### json
```json
{
  "@context": {
    "odrl": "http://www.w3.org/ns/odrl/2/"
  },
  "@type": [
    "odrl:PartyCollection"
  ],
  "odrl:source": {
    "@id": "https://example.org/partycollection/registered-users"
  },
  "odrl:refinement": [
    {
      "@type": [
        "odrl:Constraint"
      ],
      "odrl:leftOperand": {
        "@id": "odrl:spatial"
      },
      "odrl:operator": {
        "@id": "odrl:eq"
      },
      "odrl:rightOperand": {
        "@id": "http://publications.europa.eu/resource/authority/country/GBR"
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
      "odrl": "http://www.w3.org/ns/odrl/2/"
    },
    "https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/odrlProperties/odrlParty/context.jsonld",
    {
      "odrl": "http://www.w3.org/ns/odrl/2/"
    }
  ],
  "@type": [
    "odrl:PartyCollection"
  ],
  "odrl:source": {
    "@id": "https://example.org/partycollection/registered-users"
  },
  "odrl:refinement": [
    {
      "@type": [
        "odrl:Constraint"
      ],
      "odrl:leftOperand": {
        "@id": "odrl:spatial"
      },
      "odrl:operator": {
        "@id": "odrl:eq"
      },
      "odrl:rightOperand": {
        "@id": "http://publications.europa.eu/resource/authority/country/GBR"
      }
    }
  ]
}
```

#### ttl
```ttl
@prefix odrl: <http://www.w3.org/ns/odrl/2/> .

[] a odrl:PartyCollection ;
    odrl:refinement [ a odrl:Constraint ;
            odrl:leftOperand odrl:spatial ;
            odrl:operator odrl:eq ;
            odrl:rightOperand <http://publications.europa.eu/resource/authority/country/GBR> ] ;
    odrl:source <https://example.org/partycollection/registered-users> .


```


### ODRL Party typed as a schema.org Person
A person dual-typed odrl:Party and schema:Person, validated by the
schemaorgProperties person block (name or identifier required).
#### json
```json
{
  "@context": {
    "odrl": "http://www.w3.org/ns/odrl/2/",
    "schema": "http://schema.org/"
  },
  "@type": [
    "odrl:Party",
    "schema:Person"
  ],
  "@id": "https://example.org/person/jane-researcher",
  "schema:name": "Researcher, Jane",
  "schema:identifier": "https://orcid.org/0000-0000-0000-0000",
  "schema:affiliation": {
    "@type": [
      "schema:Organization"
    ],
    "schema:name": "Example University"
  }
}

```

#### jsonld
```jsonld
{
  "@context": [
    {
      "odrl": "http://www.w3.org/ns/odrl/2/",
      "schema": "http://schema.org/"
    },
    "https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/odrlProperties/odrlParty/context.jsonld",
    {
      "odrl": "http://www.w3.org/ns/odrl/2/",
      "schema": "http://schema.org/"
    }
  ],
  "@type": [
    "odrl:Party",
    "schema:Person"
  ],
  "@id": "https://example.org/person/jane-researcher",
  "schema:name": "Researcher, Jane",
  "schema:identifier": "https://orcid.org/0000-0000-0000-0000",
  "schema:affiliation": {
    "@type": [
      "schema:Organization"
    ],
    "schema:name": "Example University"
  }
}
```

#### ttl
```ttl
@prefix odrl: <http://www.w3.org/ns/odrl/2/> .
@prefix schema1: <http://schema.org/> .

<https://example.org/person/jane-researcher> a schema1:Person,
        odrl:Party ;
    schema1:affiliation [ a schema1:Organization ;
            schema1:name "Example University" ] ;
    schema1:identifier "https://orcid.org/0000-0000-0000-0000" ;
    schema1:name "Researcher, Jane" .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: ODRL Party
description: 'An ODRL 2.2 Party (https://www.w3.org/TR/odrl-model/#party) or PartyCollection
  (https://www.w3.org/TR/odrl-model/#party-collection): who takes a role (assigner,
  assignee) in a rule. A Party is a person, organization or agent identified by its
  IRI. A PartyCollection is a group of parties: either the collection itself, identified
  by @id, or a subset of one, where odrl:source names the collection and odrl:refinement
  narrows it (e.g. registered users located in the UK).'
type: object
properties:
  '@context':
    type: object
    description: JSON-LD namespace prefixes for ODRL and schema.org properties.
    properties:
      odrl:
        const: http://www.w3.org/ns/odrl/2/
      schema:
        const: http://schema.org/
anyOf:
- $ref: '#/$defs/Party'
- $ref: '#/$defs/PartyCollection'
$defs:
  Party:
    description: Typed odrl:Party, schema:Person or schema:Organization. ODRL declares
      odrl:Party a subclass of schema:Person or schema:Organization (among FOAF and
      vCard classes), and gives odrl:assigner and odrl:assignee the range odrl:Party,
      so a schema.org-typed node in those roles is an odrl:Party without saying so.
      A schema:Person is validated by the person block and a schema:Organization by
      the organization block. A person may also carry odrl:Party; an organization
      may not, because the organization block only accepts schema.org organization
      types in @type.
    type: object
    properties:
      '@type':
        type: array
        items:
          type: string
      '@id':
        type: string
        format: iri
    required:
    - '@type'
    - '@id'
    anyOf:
    - properties:
        '@type':
          contains:
            const: odrl:Party
    - properties:
        '@type':
          contains:
            const: schema:Person
    - properties:
        '@type':
          contains:
            const: schema:Organization
    allOf:
    - if:
        properties:
          '@type':
            contains:
              const: schema:Person
      then:
        $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/person/schema.yaml
    - if:
        properties:
          '@type':
            contains:
              const: schema:Organization
      then:
        $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/organization/schema.yaml
  PartyCollection:
    description: Per ODRL, a refined collection is identified through odrl:source,
      so odrl:refinement requires odrl:source.
    type: object
    properties:
      '@type':
        type: array
        items:
          type: string
        contains:
          const: odrl:PartyCollection
      '@id':
        type: string
        format: iri
      odrl:source:
        description: The collection this one is drawn from.
        $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifDataType/objectReference/schema.yaml
        x-jsonld-id: http://www.w3.org/ns/odrl/2/source
      odrl:refinement:
        description: Constraints selecting the members of odrl:source that belong
          to this collection.
        type: array
        minItems: 1
        items:
          $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/odrlProperties/odrlConstraint/schema.yaml
        x-jsonld-id: http://www.w3.org/ns/odrl/2/refinement
    required:
    - '@type'
    anyOf:
    - required:
      - '@id'
    - required:
      - odrl:source
    dependentRequired:
      odrl:refinement:
      - odrl:source
x-jsonld-prefixes:
  odrl: http://www.w3.org/ns/odrl/2/
  schema: http://schema.org/
x-bblocks-metadata:
  itemIdentifier: cdif.bbr.metadata.odrlProperties.odrlParty
  register: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/register.json
  version: '0.1'
  dateOfLastChange: '2026-10-29'

```

Links to the schema:

* YAML version: [schema.yaml](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/odrlProperties/odrlParty/schema.json)
* JSON version: [schema.json](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/odrlProperties/odrlParty/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "schema": "http://schema.org/",
    "skos": "http://www.w3.org/2004/02/skos/core#",
    "odrl": "http://www.w3.org/ns/odrl/2/",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/odrlProperties/odrlParty/context.jsonld)

## Sources

* [W3C ODRL Information Model 2.2](https://www.w3.org/TR/odrl-model/)
* [W3C ODRL Vocabulary & Expression 2.2](https://www.w3.org/TR/odrl-vocab/)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/Cross-Domain-Interoperability-Framework/metadataBuildingBlocks](https://github.com/Cross-Domain-Interoperability-Framework/metadataBuildingBlocks)
* Path: `_sources/odrlProperties/odrlParty`

