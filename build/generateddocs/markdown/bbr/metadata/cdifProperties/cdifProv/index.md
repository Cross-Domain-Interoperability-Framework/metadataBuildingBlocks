
# CDIF Provenance Activity (Schema)

`cdif.bbr.metadata.cdifProperties.cdifProv` *v0.1*

Extended provenance activity for CDIF metadata, adding schema.org Action properties (agents, methodology, temporal bounds, action chaining) to the base prov:Activity. Instruments are nested within prov:used items via schema:instrument sub-key, referencing the generic instrument building block. Defines properties: @type, prov:used, schema:name, schema:description, schema:identifier, schema:agent, schema:participant, schema:object, schema:result, schema:actionStatus, schema:startTime, schema:endTime, schema:location, schema:actionProcess, schema:error, schema:additionalProperty. Uses building blocks: generatedBy (provProperties), person (schemaorgProperties), organization (schemaorgProperties), agentInRole (schemaorgProperties), identifier (schemaorgProperties), instrument (schemaorgProperties), definedTerm (schemaorgProperties), labeledLink (schemaorgProperties), spatialExtent (schemaorgProperties), additionalProperty (schemaorgProperties).

[*Status*](http://www.opengis.net/def/status): Under development

## Description

## CDIF Provenance Activity

Extended provenance activity for CDIF metadata, adding schema.org Action properties (agents, methodology, temporal bounds, action chaining) to the base prov:Activity. Instruments are nested within prov:used items via schema:instrument sub-key.

### Defined properties

- **@type** — must include both schema:Action and prov:Activity
- **prov:used** — items used by the activity; can include instruments via schema:instrument sub-key
- **schema:name** — human-readable name for the activity
- **schema:description** — text description of what this activity did
- **schema:identifier** — formal identifier for this activity
- **schema:agent** — primary responsible agent for this activity
- **schema:participant** — other participants in this activity
- **schema:object** — input entity for this activity (for action chaining)
- **schema:result** — output entity produced by this activity (for action chaining)
- **schema:actionStatus** — status of this activity
- **schema:startTime** — ISO 8601 date-time when the activity started
- **schema:endTime** — ISO 8601 date-time when the activity ended
- **schema:location** — where the activity occurred
- **schema:actionProcess** — methodology or protocol for this activity
- **schema:error** — error description for failed activities
- **schema:additionalProperty** — domain-specific extension properties

### Dependencies

- [generatedBy](../../provProperties/generatedBy/) — base provenance activity
- [person](../../schemaorgProperties/person/) — person agent
- [organization](../../schemaorgProperties/organization/) — organization agent
- [agentInRole](../../schemaorgProperties/agentInRole/) — agent with qualified role
- [identifier](../../schemaorgProperties/identifier/) — structured identifier
- [instrument](../../schemaorgProperties/instrument/) — generic instrument
- [definedTerm](../../schemaorgProperties/definedTerm/) — controlled vocabulary term
- [labeledLink](../../schemaorgProperties/labeledLink/) — link with label and description
- [spatialExtent](../../schemaorgProperties/spatialExtent/) — spatial location
- [additionalProperty](../../schemaorgProperties/additionalProperty/) — PropertyValue for extension properties

## Examples

### Example CDIF provenance activity.
Soil chemistry analysis activity demonstrating extended cdifProv building
block features: multi-typed activity (schema:Action + prov:Activity), agent
with ORCID, DefinedTerm instrument with detection limit, prov:used array
(vocab URI, string, CreativeWork), action chaining via schema:object/result,
schema:actionProcess HowTo with ordered steps, and facility location.
#### json
```json
{
    "@context": {
        "schema": "http://schema.org/",
        "prov": "http://www.w3.org/ns/prov#",
        "ex": "https://example.org/"
    },
    "@id": "ex:activity-soil-chem-analysis",
    "@type": ["schema:Action", "prov:Activity"],
    "schema:name": "Soil Chemistry Analysis - Great Basin Transect 2025",
    "schema:description": "Major and trace element analysis of soil samples collected along a 200 km transect across the Great Basin, using ICP-MS and XRF spectrometry with certified reference materials.",
    "prov:used": [
        {
            "schema:instrument": {
                "@type": ["schema:Thing", "schema:DefinedTerm"],
                "schema:name": "Inductively Coupled Plasma Mass Spectrometry",
                "schema:termCode": "ICP-MS",
                "schema:inDefinedTermSet": "https://vocab.nerc.ac.uk/collection/L05/current/",
                "schema:alternateName": "Thermo Fisher iCAP RQ ICP-MS",
                "schema:additionalProperty": [
                    {
                        "@type": "schema:PropertyValue",
                        "schema:propertyID": ["detectionLimit"],
                        "schema:name": "Typical Detection Limit",
                        "schema:value": "0.01 mg/kg for trace elements"
                    }
                ]
            }
        },
        "https://vocab.nerc.ac.uk/collection/L05/current/LAB02",
        "Soil core samples collected June 2025, sites GB-001 through GB-045",
        {
            "@type": "schema:CreativeWork",
            "schema:name": "EPA Method 6200 - XRF Analysis of Soils",
            "schema:url": "https://www.epa.gov/hw-sw846/sw-846-test-method-6200-field-portable-x-ray-fluorescence-spectrometry-determination"
        }
    ],
    "schema:agent": {
        "@type": "schema:Person",
        "schema:name": "Dr. Maria Chen",
        "schema:identifier": {
            "@type": "schema:PropertyValue",
            "schema:propertyID": "https://registry.identifiers.org/registry/orcid",
            "schema:value": "0000-0002-8765-4321",
            "schema:url": "https://orcid.org/0000-0002-8765-4321"
        },
        "schema:contactPoint": {"@id": "mailto:maria.chen@unr.edu"}
    },
    "schema:object": "Dried and sieved soil samples (<2 mm fraction) from Great Basin transect",
    "schema:result": {"@id": "ex:dataset-soil-chem-gb-2025"},
    "schema:actionStatus": "schema:CompletedActionStatus",
    "schema:startTime": "2025-07-15T08:00:00Z",
    "schema:endTime": "2025-09-30T17:00:00Z",
    "schema:location": {
        "@type": "schema:Place",
        "schema:name": "Nevada Bureau of Mines and Geology Analytical Lab",
        "schema:address": "University of Nevada, Reno, 1664 N. Virginia Street, Reno, NV 89557",
        "schema:url": "https://www.unr.edu/nbmg"
    },
    "schema:actionProcess": {
        "@type": "schema:HowTo",
        "schema:name": "EPA 6200 / ICP-MS Soil Geochemistry Protocol",
        "schema:description": "Combined XRF screening and ICP-MS confirmatory analysis for major and trace elements in soil matrices.",
        "schema:step": [
            {
                "@type": "schema:HowToStep",
                "schema:name": "Sample preparation and acid digestion",
                "schema:description": "Homogenize dried samples, split 0.5 g aliquots, digest with HNO3-HCl-HF mixture at 190 C in closed vessels.",
                "schema:position": 1
            },
            {
                "@type": "schema:HowToStep",
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
      "schema": "http://schema.org/",
      "prov": "http://www.w3.org/ns/prov#"
    },
    "https://usgin.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifProperties/cdifProv/context.jsonld",
    {
      "schema": "http://schema.org/",
      "prov": "http://www.w3.org/ns/prov#",
      "ex": "https://example.org/"
    }
  ],
  "@id": "ex:activity-soil-chem-analysis",
  "@type": [
    "schema:Action",
    "prov:Activity"
  ],
  "schema:name": "Soil Chemistry Analysis - Great Basin Transect 2025",
  "schema:description": "Major and trace element analysis of soil samples collected along a 200 km transect across the Great Basin, using ICP-MS and XRF spectrometry with certified reference materials.",
  "prov:used": [
    {
      "schema:instrument": {
        "@type": [
          "schema:Thing",
          "schema:DefinedTerm"
        ],
        "schema:name": "Inductively Coupled Plasma Mass Spectrometry",
        "schema:termCode": "ICP-MS",
        "schema:inDefinedTermSet": "https://vocab.nerc.ac.uk/collection/L05/current/",
        "schema:alternateName": "Thermo Fisher iCAP RQ ICP-MS",
        "schema:additionalProperty": [
          {
            "@type": "schema:PropertyValue",
            "schema:propertyID": [
              "detectionLimit"
            ],
            "schema:name": "Typical Detection Limit",
            "schema:value": "0.01 mg/kg for trace elements"
          }
        ]
      }
    },
    "https://vocab.nerc.ac.uk/collection/L05/current/LAB02",
    "Soil core samples collected June 2025, sites GB-001 through GB-045",
    {
      "@type": "schema:CreativeWork",
      "schema:name": "EPA Method 6200 - XRF Analysis of Soils",
      "schema:url": "https://www.epa.gov/hw-sw846/sw-846-test-method-6200-field-portable-x-ray-fluorescence-spectrometry-determination"
    }
  ],
  "schema:agent": {
    "@type": "schema:Person",
    "schema:name": "Dr. Maria Chen",
    "schema:identifier": {
      "@type": "schema:PropertyValue",
      "schema:propertyID": "https://registry.identifiers.org/registry/orcid",
      "schema:value": "0000-0002-8765-4321",
      "schema:url": "https://orcid.org/0000-0002-8765-4321"
    },
    "schema:contactPoint": {
      "@id": "mailto:maria.chen@unr.edu"
    }
  },
  "schema:object": "Dried and sieved soil samples (<2 mm fraction) from Great Basin transect",
  "schema:result": {
    "@id": "ex:dataset-soil-chem-gb-2025"
  },
  "schema:actionStatus": "schema:CompletedActionStatus",
  "schema:startTime": "2025-07-15T08:00:00Z",
  "schema:endTime": "2025-09-30T17:00:00Z",
  "schema:location": {
    "@type": "schema:Place",
    "schema:name": "Nevada Bureau of Mines and Geology Analytical Lab",
    "schema:address": "University of Nevada, Reno, 1664 N. Virginia Street, Reno, NV 89557",
    "schema:url": "https://www.unr.edu/nbmg"
  },
  "schema:actionProcess": {
    "@type": "schema:HowTo",
    "schema:name": "EPA 6200 / ICP-MS Soil Geochemistry Protocol",
    "schema:description": "Combined XRF screening and ICP-MS confirmatory analysis for major and trace elements in soil matrices.",
    "schema:step": [
      {
        "@type": "schema:HowToStep",
        "schema:name": "Sample preparation and acid digestion",
        "schema:description": "Homogenize dried samples, split 0.5 g aliquots, digest with HNO3-HCl-HF mixture at 190 C in closed vessels.",
        "schema:position": 1
      },
      {
        "@type": "schema:HowToStep",
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

ex:activity-soil-chem-analysis a schema1:Action,
        prov:Activity ;
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
    schema1:agent [ a schema1:Person ;
            schema1:contactPoint <mailto:maria.chen@unr.edu> ;
            schema1:identifier [ a schema1:PropertyValue ;
                    schema1:propertyID "https://registry.identifiers.org/registry/orcid" ;
                    schema1:url "https://orcid.org/0000-0002-8765-4321" ;
                    schema1:value "0000-0002-8765-4321" ] ;
            schema1:name "Dr. Maria Chen" ] ;
    schema1:description "Major and trace element analysis of soil samples collected along a 200 km transect across the Great Basin, using ICP-MS and XRF spectrometry with certified reference materials." ;
    schema1:endTime "2025-09-30T17:00:00Z" ;
    schema1:location [ a schema1:Place ;
            schema1:address "University of Nevada, Reno, 1664 N. Virginia Street, Reno, NV 89557" ;
            schema1:name "Nevada Bureau of Mines and Geology Analytical Lab" ;
            schema1:url "https://www.unr.edu/nbmg" ] ;
    schema1:name "Soil Chemistry Analysis - Great Basin Transect 2025" ;
    schema1:object "Dried and sieved soil samples (<2 mm fraction) from Great Basin transect" ;
    schema1:result ex:dataset-soil-chem-gb-2025 ;
    schema1:startTime "2025-07-15T08:00:00Z" ;
    prov:used [ schema1:instrument [ a schema1:DefinedTerm,
                        schema1:Thing ;
                    schema1:additionalProperty [ a schema1:PropertyValue ;
                            schema1:name "Typical Detection Limit" ;
                            schema1:propertyID "detectionLimit" ;
                            schema1:value "0.01 mg/kg for trace elements" ] ;
                    schema1:alternateName "Thermo Fisher iCAP RQ ICP-MS" ;
                    schema1:inDefinedTermSet "https://vocab.nerc.ac.uk/collection/L05/current/" ;
                    schema1:name "Inductively Coupled Plasma Mass Spectrometry" ;
                    schema1:termCode "ICP-MS" ] ],
        [ a schema1:CreativeWork ;
            schema1:name "EPA Method 6200 - XRF Analysis of Soils" ;
            schema1:url "https://www.epa.gov/hw-sw846/sw-846-test-method-6200-field-portable-x-ray-fluorescence-spectrometry-determination" ],
        "Soil core samples collected June 2025, sites GB-001 through GB-045",
        "https://vocab.nerc.ac.uk/collection/L05/current/LAB02" .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: CDIF Provenance Activity
description: Extended provenance activity building block for CDIF. Extends the minimal
  prov:Activity (generatedBy) with schema.org Action properties for comprehensive
  provenance documentation including agents, instruments, methodology, temporal bounds,
  action chaining, and more.
type: object
allOf:
- $ref: https://usgin.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/provProperties/generatedBy/schema.yaml
- type: object
  properties:
    '@type':
      type: array
      items:
        type: string
      minItems: 2
      contains:
        const: schema:Action
      description: Must include both schema:Action and prov:Activity (prov:Activity
        required by base generatedBy schema)
    prov:used:
      type: array
      items:
        anyOf:
        - type: string
        - type: object
          properties:
            '@id':
              type: string
              description: a resolvable reference to a representation of the software
                or instrument used
        - type: object
          description: an item used by the activity that includes a schema:instrument
            sub-key
          properties:
            schema:instrument:
              $ref: '#/$defs/Instrument'
          required:
          - schema:instrument
    schema:name:
      type: string
      description: Human-readable name for the activity
    schema:description:
      type: string
      description: Text description of what this activity did
    schema:identifier:
      description: Formal identifier for this activity
      anyOf:
      - $ref: '#/$defs/Identifier'
      - type: string
    schema:agent:
      description: Primary responsible agent for this activity (maps to PROV wasAssociatedWith)
      anyOf:
      - $ref: '#/$defs/Person'
      - $ref: '#/$defs/Organization'
      - $ref: '#/$defs/AgentInRole'
      - type: object
        properties:
          '@id':
            type: string
            description: reference to an agent defined elsewhere
    schema:participant:
      description: Other participants in this activity
      type: array
      items:
        anyOf:
        - $ref: '#/$defs/Person'
        - $ref: '#/$defs/Organization'
        - $ref: '#/$defs/AgentInRole'
        - type: object
          properties:
            '@id':
              type: string
              description: reference to a participant defined elsewhere
    schema:object:
      description: Input entity for this activity (for action chaining, references
        the result of a prior activity)
      anyOf:
      - type: string
      - type: object
        properties:
          '@id':
            type: string
            description: reference to an input entity
    schema:result:
      description: Output entity produced by this activity (for action chaining, can
        be referenced as object of a subsequent activity)
      anyOf:
      - type: string
      - type: object
        properties:
          '@id':
            type: string
            description: reference to an output entity
    schema:actionStatus:
      type: string
      description: Status of this activity
      enum:
      - schema:CompletedActionStatus
      - schema:ActiveActionStatus
      - schema:PotentialActionStatus
      - schema:FailedActionStatus
    schema:startTime:
      type: string
      description: ISO8601 date-time when the activity started (maps to PROV startedAtTime)
    schema:endTime:
      type: string
      description: ISO8601 date-time when the activity ended (maps to PROV endedAtTime)
    schema:location:
      description: Where the activity occurred
      anyOf:
      - $ref: '#/$defs/SpatialExtent'
      - type: string
      - type: object
        properties:
          '@id':
            type: string
            description: reference to a place defined elsewhere
    schema:actionProcess:
      description: Methodology or protocol for this activity
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
      description: Error description for failed activities
    schema:additionalProperty:
      description: Domain-specific extension properties
      type: array
      items:
        $ref: '#/$defs/AdditionalProperty'
$defs:
  Person:
    $ref: https://usgin.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/person/schema.yaml
  Organization:
    $ref: https://usgin.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/organization/schema.yaml
  AgentInRole:
    $ref: https://usgin.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/agentInRole/schema.yaml
  Identifier:
    $ref: https://usgin.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/identifier/schema.yaml
  Instrument:
    $ref: https://usgin.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/instrument/schema.yaml
  DefinedTerm:
    $ref: https://usgin.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/definedTerm/schema.yaml
  LabeledLink:
    $ref: https://usgin.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/labeledLink/schema.yaml
  SpatialExtent:
    $ref: https://usgin.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/spatialExtent/schema.yaml
  AdditionalProperty:
    $ref: https://usgin.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/additionalProperty/schema.yaml
  HowTo:
    type: object
    description: A methodology or protocol described as a HowTo with optional steps
    properties:
      '@type':
        type: string
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
        type: string
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
  Claim:
    type: object
    description: A statement or assertion about the dataset, such as a quality claim
    properties:
      '@type':
        type: string
        const: schema:Claim
      '@id':
        type: string
      schema:claimReviewed:
        type: string
        description: The claim being reviewed or asserted
      schema:author:
        description: Author of this claim
        anyOf:
        - $ref: '#/$defs/Person'
        - $ref: '#/$defs/Organization'
        - type: object
          properties:
            '@id':
              type: string
      schema:datePublished:
        type: string
        description: ISO8601 date when this claim was published
      schema:appearance:
        description: Where this claim appears
        anyOf:
        - type: string
        - $ref: '#/$defs/LabeledLink'
    required:
    - '@type'
    - schema:claimReviewed
x-jsonld-prefixes:
  schema: http://schema.org/
  prov: http://www.w3.org/ns/prov#

```

Links to the schema:

* YAML version: [schema.yaml](https://usgin.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifProperties/cdifProv/schema.json)
* JSON version: [schema.json](https://usgin.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifProperties/cdifProv/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "schema": "http://schema.org/",
    "prov": "http://www.w3.org/ns/prov#",
    "nxs": "http://purl.org/nexusformat/definitions/",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://usgin.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifProperties/cdifProv/context.jsonld)

## Sources

* [ODIS Provenance Recommendations](https://book.odis.org/thematics/provenance/README.html)
* [schema.org Action](https://schema.org/Action)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/usgin/metadataBuildingBlocks](https://github.com/usgin/metadataBuildingBlocks)
* Path: `_sources/cdifProperties/cdifProv`

