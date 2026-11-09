
# NIAID monetary grant (Schema)

`cdif.bbr.metadata.niaidProperties.niaidMonetaryGrant` *v1.0*

A schema:MonetaryGrant with the NIAID Data Discovery Portal's breakdown of an NIH project number into its parts. Extends the monetaryGrant block. Uses building blocks: monetaryGrant (schemaorgProperties).

[*Status*](http://www.opengis.net/def/status): Under development

## Description

## NIAID monetary grant

A schema:MonetaryGrant with the NIAID Data Discovery Portal's breakdown of an NIH project number into its parts. Extends the monetaryGrant block.

Used by [`niaidDataset`](../niaidDataset/) for `schema:funding` on a dataset. The
[`cdifNIAID`](../../profiles/cdifCompositeProfile/cdifNIAID/) profile composes
`niaidDataset` with `cdifCore`. `converters/NIAID/harvest_niaid_to_cdif.py` produces
these objects, and gives the type to one the portal left untyped.

| Property | Value | Meaning |
|---|---|---|
| `cdifniaid:projectNumSplit` | object | The parts of an NIH project number such as `5R01AI012345-03`: `cdifniaid:applTypeCode` (5), `activityCode` (R01), `icCode` (AI), `serialNum`, `supportYear`, `fullSupportYear`, `suffixCode` |

## Examples

### Minimal NIAID grant
The grant with the fewest properties among the converted NIAID examples: schema:funding of
converters/NIAID/niaidExamples/gse73472.json, converted by harvest_niaid_to_cdif.py.
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
    "schema:MonetaryGrant"
  ],
  "schema:endDate": "2003-06-30",
  "schema:funder": {
    "@type": [
      "schema:Organization"
    ],
    "schema:name": "National Heart Lung and Blood Institute"
  },
  "schema:identifier": {
    "@type": [
      "schema:PropertyValue"
    ],
    "schema:value": "1T32HL007893-01"
  },
  "schema:name": "TRAINING PROGRAM IN ANGIOGENESIS AND INFLAMMATION",
  "cdifniaid:projectNumSplit": {
    "cdifniaid:activityCode": "T32",
    "cdifniaid:applTypeCode": "1",
    "cdifniaid:fullSupportYear": "01",
    "cdifniaid:icCode": "HL",
    "cdifniaid:serialNum": "007893",
    "cdifniaid:supportYear": "01"
  },
  "schema:startDate": "1998-07-01",
  "schema:url": "https://reporter.nih.gov/project-details/2433284"
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
    "https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/niaidProperties/niaidMonetaryGrant/context.jsonld",
    {
      "schema": "http://schema.org/",
      "nde": "https://discovery.biothings.io/ns/nde/",
      "bios": "https://bioschemas.org/",
      "cdifniaid": "https://w3id.org/cdif/niaid/terms/"
    }
  ],
  "@type": [
    "schema:MonetaryGrant"
  ],
  "schema:endDate": "2003-06-30",
  "schema:funder": {
    "@type": [
      "schema:Organization"
    ],
    "schema:name": "National Heart Lung and Blood Institute"
  },
  "schema:identifier": {
    "@type": [
      "schema:PropertyValue"
    ],
    "schema:value": "1T32HL007893-01"
  },
  "schema:name": "TRAINING PROGRAM IN ANGIOGENESIS AND INFLAMMATION",
  "cdifniaid:projectNumSplit": {
    "cdifniaid:activityCode": "T32",
    "cdifniaid:applTypeCode": "1",
    "cdifniaid:fullSupportYear": "01",
    "cdifniaid:icCode": "HL",
    "cdifniaid:serialNum": "007893",
    "cdifniaid:supportYear": "01"
  },
  "schema:startDate": "1998-07-01",
  "schema:url": "https://reporter.nih.gov/project-details/2433284"
}
```

#### ttl
```ttl
@prefix cdifniaid: <https://w3id.org/cdif/niaid/terms/> .
@prefix schema1: <http://schema.org/> .

[] a schema1:MonetaryGrant ;
    schema1:endDate "2003-06-30" ;
    schema1:funder [ a schema1:Organization ;
            schema1:name "National Heart Lung and Blood Institute" ] ;
    schema1:identifier [ a schema1:PropertyValue ;
            schema1:value "1T32HL007893-01" ] ;
    schema1:name "TRAINING PROGRAM IN ANGIOGENESIS AND INFLAMMATION" ;
    schema1:startDate "1998-07-01" ;
    schema1:url "https://reporter.nih.gov/project-details/2433284" ;
    cdifniaid:projectNumSplit [ cdifniaid:activityCode "T32" ;
            cdifniaid:applTypeCode "1" ;
            cdifniaid:fullSupportYear "01" ;
            cdifniaid:icCode "HL" ;
            cdifniaid:serialNum "007893" ;
            cdifniaid:supportYear "01" ] .


```


### Complete NIAID grant
The grant with the most NIAID properties, then the most properties among the converted NIAID examples: schema:funding of
converters/NIAID/niaidExamples/phs000239.json, converted by harvest_niaid_to_cdif.py.
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
    "schema:MonetaryGrant"
  ],
  "schema:endDate": "2018-08-31",
  "schema:funder": {
    "@type": [
      "schema:Organization"
    ],
    "schema:alternateName": [
      "NIH Eunice Kennedy Shriver National Institute of Child Health and Human Development",
      "NIH Eunice Kennedy Shriver National Institute of Child Health & Human Development",
      "Eunice Kennedy Shriver National Institute of Child Health and Human Development at the National Institutes of Health",
      "National Institutes of Health/Eunice Kennedy Shriver National Institute of Child Health & Human Development",
      "Eunice Kennedy Shriver National Institute of Child Health & Human Development",
      "National Institute of Child Health and Human Development",
      "Instituto Nacional de Salud Infantil y Desarrollo Humano Eunice Kennedy Shriver",
      "NIH/NICHD",
      "Eunice Kennedy Shriver National Institute of Child Health and Human Development of the National Institutes of Health",
      "NICHD",
      "NIH/Eunice Kennedy Shriver National Institute of Child Health and Human Development"
    ],
    "schema:identifier": "https://ror.org/04byxyr05",
    "schema:name": "Eunice Kennedy Shriver National Institute of Child Health and Human Development",
    "schema:parentOrganization": "National Institutes of Health"
  },
  "schema:identifier": {
    "@type": [
      "schema:PropertyValue"
    ],
    "schema:value": "1U19HD077693-01"
  },
  "schema:name": "Clinical and Social Implications of 2-day Genome Results in Acutely III Newborns",
  "cdifniaid:projectNumSplit": {
    "cdifniaid:activityCode": "U19",
    "cdifniaid:applTypeCode": "1",
    "cdifniaid:fullSupportYear": "01",
    "cdifniaid:icCode": "HD",
    "cdifniaid:serialNum": "077693",
    "cdifniaid:supportYear": "01"
  },
  "schema:startDate": "2013-09-05",
  "schema:url": "https://reporter.nih.gov/project-details/8585138"
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
    "https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/niaidProperties/niaidMonetaryGrant/context.jsonld",
    {
      "schema": "http://schema.org/",
      "nde": "https://discovery.biothings.io/ns/nde/",
      "bios": "https://bioschemas.org/",
      "cdifniaid": "https://w3id.org/cdif/niaid/terms/"
    }
  ],
  "@type": [
    "schema:MonetaryGrant"
  ],
  "schema:endDate": "2018-08-31",
  "schema:funder": {
    "@type": [
      "schema:Organization"
    ],
    "schema:alternateName": [
      "NIH Eunice Kennedy Shriver National Institute of Child Health and Human Development",
      "NIH Eunice Kennedy Shriver National Institute of Child Health & Human Development",
      "Eunice Kennedy Shriver National Institute of Child Health and Human Development at the National Institutes of Health",
      "National Institutes of Health/Eunice Kennedy Shriver National Institute of Child Health & Human Development",
      "Eunice Kennedy Shriver National Institute of Child Health & Human Development",
      "National Institute of Child Health and Human Development",
      "Instituto Nacional de Salud Infantil y Desarrollo Humano Eunice Kennedy Shriver",
      "NIH/NICHD",
      "Eunice Kennedy Shriver National Institute of Child Health and Human Development of the National Institutes of Health",
      "NICHD",
      "NIH/Eunice Kennedy Shriver National Institute of Child Health and Human Development"
    ],
    "schema:identifier": "https://ror.org/04byxyr05",
    "schema:name": "Eunice Kennedy Shriver National Institute of Child Health and Human Development",
    "schema:parentOrganization": "National Institutes of Health"
  },
  "schema:identifier": {
    "@type": [
      "schema:PropertyValue"
    ],
    "schema:value": "1U19HD077693-01"
  },
  "schema:name": "Clinical and Social Implications of 2-day Genome Results in Acutely III Newborns",
  "cdifniaid:projectNumSplit": {
    "cdifniaid:activityCode": "U19",
    "cdifniaid:applTypeCode": "1",
    "cdifniaid:fullSupportYear": "01",
    "cdifniaid:icCode": "HD",
    "cdifniaid:serialNum": "077693",
    "cdifniaid:supportYear": "01"
  },
  "schema:startDate": "2013-09-05",
  "schema:url": "https://reporter.nih.gov/project-details/8585138"
}
```

#### ttl
```ttl
@prefix cdifniaid: <https://w3id.org/cdif/niaid/terms/> .
@prefix schema1: <http://schema.org/> .

[] a schema1:MonetaryGrant ;
    schema1:endDate "2018-08-31" ;
    schema1:funder [ a schema1:Organization ;
            schema1:alternateName "Eunice Kennedy Shriver National Institute of Child Health & Human Development",
                "Eunice Kennedy Shriver National Institute of Child Health and Human Development at the National Institutes of Health",
                "Eunice Kennedy Shriver National Institute of Child Health and Human Development of the National Institutes of Health",
                "Instituto Nacional de Salud Infantil y Desarrollo Humano Eunice Kennedy Shriver",
                "NICHD",
                "NIH Eunice Kennedy Shriver National Institute of Child Health & Human Development",
                "NIH Eunice Kennedy Shriver National Institute of Child Health and Human Development",
                "NIH/Eunice Kennedy Shriver National Institute of Child Health and Human Development",
                "NIH/NICHD",
                "National Institute of Child Health and Human Development",
                "National Institutes of Health/Eunice Kennedy Shriver National Institute of Child Health & Human Development" ;
            schema1:identifier "https://ror.org/04byxyr05" ;
            schema1:name "Eunice Kennedy Shriver National Institute of Child Health and Human Development" ;
            schema1:parentOrganization "National Institutes of Health" ] ;
    schema1:identifier [ a schema1:PropertyValue ;
            schema1:value "1U19HD077693-01" ] ;
    schema1:name "Clinical and Social Implications of 2-day Genome Results in Acutely III Newborns" ;
    schema1:startDate "2013-09-05" ;
    schema1:url "https://reporter.nih.gov/project-details/8585138" ;
    cdifniaid:projectNumSplit [ cdifniaid:activityCode "U19" ;
            cdifniaid:applTypeCode "1" ;
            cdifniaid:fullSupportYear "01" ;
            cdifniaid:icCode "HD" ;
            cdifniaid:serialNum "077693" ;
            cdifniaid:supportYear "01" ] .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: NIAID monetary grant
description: A schema:MonetaryGrant, as CDIF's monetaryGrant block defines it, with
  the NIAID Data Discovery Portal's parts of an NIH project number.
type: object
allOf:
- $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/monetaryGrant/schema.yaml
properties:
  '@type':
    type: array
    items:
      type: string
    contains:
      const: schema:MonetaryGrant
    minItems: 1
  cdifniaid:projectNumSplit:
    $ref: '#/$defs/projectNumber'
    x-jsonld-id: https://w3id.org/cdif/niaid/terms/projectNumSplit
required:
- '@type'
$defs:
  projectNumber:
    description: The parts of an NIH project number such as 5R01AI012345-03, which
      NIH grant identifiers follow.
    type: object
    properties:
      cdifniaid:applTypeCode:
        description: Application type, e.g. 5 for a non-competing continuation.
        type: string
        x-jsonld-id: https://w3id.org/cdif/niaid/terms/applTypeCode
      cdifniaid:activityCode:
        description: Activity code, e.g. R01.
        type: string
        x-jsonld-id: https://w3id.org/cdif/niaid/terms/activityCode
      cdifniaid:icCode:
        description: The NIH institute or center, e.g. AI for NIAID.
        type: string
        x-jsonld-id: https://w3id.org/cdif/niaid/terms/icCode
      cdifniaid:serialNum:
        description: Serial number of the grant.
        type: string
        x-jsonld-id: https://w3id.org/cdif/niaid/terms/serialNum
      cdifniaid:supportYear:
        description: Year of support.
        type: string
        x-jsonld-id: https://w3id.org/cdif/niaid/terms/supportYear
      cdifniaid:fullSupportYear:
        description: Year of support with any suffix.
        type: string
        x-jsonld-id: https://w3id.org/cdif/niaid/terms/fullSupportYear
      cdifniaid:suffixCode:
        description: Suffix, e.g. S1 for a supplement.
        type: string
        x-jsonld-id: https://w3id.org/cdif/niaid/terms/suffixCode
x-jsonld-prefixes:
  schema: http://schema.org/
  nde: https://discovery.biothings.io/ns/nde/
  bios: https://bioschemas.org/
  cdifniaid: https://w3id.org/cdif/niaid/terms/
x-bblocks-metadata:
  itemIdentifier: cdif.bbr.metadata.niaidProperties.niaidMonetaryGrant
  register: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/register.json
  version: '1.0'
  dateOfLastChange: '2026-11-09'

```

Links to the schema:

* YAML version: [schema.yaml](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/niaidProperties/niaidMonetaryGrant/schema.json)
* JSON version: [schema.json](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/niaidProperties/niaidMonetaryGrant/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "schema": "http://schema.org/",
    "skos": "http://www.w3.org/2004/02/skos/core#",
    "nde": "https://discovery.biothings.io/ns/nde/",
    "bios": "https://bioschemas.org/",
    "cdifniaid": "https://w3id.org/cdif/niaid/terms/",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/niaidProperties/niaidMonetaryGrant/context.jsonld)

## Sources

* [NIAID Data Ecosystem schemas](https://github.com/NIAID-Data-Ecosystem/nde-schemas)
* [NIAID Data Discovery Portal](https://data.niaid.nih.gov/)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/Cross-Domain-Interoperability-Framework/metadataBuildingBlocks](https://github.com/Cross-Domain-Interoperability-Framework/metadataBuildingBlocks)
* Path: `_sources/niaidProperties/niaidMonetaryGrant`

