
# DDI-CDI Agent (Schema)

`cdif.bbr.metadata.ddiProperties.ddicdiAgent` *v0.1*

DDI-CDI Agent class hierarchy for CDIF metadata. Covers Agent (abstract base) and its subclasses: Individual (person), Machine (software/hardware), Organization (group/institution), and ProcessingAgent (orchestrates production). Defines properties for identification, contact information, naming, and agent-activity relationships.

[*Status*](http://www.opengis.net/def/status): Under development

## Examples

### Example DDI-CDI agent hierarchy.
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
  "@graph": [
    {
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
            "cdi:entryValue": "work"
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
            "cdi:entryValue": "US"
          },
          "cdi:typeOfAddress": {
            "@type": [
              "cdi:ControlledVocabularyEntry"
            ],
            "cdi:entryValue": "work"
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
    },
    {
      "@id": "ex:org-earth-science-institute",
      "@type": [
        "cdi:Organization"
      ],
      "cdi:organizationName": {
        "@type": [
          "cdi:OrganizationName"
        ],
        "cdi:name": "Earth Science Research Institute",
        "cdi:abbreviation": {
          "@type": [
            "cdi:InternationalString"
          ],
          "cdi:languageSpecificString": {
            "@type": [
              "cdi:LanguageString"
            ],
            "cdi:content": "ESRI",
            "cdi:language": "en"
          }
        },
        "cdi:isFormal": true,
        "cdi:typeOfOrganizationName": {
          "@type": [
            "cdi:ControlledVocabularyEntry"
          ],
          "cdi:entryValue": "legal"
        }
      },
      "cdi:contactInformation": {
        "@type": [
          "cdi:ContactInformation"
        ],
        "cdi:website": {
          "@type": [
            "cdi:WebLink"
          ],
          "cdi:uri": "https://www.esri-example.org",
          "cdi:typeOfWebsite": {
            "@type": [
              "cdi:ControlledVocabularyEntry"
            ],
            "cdi:entryValue": "homepage"
          },
          "cdi:isPreferred": true
        },
        "cdi:address": {
          "@type": [
            "cdi:Address"
          ],
          "cdi:line": ["456 Research Boulevard"],
          "cdi:cityPlaceLocal": "Reno",
          "cdi:stateProvince": "Nevada",
          "cdi:postalCode": "89512",
          "cdi:countryCode": {
            "@type": [
              "cdi:ControlledVocabularyEntry"
            ],
            "cdi:entryValue": "US"
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
          "cdi:identifierContent": "https://ror.org/00example",
          "cdi:managingAgency": "ROR"
        }
      }
    },
    {
      "@id": "ex:agent-data-pipeline",
      "@type": [
        "cdi:ProcessingAgent"
      ],
      "cdi:identifier": {
        "@type": [
          "cdi:Identifier"
        ],
        "cdi:nonDdiIdentifier": {
          "@type": [
            "cdi:NonDdiIdentifier"
          ],
          "cdi:identifierContent": "pipeline-agent-v2.1",
          "cdi:managingAgency": "ESRI internal"
        }
      },
      "cdi:purpose": {
        "@type": [
          "cdi:InternationalString"
        ],
        "cdi:languageSpecificString": {
          "@type": [
            "cdi:LanguageString"
          ],
          "cdi:content": "Automated data processing and quality control pipeline",
          "cdi:language": "en"
        }
      },
      "cdi:performs": [
        {
          "@id": "ex:activity-soil-chem-analysis"
        }
      ],
      "cdi:operatesOn": [
        {
          "@id": "ex:env-hpc-cluster"
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
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/"
    },
    "https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiAgent/context.jsonld",
    {
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "ex": "https://example.org/"
    }
  ],
  "@graph": [
    {
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
            "cdi:entryValue": "work"
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
            "cdi:entryValue": "US"
          },
          "cdi:typeOfAddress": {
            "@type": [
              "cdi:ControlledVocabularyEntry"
            ],
            "cdi:entryValue": "work"
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
    },
    {
      "@id": "ex:org-earth-science-institute",
      "@type": [
        "cdi:Organization"
      ],
      "cdi:organizationName": {
        "@type": [
          "cdi:OrganizationName"
        ],
        "cdi:name": "Earth Science Research Institute",
        "cdi:abbreviation": {
          "@type": [
            "cdi:InternationalString"
          ],
          "cdi:languageSpecificString": {
            "@type": [
              "cdi:LanguageString"
            ],
            "cdi:content": "ESRI",
            "cdi:language": "en"
          }
        },
        "cdi:isFormal": true,
        "cdi:typeOfOrganizationName": {
          "@type": [
            "cdi:ControlledVocabularyEntry"
          ],
          "cdi:entryValue": "legal"
        }
      },
      "cdi:contactInformation": {
        "@type": [
          "cdi:ContactInformation"
        ],
        "cdi:website": {
          "@type": [
            "cdi:WebLink"
          ],
          "cdi:uri": "https://www.esri-example.org",
          "cdi:typeOfWebsite": {
            "@type": [
              "cdi:ControlledVocabularyEntry"
            ],
            "cdi:entryValue": "homepage"
          },
          "cdi:isPreferred": true
        },
        "cdi:address": {
          "@type": [
            "cdi:Address"
          ],
          "cdi:line": [
            "456 Research Boulevard"
          ],
          "cdi:cityPlaceLocal": "Reno",
          "cdi:stateProvince": "Nevada",
          "cdi:postalCode": "89512",
          "cdi:countryCode": {
            "@type": [
              "cdi:ControlledVocabularyEntry"
            ],
            "cdi:entryValue": "US"
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
          "cdi:identifierContent": "https://ror.org/00example",
          "cdi:managingAgency": "ROR"
        }
      }
    },
    {
      "@id": "ex:agent-data-pipeline",
      "@type": [
        "cdi:ProcessingAgent"
      ],
      "cdi:identifier": {
        "@type": [
          "cdi:Identifier"
        ],
        "cdi:nonDdiIdentifier": {
          "@type": [
            "cdi:NonDdiIdentifier"
          ],
          "cdi:identifierContent": "pipeline-agent-v2.1",
          "cdi:managingAgency": "ESRI internal"
        }
      },
      "cdi:purpose": {
        "@type": [
          "cdi:InternationalString"
        ],
        "cdi:languageSpecificString": {
          "@type": [
            "cdi:LanguageString"
          ],
          "cdi:content": "Automated data processing and quality control pipeline",
          "cdi:language": "en"
        }
      },
      "cdi:performs": [
        {
          "@id": "ex:activity-soil-chem-analysis"
        }
      ],
      "cdi:operatesOn": [
        {
          "@id": "ex:env-hpc-cluster"
        }
      ]
    }
  ]
}
```

#### ttl
```ttl
@prefix cdi: <http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/> .
@prefix ex: <https://example.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ex:agent-data-pipeline a cdi:ProcessingAgent ;
    cdi:identifier [ a cdi:Identifier ;
            cdi:nonDdiIdentifier [ a cdi:NonDdiIdentifier ;
                    cdi:identifierContent "pipeline-agent-v2.1" ;
                    cdi:managingAgency "ESRI internal" ] ] ;
    cdi:operatesOn ex:env-hpc-cluster ;
    cdi:performs ex:activity-soil-chem-analysis ;
    cdi:purpose [ a cdi:InternationalString ;
            cdi:languageSpecificString [ a cdi:LanguageString ;
                    cdi:content "Automated data processing and quality control pipeline" ;
                    cdi:language "en" ] ] .

ex:org-earth-science-institute a cdi:Organization ;
    cdi:contactInformation [ a cdi:ContactInformation ;
            cdi:address [ a cdi:Address ;
                    cdi:cityPlaceLocal "Reno" ;
                    cdi:countryCode [ a cdi:ControlledVocabularyEntry ;
                            cdi:entryValue "US" ] ;
                    cdi:line "456 Research Boulevard" ;
                    cdi:postalCode "89512" ;
                    cdi:stateProvince "Nevada" ] ;
            cdi:website [ a cdi:WebLink ;
                    cdi:isPreferred true ;
                    cdi:typeOfWebsite [ a cdi:ControlledVocabularyEntry ;
                            cdi:entryValue "homepage" ] ;
                    cdi:uri "https://www.esri-example.org" ] ] ;
    cdi:identifier [ a cdi:Identifier ;
            cdi:nonDdiIdentifier [ a cdi:NonDdiIdentifier ;
                    cdi:identifierContent "https://ror.org/00example" ;
                    cdi:managingAgency "ROR" ] ] ;
    cdi:organizationName [ a cdi:OrganizationName ;
            cdi:abbreviation [ a cdi:InternationalString ;
                    cdi:languageSpecificString [ a cdi:LanguageString ;
                            cdi:content "ESRI" ;
                            cdi:language "en" ] ] ;
            cdi:isFormal true ;
            cdi:name "Earth Science Research Institute" ;
            cdi:typeOfOrganizationName [ a cdi:ControlledVocabularyEntry ;
                    cdi:entryValue "legal" ] ] .

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
- description: Single agent node
  type: object
  anyOf:
  - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiIndividual/schema.yaml
  - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiMachine/schema.yaml
  - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiOrganization/schema.yaml
  - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiProcessingAgent/schema.yaml
- description: Unwrapped @graph array of agent nodes (OGC pipeline)
  type: array
  items:
    anyOf:
    - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiIndividual/schema.yaml
    - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiMachine/schema.yaml
    - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiOrganization/schema.yaml
    - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiProcessingAgent/schema.yaml
- description: JSON-LD document with @context and @graph
  type: object
  properties:
    '@context': {}
    '@graph':
      type: array
      items:
        anyOf:
        - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiIndividual/schema.yaml
        - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiMachine/schema.yaml
        - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiOrganization/schema.yaml
        - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiProcessingAgent/schema.yaml
  required:
  - '@graph'
x-jsonld-prefixes:
  cdi: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/

```

Links to the schema:

* YAML version: [schema.yaml](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiAgent/schema.json)
* JSON version: [schema.json](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiAgent/schema.yaml)


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
[context.jsonld](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiAgent/context.jsonld)

## Sources

* [DDI-CDI 1.0 Specification](https://ddialliance.org/Specification/DDI-CDI/1.0/)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/Cross-Domain-Interoperability-Framework/metadataBuildingBlocks](https://github.com/Cross-Domain-Interoperability-Framework/metadataBuildingBlocks)
* Path: `_sources/ddiProperties/ddicdiAgent`

