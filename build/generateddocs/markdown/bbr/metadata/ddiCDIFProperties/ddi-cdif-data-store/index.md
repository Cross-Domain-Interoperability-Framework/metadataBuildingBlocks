
# DDI-CDI Data Store (Schema)

`cdif.bbr.metadata.ddiCDIFProperties.ddi-cdif-data-store` *v0.1*

Collection of logical records.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

DDI-CDI DataStore models a collection of logical records held together as a managed datastore (delimited file, fixed-record-length file, relational database, etc.). The root `cdi:DataStore` carries `cdi:has_LogicalRecord` (members from the `ddicdiLogicalRecord` BB), `cdi:has_LogicalRecordPosition` to order them, optional `cdi:has_RecordRelation` describing relationships across records, and characterization properties `cdi:dataStoreType`, `cdi:characterSet`, `cdi:recordCount`, and `cdi:aboutMissing`.

Cross-record linkage is expressed through the local `$defs/RecordRelation` and `$defs/InstanceVariableMap` constructs, which capture key relationships between source and target instance variables along with a `CorrespondenceDefinition` describing how they match. DataStore is the top-level container that ties together the structural-description side of the CDIF Data Description profile.

## Examples

### Minimal DataStore
DataStore with the required @type, cdi:name, and one cdi:has_LogicalRecord
by @id reference.
#### json
```json
{
  "@context": {
    "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
    "ex": "https://example.org/"
  },
  "@type": ["cdi:DataStore"],
  "@id": "ex:datastore/observations",
  "cdi:name": [
    {
      "@type": ["cdi:ObjectName"],
      "cdi:name": "Observations data store"
    }
  ],
  "cdi:has_LogicalRecord": [
    { "@id": "ex:logical-record/observations" }
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
    "https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiCDIFProperties/ddi-cdif-data-store/context.jsonld",
    {
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "ex": "https://example.org/"
    }
  ],
  "@type": [
    "cdi:DataStore"
  ],
  "@id": "ex:datastore/observations",
  "cdi:name": [
    {
      "@type": [
        "cdi:ObjectName"
      ],
      "cdi:name": "Observations data store"
    }
  ],
  "cdi:has_LogicalRecord": [
    {
      "@id": "ex:logical-record/observations"
    }
  ]
}
```

#### ttl
```ttl
@prefix cdi: <http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/> .

<https://example.org/datastore/observations> a cdi:DataStore ;
    cdi:has_LogicalRecord <https://example.org/logical-record/observations> ;
    cdi:name [ a cdi:ObjectName ;
            cdi:name "Observations data store" ] .


```


### Complete DataStore
Clinical observations DataStore exercising every property: cdi:identifier,
cdi:characterSet, cdi:dataStoreType (with full ControlledVocabularyEntry),
cdi:purpose (InternationalString), cdi:recordCount, and multiple
cdi:has_LogicalRecord entries.
#### json
```json
{
  "@context": {
    "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
    "ex": "https://example.org/"
  },
  "@type": ["cdi:DataStore"],
  "@id": "ex:datastore/clinical-2026",
  "cdi:identifier": {
    "@type": ["cdi:Identifier"],
    "cdi:uri": "https://example.org/datastore/clinical-2026"
  },
  "cdi:name": [
    {
      "@type": ["cdi:ObjectName"],
      "cdi:name": "Clinical observations 2026"
    }
  ],
  "cdi:characterSet": "UTF-8",
  "cdi:dataStoreType": {
    "@type": ["cdi:ControlledVocabularyEntry"],
    "cdi:name": "DDI-CDI DataStoreType vocabulary",
    "cdi:vocabulary": {
      "@type": ["cdi:Reference"],
      "cdi:uri": "https://ddialliance.org/Specification/DDI-CDI/1.0/CV/DataStoreType",
      "cdi:description": "Controlled vocabulary of DDI-CDI data store types."
    },
    "cdi:entryReference": [
      {
        "@type": ["cdi:Reference"],
        "cdi:uri": "https://ddialliance.org/Specification/DDI-CDI/1.0/CV/DataStoreType/DelimitedFile"
      }
    ],
    "cdi:entryValue": ["DelimitedFile"]
  },
  "cdi:purpose": {
    "@type": ["cdi:InternationalString"],
    "cdi:languageSpecificString": [
      {
        "@type": ["cdi:LanguageString"],
        "cdi:content": "Longitudinal clinical observations for the 2026 cohort.",
        "cdi:language": "en"
      }
    ]
  },
  "cdi:recordCount": 12450,
  "cdi:has_LogicalRecord": [
    { "@id": "ex:logical-record/visits" },
    { "@id": "ex:logical-record/lab-results" }
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
    "https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiCDIFProperties/ddi-cdif-data-store/context.jsonld",
    {
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "ex": "https://example.org/"
    }
  ],
  "@type": [
    "cdi:DataStore"
  ],
  "@id": "ex:datastore/clinical-2026",
  "cdi:identifier": {
    "@type": [
      "cdi:Identifier"
    ],
    "cdi:uri": "https://example.org/datastore/clinical-2026"
  },
  "cdi:name": [
    {
      "@type": [
        "cdi:ObjectName"
      ],
      "cdi:name": "Clinical observations 2026"
    }
  ],
  "cdi:characterSet": "UTF-8",
  "cdi:dataStoreType": {
    "@type": [
      "cdi:ControlledVocabularyEntry"
    ],
    "cdi:name": "DDI-CDI DataStoreType vocabulary",
    "cdi:vocabulary": {
      "@type": [
        "cdi:Reference"
      ],
      "cdi:uri": "https://ddialliance.org/Specification/DDI-CDI/1.0/CV/DataStoreType",
      "cdi:description": "Controlled vocabulary of DDI-CDI data store types."
    },
    "cdi:entryReference": [
      {
        "@type": [
          "cdi:Reference"
        ],
        "cdi:uri": "https://ddialliance.org/Specification/DDI-CDI/1.0/CV/DataStoreType/DelimitedFile"
      }
    ],
    "cdi:entryValue": [
      "DelimitedFile"
    ]
  },
  "cdi:purpose": {
    "@type": [
      "cdi:InternationalString"
    ],
    "cdi:languageSpecificString": [
      {
        "@type": [
          "cdi:LanguageString"
        ],
        "cdi:content": "Longitudinal clinical observations for the 2026 cohort.",
        "cdi:language": "en"
      }
    ]
  },
  "cdi:recordCount": 12450,
  "cdi:has_LogicalRecord": [
    {
      "@id": "ex:logical-record/visits"
    },
    {
      "@id": "ex:logical-record/lab-results"
    }
  ]
}
```

#### ttl
```ttl
@prefix cdi: <http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<https://example.org/datastore/clinical-2026> a cdi:DataStore ;
    cdi:characterSet "UTF-8" ;
    cdi:dataStoreType [ a cdi:ControlledVocabularyEntry ;
            cdi:entryReference [ a cdi:Reference ;
                    cdi:uri "https://ddialliance.org/Specification/DDI-CDI/1.0/CV/DataStoreType/DelimitedFile" ] ;
            cdi:entryValue "DelimitedFile" ;
            cdi:name "DDI-CDI DataStoreType vocabulary" ;
            cdi:vocabulary [ a cdi:Reference ;
                    cdi:description "Controlled vocabulary of DDI-CDI data store types." ;
                    cdi:uri "https://ddialliance.org/Specification/DDI-CDI/1.0/CV/DataStoreType" ] ] ;
    cdi:has_LogicalRecord <https://example.org/logical-record/lab-results>,
        <https://example.org/logical-record/visits> ;
    cdi:identifier [ a cdi:Identifier ;
            cdi:uri "https://example.org/datastore/clinical-2026" ] ;
    cdi:name [ a cdi:ObjectName ;
            cdi:name "Clinical observations 2026" ] ;
    cdi:purpose [ a cdi:InternationalString ;
            cdi:languageSpecificString [ a cdi:LanguageString ;
                    cdi:content "Longitudinal clinical observations for the 2026 cohort." ;
                    cdi:language "en" ] ] ;
    cdi:recordCount 12450 .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: DDI-CDI Data Store
description: Collection of logical records. This represents a queryable service.
type: object
properties:
  '@type':
    type: array
    items:
      type: string
    contains:
      allOf:
      - const: cdi:DataStore
    minItems: 1
  '@id':
    type: string
    description: Identifier for this DataStore node
  cdi:characterSet:
    type: string
    description: Default character set used in the Data Store.
  cdi:dataStoreType:
    $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiCDIFProperties/ddi-cdif-data-types/schema.yaml#/$defs/ControlledVocabularyEntry
    description: The type of datastore. Could be delimited file, fixed record length
      file, relational database, etc. Points to an external definition which can be
      part of a controlled vocabulary maintained by the DDI Alliance.
  cdi:identifier:
    $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiCDIFProperties/ddi-cdif-data-types/schema.yaml#/$defs/Identifier
    description: Identifier for objects requiring short- or long-lasting referencing
      and management.
  cdi:name:
    type: array
    items:
      $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiCDIFProperties/ddi-cdif-data-types/schema.yaml#/$defs/ObjectName
    minItems: 1
    description: a string assigning a name to the service. Human understandable name
      (liguistic signifier, word, phrase, or mnemonic). May follow ISO/IEC 11179-5
      naming principles, and have context provided to specify usage.
  cdi:has_LogicalRecord:
    type: array
    description: the logicalRecord is just a list of InstanceVariables
    items:
      anyOf:
      - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiCDIFProperties/ddi-cdif-logical-record/schema.yaml
      - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiCDIFProperties/ddi-cdif-data-types/schema.yaml#/$defs/id-reference
    minItems: 1
  cdi:purpose:
    $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiCDIFProperties/ddi-cdif-data-types/schema.yaml#/$defs/InternationalString
    description: Intent or reason for the object/the description of the object.
  cdi:recordCount:
    type: integer
    description: The number of records in the Data Store.
required:
- '@type'
- cdi:name
- cdi:has_LogicalRecord
x-jsonld-prefixes:
  cdi: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/

```

Links to the schema:

* YAML version: [schema.yaml](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiCDIFProperties/ddi-cdif-data-store/schema.json)
* JSON version: [schema.json](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiCDIFProperties/ddi-cdif-data-store/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
    "skos": "http://www.w3.org/2004/02/skos/core#",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiCDIFProperties/ddi-cdif-data-store/context.jsonld)

## Sources

* [DDI-CDI 1.0 Specification](https://ddialliance.org/Specification/DDI-CDI/1.0/)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/Cross-Domain-Interoperability-Framework/metadataBuildingBlocks](https://github.com/Cross-Domain-Interoperability-Framework/metadataBuildingBlocks)
* Path: `_sources/ddiCDIFProperties/ddi-cdif-data-store`

