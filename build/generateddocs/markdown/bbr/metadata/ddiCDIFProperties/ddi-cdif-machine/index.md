
# DDI-CDI Machine (Schema)

`cdif.bbr.metadata.ddiCDIFProperties.ddi-cdif-machine` *v0.1*

DDI-CDI Machine agent (software/hardware) with access location, function, and interface specifications. Uses DDI Cross-Domain Integration vocabulary.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

DDI-CDI Machine represents a software or hardware Agent (`cls-Machine`, extends `cdi:Agent`). The root `cdi:Machine` carries `cdi:accessLocation` (a `cdi:AccessLocation` with URI, MIME type, and physical location), `cdi:function` and `cdi:typeOfMachine` (controlled-vocabulary classifications), `cdi:machineInterface` describing the interface type, `cdi:ownerOperatorContact` for the responsible party, and `cdi:name`.

Machine is one of the four agent subtypes composed by `ddicdiAgent`. It captures the systems involved in data production or processing — useful for documenting, e.g., the API endpoint of a service, the model identifier of an instrument, or the package used to run a transformation step.

## Examples

### Minimal Machine
Bare cdi:Machine — schema only requires @type.
#### json
```json
{
  "@context": {
    "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
    "ex": "https://example.org/"
  },
  "@type": ["cdi:Machine"],
  "@id": "ex:software/process-pipeline-v1"
}

```

#### jsonld
```jsonld
{
  "@context": [
    {
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/"
    },
    "https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiCDIFProperties/ddi-cdif-machine/context.jsonld",
    {
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "ex": "https://example.org/"
    }
  ],
  "@type": [
    "cdi:Machine"
  ],
  "@id": "ex:software/process-pipeline-v1"
}
```

#### ttl
```ttl
@prefix cdi: <http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/> .

<https://example.org/software/process-pipeline-v1> a cdi:Machine .


```


### Complete Machine
Machine (HPC cluster) with access location, type classification,
and identifier.
#### json
```json
{
  "@context": {
    "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
    "ex": "https://example.org/"
  },
  "@id": "ex:machine-hpc-cluster",
  "@type": [
    "cdi:Machine"
  ],
  "cdi:name": {
    "@type": [
      "cdi:ObjectName"
    ],
    "cdi:name": "HPC Processing Cluster"
  },
  "cdi:typeOfMachine": {
    "@type": [
      "cdi:ControlledVocabularyEntry"
    ],
    "cdi:entryValue": [
      "high-performance-computing"
    ]
  },
  "cdi:accessLocation": {
    "@type": [
      "cdi:AccessLocation"
    ],
    "cdi:uri": "https://hpc.example.org/api",
    "cdi:physicalLocation": {
      "@type": [
        "cdi:InternationalString"
      ],
      "cdi:languageSpecificString": {
        "@type": [
          "cdi:LanguageString"
        ],
        "cdi:content": "University Data Center, Building 5",
        "cdi:language": "en"
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
      "cdi:identifierContent": "hpc-cluster-001",
      "cdi:managingAgency": "University IT"
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
    "https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiCDIFProperties/ddi-cdif-machine/context.jsonld",
    {
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "ex": "https://example.org/"
    }
  ],
  "@id": "ex:machine-hpc-cluster",
  "@type": [
    "cdi:Machine"
  ],
  "cdi:name": {
    "@type": [
      "cdi:ObjectName"
    ],
    "cdi:name": "HPC Processing Cluster"
  },
  "cdi:typeOfMachine": {
    "@type": [
      "cdi:ControlledVocabularyEntry"
    ],
    "cdi:entryValue": [
      "high-performance-computing"
    ]
  },
  "cdi:accessLocation": {
    "@type": [
      "cdi:AccessLocation"
    ],
    "cdi:uri": "https://hpc.example.org/api",
    "cdi:physicalLocation": {
      "@type": [
        "cdi:InternationalString"
      ],
      "cdi:languageSpecificString": {
        "@type": [
          "cdi:LanguageString"
        ],
        "cdi:content": "University Data Center, Building 5",
        "cdi:language": "en"
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
      "cdi:identifierContent": "hpc-cluster-001",
      "cdi:managingAgency": "University IT"
    }
  }
}
```

#### ttl
```ttl
@prefix cdi: <http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/> .
@prefix ex: <https://example.org/> .

ex:machine-hpc-cluster a cdi:Machine ;
    cdi:accessLocation [ a cdi:AccessLocation ;
            cdi:physicalLocation [ a cdi:InternationalString ;
                    cdi:languageSpecificString [ a cdi:LanguageString ;
                            cdi:content "University Data Center, Building 5" ;
                            cdi:language "en" ] ] ;
            cdi:uri "https://hpc.example.org/api" ] ;
    cdi:identifier [ a cdi:Identifier ;
            cdi:nonDdiIdentifier [ a cdi:NonDdiIdentifier ;
                    cdi:identifierContent "hpc-cluster-001" ;
                    cdi:managingAgency "University IT" ] ] ;
    cdi:name [ a cdi:ObjectName ;
            cdi:name "HPC Processing Cluster" ] ;
    cdi:typeOfMachine [ a cdi:ControlledVocabularyEntry ;
            cdi:entryValue "high-performance-computing" ] .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: DDI-CDI Machine
description: DDI-CDI Machine agent (cls-Machine, extends Agent). Represents software
  or hardware with access location, function, and interface specifications.
type: object
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
    $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiCDIFProperties/ddi-cdif-data-types/schema.yaml#/$defs/AccessLocation
    x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/accessLocation
  cdi:function:
    description: Function performed by this machine
    $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiCDIFProperties/ddi-cdif-data-types/schema.yaml#/$defs/ControlledVocabularyEntry
    x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/function
  cdi:machineInterface:
    description: Interface type for this machine
    $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiCDIFProperties/ddi-cdif-data-types/schema.yaml#/$defs/ControlledVocabularyEntry
    x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/machineInterface
  cdi:name:
    description: Name(s) of this machine
    anyOf:
    - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiCDIFProperties/ddi-cdif-data-types/schema.yaml#/$defs/ObjectName
    - type: array
      items:
        $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiCDIFProperties/ddi-cdif-data-types/schema.yaml#/$defs/ObjectName
    x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/name
  cdi:ownerOperatorContact:
    description: Contact information for the owner or operator
    $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiCDIFProperties/ddi-cdif-data-types/schema.yaml#/$defs/ContactInformation
    x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/ownerOperatorContact
  cdi:typeOfMachine:
    description: Classification of this machine
    $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiCDIFProperties/ddi-cdif-data-types/schema.yaml#/$defs/ControlledVocabularyEntry
    x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/typeOfMachine
  cdi:identifier:
    description: Formal identifier for this agent
    $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiCDIFProperties/ddi-cdif-data-types/schema.yaml#/$defs/Identifier
    x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/identifier
  cdi:image:
    description: Image associated with this agent
    $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiCDIFProperties/ddi-cdif-data-types/schema.yaml#/$defs/PrivateImage
    x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/image
  cdi:purpose:
    description: Purpose or role of this agent
    $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiCDIFProperties/ddi-cdif-data-types/schema.yaml#/$defs/InternationalString
    x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/purpose
required:
- '@type'
x-jsonld-prefixes:
  cdi: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/

```

Links to the schema:

* YAML version: [schema.yaml](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiCDIFProperties/ddi-cdif-machine/schema.json)
* JSON version: [schema.json](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiCDIFProperties/ddi-cdif-machine/schema.yaml)


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
[context.jsonld](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiCDIFProperties/ddi-cdif-machine/context.jsonld)

## Sources

* [DDI-CDI 1.0 Specification](https://ddialliance.org/Specification/DDI-CDI/1.0/)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/Cross-Domain-Interoperability-Framework/metadataBuildingBlocks](https://github.com/Cross-Domain-Interoperability-Framework/metadataBuildingBlocks)
* Path: `_sources/ddiCDIFProperties/ddi-cdif-machine`

