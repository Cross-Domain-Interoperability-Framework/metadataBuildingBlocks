
# Labeled Link (Schema)

`cdif.bbr.metadata.schemaorgProperties.labeledLink` *v0.1*

Schema for a labeled link, implemented as a profile of schema.org/CreativeWork: a resolvable URL with an optional name and description. Optionally carries the DCAT relation surface for a link that expresses a typed relationship. Absorbed the cdifDataType/cdifReference block on 2026-09-23, which was this schema plus exactly these two optional properties. Defines properties: @type, schema:name, schema:description, schema:url, dcat:hadRole, dcterms:relation. Uses building blocks: cdifConceptOrTermOrString (cdifDataType).

[*Status*](http://www.opengis.net/def/status): Under development

## Description

## Labeled Link properties

Defines a set of properties for use describing a web link (url) with a label to indicate the target, like an html:anchor. For the schema.org implementation of the [Cross Domain Interoperability Framework](https://cross-domain-interoperability-framework.github.io/cdifbook/metadata/schemaorgimplementation.html#implementation-of-metadata-content-items) (CDIF) discovery profile.
## Examples

### Labeled Link building block.
Example labeled link instance.
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "ex": "https://example.org/",
    "xsd": "http://www.w3.org/2001/XMLSchema#"
  },
  "@id": "ex:LabeledLinkExample_zZc",
  "@type": [
    "schema:CreativeWork"
  ],
  "schema:name": "Some related resource",
  "schema:description": "URL to get the related resource",
  "schema:url": "https://example.org/relatedresource/2342747"
}

```

#### jsonld
```jsonld
{
  "@context": [
    {
      "schema": "http://schema.org/"
    },
    "https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/labeledLink/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ex": "https://example.org/",
      "xsd": "http://www.w3.org/2001/XMLSchema#"
    }
  ],
  "@id": "ex:LabeledLinkExample_zZc",
  "@type": [
    "schema:CreativeWork"
  ],
  "schema:name": "Some related resource",
  "schema:description": "URL to get the related resource",
  "schema:url": "https://example.org/relatedresource/2342747"
}
```

#### ttl
```ttl
@prefix ex: <https://example.org/> .
@prefix schema1: <http://schema.org/> .

ex:LabeledLinkExample_zZc a schema1:CreativeWork ;
    schema1:description "URL to get the related resource" ;
    schema1:name "Some related resource" ;
    schema1:url "https://example.org/relatedresource/2342747" .


```


### Complete labeled link example.
LabeledLink instance exercising all properties: name, description, and url.
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "ex": "https://example.org/"
  },
  "@id": "ex:LabeledLinkComplete_001",
  "@type": ["schema:CreativeWork"],
  "schema:name": "Data Quality Assessment Report",
  "schema:description": "Detailed report documenting the quality control procedures, flagging criteria, and validation results for this dataset",
  "schema:url": "https://example.org/reports/quality-assessment-2024.pdf"
}

```

#### jsonld
```jsonld
{
  "@context": [
    {
      "schema": "http://schema.org/"
    },
    "https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/labeledLink/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ex": "https://example.org/"
    }
  ],
  "@id": "ex:LabeledLinkComplete_001",
  "@type": [
    "schema:CreativeWork"
  ],
  "schema:name": "Data Quality Assessment Report",
  "schema:description": "Detailed report documenting the quality control procedures, flagging criteria, and validation results for this dataset",
  "schema:url": "https://example.org/reports/quality-assessment-2024.pdf"
}
```

#### ttl
```ttl
@prefix ex: <https://example.org/> .
@prefix schema1: <http://schema.org/> .

ex:LabeledLinkComplete_001 a schema1:CreativeWork ;
    schema1:description "Detailed report documenting the quality control procedures, flagging criteria, and validation results for this dataset" ;
    schema1:name "Data Quality Assessment Report" ;
    schema1:url "https://example.org/reports/quality-assessment-2024.pdf" .


```


### Labeled link expressing a relation.
A labeled link that also declares dcat:Relationship and carries
dcterms:relation -- the DCAT pointer to the related resource, distinct from
schema:url, which is the link's own presentation URL.
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "dcterms": "http://purl.org/dc/terms/",
    "dcat": "http://www.w3.org/ns/dcat#",
    "ex": "https://example.org/"
  },
  "@id": "ex:CdifRelationExample_001",
  "@type": ["schema:CreativeWork", "dcat:Relationship"],
  "schema:name": "Predecessor version of this dataset",
  "schema:url": "https://example.org/datasets/source-2023",
  "dcterms:relation": "https://example.org/datasets/source-2023"
}

```

#### jsonld
```jsonld
{
  "@context": [
    {
      "schema": "http://schema.org/",
      "dcterms": "http://purl.org/dc/terms/",
      "dcat": "http://www.w3.org/ns/dcat#"
    },
    "https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/labeledLink/context.jsonld",
    {
      "schema": "http://schema.org/",
      "dcterms": "http://purl.org/dc/terms/",
      "dcat": "http://www.w3.org/ns/dcat#",
      "ex": "https://example.org/"
    }
  ],
  "@id": "ex:CdifRelationExample_001",
  "@type": [
    "schema:CreativeWork",
    "dcat:Relationship"
  ],
  "schema:name": "Predecessor version of this dataset",
  "schema:url": "https://example.org/datasets/source-2023",
  "dcterms:relation": "https://example.org/datasets/source-2023"
}
```

#### ttl
```ttl
@prefix dcat: <http://www.w3.org/ns/dcat#> .
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix ex: <https://example.org/> .
@prefix schema1: <http://schema.org/> .

ex:CdifRelationExample_001 a schema1:CreativeWork,
        dcat:Relationship ;
    dcterms:relation "https://example.org/datasets/source-2023" ;
    schema1:name "Predecessor version of this dataset" ;
    schema1:url "https://example.org/datasets/source-2023" .


```


### Complete relation example, with a SKOS-typed role.
The full relation surface: dcat:hadRole classifying the relationship with a
skos:Concept, alongside dcterms:relation and the descriptive properties.
Moved here from cdifDataType/cdifReference when that block was folded into
this one.
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "skos": "http://www.w3.org/2004/02/skos/core#",
    "dcterms": "http://purl.org/dc/terms/",
    "dcat": "http://www.w3.org/ns/dcat#",
    "ex": "https://example.org/"
  },
  "@id": "ex:CdifRelationComplete_001",
  "@type": [
    "schema:CreativeWork",
    "dcat:Relationship"
  ],
  "schema:name": "Predecessor version of this dataset",
  "schema:description": "Relationship pointing at the previous published version, expressed in the DCAT qualifiedRelation pattern with a SKOS-typed role.",
  "schema:url": "https://example.org/datasets/source-2023",
  "dcterms:relation": "https://doi.org/10.5281/zenodo.7654320",
  "dcat:hadRole": {
    "@id": "ex:concepts/isVersionOf",
    "@type": [
      "skos:Concept"
    ],
    "skos:prefLabel": {
      "@value": "is version of",
      "@language": "en"
    },
    "skos:definition": {
      "@value": "The related resource is a version, edition, or adaptation of the described resource.",
      "@language": "en"
    },
    "skos:inScheme": {
      "@id": "ex:vocab/relationRoles"
    },
    "skos:notation": "isVersionOf"
  }
}

```

#### jsonld
```jsonld
{
  "@context": [
    {
      "schema": "http://schema.org/",
      "skos": "http://www.w3.org/2004/02/skos/core#",
      "dcterms": "http://purl.org/dc/terms/",
      "dcat": "http://www.w3.org/ns/dcat#"
    },
    "https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/labeledLink/context.jsonld",
    {
      "schema": "http://schema.org/",
      "skos": "http://www.w3.org/2004/02/skos/core#",
      "dcterms": "http://purl.org/dc/terms/",
      "dcat": "http://www.w3.org/ns/dcat#",
      "ex": "https://example.org/"
    }
  ],
  "@id": "ex:CdifRelationComplete_001",
  "@type": [
    "schema:CreativeWork",
    "dcat:Relationship"
  ],
  "schema:name": "Predecessor version of this dataset",
  "schema:description": "Relationship pointing at the previous published version, expressed in the DCAT qualifiedRelation pattern with a SKOS-typed role.",
  "schema:url": "https://example.org/datasets/source-2023",
  "dcterms:relation": "https://doi.org/10.5281/zenodo.7654320",
  "dcat:hadRole": {
    "@id": "ex:concepts/isVersionOf",
    "@type": [
      "skos:Concept"
    ],
    "skos:prefLabel": {
      "@value": "is version of",
      "@language": "en"
    },
    "skos:definition": {
      "@value": "The related resource is a version, edition, or adaptation of the described resource.",
      "@language": "en"
    },
    "skos:inScheme": {
      "@id": "ex:vocab/relationRoles"
    },
    "skos:notation": "isVersionOf"
  }
}
```

#### ttl
```ttl
@prefix dcat: <http://www.w3.org/ns/dcat#> .
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix ex: <https://example.org/> .
@prefix schema1: <http://schema.org/> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .

ex:CdifRelationComplete_001 a schema1:CreativeWork,
        dcat:Relationship ;
    dcterms:relation "https://doi.org/10.5281/zenodo.7654320" ;
    schema1:description "Relationship pointing at the previous published version, expressed in the DCAT qualifiedRelation pattern with a SKOS-typed role." ;
    schema1:name "Predecessor version of this dataset" ;
    schema1:url "https://example.org/datasets/source-2023" ;
    dcat:hadRole <https://example.org/concepts/isVersionOf> .

<https://example.org/concepts/isVersionOf> a skos:Concept ;
    skos:definition "The related resource is a version, edition, or adaptation of the described resource."@en ;
    skos:inScheme <https://example.org/vocab/relationRoles> ;
    skos:notation "isVersionOf" ;
    skos:prefLabel "is version of"@en .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
description: 'Schema for a labeled link, a profile of schema.org/CreativeWork: a resolvable
  URL with an optional name and description. Optionally carries the DCAT relation
  surface (dcat:hadRole, dcterms:relation) for a link that expresses a typed relationship
  rather than a plain reference.

  Those two properties were a separate block, cdifDataType/cdifReference, which was
  an allOf of this schema plus exactly those two optional properties and nothing else
  -- its dcat:Relationship co-type mandate had already been removed because it made
  every labeled link unsatisfiable and broke every schema:license example that followed
  schema.org''s own advice. Since both are optional, folding them in here changes
  no document''s validity while removing a block and five levels of $defs/Reference
  indirection. cdifReference was retired 2026-09-23.'
type: object
properties:
  '@type':
    default: schema:CreativeWork
    type: array
    items:
      type: string
    contains:
      const: schema:CreativeWork
    minItems: 1
  schema:name:
    type: string
    x-jsonld-id: http://schema.org/name
  schema:description:
    type: string
    x-jsonld-id: http://schema.org/description
  schema:url:
    type: string
    format: uri
    x-jsonld-id: http://schema.org/url
  dcat:hadRole:
    description: Role of the related resource as a SKOS Concept (DCAT canonical role
      slot). Present only on a link that expresses a relationship; a plain labeled
      link such as a license omits it.
    $ref: '#/$defs/cdifConceptOrTermOrString'
    x-jsonld-id: http://www.w3.org/ns/dcat#hadRole
  dcterms:relation:
    type: string
    format: uri
    description: URI of the related resource -- the DCAT canonical pointer to what
      is being related to, which is distinct from schema:url, the presentation URL
      of the link itself.
    x-jsonld-id: http://purl.org/dc/terms/relation
required:
- '@type'
- schema:url
$defs:
  cdifConceptOrTermOrString:
    $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifDataType/cdifConceptOrTermOrString/schema.yaml
x-jsonld-prefixes:
  schema: http://schema.org/
  skos: http://www.w3.org/2004/02/skos/core#
  dcterms: http://purl.org/dc/terms/
  dcat: http://www.w3.org/ns/dcat#

```

Links to the schema:

* YAML version: [schema.yaml](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/labeledLink/schema.json)
* JSON version: [schema.json](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/labeledLink/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "schema": "http://schema.org/",
    "skos": "http://www.w3.org/2004/02/skos/core#",
    "dcterms": "http://purl.org/dc/terms/",
    "dcat": "http://www.w3.org/ns/dcat#",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/labeledLink/context.jsonld)

## Sources

* [schema.org](https://schema.org/CreativeWork)
* [DCAT Relationship](https://www.w3.org/TR/vocab-dcat-3/#Class:Relationship)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/Cross-Domain-Interoperability-Framework/metadataBuildingBlocks](https://github.com/Cross-Domain-Interoperability-Framework/metadataBuildingBlocks)
* Path: `_sources/schemaorgProperties/labeledLink`

