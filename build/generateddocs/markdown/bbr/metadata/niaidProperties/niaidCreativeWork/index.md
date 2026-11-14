
# NIAID creative work (Schema)

`cdif.bbr.metadata.niaidProperties.niaidCreativeWork` *v1.0*

A schema:CreativeWork or ScholarlyArticle cited by or citing a dataset, with the NIAID Data Discovery Portal's PubMed id, DOI and journal names.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

## NIAID creative work

A schema:CreativeWork or ScholarlyArticle cited by or citing a dataset, with the NIAID Data Discovery Portal's PubMed id, DOI and journal names.

Used by [`niaidDataset`](../niaidDataset/) for `schema:citation` and `nde:citedBy` on a dataset. The
[`cdifNIAID`](../../profiles/cdifCompositeProfile/cdifNIAID/) profile composes
`niaidDataset` with `cdifCore`. `converters/NIAID/harvest_niaid_to_cdif.py` produces
these objects, and gives the type to one the portal left untyped.

| Property | Value | Meaning |
|---|---|---|
| `nde:pmid` | text, digits | The PubMed id |
| `nde:doi` | text | The DOI, as the portal gives it |
| `nde:journalName` | text | The journal's name |
| `nde:journalNameAbbrev` | text | The journal's abbreviated name |

CDIF's own citation rules come from cdifCore; this block adds only the NIAID properties and the type.

## Examples

### Minimal NIAID cited work
The cited work with the fewest properties among the converted NIAID examples: schema:citation of
converters/NIAID/niaidExamples/pxd061439.json, converted by harvest_niaid_to_cdif.py.
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
    "schema:ScholarlyArticle"
  ],
  "nde:pmid": "40451765"
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
    "https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/niaidProperties/niaidCreativeWork/context.jsonld",
    {
      "schema": "http://schema.org/",
      "nde": "https://discovery.biothings.io/ns/nde/",
      "bios": "https://bioschemas.org/",
      "cdifniaid": "https://w3id.org/cdif/niaid/terms/"
    }
  ],
  "@type": [
    "schema:ScholarlyArticle"
  ],
  "nde:pmid": "40451765"
}
```

#### ttl
```ttl
@prefix nde: <https://discovery.biothings.io/ns/nde/> .
@prefix schema1: <http://schema.org/> .

[] a schema1:ScholarlyArticle ;
    nde:pmid "40451765" .


```


### Complete NIAID cited work
The cited work with the most NIAID properties, then the most properties among the converted NIAID examples: schema:citation of
converters/NIAID/niaidExamples/empiar-10514.json, converted by harvest_niaid_to_cdif.py.
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
    "schema:ScholarlyArticle"
  ],
  "schema:author": [
    {
      "@type": [
        "schema:Person"
      ],
      "schema:name": "Melero R"
    },
    {
      "@type": [
        "schema:Person"
      ],
      "schema:name": "Sorzano COS"
    },
    {
      "@type": [
        "schema:Person"
      ],
      "schema:name": "Foster B"
    },
    {
      "@type": [
        "schema:Person"
      ],
      "schema:name": "Vilas JL"
    },
    {
      "@type": [
        "schema:Person"
      ],
      "schema:name": "Martínez M"
    },
    {
      "@type": [
        "schema:Person"
      ],
      "schema:name": "Marabini R"
    },
    {
      "@type": [
        "schema:Person"
      ],
      "schema:name": "Ramírez-Aportela E"
    },
    {
      "@type": [
        "schema:Person"
      ],
      "schema:name": "Sanchez-Garcia R"
    },
    {
      "@type": [
        "schema:Person"
      ],
      "schema:name": "Herreros D"
    },
    {
      "@type": [
        "schema:Person"
      ],
      "schema:name": "Del Caño L"
    },
    {
      "@type": [
        "schema:Person"
      ],
      "schema:name": "Losana P"
    },
    {
      "@type": [
        "schema:Person"
      ],
      "schema:name": "Fonseca-Reyna YC"
    },
    {
      "@type": [
        "schema:Person"
      ],
      "schema:name": "Conesa P"
    },
    {
      "@type": [
        "schema:Person"
      ],
      "schema:name": "Wrapp D"
    },
    {
      "@type": [
        "schema:Person"
      ],
      "schema:name": "Chacon P"
    },
    {
      "@type": [
        "schema:Person"
      ],
      "schema:name": "McLellan JS"
    },
    {
      "@type": [
        "schema:Person"
      ],
      "schema:name": "Tagare HD"
    },
    {
      "@type": [
        "schema:Person"
      ],
      "schema:name": "Carazo JM"
    }
  ],
  "schema:datePublished": "2020",
  "nde:doi": "10.1107/s2052252520012725",
  "schema:issueNumber": "Pt 6",
  "nde:journalName": "IUCrJ",
  "nde:journalNameAbbrev": "IUCrJ",
  "schema:name": "Continuous flexibility analysis of SARS-CoV-2 spike prefusion structures",
  "nde:pmid": "33063791",
  "schema:url": "https://doi.org/10.1107/s2052252520012725",
  "schema:volumeNumber": "7"
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
    "https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/niaidProperties/niaidCreativeWork/context.jsonld",
    {
      "schema": "http://schema.org/",
      "nde": "https://discovery.biothings.io/ns/nde/",
      "bios": "https://bioschemas.org/",
      "cdifniaid": "https://w3id.org/cdif/niaid/terms/"
    }
  ],
  "@type": [
    "schema:ScholarlyArticle"
  ],
  "schema:author": [
    {
      "@type": [
        "schema:Person"
      ],
      "schema:name": "Melero R"
    },
    {
      "@type": [
        "schema:Person"
      ],
      "schema:name": "Sorzano COS"
    },
    {
      "@type": [
        "schema:Person"
      ],
      "schema:name": "Foster B"
    },
    {
      "@type": [
        "schema:Person"
      ],
      "schema:name": "Vilas JL"
    },
    {
      "@type": [
        "schema:Person"
      ],
      "schema:name": "Mart\u00ednez M"
    },
    {
      "@type": [
        "schema:Person"
      ],
      "schema:name": "Marabini R"
    },
    {
      "@type": [
        "schema:Person"
      ],
      "schema:name": "Ram\u00edrez-Aportela E"
    },
    {
      "@type": [
        "schema:Person"
      ],
      "schema:name": "Sanchez-Garcia R"
    },
    {
      "@type": [
        "schema:Person"
      ],
      "schema:name": "Herreros D"
    },
    {
      "@type": [
        "schema:Person"
      ],
      "schema:name": "Del Ca\u00f1o L"
    },
    {
      "@type": [
        "schema:Person"
      ],
      "schema:name": "Losana P"
    },
    {
      "@type": [
        "schema:Person"
      ],
      "schema:name": "Fonseca-Reyna YC"
    },
    {
      "@type": [
        "schema:Person"
      ],
      "schema:name": "Conesa P"
    },
    {
      "@type": [
        "schema:Person"
      ],
      "schema:name": "Wrapp D"
    },
    {
      "@type": [
        "schema:Person"
      ],
      "schema:name": "Chacon P"
    },
    {
      "@type": [
        "schema:Person"
      ],
      "schema:name": "McLellan JS"
    },
    {
      "@type": [
        "schema:Person"
      ],
      "schema:name": "Tagare HD"
    },
    {
      "@type": [
        "schema:Person"
      ],
      "schema:name": "Carazo JM"
    }
  ],
  "schema:datePublished": "2020",
  "nde:doi": "10.1107/s2052252520012725",
  "schema:issueNumber": "Pt 6",
  "nde:journalName": "IUCrJ",
  "nde:journalNameAbbrev": "IUCrJ",
  "schema:name": "Continuous flexibility analysis of SARS-CoV-2 spike prefusion structures",
  "nde:pmid": "33063791",
  "schema:url": "https://doi.org/10.1107/s2052252520012725",
  "schema:volumeNumber": "7"
}
```

#### ttl
```ttl
@prefix nde: <https://discovery.biothings.io/ns/nde/> .
@prefix schema1: <http://schema.org/> .

[] a schema1:ScholarlyArticle ;
    schema1:author [ a schema1:Person ;
            schema1:name "Ramírez-Aportela E" ],
        [ a schema1:Person ;
            schema1:name "Vilas JL" ],
        [ a schema1:Person ;
            schema1:name "Melero R" ],
        [ a schema1:Person ;
            schema1:name "Wrapp D" ],
        [ a schema1:Person ;
            schema1:name "Marabini R" ],
        [ a schema1:Person ;
            schema1:name "McLellan JS" ],
        [ a schema1:Person ;
            schema1:name "Tagare HD" ],
        [ a schema1:Person ;
            schema1:name "Losana P" ],
        [ a schema1:Person ;
            schema1:name "Chacon P" ],
        [ a schema1:Person ;
            schema1:name "Carazo JM" ],
        [ a schema1:Person ;
            schema1:name "Fonseca-Reyna YC" ],
        [ a schema1:Person ;
            schema1:name "Conesa P" ],
        [ a schema1:Person ;
            schema1:name "Foster B" ],
        [ a schema1:Person ;
            schema1:name "Martínez M" ],
        [ a schema1:Person ;
            schema1:name "Sanchez-Garcia R" ],
        [ a schema1:Person ;
            schema1:name "Sorzano COS" ],
        [ a schema1:Person ;
            schema1:name "Herreros D" ],
        [ a schema1:Person ;
            schema1:name "Del Caño L" ] ;
    schema1:datePublished "2020" ;
    schema1:issueNumber "Pt 6" ;
    schema1:name "Continuous flexibility analysis of SARS-CoV-2 spike prefusion structures" ;
    schema1:url "https://doi.org/10.1107/s2052252520012725" ;
    schema1:volumeNumber "7" ;
    nde:doi "10.1107/s2052252520012725" ;
    nde:journalName "IUCrJ" ;
    nde:journalNameAbbrev "IUCrJ" ;
    nde:pmid "33063791" .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: NIAID creative work
description: A work that a NIAID Data Discovery Portal dataset cites or is cited by,
  with the portal's PubMed id, DOI and journal names. The portal types these as ScholarlyArticle
  or CreativeWork; JSON Schema cannot follow schema.org's subclass hierarchy, so both
  are listed.
type: object
properties:
  '@type':
    type: array
    items:
      type: string
    contains:
      enum:
      - schema:CreativeWork
      - schema:ScholarlyArticle
    minItems: 1
  schema:name:
    type: string
    x-jsonld-id: http://schema.org/name
  schema:url:
    type: string
    x-jsonld-id: http://schema.org/url
  nde:pmid:
    description: The PubMed id, digits only.
    $ref: '#/$defs/pmid'
    x-jsonld-id: https://discovery.biothings.io/ns/nde/pmid
  nde:doi:
    description: The DOI, as the portal gives it.
    $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/bioschemasProperties/bioschemasSample/schema.yaml#/$defs/texts
    x-jsonld-id: https://discovery.biothings.io/ns/nde/doi
  nde:journalName:
    type: string
    x-jsonld-id: https://discovery.biothings.io/ns/nde/journalName
  nde:journalNameAbbrev:
    type: string
    x-jsonld-id: https://discovery.biothings.io/ns/nde/journalNameAbbrev
required:
- '@type'
$defs:
  pmid:
    type: string
    pattern: ^\d+$
x-jsonld-prefixes:
  schema: http://schema.org/
  nde: https://discovery.biothings.io/ns/nde/
  bios: https://bioschemas.org/
  cdifniaid: https://w3id.org/cdif/niaid/terms/
x-bblocks-metadata:
  itemIdentifier: cdif.bbr.metadata.niaidProperties.niaidCreativeWork
  register: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/register.json
  version: '1.0'
  dateOfLastChange: '2026-11-14'

```

Links to the schema:

* YAML version: [schema.yaml](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/niaidProperties/niaidCreativeWork/schema.json)
* JSON version: [schema.json](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/niaidProperties/niaidCreativeWork/schema.yaml)


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
[context.jsonld](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/niaidProperties/niaidCreativeWork/context.jsonld)

## Sources

* [NIAID Data Ecosystem schemas](https://github.com/NIAID-Data-Ecosystem/nde-schemas)
* [NIAID Data Discovery Portal](https://data.niaid.nih.gov/)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/Cross-Domain-Interoperability-Framework/metadataBuildingBlocks](https://github.com/Cross-Domain-Interoperability-Framework/metadataBuildingBlocks)
* Path: `_sources/niaidProperties/niaidCreativeWork`

