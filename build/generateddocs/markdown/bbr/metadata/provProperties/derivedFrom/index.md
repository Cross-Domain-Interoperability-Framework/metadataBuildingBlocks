
# Properties for PROV was derived from (Schema)

`cdif.bbr.metadata.provProperties.derivedFrom` *v0.1*

Schema defining properties for documenting sources used for compiled or aggregated dataset. Defines properties: prov:wasDerivedFrom. Uses building blocks: labeledLink (schemaorgProperties).

[*Status*](http://www.opengis.net/def/status): Under development

## Description

## PROV derived from properties

Defines a set of properties for specifying sources of data or interpretation used in the generation of a derived resource.  Uses terms from the base prov vocabulary. For the schema.org implementation of the [Cross Domain Interoperability Framework](https://cross-domain-interoperability-framework.github.io/cdifbook/metadata/schemaorgimplementation.html#implementation-of-metadata-content-items) (CDIF) discovery profile.
## Examples

### Example PROV derived from.
very simple implementation for discovery-level citation of sources used to generate a resource. Note this building block defines a property, not a node.
#### json
```json
{
    "@context": {
        "schema": "http://schema.org/",
        "prov": "http://www.w3.org/ns/prov#",
        "nerc": "https://vocab.nerc.ac.uk/",
        "ex": "https://example.org/"
    },
    "@id": "ex:generatedBy_345y254h",
    "prov:wasDerivedFrom": [
        {"@id": "http://doi.org/10.547/347848"},
        "http://doi.org/10.3578/h5ls",
        {
            "@id": "ex:source_z536Zc",
            "@type": "schema:CreativeWork",
            "schema:name": "Title data source",
            "schema:description": "short summary of source content",
            "schema:url": "https://doi.org/20456/2342747"
        }
    ]
}
```

#### jsonld
```jsonld
{
  "@context": [
    {
      "schema": "http://schema.org/",
      "prov": "http://www.w3.org/ns/prov#",
      "nerc": "https://vocab.nerc.ac.uk/",
      "ex": "https://example.org/"
    },
    "https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/provProperties/derivedFrom/context.jsonld",
    {
      "schema": "http://schema.org/",
      "prov": "http://www.w3.org/ns/prov#",
      "nerc": "https://vocab.nerc.ac.uk/",
      "ex": "https://example.org/"
    }
  ],
  "@id": "ex:generatedBy_345y254h",
  "prov:wasDerivedFrom": [
    {
      "@id": "http://doi.org/10.547/347848"
    },
    "http://doi.org/10.3578/h5ls",
    {
      "@id": "ex:source_z536Zc",
      "@type": "schema:CreativeWork",
      "schema:name": "Title data source",
      "schema:description": "short summary of source content",
      "schema:url": "https://doi.org/20456/2342747"
    }
  ]
}
```

#### ttl
```ttl
@prefix ex: <https://example.org/> .
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix schema1: <http://schema.org/> .

ex:generatedBy_345y254h prov:wasDerivedFrom <http://doi.org/10.547/347848>,
        ex:source_z536Zc,
        "http://doi.org/10.3578/h5ls" .

ex:source_z536Zc a schema1:CreativeWork ;
    schema1:description "short summary of source content" ;
    schema1:name "Title data source" ;
    schema1:url "https://doi.org/20456/2342747" .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: very simple links or names of data sources used to generate the described resource.
anyOf:
- type: string
- type: object
  properties:
    '@id':
      type: string
      description: a resolvable reference to a representation of the software or instrument
        used
- $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/labeledLink/schema.yaml
x-jsonld-prefixes:
  schema: http://schema.org/
  prov: http://www.w3.org/ns/prov#

```

Links to the schema:

* YAML version: [schema.yaml](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/provProperties/derivedFrom/schema.json)
* JSON version: [schema.json](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/provProperties/derivedFrom/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "schema": "http://schema.org/",
    "prov": "http://www.w3.org/ns/prov#",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/provProperties/derivedFrom/context.jsonld)

## Sources

* [See Provenance for discovery in Implementation of metadata content items](https://cross-domain-interoperability-framework.github.io/cdifbook/metadata/schemaorgimplementation.html#implementation-of-metadata-content-items)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/Cross-Domain-Interoperability-Framework/metadataBuildingBlocks](https://github.com/Cross-Domain-Interoperability-Framework/metadataBuildingBlocks)
* Path: `_sources/provProperties/derivedFrom`

