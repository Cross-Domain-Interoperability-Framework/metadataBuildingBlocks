
# Labeled Link (Schema)

`cdif.bbr.metadata.schemaorgProperties.labeledLink` *v0.1*

Schema defining propertis for a labeled link, implemented using a profile of schema.org/CreativeWork. Defines properties: @type, schema:name, schema:description, schema:url.

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
    "@type": "schema:CreativeWork",
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
  "@type": "schema:CreativeWork",
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

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
description: schema for a labeled link, a profile of schema.org/CreativeWork
type: object
properties:
  '@type':
    default: schema:CreativeWork
    anyOf:
    - type: string
      const: schema:CreativeWork
    - type: array
      items:
        type: string
      contains:
        const: schema:CreativeWork
  schema:name:
    type: string
  schema:description:
    type: string
  schema:url:
    type: string
    format: uri
required:
- '@type'
- schema:url
x-jsonld-prefixes:
  schema: http://schema.org/

```

Links to the schema:

* YAML version: [schema.yaml](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/labeledLink/schema.json)
* JSON version: [schema.json](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/labeledLink/schema.yaml)


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
[context.jsonld](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/labeledLink/context.jsonld)

## Sources

* [schema.org](https://schema.org/CreativeWork)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/Cross-Domain-Interoperability-Framework/metadataBuildingBlocks](https://github.com/Cross-Domain-Interoperability-Framework/metadataBuildingBlocks)
* Path: `_sources/schemaorgProperties/labeledLink`

