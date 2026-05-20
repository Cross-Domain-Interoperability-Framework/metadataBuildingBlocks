
# CDIF Relation (Schema)

`cdif.bbr.metadata.cdifProperties.cdifReference` *v0.2*

A typed relation describing a link to another resource, combining the schema.org labeled-link surface (name, description, url) from labeledLink with the DCAT qualifiedRelation pattern. Carries a third @type (dcat:Relationship), a SKOS-typed role (dcat:hadRole), and the DCAT-canonical pointer to the related resource (dcterms:relation). Use as the target of a dcat:qualifiedRelation property, or wherever a typed link with an explicit role is needed. Defines properties: @type (must include 'schema:CreativeWork' and 'dcat:Relationship'), schema:name, schema:description, schema:url (required), dcat:hadRole (skos:Concept), dcterms:relation.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

## CDIF Relation

A typed relation describing a link to another resource. Combines the schema.org labeled-link surface inherited from `schemaorgProperties/labeledLink` (`schema:name`, `schema:description`, required `schema:url`) with the DCAT `dcat:qualifiedRelation` pattern by adding:

1. A second `@type` entry: `dcat:Relationship`, so the node satisfies DCAT-3 consumers expecting a typed Relationship resource.
2. `dcat:hadRole` — the role of the related resource as a `skos:Concept`.
3. `dcterms:relation` — the URI of the related resource (DCAT-canonical pointer to "what is being related to"). Distinct from `schema:url`, which is the presentation URL inherited from `labeledLink`.

### When to use

Use this building block wherever a metadata record needs a typed link to another resource with an explicit role — for example, to express that this dataset is a version of another dataset, derives from a source sample, or points at a sample-registration record (see [Discovery issue 13](https://github.com/Cross-Domain-Interoperability-Framework/Discovery/issues/13)). It is the target shape for `dcat:qualifiedRelation` on a `dcat:Resource`.

### Required properties

- `@type` must contain both `schema:CreativeWork` (inherited from `labeledLink`) and `dcat:Relationship` — typically `["schema:CreativeWork", "dcat:Relationship"]`.
- `schema:url` is required (inherited from `labeledLink`).

All other properties are optional.

### Relationship to upstream vocabularies

- `dcat:Relationship` (DCAT 3) is a class describing a qualified relationship between two resources. It is the target of `dcat:qualifiedRelation` on a `dcat:Resource`.
- `dcat:hadRole` carries a `dcat:Role` or `skos:Concept` describing the role the related resource plays.
- `dcterms:relation` is the dcterms (also written `dct:`) canonical pointer to the related resource.

### Note on the building-block name

The building-block directory is named `cdifReference` for historical reasons (it began life as a typed reference combining schema.org and DDI-CDI `dt-Reference` semantics). The DDI-CDI surface has been retired; the BB now models a DCAT-flavoured `cdif:Relation`. The folder name is retained so the 7 downstream BBs that `$ref` this schema continue to resolve.

## Examples

### CDIF Relation - minimal
Minimal cdif:Relation. Declares the @type with both required entries
(schema:CreativeWork inherited from labeledLink, dcat:Relationship from
the DCAT surface), carries the required schema:url, and uses
dcterms:relation to point at the related resource.
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
    "https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifProperties/cdifReference/context.jsonld",
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


### CDIF Relation - complete (with role)
Full cdif:Relation exercising dcat:hadRole as a SKOS Concept (here, the
role 'isVersionOf' from a relation-role vocabulary). Demonstrates the
DCAT qualifiedRelation pattern: this node is the target of an outer
dcat:qualifiedRelation property, with dcterms:relation pointing at the
related resource and dcat:hadRole classifying the role.
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
  "@type": ["schema:CreativeWork", "dcat:Relationship"],
  "schema:name": "Predecessor version of this dataset",
  "schema:description": "Relationship pointing at the previous published version, expressed in the DCAT qualifiedRelation pattern with a SKOS-typed role.",
  "schema:url": "https://example.org/datasets/source-2023",
  "dcterms:relation": "https://doi.org/10.5281/zenodo.7654320",
  "dcat:hadRole": {
    "@id": "ex:concepts/isVersionOf",
    "@type": ["skos:Concept"],
    "skos:prefLabel": {
      "@value": "is version of",
      "@language": "en"
    },
    "skos:inScheme": { "@id": "ex:vocab/relationRoles" },
    "skos:notation": ["isVersionOf"]
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
    "https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifProperties/cdifReference/context.jsonld",
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
    "skos:inScheme": {
      "@id": "ex:vocab/relationRoles"
    },
    "skos:notation": [
      "isVersionOf"
    ]
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
    skos:inScheme <https://example.org/vocab/relationRoles> ;
    skos:notation "isVersionOf" ;
    skos:prefLabel "is version of"@en .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
type: object
description: Building block to implement relations to other resources using a URL
  and some semantics.
allOf:
- $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/labeledLink/schema.yaml
- $ref: '#/$defs/Relation'
$defs:
  Relation:
    type: object
    description: DCAT Relationship surface added on top of the schema.org labeled
      link construct.
    properties:
      '@type':
        type: array
        items:
          type: string
        contains:
          const: dcat:Relationship
        minItems: 1
      dcat:hadRole:
        description: Role of the related resource as a SKOS Concept (DCAT canonical
          role slot).
        $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/skosProperties/skosConcept/schema.yaml
        x-jsonld-id: http://www.w3.org/ns/dcat#hadRole
      dcterms:relation:
        type: string
        format: uri
        description: URI of the related resource (DCAT canonical pointer to what is
          being related to; distinct from schema:url which is the presentation URL
          inherited from labeledLink).
        x-jsonld-id: http://purl.org/dc/terms/relation
x-jsonld-prefixes:
  schema: http://schema.org/
  skos: http://www.w3.org/2004/02/skos/core#
  cdi: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/
  cdif: https://cdif.org/0.1/
  ex: https://example.org/
  xsd: http://www.w3.org/2001/XMLSchema#
  dcterms: http://purl.org/dc/terms/
  dcat: http://www.w3.org/ns/dcat#

```

Links to the schema:

* YAML version: [schema.yaml](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifProperties/cdifReference/schema.json)
* JSON version: [schema.json](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifProperties/cdifReference/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "schema": "http://schema.org/",
    "skos": "http://www.w3.org/2004/02/skos/core#",
    "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
    "cdif": "https://cdif.org/0.1/",
    "ex": "https://example.org/",
    "xsd": "http://www.w3.org/2001/XMLSchema#",
    "dcterms": "http://purl.org/dc/terms/",
    "dcat": "http://www.w3.org/ns/dcat#",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifProperties/cdifReference/context.jsonld)

## Sources

* [schema.org/CreativeWork](https://schema.org/CreativeWork)
* [DCAT 3 qualifiedRelation](https://www.w3.org/TR/vocab-dcat-3/#Property:resource_qualified_relation)
* [DCAT 3 Relationship](https://www.w3.org/TR/vocab-dcat-3/#Class:Relationship)
* [SKOS Concept (role of related resource)](https://www.w3.org/TR/skos-reference/)
* [Discovery issue 13 - distinct assertions about sample registration vs physical object](https://github.com/Cross-Domain-Interoperability-Framework/Discovery/issues/13)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/Cross-Domain-Interoperability-Framework/metadataBuildingBlocks](https://github.com/Cross-Domain-Interoperability-Framework/metadataBuildingBlocks)
* Path: `_sources/cdifProperties/cdifReference`

