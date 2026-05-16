
# DDI-CDI Collections (Schema)

`cdif.bbr.metadata.ddiProperties.ddicdiCollections` *v0.1*

Generic container that supports different types of groupings, from unordered sets to all sorts of hierarchies, nesting and ordered sets/bags.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

DDI-CDI **Collections** is the generic collections pattern from the 2026-03 DDI-CDI model (`CollectionsPattern` package) — the abstract machinery for grouping, ordering, and relating members that the more specific structural classes (data structures, code lists, keys, …) specialize.

The root validates any of nine concrete classes:

- **`cdi:Collection`** — generic container supporting sets, bags, hierarchies, ordered and unordered groupings (`cdi:has` → `Member`, `cdi:allowsDuplicates`).
- **`cdi:List`** — a simple ordered Collection whose member order is given by `Position` objects.
- **`cdi:Map`** — a comparison map identifying source/target members and a `CorrespondenceDefinition`.
- **`cdi:Member`** — an element in a collection (atomic or composite).
- **`cdi:IndividualMember`** — a distinct, atomic (non-collection) member.
- **`cdi:MemberRelationship`** — a directional relationship between members (`cdi:hasSource` / `cdi:hasTarget`).
- **`cdi:Position`** — the position of a member within a `List` (`cdi:value`, `cdi:indexes`).
- **`cdi:Structure`** — an organized set of member relationships, characterized by `cdi:specification` (reflexive/symmetric/transitive), `cdi:topology`, and `cdi:totality`.
- **`cdi:Comparison`** — the minimal comparison pattern, carrying member `Map`s.

## Examples

### Generic collection of members
A cdi:Collection ("Monitoring stations") that does not allow duplicates and
holds two cdi:Member entries - one inline, one as an @id reference.
#### json
```json
{
  "@context": {
    "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
    "ex": "https://example.org/"
  },
  "@type": ["cdi:Collection"],
  "@id": "ex:collection/monitoringStations",
  "cdi:name": [
    {
      "@type": ["cdi:ObjectName"],
      "cdi:name": "Monitoring stations"
    }
  ],
  "cdi:allowsDuplicates": false,
  "cdi:has": [
    {
      "@type": ["cdi:Member"],
      "@id": "ex:member/stationA"
    },
    {
      "@id": "ex:member/stationB"
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
    "https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiCollections/context.jsonld",
    {
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "ex": "https://example.org/"
    }
  ],
  "@type": [
    "cdi:Collection"
  ],
  "@id": "ex:collection/monitoringStations",
  "cdi:name": [
    {
      "@type": [
        "cdi:ObjectName"
      ],
      "cdi:name": "Monitoring stations"
    }
  ],
  "cdi:allowsDuplicates": false,
  "cdi:has": [
    {
      "@type": [
        "cdi:Member"
      ],
      "@id": "ex:member/stationA"
    },
    {
      "@id": "ex:member/stationB"
    }
  ]
}
```

#### ttl
```ttl
@prefix cdi: <http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<https://example.org/collection/monitoringStations> a cdi:Collection ;
    cdi:allowsDuplicates false ;
    cdi:has <https://example.org/member/stationA>,
        <https://example.org/member/stationB> ;
    cdi:name [ a cdi:ObjectName ;
            cdi:name "Monitoring stations" ] .

<https://example.org/member/stationA> a cdi:Member .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: DDI-CDI Collections
description: Generic container that supports different types of groupings, from unordered
  sets to all sorts of hierarchies, nesting and ordered sets/bags.
anyOf:
- $ref: '#/$defs/Collection'
- $ref: '#/$defs/List'
- $ref: '#/$defs/Map'
- $ref: '#/$defs/Member'
- $ref: '#/$defs/MemberRelationship'
- $ref: '#/$defs/Position'
- $ref: '#/$defs/Structure'
- $ref: '#/$defs/IndividualMember'
- $ref: '#/$defs/Comparison'
$defs:
  Collection:
    type: object
    description: Generic container that supports different types of groupings, from
      unordered sets to all sorts of hierarchies, nesting and ordered sets/bags.
    properties:
      '@type':
        type: array
        items:
          type: string
        contains:
          const: cdi:Collection
        minItems: 1
      '@id':
        type: string
        description: Identifier for this Collection node
      cdi:allowsDuplicates:
        type: boolean
        description: "If value is False, the members are unique within the collection
          - if True, there may be duplicates. (Note that a mathematical \u201Cbag\u201D
          permits duplicates and is unordered - a \u201Cset\u201D does not have duplicates
          and may be ordered.)"
      cdi:name:
        type: array
        items:
          $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/ObjectName
        description: Human understandable name (linguistic signifier, word, phrase,
          or mnemonic). May follow ISO/IEC 11179-5 naming principles, and have context
          provided to specify usage.
      cdi:purpose:
        $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/InternationalString
        description: Intent or reason for the object/the description of the object.
      cdi:has:
        type: array
        items:
          anyOf:
          - $ref: '#/$defs/Member'
          - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/id-reference
    required:
    - '@type'
  List:
    type: object
    description: Simple ordered Collection defined as a list of Members where the
      location of each Member in the list is given by the associated Position class.
    properties:
      '@type':
        type: array
        items:
          type: string
        contains:
          const: cdi:List
        minItems: 1
      '@id':
        type: string
        description: Identifier for this List node
      cdi:has:
        type: array
        items:
          anyOf:
          - $ref: '#/$defs/Position'
          - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/id-reference
      cdi:allowsDuplicates:
        type: boolean
        description: "If value is False, the members are unique within the collection
          - if True, there may be duplicates. (Note that a mathematical \u201Cbag\u201D
          permits duplicates and is unordered - a \u201Cset\u201D does not have duplicates
          and may be ordered.)"
      cdi:name:
        type: array
        items:
          $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/ObjectName
        description: Human understandable name (linguistic signifier, word, phrase,
          or mnemonic). May follow ISO/IEC 11179-5 naming principles, and have context
          provided to specify usage.
      cdi:purpose:
        $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/InternationalString
        description: Intent or reason for the object/the description of the object.
    required:
    - '@type'
  Map:
    type: object
    description: Provides a basic pattern for a comparison map which identifies source
      and target members and details about their match. Source and target were retained
      as in describing differences and commonalities the direction of the comparison
      may be important.
    properties:
      '@type':
        type: array
        items:
          type: string
        contains:
          const: cdi:Map
        minItems: 1
      '@id':
        type: string
        description: Identifier for this Map node
      cdi:correspondence:
        $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/CorrespondenceDefinition
        description: Type of correspondence in terms of commonalities and differences
          between two members.
      cdi:hasTarget:
        type: array
        items:
          anyOf:
          - $ref: '#/$defs/Member'
          - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/id-reference
      cdi:hasSource:
        type: array
        items:
          anyOf:
          - $ref: '#/$defs/Member'
          - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/id-reference
    required:
    - '@type'
  Member:
    type: object
    description: Element in a collection that can be either atomic (individual member)
      or composite (collection).
    properties:
      '@type':
        type: array
        items:
          type: string
        contains:
          const: cdi:Member
        minItems: 1
      '@id':
        type: string
        description: Identifier for this Member node
    required:
    - '@type'
  MemberRelationship:
    type: object
    description: Relationship between members in a collection with directionality
      given by source and target.
    properties:
      '@type':
        type: array
        items:
          type: string
        contains:
          const: cdi:MemberRelationship
        minItems: 1
      '@id':
        type: string
        description: Identifier for this MemberRelationship node
      cdi:semantics:
        $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/ControlledVocabularyEntry
        description: Specifies the semantics of the object in reference to a vocabulary,
          ontology, etc.
      cdi:hasTarget:
        type: array
        items:
          anyOf:
          - $ref: '#/$defs/Member'
          - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/id-reference
      cdi:hasSource:
        type: array
        items:
          anyOf:
          - $ref: '#/$defs/Member'
          - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/id-reference
    required:
    - '@type'
  Position:
    type: object
    description: Position of the associated member within the associated List.
    properties:
      '@type':
        type: array
        items:
          type: string
        contains:
          const: cdi:Position
        minItems: 1
      '@id':
        type: string
        description: Identifier for this Position node
      cdi:value:
        type: integer
        description: Index value of the member in an ordered array.
      cdi:indexes:
        anyOf:
        - $ref: '#/$defs/Member'
        - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/id-reference
    required:
    - '@type'
  Structure:
    type: object
    description: 'Organized set of relationships between members in a collection.
      These relationships can be characterized mathematically in terms of reflexivity,
      symmetry and transitivity, or informally in terms of the collection''s topology,
      e.g. network, tree, etc. In both cases it can also be defined either on all
      (total) or some (partial) members.


      - Specification: formal characterization of a structure in terms of reflexivity,
      symmetry and transitivity. - StructureSpecification: set of mathematical properties
      of a structure (reflexivity, symmetry and transitivity). - Totality: characterization
      of a structure in terms of whether it applies to all (total) or some (partial)
      members.'
    properties:
      '@type':
        type: array
        items:
          type: string
        contains:
          const: cdi:Structure
        minItems: 1
      '@id':
        type: string
        description: Identifier for this Structure node
      cdi:name:
        type: array
        items:
          $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/ObjectName
        description: Human understandable name (linguistic signifier, word, phrase,
          or mnemonic). May follow ISO/IEC 11179-5 naming principles, and have context
          provided to specify usage.
      cdi:purpose:
        $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/InternationalString
        description: Intent or reason for the object/the description of the object.
      cdi:semantics:
        $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/ControlledVocabularyEntry
        description: Specifies the semantics of the object in reference to a vocabulary,
          ontology, etc.
      cdi:specification:
        $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/StructureSpecification
        description: Provides information on reflexivity, transitivity, and symmetry
          of relationship using a descriptive term from an enumerated list. Use if
          all relations within this relation structure are of the same specification.
      cdi:topology:
        $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/ControlledVocabularyEntry
        description: 'Means of organizing a set of members in a collection based on
          explicit rules for how members are related to each other. At a minimum,
          the controlled vocabulary should contain the following entries below. Note
          that these entries overlap and need to be organized into a type hierarchy
          once other entries are identified and defined.


          - Graph: organized collection where members are vertices and relationships
          between them are edges. - Lattice: organized collection where members are
          vertices, relationships between them are directed edges and there are two
          and only two distinguished vertices, i.e. a source, which has only outgoing
          edges, and a sink, which has only incoming edges. - Network/mesh: collection
          of linked members. - Partition: organized collection where members are grouped
          into non-empty and non-overlapping sub-collections - Tree: organized collection
          where members are vertices, relationships between them are edges and any
          two vertices are connected by exactly one path (sequence of contiguous edges)'
      cdi:totality:
        type: string
        enum:
        - Partial
        - Total
        description: Indicates whether the related collections are comprehensive in
          terms of their coverage i.e application to all (total) or some (partial)
          members.
      cdi:structures:
        anyOf:
        - $ref: '#/$defs/Collection'
        - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/id-reference
      cdi:has:
        type: array
        items:
          anyOf:
          - $ref: '#/$defs/MemberRelationship'
          - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/id-reference
    required:
    - '@type'
  IndividualMember:
    type: object
    description: Distinct element that is not itself a collection (atomic).
    properties:
      '@type':
        type: array
        items:
          type: string
        contains:
          const: cdi:IndividualMember
        minItems: 1
      '@id':
        type: string
        description: Identifier for this IndividualMember node
    required:
    - '@type'
  Comparison:
    type: object
    description: The minimal pattern for a comparison including a mapping between
      members.
    properties:
      '@type':
        type: array
        items:
          type: string
        contains:
          const: cdi:Comparison
        minItems: 1
      '@id':
        type: string
        description: Identifier for this Comparison node
      cdi:purpose:
        $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/InternationalString
        description: Intent or reason for the object/the description of the object.
      cdi:maps:
        type: array
        items:
          anyOf:
          - $ref: '#/$defs/Collection'
          - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/id-reference
        minItems: 2
      cdi:has:
        type: array
        items:
          anyOf:
          - $ref: '#/$defs/Map'
          - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiDataTypes/schema.yaml#/$defs/id-reference
    required:
    - '@type'
x-jsonld-prefixes:
  cdi: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/

```

Links to the schema:

* YAML version: [schema.yaml](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiCollections/schema.json)
* JSON version: [schema.json](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiCollections/schema.yaml)


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
[context.jsonld](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiProperties/ddicdiCollections/context.jsonld)

## Sources

* [DDI-CDI 1.0 Specification](https://ddialliance.org/Specification/DDI-CDI/1.0/)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/Cross-Domain-Interoperability-Framework/metadataBuildingBlocks](https://github.com/Cross-Domain-Interoperability-Framework/metadataBuildingBlocks)
* Path: `_sources/ddiProperties/ddicdiCollections`

