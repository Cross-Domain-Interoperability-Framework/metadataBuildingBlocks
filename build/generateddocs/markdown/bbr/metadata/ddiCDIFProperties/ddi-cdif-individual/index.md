
# DDI-CDI Individual (Schema)

`cdif.bbr.metadata.ddiCDIFProperties.ddi-cdif-individual` *v0.1*

DDI-CDI Individual agent (person) with structured name, contact information, and identification. Uses DDI Cross-Domain Integration vocabulary.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

DDI-CDI Individual represents a person as an Agent (`cls-Individual`, extends `cdi:Agent`). The root `cdi:Individual` carries `cdi:individualName` (one or more `IndividualName` records), `cdi:contactInformation` for postal, email, telephone, messaging, and web contacts, plus the agent-shared properties `cdi:identifier`, `cdi:image`, and `cdi:purpose`.

Individual is one of the four concrete agent types composed by `ddicdiAgent`; alongside `ddicdiOrganization`, `ddicdiMachine`, and `ddicdiProcessingAgent` it covers the people involved in producing, maintaining, or using the data being described.

## Examples

### Minimal Individual
Bare cdi:Individual — schema only requires @type.
#### json
```json
{
  "@context": {
    "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
    "ex": "https://example.org/"
  },
  "@type": ["cdi:Individual"],
  "@id": "ex:person/jane-doe"
}

```

#### jsonld
```jsonld
{
  "@context": [
    {
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/"
    },
    "https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiCDIFProperties/ddi-cdif-individual/context.jsonld",
    {
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "ex": "https://example.org/"
    }
  ],
  "@type": [
    "cdi:Individual"
  ],
  "@id": "ex:person/jane-doe"
}
```

#### ttl
```ttl
@prefix cdi: <http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/> .

<https://example.org/person/jane-doe> a cdi:Individual .


```


### Complete Individual
Individual (person) with structured name, contact information,
and ORCID identifier.
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
    "https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiCDIFProperties/ddi-cdif-individual/context.jsonld",
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
title: DDI-CDI Individual
description: DDI-CDI Individual agent (cls-Individual, extends Agent). Represents
  a person with name, contact information, and identification.
type: object
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
    - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiCDIFProperties/ddi-cdif-data-types/schema.yaml#/$defs/IndividualName
    - type: array
      items:
        $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiCDIFProperties/ddi-cdif-data-types/schema.yaml#/$defs/IndividualName
  cdi:contactInformation:
    description: Contact details for this individual
    anyOf:
    - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiCDIFProperties/ddi-cdif-data-types/schema.yaml#/$defs/ContactInformation
    - type: array
      items:
        $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiCDIFProperties/ddi-cdif-data-types/schema.yaml#/$defs/ContactInformation
  cdi:identifier:
    description: Formal identifier for this agent
    $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiCDIFProperties/ddi-cdif-data-types/schema.yaml#/$defs/Identifier
  cdi:image:
    description: Image associated with this agent
    $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiCDIFProperties/ddi-cdif-data-types/schema.yaml#/$defs/PrivateImage
  cdi:purpose:
    description: Purpose or role of this agent
    $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiCDIFProperties/ddi-cdif-data-types/schema.yaml#/$defs/InternationalString
required:
- '@type'
x-jsonld-prefixes:
  cdi: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/

```

Links to the schema:

* YAML version: [schema.yaml](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiCDIFProperties/ddi-cdif-individual/schema.json)
* JSON version: [schema.json](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiCDIFProperties/ddi-cdif-individual/schema.yaml)


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
[context.jsonld](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiCDIFProperties/ddi-cdif-individual/context.jsonld)

## Sources

* [DDI-CDI 1.0 Specification](https://ddialliance.org/Specification/DDI-CDI/1.0/)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/Cross-Domain-Interoperability-Framework/metadataBuildingBlocks](https://github.com/Cross-Domain-Interoperability-Framework/metadataBuildingBlocks)
* Path: `_sources/ddiCDIFProperties/ddi-cdif-individual`

