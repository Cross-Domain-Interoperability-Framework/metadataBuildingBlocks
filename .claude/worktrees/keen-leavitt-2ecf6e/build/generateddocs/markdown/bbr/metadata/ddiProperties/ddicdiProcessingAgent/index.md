
# DDI-CDI ProcessingAgent (Schema)

`cdif.bbr.metadata.ddiProperties.ddicdiProcessingAgent` *v0.1*

DDI-CDI ProcessingAgent that orchestrates production activities, linking agents to activities and environments. Uses DDI Cross-Domain Integration vocabulary.

[*Status*](http://www.opengis.net/def/status): Under development

## Examples

### Example DDI-CDI ProcessingAgent.
Demonstrates a ProcessingAgent with activity and environment
references, identifier, and purpose.
#### json
```json
{
  "@context": {
    "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
    "ex": "https://example.org/"
  },
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

```

#### jsonld
```jsonld
{
  "@context": [
    {
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/"
    },
    "https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiProcessingAgent/context.jsonld",
    {
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "ex": "https://example.org/"
    }
  ],
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
```

#### ttl
```ttl
@prefix cdi: <http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/> .
@prefix ex: <https://example.org/> .

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


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: DDI-CDI ProcessingAgent
description: DDI-CDI ProcessingAgent (cls-ProcessingAgent, extends Agent). Orchestrates
  production activities, linking agents to the activities they perform and environments
  they operate on.
type: object
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
      $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/id-reference
  cdi:operatesOn:
    description: Production environments this agent operates on (cdi:ProductionEnvironment)
    type: array
    items:
      $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/id-reference
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

* YAML version: [schema.yaml](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiProcessingAgent/schema.json)
* JSON version: [schema.json](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiProcessingAgent/schema.yaml)


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
[context.jsonld](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiProcessingAgent/context.jsonld)

## Sources

* [DDI-CDI 1.0 Specification](https://ddialliance.org/Specification/DDI-CDI/1.0/)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/Cross-Domain-Interoperability-Framework/metadataBuildingBlocks](https://github.com/Cross-Domain-Interoperability-Framework/metadataBuildingBlocks)
* Path: `_sources/ddiProperties/ddicdiProcessingAgent`

