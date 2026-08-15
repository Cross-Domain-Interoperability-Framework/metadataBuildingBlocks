
# Properties for PROV was derived from (Schema)

`cdif.bbr.metadata.provProperties.derivedFrom` *v0.1*

Schema defining properties for documenting sources used for compiled or aggregated dataset. Defines properties: prov:wasDerivedFrom. Uses building blocks: cdifReference (cdifDataType).

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
    "dcterms": "http://purl.org/dc/terms/",
    "dcat": "http://www.w3.org/ns/dcat#"
  },
  "@type": [
    "schema:CreativeWork",
    "dcat:Relationship"
  ],
  "schema:name": "Source dataset (DOI)",
  "schema:url": "http://doi.org/10.547/347848",
  "dcterms:relation": "http://doi.org/10.547/347848"
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
      "dcterms": "http://purl.org/dc/terms/",
      "dcat": "http://www.w3.org/ns/dcat#"
    }
  ],
  "@type": [
    "schema:CreativeWork",
    "dcat:Relationship"
  ],
  "schema:name": "Source dataset (DOI)",
  "schema:url": "http://doi.org/10.547/347848",
  "dcterms:relation": "http://doi.org/10.547/347848"
}
```

#### ttl
```ttl
@prefix dcat: <http://www.w3.org/ns/dcat#> .
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix schema1: <http://schema.org/> .

[] a schema1:CreativeWork,
        dcat:Relationship ;
    dcterms:relation "http://doi.org/10.547/347848" ;
    schema1:name "Source dataset (DOI)" ;
    schema1:url "http://doi.org/10.547/347848" .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: very simple links or names of data sources used to generate the described resource.
anyOf:
- type: string
- type: object
  required:
  - '@id'
  additionalProperties: false
  properties:
    '@id':
      type: string
      description: a resolvable reference to a representation of the software or instrument
        used
- $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifDataType/cdifReference/schema.yaml
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
    "skos": "http://www.w3.org/2004/02/skos/core#",
    "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
    "cdif": "https://w3id.org/cdif/",
    "ex": "https://example.org/",
    "xsd": "http://www.w3.org/2001/XMLSchema#",
    "dcterms": "http://purl.org/dc/terms/",
    "dcat": "http://www.w3.org/ns/dcat#",
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

