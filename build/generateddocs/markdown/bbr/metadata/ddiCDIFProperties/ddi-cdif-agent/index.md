
# DDI-CDI Agent (Schema)

`cdif.bbr.metadata.ddiCDIFProperties.ddi-cdif-agent` *v0.1*

DDI-CDI Agent class hierarchy for CDIF metadata. Covers Agent (abstract base) and its subclasses: Individual (person), Machine (software/hardware), Organization (group/institution), and ProcessingAgent (orchestrates production). Defines properties for identification, contact information, naming, and agent-activity relationships.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

DDI-CDI Agent is the abstract supertype for entities that can act, hold roles, or be referenced from provenance and process metadata. This BB is a thin polymorphic wrapper that composes the four concrete Agent subtypes via `anyOf`: `cdi:Individual` (a person), `cdi:Machine` (software or hardware), `cdi:Organization` (a group or institution), and `cdi:ProcessingAgent` (an agent that orchestrates production activities).

Each subtype is defined in its own building block (`ddicdiIndividual`, `ddicdiMachine`, `ddicdiOrganization`, `ddicdiProcessingAgent`); use this BB when a property's range is `cdi:Agent` and any of the four subclasses is acceptable.

## Examples

### Minimal Agent
Bare cdi:Individual — the BB root is an anyOf of Individual, Machine,
Organization, or ProcessingAgent. Any of those subtypes with @type only
satisfies the umbrella schema.
#### json
```json
{
  "@context": {
    "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
    "ex": "https://example.org/"
  },
  "@type": ["cdi:Individual"],
  "@id": "ex:person/alice"
}

```

#### jsonld
```jsonld
{
  "@context": [
    {
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/"
    },
    "https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiCDIFProperties/ddi-cdif-agent/context.jsonld",
    {
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "ex": "https://example.org/"
    }
  ],
  "@type": [
    "cdi:Individual"
  ],
  "@id": "ex:person/alice"
}
```

#### ttl
```ttl
@prefix cdi: <http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/> .

<https://example.org/person/alice> a cdi:Individual .


```


### Complete Agent hierarchy
Demonstrates Individual, Organization, and ProcessingAgent
agent types with identification, contact information, and
activity relationships.
#### json
```json
{
  "@context": {
    "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
    "ex": "https://example.org/"
  },
  "@id": "ex:researcher-jane-doe",
  "@type": [
    "cdi:Individual"
  ],
  "cdi:individualName": {
    "@type": [
      "cdi:IndividualName"
    ],
    "cdi:firstGiven": "Jane",
    "cdi:lastFamily": "Doe",
    "cdi:prefix": "Dr.",
    "cdi:fullName": {
      "@type": [
        "cdi:InternationalString"
      ],
      "cdi:languageSpecificString": {
        "@type": [
          "cdi:LanguageString"
        ],
        "cdi:content": "Dr. Jane Doe",
        "cdi:language": "en"
      }
    },
    "cdi:isPreferred": true
  },
  "cdi:contactInformation": {
    "@type": [
      "cdi:ContactInformation"
    ],
    "cdi:email": {
      "@type": [
        "cdi:Email"
      ],
      "cdi:internetEmail": "jane.doe@example.org",
      "cdi:typeOfEmail": {
        "@type": [
          "cdi:ControlledVocabularyEntry"
        ],
        "cdi:entryValue": [
          "work"
        ]
      },
      "cdi:isPreferred": true
    },
    "cdi:address": {
      "@type": [
        "cdi:Address"
      ],
      "cdi:line": [
        "Department of Earth Sciences",
        "123 University Avenue"
      ],
      "cdi:cityPlaceLocal": "Reno",
      "cdi:stateProvince": "Nevada",
      "cdi:postalCode": "89557",
      "cdi:countryCode": {
        "@type": [
          "cdi:ControlledVocabularyEntry"
        ],
        "cdi:entryValue": [
          "US"
        ]
      },
      "cdi:typeOfAddress": {
        "@type": [
          "cdi:ControlledVocabularyEntry"
        ],
        "cdi:entryValue": [
          "work"
        ]
      }
    }
  },
  "cdi:identifier": {
    "@type": [
      "cdi:Identifier"
    ],
    "cdi:nonDdiIdentifier": {
      "@type": [
        "cdi:NonDdiIdentifier"
      ],
      "cdi:identifierContent": "https://orcid.org/0000-0002-1234-5678",
      "cdi:managingAgency": "ORCID"
    }
  }
}

```

#### jsonld
```jsonld
{
  "@context": [
    {
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/"
    },
    "https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiCDIFProperties/ddi-cdif-agent/context.jsonld",
    {
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "ex": "https://example.org/"
    }
  ],
  "@id": "ex:researcher-jane-doe",
  "@type": [
    "cdi:Individual"
  ],
  "cdi:individualName": {
    "@type": [
      "cdi:IndividualName"
    ],
    "cdi:firstGiven": "Jane",
    "cdi:lastFamily": "Doe",
    "cdi:prefix": "Dr.",
    "cdi:fullName": {
      "@type": [
        "cdi:InternationalString"
      ],
      "cdi:languageSpecificString": {
        "@type": [
          "cdi:LanguageString"
        ],
        "cdi:content": "Dr. Jane Doe",
        "cdi:language": "en"
      }
    },
    "cdi:isPreferred": true
  },
  "cdi:contactInformation": {
    "@type": [
      "cdi:ContactInformation"
    ],
    "cdi:email": {
      "@type": [
        "cdi:Email"
      ],
      "cdi:internetEmail": "jane.doe@example.org",
      "cdi:typeOfEmail": {
        "@type": [
          "cdi:ControlledVocabularyEntry"
        ],
        "cdi:entryValue": [
          "work"
        ]
      },
      "cdi:isPreferred": true
    },
    "cdi:address": {
      "@type": [
        "cdi:Address"
      ],
      "cdi:line": [
        "Department of Earth Sciences",
        "123 University Avenue"
      ],
      "cdi:cityPlaceLocal": "Reno",
      "cdi:stateProvince": "Nevada",
      "cdi:postalCode": "89557",
      "cdi:countryCode": {
        "@type": [
          "cdi:ControlledVocabularyEntry"
        ],
        "cdi:entryValue": [
          "US"
        ]
      },
      "cdi:typeOfAddress": {
        "@type": [
          "cdi:ControlledVocabularyEntry"
        ],
        "cdi:entryValue": [
          "work"
        ]
      }
    }
  },
  "cdi:identifier": {
    "@type": [
      "cdi:Identifier"
    ],
    "cdi:nonDdiIdentifier": {
      "@type": [
        "cdi:NonDdiIdentifier"
      ],
      "cdi:identifierContent": "https://orcid.org/0000-0002-1234-5678",
      "cdi:managingAgency": "ORCID"
    }
  }
}
```

#### ttl
```ttl
@prefix cdi: <http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/> .
@prefix ex: <https://example.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ex:researcher-jane-doe a cdi:Individual ;
    cdi:contactInformation [ a cdi:ContactInformation ;
            cdi:address [ a cdi:Address ;
                    cdi:cityPlaceLocal "Reno" ;
                    cdi:countryCode [ a cdi:ControlledVocabularyEntry ;
                            cdi:entryValue "US" ] ;
                    cdi:line "123 University Avenue",
                        "Department of Earth Sciences" ;
                    cdi:postalCode "89557" ;
                    cdi:stateProvince "Nevada" ;
                    cdi:typeOfAddress [ a cdi:ControlledVocabularyEntry ;
                            cdi:entryValue "work" ] ] ;
            cdi:email [ a cdi:Email ;
                    cdi:internetEmail "jane.doe@example.org" ;
                    cdi:isPreferred true ;
                    cdi:typeOfEmail [ a cdi:ControlledVocabularyEntry ;
                            cdi:entryValue "work" ] ] ] ;
    cdi:identifier [ a cdi:Identifier ;
            cdi:nonDdiIdentifier [ a cdi:NonDdiIdentifier ;
                    cdi:identifierContent "https://orcid.org/0000-0002-1234-5678" ;
                    cdi:managingAgency "ORCID" ] ] ;
    cdi:individualName [ a cdi:IndividualName ;
            cdi:firstGiven "Jane" ;
            cdi:fullName [ a cdi:InternationalString ;
                    cdi:languageSpecificString [ a cdi:LanguageString ;
                            cdi:content "Dr. Jane Doe" ;
                            cdi:language "en" ] ] ;
            cdi:isPreferred true ;
            cdi:lastFamily "Doe" ;
            cdi:prefix "Dr." ] .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: DDI-CDI Agent
description: DDI-CDI Agent class hierarchy. Covers Individual (person), Machine (software/hardware),
  Organization (group/institution), and ProcessingAgent (orchestrates production activities)
  using DDI Cross-Domain Integration vocabulary. Each agent subtype is defined in
  its own building block; this schema composes them.
anyOf:
- $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiCDIFProperties/ddi-cdif-individual/schema.yaml
- $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiCDIFProperties/ddi-cdif-machine/schema.yaml
- $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiCDIFProperties/ddi-cdif-organization/schema.yaml
- $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiCDIFProperties/ddi-cdif-processing-agent/schema.yaml
x-jsonld-prefixes:
  cdi: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/

```

Links to the schema:

* YAML version: [schema.yaml](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiCDIFProperties/ddi-cdif-agent/schema.json)
* JSON version: [schema.json](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiCDIFProperties/ddi-cdif-agent/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiCDIFProperties/ddi-cdif-agent/context.jsonld)

## Sources

* [DDI-CDI 1.0 Specification](https://ddialliance.org/Specification/DDI-CDI/1.0/)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/Cross-Domain-Interoperability-Framework/metadataBuildingBlocks](https://github.com/Cross-Domain-Interoperability-Framework/metadataBuildingBlocks)
* Path: `_sources/ddiCDIFProperties/ddi-cdif-agent`

