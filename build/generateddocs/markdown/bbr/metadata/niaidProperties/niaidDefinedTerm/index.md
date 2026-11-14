
# NIAID defined term (Schema)

`cdif.bbr.metadata.niaidProperties.niaidDefinedTerm` *v1.0*

A schema:DefinedTerm with the annotations the NIAID Data Discovery Portal adds to the terms it attaches to a dataset: whether a curator checked the term, the text it was matched from, who curated it, and a taxon's common name. The annotations occur only on DefinedTerms, so the block requires that type. Uses building blocks: bioschemasSample (bioschemasProperties).

[*Status*](http://www.opengis.net/def/status): Under development

## Description

## NIAID defined term

A schema:DefinedTerm with the annotations the NIAID Data Discovery Portal adds to the terms it attaches to a dataset: whether a curator checked the term, the text it was matched from, who curated it, and a taxon's common name. The annotations occur only on DefinedTerms, so the block requires that type.

Used by [`niaidDataset`](../niaidDataset/) for `nde:species`, `schema:infectiousAgent` and `schema:healthCondition` on a dataset, the `schema:keywords`, `schema:measurementTechnique` and `schema:variableMeasured` items that carry an annotation, and `nde:species` on a sample. The
[`cdifNIAID`](../../profiles/cdifCompositeProfile/cdifNIAID/) profile composes
`niaidDataset` with `cdifCore`. `converters/NIAID/harvest_niaid_to_cdif.py` produces
these objects, and gives the type to one the portal left untyped.

| Property | Value | Meaning |
|---|---|---|
| `nde:isCurated` | boolean | Whether a curator checked the term against its source text |
| `nde:originalName` | text | The text in the source record the term was matched from |
| `nde:curatedBy` | agent | Who or what produced or checked the annotation, often software (PubTator, GPT-4o-mini, the Biothings API) |
| `cdifniaid:commonName` | text | A taxon's common name, e.g. Human |

The portal also puts `fromGPT`, `fromPMID`, `fromEXTRACT` and `fromNCT` flags, `classification` and `displayName` on terms. The converter turns the flags into one sentence on the catalog record's description, `classification` into a keyword and `displayName` into `schema:alternateName`, so none of them appear here.

## Examples

### Minimal NIAID defined term
The defined term with the fewest properties among the converted NIAID examples: schema:healthCondition of
converters/NIAID/niaidExamples/sdy1256.json, converted by harvest_niaid_to_cdif.py.
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
    "schema:DefinedTerm"
  ],
  "schema:name": "healthy appearing infants",
  "nde:originalName": "healthy appearing infants"
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
    "https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/niaidProperties/niaidDefinedTerm/context.jsonld",
    {
      "schema": "http://schema.org/",
      "nde": "https://discovery.biothings.io/ns/nde/",
      "bios": "https://bioschemas.org/",
      "cdifniaid": "https://w3id.org/cdif/niaid/terms/"
    }
  ],
  "@type": [
    "schema:DefinedTerm"
  ],
  "schema:name": "healthy appearing infants",
  "nde:originalName": "healthy appearing infants"
}
```

#### ttl
```ttl
@prefix nde: <https://discovery.biothings.io/ns/nde/> .
@prefix schema1: <http://schema.org/> .

[] a schema1:DefinedTerm ;
    schema1:name "healthy appearing infants" ;
    nde:originalName "healthy appearing infants" .


```


### Complete NIAID defined term
The defined term with the most NIAID properties, then the most properties among the converted NIAID examples: schema:infectiousAgent of
converters/NIAID/niaidExamples/gse61521.json, converted by harvest_niaid_to_cdif.py.
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
    "schema:DefinedTerm"
  ],
  "schema:alternateName": [
    "NBRC 14782",
    "Rhizobium meliloti (plasmid pRmeGR4b)",
    "Sinorhizobium meliloti (Dangeard 1926) De Lajudie et al. 1994",
    "ICMP 12623",
    "Rhizobium sp. AC50e",
    "Ensifer meliloti (Dangeard 1926) Young 2003",
    "Ensifer meliloti",
    "Rhizobium meliloti plasmid pRmeGR4b",
    "CFBP 5561",
    "CCUG 27879",
    "NRRL L-45",
    "Ensifer sp. AC50e",
    "NZP 4027",
    "ATCC 9930",
    "LMG 6133",
    "Rhizobium meliloti Dangeard 1926 (Approved Lists 1980)",
    "USDA 1002",
    "IAM 12611",
    "DSM 30135",
    "LMG:6133",
    "NCAIM B.01520",
    "NRRL:L:45",
    "Rhizobium meliloti (megaplasmid pRME41B SYM)",
    "HAMBI 2148",
    "JCM 20682",
    "IFO 14782",
    "Ensifer sp. AC50a"
  ],
  "cdifniaid:commonName": "Ensifer meliloti",
  "nde:curatedBy": {
    "@type": [
      "schema:SoftwareApplication"
    ],
    "schema:dateModified": "2024-01-26",
    "schema:name": "PubTator",
    "schema:url": "https://www.ncbi.nlm.nih.gov/research/pubtator/api.html"
  },
  "schema:identifier": "382",
  "schema:inDefinedTermSet": "UniProt",
  "nde:isCurated": true,
  "schema:name": "Rhizobium meliloti",
  "nde:originalName": "Sinorhizobium meliloti",
  "schema:url": "https://www.uniprot.org/taxonomy/382"
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
    "https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/niaidProperties/niaidDefinedTerm/context.jsonld",
    {
      "schema": "http://schema.org/",
      "nde": "https://discovery.biothings.io/ns/nde/",
      "bios": "https://bioschemas.org/",
      "cdifniaid": "https://w3id.org/cdif/niaid/terms/"
    }
  ],
  "@type": [
    "schema:DefinedTerm"
  ],
  "schema:alternateName": [
    "NBRC 14782",
    "Rhizobium meliloti (plasmid pRmeGR4b)",
    "Sinorhizobium meliloti (Dangeard 1926) De Lajudie et al. 1994",
    "ICMP 12623",
    "Rhizobium sp. AC50e",
    "Ensifer meliloti (Dangeard 1926) Young 2003",
    "Ensifer meliloti",
    "Rhizobium meliloti plasmid pRmeGR4b",
    "CFBP 5561",
    "CCUG 27879",
    "NRRL L-45",
    "Ensifer sp. AC50e",
    "NZP 4027",
    "ATCC 9930",
    "LMG 6133",
    "Rhizobium meliloti Dangeard 1926 (Approved Lists 1980)",
    "USDA 1002",
    "IAM 12611",
    "DSM 30135",
    "LMG:6133",
    "NCAIM B.01520",
    "NRRL:L:45",
    "Rhizobium meliloti (megaplasmid pRME41B SYM)",
    "HAMBI 2148",
    "JCM 20682",
    "IFO 14782",
    "Ensifer sp. AC50a"
  ],
  "cdifniaid:commonName": "Ensifer meliloti",
  "nde:curatedBy": {
    "@type": [
      "schema:SoftwareApplication"
    ],
    "schema:dateModified": "2024-01-26",
    "schema:name": "PubTator",
    "schema:url": "https://www.ncbi.nlm.nih.gov/research/pubtator/api.html"
  },
  "schema:identifier": "382",
  "schema:inDefinedTermSet": "UniProt",
  "nde:isCurated": true,
  "schema:name": "Rhizobium meliloti",
  "nde:originalName": "Sinorhizobium meliloti",
  "schema:url": "https://www.uniprot.org/taxonomy/382"
}
```

#### ttl
```ttl
@prefix cdifniaid: <https://w3id.org/cdif/niaid/terms/> .
@prefix nde: <https://discovery.biothings.io/ns/nde/> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

[] a schema1:DefinedTerm ;
    schema1:alternateName "ATCC 9930",
        "CCUG 27879",
        "CFBP 5561",
        "DSM 30135",
        "Ensifer meliloti",
        "Ensifer meliloti (Dangeard 1926) Young 2003",
        "Ensifer sp. AC50a",
        "Ensifer sp. AC50e",
        "HAMBI 2148",
        "IAM 12611",
        "ICMP 12623",
        "IFO 14782",
        "JCM 20682",
        "LMG 6133",
        "LMG:6133",
        "NBRC 14782",
        "NCAIM B.01520",
        "NRRL L-45",
        "NRRL:L:45",
        "NZP 4027",
        "Rhizobium meliloti (megaplasmid pRME41B SYM)",
        "Rhizobium meliloti (plasmid pRmeGR4b)",
        "Rhizobium meliloti Dangeard 1926 (Approved Lists 1980)",
        "Rhizobium meliloti plasmid pRmeGR4b",
        "Rhizobium sp. AC50e",
        "Sinorhizobium meliloti (Dangeard 1926) De Lajudie et al. 1994",
        "USDA 1002" ;
    schema1:identifier "382" ;
    schema1:inDefinedTermSet "UniProt" ;
    schema1:name "Rhizobium meliloti" ;
    schema1:url "https://www.uniprot.org/taxonomy/382" ;
    nde:curatedBy [ a schema1:SoftwareApplication ;
            schema1:dateModified "2024-01-26" ;
            schema1:name "PubTator" ;
            schema1:url "https://www.ncbi.nlm.nih.gov/research/pubtator/api.html" ] ;
    nde:isCurated true ;
    nde:originalName "Sinorhizobium meliloti" ;
    cdifniaid:commonName "Ensifer meliloti" .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: NIAID defined term
description: 'A schema:DefinedTerm with NIAID''s annotations. The NIAID Data Discovery
  Portal annotates every term it attaches to a dataset (species, infectious agents,
  health conditions, measurement techniques, variables): whether a curator checked
  it, the text it was matched from, who or what curated it, and for a taxon its common
  name. Across the portal''s records these properties appear on DefinedTerms and nowhere
  else, so this block is an extension of that type and requires it.'
type: object
allOf:
- $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/bioschemasProperties/bioschemasSample/schema.yaml#/$defs/term
properties:
  '@type':
    type: array
    items:
      type: string
    contains:
      const: schema:DefinedTerm
    minItems: 1
  nde:isCurated:
    description: Whether a curator checked the term against its source text.
    type: boolean
    x-jsonld-id: https://discovery.biothings.io/ns/nde/isCurated
  nde:originalName:
    description: The text in the source record the term was matched from.
    type: string
    x-jsonld-id: https://discovery.biothings.io/ns/nde/originalName
  nde:curatedBy:
    description: Who or what produced or checked the annotation, often software (PubTator,
      GPT-4o-mini, the Biothings API).
    $ref: '#/$defs/curator'
    x-jsonld-id: https://discovery.biothings.io/ns/nde/curatedBy
  cdifniaid:commonName:
    description: The common name of a taxon, e.g. Human for Homo sapiens.
    type: string
    x-jsonld-id: https://w3id.org/cdif/niaid/terms/commonName
required:
- '@type'
$defs:
  curator:
    description: An agent, software application or catalog that curated something,
      and when. The portal types it as SoftwareApplication, Organization or DataCatalog,
      so the type is not constrained.
    type: object
    properties:
      schema:name:
        type: string
        x-jsonld-id: http://schema.org/name
      schema:url:
        type: string
        x-jsonld-id: http://schema.org/url
      schema:dateModified:
        type: string
        x-jsonld-id: http://schema.org/dateModified
      schema:archivedAt:
        type: string
        x-jsonld-id: http://schema.org/archivedAt
      nde:versionDate:
        type: string
        x-jsonld-id: https://discovery.biothings.io/ns/nde/versionDate
x-jsonld-prefixes:
  schema: http://schema.org/
  nde: https://discovery.biothings.io/ns/nde/
  bios: https://bioschemas.org/
  cdifniaid: https://w3id.org/cdif/niaid/terms/
x-bblocks-metadata:
  itemIdentifier: cdif.bbr.metadata.niaidProperties.niaidDefinedTerm
  register: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/register.json
  version: '1.0'
  dateOfLastChange: '2026-11-14'

```

Links to the schema:

* YAML version: [schema.yaml](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/niaidProperties/niaidDefinedTerm/schema.json)
* JSON version: [schema.json](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/niaidProperties/niaidDefinedTerm/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "schema": "http://schema.org/",
    "bios": "https://bioschemas.org/",
    "nde": "https://discovery.biothings.io/ns/nde/",
    "cdifniaid": "https://w3id.org/cdif/niaid/terms/",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/niaidProperties/niaidDefinedTerm/context.jsonld)

## Sources

* [NIAID Data Ecosystem schemas](https://github.com/NIAID-Data-Ecosystem/nde-schemas)
* [NIAID Data Discovery Portal](https://data.niaid.nih.gov/)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/Cross-Domain-Interoperability-Framework/metadataBuildingBlocks](https://github.com/Cross-Domain-Interoperability-Framework/metadataBuildingBlocks)
* Path: `_sources/niaidProperties/niaidDefinedTerm`

