
# CDIF Provenance Activity (Schema)

`cdif.bbr.metadata.cdifDataType.cdifProvActivity` *v0.1*

Extended provenance activity for CDIF metadata, adding schema.org Action properties (agents, methodology, temporal bounds, action chaining) to the base prov:Activity. Instruments are nested within prov:used items via schema:instrument sub-key, referencing the generic instrument building block. Defines properties: @type, prov:used, schema:name, schema:description, schema:identifier, schema:agent, schema:participant, schema:object, schema:result, schema:actionStatus, schema:startTime, schema:endTime, schema:location, schema:actionProcess, schema:error, schema:additionalProperty. Uses building blocks: generatedBy (provProperties), person (schemaorgProperties), organization (schemaorgProperties), agentInRole (schemaorgProperties), identifier (schemaorgProperties), instrument (schemaorgProperties), definedTerm (schemaorgProperties), labeledLink (schemaorgProperties), spatialExtent (schemaorgProperties), additionalProperty (schemaorgProperties).

[*Status*](http://www.opengis.net/def/status): Under development

## Description

## CDIF Provenance Activity

Extended provenance activity for CDIF metadata, adding schema.org Action properties (agents, methodology, temporal bounds, action chaining) to the base prov:Activity. What the activity used is recorded with schema:instrument (instruments, software and reagents, each told apart by a Wikidata kind term in schema:additionalType) and schema:object (inputs). An activity must have at least one of schema:instrument, schema:object or schema:actionProcess. The plan it followed is the {@id} form of schema:actionProcess; an inline HowTo records the procedure as performed and links the plan with schema:isBasedOn.

### Defined properties

- **@type** — must include both schema:Action and prov:Activity
- **schema:instrument** — instruments, software and reagents used: an {@id} reference, or a description in place whose schema:additionalType carries one of Q3099911 (instrument), Q7397 (software) or Q2356542 (reagent)
- **prov:used** — not used by this profile; accepted only in the core shape (strings and @id references)
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

### Minimal CDIF Provenance Activity
Bare schema:Action + prov:Activity with a name — the smallest shape
the BB allows.
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "prov": "http://www.w3.org/ns/prov#",
    "ex": "https://example.org/"
  },
  "@type": [
    "schema:Action",
    "prov:Activity"
  ],
  "@id": "ex:activity/sample-prep",
  "schema:name": "Sample preparation",
  "schema:object": [
    {
      "@id": "ex:sample-001"
    }
  ]
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
    "https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifDataType/cdifProvActivity/context.jsonld",
    {
      "schema": "http://schema.org/",
      "prov": "http://www.w3.org/ns/prov#",
      "ex": "https://example.org/"
    }
  ],
  "@type": [
    "schema:Action",
    "prov:Activity"
  ],
  "@id": "ex:activity/sample-prep",
  "schema:name": "Sample preparation",
  "schema:object": [
    {
      "@id": "ex:sample-001"
    }
  ]
}
```

#### ttl
```ttl
@prefix ex: <https://example.org/> .
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix schema1: <http://schema.org/> .

<https://example.org/activity/sample-prep> a schema1:Action,
        prov:Activity ;
    schema1:name "Sample preparation" ;
    schema1:object ex:sample-001 .


```


### Complete CDIF Provenance Activity
Soil chemistry analysis activity demonstrating extended cdifProvActivity
block features: multi-typed activity (schema:Action + prov:Activity),
agent with ORCID, schema:instrument with a Wikidata kind term and a
NERC device category, inputs in schema:object, action chaining via
schema:object/result, schema:actionProcess HowTo with ordered steps
whose schema:isBasedOn names the EPA method it followed, and facility
location.
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
    "schema:Action",
    "prov:Activity"
  ],
  "schema:name": "Soil Chemistry Analysis - Great Basin Transect 2025",
  "schema:description": "Major and trace element analysis of soil samples collected along a 200 km transect across the Great Basin, using ICP-MS and XRF spectrometry with certified reference materials.",
  "schema:agent": {
    "@type": [
      "schema:Person"
    ],
    "schema:name": "Dr. Maria Chen",
    "schema:identifier": {
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": {
        "@id": "https://registry.identifiers.org/registry/orcid"
      },
      "schema:value": "0000-0002-8765-4321",
      "schema:url": "https://orcid.org/0000-0002-8765-4321"
    },
    "schema:contactPoint": {
      "@type": [
        "schema:ContactPoint"
      ],
      "schema:email": "maria.chen@unr.edu"
    }
  },
  "schema:object": [
    "Dried and sieved soil samples (<2 mm fraction) from Great Basin transect",
    "Soil core samples collected June 2025, sites GB-001 through GB-045"
  ],
  "schema:result": [
    {
      "@id": "ex:dataset-soil-chem-gb-2025"
    }
  ],
  "schema:actionStatus": "schema:CompletedActionStatus",
  "schema:startTime": "2025-07-15T08:00:00Z",
  "schema:endTime": "2025-09-30T17:00:00Z",
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "Nevada Bureau of Mines and Geology Analytical Lab",
    "schema:address": "University of Nevada, Reno, 1664 N. Virginia Street, Reno, NV 89557",
    "schema:url": "https://www.unr.edu/nbmg"
  },
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
    ],
    "schema:isBasedOn": {
      "@id": "https://www.epa.gov/hw-sw846/sw-846-test-method-6200-field-portable-x-ray-fluorescence-spectrometry-determination"
    }
  },
  "schema:instrument": [
    {
      "@type": [
        "schema:Product",
        "schema:Thing",
        "schema:DefinedTerm"
      ],
      "schema:name": "Inductively Coupled Plasma Mass Spectrometry",
      "schema:termCode": "ICP-MS",
      "schema:inDefinedTermSet": "https://vocab.nerc.ac.uk/collection/L05/current/",
      "schema:alternateName": [
        "Thermo Fisher iCAP RQ ICP-MS"
      ],
      "schema:category": [
        {
          "@type": [
            "schema:DefinedTerm"
          ],
          "schema:name": "Inductively coupled plasma mass spectrometer",
          "schema:termCode": "LAB21",
          "schema:inDefinedTermSet": "https://vocab.nerc.ac.uk/collection/L05/current/"
        }
      ],
      "schema:additionalProperty": [
        {
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            "detectionLimit"
          ],
          "schema:name": "Typical Detection Limit",
          "schema:value": "0.01 mg/kg for trace elements"
        }
      ],
      "schema:additionalType": [
        {
          "@id": "https://vocab.nerc.ac.uk/collection/L05/current/LAB02"
        },
        {
          "@id": "https://www.wikidata.org/entity/Q3099911"
        }
      ]
    }
  ]
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
    "https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifDataType/cdifProvActivity/context.jsonld",
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
  "schema:agent": {
    "@type": [
      "schema:Person"
    ],
    "schema:name": "Dr. Maria Chen",
    "schema:identifier": {
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": {
        "@id": "https://registry.identifiers.org/registry/orcid"
      },
      "schema:value": "0000-0002-8765-4321",
      "schema:url": "https://orcid.org/0000-0002-8765-4321"
    },
    "schema:contactPoint": {
      "@type": [
        "schema:ContactPoint"
      ],
      "schema:email": "maria.chen@unr.edu"
    }
  },
  "schema:object": [
    "Dried and sieved soil samples (<2 mm fraction) from Great Basin transect",
    "Soil core samples collected June 2025, sites GB-001 through GB-045"
  ],
  "schema:result": [
    {
      "@id": "ex:dataset-soil-chem-gb-2025"
    }
  ],
  "schema:actionStatus": "schema:CompletedActionStatus",
  "schema:startTime": "2025-07-15T08:00:00Z",
  "schema:endTime": "2025-09-30T17:00:00Z",
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "Nevada Bureau of Mines and Geology Analytical Lab",
    "schema:address": "University of Nevada, Reno, 1664 N. Virginia Street, Reno, NV 89557",
    "schema:url": "https://www.unr.edu/nbmg"
  },
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
    ],
    "schema:isBasedOn": {
      "@id": "https://www.epa.gov/hw-sw846/sw-846-test-method-6200-field-portable-x-ray-fluorescence-spectrometry-determination"
    }
  },
  "schema:instrument": [
    {
      "@type": [
        "schema:Product",
        "schema:Thing",
        "schema:DefinedTerm"
      ],
      "schema:name": "Inductively Coupled Plasma Mass Spectrometry",
      "schema:termCode": "ICP-MS",
      "schema:inDefinedTermSet": "https://vocab.nerc.ac.uk/collection/L05/current/",
      "schema:alternateName": [
        "Thermo Fisher iCAP RQ ICP-MS"
      ],
      "schema:category": [
        {
          "@type": [
            "schema:DefinedTerm"
          ],
          "schema:name": "Inductively coupled plasma mass spectrometer",
          "schema:termCode": "LAB21",
          "schema:inDefinedTermSet": "https://vocab.nerc.ac.uk/collection/L05/current/"
        }
      ],
      "schema:additionalProperty": [
        {
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            "detectionLimit"
          ],
          "schema:name": "Typical Detection Limit",
          "schema:value": "0.01 mg/kg for trace elements"
        }
      ],
      "schema:additionalType": [
        {
          "@id": "https://vocab.nerc.ac.uk/collection/L05/current/LAB02"
        },
        {
          "@id": "https://www.wikidata.org/entity/Q3099911"
        }
      ]
    }
  ]
}
```

#### ttl
```ttl
@prefix ex: <https://example.org/> .
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix schema1: <http://schema.org/> .
@prefix wd: <https://www.wikidata.org/entity/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ex:activity-soil-chem-analysis a schema1:Action,
        prov:Activity ;
    schema1:actionProcess [ a schema1:HowTo ;
            schema1:description "Combined XRF screening and ICP-MS confirmatory analysis for major and trace elements in soil matrices." ;
            schema1:isBasedOn <https://www.epa.gov/hw-sw846/sw-846-test-method-6200-field-portable-x-ray-fluorescence-spectrometry-determination> ;
            schema1:name "EPA 6200 / ICP-MS Soil Geochemistry Protocol" ;
            schema1:step [ a schema1:HowToStep ;
                    schema1:description "Analyze digested solutions by ICP-MS using external calibration with NIST SRM 2710a and 2711a as quality control standards." ;
                    schema1:name "ICP-MS measurement and calibration" ;
                    schema1:position 2 ],
                [ a schema1:HowToStep ;
                    schema1:description "Homogenize dried samples, split 0.5 g aliquots, digest with HNO3-HCl-HF mixture at 190 C in closed vessels." ;
                    schema1:name "Sample preparation and acid digestion" ;
                    schema1:position 1 ] ] ;
    schema1:actionStatus "schema:CompletedActionStatus" ;
    schema1:agent [ a schema1:Person ;
            schema1:contactPoint [ a schema1:ContactPoint ;
                    schema1:email "maria.chen@unr.edu" ] ;
            schema1:identifier [ a schema1:PropertyValue ;
                    schema1:propertyID <https://registry.identifiers.org/registry/orcid> ;
                    schema1:url "https://orcid.org/0000-0002-8765-4321" ;
                    schema1:value "0000-0002-8765-4321" ] ;
            schema1:name "Dr. Maria Chen" ] ;
    schema1:description "Major and trace element analysis of soil samples collected along a 200 km transect across the Great Basin, using ICP-MS and XRF spectrometry with certified reference materials." ;
    schema1:endTime "2025-09-30T17:00:00Z" ;
    schema1:instrument [ a schema1:DefinedTerm,
                schema1:Product,
                schema1:Thing ;
            schema1:additionalProperty [ a schema1:PropertyValue ;
                    schema1:name "Typical Detection Limit" ;
                    schema1:propertyID "detectionLimit" ;
                    schema1:value "0.01 mg/kg for trace elements" ] ;
            schema1:additionalType <https://vocab.nerc.ac.uk/collection/L05/current/LAB02>,
                wd:Q3099911 ;
            schema1:alternateName "Thermo Fisher iCAP RQ ICP-MS" ;
            schema1:category [ a schema1:DefinedTerm ;
                    schema1:inDefinedTermSet "https://vocab.nerc.ac.uk/collection/L05/current/" ;
                    schema1:name "Inductively coupled plasma mass spectrometer" ;
                    schema1:termCode "LAB21" ] ;
            schema1:inDefinedTermSet "https://vocab.nerc.ac.uk/collection/L05/current/" ;
            schema1:name "Inductively Coupled Plasma Mass Spectrometry" ;
            schema1:termCode "ICP-MS" ] ;
    schema1:location [ a schema1:Place ;
            schema1:address "University of Nevada, Reno, 1664 N. Virginia Street, Reno, NV 89557" ;
            schema1:name "Nevada Bureau of Mines and Geology Analytical Lab" ;
            schema1:url "https://www.unr.edu/nbmg" ] ;
    schema1:name "Soil Chemistry Analysis - Great Basin Transect 2025" ;
    schema1:object "Dried and sieved soil samples (<2 mm fraction) from Great Basin transect",
        "Soil core samples collected June 2025, sites GB-001 through GB-045" ;
    schema1:result ex:dataset-soil-chem-gb-2025 ;
    schema1:startTime "2025-07-15T08:00:00Z" .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: CDIF Provenance Activity
description: Extended provenance activity building block for CDIF -- the schema.org
  implementation. Extends the minimal prov:Activity (generatedBy) with schema.org
  Action properties for agents, instruments, inputs and outputs, methodology and plan,
  temporal bounds, action chaining, and more. What the activity used is recorded with
  schema:instrument (instruments, software, reagents) and schema:object (inputs),
  not with prov:used.
type: object
allOf:
- $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/provProperties/generatedBy/schema.yaml
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
      description: Not used by this profile. A prov:used a record carries is accepted
        when it passes the core shape in generatedBy (strings and @id references)
        and is checked by nothing more. Record instruments, software and reagents
        with schema:instrument, and inputs with schema:object.
      x-jsonld-id: http://www.w3.org/ns/prov#used
    schema:instrument:
      type: array
      minItems: 1
      description: 'Instruments, software and reagents the activity used. Each item
        is either an {@id} reference to a thing described elsewhere, or a description
        in place whose schema:additionalType carries exactly one of three Wikidata
        terms (as the Wikidata entity IRI https://www.wikidata.org/entity/Q..., or
        a wd: CURIE bound to it), which says what kind of thing it is and selects
        the shape it must have: https://www.wikidata.org/entity/Q3099911 (measuring
        instrument) -> Instrument; https://www.wikidata.org/entity/Q7397 (software)
        -> Software; https://www.wikidata.org/entity/Q2356542 (chemical reagent, used
        here for reagents and reference materials) -> Reagent. The kind is read from
        additionalType, not @type, because a reagent can be a schema:Product just
        as an instrument is. Always an array: one activity commonly uses several (a
        laser ablation cell plus the ICP-MS it feeds, the acquisition software, the
        standards).'
      items:
        anyOf:
        - description: reference to an instrument, software or reagent described elsewhere
          $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifDataType/objectReference/schema.yaml
        - $ref: '#/$defs/UsedResource'
      x-jsonld-id: http://schema.org/instrument
  anyOf:
  - required:
    - schema:instrument
  - required:
    - schema:object
  - required:
    - schema:actionProcess
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
      - description: reference to an agent defined elsewhere
        $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifDataType/objectReference/schema.yaml
    schema:participant:
      description: Other participants in this activity
      type: array
      items:
        anyOf:
        - $ref: '#/$defs/Person'
        - $ref: '#/$defs/Organization'
        - $ref: '#/$defs/AgentInRole'
        - description: reference to a participant defined elsewhere
          $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifDataType/objectReference/schema.yaml
    schema:object:
      description: Input entity (or entities) for this activity. Per schema.org, the
        range of schema:object is schema:Thing. Accepts four shapes (1) a string URI,
        (2) an @id reference object, (3) an inline schema:Thing object, or (4) an
        array whose items take any of those shapes (used when an activity has multiple
        inputs, e.g. samples analyzed). Supports action chaining where the value references
        the result of a prior activity.
      anyOf:
      - type: string
      - description: reference to an input entity
        $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifDataType/objectReference/schema.yaml
      - type: object
        description: Inline schema:Thing object describing the input entity.
        properties:
          '@type':
            type: array
            items:
              type: string
            minItems: 1
        required:
        - '@type'
      - type: array
        description: Multiple input entities (e.g. samples analyzed). Each item may
          be a string URI, an @id reference, or an inline schema:Thing.
        items:
          anyOf:
          - type: string
          - type: object
    schema:result:
      description: 'Output entity (or entities) produced by this activity. Per schema.org,
        the range is schema:Thing. Accepts: (1) a string URI reference (action chaining
        shorthand to be referenced as schema:object of a subsequent activity); (2)
        a single {"@id": "<uri>"} object reference; (3) an inline schema:Thing (object
        with @type); or (4) an array of any of these forms (e.g. multiple datasets
        produced by this activity). Profiles may restrict the array item shape further.'
      anyOf:
      - type: string
      - description: reference to an output entity
        $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifDataType/objectReference/schema.yaml
      - type: object
        description: Inline schema:Thing object describing the output entity.
        properties:
          '@type':
            type: array
            items:
              type: string
            minItems: 1
        required:
        - '@type'
      - type: array
        description: Multiple output entities. Each item may be a string URI, an @id
          reference, or an inline schema:Thing.
        items:
          anyOf:
          - type: string
          - type: object
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
      - description: reference to a place defined elsewhere
        $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifDataType/objectReference/schema.yaml
    schema:actionProcess:
      description: 'The plan the activity followed, or the procedure as it was performed.
        The {@id} reference form is the link to the plan (a protocol, method or workflow
        definition described elsewhere; CDIF defines no inline plan object). An inline
        HowTo is the procedure as performed; when the activity also followed a plan,
        that HowTo links the plan with schema:isBasedOn. One path finds the plan in
        both cases: prov:wasGeneratedBy/schema:actionProcess/schema:isBasedOn?'
      anyOf:
      - $ref: '#/$defs/HowTo'
      - type: string
      - description: reference to a methodology defined elsewhere
        $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifDataType/objectReference/schema.yaml
    schema:error:
      type: string
      description: Error description for failed activities
    schema:additionalProperty:
      description: Domain-specific extension properties, typically the parameter values
        this run used. schema.org does not list Action among this property's domains,
        so validator.schema.org warns on it; that warning is known and accepted, because
        schema.org has no Action property for parameter values.
      type: array
      items:
        $ref: '#/$defs/AdditionalProperty'
$defs:
  Person:
    $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/person/schema.yaml
  Organization:
    $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/organization/schema.yaml
  AgentInRole:
    $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/agentInRole/schema.yaml
  Identifier:
    $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/identifier/schema.yaml
  Instrument:
    $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/instrument/schema.yaml
  SpatialExtent:
    $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/spatialExtent/schema.yaml
  AdditionalProperty:
    $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/additionalProperty/schema.yaml
  UsedResource:
    type: object
    description: An instrument, software or reagent described in place. schema:additionalType
      must carry exactly one of the three kind terms; the kind then pins the shape.
      A domain profile adds its own properties (a role, a version, settings).
    required:
    - '@type'
    - schema:additionalType
    properties:
      '@type':
        type: array
        items:
          type: string
        minItems: 1
      schema:additionalType:
        type: array
        minItems: 1
        x-jsonld-id: http://schema.org/additionalType
    oneOf:
    - $ref: '#/$defs/KindInstrument'
    - $ref: '#/$defs/KindSoftware'
    - $ref: '#/$defs/KindReagent'
    allOf:
    - if:
        $ref: '#/$defs/KindInstrument'
      then:
        $ref: '#/$defs/Instrument'
    - if:
        $ref: '#/$defs/KindSoftware'
      then:
        $ref: '#/$defs/Software'
    - if:
        $ref: '#/$defs/KindReagent'
      then:
        $ref: '#/$defs/Reagent'
  KindInstrument:
    description: schema:additionalType names the Wikidata measuring-instrument term
    properties:
      schema:additionalType:
        contains:
          type: object
          required:
          - '@id'
          properties:
            '@id':
              enum:
              - https://www.wikidata.org/entity/Q3099911
              - wd:Q3099911
        x-jsonld-id: http://schema.org/additionalType
    required:
    - schema:additionalType
  KindSoftware:
    description: schema:additionalType names the Wikidata software term
    properties:
      schema:additionalType:
        contains:
          type: object
          required:
          - '@id'
          properties:
            '@id':
              enum:
              - https://www.wikidata.org/entity/Q7397
              - wd:Q7397
        x-jsonld-id: http://schema.org/additionalType
    required:
    - schema:additionalType
  KindReagent:
    description: schema:additionalType names the Wikidata chemical-reagent term
    properties:
      schema:additionalType:
        contains:
          type: object
          required:
          - '@id'
          properties:
            '@id':
              enum:
              - https://www.wikidata.org/entity/Q2356542
              - wd:Q2356542
        x-jsonld-id: http://schema.org/additionalType
    required:
    - schema:additionalType
  Software:
    type: object
    description: Software used by the activity (acquisition, reduction, processing).
    properties:
      '@type':
        type: array
        items:
          type: string
        contains:
          const: schema:SoftwareApplication
      '@id':
        type: string
      schema:name:
        type: string
        x-jsonld-id: http://schema.org/name
      schema:softwareVersion:
        type: string
        x-jsonld-id: http://schema.org/softwareVersion
      schema:url:
        type: string
        format: uri
        x-jsonld-id: http://schema.org/url
    required:
    - '@type'
    - schema:name
  Reagent:
    type: object
    description: 'A reagent, standard or reference material used by the activity.
      @type says what the material is: schema:DefinedTerm for a material identified
      by a registry entry (e.g. a GeoReM reference material), schema:Product for a
      catalogued specimen or purchased lot, schema:ChemicalSubstance for a bulk chemical.'
    properties:
      '@type':
        type: array
        items:
          type: string
        contains:
          enum:
          - schema:DefinedTerm
          - schema:Product
          - schema:ChemicalSubstance
      '@id':
        type: string
      schema:name:
        type: string
        x-jsonld-id: http://schema.org/name
    required:
    - '@type'
    - schema:name
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
        x-jsonld-id: http://schema.org/name
      schema:description:
        type: string
        description: Description of the methodology
        x-jsonld-id: http://schema.org/description
      schema:url:
        type: string
        format: uri
        description: URL to a published methodology or protocol document
        x-jsonld-id: http://schema.org/url
      schema:isBasedOn:
        description: The plan this procedure was based on, when the activity both
          followed a plan and records the procedure as performed. A reference only,
          for now.
        $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifDataType/objectReference/schema.yaml
        x-jsonld-id: http://schema.org/isBasedOn
      schema:step:
        type: array
        description: Ordered steps in this methodology
        items:
          $ref: '#/$defs/HowToStep'
        x-jsonld-id: http://schema.org/step
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
        x-jsonld-id: http://schema.org/name
      schema:description:
        type: string
        description: Description of what this step involves
        x-jsonld-id: http://schema.org/description
      schema:url:
        type: string
        format: uri
        description: URL to documentation for this step
        x-jsonld-id: http://schema.org/url
      schema:position:
        type: integer
        description: Ordinal position of this step
        x-jsonld-id: http://schema.org/position
    required:
    - '@type'
    - schema:name
x-jsonld-prefixes:
  schema: http://schema.org/
  prov: http://www.w3.org/ns/prov#
x-bblocks-metadata:
  itemIdentifier: cdif.bbr.metadata.cdifDataType.cdifProvActivity
  register: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/register.json
  version: '0.1'
  dateOfLastChange: '2026-11-11'

```

Links to the schema:

* YAML version: [schema.yaml](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifDataType/cdifProvActivity/schema.json)
* JSON version: [schema.json](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifDataType/cdifProvActivity/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "schema": "http://schema.org/",
    "prov": "http://www.w3.org/ns/prov#",
    "skos": "http://www.w3.org/2004/02/skos/core#",
    "wd": "https://www.wikidata.org/entity/",
    "nxs": "https://manual.nexusformat.org/classes/",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifDataType/cdifProvActivity/context.jsonld)

## Sources

* [ODIS Provenance Recommendations](https://book.odis.org/thematics/provenance/README.html)
* [schema.org Action](https://schema.org/Action)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/Cross-Domain-Interoperability-Framework/metadataBuildingBlocks](https://github.com/Cross-Domain-Interoperability-Framework/metadataBuildingBlocks)
* Path: `_sources/cdifDataType/cdifProvActivity`

