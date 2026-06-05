
# CDIF Concept or Term (Schema)

`cdif.bbr.metadata.cdifDataType.cdifConceptOrTerm` *v0.1*

Shared union shape for a controlled-vocabulary value: a SKOS concept referenced by '@id', a schema:DefinedTerm node, or an inline cdif:Concept. Replaces the duplicate 'cdifConceptOrTerm' $defs that previously appeared in cdifInstanceVariable, cdifRepresentedVariable, cdifDataStructureComponent, cdifReference, cdifPhysicalMapping, cdifStatistics, cdifOpenApi, cdifCore, and cdifDiscovery.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

## CDIF Concept or Term

A shared union shape used wherever a CDIF property accepts a controlled-vocabulary value. The property's value can be:

1. **A SKOS concept referenced by URI** — an object carrying just an `@id` pointing at a `skos:Concept` in some published vocabulary.
2. **A `schema:DefinedTerm`** — the schema.org DefinedTerm shape inherited from the `schemaorgProperties/definedTerm` building block, used to inline name/identifier/termCode alongside a `inDefinedTermSet` pointer.
3. **An inline `cdif:Concept`** — the `cdifConcept` shape from the CDIF ConceptScheme profile, used to inline a complete concept definition (preferred label, alternate labels, definition, broader/narrower, etc.) directly in the metadata record.

### When to use

`$ref` this building block from any property that previously accepted the inlined `cdifConceptOrTerm` `anyOf` union. The intent is to consolidate that duplicated shape — every CDIF building block that needs a concept-or-term value should reference this single definition rather than redefining it locally.

### Migration note

Prior to 2026-06-05, this union appeared as a local `$defs.cdifConceptOrTerm` entry inside nine separate building-block schemas (`cdifInstanceVariable`, `cdifRepresentedVariable`, `cdifDataStructureComponent`, `cdifReference`, `cdifPhysicalMapping`, `cdifStatistics`, `cdifOpenApi`, `cdifCore`, `cdifDiscovery`). Each of those local `$defs` is now a single-line `$ref` delegation to this BB, so existing in-document `#/$defs/cdifConceptOrTerm` references continue to resolve unchanged.

## Examples

### SKOS concept by URI reference
Minimal form: a single '@id' pointing at a SKOS concept in a published
vocabulary (here, a NERC P01 parameter).
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/"
  },
  "@id": "http://vocab.nerc.ac.uk/collection/P01/current/TEMPST01/"
}

```

#### jsonld
```jsonld
{
  "@context": [
    {
      "schema": "http://schema.org/"
    },
    "https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifDataType/cdifConceptOrTerm/context.jsonld",
    {
      "schema": "http://schema.org/"
    }
  ],
  "@id": "http://vocab.nerc.ac.uk/collection/P01/current/TEMPST01/"
}
```

#### ttl
```ttl


```


### schema:DefinedTerm node
A schema:DefinedTerm with a name, an identifier URI, and a pointer to the
enclosing DefinedTermSet. Inline form used when the consumer should be
able to render a label without dereferencing the URI.
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/"
  },
  "@type": [
    "schema:DefinedTerm"
  ],
  "schema:name": "Sea Water Temperature",
  "schema:identifier": "http://vocab.nerc.ac.uk/collection/P01/current/TEMPST01/",
  "schema:inDefinedTermSet": "http://vocab.nerc.ac.uk/collection/P01/"
}

```

#### jsonld
```jsonld
{
  "@context": [
    {
      "schema": "http://schema.org/"
    },
    "https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifDataType/cdifConceptOrTerm/context.jsonld",
    {
      "schema": "http://schema.org/"
    }
  ],
  "@type": [
    "schema:DefinedTerm"
  ],
  "schema:name": "Sea Water Temperature",
  "schema:identifier": "http://vocab.nerc.ac.uk/collection/P01/current/TEMPST01/",
  "schema:inDefinedTermSet": "http://vocab.nerc.ac.uk/collection/P01/"
}
```

#### ttl
```ttl
@prefix schema1: <http://schema.org/> .

[] a schema1:DefinedTerm ;
    schema1:identifier "http://vocab.nerc.ac.uk/collection/P01/current/TEMPST01/" ;
    schema1:inDefinedTermSet "http://vocab.nerc.ac.uk/collection/P01/" ;
    schema1:name "Sea Water Temperature" .


```


### Inline cdif:Concept
Fully inline concept: prefLabel + definition embedded directly in the
metadata record. Use when the concept is not (yet) published in an
external vocabulary.
#### json
```json
{
  "@context": {
    "skos": "http://www.w3.org/2004/02/skos/core#",
    "cdif": "https://w3id.org/cdif/"
  },
  "@type": [
    "skos:Concept"
  ],
  "@id": "https://example.org/concepts/sea-water-temperature",
  "skos:prefLabel": "Sea water temperature",
  "skos:definition": "The temperature of a water sample collected from the ocean."
}

```

#### jsonld
```jsonld
{
  "@context": [
    {
      "skos": "http://www.w3.org/2004/02/skos/core#",
      "cdif": "https://w3id.org/cdif/"
    },
    "https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifDataType/cdifConceptOrTerm/context.jsonld",
    {
      "skos": "http://www.w3.org/2004/02/skos/core#",
      "cdif": "https://w3id.org/cdif/"
    }
  ],
  "@type": [
    "skos:Concept"
  ],
  "@id": "https://example.org/concepts/sea-water-temperature",
  "skos:prefLabel": "Sea water temperature",
  "skos:definition": "The temperature of a water sample collected from the ocean."
}
```

#### ttl
```ttl
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .

<https://example.org/concepts/sea-water-temperature> a skos:Concept ;
    skos:definition "The temperature of a water sample collected from the ocean." ;
    skos:prefLabel "Sea water temperature" .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
description: A SKOS concept identified by URI, a schema:DefinedTerm, or an inline
  cdif:Concept. Shared shape used wherever a CDIF property carries either a controlled-vocabulary
  reference or an inline concept definition.
anyOf:
- type: object
  properties:
    '@id':
      type: string
      description: reference to a skos concept for the data type
- $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/definedTerm/schema.yaml
- $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/profiles/cdifProfile/cdifConceptScheme/schema.yaml#/$defs/cdifConcept

```

Links to the schema:

* YAML version: [schema.yaml](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifDataType/cdifConceptOrTerm/schema.json)
* JSON version: [schema.json](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifDataType/cdifConceptOrTerm/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "schema": "http://schema.org/",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifDataType/cdifConceptOrTerm/context.jsonld)

## Sources

* [SKOS Concept](https://www.w3.org/TR/skos-reference/)
* [schema.org DefinedTerm](https://schema.org/DefinedTerm)
* [CDIF ConceptScheme profile (cdif:Concept)](https://github.com/Cross-Domain-Interoperability-Framework/profile-conceptscheme)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/Cross-Domain-Interoperability-Framework/metadataBuildingBlocks](https://github.com/Cross-Domain-Interoperability-Framework/metadataBuildingBlocks)
* Path: `_sources/cdifDataType/cdifConceptOrTerm`

