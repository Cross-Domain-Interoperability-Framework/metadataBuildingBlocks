
# ODRL Constraint (Schema)

`cdif.bbr.metadata.odrlProperties.odrlConstraint` *v0.1*

W3C ODRL 2.2 Constraint (leftOperand, operator, rightOperand or rightOperandReference, with optional dataType, unit and status) or LogicalConstraint combining constraints with exactly one of odrl:and, odrl:or, odrl:xone or odrl:andSequence. Operands and operators are open IRIs. Uses building blocks: odrlTerms (odrlProperties), objectReference (cdifDataType).

[*Status*](http://www.opengis.net/def/status): Under development

## Description

## ODRL Constraint

W3C ODRL 2.2 Constraint (leftOperand, operator, rightOperand or rightOperandReference, with optional dataType, unit and status) or LogicalConstraint combining constraints with exactly one of odrl:and, odrl:or, odrl:xone or odrl:andSequence. Operands and operators are open IRIs.

Generic W3C ODRL; CDIF-specific rules belong in profile blocks such as [odrlOffer](../odrlOffer/).

### Dependencies

- [odrlTerms](../odrlTerms/)
- [objectReference](../../cdifDataType/objectReference/)

## Examples

### ODRL LogicalConstraint
Users located in the UK or in Ireland: an odrl:or over two spatial constraints.
#### json
```json
{
  "@context": {
    "odrl": "http://www.w3.org/ns/odrl/2/"
  },
  "@type": [
    "odrl:LogicalConstraint"
  ],
  "odrl:or": {
    "@list": [
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
      },
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
          "@id": "http://publications.europa.eu/resource/authority/country/IRL"
        }
      }
    ]
  }
}

```

#### jsonld
```jsonld
{
  "@context": [
    {
      "odrl": "http://www.w3.org/ns/odrl/2/"
    },
    "https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/odrlProperties/odrlConstraint/context.jsonld",
    {
      "odrl": "http://www.w3.org/ns/odrl/2/"
    }
  ],
  "@type": [
    "odrl:LogicalConstraint"
  ],
  "odrl:or": {
    "@list": [
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
      },
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
          "@id": "http://publications.europa.eu/resource/authority/country/IRL"
        }
      }
    ]
  }
}
```

#### ttl
```ttl
@prefix odrl: <http://www.w3.org/ns/odrl/2/> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .

[] a odrl:LogicalConstraint ;
    odrl:or ( [ a odrl:Constraint ;
                odrl:leftOperand odrl:spatial ;
                odrl:operator odrl:eq ;
                odrl:rightOperand <http://publications.europa.eu/resource/authority/country/GBR> ] [ a odrl:Constraint ;
                odrl:leftOperand odrl:spatial ;
                odrl:operator odrl:eq ;
                odrl:rightOperand <http://publications.europa.eu/resource/authority/country/IRL> ] ) .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: ODRL Constraint
description: An ODRL 2.2 Constraint (https://www.w3.org/TR/odrl-model/#constraint)
  or LogicalConstraint (https://www.w3.org/TR/odrl-model/#constraint-logical). A Constraint
  compares a left operand with a right operand using an operator, e.g. odrl:spatial
  odrl:eq <country>. A LogicalConstraint combines constraints with exactly one of
  odrl:and, odrl:or, odrl:xone or odrl:andSequence. Operands and operators are open
  IRIs (odrlTerms), so ODRL profile terms validate.
type: object
properties:
  '@context':
    type: object
    description: JSON-LD namespace prefixes for ODRL properties.
    properties:
      odrl:
        const: http://www.w3.org/ns/odrl/2/
anyOf:
- $ref: '#/$defs/Constraint'
- $ref: '#/$defs/LogicalConstraint'
$defs:
  Constraint:
    type: object
    properties:
      '@id':
        description: Optional; needed when a LogicalConstraint refers to this constraint
          by reference.
        type: string
        format: iri
      '@type':
        type: array
        items:
          type: string
        contains:
          const: odrl:Constraint
      odrl:leftOperand:
        $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/odrlProperties/odrlTerms/schema.yaml#/$defs/LeftOperand
        x-jsonld-id: http://www.w3.org/ns/odrl/2/leftOperand
      odrl:operator:
        $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/odrlProperties/odrlTerms/schema.yaml#/$defs/Operator
        x-jsonld-id: http://www.w3.org/ns/odrl/2/operator
      odrl:rightOperand:
        description: A literal, a value object ({"@value", "@type"}) or an {@id} reference.
        x-jsonld-id: http://www.w3.org/ns/odrl/2/rightOperand
      odrl:rightOperandReference:
        description: An IRI whose dereferenced value is the right operand.
        $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifDataType/objectReference/schema.yaml
        x-jsonld-id: http://www.w3.org/ns/odrl/2/rightOperandReference
      odrl:dataType:
        description: Datatype of the right operand, e.g. xsd:decimal.
        $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifDataType/objectReference/schema.yaml
        x-jsonld-id: http://www.w3.org/ns/odrl/2/dataType
      odrl:unit:
        description: Unit of the right operand, e.g. a currency or unit of measure.
        $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifDataType/objectReference/schema.yaml
        x-jsonld-id: http://www.w3.org/ns/odrl/2/unit
      odrl:status:
        description: The current value of the left operand, for comparison with the
          right operand.
        x-jsonld-id: http://www.w3.org/ns/odrl/2/status
    required:
    - odrl:leftOperand
    - odrl:operator
    anyOf:
    - required:
      - odrl:rightOperand
    - required:
      - odrl:rightOperandReference
  LogicalConstraint:
    type: object
    properties:
      '@id':
        type: string
        format: iri
      '@type':
        type: array
        items:
          type: string
        contains:
          const: odrl:LogicalConstraint
      odrl:and:
        description: All of the constraints must be satisfied.
        $ref: '#/$defs/constraintList'
        x-jsonld-id: http://www.w3.org/ns/odrl/2/and
      odrl:or:
        description: At least one of the constraints must be satisfied.
        $ref: '#/$defs/constraintList'
        x-jsonld-id: http://www.w3.org/ns/odrl/2/or
      odrl:xone:
        description: Exactly one of the constraints must be satisfied.
        $ref: '#/$defs/constraintList'
        x-jsonld-id: http://www.w3.org/ns/odrl/2/xone
      odrl:andSequence:
        description: All of the constraints must be satisfied, in order.
        $ref: '#/$defs/constraintList'
        x-jsonld-id: http://www.w3.org/ns/odrl/2/andSequence
    oneOf:
    - required:
      - odrl:and
    - required:
      - odrl:or
    - required:
      - odrl:xone
    - required:
      - odrl:andSequence
  constraintList:
    description: 'The operand constraints, as an RDF list ({"@list": [...]}), each
      inline or an {@id} reference.'
    type: object
    properties:
      '@list':
        type: array
        minItems: 1
        items:
          anyOf:
          - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifDataType/objectReference/schema.yaml
          - $ref: '#/$defs/Constraint'
    required:
    - '@list'
x-jsonld-prefixes:
  odrl: http://www.w3.org/ns/odrl/2/
x-bblocks-metadata:
  itemIdentifier: cdif.bbr.metadata.odrlProperties.odrlConstraint
  register: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/register.json
  version: '0.1'
  dateOfLastChange: '2026-10-29'

```

Links to the schema:

* YAML version: [schema.yaml](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/odrlProperties/odrlConstraint/schema.json)
* JSON version: [schema.json](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/odrlProperties/odrlConstraint/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "odrl": "http://www.w3.org/ns/odrl/2/",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/odrlProperties/odrlConstraint/context.jsonld)

## Sources

* [W3C ODRL Information Model 2.2](https://www.w3.org/TR/odrl-model/)
* [W3C ODRL Vocabulary & Expression 2.2](https://www.w3.org/TR/odrl-vocab/)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/Cross-Domain-Interoperability-Framework/metadataBuildingBlocks](https://github.com/Cross-Domain-Interoperability-Framework/metadataBuildingBlocks)
* Path: `_sources/odrlProperties/odrlConstraint`

