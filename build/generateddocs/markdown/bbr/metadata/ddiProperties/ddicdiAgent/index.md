
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
          "cdi:line": "456 Research Boulevard",
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
          "cdi:line": "456 Research Boulevard",
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
  using DDI Cross-Domain Integration vocabulary.
anyOf:
- description: Single graph node (Individual, Machine, Organization, or ProcessingAgent)
  type: object
  anyOf:
  - $ref: '#/$defs/Individual'
  - $ref: '#/$defs/Machine'
  - $ref: '#/$defs/Organization'
  - $ref: '#/$defs/ProcessingAgent'
- description: Unwrapped @graph array of nodes
  type: array
  items:
    anyOf:
    - $ref: '#/$defs/Individual'
    - $ref: '#/$defs/Machine'
    - $ref: '#/$defs/Organization'
    - $ref: '#/$defs/ProcessingAgent'
- description: JSON-LD document with @context and @graph
  type: object
  properties:
    '@context': {}
    '@graph':
      type: array
      items:
        anyOf:
        - $ref: '#/$defs/Individual'
        - $ref: '#/$defs/Machine'
        - $ref: '#/$defs/Organization'
        - $ref: '#/$defs/ProcessingAgent'
  required:
  - '@graph'
$defs:
  Individual:
    type: object
    description: DDI-CDI Individual agent (cls-Individual, extends Agent). Represents
      a person.
    properties:
      '@type':
        type: array
        items:
          type: string
        contains:
          const: cdi:Individual
        minItems: 1
      '@id':
        type: string
        description: Identifier for this individual node
      cdi:individualName:
        description: Name(s) of this individual
        anyOf:
        - $ref: '#/$defs/IndividualName'
        - type: array
          items:
            $ref: '#/$defs/IndividualName'
      cdi:contactInformation:
        description: Contact details for this individual
        anyOf:
        - $ref: '#/$defs/ContactInformation'
        - type: array
          items:
            $ref: '#/$defs/ContactInformation'
      cdi:catalogDetails:
        description: Catalog metadata for this agent
        $ref: '#/$defs/CatalogDetails'
      cdi:identifier:
        description: Formal identifier for this agent
        $ref: '#/$defs/Identifier'
      cdi:image:
        description: Image associated with this agent
        $ref: '#/$defs/PrivateImage'
      cdi:purpose:
        description: Purpose or role of this agent
        $ref: '#/$defs/InternationalString'
    required:
    - '@type'
  Machine:
    type: object
    description: DDI-CDI Machine agent (cls-Machine, extends Agent). Represents software
      or hardware.
    properties:
      '@type':
        type: array
        items:
          type: string
        contains:
          const: cdi:Machine
        minItems: 1
      '@id':
        type: string
        description: Identifier for this machine node
      cdi:accessLocation:
        description: Network or physical access point for this machine
        $ref: '#/$defs/AccessLocation'
      cdi:function:
        description: Function performed by this machine
        $ref: '#/$defs/ControlledVocabularyEntry'
      cdi:machineInterface:
        description: Interface type for this machine
        $ref: '#/$defs/ControlledVocabularyEntry'
      cdi:name:
        description: Name(s) of this machine
        anyOf:
        - $ref: '#/$defs/ObjectName'
        - type: array
          items:
            $ref: '#/$defs/ObjectName'
      cdi:ownerOperatorContact:
        description: Contact information for the owner or operator
        $ref: '#/$defs/ContactInformation'
      cdi:typeOfMachine:
        description: Classification of this machine
        $ref: '#/$defs/ControlledVocabularyEntry'
      cdi:catalogDetails:
        description: Catalog metadata for this agent
        $ref: '#/$defs/CatalogDetails'
      cdi:identifier:
        description: Formal identifier for this agent
        $ref: '#/$defs/Identifier'
      cdi:image:
        description: Image associated with this agent
        $ref: '#/$defs/PrivateImage'
      cdi:purpose:
        description: Purpose or role of this agent
        $ref: '#/$defs/InternationalString'
    required:
    - '@type'
  Organization:
    type: object
    description: DDI-CDI Organization agent (cls-Organization, extends Agent). Represents
      a group or institution.
    properties:
      '@type':
        type: array
        items:
          type: string
        contains:
          const: cdi:Organization
        minItems: 1
      '@id':
        type: string
        description: Identifier for this organization node
      cdi:organizationName:
        description: Name(s) of this organization
        anyOf:
        - $ref: '#/$defs/OrganizationName'
        - type: array
          items:
            $ref: '#/$defs/OrganizationName'
      cdi:contactInformation:
        description: Contact details for this organization
        anyOf:
        - $ref: '#/$defs/ContactInformation'
        - type: array
          items:
            $ref: '#/$defs/ContactInformation'
      cdi:catalogDetails:
        description: Catalog metadata for this agent
        $ref: '#/$defs/CatalogDetails'
      cdi:identifier:
        description: Formal identifier for this agent
        $ref: '#/$defs/Identifier'
      cdi:image:
        description: Image associated with this agent
        $ref: '#/$defs/PrivateImage'
      cdi:purpose:
        description: Purpose or role of this agent
        $ref: '#/$defs/InternationalString'
    required:
    - '@type'
  ProcessingAgent:
    type: object
    description: DDI-CDI ProcessingAgent (cls-ProcessingAgent, extends Agent). Orchestrates
      production activities.
    properties:
      '@type':
        type: array
        items:
          type: string
        contains:
          const: cdi:ProcessingAgent
        minItems: 1
      '@id':
        type: string
        description: Identifier for this processing agent node
      cdi:performs:
        description: Activities this agent performs (cdi:Activity). Use @id references
          to Activity nodes defined elsewhere in the graph.
        type: array
        items:
          $ref: '#/$defs/id-reference'
      cdi:operatesOn:
        description: Production environments this agent operates on (cdi:ProductionEnvironment)
        type: array
        items:
          $ref: '#/$defs/id-reference'
      cdi:catalogDetails:
        description: Catalog metadata for this agent
        $ref: '#/$defs/CatalogDetails'
      cdi:identifier:
        description: Formal identifier for this agent
        $ref: '#/$defs/Identifier'
      cdi:image:
        description: Image associated with this agent
        $ref: '#/$defs/PrivateImage'
      cdi:purpose:
        description: Purpose or role of this agent
        $ref: '#/$defs/InternationalString'
    required:
    - '@type'
  id-reference:
    type: object
    description: JSON-LD @id reference to a node defined elsewhere in the graph
    properties:
      '@id':
        type: string
        description: IRI or blank node identifier of the referenced node
    required:
    - '@id'
  ObjectName:
    type: object
    description: DDI-CDI structured name wrapper (dt-ObjectName)
    properties:
      '@type':
        type: array
        items:
          type: string
        contains:
          const: cdi:ObjectName
        minItems: 1
      cdi:name:
        type: string
        description: The name string
      cdi:context:
        description: Context or usage of this name
        $ref: '#/$defs/ControlledVocabularyEntry'
    required:
    - cdi:name
  OrganizationName:
    type: object
    description: DDI-CDI organization name (dt-OrganizationName, extends ObjectName)
    properties:
      '@type':
        type: array
        items:
          type: string
        contains:
          const: cdi:OrganizationName
        minItems: 1
      cdi:name:
        type: string
        description: The name string
      cdi:context:
        description: Context or usage of this name
        $ref: '#/$defs/ControlledVocabularyEntry'
      cdi:abbreviation:
        description: Abbreviated form of the name
        $ref: '#/$defs/InternationalString'
      cdi:effectiveDates:
        description: Date range when this name is/was effective
        $ref: '#/$defs/DateRange'
      cdi:isFormal:
        type: boolean
        default: true
        description: Whether this is the formal/legal name
      cdi:typeOfOrganizationName:
        description: Classification of this name (e.g. legal, trade, acronym)
        $ref: '#/$defs/ControlledVocabularyEntry'
    required:
    - cdi:name
  IndividualName:
    type: object
    description: DDI-CDI individual name (dt-IndividualName)
    properties:
      '@type':
        type: array
        items:
          type: string
        contains:
          const: cdi:IndividualName
        minItems: 1
      cdi:firstGiven:
        type: string
        description: First or given name
      cdi:lastFamily:
        type: string
        description: Last or family name
      cdi:middle:
        type: string
        description: Middle name(s)
      cdi:prefix:
        type: string
        description: Name prefix (e.g. Dr., Prof.)
      cdi:suffix:
        type: string
        description: Name suffix (e.g. Jr., III)
      cdi:fullName:
        description: Full name as a single internationalized string
        $ref: '#/$defs/InternationalString'
      cdi:abbreviation:
        description: Abbreviated form of the name
        $ref: '#/$defs/InternationalString'
      cdi:isFormal:
        type: boolean
        default: true
        description: Whether this is a formal name
      cdi:isPreferred:
        type: boolean
        default: false
        description: Whether this is the preferred name
      cdi:effectiveDates:
        description: Date range when this name is/was effective
        $ref: '#/$defs/DateRange'
      cdi:context:
        description: Context or usage of this name
        $ref: '#/$defs/ControlledVocabularyEntry'
      cdi:typeOfIndividualName:
        description: Classification of this name (e.g. birth, married, pen)
        $ref: '#/$defs/ControlledVocabularyEntry'
      cdi:sex:
        description: Sex specification associated with this name
        $ref: '#/$defs/SexSpecification'
  SexSpecification:
    type: object
    description: DDI-CDI sex specification (dt-SexSpecification)
    properties:
      '@type':
        type: array
        items:
          type: string
        contains:
          const: cdi:SexSpecification
        minItems: 1
      cdi:sexCode:
        type: string
        description: Code identifying sex (e.g. ISO 5218 values)
  ContactInformation:
    type: object
    description: DDI-CDI contact information (dt-ContactInformation)
    properties:
      '@type':
        type: array
        items:
          type: string
        contains:
          const: cdi:ContactInformation
        minItems: 1
      cdi:address:
        description: Postal address(es)
        anyOf:
        - $ref: '#/$defs/Address'
        - type: array
          items:
            $ref: '#/$defs/Address'
      cdi:email:
        description: Email address(es)
        anyOf:
        - $ref: '#/$defs/Email'
        - type: array
          items:
            $ref: '#/$defs/Email'
      cdi:emessaging:
        description: Electronic messaging contact(s)
        anyOf:
        - $ref: '#/$defs/ElectronicMessageSystem'
        - type: array
          items:
            $ref: '#/$defs/ElectronicMessageSystem'
      cdi:telephone:
        description: Telephone number(s)
        anyOf:
        - $ref: '#/$defs/Telephone'
        - type: array
          items:
            $ref: '#/$defs/Telephone'
      cdi:website:
        description: Website link(s)
        anyOf:
        - $ref: '#/$defs/WebLink'
        - type: array
          items:
            $ref: '#/$defs/WebLink'
  Address:
    type: object
    description: DDI-CDI postal address (dt-Address)
    properties:
      '@type':
        type: array
        items:
          type: string
        contains:
          const: cdi:Address
        minItems: 1
      cdi:line:
        description: Address line(s)
        anyOf:
        - type: string
        - type: array
          items:
            type: string
      cdi:cityPlaceLocal:
        type: string
        description: City, town, or locality
      cdi:stateProvince:
        type: string
        description: State, province, or region
      cdi:postalCode:
        type: string
        description: Postal or ZIP code
      cdi:countryCode:
        description: Country code
        $ref: '#/$defs/ControlledVocabularyEntry'
      cdi:typeOfAddress:
        description: Type of address (e.g. home, work, mailing)
        $ref: '#/$defs/ControlledVocabularyEntry'
      cdi:isPreferred:
        type: boolean
        default: false
        description: Whether this is the preferred address
  Email:
    type: object
    description: DDI-CDI email address (dt-Email)
    properties:
      '@type':
        type: array
        items:
          type: string
        contains:
          const: cdi:Email
        minItems: 1
      cdi:internetEmail:
        type: string
        description: Email address string
      cdi:typeOfEmail:
        description: Type of email (e.g. personal, work)
        $ref: '#/$defs/ControlledVocabularyEntry'
      cdi:isPreferred:
        type: boolean
        default: false
        description: Whether this is the preferred email
  Telephone:
    type: object
    description: DDI-CDI telephone number (dt-Telephone)
    properties:
      '@type':
        type: array
        items:
          type: string
        contains:
          const: cdi:Telephone
        minItems: 1
      cdi:telephoneNumber:
        type: string
        description: Telephone number string
      cdi:typeOfTelephone:
        description: Type of telephone (e.g. mobile, office, fax)
        $ref: '#/$defs/ControlledVocabularyEntry'
      cdi:isPreferred:
        type: boolean
        default: false
        description: Whether this is the preferred telephone
  WebLink:
    type: object
    description: DDI-CDI website link (dt-WebLink)
    properties:
      '@type':
        type: array
        items:
          type: string
        contains:
          const: cdi:WebLink
        minItems: 1
      cdi:uri:
        type: string
        format: uri
        description: URI of the website
      cdi:typeOfWebsite:
        description: Type of website (e.g. homepage, documentation)
        $ref: '#/$defs/ControlledVocabularyEntry'
      cdi:isPreferred:
        type: boolean
        default: false
        description: Whether this is the preferred website
  ElectronicMessageSystem:
    type: object
    description: DDI-CDI electronic messaging system contact (dt-ElectronicMessageSystem)
    properties:
      '@type':
        type: array
        items:
          type: string
        contains:
          const: cdi:ElectronicMessageSystem
        minItems: 1
      cdi:contactAddress:
        type: string
        description: Messaging address or handle
      cdi:typeOfService:
        description: Type of messaging service (e.g. Slack, Teams)
        $ref: '#/$defs/ControlledVocabularyEntry'
      cdi:isPreferred:
        type: boolean
        default: false
        description: Whether this is the preferred messaging service
  AccessLocation:
    type: object
    description: DDI-CDI access location for a machine (dt-AccessLocation)
    properties:
      '@type':
        type: array
        items:
          type: string
        contains:
          const: cdi:AccessLocation
        minItems: 1
      cdi:uri:
        type: string
        format: uri
        description: URI of the access endpoint
      cdi:mimeType:
        description: MIME type of the resource at this location
        $ref: '#/$defs/ControlledVocabularyEntry'
      cdi:physicalLocation:
        description: Physical location description
        $ref: '#/$defs/InternationalString'
  PrivateImage:
    type: object
    description: DDI-CDI private image (dt-PrivateImage)
    properties:
      '@type':
        type: array
        items:
          type: string
        contains:
          const: cdi:PrivateImage
        minItems: 1
      cdi:effectiveDates:
        description: Date range when this image is effective
        $ref: '#/$defs/DateRange'
      cdi:privacy:
        description: Privacy classification
        $ref: '#/$defs/ControlledVocabularyEntry'
  CatalogDetails:
    type: object
    description: DDI-CDI catalog details (dt-CatalogDetails)
    properties:
      '@type':
        type: array
        items:
          type: string
        contains:
          const: cdi:CatalogDetails
        minItems: 1
      cdi:title:
        description: Title for the catalog entry
        $ref: '#/$defs/InternationalString'
      cdi:summary:
        description: Summary description
        $ref: '#/$defs/InternationalString'
      cdi:identifier:
        description: Catalog identifier
        type: object
        properties:
          cdi:identifierContent:
            type: string
          cdi:isUri:
            type: boolean
      cdi:creator:
        description: Creator of the catalog entry
        $ref: '#/$defs/AgentInRole'
  AgentInRole:
    type: object
    description: DDI-CDI agent in a role (dt-AgentInRole)
    properties:
      '@type':
        type: array
        items:
          type: string
        contains:
          const: cdi:AgentInRole
        minItems: 1
      cdi:agentName:
        description: Name of the agent
        $ref: '#/$defs/InternationalString'
      cdi:reference:
        description: Reference to the agent entity
        $ref: '#/$defs/Reference'
      cdi:role:
        description: Role of the agent
        $ref: '#/$defs/ControlledVocabularyEntry'
  Identifier:
    type: object
    description: DDI-CDI composite identifier (dt-Identifier)
    properties:
      '@type':
        type: array
        items:
          type: string
        contains:
          const: cdi:Identifier
        minItems: 1
      cdi:ddiIdentifier:
        description: DDI-specific IRDI identifier
        $ref: '#/$defs/InternationalRegistrationDataIdentifier'
      cdi:uri:
        type: string
        format: uri
        description: URI form of the identifier
      cdi:nonDdiIdentifier:
        description: Non-DDI identifier
        anyOf:
        - $ref: '#/$defs/NonDdiIdentifier'
        - type: array
          items:
            $ref: '#/$defs/NonDdiIdentifier'
  InternationalRegistrationDataIdentifier:
    type: object
    description: DDI-CDI IRDI (dt-InternationalRegistrationDataIdentifier)
    properties:
      '@type':
        type: array
        items:
          type: string
        contains:
          const: cdi:InternationalRegistrationDataIdentifier
        minItems: 1
      cdi:dataIdentifier:
        type: string
      cdi:registrationAuthorityIdentifier:
        type: string
      cdi:versionIdentifier:
        type: string
    required:
    - cdi:dataIdentifier
    - cdi:registrationAuthorityIdentifier
    - cdi:versionIdentifier
  NonDdiIdentifier:
    type: object
    description: Non-DDI identifier (dt-NonDdiIdentifier)
    properties:
      '@type':
        type: array
        items:
          type: string
        contains:
          const: cdi:NonDdiIdentifier
        minItems: 1
      cdi:identifierContent:
        type: string
        description: The identifier value
      cdi:managingAgency:
        type: string
        description: Agency managing this identifier scheme
    required:
    - cdi:identifierContent
  Reference:
    type: object
    description: DDI-CDI reference to an entity (dt-Reference)
    properties:
      '@type':
        type: array
        items:
          type: string
        contains:
          const: cdi:Reference
        minItems: 1
      cdi:uri:
        type: string
        format: uri
        description: URI of the referenced entity
      cdi:description:
        type: string
        description: Human-readable description of the reference
      cdi:ddiReference:
        description: DDI IRDI reference
        $ref: '#/$defs/InternationalRegistrationDataIdentifier'
      cdi:semantic:
        description: Semantic role of this reference
        $ref: '#/$defs/ControlledVocabularyEntry'
  ControlledVocabularyEntry:
    type: object
    description: DDI-CDI controlled vocabulary entry (dt-ControlledVocabularyEntry)
    properties:
      '@type':
        type: array
        items:
          type: string
        contains:
          const: cdi:ControlledVocabularyEntry
        minItems: 1
      cdi:entryValue:
        type: string
        description: The vocabulary code or value
      cdi:name:
        type: string
        description: Human-readable name
      cdi:vocabulary:
        description: Reference to the vocabulary scheme
        $ref: '#/$defs/Reference'
  InternationalString:
    type: object
    description: DDI-CDI internationalized string (dt-InternationalString)
    properties:
      '@type':
        type: array
        items:
          type: string
        contains:
          const: cdi:InternationalString
        minItems: 1
      cdi:languageSpecificString:
        description: Language-tagged string value(s)
        anyOf:
        - $ref: '#/$defs/LanguageString'
        - type: array
          items:
            $ref: '#/$defs/LanguageString'
  LanguageString:
    type: object
    description: DDI-CDI language-tagged string (dt-LanguageString)
    properties:
      '@type':
        type: array
        items:
          type: string
        contains:
          const: cdi:LanguageString
        minItems: 1
      cdi:content:
        type: string
        description: The text content
      cdi:language:
        type: string
        description: ISO language code (e.g. en, fr, de)
    required:
    - cdi:content
  DateRange:
    type: object
    description: DDI-CDI date range (dt-DateRange)
    properties:
      '@type':
        type: array
        items:
          type: string
        contains:
          const: cdi:DateRange
        minItems: 1
      cdi:startDate:
        description: Start date of the range
        $ref: '#/$defs/CombinedDate'
      cdi:endDate:
        description: End date of the range
        $ref: '#/$defs/CombinedDate'
  CombinedDate:
    type: object
    description: DDI-CDI combined date (dt-CombinedDate)
    properties:
      '@type':
        type: array
        items:
          type: string
        contains:
          const: cdi:CombinedDate
        minItems: 1
      cdi:isoDate:
        type: string
        format: date-time
        description: ISO 8601 date-time value
      cdi:historicDate:
        type: string
        description: Free-text historic date
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

