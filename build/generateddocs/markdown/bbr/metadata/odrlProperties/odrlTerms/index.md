
# ODRL Terms (Schema)

`cdif.bbr.metadata.odrlProperties.odrlTerms` *v0.1*

Type library of references to W3C ODRL 2.2 vocabulary terms: Action, LeftOperand, Operator, RightOperand and ConflictTerm, generated from ODRL22.ttl excluding deprecated terms. Actions and operands are open IRIs (ODRL profiles extend them), with the core terms listed as examples; conflict terms are closed.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

## ODRL Terms

Type library of `{"@id": ...}` references to W3C ODRL 2.2 vocabulary terms, generated from [ODRL22.ttl](https://www.w3.org/ns/odrl/2/ODRL22.ttl) without deprecated terms:

- **Action**: 42 terms (open: any IRI accepted)
- **LeftOperand**: 32 terms (open: any IRI accepted)
- **Operator**: 12 terms (open: any IRI accepted)
- **RightOperand**: 1 terms (open: any IRI accepted)
- **ConflictTerm**: 3 terms (closed)

Definitions only; it has no example of its own.

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: ODRL Terms
description: 'Type library of references to ODRL 2.2 vocabulary terms (https://www.w3.org/TR/odrl-vocab/):
  actions, left operands, operators, right operands and conflict strategies. Generated
  from https://www.w3.org/ns/odrl/2/ODRL22.ttl, excluding terms marked deprecated.
  Actions and operands are open, because ODRL profiles extend them; conflict terms
  are closed. Each term is an {"@id": ...} reference, compact (odrl:use) or full IRI.'
$defs:
  Action:
    description: 'Reference to an ODRL Action action. Open: any IRI is accepted, so
      ODRL profile terms (e.g. cdifa1:) validate; the examples list the 42 non-deprecated
      ODRL 2.2 Action terms.'
    type: object
    properties:
      '@id':
        type: string
        examples:
        - odrl:acceptTracking
        - odrl:aggregate
        - odrl:annotate
        - odrl:anonymize
        - odrl:archive
        - odrl:attribute
        - odrl:compensate
        - odrl:concurrentUse
        - odrl:delete
        - odrl:derive
        - odrl:digitize
        - odrl:display
        - odrl:distribute
        - odrl:ensureExclusivity
        - odrl:execute
        - odrl:extract
        - odrl:give
        - odrl:grantUse
        - odrl:include
        - odrl:index
        - odrl:inform
        - odrl:install
        - odrl:modify
        - odrl:move
        - odrl:nextPolicy
        - odrl:obtainConsent
        - odrl:play
        - odrl:present
        - odrl:print
        - odrl:read
        - odrl:reproduce
        - odrl:reviewPolicy
        - odrl:sell
        - odrl:stream
        - odrl:synchronize
        - odrl:textToSpeech
        - odrl:transfer
        - odrl:transform
        - odrl:translate
        - odrl:uninstall
        - odrl:use
        - odrl:watermark
    required:
    - '@id'
    additionalProperties: false
  LeftOperand:
    description: 'Reference to an ODRL LeftOperand left operand. Open: any IRI is
      accepted, so ODRL profile terms (e.g. cdifa1:) validate; the examples list the
      32 non-deprecated ODRL 2.2 LeftOperand terms.'
    type: object
    properties:
      '@id':
        type: string
        examples:
        - odrl:absolutePosition
        - odrl:absoluteSize
        - odrl:absoluteSpatialPosition
        - odrl:absoluteTemporalPosition
        - odrl:count
        - odrl:dateTime
        - odrl:delayPeriod
        - odrl:deliveryChannel
        - odrl:elapsedTime
        - odrl:event
        - odrl:fileFormat
        - odrl:industry
        - odrl:language
        - odrl:media
        - odrl:meteredTime
        - odrl:payAmount
        - odrl:percentage
        - odrl:product
        - odrl:purpose
        - odrl:recipient
        - odrl:relativePosition
        - odrl:relativeSize
        - odrl:relativeSpatialPosition
        - odrl:relativeTemporalPosition
        - odrl:resolution
        - odrl:spatial
        - odrl:spatialCoordinates
        - odrl:systemDevice
        - odrl:timeInterval
        - odrl:unitOfCount
        - odrl:version
        - odrl:virtualLocation
    required:
    - '@id'
    additionalProperties: false
  Operator:
    description: 'Reference to an ODRL Operator operator. Open: any IRI is accepted,
      so ODRL profile terms (e.g. cdifa1:) validate; the examples list the 12 non-deprecated
      ODRL 2.2 Operator terms.'
    type: object
    properties:
      '@id':
        type: string
        examples:
        - odrl:eq
        - odrl:gt
        - odrl:gteq
        - odrl:hasPart
        - odrl:isA
        - odrl:isAllOf
        - odrl:isAnyOf
        - odrl:isNoneOf
        - odrl:isPartOf
        - odrl:lt
        - odrl:lteq
        - odrl:neq
    required:
    - '@id'
    additionalProperties: false
  RightOperand:
    description: 'Reference to an ODRL RightOperand right operand. Open: any IRI is
      accepted, so ODRL profile terms (e.g. cdifa1:) validate; the examples list the
      1 non-deprecated ODRL 2.2 RightOperand terms. Most right operands are literals
      or value objects, not terms; this is for the few that are IRIs.'
    type: object
    properties:
      '@id':
        type: string
        examples:
        - odrl:policyUsage
    required:
    - '@id'
    additionalProperties: false
  ConflictTerm:
    description: 'Strategy for resolving conflicts between permissions and prohibitions
      (odrl:conflict). Closed: ODRL defines exactly these three.'
    type: object
    properties:
      '@id':
        enum:
        - odrl:invalid
        - http://www.w3.org/ns/odrl/2/invalid
        - odrl:perm
        - http://www.w3.org/ns/odrl/2/perm
        - odrl:prohibit
        - http://www.w3.org/ns/odrl/2/prohibit
    required:
    - '@id'
    additionalProperties: false
x-jsonld-prefixes:
  odrl: http://www.w3.org/ns/odrl/2/
x-bblocks-metadata:
  itemIdentifier: cdif.bbr.metadata.odrlProperties.odrlTerms
  register: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/register.json
  version: '0.1'
  dateOfLastChange: '2026-10-29'

```

Links to the schema:

* YAML version: [schema.yaml](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/odrlProperties/odrlTerms/schema.json)
* JSON version: [schema.json](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/odrlProperties/odrlTerms/schema.yaml)


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
[context.jsonld](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/odrlProperties/odrlTerms/context.jsonld)

## Sources

* [W3C ODRL Information Model 2.2](https://www.w3.org/TR/odrl-model/)
* [W3C ODRL Vocabulary & Expression 2.2](https://www.w3.org/TR/odrl-vocab/)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/Cross-Domain-Interoperability-Framework/metadataBuildingBlocks](https://github.com/Cross-Domain-Interoperability-Framework/metadataBuildingBlocks)
* Path: `_sources/odrlProperties/odrlTerms`

