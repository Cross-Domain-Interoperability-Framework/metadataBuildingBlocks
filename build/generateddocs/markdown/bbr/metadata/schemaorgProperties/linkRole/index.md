
# Link Role (Schema)

`cdif.bbr.metadata.schemaorgProperties.linkRole` *v0.1*

Schema for a typed link, implemented as a schema.org LinkRole: schema:linkRelationship names how the target relates to the subject, and schema:target carries the schema:EntryPoint being linked to. Use for a link whose relationship is the point; use labeledLink where the value is simply a work at a URL, such as a license. Defines properties: @type, schema:linkRelationship, schema:target. Uses building blocks: cdifConceptOrTermOrString (cdifDataType).

[*Status*](http://www.opengis.net/def/status): Under development

## Description

# Link Role

A typed link. `schema:linkRelationship` names how the target relates to the
subject; `schema:target` carries the `schema:EntryPoint` being linked to.

## When to use this, and when not to

Use `linkRole` where the **relationship is the point** -- "the canonical version
of this", "the download endpoint for this". Use
[`labeledLink`](../labeledLink/) where the value is simply **a work at a URL**:
a license, a terms-of-service document, a manual. A license is a work, not a
role, and wrapping one in a Role forces every consumer through an indirection to
reach the document itself.

That division is why this block does not replace `labeledLink`. In the corpus,
`schema:license` and `schema:conditionsOfAccess` appear 36 times as plain strings
or `CreativeWork`s and never as a `LinkRole`.

## History

Until 2026-09-23 this shape was defined inline inside the `cdifCore` profile, so
nothing else could reuse it. `schemaorgProperties/instrument` consequently
defined `schema:relatedLink` as a labeled link instead -- the same property
carrying two different shapes depending on which node held it. Both now
reference this block.

## Examples

### Link role building block.
A typed link whose relationship is given as a plain string label.
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "ex": "https://example.org/"
  },
  "@type": [
    "schema:LinkRole"
  ],
  "schema:linkRelationship": "canonical version",
  "schema:target": {
    "@type": [
      "schema:EntryPoint"
    ],
    "schema:name": "Landing page for the published version of record",
    "schema:url": "https://example.org/datasets/soil-moisture-2026",
    "schema:encodingFormat": "text/html"
  }
}

```

#### jsonld
```jsonld
{
  "@context": [
    {
      "schema": "http://schema.org/"
    },
    "https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/linkRole/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ex": "https://example.org/"
    }
  ],
  "@type": [
    "schema:LinkRole"
  ],
  "schema:linkRelationship": "canonical version",
  "schema:target": {
    "@type": [
      "schema:EntryPoint"
    ],
    "schema:name": "Landing page for the published version of record",
    "schema:url": "https://example.org/datasets/soil-moisture-2026",
    "schema:encodingFormat": "text/html"
  }
}
```

#### ttl
```ttl
@prefix schema1: <http://schema.org/> .

[] a schema1:LinkRole ;
    schema1:linkRelationship "canonical version" ;
    schema1:target [ a schema1:EntryPoint ;
            schema1:encodingFormat "text/html" ;
            schema1:name "Landing page for the published version of record" ;
            schema1:url "https://example.org/datasets/soil-moisture-2026" ] .


```


### Complete link role example.
The relationship given as a SKOS concept rather than a string, with a fully
described EntryPoint target.
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "skos": "http://www.w3.org/2004/02/skos/core#",
    "ex": "https://example.org/"
  },
  "@type": [
    "schema:LinkRole"
  ],
  "schema:linkRelationship": {
    "@id": "ex:concepts/isDocumentedBy",
    "@type": [
      "skos:Concept"
    ],
    "skos:prefLabel": {
      "@value": "is documented by",
      "@language": "en"
    },
    "skos:definition": {
      "@value": "The target documents the described resource.",
      "@language": "en"
    },
    "skos:inScheme": {
      "@id": "ex:vocab/linkRelationships"
    },
    "skos:notation": "isDocumentedBy"
  },
  "schema:target": {
    "@type": [
      "schema:EntryPoint"
    ],
    "schema:name": "Instrument handbook, revision 4",
    "schema:url": "https://example.org/docs/handbook-r4.pdf",
    "schema:encodingFormat": "application/pdf"
  }
}

```

#### jsonld
```jsonld
{
  "@context": [
    {
      "schema": "http://schema.org/",
      "skos": "http://www.w3.org/2004/02/skos/core#"
    },
    "https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/linkRole/context.jsonld",
    {
      "schema": "http://schema.org/",
      "skos": "http://www.w3.org/2004/02/skos/core#",
      "ex": "https://example.org/"
    }
  ],
  "@type": [
    "schema:LinkRole"
  ],
  "schema:linkRelationship": {
    "@id": "ex:concepts/isDocumentedBy",
    "@type": [
      "skos:Concept"
    ],
    "skos:prefLabel": {
      "@value": "is documented by",
      "@language": "en"
    },
    "skos:definition": {
      "@value": "The target documents the described resource.",
      "@language": "en"
    },
    "skos:inScheme": {
      "@id": "ex:vocab/linkRelationships"
    },
    "skos:notation": "isDocumentedBy"
  },
  "schema:target": {
    "@type": [
      "schema:EntryPoint"
    ],
    "schema:name": "Instrument handbook, revision 4",
    "schema:url": "https://example.org/docs/handbook-r4.pdf",
    "schema:encodingFormat": "application/pdf"
  }
}
```

#### ttl
```ttl
@prefix schema1: <http://schema.org/> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .

<https://example.org/concepts/isDocumentedBy> a skos:Concept ;
    skos:definition "The target documents the described resource."@en ;
    skos:inScheme <https://example.org/vocab/linkRelationships> ;
    skos:notation "isDocumentedBy" ;
    skos:prefLabel "is documented by"@en .

[] a schema1:LinkRole ;
    schema1:linkRelationship <https://example.org/concepts/isDocumentedBy> ;
    schema1:target [ a schema1:EntryPoint ;
            schema1:encodingFormat "application/pdf" ;
            schema1:name "Instrument handbook, revision 4" ;
            schema1:url "https://example.org/docs/handbook-r4.pdf" ] .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
description: 'A typed link, implemented as a schema.org LinkRole: schema:linkRelationship
  names how the target relates to the subject, and schema:target carries the EntryPoint
  actually being linked to.

  This is the right shape when the relationship itself is the point -- "this is the
  canonical version of", "this is the download endpoint for". Where the value is simply
  a work at a URL, such as a license or a terms-of-service document, use schemaorgProperties/labeledLink
  instead: a licence is a work, not a role, and wrapping it in a Role forces every
  consumer through an indirection to reach the thing itself.

  Defined here as a block rather than inline in a profile (where it lived until 2026-09-23)
  so that more than one consumer can reuse it. While it was inline in cdifCore, schemaorgProperties/instrument
  could not reach it and defined schema:relatedLink as a labeled link instead -- the
  same property carrying two different shapes depending on which node held it.'
type: object
properties:
  '@type':
    default: schema:LinkRole
    type: array
    items:
      type: string
    contains:
      const: schema:LinkRole
    minItems: 1
  schema:linkRelationship:
    description: How the target relates to the subject, as a controlled-vocabulary
      value or a plain string label.
    $ref: '#/$defs/cdifConceptOrTermOrString'
    x-jsonld-id: http://schema.org/linkRelationship
  schema:target:
    type: object
    description: 'The entry point being linked to. Deliberately not sealed: real targets
      also carry schema:httpMethod, schema:urlTemplate, schema:contentType and domain-specific
      properties, and JSON-LD is open-world.'
    properties:
      '@type':
        default: schema:EntryPoint
        type: array
        items:
          type: string
        contains:
          const: schema:EntryPoint
        minItems: 1
      schema:name:
        type: string
        x-jsonld-id: http://schema.org/name
      schema:url:
        type: string
        format: uri
        x-jsonld-id: http://schema.org/url
      schema:encodingFormat:
        type: string
        description: registered MIME types are expected
        x-jsonld-id: http://schema.org/encodingFormat
    x-jsonld-id: http://schema.org/target
required:
- '@type'
$defs:
  cdifConceptOrTermOrString:
    $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifDataType/cdifConceptOrTermOrString/schema.yaml
x-jsonld-prefixes:
  schema: http://schema.org/
  skos: http://www.w3.org/2004/02/skos/core#

```

Links to the schema:

* YAML version: [schema.yaml](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/linkRole/schema.json)
* JSON version: [schema.json](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/linkRole/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "schema": "http://schema.org/",
    "skos": "http://www.w3.org/2004/02/skos/core#",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/linkRole/context.jsonld)

## Sources

* [schema.org LinkRole](https://schema.org/LinkRole)
* [schema.org EntryPoint](https://schema.org/EntryPoint)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/Cross-Domain-Interoperability-Framework/metadataBuildingBlocks](https://github.com/Cross-Domain-Interoperability-Framework/metadataBuildingBlocks)
* Path: `_sources/schemaorgProperties/linkRole`

