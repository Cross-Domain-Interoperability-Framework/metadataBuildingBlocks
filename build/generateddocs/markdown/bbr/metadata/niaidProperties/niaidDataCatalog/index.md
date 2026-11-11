
# NIAID data catalog (Schema)

`cdif.bbr.metadata.niaidProperties.niaidDataCatalog` *v1.0*

A schema:DataCatalog that a NIAID Data Discovery Portal dataset comes from, with where the dataset is archived there and the version of the catalog the portal harvested.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

## NIAID data catalog

A schema:DataCatalog that a NIAID Data Discovery Portal dataset comes from, with where the dataset is archived there and the version of the catalog the portal harvested.

Used by [`niaidDataset`](../niaidDataset/) for `schema:includedInDataCatalog` on a dataset. The
[`cdifNIAID`](../../profiles/cdifCompositeProfile/cdifNIAID/) profile composes
`niaidDataset` with `cdifCore`. `converters/NIAID/harvest_niaid_to_cdif.py` produces
these objects, and gives the type to one the portal left untyped.

| Property | Value | Meaning |
|---|---|---|
| `schema:archivedAt` | URL | The dataset's page in this catalog (a schema.org property the portal uses here) |
| `nde:versionDate` | date | The version of the catalog the portal harvested |

## Examples

### Minimal NIAID catalog
The catalog with the fewest properties among the converted NIAID examples: schema:includedInDataCatalog of
converters/NIAID/niaidExamples/vivli_40b1791e-dd8a-46ad-b438-35fd21b4d4bb.json, converted by harvest_niaid_to_cdif.py.
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
    "schema:DataCatalog"
  ],
  "schema:archivedAt": "https://doi.org/10.25934/00003631",
  "schema:name": "Vivli",
  "schema:url": "https://vivli.org/",
  "nde:versionDate": "2026-10-24"
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
    "https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/niaidProperties/niaidDataCatalog/context.jsonld",
    {
      "schema": "http://schema.org/",
      "nde": "https://discovery.biothings.io/ns/nde/",
      "bios": "https://bioschemas.org/",
      "cdifniaid": "https://w3id.org/cdif/niaid/terms/"
    }
  ],
  "@type": [
    "schema:DataCatalog"
  ],
  "schema:archivedAt": "https://doi.org/10.25934/00003631",
  "schema:name": "Vivli",
  "schema:url": "https://vivli.org/",
  "nde:versionDate": "2026-10-24"
}
```

#### ttl
```ttl
@prefix nde: <https://discovery.biothings.io/ns/nde/> .
@prefix schema1: <http://schema.org/> .

[] a schema1:DataCatalog ;
    schema1:archivedAt "https://doi.org/10.25934/00003631" ;
    schema1:name "Vivli" ;
    schema1:url "https://vivli.org/" ;
    nde:versionDate "2026-10-24" .


```


### Complete NIAID catalog
The catalog with the most NIAID properties, then the most properties among the converted NIAID examples: schema:includedInDataCatalog of
converters/NIAID/niaidExamples/figshare_10932983.json, converted by harvest_niaid_to_cdif.py.
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
    "schema:DataCatalog"
  ],
  "schema:archivedAt": "https://figshare.com/articles/dataset/MOESM3_of_How_are_nature_based_solutions_contributing_to_priority_societal_challenges_surrounding_human_well-being_in_the_United_Kingdom_a_systematic_map_protocol/10932983",
  "schema:name": "Figshare",
  "schema:url": "https://figshare.com",
  "nde:versionDate": "2026-10-23"
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
    "https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/niaidProperties/niaidDataCatalog/context.jsonld",
    {
      "schema": "http://schema.org/",
      "nde": "https://discovery.biothings.io/ns/nde/",
      "bios": "https://bioschemas.org/",
      "cdifniaid": "https://w3id.org/cdif/niaid/terms/"
    }
  ],
  "@type": [
    "schema:DataCatalog"
  ],
  "schema:archivedAt": "https://figshare.com/articles/dataset/MOESM3_of_How_are_nature_based_solutions_contributing_to_priority_societal_challenges_surrounding_human_well-being_in_the_United_Kingdom_a_systematic_map_protocol/10932983",
  "schema:name": "Figshare",
  "schema:url": "https://figshare.com",
  "nde:versionDate": "2026-10-23"
}
```

#### ttl
```ttl
@prefix nde: <https://discovery.biothings.io/ns/nde/> .
@prefix schema1: <http://schema.org/> .

[] a schema1:DataCatalog ;
    schema1:archivedAt "https://figshare.com/articles/dataset/MOESM3_of_How_are_nature_based_solutions_contributing_to_priority_societal_challenges_surrounding_human_well-being_in_the_United_Kingdom_a_systematic_map_protocol/10932983" ;
    schema1:name "Figshare" ;
    schema1:url "https://figshare.com" ;
    nde:versionDate "2026-10-23" .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: NIAID data catalog
description: 'A repository a NIAID Data Discovery Portal dataset comes from: its name
  and address, the dataset''s page there (schema:archivedAt), and the version of the
  catalog the portal harvested (nde:versionDate).'
type: object
properties:
  '@type':
    type: array
    items:
      type: string
    contains:
      const: schema:DataCatalog
    minItems: 1
  schema:name:
    type: string
    x-jsonld-id: http://schema.org/name
  schema:url:
    type: string
    x-jsonld-id: http://schema.org/url
  schema:archivedAt:
    description: The dataset's page in this catalog.
    type: string
    x-jsonld-id: http://schema.org/archivedAt
  nde:versionDate:
    description: The date of the version of the catalog the portal harvested.
    type: string
    x-jsonld-id: https://discovery.biothings.io/ns/nde/versionDate
required:
- '@type'
anyOf:
- required:
  - schema:name
- required:
  - schema:url
x-jsonld-prefixes:
  schema: http://schema.org/
  nde: https://discovery.biothings.io/ns/nde/
  bios: https://bioschemas.org/
  cdifniaid: https://w3id.org/cdif/niaid/terms/
x-bblocks-metadata:
  itemIdentifier: cdif.bbr.metadata.niaidProperties.niaidDataCatalog
  register: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/register.json
  version: '1.0'
  dateOfLastChange: '2026-11-11'

```

Links to the schema:

* YAML version: [schema.yaml](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/niaidProperties/niaidDataCatalog/schema.json)
* JSON version: [schema.json](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/niaidProperties/niaidDataCatalog/schema.yaml)


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
[context.jsonld](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/niaidProperties/niaidDataCatalog/context.jsonld)

## Sources

* [NIAID Data Ecosystem schemas](https://github.com/NIAID-Data-Ecosystem/nde-schemas)
* [NIAID Data Discovery Portal](https://data.niaid.nih.gov/)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/Cross-Domain-Interoperability-Framework/metadataBuildingBlocks](https://github.com/Cross-Domain-Interoperability-Framework/metadataBuildingBlocks)
* Path: `_sources/niaidProperties/niaidDataCatalog`

