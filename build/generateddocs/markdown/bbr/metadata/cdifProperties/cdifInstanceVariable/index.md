
# CDIF Instance Variable (Schema)

`cdif.bbr.metadata.cdifProperties.cdifInstanceVariable` *v0.2*

Profile of cdi:InstanceVariable / schema:PropertyValue used as a member of a schema:variableMeasured array. Adds DDI-CDI properties (cdif:physicalDataType, cdif:role, cdif:simpleUnitOfMeasure, cdif:uses, cdi:qualifies) on top of schemaorgProperties/variableMeasured and ddiProperties/ddicdiInstanceVariable. Accepts a single node, an unwrapped @graph array of nodes (OGC pipeline), or a JSON-LD document with @context and @graph.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

## CDIF Instance Variable

Profile of `cdi:InstanceVariable` / `schema:PropertyValue` for use as a member of a `schema:variableMeasured` array. Composes the base [variableMeasured](../../schemaorgProperties/variableMeasured/) building block with the DDI-CDI properties of `InstanceVariable` and its `RepresentedVariable` superclass.

The BB accepts three shapes interchangeably:

1. a single CDIF Instance Variable node;
2. an unwrapped array of such nodes (OGC pipeline `@graph` form);
3. a full JSON-LD document with `@context` and `@graph`.

### Property scope

The schema carries **all `InstanceVariable`-own and `RepresentedVariable`-own properties** from the DDI-CDI class hierarchy (`ConceptualVariable → RepresentedVariable → InstanceVariable`). Properties inherited from `ConceptualVariable` and above (`descriptiveText`, `unitOfMeasureKind`, `definition`, `displayLabel`, `name`, `measures`, `takesSentinel/SubstantiveConceptsFrom`, `uses`-as-Concept, …) are **not** included — the conceptual layer is described separately.

**InstanceVariable-own:**

- **@type** — must include `cdi:InstanceVariable` (and, as a `schema:PropertyValue`, that type too)
- **cdif:physicalDataType** — physical data type concept (string, URI reference, or DefinedTerm)
- **cdif:role** — role in a data structure (`UnitIdentifier`, `Measure`, `Attribute`, `Dimension`, `Descriptor`, `ReferenceVariable`)
- **cdi:function** — immutable characteristic (geographic designator, weight, temporal designation, …)
- **cdi:platformType** — application / technical system context the variable was realized in
- **cdi:source** — provenance reference
- **cdif:isDescribedBy_StatisticsCollection** — the `StatisticsCollection` of summary / category statistics for this variable (target-suffixed: `isDescribedBy` is polymorphic in DDI-CDI)

**RepresentedVariable-own:**

- **cdi:hasIntendedDataType** — intended data type, independent of physical representation
- **cdi:describedUnitOfMeasure** — unit of measure as a controlled-vocabulary entry
- **cdif:simpleUnitOfMeasure** — unit of measure as a plain string / URI / DefinedTerm
- **cdi:takesSentinelValuesFrom** — sentinel (missing / not-applicable) value domain(s) — `cdifValueDomain`
- **cdi:takesSubstantiveValuesFrom** — substantive value domain — `cdifValueDomain`

**CDIF extensions:**

- **cdif:uses** — concepts (or, under the Data Structure profile, the `RepresentedVariable`) that this variable represents
- **cdi:qualifies** — `@id` reference to another instance variable; used when `cdif:role` is `Attribute`

### Data Structure profile constraint

When a dataset's distribution carries `cdi:isStructuredBy` (CDIF **Data Structure** profile), the `RepresentedVariable`-own properties above live on the referenced `RepresentedVariable` and are reached from the InstanceVariable via `cdif:uses` — they must **not** be duplicated on the InstanceVariable. The Data Structure profile disallows them on `schema:variableMeasured` items for that reason. In the plain **Data Description** profile (no `cdi:isStructuredBy`), they may be carried directly on the InstanceVariable.

### Dependencies

- [variableMeasured](../../schemaorgProperties/variableMeasured/) — base variable measured properties
- [cdifValueDomain](../cdifValueDomain/) — substantive / sentinel value domains
- [cdifStatistics](../cdifStatistics/) — `StatisticsCollection` target of `cdif:isDescribedBy_StatisticsCollection`
- [definedTerm](../../schemaorgProperties/definedTerm/) — controlled vocabulary term

## Examples

### Minimal CDIF Instance Variable
Single PropertyValue + cdi:InstanceVariable node with the four
properties required by the CdifInstanceVariableNode shape (which
inherits ddicdiInstanceVariable's required list): @type, cdi:name,
cdi:definition, cdi:takesSubstantiveValuesFrom.
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
    "ex": "https://example.org/",
    "cdif": "https://cdif.org/0.1/"
  },
  "@type": [
    "cdi:InstanceVariable",
    "schema:PropertyValue"
  ],
  "@id": "ex:var/temperature",
  "schema:name": "temperature",
  "cdif:name": [
    "temperature"
  ],
  "cdif:definition": "Air temperature measurement.",
  "cdi:takesSubstantiveValuesFrom": {
    "@id": "ex:value-domain/decimal"
  }
}

```

#### jsonld
```jsonld
{
  "@context": [
    {
      "schema": "http://schema.org/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/"
    },
    "https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifProperties/cdifInstanceVariable/context.jsonld",
    {
      "schema": "http://schema.org/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "ex": "https://example.org/",
      "cdif": "https://cdif.org/0.1/"
    }
  ],
  "@type": [
    "cdi:InstanceVariable",
    "schema:PropertyValue"
  ],
  "@id": "ex:var/temperature",
  "schema:name": "temperature",
  "cdif:name": [
    "temperature"
  ],
  "cdif:definition": "Air temperature measurement.",
  "cdi:takesSubstantiveValuesFrom": {
    "@id": "ex:value-domain/decimal"
  }
}
```

#### ttl
```ttl
@prefix cdi: <http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/> .
@prefix cdif: <https://cdif.org/0.1/> .
@prefix schema1: <http://schema.org/> .

<https://example.org/var/temperature> a cdi:InstanceVariable,
        schema1:PropertyValue ;
    cdi:takesSubstantiveValuesFrom <https://example.org/value-domain/decimal> ;
    schema1:name "temperature" ;
    cdif:definition "Air temperature measurement." ;
    cdif:name "temperature" .


```


### Complete CDIF Instance Variable (XAS)
Implementation of Schema.org PropertyValue as value for variableMeasured
property, adding cdi:InstanceVariable type and several other DDI-CDI
properties. From the X-Ray Absorption profile testing corpus, with two
InstanceVariables in an @graph and a parent schema:Dataset that references
them via schema:variableMeasured.
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "ex": "https://example.org/",
    "xsd": "http://www.w3.org/2001/XMLSchema#",
    "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
    "cdif": "https://cdif.org/0.1/",
    "skos": "http://www.w3.org/2004/02/skos/core#",
    "xas": "https://xas.org/dictionary/"
  },
  "@type": [
    "cdi:InstanceVariable",
    "schema:PropertyValue"
  ],
  "@id": "xas:monochromatorEnergy",
  "schema:name": "energy",
  "schema:alternateName": [
    "Monochromator energy"
  ],
  "schema:description": "Incident photon energy selected by the monochromator during the XAS scan.",
  "schema:propertyID": [
    "xas:monochromatorEnergyConcept"
  ],
  "schema:unitText": "eV",
  "cdi:identifier": {
    "@type": [
      "cdi:Identifier"
    ],
    "cdi:uri": "https://xas.org/dictionary/monochromatorEnergy"
  },
  "cdif:name": [
    "energy"
  ],
  "cdif:displayLabel": [
    "Monochromator energy"
  ],
  "cdif:definition": "Incident photon energy selected by the monochromator during the XAS scan.",
  "cdif:physicalDataType": [
    {
      "@type": [
        "cdi:ControlledVocabularyEntry"
      ],
      "cdi:entryValue": [
        "xsd:decimal"
      ]
    }
  ],
  "cdi:takesSubstantiveValuesFrom": {
    "@id": "ex:value-domain/decimal-eV"
  },
  "cdif:simpleUnitOfMeasure": "eV",
  "cdif:uses": [
    "xas:monochromatorEnergyConcept"
  ],
  "cdif:role": "Attribute",
  "cdi:qualifies": {
    "@id": "ex:temperatureVariable"
  }
}

```

#### jsonld
```jsonld
{
  "@context": [
    {
      "schema": "http://schema.org/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "xas": "https://xas.org/dictionary/",
      "skos": "http://www.w3.org/2004/02/skos/core#"
    },
    "https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifProperties/cdifInstanceVariable/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ex": "https://example.org/",
      "xsd": "http://www.w3.org/2001/XMLSchema#",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "cdif": "https://cdif.org/0.1/",
      "skos": "http://www.w3.org/2004/02/skos/core#",
      "xas": "https://xas.org/dictionary/"
    }
  ],
  "@type": [
    "cdi:InstanceVariable",
    "schema:PropertyValue"
  ],
  "@id": "xas:monochromatorEnergy",
  "schema:name": "energy",
  "schema:alternateName": [
    "Monochromator energy"
  ],
  "schema:description": "Incident photon energy selected by the monochromator during the XAS scan.",
  "schema:propertyID": [
    "xas:monochromatorEnergyConcept"
  ],
  "schema:unitText": "eV",
  "cdi:identifier": {
    "@type": [
      "cdi:Identifier"
    ],
    "cdi:uri": "https://xas.org/dictionary/monochromatorEnergy"
  },
  "cdif:name": [
    "energy"
  ],
  "cdif:displayLabel": [
    "Monochromator energy"
  ],
  "cdif:definition": "Incident photon energy selected by the monochromator during the XAS scan.",
  "cdif:physicalDataType": [
    {
      "@type": [
        "cdi:ControlledVocabularyEntry"
      ],
      "cdi:entryValue": [
        "xsd:decimal"
      ]
    }
  ],
  "cdi:takesSubstantiveValuesFrom": {
    "@id": "ex:value-domain/decimal-eV"
  },
  "cdif:simpleUnitOfMeasure": "eV",
  "cdif:uses": [
    "xas:monochromatorEnergyConcept"
  ],
  "cdif:role": "Attribute",
  "cdi:qualifies": {
    "@id": "ex:temperatureVariable"
  }
}
```

#### ttl
```ttl
@prefix cdi: <http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/> .
@prefix cdif: <https://cdif.org/0.1/> .
@prefix ex: <https://example.org/> .
@prefix schema1: <http://schema.org/> .
@prefix xas: <https://xas.org/dictionary/> .

xas:monochromatorEnergy a cdi:InstanceVariable,
        schema1:PropertyValue ;
    cdi:identifier [ a cdi:Identifier ;
            cdi:uri "https://xas.org/dictionary/monochromatorEnergy" ] ;
    cdi:qualifies ex:temperatureVariable ;
    cdi:takesSubstantiveValuesFrom <https://example.org/value-domain/decimal-eV> ;
    schema1:alternateName "Monochromator energy" ;
    schema1:description "Incident photon energy selected by the monochromator during the XAS scan." ;
    schema1:name "energy" ;
    schema1:propertyID "xas:monochromatorEnergyConcept" ;
    schema1:unitText "eV" ;
    cdif:definition "Incident photon energy selected by the monochromator during the XAS scan." ;
    cdif:displayLabel "Monochromator energy" ;
    cdif:name "energy" ;
    cdif:physicalDataType [ a cdi:ControlledVocabularyEntry ;
            cdi:entryValue "xsd:decimal" ] ;
    cdif:role "Attribute" ;
    cdif:simpleUnitOfMeasure "eV" ;
    cdif:uses "xas:monochromatorEnergyConcept" .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: CDIF Instance Variable
type: object
properties:
  '@type':
    type: array
    description: Must include both schema:PropertyValue and cdi:InstanceVariable.
      Additional types may be included.
    items:
      type: string
    contains:
      const: cdi:InstanceVariable
  cdif:physicalDataType:
    type: array
    items:
      anyOf:
      - type: string
      - type: object
        properties:
          '@id':
            type: string
            description: reference to a skos concept for the data type
      - $ref: '#/$defs/DefinedTerm'
    description: identifier or name for the data type concept.
  cdif:role:
    type: string
    enum:
    - UnitIdentifier
    - Measure
    - Attribute
    - Dimension
    - Descriptor
    - ReferenceVariable
    description: Specifies the role this variable plays in a data structure. UnitIdentifier
      names the unit a row describes; Measure holds observed/derived values; Attribute
      qualifies an observation; Dimension addresses a cell in a multi-dimensional
      cube; Descriptor names the variable that a Reference column records values for
      (long format); ReferenceVariable holds those recorded values.
  cdif:simpleUnitOfMeasure:
    anyOf:
    - type: string
    - type: object
      properties:
        '@id':
          type: string
          description: reference to a skos concept for the data type
    - $ref: '#/$defs/DefinedTerm'
  cdif:uses:
    type: array
    items:
      anyOf:
      - type: string
      - type: object
        properties:
          '@id':
            type: string
            description: reference to a skos concept for the property
      - $ref: '#/$defs/DefinedTerm'
    description: Essentially the same as schema:propertyID. References to concepts
      that this variable measures or represents. When the dataset's distribution carries
      cdi:isStructuredBy (CDIF Data Structure profile), cdif:uses references the RepresentedVariable
      that supplies the represented-variable-level properties below, which are then
      NOT duplicated on the InstanceVariable.
  cdi:function:
    type: array
    items:
      anyOf:
      - type: string
      - type: object
        properties:
          '@id':
            type: string
      - $ref: '#/$defs/DefinedTerm'
    description: Immutable characteristic of the variable such as geographic designator,
      weight, temporal designation, etc. (InstanceVariable.function).
    x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/function
  cdi:platformType:
    anyOf:
    - type: string
    - type: object
      properties:
        '@id':
          type: string
    - $ref: '#/$defs/DefinedTerm'
    description: The application or technical system context in which the variable
      has been realized - typically a statistical processing package or processing
      environment (InstanceVariable.platformType).
    x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/platformType
  cdi:source:
    anyOf:
    - type: string
    - type: object
      properties:
        '@id':
          type: string
    description: Reference capturing provenance information for this InstanceVariable
      (InstanceVariable.source).
    x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/source
  cdif:isDescribedBy_StatisticsCollection:
    description: 'The StatisticsCollection holding summary / category statistics for
      this InstanceVariable (InstanceVariable.isDescribedBy). cdif: namespaced and
      target-suffixed because the DDI-CDI isDescribedBy association is polymorphic.'
    anyOf:
    - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifProperties/cdifStatistics/schema.yaml#/$defs/StatisticsCollection
    - type: object
      properties:
        '@id':
          type: string
      required:
      - '@id'
  cdi:hasIntendedDataType:
    anyOf:
    - type: string
    - type: object
      properties:
        '@id':
          type: string
    - $ref: '#/$defs/DefinedTerm'
    description: The data type intended to be used by this variable, independent of
      its physical representation (RepresentedVariable.hasIntendedDataType).
    x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/hasIntendedDataType
  cdi:describedUnitOfMeasure:
    anyOf:
    - type: string
    - type: object
      properties:
        '@id':
          type: string
    - $ref: '#/$defs/DefinedTerm'
    description: The unit in which the data values are measured, expressed as a controlled-vocabulary
      entry (RepresentedVariable.describedUnitOfMeasure). For a plain-string unit,
      use cdif:simpleUnitOfMeasure instead.
    x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/describedUnitOfMeasure
  cdi:qualifies:
    type: object
    properties:
      '@id':
        type: string
    description: reference to an instance variable defined for this dataset
    x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/qualifies
allOf:
- required:
  - '@type'
- $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/variableMeasured/schema.yaml
$defs:
  DefinedTerm:
    anyOf:
    - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/definedTerm/schema.yaml
    - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/skosProperties/skosConcept/schema.yaml
x-jsonld-prefixes:
  schema: http://schema.org/
  spdx: http://spdx.org/rdf/terms#
  cdi: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/
  skos: http://www.w3.org/2004/02/skos/core#
  xas: https://xas.org/dictionary/
  nxs: http://purl.org/nexusformat/definitions/
  prov: http://www.w3.org/ns/prov#

```

Links to the schema:

* YAML version: [schema.yaml](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifProperties/cdifInstanceVariable/schema.json)
* JSON version: [schema.json](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifProperties/cdifInstanceVariable/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "schema": "http://schema.org/",
    "spdx": "http://spdx.org/rdf/terms#",
    "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
    "skos": "http://www.w3.org/2004/02/skos/core#",
    "xas": "https://xas.org/dictionary/",
    "nxs": "http://purl.org/nexusformat/definitions/",
    "prov": "http://www.w3.org/ns/prov#",
    "cdif": "https://cdif.org/0.1/",
    "ex": "https://example.org/",
    "xsd": "http://www.w3.org/2001/XMLSchema#",
    "dcterms": "http://purl.org/dc/terms/",
    "dcat": "http://www.w3.org/ns/dcat#",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifProperties/cdifInstanceVariable/context.jsonld)

## Sources

* [DDI-CDI 1.0 Specification](https://ddialliance.org/Specification/DDI-CDI/1.0/)
* [schema.org/variableMeasured](https://schema.org/variableMeasured)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/Cross-Domain-Interoperability-Framework/metadataBuildingBlocks](https://github.com/Cross-Domain-Interoperability-Framework/metadataBuildingBlocks)
* Path: `_sources/cdifProperties/cdifInstanceVariable`

