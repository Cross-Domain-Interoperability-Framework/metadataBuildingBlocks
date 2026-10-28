
# ODRL Action (Schema)

`cdif.bbr.metadata.odrlProperties.odrlAction` *v0.1*

W3C ODRL 2.2 Action as used in a rule: a reference to an action IRI, or a refined action holding the action in rdf:value plus odrl:refinement constraints. Actions are open IRIs, so ODRL profile actions validate. Uses building blocks: odrlTerms, odrlConstraint (odrlProperties).

[*Status*](http://www.opengis.net/def/status): Under development

## Description

## ODRL Action

W3C ODRL 2.2 Action as used in a rule: a reference to an action IRI, or a refined action holding the action in rdf:value plus odrl:refinement constraints. Actions are open IRIs, so ODRL profile actions validate.

Generic W3C ODRL; CDIF-specific rules belong in profile blocks such as [odrlOffer](../odrlOffer/).

### Dependencies

- [odrlTerms](../odrlTerms/)
- [odrlConstraint](../odrlConstraint/)

## Examples

### ODRL refined action
odrl:reproduce, refined to at most 10 copies.
#### json
```json
{
  "@context": {
    "odrl": "http://www.w3.org/ns/odrl/2/",
    "rdf": "http://www.w3.org/1999/02/22-rdf-syntax-ns#",
    "xsd": "http://www.w3.org/2001/XMLSchema#"
  },
  "rdf:value": {
    "@id": "odrl:reproduce"
  },
  "odrl:refinement": [
    {
      "@type": [
        "odrl:Constraint"
      ],
      "odrl:leftOperand": {
        "@id": "odrl:count"
      },
      "odrl:operator": {
        "@id": "odrl:lteq"
      },
      "odrl:rightOperand": {
        "@value": "10",
        "@type": "xsd:integer"
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
      "odrl": "http://www.w3.org/ns/odrl/2/",
      "rdf": "http://www.w3.org/1999/02/22-rdf-syntax-ns#",
      "xsd": "http://www.w3.org/2001/XMLSchema#"
    },
    "https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/odrlProperties/odrlAction/context.jsonld",
    {
      "odrl": "http://www.w3.org/ns/odrl/2/",
      "rdf": "http://www.w3.org/1999/02/22-rdf-syntax-ns#",
      "xsd": "http://www.w3.org/2001/XMLSchema#"
    }
  ],
  "rdf:value": {
    "@id": "odrl:reproduce"
  },
  "odrl:refinement": [
    {
      "@type": [
        "odrl:Constraint"
      ],
      "odrl:leftOperand": {
        "@id": "odrl:count"
      },
      "odrl:operator": {
        "@id": "odrl:lteq"
      },
      "odrl:rightOperand": {
        "@value": "10",
        "@type": "xsd:integer"
      }
    }
  ]
}
```

#### ttl
```ttl
@prefix odrl: <http://www.w3.org/ns/odrl/2/> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

[] rdf:value odrl:reproduce ;
    odrl:refinement [ a odrl:Constraint ;
            odrl:leftOperand odrl:count ;
            odrl:operator odrl:lteq ;
            odrl:rightOperand 10 ] .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: ODRL Action
description: 'An ODRL 2.2 Action (https://www.w3.org/TR/odrl-model/#action) as used
  in a rule: either a reference to the action ({"@id": "odrl:use"}), or, when the
  action itself is narrowed, an object holding the action in rdf:value plus odrl:refinement
  constraints (e.g. print, at most 1200 dpi). Actions are open IRIs (odrlTerms), so
  ODRL profile actions validate.'
type: object
properties:
  '@context':
    type: object
    description: JSON-LD namespace prefixes for ODRL properties.
    properties:
      odrl:
        const: http://www.w3.org/ns/odrl/2/
      rdf:
        const: http://www.w3.org/1999/02/22-rdf-syntax-ns#
anyOf:
- $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/odrlProperties/odrlTerms/schema.yaml#/$defs/Action
- $ref: '#/$defs/RefinedAction'
$defs:
  RefinedAction:
    type: object
    properties:
      rdf:value:
        $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/odrlProperties/odrlTerms/schema.yaml#/$defs/Action
        x-jsonld-id: http://www.w3.org/1999/02/22-rdf-syntax-ns#value
      odrl:refinement:
        type: array
        minItems: 1
        items:
          $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/odrlProperties/odrlConstraint/schema.yaml
        x-jsonld-id: http://www.w3.org/ns/odrl/2/refinement
    required:
    - rdf:value
    - odrl:refinement
x-jsonld-prefixes:
  odrl: http://www.w3.org/ns/odrl/2/
  rdf: http://www.w3.org/1999/02/22-rdf-syntax-ns#
  xsd: http://www.w3.org/2001/XMLSchema#
x-bblocks-metadata:
  itemIdentifier: cdif.bbr.metadata.odrlProperties.odrlAction
  register: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/register.json
  version: '0.1'
  dateOfLastChange: '2026-10-28'

```

Links to the schema:

* YAML version: [schema.yaml](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/odrlProperties/odrlAction/schema.json)
* JSON version: [schema.json](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/odrlProperties/odrlAction/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "odrl": "http://www.w3.org/ns/odrl/2/",
    "rdf": "http://www.w3.org/1999/02/22-rdf-syntax-ns#",
    "xsd": "http://www.w3.org/2001/XMLSchema#",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/odrlProperties/odrlAction/context.jsonld)

## Sources

* [W3C ODRL Information Model 2.2](https://www.w3.org/TR/odrl-model/)
* [W3C ODRL Vocabulary & Expression 2.2](https://www.w3.org/TR/odrl-vocab/)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/Cross-Domain-Interoperability-Framework/metadataBuildingBlocks](https://github.com/Cross-Domain-Interoperability-Framework/metadataBuildingBlocks)
* Path: `_sources/odrlProperties/odrlAction`

