
# DDI-CDI Controlled Vocabulary Entry (Schema)

`cdif.bbr.metadata.ddiCDIFProperties.ddi-cdif-controlled-vocabulary-entry` *v0.1*

Allows for unstructured content which may be an entry from an externally maintained controlled vocabulary.If the content is from a controlled vocabulary provide the code value of the entry, as well as a reference to the controlled vocabulary from which the value is taken. Provide as many of the identifying attributes as needed to adequately identify the controlled vocabulary. Note that DDI has published a number of controlled vocabularies applicable to several locations using the external controlled vocabulary entry structure. If the code portion of the controlled vocabulary entry is language specific (i.e. a list of keywords or subject headings) use language to specify that language. In most cases the code portion of an entry is not language specific although the description and usage may be managed in one or more languages. Use of shared controlled vocabularies helps support interoperability and machine actionability.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

DDI-CDI ControlledVocabularyEntry carries a single entry drawn from a controlled vocabulary, or a free-text term when no vocabulary applies. The root `cdi:ControlledVocabularyEntry` holds the value in `cdi:entryValue`, an optional `cdi:entryReference` to the specific item, `cdi:vocabulary` referencing the controlled vocabulary itself, and `cdi:valueForOther` for cases where the chosen entry is "Other" and a more specific value is needed.

It is the standalone-BB form of the `ControlledVocabularyEntry` data type defined in `ddicdiDataTypes`, intended for use when a controlled-vocabulary value needs its own `@id` and graph node rather than being embedded inline. Most uses of controlled-vocabulary terms inside DDI-CDI BBs reference the inline `$defs/ControlledVocabularyEntry` from `ddicdiDataTypes` instead.

## Examples

### Minimal ControlledVocabularyEntry
Bare entry value with no vocabulary or reference — useful when the term
is well-known and does not need an external definition.
#### json
```json
{
  "@context": {
    "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/"
  },
  "@type": ["cdi:ControlledVocabularyEntry"],
  "cdi:entryValue": ["MeasureComponent"]
}

```

#### jsonld
```jsonld
{
  "@context": [
    {
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/"
    },
    "https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiCDIFProperties/ddi-cdif-controlled-vocabulary-entry/context.jsonld",
    {
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/"
    }
  ],
  "@type": [
    "cdi:ControlledVocabularyEntry"
  ],
  "cdi:entryValue": [
    "MeasureComponent"
  ]
}
```

#### ttl
```ttl
@prefix cdi: <http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/> .

[] a cdi:ControlledVocabularyEntry ;
    cdi:entryValue "MeasureComponent" .


```


### Complete ControlledVocabularyEntry
DDI-CDI DataStructureComponent-role entry exercising every property:
cdi:vocabulary (the CV root), cdi:entryReference (resolvable URI for
the specific term), cdi:entryValue, cdi:name, and cdi:valueForOther.
#### json
```json
{
  "@context": {
    "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
    "ex": "https://example.org/"
  },
  "@type": ["cdi:ControlledVocabularyEntry"],
  "@id": "ex:cve/role/measure",
  "cdi:name": "DDI-CDI DataStructureComponent role vocabulary",
  "cdi:vocabulary": {
    "@type": ["cdif:Reference"],
    "cdi:uri": "https://vocabularies.cessda.eu/v2/vocabularies/DataStructureComponentRole",
    "cdi:description": "CESSDA controlled vocabulary for DDI-CDI data structure component roles."
  },
  "cdi:entryReference": [
    {
      "@type": ["cdif:Reference"],
      "cdi:uri": "https://vocabularies.cessda.eu/v2/vocabularies/DataStructureComponentRole/MeasureComponent",
      "cdi:description": "Vocabulary item for the MeasureComponent role."
    }
  ],
  "cdi:entryValue": ["MeasureComponent"],
  "cdi:valueForOther": "AggregatedMeasureComponent"
}

```

#### jsonld
```jsonld
{
  "@context": [
    {
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/"
    },
    "https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiCDIFProperties/ddi-cdif-controlled-vocabulary-entry/context.jsonld",
    {
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "ex": "https://example.org/"
    }
  ],
  "@type": [
    "cdi:ControlledVocabularyEntry"
  ],
  "@id": "ex:cve/role/measure",
  "cdi:name": "DDI-CDI DataStructureComponent role vocabulary",
  "cdi:vocabulary": {
    "@type": [
      "cdif:Reference"
    ],
    "cdi:uri": "https://vocabularies.cessda.eu/v2/vocabularies/DataStructureComponentRole",
    "cdi:description": "CESSDA controlled vocabulary for DDI-CDI data structure component roles."
  },
  "cdi:entryReference": [
    {
      "@type": [
        "cdif:Reference"
      ],
      "cdi:uri": "https://vocabularies.cessda.eu/v2/vocabularies/DataStructureComponentRole/MeasureComponent",
      "cdi:description": "Vocabulary item for the MeasureComponent role."
    }
  ],
  "cdi:entryValue": [
    "MeasureComponent"
  ],
  "cdi:valueForOther": "AggregatedMeasureComponent"
}
```

#### ttl
```ttl
@prefix cdi: <http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/> .

<https://example.org/cve/role/measure> a cdi:ControlledVocabularyEntry ;
    cdi:entryReference [ a <cdif:Reference> ;
            cdi:description "Vocabulary item for the MeasureComponent role." ;
            cdi:uri "https://vocabularies.cessda.eu/v2/vocabularies/DataStructureComponentRole/MeasureComponent" ] ;
    cdi:entryValue "MeasureComponent" ;
    cdi:name "DDI-CDI DataStructureComponent role vocabulary" ;
    cdi:valueForOther "AggregatedMeasureComponent" ;
    cdi:vocabulary [ a <cdif:Reference> ;
            cdi:description "CESSDA controlled vocabulary for DDI-CDI data structure component roles." ;
            cdi:uri "https://vocabularies.cessda.eu/v2/vocabularies/DataStructureComponentRole" ] .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: DDI-CDI Controlled Vocabulary Entry
description: Allows for unstructured content which may be an entry from an externally
  maintained controlled vocabulary.If the content is from a controlled vocabulary
  provide the code value of the entry, as well as a reference to the controlled vocabulary
  from which the value is taken. Provide as many of the identifying attributes as
  needed to adequately identify the controlled vocabulary. Note that DDI has published
  a number of controlled vocabularies applicable to several locations using the external
  controlled vocabulary entry structure. If the code portion of the controlled vocabulary
  entry is language specific (i.e. a list of keywords or subject headings) use language
  to specify that language. In most cases the code portion of an entry is not language
  specific although the description and usage may be managed in one or more languages.
  Use of shared controlled vocabularies helps support interoperability and machine
  actionability.
type: object
properties:
  '@type':
    type: array
    items:
      type: string
    contains:
      const: cdi:ControlledVocabularyEntry
    minItems: 1
  '@id':
    type: string
    description: Identifier for this ControlledVocabularyEntry node
  cdi:entryReference:
    type: array
    items:
      $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiCDIFProperties/ddi-cdif-data-types/schema.yaml#/$defs/Reference
    minItems: 1
    description: A reference to the specific item in the vocabulary referenced in
      the vocabulary attribute, using a URI or other resolvable identifier.
    x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/entryReference
  cdi:entryValue:
    type: array
    items:
      type: string
    minItems: 1
    description: The value of the entry of the controlled vocabulary. If no controlled
      vocabulary is used the term is entered here and none of the properties defining
      the controlled vocabulary location are used.
    x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/entryValue
  cdi:name:
    type: string
    description: The name of the code list (controlled vocabulary).
    x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/name
  cdi:valueForOther:
    type: string
    description: If the value of the string is "Other" or the equivalent from the
      codelist, this attribute can provide a more specific value not found in the
      codelist.
    x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/valueForOther
  cdi:vocabulary:
    $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiCDIFProperties/ddi-cdif-data-types/schema.yaml#/$defs/Reference
    description: A reference to the external controlled vocabulary, using a URI or
      other resolvable identifier.
    x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/vocabulary
required:
- '@type'
x-jsonld-prefixes:
  cdi: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/

```

Links to the schema:

* YAML version: [schema.yaml](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiCDIFProperties/ddi-cdif-controlled-vocabulary-entry/schema.json)
* JSON version: [schema.json](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiCDIFProperties/ddi-cdif-controlled-vocabulary-entry/schema.yaml)


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
[context.jsonld](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiCDIFProperties/ddi-cdif-controlled-vocabulary-entry/context.jsonld)

## Sources

* [DDI-CDI 1.0 Specification](https://ddialliance.org/Specification/DDI-CDI/1.0/)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/Cross-Domain-Interoperability-Framework/metadataBuildingBlocks](https://github.com/Cross-Domain-Interoperability-Framework/metadataBuildingBlocks)
* Path: `_sources/ddiCDIFProperties/ddi-cdif-controlled-vocabulary-entry`

