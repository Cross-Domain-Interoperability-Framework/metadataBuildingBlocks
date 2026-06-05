
# CDIF Enumeration Domain (Schema)

`cdif.bbr.metadata.cdifDataType.cdifEnumerationDomain` *v0.1*

Extension point that documents a codification vocabulary as an enumerated value domain. Composes schemaorgProperties/identifier for cdi:identifier; cdif:references accepts a cdifProfile/cdifCodelist, a schemaorgProperties/definedTermSet, or an @id-only id-reference; cdi:purpose uses a plain string.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

# CDIF Enumeration Domain

A **CDIF Enumeration Domain** documents a codification vocabulary as an enumerated value domain — the set of permissible values a variable may take when those values are drawn from a controlled vocabulary, codelist, statistical classification, or SKOS concept scheme.

This is a CDIF profile of the DDI-CDI `EnumerationDomain` extension point. It is intentionally light at the root level (only `@type` is required) so that any codification — whether expressed as a SKOS `ConceptScheme`, a schema.org `DefinedTermSet`, or an `@id`-only reference to a domain defined elsewhere — can be advertised as a domain with the same shape. The detailed structure of the codification itself lives in the referenced BB (or external resource); this BB only carries the umbrella identity, naming, and intent properties.

## Structure

- `@type` must contain `"cdif:EnumerationDomain"`.
- `@id` — recommended URI for the domain itself.
- `cdif:identifier` — formal `schema:identifier` for the domain.
- `schema:name` — short human label.
- `cdif:references` *(required)* — anyOf an inline `skos:ConceptScheme` or an `@id`-only id-reference to a domain defined elsewhere. Points at the SKOS concept scheme whose concepts define the permitted values.
- `cdif:purpose` — short string describing intent/use.

## Relationship to other BBs

CDIF Enumeration Domain is the **abstract umbrella**; concrete codification BBs (e.g. the DDI-CDIF `CodeList` or `StatisticalClassification`) provide the actual content. Use this BB at points in the data-description graph where any codification will do; pin the specific codification BB when the value domain must be of a particular kind.

## Examples

### Minimal CDIF Enumeration Domain
Bare cdif:EnumerationDomain pointing at an external SKOS ConceptScheme
by @id reference. Schema only requires @type; the schema:name and
schema:inDefinedTermSet here meet the SHACL Warning-level recommendations.
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "cdif": "https://w3id.org/cdif/",
    "skos": "http://www.w3.org/2004/02/skos/core#",
    "ex": "https://example.org/"
  },
  "@type": ["cdif:EnumerationDomain"],
  "@id": "ex:enum-domain/iso3166",
  "schema:name": "ISO 3166-1 alpha-2 country codes",
  "cdif:references": {
    "@id": "https://www.iso.org/obp/ui/#iso:pub:PUB500001"
  }
}

```

#### jsonld
```jsonld
{
  "@context": [
    {
      "schema": "http://schema.org/",
      "cdif": "https://w3id.org/cdif/",
      "skos": "http://www.w3.org/2004/02/skos/core#"
    },
    "https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifDataType/cdifEnumerationDomain/context.jsonld",
    {
      "schema": "http://schema.org/",
      "cdif": "https://w3id.org/cdif/",
      "skos": "http://www.w3.org/2004/02/skos/core#",
      "ex": "https://example.org/"
    }
  ],
  "@type": [
    "cdif:EnumerationDomain"
  ],
  "@id": "ex:enum-domain/iso3166",
  "schema:name": "ISO 3166-1 alpha-2 country codes",
  "cdif:references": {
    "@id": "https://www.iso.org/obp/ui/#iso:pub:PUB500001"
  }
}
```

#### ttl
```ttl
@prefix cdif: <https://w3id.org/cdif/> .
@prefix schema1: <http://schema.org/> .

<https://example.org/enum-domain/iso3166> a cdif:EnumerationDomain ;
    schema1:name "ISO 3166-1 alpha-2 country codes" ;
    cdif:references <https://www.iso.org/obp/ui/#iso:pub:PUB500001> .


```


### Complete CDIF Enumeration Domain
EU-country EnumerationDomain exercising every schema property at the
root: cdi:identifier (schema:PropertyValue with propertyID/value/url),
schema:name, schema:inDefinedTermSet (inline skos:ConceptScheme), and
cdi:purpose (multilingual InternationalString).
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
    "cdif": "https://w3id.org/cdif/",
    "skos": "http://www.w3.org/2004/02/skos/core#",
    "ex": "https://example.org/"
  },
  "@type": ["cdif:EnumerationDomain"],
  "@id": "ex:enum-domain/iso3166-eu",
  "cdif:identifier": {
    "@type": ["schema:PropertyValue"],
    "schema:propertyID": "https://registry.identifiers.org/registry/cdif",
    "schema:value": "iso3166-eu",
    "schema:url": "https://example.org/enum-domain/iso3166-eu"
  },
  "schema:name": "ISO 3166-1 alpha-2 — EU subset",
  "cdif:references": {
    "@type": ["skos:ConceptScheme"],
    "@id": "https://example.org/concept-scheme/iso3166-eu",
    "skos:prefLabel": [
      { "@value": "ISO 3166-1 alpha-2 — EU subset", "@language": "en" },
      { "@value": "ISO 3166-1 alpha-2 — Sous-ensemble UE", "@language": "fr" }
    ],
    "skos:hasTopConcept": [
      { "@id": "ex:concept/DE" },
      { "@id": "ex:concept/FR" }
    ]
  },
  "cdif:purpose": "Subset of ISO 3166-1 alpha-2 country codes covering EU member states."
}

```

#### jsonld
```jsonld
{
  "@context": [
    {
      "schema": "http://schema.org/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "cdif": "https://w3id.org/cdif/",
      "skos": "http://www.w3.org/2004/02/skos/core#"
    },
    "https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifDataType/cdifEnumerationDomain/context.jsonld",
    {
      "schema": "http://schema.org/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "cdif": "https://w3id.org/cdif/",
      "skos": "http://www.w3.org/2004/02/skos/core#",
      "ex": "https://example.org/"
    }
  ],
  "@type": [
    "cdif:EnumerationDomain"
  ],
  "@id": "ex:enum-domain/iso3166-eu",
  "cdif:identifier": {
    "@type": [
      "schema:PropertyValue"
    ],
    "schema:propertyID": "https://registry.identifiers.org/registry/cdif",
    "schema:value": "iso3166-eu",
    "schema:url": "https://example.org/enum-domain/iso3166-eu"
  },
  "schema:name": "ISO 3166-1 alpha-2 \u2014 EU subset",
  "cdif:references": {
    "@type": [
      "skos:ConceptScheme"
    ],
    "@id": "https://example.org/concept-scheme/iso3166-eu",
    "skos:prefLabel": [
      {
        "@value": "ISO 3166-1 alpha-2 \u2014 EU subset",
        "@language": "en"
      },
      {
        "@value": "ISO 3166-1 alpha-2 \u2014 Sous-ensemble UE",
        "@language": "fr"
      }
    ],
    "skos:hasTopConcept": [
      {
        "@id": "ex:concept/DE"
      },
      {
        "@id": "ex:concept/FR"
      }
    ]
  },
  "cdif:purpose": "Subset of ISO 3166-1 alpha-2 country codes covering EU member states."
}
```

#### ttl
```ttl
@prefix cdif: <https://w3id.org/cdif/> .
@prefix schema1: <http://schema.org/> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .

<https://example.org/enum-domain/iso3166-eu> a cdif:EnumerationDomain ;
    schema1:name "ISO 3166-1 alpha-2 — EU subset" ;
    cdif:identifier [ a schema1:PropertyValue ;
            schema1:propertyID "https://registry.identifiers.org/registry/cdif" ;
            schema1:url "https://example.org/enum-domain/iso3166-eu" ;
            schema1:value "iso3166-eu" ] ;
    cdif:purpose "Subset of ISO 3166-1 alpha-2 country codes covering EU member states." ;
    cdif:references <https://example.org/concept-scheme/iso3166-eu> .

<https://example.org/concept-scheme/iso3166-eu> a skos:ConceptScheme ;
    skos:hasTopConcept <https://example.org/concept/DE>,
        <https://example.org/concept/FR> ;
    skos:prefLabel "ISO 3166-1 alpha-2 — EU subset"@en,
        "ISO 3166-1 alpha-2 — Sous-ensemble UE"@fr .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: CDIF Enumeration Domain
description: A base class acting as an extension point to allow a codification vocabulary
  to be documented as enumerated value domain.
type: object
properties:
  '@type':
    type: array
    items:
      type: string
    contains:
      const: cdif:EnumerationDomain
    minItems: 1
  '@id':
    type: string
    description: Identifier for this EnumerationDomain node
  cdif:identifier:
    $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/identifier/schema.yaml
    description: Identifier for this enumerated (categorical) domain.
    x-jsonld-id: https://w3id.org/cdif/identifier
  schema:name:
    type: string
    description: Human understandable name (liguistic signifier, word, phrase, or
      mnemonic).
    x-jsonld-id: http://schema.org/name
  cdif:references:
    description: CDIF codelist (skos:ConceptScheme) whose concepts define the allowed
      values of this enumeration domain.
    anyOf:
    - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/profiles/cdifProfile/cdifCodelist/schema.yaml
    - type: object
      description: object reference via URI or URI fragment referencing an @id in
        the same document
      properties:
        '@id':
          type: string
    x-jsonld-id: https://w3id.org/cdif/references
  cdif:purpose:
    type: string
    description: Intent or reason for the object/the description of the object.
    x-jsonld-id: https://w3id.org/cdif/purpose
required:
- '@type'
- cdif:references
x-jsonld-prefixes:
  schema: http://schema.org/
  cdi: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/
  cdif: https://w3id.org/cdif/
  skos: http://www.w3.org/2004/02/skos/core#

```

Links to the schema:

* YAML version: [schema.yaml](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifDataType/cdifEnumerationDomain/schema.json)
* JSON version: [schema.json](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifDataType/cdifEnumerationDomain/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "schema": "http://schema.org/",
    "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
    "cdif": "https://w3id.org/cdif/",
    "skos": "http://www.w3.org/2004/02/skos/core#",
    "dcterms": "http://purl.org/dc/terms/",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifDataType/cdifEnumerationDomain/context.jsonld)

## Sources

* [DDI-CDI 1.0 Specification](https://ddialliance.org/Specification/DDI-CDI/1.0/)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/Cross-Domain-Interoperability-Framework/metadataBuildingBlocks](https://github.com/Cross-Domain-Interoperability-Framework/metadataBuildingBlocks)
* Path: `_sources/cdifDataType/cdifEnumerationDomain`

