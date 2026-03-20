
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

## Examples

### Example PROV-O Activity
Example PROV-O provenance activity with associations, inputs, outputs, and methodology.
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "prov": "http://www.w3.org/ns/prov#",
    "ex": "https://example.org/"
  },
  "@id": "ex:activity-soil-chem-analysis",
  "@type": [
    "prov:Activity"
  ],
  "schema:name": "Soil Chemistry Analysis - Great Basin Transect 2025",
  "schema:description": "Major and trace element analysis of soil samples collected along a 200 km transect across the Great Basin, using ICP-MS and XRF spectrometry with certified reference materials.",
  "prov:used": [
    {
      "@id": "http://example.org/inst/TF_RQICP-MS"
    },
    "https://vocab.nerc.ac.uk/collection/L05/current/LAB02",
    "Soil core samples collected June 2025, sites GB-001 through GB-045",
    {
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:name": "EPA Method 6200 - XRF Analysis of Soils",
      "schema:url": "https://www.epa.gov/hw-sw846/sw-846-test-method-6200-field-portable-x-ray-fluorescence-spectrometry-determination"
    }
  ],
  "prov:generated": [
    {
      "@id": "ex:dataset-soil-chem-gb-2025"
    }
  ],
  "prov:wasAssociatedWith": [
    {
      "@type": [
        "schema:Person"
      ],
      "schema:name": "Dr. Maria Chen",
      "schema:identifier": {
        "@type": [
          "schema:PropertyValue"
        ],
        "schema:propertyID": "https://registry.identifiers.org/registry/orcid",
        "schema:value": "0000-0002-8765-4321",
        "schema:url": "https://orcid.org/0000-0002-8765-4321"
      },
      "schema:contactPoint": {
        "@id": "mailto:maria.chen@unr.edu"
      }
    }
  ],
  "prov:wasInformedBy": [
    {
      "@id": "ex:activity-sample-collection"
    }
  ],
  "prov:startedAtTime": "2025-07-15T08:00:00Z",
  "prov:endedAtTime": "2025-09-30T17:00:00Z",
  "prov:atLocation": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "Nevada Bureau of Mines and Geology Analytical Lab",
    "schema:address": "University of Nevada, Reno, 1664 N. Virginia Street, Reno, NV 89557",
    "schema:url": "https://www.unr.edu/nbmg"
  },
  "schema:actionStatus": "schema:CompletedActionStatus",
  "schema:actionProcess": {
    "@type": [
      "schema:HowTo"
    ],
    "schema:name": "EPA 6200 / ICP-MS Soil Geochemistry Protocol",
    "schema:description": "Combined XRF screening and ICP-MS confirmatory analysis for major and trace elements in soil matrices.",
    "schema:step": [
      {
        "@type": [
          "schema:HowToStep"
        ],
        "schema:name": "Sample preparation and acid digestion",
        "schema:description": "Homogenize dried samples, split 0.5 g aliquots, digest with HNO3-HCl-HF mixture at 190 C in closed vessels.",
        "schema:position": 1
      },
      {
        "@type": [
          "schema:HowToStep"
        ],
        "schema:name": "ICP-MS measurement and calibration",
        "schema:description": "Analyze digested solutions by ICP-MS using external calibration with NIST SRM 2710a and 2711a as quality control standards.",
        "schema:position": 2
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
      "prov": "http://www.w3.org/ns/prov#",
      "schema": "http://schema.org/"
    },
    "https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/provProperties/provActivity/context.jsonld",
    {
      "schema": "http://schema.org/",
      "prov": "http://www.w3.org/ns/prov#",
      "ex": "https://example.org/"
    }
  ],
  "@id": "ex:activity-soil-chem-analysis",
  "@type": [
    "prov:Activity"
  ],
  "schema:name": "Soil Chemistry Analysis - Great Basin Transect 2025",
  "schema:description": "Major and trace element analysis of soil samples collected along a 200 km transect across the Great Basin, using ICP-MS and XRF spectrometry with certified reference materials.",
  "prov:used": [
    {
      "@id": "http://example.org/inst/TF_RQICP-MS"
    },
    "https://vocab.nerc.ac.uk/collection/L05/current/LAB02",
    "Soil core samples collected June 2025, sites GB-001 through GB-045",
    {
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:name": "EPA Method 6200 - XRF Analysis of Soils",
      "schema:url": "https://www.epa.gov/hw-sw846/sw-846-test-method-6200-field-portable-x-ray-fluorescence-spectrometry-determination"
    }
  ],
  "prov:generated": [
    {
      "@id": "ex:dataset-soil-chem-gb-2025"
    }
  ],
  "prov:wasAssociatedWith": [
    {
      "@type": [
        "schema:Person"
      ],
      "schema:name": "Dr. Maria Chen",
      "schema:identifier": {
        "@type": [
          "schema:PropertyValue"
        ],
        "schema:propertyID": "https://registry.identifiers.org/registry/orcid",
        "schema:value": "0000-0002-8765-4321",
        "schema:url": "https://orcid.org/0000-0002-8765-4321"
      },
      "schema:contactPoint": {
        "@id": "mailto:maria.chen@unr.edu"
      }
    }
  ],
  "prov:wasInformedBy": [
    {
      "@id": "ex:activity-sample-collection"
    }
  ],
  "prov:startedAtTime": "2025-07-15T08:00:00Z",
  "prov:endedAtTime": "2025-09-30T17:00:00Z",
  "prov:atLocation": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "Nevada Bureau of Mines and Geology Analytical Lab",
    "schema:address": "University of Nevada, Reno, 1664 N. Virginia Street, Reno, NV 89557",
    "schema:url": "https://www.unr.edu/nbmg"
  },
  "schema:actionStatus": "schema:CompletedActionStatus",
  "schema:actionProcess": {
    "@type": [
      "schema:HowTo"
    ],
    "schema:name": "EPA 6200 / ICP-MS Soil Geochemistry Protocol",
    "schema:description": "Combined XRF screening and ICP-MS confirmatory analysis for major and trace elements in soil matrices.",
    "schema:step": [
      {
        "@type": [
          "schema:HowToStep"
        ],
        "schema:name": "Sample preparation and acid digestion",
        "schema:description": "Homogenize dried samples, split 0.5 g aliquots, digest with HNO3-HCl-HF mixture at 190 C in closed vessels.",
        "schema:position": 1
      },
      {
        "@type": [
          "schema:HowToStep"
        ],
        "schema:name": "ICP-MS measurement and calibration",
        "schema:description": "Analyze digested solutions by ICP-MS using external calibration with NIST SRM 2710a and 2711a as quality control standards.",
        "schema:position": 2
      }
    ]
  }
}
```

#### ttl
```ttl
@prefix ex: <https://example.org/> .
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ex:activity-soil-chem-analysis a prov:Activity ;
    schema1:actionProcess [ a schema1:HowTo ;
            schema1:description "Combined XRF screening and ICP-MS confirmatory analysis for major and trace elements in soil matrices." ;
            schema1:name "EPA 6200 / ICP-MS Soil Geochemistry Protocol" ;
            schema1:step [ a schema1:HowToStep ;
                    schema1:description "Homogenize dried samples, split 0.5 g aliquots, digest with HNO3-HCl-HF mixture at 190 C in closed vessels." ;
                    schema1:name "Sample preparation and acid digestion" ;
                    schema1:position 1 ],
                [ a schema1:HowToStep ;
                    schema1:description "Analyze digested solutions by ICP-MS using external calibration with NIST SRM 2710a and 2711a as quality control standards." ;
                    schema1:name "ICP-MS measurement and calibration" ;
                    schema1:position 2 ] ] ;
    schema1:actionStatus "schema:CompletedActionStatus" ;
    schema1:description "Major and trace element analysis of soil samples collected along a 200 km transect across the Great Basin, using ICP-MS and XRF spectrometry with certified reference materials." ;
    schema1:name "Soil Chemistry Analysis - Great Basin Transect 2025" ;
    prov:atLocation [ a schema1:Place ;
            schema1:address "University of Nevada, Reno, 1664 N. Virginia Street, Reno, NV 89557" ;
            schema1:name "Nevada Bureau of Mines and Geology Analytical Lab" ;
            schema1:url "https://www.unr.edu/nbmg" ] ;
    prov:endedAtTime "2025-09-30T17:00:00Z" ;
    prov:generated ex:dataset-soil-chem-gb-2025 ;
    prov:startedAtTime "2025-07-15T08:00:00Z" ;
    prov:used [ a schema1:CreativeWork ;
            schema1:name "EPA Method 6200 - XRF Analysis of Soils" ;
            schema1:url "https://www.epa.gov/hw-sw846/sw-846-test-method-6200-field-portable-x-ray-fluorescence-spectrometry-determination" ],
        <http://example.org/inst/TF_RQICP-MS>,
        "Soil core samples collected June 2025, sites GB-001 through GB-045",
        "https://vocab.nerc.ac.uk/collection/L05/current/LAB02" ;
    prov:wasAssociatedWith [ a schema1:Person ;
            schema1:contactPoint <mailto:maria.chen@unr.edu> ;
            schema1:identifier [ a schema1:PropertyValue ;
                    schema1:propertyID "https://registry.identifiers.org/registry/orcid" ;
                    schema1:url "https://orcid.org/0000-0002-8765-4321" ;
                    schema1:value "0000-0002-8765-4321" ] ;
            schema1:name "Dr. Maria Chen" ] ;
    prov:wasInformedBy ex:activity-sample-collection .


```

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
- $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/provProperties/generatedBy/schema.yaml
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
    $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/person/schema.yaml
  Organization:
    $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/organization/schema.yaml
  AgentInRole:
    $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/agentInRole/schema.yaml
  Instrument:
    $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/instrument/schema.yaml
  DefinedTerm:
    $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/definedTerm/schema.yaml
  LabeledLink:
    $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/labeledLink/schema.yaml
  SpatialExtent:
    $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/spatialExtent/schema.yaml
  HowTo:
    type: object
    description: A methodology or protocol described as a HowTo with optional steps
    properties:
      '@type':
        type: array
        items:
          type: string
        contains:
          const: schema:HowTo
        minItems: 1
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
        type: array
        items:
          type: string
        contains:
          const: schema:HowToStep
        minItems: 1
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

* YAML version: [schema.yaml](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/provProperties/provActivity/schema.json)
* JSON version: [schema.json](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/provProperties/provActivity/schema.yaml)


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
[context.jsonld](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/provProperties/provActivity/context.jsonld)

## Sources

* [W3C PROV-O: The PROV Ontology](https://www.w3.org/TR/prov-o/)
* [W3C PROV-DM: The PROV Data Model](https://www.w3.org/TR/prov-dm/)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/Cross-Domain-Interoperability-Framework/metadataBuildingBlocks](https://github.com/Cross-Domain-Interoperability-Framework/metadataBuildingBlocks)
* Path: `_sources/provProperties/provActivity`

