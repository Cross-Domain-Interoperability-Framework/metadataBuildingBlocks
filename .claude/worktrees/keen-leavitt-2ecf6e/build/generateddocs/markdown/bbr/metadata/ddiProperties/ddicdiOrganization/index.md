
# DDI-CDI Organization (Schema)

`cdif.bbr.metadata.ddiProperties.ddicdiOrganization` *v0.1*

DDI-CDI Organization agent (group/institution) with structured name, contact information, and identification. Uses DDI Cross-Domain Integration vocabulary.

[*Status*](http://www.opengis.net/def/status): Under development

## Examples

### Example DDI-CDI Organization agent.
Demonstrates an Organization with structured name,
website contact, and ROR identifier.
#### json
```json
{
  "@context": {
    "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
    "ex": "https://example.org/"
  },
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
    "cdi:isFormal": true
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
      "cdi:identifierContent": "https://ror.org/00example",
      "cdi:managingAgency": "ROR"
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
    "https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiOrganization/context.jsonld",
    {
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "ex": "https://example.org/"
    }
  ],
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
    "cdi:isFormal": true
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
      "cdi:identifierContent": "https://ror.org/00example",
      "cdi:managingAgency": "ROR"
    }
  }
}
```

#### ttl
```ttl
@prefix cdi: <http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/> .
@prefix ex: <https://example.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ex:org-earth-science-institute a cdi:Organization ;
    cdi:contactInformation [ a cdi:ContactInformation ;
            cdi:website [ a cdi:WebLink ;
                    cdi:isPreferred true ;
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
            cdi:name "Earth Science Research Institute" ] .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: DDI-CDI Organization
description: DDI-CDI Organization agent (cls-Organization, extends Agent). Represents
  a group or institution with structured name, contact information, and identification.
type: object
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
    - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/OrganizationName
    - type: array
      items:
        $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/OrganizationName
  cdi:contactInformation:
    description: Contact details for this organization
    anyOf:
    - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/ContactInformation
    - type: array
      items:
        $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/ContactInformation
  cdi:catalogDetails:
    description: Catalog metadata for this agent
    $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/CatalogDetails
  cdi:identifier:
    description: Formal identifier for this agent
    $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/Identifier
  cdi:image:
    description: Image associated with this agent
    $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/PrivateImage
  cdi:purpose:
    description: Purpose or role of this agent
    $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/InternationalString
required:
- '@type'
x-jsonld-prefixes:
  cdi: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/

```

Links to the schema:

* YAML version: [schema.yaml](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiOrganization/schema.json)
* JSON version: [schema.json](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiOrganization/schema.yaml)


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
[context.jsonld](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiOrganization/context.jsonld)

## Sources

* [DDI-CDI 1.0 Specification](https://ddialliance.org/Specification/DDI-CDI/1.0/)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/Cross-Domain-Interoperability-Framework/metadataBuildingBlocks](https://github.com/Cross-Domain-Interoperability-Framework/metadataBuildingBlocks)
* Path: `_sources/ddiProperties/ddicdiOrganization`

