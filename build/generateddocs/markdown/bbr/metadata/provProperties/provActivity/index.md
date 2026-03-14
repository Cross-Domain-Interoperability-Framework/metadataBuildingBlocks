
# PROV-O Provenance Activity (Schema)

`cdif.bbr.metadata.provProperties.provActivity` *v0.1*

PROV-O native provenance activity for CDIF metadata. Uses W3C PROV-O vocabulary for provenance relationships (used, generated, wasAssociatedWith, wasInformedBy, temporal bounds, location) with schema.org fallbacks for properties without PROV equivalents (name, description, methodology, status). Instruments are nested within prov:used items via schema:instrument sub-key, referencing the generic instrument building block. Defines properties: @type, schema:name, schema:description, prov:generated, prov:wasAssociatedWith, prov:wasInformedBy, prov:startedAtTime, prov:endedAtTime, prov:atLocation, prov:wasStartedBy, prov:wasEndedBy, schema:actionStatus, schema:actionProcess, schema:error. Uses building blocks: generatedBy (provProperties), person (schemaorgProperties), organization (schemaorgProperties), agentInRole (schemaorgProperties), instrument (schemaorgProperties), definedTerm (schemaorgProperties), labeledLink (schemaorgProperties), spatialExtent (schemaorgProperties).

[*Status*](http://www.opengis.net/def/status): Under development

## Description

## PROV-O Provenance Activity

PROV-O native provenance activity for CDIF metadata. Extends the minimal [generatedBy](../generatedBy/) with W3C PROV-O vocabulary for comprehensive provenance (used, generated, wasAssociatedWith, wasInformedBy, temporal bounds, location) with schema.org fallbacks for name, description, methodology, and status. Instruments are nested in prov:used via schema:instrument sub-key.

### Defined properties

- **@type** — must include prov:Activity
- **schema:name** — human-readable name for the activity
- **schema:description** — text description of what this activity did
- **prov:generated** — entities produced by this activity
- **prov:wasAssociatedWith** — agents responsible for this activity
- **prov:wasInformedBy** — other activities that communicated information to this one
- **prov:startedAtTime** — ISO 8601 date-time when the activity started
- **prov:endedAtTime** — ISO 8601 date-time when the activity ended
- **prov:atLocation** — location where the activity occurred
- **prov:wasStartedBy** — entity that triggered the start of this activity
- **prov:wasEndedBy** — entity that triggered the end of this activity
- **schema:actionStatus** — status of this activity (Completed, Active, Potential, Failed)
- **schema:actionProcess** — methodology or protocol for this activity
- **schema:error** — error description for failed activities

### Dependencies

- [generatedBy](../generatedBy/) — base provenance activity
- [person](../../schemaorgProperties/person/) — person agent
- [organization](../../schemaorgProperties/organization/) — organization agent
- [agentInRole](../../schemaorgProperties/agentInRole/) — agent with qualified role
- [instrument](../../schemaorgProperties/instrument/) — generic instrument
- [definedTerm](../../schemaorgProperties/definedTerm/) — controlled vocabulary term
- [labeledLink](../../schemaorgProperties/labeledLink/) — link with label and description
- [spatialExtent](../../schemaorgProperties/spatialExtent/) — spatial location

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: PROV-O Provenance Activity
description: PROV-O native provenance activity building block for CDIF. Extends the
  minimal prov:Activity (generatedBy) with W3C PROV-O properties for comprehensive
  provenance documentation. Uses schema.org fallbacks only where PROV-O has no equivalent
  (name, description, instrument, methodology, status).
type: object
allOf:
- $ref: https://usgin.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/provProperties/generatedBy/schema.yaml
- type: object
  properties:
    '@type':
      type: array
      items:
        type: string
      minItems: 1
      contains:
        const: prov:Activity
      description: Must include prov:Activity. Unlike cdifProvActivity, does not require
        schema:Action dual typing.
    schema:name:
      type: string
      description: Human-readable name for the activity (schema.org fallback -- PROV-O
        has no name property)
    schema:description:
      type: string
      description: Text description of what this activity did (schema.org fallback
        -- PROV-O has no description property)
    prov:generated:
      description: Entities produced by this activity (inverse of prov:wasGeneratedBy)
      type: array
      items:
        anyOf:
        - type: string
        - type: object
          properties:
            '@id':
              type: string
              description: reference to an entity produced by this activity
    prov:wasAssociatedWith:
      description: Agents responsible for this activity (PROV-O native -- maps to
        schema:agent in cdifProvActivity)
      type: array
      items:
        anyOf:
        - $ref: '#/$defs/Person'
        - $ref: '#/$defs/Organization'
        - $ref: '#/$defs/AgentInRole'
        - type: string
        - type: object
          properties:
            '@id':
              type: string
              description: reference to an agent defined elsewhere
    prov:wasInformedBy:
      description: Other activities that communicated information to this one (PROV-O
        activity-to-activity chain -- maps to schema:object in cdifProvActivity)
      type: array
      items:
        anyOf:
        - type: object
          properties:
            '@id':
              type: string
              description: reference to a prior activity
        - type: string
    prov:startedAtTime:
      type: string
      description: ISO8601 date-time when the activity started (PROV-O native -- maps
        to schema:startTime in cdifProvActivity)
    prov:endedAtTime:
      type: string
      description: ISO8601 date-time when the activity ended (PROV-O native -- maps
        to schema:endTime in cdifProvActivity)
    prov:atLocation:
      description: Location where the activity occurred (PROV-O expanded term -- maps
        to schema:location in cdifProvActivity)
      anyOf:
      - $ref: '#/$defs/SpatialExtent'
      - type: string
      - type: object
        properties:
          '@id':
            type: string
            description: reference to a place defined elsewhere
    prov:wasStartedBy:
      description: Entity that triggered the start of this activity (PROV-O expanded
        term)
      anyOf:
      - type: string
      - type: object
        properties:
          '@id':
            type: string
            description: reference to a triggering entity
    prov:wasEndedBy:
      description: Entity that triggered the end of this activity (PROV-O expanded
        term)
      anyOf:
      - type: string
      - type: object
        properties:
          '@id':
            type: string
            description: reference to an entity that ended this activity
    schema:actionStatus:
      type: string
      description: Status of this activity (schema.org fallback -- no PROV-O equivalent)
      enum:
      - schema:CompletedActionStatus
      - schema:ActiveActionStatus
      - schema:PotentialActionStatus
      - schema:FailedActionStatus
    schema:actionProcess:
      description: Methodology or protocol for this activity (schema.org fallback
        -- PROV-O has prov:hadPlan only inside qualified Association)
      anyOf:
      - $ref: '#/$defs/HowTo'
      - type: string
      - type: object
        properties:
          '@id':
            type: string
            description: reference to a methodology defined elsewhere
    schema:error:
      type: string
      description: Error description for failed activities (schema.org fallback --
        no PROV-O equivalent)
$defs:
  Person:
    $ref: https://usgin.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/person/schema.yaml
  Organization:
    $ref: https://usgin.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/organization/schema.yaml
  AgentInRole:
    $ref: https://usgin.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/agentInRole/schema.yaml
  Instrument:
    $ref: https://usgin.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/instrument/schema.yaml
  DefinedTerm:
    $ref: https://usgin.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/definedTerm/schema.yaml
  LabeledLink:
    $ref: https://usgin.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/labeledLink/schema.yaml
  SpatialExtent:
    $ref: https://usgin.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/spatialExtent/schema.yaml
  HowTo:
    type: object
    description: A methodology or protocol described as a HowTo with optional steps
    properties:
      '@type':
        anyOf:
        - type: string
          const: schema:HowTo
        - type: array
          items:
            type: string
          contains:
            const: schema:HowTo
      '@id':
        type: string
      schema:name:
        type: string
        description: Name of the methodology or protocol
      schema:description:
        type: string
        description: Description of the methodology
      schema:url:
        type: string
        format: uri
        description: URL to a published methodology or protocol document
      schema:step:
        type: array
        description: Ordered steps in this methodology
        items:
          $ref: '#/$defs/HowToStep'
    required:
    - '@type'
    anyOf:
    - required:
      - schema:name
    - required:
      - schema:url
  HowToStep:
    type: object
    description: A single step in a HowTo methodology
    properties:
      '@type':
        anyOf:
        - type: string
          const: schema:HowToStep
        - type: array
          items:
            type: string
          contains:
            const: schema:HowToStep
      schema:name:
        type: string
        description: Name of this step
      schema:description:
        type: string
        description: Description of what this step involves
      schema:url:
        type: string
        format: uri
        description: URL to documentation for this step
      schema:position:
        type: integer
        description: Ordinal position of this step
    required:
    - '@type'
    - schema:name
x-jsonld-prefixes:
  schema: http://schema.org/
  prov: http://www.w3.org/ns/prov#

```

Links to the schema:

* YAML version: [schema.yaml](https://usgin.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/provProperties/provActivity/schema.json)
* JSON version: [schema.json](https://usgin.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/provProperties/provActivity/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "schema": "http://schema.org/",
    "prov": "http://www.w3.org/ns/prov#",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://usgin.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/provProperties/provActivity/context.jsonld)

## Sources

* [W3C PROV-O: The PROV Ontology](https://www.w3.org/TR/prov-o/)
* [W3C PROV-DM: The PROV Data Model](https://www.w3.org/TR/prov-dm/)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/usgin/metadataBuildingBlocks](https://github.com/usgin/metadataBuildingBlocks)
* Path: `_sources/provProperties/provActivity`

