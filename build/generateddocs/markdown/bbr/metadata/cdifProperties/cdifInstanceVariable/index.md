
# CDIF Instance Variable (Schema)

`cdif.bbr.metadata.cdifProperties.cdifInstanceVariable` *v0.2*

Profile of cdi:InstanceVariable / schema:PropertyValue used as a member of a schema:variableMeasured array. Adds DDI-CDI properties (cdif:physicalDataType, cdi:role, cdif:simpleUnitOfMeasure, cdif:uses, cdi:qualifies) on top of schemaorgProperties/variableMeasured and ddiCDIFProperties/ddi-cdif-instance-variable. Accepts a single node, an unwrapped @graph array of nodes (OGC pipeline), or a JSON-LD document with @context and @graph.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

## CDIF Instance Variable

Profile of `cdi:InstanceVariable` / `schema:PropertyValue` for use as a member of a `schema:variableMeasured` array. Extends the base [variableMeasured](../../schemaorgProperties/variableMeasured/) and [ddi-cdif-instance-variable](../../ddiCDIFProperties/ddi-cdif-instance-variable/) building blocks with the DDI-CDI properties most commonly needed for variable description in CDIF integration profiles.

The BB accepts three shapes interchangeably:

1. a single CDIF Instance Variable node;
2. an unwrapped array of such nodes (OGC pipeline `@graph` form);
3. a full JSON-LD document with `@context` and `@graph`.

### Defined properties

- **@type** — must include `schema:PropertyValue` and `cdi:InstanceVariable`
- **cdi:identifier** — identifier for this variable
- **cdif:physicalDataType** — physical data type concept (string, URI reference, or DefinedTerm)
- **cdi:intendedDataType** — intended data type for values (recommended: XML Schema datatypes)
- **cdi:role** — role of variable in data structure (`UnitIdentifier`, `Measure`, `Attribute`, `Dimension`, `Descriptor`, `ReferenceVariable`)
- **cdi:describedUnitOfMeasure** — structured unit of measure from controlled vocabulary (DefinedTerm)
- **cdif:simpleUnitOfMeasure** — simple unit of measure (string, URI reference, or DefinedTerm)
- **cdif:uses** — concepts that this variable measures or represents
- **cdi:qualifies** — `@id` reference to another instance variable in the same dataset; required when `cdi:role` is `Attribute`
- **cdi:name** — name of variable in DDI-CDI model
- **cdi:displayLabel** — human-readable label for display purposes

### Dependencies

- [variableMeasured](../../schemaorgProperties/variableMeasured/) — base variable measured properties
- [ddi-cdif-instance-variable](../../ddiCDIFProperties/ddi-cdif-instance-variable/) — full DDI-CDI InstanceVariable shape
- [definedTerm](../../schemaorgProperties/definedTerm/) — controlled vocabulary term

## Examples

### Minimal CDIF Instance Variable
Single PropertyValue + cdi:InstanceVariable node with the four
properties required by the CdifInstanceVariableNode shape (which
inherits ddi-cdif-instance-variable's required list): @type, cdi:name,
cdi:definition, cdi:takesSubstantiveValuesFrom.
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
    "ex": "https://example.org/"
  },
  "@type": ["cdi:InstanceVariable", "schema:PropertyValue"],
  "@id": "ex:var/temperature",
  "schema:name": "temperature",
  "cdi:name": [
    {
      "@type": ["cdi:ObjectName"],
      "cdi:name": "temperature"
    }
  ],
  "cdi:definition": {
    "@type": ["cdi:InternationalString"],
    "cdi:languageSpecificString": [
      {
        "@type": ["cdi:LanguageString"],
        "cdi:content": "Air temperature measurement.",
        "cdi:language": "en"
      }
    ]
  },
  "cdi:takesSubstantiveValuesFrom": { "@id": "ex:value-domain/decimal" }
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
      "ex": "https://example.org/"
    }
  ],
  "@type": [
    "cdi:InstanceVariable",
    "schema:PropertyValue"
  ],
  "@id": "ex:var/temperature",
  "schema:name": "temperature",
  "cdi:name": [
    {
      "@type": [
        "cdi:ObjectName"
      ],
      "cdi:name": "temperature"
    }
  ],
  "cdi:definition": {
    "@type": [
      "cdi:InternationalString"
    ],
    "cdi:languageSpecificString": [
      {
        "@type": [
          "cdi:LanguageString"
        ],
        "cdi:content": "Air temperature measurement.",
        "cdi:language": "en"
      }
    ]
  },
  "cdi:takesSubstantiveValuesFrom": {
    "@id": "ex:value-domain/decimal"
  }
}
```

#### ttl
```ttl
@prefix cdi: <http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/> .
@prefix schema1: <http://schema.org/> .

<https://example.org/var/temperature> a cdi:InstanceVariable,
        schema1:PropertyValue ;
    cdi:definition [ a cdi:InternationalString ;
            cdi:languageSpecificString [ a cdi:LanguageString ;
                    cdi:content "Air temperature measurement." ;
                    cdi:language "en" ] ] ;
    cdi:name [ a cdi:ObjectName ;
            cdi:name "temperature" ] ;
    cdi:takesSubstantiveValuesFrom <https://example.org/value-domain/decimal> ;
    schema1:name "temperature" .


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
  "schema:alternateName": ["Monochromator energy"],
  "schema:description": "Incident photon energy selected by the monochromator during the XAS scan.",
  "schema:propertyID": ["xas:monochromatorEnergyConcept"],
  "schema:unitText": "eV",
  "cdi:identifier": {
    "@type": ["cdi:Identifier"],
    "cdi:uri": "https://xas.org/dictionary/monochromatorEnergy"
  },
  "cdi:name": [
    {
      "@type": ["cdi:ObjectName"],
      "cdi:name": "energy"
    }
  ],
  "cdi:displayLabel": [
    {
      "@type": ["cdi:LabelForDisplay"],
      "cdi:content": "Monochromator energy",
      "cdi:language": "en"
    }
  ],
  "cdi:definition": {
    "@type": ["cdi:InternationalString"],
    "cdi:languageSpecificString": [
      {
        "@type": ["cdi:LanguageString"],
        "cdi:content": "Incident photon energy selected by the monochromator during the XAS scan.",
        "cdi:language": "en"
      }
    ]
  },
  "cdif:physicalDataType": [
    {
      "@type": ["cdi:ControlledVocabularyEntry"],
      "cdi:entryValue": ["xsd:decimal"]
    }
  ],
  "cdi:takesSubstantiveValuesFrom": { "@id": "ex:value-domain/decimal-eV" },
  "cdif:simpleUnitOfMeasure": "eV",
  "cdif:uses": ["xas:monochromatorEnergyConcept"],
  "cdi:role": "Attribute",
  "cdi:qualifies": { "@id": "ex:temperatureVariable" }
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
  "cdi:name": [
    {
      "@type": [
        "cdi:ObjectName"
      ],
      "cdi:name": "energy"
    }
  ],
  "cdi:displayLabel": [
    {
      "@type": [
        "cdi:LabelForDisplay"
      ],
      "cdi:content": "Monochromator energy",
      "cdi:language": "en"
    }
  ],
  "cdi:definition": {
    "@type": [
      "cdi:InternationalString"
    ],
    "cdi:languageSpecificString": [
      {
        "@type": [
          "cdi:LanguageString"
        ],
        "cdi:content": "Incident photon energy selected by the monochromator during the XAS scan.",
        "cdi:language": "en"
      }
    ]
  },
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
  "cdi:role": "Attribute",
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
    cdi:definition [ a cdi:InternationalString ;
            cdi:languageSpecificString [ a cdi:LanguageString ;
                    cdi:content "Incident photon energy selected by the monochromator during the XAS scan." ;
                    cdi:language "en" ] ] ;
    cdi:displayLabel [ a cdi:LabelForDisplay ;
            cdi:content "Monochromator energy" ;
            cdi:language "en" ] ;
    cdi:identifier [ a cdi:Identifier ;
            cdi:uri "https://xas.org/dictionary/monochromatorEnergy" ] ;
    cdi:name [ a cdi:ObjectName ;
            cdi:name "energy" ] ;
    cdi:qualifies ex:temperatureVariable ;
    cdi:role "Attribute" ;
    cdi:takesSubstantiveValuesFrom <https://example.org/value-domain/decimal-eV> ;
    schema1:alternateName "Monochromator energy" ;
    schema1:description "Incident photon energy selected by the monochromator during the XAS scan." ;
    schema1:name "energy" ;
    schema1:propertyID "xas:monochromatorEnergyConcept" ;
    schema1:unitText "eV" ;
    cdif:physicalDataType [ a cdi:ControlledVocabularyEntry ;
            cdi:entryValue "xsd:decimal" ] ;
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
  cdi:role:
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
      that this variable measures or represents.
  cdi:qualifies:
    type: object
    properties:
      '@id':
        type: string
    description: reference to an instance variable defined for this dataset
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

