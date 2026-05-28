
# DDI-CDI Logical Record Repository (Schema)

`cdif.bbr.metadata.ddiProperties.ddicdiLogicalRecordRepository` *v0.1*

A managed collection of logical records (delimited file, fixed-record-length file, relational database, etc.). Successor to the DDI-CDI 1.0 DataStore class, renamed and relocated to the FormatDescription package in the 2026-03 DDI-CDI model. Provides $defs for LogicalRecordRepositoryStructure (topology), LogicalRecordRelationship (cross-record linkage, successor to RecordRelation), and InstanceVariableMap. Composes building block: ddicdiLogicalRecord, ddicdiDataTypes (ddiProperties); cdifInstanceVariable (cdifDataType).

[*Status*](http://www.opengis.net/def/status): Under development

## Description

DDI-CDI **LogicalRecordRepository** models a managed collection of logical records held together as a repository — a delimited file, fixed-record-length file, relational database, and so on. It is the successor to the DDI-CDI 1.0 `DataStore` class: the 2026-03 DDI-CDI model renamed `DataStore` to `LogicalRecordRepository` and moved it into the `FormatDescription` package.

The root `cdi:LogicalRecordRepository` carries `cdi:has_LogicalRecord` (members from the `ddicdiLogicalRecord` BB) and characterization properties `cdi:repositoryType` (renamed from `DataStore.dataStoreType`), `cdi:characterSet`, `cdi:recordCount`, `cdi:aboutMissing`, `cdi:allowsDuplicates`, `cdi:name`, `cdi:purpose`, and `cdi:isDefinedBy`.

## Changes from DDI-CDI 1.0 `DataStore`

- `DataStore` → `LogicalRecordRepository`; `dataStoreType` → `repositoryType`.
- `has_LogicalRecordPosition` is dropped — `LogicalRecordPosition` was deleted from the model.
- `has_RecordRelation` is replaced by the `LogicalRecordRelationship` `$def` — `RecordRelation` was deleted and its capability moved into `LogicalRecordRelationship`.
- `CorrespondenceDefinition` is now a canonical DDI-CDI structured datatype and lives in the `ddicdiDataTypes` BB.

## `$defs`

- **`LogicalRecordRepositoryStructure`** — describes the topology and mathematical properties (`cdi:specification` → `StructureSpecification`: reflexive / symmetric / transitive; `cdi:totality`: Partial / Total) of a repository, and the `LogicalRecordRelationship`s that compose it.
- **`LogicalRecordRelationship`** — successor to `RecordRelation`. Pairs source and target `LogicalRecord`s (`cdi:hasSource` / `cdi:hasTarget`) and carries the `InstanceVariableMap`s that define how their instance variables correspond.
- **`InstanceVariableMap`** — a key/value relationship between equivalent instance variables of two logical records. Carries a required `cdi:correspondence` (`CorrespondenceDefinition`), a required `cdi:comparison` (`ComparisonOperator`), and a required `cdi:setValue`, plus `cdi:hasSource` / `cdi:hasTarget` instance-variable references. The three required members follow the `[1..1]` multiplicities in the 2026-03 DDI-CDI model.

## Examples

### Logical Record Repository over two delimited-file records
A cdi:LogicalRecordRepository characterising a delimited-file repository
that holds two logical records (household and person), referenced by @id.
Shows the renamed cdi:repositoryType property and the cdi:has_LogicalRecord
membership association.
#### json
```json
{
  "@context": {
    "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
    "ex": "https://example.org/"
  },
  "@id": "ex:repo/survey-2025",
  "@type": ["cdi:LogicalRecordRepository"],
  "cdi:name": [
    {
      "@type": ["cdi:ObjectName"],
      "cdi:name": "Household survey 2025 repository"
    }
  ],
  "cdi:repositoryType": {
    "@type": ["cdi:ControlledVocabularyEntry"],
    "cdi:entryValue": ["delimited-file"]
  },
  "cdi:characterSet": "UTF-8",
  "cdi:recordCount": 2,
  "cdi:allowsDuplicates": false,
  "cdi:has_LogicalRecord": [
    { "@id": "ex:lr/household" },
    { "@id": "ex:lr/person" }
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
    "https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiLogicalRecordRepository/context.jsonld",
    {
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "ex": "https://example.org/"
    }
  ],
  "@id": "ex:repo/survey-2025",
  "@type": [
    "cdi:LogicalRecordRepository"
  ],
  "cdi:name": [
    {
      "@type": [
        "cdi:ObjectName"
      ],
      "cdi:name": "Household survey 2025 repository"
    }
  ],
  "cdi:repositoryType": {
    "@type": [
      "cdi:ControlledVocabularyEntry"
    ],
    "cdi:entryValue": [
      "delimited-file"
    ]
  },
  "cdi:characterSet": "UTF-8",
  "cdi:recordCount": 2,
  "cdi:allowsDuplicates": false,
  "cdi:has_LogicalRecord": [
    {
      "@id": "ex:lr/household"
    },
    {
      "@id": "ex:lr/person"
    }
  ]
}
```

#### ttl
```ttl
@prefix cdi: <http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<https://example.org/repo/survey-2025> a cdi:LogicalRecordRepository ;
    cdi:allowsDuplicates false ;
    cdi:characterSet "UTF-8" ;
    cdi:has_LogicalRecord <https://example.org/lr/household>,
        <https://example.org/lr/person> ;
    cdi:name [ a cdi:ObjectName ;
            cdi:name "Household survey 2025 repository" ] ;
    cdi:recordCount 2 ;
    cdi:repositoryType [ a cdi:ControlledVocabularyEntry ;
            cdi:entryValue "delimited-file" ] .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: DDI-CDI Logical Record Repository
description: A managed collection of logical records (delimited file, fixed-record-length
  file, relational database, etc.). Successor to the DDI-CDI 1.0 DataStore class;
  renamed and relocated to the FormatDescription package in the 2026-03 DDI-CDI model.
  The repository carries characterization properties and references its member LogicalRecords;
  cross-record linkage is described by LogicalRecordRelationship, and the repository's
  overall topology by LogicalRecordRepositoryStructure.
type: object
properties:
  '@type':
    type: array
    items:
      type: string
    contains:
      const: cdi:LogicalRecordRepository
    minItems: 1
  '@id':
    type: string
    description: Identifier for this LogicalRecordRepository node
  cdi:aboutMissing:
    $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/InternationalString
    description: General information about missing data, e.g., that missing data have
      been standardized across the collection, missing data are present because of
      merging, etc. - corresponds to DDI 2.5 dataMsng.
    x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/aboutMissing
  cdi:allowsDuplicates:
    type: boolean
    description: If False, members are unique within the collection; if True, duplicates
      may be present.
    x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/allowsDuplicates
  cdi:characterSet:
    type: string
    description: Default character set used in the Logical Record Repository.
    x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/characterSet
  cdi:repositoryType:
    $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/ControlledVocabularyEntry
    description: The type of repository - delimited file, fixed-width file, relational
      database, etc. Points to an external definition which can be part of a controlled
      vocabulary maintained by the DDI Alliance. Renamed from DataStore.dataStoreType
      in the 2026-03 model.
    x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/repositoryType
  cdi:identifier:
    $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/Identifier
    description: Identifier for objects requiring short- or long-lasting referencing
      and management.
    x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/identifier
  cdi:name:
    type: array
    items:
      $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/ObjectName
    minItems: 1
    description: Human understandable name (linguistic signifier, word, phrase, or
      mnemonic). May follow ISO/IEC 11179-5 naming principles, with context provided
      to specify usage.
    x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/name
  cdi:purpose:
    $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/InternationalString
    description: Intent or reason for the object / the description of the object.
    x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/purpose
  cdi:recordCount:
    type: integer
    description: The number of records in the Logical Record Repository.
    x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/recordCount
  cdi:isDefinedBy:
    type: array
    items:
      anyOf:
      - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/skosProperties/skosConcept/schema.yaml
      - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/id-reference
    minItems: 1
    description: One or more Concepts characterising the repository.
    x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/isDefinedBy
  cdi:has_LogicalRecord:
    type: array
    items:
      anyOf:
      - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiLogicalRecord/schema.yaml
      - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/id-reference
    minItems: 1
    description: The LogicalRecords held by this repository.
    x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/has_LogicalRecord
required:
- '@type'
$defs:
  LogicalRecordRepositoryStructure:
    type: object
    description: Describes the topology and mathematical properties of a Logical Record
      Repository - how its LogicalRecordRelationships are organized.
    properties:
      '@type':
        type: array
        items:
          type: string
        contains:
          const: cdi:LogicalRecordRepositoryStructure
        minItems: 1
      '@id':
        type: string
        description: Identifier for this LogicalRecordRepositoryStructure node
      cdi:identifier:
        $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/Identifier
        description: Identifier for objects requiring short- or long-lasting referencing
          and management.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/identifier
      cdi:name:
        type: array
        items:
          $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/ObjectName
        minItems: 1
        description: Human understandable name for the structure.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/name
      cdi:purpose:
        $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/InternationalString
        description: Intent or reason for the object / the description of the object.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/purpose
      cdi:semantics:
        $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/ControlledVocabularyEntry
        description: The meaning of the relationship the structure expresses.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/semantics
      cdi:specification:
        $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/StructureSpecification
        description: The mathematical properties of the structure (reflexive, symmetric,
          transitive).
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/specification
      cdi:topology:
        $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/ControlledVocabularyEntry
        description: The topology of the structure.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/topology
      cdi:totality:
        type: string
        enum:
        - Partial
        - Total
        description: Whether every member participates in the structure (Total) or
          only some do (Partial) - StructureExtent.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/totality
      cdi:has_LogicalRecordRelationship:
        type: array
        items:
          anyOf:
          - $ref: '#/$defs/LogicalRecordRelationship'
          - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/id-reference
        minItems: 1
        description: The LogicalRecordRelationships that make up this structure.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/has_LogicalRecordRelationship
      cdi:structures:
        $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/id-reference
        description: The LogicalRecordRepository this structure applies to (id-reference;
          a back-pointer to the repository node declared elsewhere in the graph).
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/structures
    required:
    - '@type'
  LogicalRecordRelationship:
    type: object
    description: Relationship among LogicalRecords - the successor to the DDI-CDI
      1.0 RecordRelation class. Pairs source and target LogicalRecords and carries
      the InstanceVariableMaps that define how their instance variables correspond.
    properties:
      '@type':
        type: array
        items:
          type: string
        contains:
          const: cdi:LogicalRecordRelationship
        minItems: 1
      '@id':
        type: string
        description: Identifier for this LogicalRecordRelationship node
      cdi:identifier:
        $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/Identifier
        description: Identifier for objects requiring short- or long-lasting referencing
          and management.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/identifier
      cdi:semantics:
        $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/ControlledVocabularyEntry
        description: The meaning of the relationship.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/semantics
      cdi:has_InstanceVariableMap:
        type: array
        items:
          anyOf:
          - $ref: '#/$defs/InstanceVariableMap'
          - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/id-reference
        minItems: 1
        description: The key relationships between instance variables of the source
          and target LogicalRecords.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/has_InstanceVariableMap
      cdi:hasTarget:
        type: array
        items:
          anyOf:
          - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiLogicalRecord/schema.yaml
          - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/id-reference
        minItems: 1
        description: The target LogicalRecord(s) of the relationship.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/hasTarget
      cdi:hasSource:
        type: array
        items:
          anyOf:
          - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiLogicalRecord/schema.yaml
          - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/id-reference
        minItems: 1
        description: The source LogicalRecord(s) of the relationship.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/hasSource
    required:
    - '@type'
  InstanceVariableMap:
    type: object
    description: Key/value relationship for two or more LogicalRecords where the key
      is one or more equivalent instance variables and the value is a defined relationship
      or a relationship to a set value. Carried by LogicalRecordRelationship.
    properties:
      '@type':
        type: array
        items:
          type: string
        contains:
          const: cdi:InstanceVariableMap
        minItems: 1
      '@id':
        type: string
        description: Identifier for this InstanceVariableMap node
      cdi:identifier:
        $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/Identifier
        description: Identifier for objects requiring short- or long-lasting referencing
          and management.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/identifier
      cdi:correspondence:
        $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/CorrespondenceDefinition
        description: Describes the relationship between the source and target instance
          variables using controlled vocabularies and descriptive text. The correspondence
          refers to the instance variables, not their values; the relationship would
          normally be ExactMatch.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/correspondence
      cdi:comparison:
        type: string
        enum:
        - Equal
        - GreaterThan
        - GreaterThanOrEqualTo
        - LessThan
        - LessThanOrEqualTo
        - NotEqual
        description: Relationship between the source and target instance variables,
          or to the setValue if provided (ComparisonOperator).
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/comparison
      cdi:setValue:
        type: string
        description: A fixed value for the key source instance variables.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/setValue
      cdi:hasTarget:
        type: array
        items:
          anyOf:
          - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifDataType/cdifInstanceVariable/schema.yaml
          - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/id-reference
        description: The target instance variable(s) of the map.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/hasTarget
      cdi:hasSource:
        type: array
        items:
          anyOf:
          - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifDataType/cdifInstanceVariable/schema.yaml
          - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/id-reference
        minItems: 1
        description: The source instance variable(s) of the map.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/hasSource
    required:
    - '@type'
    - cdi:correspondence
    - cdi:comparison
    - cdi:setValue
x-jsonld-prefixes:
  cdi: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/

```

Links to the schema:

* YAML version: [schema.yaml](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiLogicalRecordRepository/schema.json)
* JSON version: [schema.json](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiLogicalRecordRepository/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
    "skos": "http://www.w3.org/2004/02/skos/core#",
    "cdif": "https://cdif.org/0.1/",
    "schema": "http://schema.org/",
    "spdx": "http://spdx.org/rdf/terms#",
    "xas": "https://xas.org/dictionary/",
    "nxs": "http://purl.org/nexusformat/definitions/",
    "prov": "http://www.w3.org/ns/prov#",
    "ex": "https://example.org/",
    "xsd": "http://www.w3.org/2001/XMLSchema#",
    "dcterms": "http://purl.org/dc/terms/",
    "dcat": "http://www.w3.org/ns/dcat#",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiLogicalRecordRepository/context.jsonld)

## Sources

* [DDI-CDI Specification (2026-03 model)](https://ddialliance.org/Specification/DDI-CDI/)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/Cross-Domain-Interoperability-Framework/metadataBuildingBlocks](https://github.com/Cross-Domain-Interoperability-Framework/metadataBuildingBlocks)
* Path: `_sources/ddiProperties/ddicdiLogicalRecordRepository`

