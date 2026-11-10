
# NIAID place (Schema)

`cdif.bbr.metadata.niaidProperties.niaidPlace` *v1.0*

A schema:Place from the NIAID Data Discovery Portal's spatial coverage, with NIAID's administrative type.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

## NIAID place

A schema:Place from the NIAID Data Discovery Portal's spatial coverage, with NIAID's administrative type.

Used by [`niaidDataset`](../niaidDataset/) for `schema:spatialCoverage` on a dataset. The
[`cdifNIAID`](../../profiles/cdifCompositeProfile/cdifNIAID/) profile composes
`niaidDataset` with `cdifCore`. `converters/NIAID/harvest_niaid_to_cdif.py` produces
these objects, and gives the type to one the portal left untyped.

| Property | Value | Meaning |
|---|---|---|
| `nde:administrativeType` | text | The kind of administrative area, e.g. `country` |

The portal's `country` (given only by Project Tycho, on areas named by ISO 3166 code) becomes the place's name, and its `locationType` the name term's `schema:about`, so neither appears here.

## Examples

### Complete NIAID place
The place with the most NIAID properties, then the most properties among the converted NIAID examples: schema:spatialCoverage of
converters/NIAID/niaidExamples/dde_5ecff76765e122b0.json, converted by harvest_niaid_to_cdif.py.
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "nde": "https://discovery.biothings.io/ns/nde/",
    "bios": "https://bioschemas.org/",
    "cdifniaid": "https://w3id.org/cdif/niaid/terms/"
  },
  "@type": [
    "schema:Place",
    "schema:AdministrativeArea"
  ],
  "nde:administrativeType": "city",
  "schema:alternateName": [
    "Cebu, Philippines",
    "Cebu, Philippines"
  ],
  "schema:name": {
    "@type": [
      "schema:DefinedTerm"
    ],
    "schema:name": "Cebu City, Philippines",
    "schema:identifier": "Q1467",
    "schema:about": "study location"
  }
}

```

#### jsonld
```jsonld
{
  "@context": [
    {
      "schema": "http://schema.org/",
      "nde": "https://discovery.biothings.io/ns/nde/",
      "bios": "https://bioschemas.org/",
      "cdifniaid": "https://w3id.org/cdif/niaid/terms/"
    },
    "https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/niaidProperties/niaidPlace/context.jsonld",
    {
      "schema": "http://schema.org/",
      "nde": "https://discovery.biothings.io/ns/nde/",
      "bios": "https://bioschemas.org/",
      "cdifniaid": "https://w3id.org/cdif/niaid/terms/"
    }
  ],
  "@type": [
    "schema:Place",
    "schema:AdministrativeArea"
  ],
  "nde:administrativeType": "city",
  "schema:alternateName": [
    "Cebu, Philippines",
    "Cebu, Philippines"
  ],
  "schema:name": {
    "@type": [
      "schema:DefinedTerm"
    ],
    "schema:name": "Cebu City, Philippines",
    "schema:identifier": "Q1467",
    "schema:about": "study location"
  }
}
```

#### ttl
```ttl
@prefix nde: <https://discovery.biothings.io/ns/nde/> .
@prefix schema1: <http://schema.org/> .

[] a schema1:AdministrativeArea,
        schema1:Place ;
    schema1:alternateName "Cebu, Philippines" ;
    schema1:name [ a schema1:DefinedTerm ;
            schema1:about "study location" ;
            schema1:identifier "Q1467" ;
            schema1:name "Cebu City, Philippines" ] ;
    nde:administrativeType "city" .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: NIAID place
description: A place in a NIAID Data Discovery Portal dataset's spatial coverage.
  The portal types it AdministrativeArea; the converter adds schema:Place, which CDIF's
  spatial extent looks for. NIAID adds the kind of administrative area.
type: object
properties:
  '@type':
    type: array
    items:
      type: string
    contains:
      const: schema:Place
    minItems: 1
  nde:administrativeType:
    description: The kind of administrative area, e.g. country.
    type: string
    x-jsonld-id: https://discovery.biothings.io/ns/nde/administrativeType
required:
- '@type'
x-jsonld-prefixes:
  schema: http://schema.org/
  nde: https://discovery.biothings.io/ns/nde/
  bios: https://bioschemas.org/
  cdifniaid: https://w3id.org/cdif/niaid/terms/
x-bblocks-metadata:
  itemIdentifier: cdif.bbr.metadata.niaidProperties.niaidPlace
  register: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/register.json
  version: '1.0'
  dateOfLastChange: '2026-11-10'

```

Links to the schema:

* YAML version: [schema.yaml](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/niaidProperties/niaidPlace/schema.json)
* JSON version: [schema.json](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/niaidProperties/niaidPlace/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "schema": "http://schema.org/",
    "nde": "https://discovery.biothings.io/ns/nde/",
    "bios": "https://bioschemas.org/",
    "cdifniaid": "https://w3id.org/cdif/niaid/terms/",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/niaidProperties/niaidPlace/context.jsonld)

## Sources

* [NIAID Data Ecosystem schemas](https://github.com/NIAID-Data-Ecosystem/nde-schemas)
* [NIAID Data Discovery Portal](https://data.niaid.nih.gov/)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/Cross-Domain-Interoperability-Framework/metadataBuildingBlocks](https://github.com/Cross-Domain-Interoperability-Framework/metadataBuildingBlocks)
* Path: `_sources/niaidProperties/niaidPlace`

