
# ODRL Policy (Schema)

`cdif.bbr.metadata.odrlProperties.odrlPolicy` *v0.1*

W3C ODRL 2.2 Policy typed by one of its subclasses (Set, Offer, Agreement, Request, Ticket, Assertion, Privacy), with permissions, prohibitions and obligations, policy-level target and parties, odrl:profile, odrl:inheritFrom and odrl:conflict. Checks each subclass's requirements from the ODRL vocabulary (e.g. an Agreement needs an assigner and an assignee, a Ticket no assignee), met at policy level or on every rule. Uses building blocks: odrlRule, odrlTerms (odrlProperties), objectReference (cdifDataType).

[*Status*](http://www.opengis.net/def/status): Under development

## Description

## ODRL Policy

W3C ODRL 2.2 Policy typed by one of its subclasses (Set, Offer, Agreement, Request, Ticket, Assertion, Privacy), with permissions, prohibitions and obligations, policy-level target and parties, odrl:profile, odrl:inheritFrom and odrl:conflict. Checks each subclass's requirements from the ODRL vocabulary (e.g. an Agreement needs an assigner and an assignee, a Ticket no assignee), met at policy level or on every rule.

Generic W3C ODRL; CDIF-specific rules belong in profile blocks such as [odrlOffer](../odrlOffer/).

### Dependencies

- [odrlRule](../odrlRule/)
- [odrlTerms](../odrlTerms/)
- [objectReference](../../cdifDataType/objectReference/)

## Examples

### ODRL Agreement
An Agreement granting one user permission to use a distribution and prohibiting its distribution; target and parties are given once at policy level, the assigner as an inline schema:Organization.
#### json
```json
{
  "@context": {
    "odrl": "http://www.w3.org/ns/odrl/2/",
    "schema": "http://schema.org/"
  },
  "@type": [
    "odrl:Agreement"
  ],
  "@id": "https://example.org/odrlagreement/d91d4663-f9bd-4bd5-8a81-c331e19bf987",
  "odrl:conflict": {
    "@id": "odrl:prohibit"
  },
  "odrl:target": {
    "@id": "https://example.org/dataset/3936/distribution/csv"
  },
  "odrl:assigner": {
    "@type": [
      "schema:Organization"
    ],
    "@id": "https://example.org/repository",
    "schema:name": "Example Data Repository"
  },
  "odrl:assignee": {
    "@id": "https://example.org/user/1"
  },
  "odrl:permission": [
    {
      "odrl:action": {
        "@id": "odrl:use"
      }
    }
  ],
  "odrl:prohibition": [
    {
      "odrl:action": {
        "@id": "odrl:distribute"
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
      "schema": "http://schema.org/"
    },
    "https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/odrlProperties/odrlPolicy/context.jsonld",
    {
      "odrl": "http://www.w3.org/ns/odrl/2/",
      "schema": "http://schema.org/"
    }
  ],
  "@type": [
    "odrl:Agreement"
  ],
  "@id": "https://example.org/odrlagreement/d91d4663-f9bd-4bd5-8a81-c331e19bf987",
  "odrl:conflict": {
    "@id": "odrl:prohibit"
  },
  "odrl:target": {
    "@id": "https://example.org/dataset/3936/distribution/csv"
  },
  "odrl:assigner": {
    "@type": [
      "schema:Organization"
    ],
    "@id": "https://example.org/repository",
    "schema:name": "Example Data Repository"
  },
  "odrl:assignee": {
    "@id": "https://example.org/user/1"
  },
  "odrl:permission": [
    {
      "odrl:action": {
        "@id": "odrl:use"
      }
    }
  ],
  "odrl:prohibition": [
    {
      "odrl:action": {
        "@id": "odrl:distribute"
      }
    }
  ]
}
```

#### ttl
```ttl
@prefix odrl: <http://www.w3.org/ns/odrl/2/> .
@prefix schema1: <http://schema.org/> .

<https://example.org/odrlagreement/d91d4663-f9bd-4bd5-8a81-c331e19bf987> a odrl:Agreement ;
    odrl:assignee <https://example.org/user/1> ;
    odrl:assigner <https://example.org/repository> ;
    odrl:conflict odrl:prohibit ;
    odrl:permission [ odrl:action odrl:use ] ;
    odrl:prohibition [ odrl:action odrl:distribute ] ;
    odrl:target <https://example.org/dataset/3936/distribution/csv> .

<https://example.org/repository> a schema1:Organization ;
    schema1:name "Example Data Repository" .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: ODRL Policy
description: 'An ODRL 2.2 Policy (https://www.w3.org/TR/odrl-model/#policy): a group
  of permissions, prohibitions and obligations, typed by one of its subclasses: Set
  (the default), Offer, Agreement, Request, Ticket, Assertion or Privacy. A target
  or party given at policy level applies to every rule (https://www.w3.org/TR/odrl-model/#composition),
  so each subclass requirement below is met by the policy-level property or by that
  property on every rule concerned. The subclass requirements are those stated in
  the ODRL vocabulary (https://www.w3.org/ns/odrl/2/ODRL22.ttl); requirements on meaning
  (e.g. an Offer grants no privileges to an assignee) cannot be checked by a schema.'
type: object
properties:
  '@context':
    type: object
    description: JSON-LD namespace prefixes for ODRL properties.
    properties:
      odrl:
        const: http://www.w3.org/ns/odrl/2/
  '@id':
    description: Globally unique IRI for the policy (ODRL uid).
    type: string
    format: iri
  '@type':
    type: array
    items:
      type: string
    contains:
      enum:
      - odrl:Policy
      - odrl:Set
      - odrl:Offer
      - odrl:Agreement
      - odrl:Request
      - odrl:Ticket
      - odrl:Assertion
      - odrl:Privacy
  odrl:profile:
    description: ODRL profiles the policy conforms to.
    anyOf:
    - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifDataType/objectReference/schema.yaml
    - type: array
      items:
        $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifDataType/objectReference/schema.yaml
    x-jsonld-id: http://www.w3.org/ns/odrl/2/profile
  odrl:inheritFrom:
    description: Parent policies whose rules this policy inherits.
    anyOf:
    - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifDataType/objectReference/schema.yaml
    - type: array
      items:
        $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifDataType/objectReference/schema.yaml
    x-jsonld-id: http://www.w3.org/ns/odrl/2/inheritFrom
  odrl:conflict:
    $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/odrlProperties/odrlTerms/schema.yaml#/$defs/ConflictTerm
    x-jsonld-id: http://www.w3.org/ns/odrl/2/conflict
  odrl:target:
    $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/odrlProperties/odrlRule/schema.yaml#/$defs/Target
    x-jsonld-id: http://www.w3.org/ns/odrl/2/target
  odrl:assigner:
    $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/odrlProperties/odrlRule/schema.yaml#/$defs/PartyRef
    x-jsonld-id: http://www.w3.org/ns/odrl/2/assigner
  odrl:assignee:
    $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/odrlProperties/odrlRule/schema.yaml#/$defs/PartyRef
    x-jsonld-id: http://www.w3.org/ns/odrl/2/assignee
  odrl:permission:
    type: array
    items:
      $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/odrlProperties/odrlRule/schema.yaml#/$defs/Permission
    x-jsonld-id: http://www.w3.org/ns/odrl/2/permission
  odrl:prohibition:
    type: array
    items:
      $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/odrlProperties/odrlRule/schema.yaml#/$defs/Prohibition
    x-jsonld-id: http://www.w3.org/ns/odrl/2/prohibition
  odrl:obligation:
    type: array
    items:
      $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/odrlProperties/odrlRule/schema.yaml#/$defs/Duty
    x-jsonld-id: http://www.w3.org/ns/odrl/2/obligation
required:
- '@type'
- '@id'
anyOf:
- required:
  - odrl:permission
- required:
  - odrl:prohibition
- required:
  - odrl:obligation
allOf:
- if:
    $ref: '#/$defs/isSet'
  then:
    allOf:
    - $ref: '#/$defs/hasTarget'
- if:
    $ref: '#/$defs/isOffer'
  then:
    allOf:
    - $ref: '#/$defs/hasPermissionOrProhibition'
    - $ref: '#/$defs/hasAssigner'
- if:
    $ref: '#/$defs/isAgreement'
  then:
    allOf:
    - $ref: '#/$defs/hasPermissionOrProhibition'
    - $ref: '#/$defs/hasAssigner'
    - $ref: '#/$defs/hasAssignee'
- if:
    $ref: '#/$defs/isRequest'
  then:
    allOf:
    - $ref: '#/$defs/hasPermissionOrProhibition'
    - $ref: '#/$defs/hasTarget'
    - $ref: '#/$defs/hasAssignee'
- if:
    $ref: '#/$defs/isTicket'
  then:
    allOf:
    - $ref: '#/$defs/hasPermissionOrProhibition'
    - $ref: '#/$defs/hasTarget'
    - $ref: '#/$defs/noAssignee'
- if:
    $ref: '#/$defs/isAssertion'
  then:
    allOf:
    - $ref: '#/$defs/hasPermissionOrProhibition'
    - $ref: '#/$defs/hasTarget'
    - anyOf:
      - $ref: '#/$defs/hasAssigner'
      - $ref: '#/$defs/hasAssignee'
- if:
    $ref: '#/$defs/isPrivacy'
  then:
    allOf:
    - $ref: '#/$defs/hasPermissionOrProhibition'
    - $ref: '#/$defs/hasTarget'
    - $ref: '#/$defs/hasAssigner'
    - $ref: '#/$defs/hasAssignee'
    - description: The rules must include a duty describing obligations on the use
        of personal information.
      anyOf:
      - required:
        - odrl:obligation
      - properties:
          odrl:permission:
            contains:
              required:
              - odrl:duty
            x-jsonld-id: http://www.w3.org/ns/odrl/2/permission
        required:
        - odrl:permission
$defs:
  isSet:
    properties:
      '@type':
        contains:
          const: odrl:Set
    required:
    - '@type'
  isOffer:
    properties:
      '@type':
        contains:
          const: odrl:Offer
    required:
    - '@type'
  isAgreement:
    properties:
      '@type':
        contains:
          const: odrl:Agreement
    required:
    - '@type'
  isRequest:
    properties:
      '@type':
        contains:
          const: odrl:Request
    required:
    - '@type'
  isTicket:
    properties:
      '@type':
        contains:
          const: odrl:Ticket
    required:
    - '@type'
  isAssertion:
    properties:
      '@type':
        contains:
          const: odrl:Assertion
    required:
    - '@type'
  isPrivacy:
    properties:
      '@type':
        contains:
          const: odrl:Privacy
    required:
    - '@type'
  hasPermissionOrProhibition:
    anyOf:
    - required:
      - odrl:permission
    - required:
      - odrl:prohibition
  hasTarget:
    description: A target at policy level, or on every rule.
    anyOf:
    - required:
      - odrl:target
    - properties:
        odrl:permission:
          items:
            required:
            - odrl:target
          x-jsonld-id: http://www.w3.org/ns/odrl/2/permission
        odrl:prohibition:
          items:
            required:
            - odrl:target
          x-jsonld-id: http://www.w3.org/ns/odrl/2/prohibition
        odrl:obligation:
          items:
            required:
            - odrl:target
          x-jsonld-id: http://www.w3.org/ns/odrl/2/obligation
  hasAssigner:
    description: An assigner at policy level, or on every permission and prohibition.
    anyOf:
    - required:
      - odrl:assigner
    - properties:
        odrl:permission:
          items:
            required:
            - odrl:assigner
          x-jsonld-id: http://www.w3.org/ns/odrl/2/permission
        odrl:prohibition:
          items:
            required:
            - odrl:assigner
          x-jsonld-id: http://www.w3.org/ns/odrl/2/prohibition
  hasAssignee:
    description: An assignee at policy level, or on every permission and prohibition.
    anyOf:
    - required:
      - odrl:assignee
    - properties:
        odrl:permission:
          items:
            required:
            - odrl:assignee
          x-jsonld-id: http://www.w3.org/ns/odrl/2/permission
        odrl:prohibition:
          items:
            required:
            - odrl:assignee
          x-jsonld-id: http://www.w3.org/ns/odrl/2/prohibition
  noAssignee:
    description: A Ticket names no assignee; it is granted to whoever holds it.
    not:
      anyOf:
      - required:
        - odrl:assignee
      - properties:
          odrl:permission:
            contains:
              required:
              - odrl:assignee
        required:
        - odrl:permission
      - properties:
          odrl:prohibition:
            contains:
              required:
              - odrl:assignee
        required:
        - odrl:prohibition
x-jsonld-prefixes:
  odrl: http://www.w3.org/ns/odrl/2/
  schema: http://schema.org/
x-bblocks-metadata:
  itemIdentifier: cdif.bbr.metadata.odrlProperties.odrlPolicy
  register: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/register.json
  version: '0.1'
  dateOfLastChange: '2026-10-28'

```

Links to the schema:

* YAML version: [schema.yaml](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/odrlProperties/odrlPolicy/schema.json)
* JSON version: [schema.json](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/odrlProperties/odrlPolicy/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "odrl": "http://www.w3.org/ns/odrl/2/",
    "schema": "http://schema.org/",
    "skos": "http://www.w3.org/2004/02/skos/core#",
    "rdf": "http://www.w3.org/1999/02/22-rdf-syntax-ns#",
    "xsd": "http://www.w3.org/2001/XMLSchema#",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/odrlProperties/odrlPolicy/context.jsonld)

## Sources

* [W3C ODRL Information Model 2.2](https://www.w3.org/TR/odrl-model/)
* [W3C ODRL Vocabulary & Expression 2.2](https://www.w3.org/TR/odrl-vocab/)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/Cross-Domain-Interoperability-Framework/metadataBuildingBlocks](https://github.com/Cross-Domain-Interoperability-Framework/metadataBuildingBlocks)
* Path: `_sources/odrlProperties/odrlPolicy`

