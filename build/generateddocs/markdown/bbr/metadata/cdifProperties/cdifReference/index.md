
# CDIF Reference (Schema)

`cdif.bbr.metadata.cdifProperties.cdifReference` *v0.1*

A typed reference to an external entity, combining the schema.org labeled-link surface (name, description, url) with the DDI-CDI dt-Reference semantics (uri, description) and an optional cdif:semantic role expressed as a SKOS Concept. Replaces direct use of schemaorgProperties/labeledLink whenever a reference needs an explicit semantic role or DDI-CDI provenance. Defines properties: @type (must include 'cdif:Reference'), schema:name, schema:description, schema:url (required), cdi:uri, cdi:description, cdif:semantic (skos:Concept).

[*Status*](http://www.opengis.net/def/status): Under development

## Description

## CDIF Reference

Defines a typed reference to an external entity for use within CDIF metadata. A `cdif:Reference` combines three things:

1. The schema.org `CreativeWork` surface inherited from `schemaorgProperties/labeledLink` — a human-readable `schema:name`, `schema:description`, and required `schema:url`.
2. The DDI-CDI `dt-Reference` semantics — `cdi:uri` for the canonical machine-readable identifier of the referenced entity (which may differ from a presentation URL), and `cdi:description` for the DDI-CDI-style description.
3. An optional `cdif:semantic` slot expressing the *role* of this reference as a [SKOS Concept](https://www.w3.org/TR/skos-reference/) — for example, distinguishing a reference to a physical sample from a reference to its registration metadata (see [Discovery issue 13](https://github.com/Cross-Domain-Interoperability-Framework/Discovery/issues/13)).

### When to use

Prefer `cdif:Reference` over `schemaorgProperties/labeledLink` whenever a reference needs:

- An explicit **semantic role** beyond "labeled link" (use `cdif:semantic`).
- A **distinct identifier** for the referenced entity separate from a presentation URL (use `cdi:uri`).
- Round-trippability with the DDI-CDI `dt-Reference` data type.

Continue to use `labeledLink` directly when the reference is a plain hyperlink and no semantic role is required.

### Required properties

- `@type` must contain `cdif:Reference` (and inherits the `schema:CreativeWork` requirement from labeledLink, so `@type` is typically `["schema:CreativeWork", "cdif:Reference"]`).
- `schema:url` is required (inherited from labeledLink).

All other properties are optional.

### Type declaration

JSON-LD instance documents that conform to this building block must declare `cdif:Reference` (rather than the previous `cdi:Reference`) in the `@type` array. The CDIF profile now owns the `Reference` concept; the `cdif:` namespace makes that ownership explicit and lets the SHACL rule below target it without conflicting with DDI-CDI's native `cdi:Reference` definition.

### Relationship to DDI-CDI

DDI-CDI defines `dt-Reference` as a DataType with attributes including a URI and a description. CDIF promotes this concept to a profile-level type (`cdif:Reference`) so that profile validators can target it directly via SHACL and so cross-profile UML can reference one canonical class. The `cdi:` attribute names are retained to preserve the round-trip with DDI-CDI source models; only the *type label* has been re-namespaced.

## Examples

### CDIF Reference - minimal
Minimal cdif:Reference. Declares the @type as both schema:CreativeWork (inherited
from labeledLink) and cdif:Reference (the CDIF profile type label). Carries the
required schema:url plus a distinct cdi:uri to address the referenced entity
independently of its presentation page.
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
    "cdif": "https://cdif.org/0.1/",
    "ex": "https://example.org/"
  },
  "@id": "ex:CdifReferenceExample_001",
  "@type": ["schema:CreativeWork", "cdif:Reference"],
  "schema:name": "Source dataset for derived measurements",
  "schema:url": "https://example.org/datasets/source-2024",
  "cdi:uri": "https://doi.org/10.5281/zenodo.7654321"
}

```

#### jsonld
```jsonld
{
  "@context": [
    {
      "schema": "http://schema.org/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "cdif": "https://cdif.org/0.1/"
    },
    "https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifProperties/cdifReference/context.jsonld",
    {
      "schema": "http://schema.org/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "cdif": "https://cdif.org/0.1/",
      "ex": "https://example.org/"
    }
  ],
  "@id": "ex:CdifReferenceExample_001",
  "@type": [
    "schema:CreativeWork",
    "cdif:Reference"
  ],
  "schema:name": "Source dataset for derived measurements",
  "schema:url": "https://example.org/datasets/source-2024",
  "cdi:uri": "https://doi.org/10.5281/zenodo.7654321"
}
```

#### ttl
```ttl
@prefix cdi: <http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/> .
@prefix cdif: <https://cdif.org/0.1/> .
@prefix ex: <https://example.org/> .
@prefix schema1: <http://schema.org/> .

ex:CdifReferenceExample_001 a schema1:CreativeWork,
        cdif:Reference ;
    cdi:uri "https://doi.org/10.5281/zenodo.7654321" ;
    schema1:name "Source dataset for derived measurements" ;
    schema1:url "https://example.org/datasets/source-2024" .


```


### CDIF Reference - complete (with semantic role)
Full cdif:Reference exercising the cdif:semantic slot. Uses a SKOS Concept to
classify the reference as a 'sample registration record' (distinguishing this
metadata-about-the-sample from a reference to the physical sample itself).
See https://github.com/Cross-Domain-Interoperability-Framework/Discovery/issues/13
for the motivating discussion.
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "skos": "http://www.w3.org/2004/02/skos/core#",
    "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
    "cdif": "https://cdif.org/0.1/",
    "ex": "https://example.org/"
  },
  "@id": "ex:CdifReferenceComplete_001",
  "@type": ["schema:CreativeWork", "cdif:Reference"],
  "schema:name": "Sample registration record IGSN IECUR0001",
  "schema:description": "Landing page in the SESAR registry describing this physical rock sample.",
  "schema:url": "https://app.geosamples.org/sample/igsn/IECUR0001",
  "cdi:uri": "https://hdl.handle.net/10273/IECUR0001",
  "cdi:description": "Canonical IGSN handle identifying the physical sample, distinct from the registry landing page above.",
  "cdif:semantic": {
    "@id": "ex:concepts/sampleRegistration",
    "@type": ["skos:Concept"],
    "skos:prefLabel": {
      "@value": "sample registration record",
      "@language": "en"
    },
    "skos:inScheme": { "@id": "ex:vocab/referenceRoles" },
    "skos:notation": ["sampleRegistration"]
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
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "cdif": "https://cdif.org/0.1/"
    },
    "https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifProperties/cdifReference/context.jsonld",
    {
      "schema": "http://schema.org/",
      "skos": "http://www.w3.org/2004/02/skos/core#",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "cdif": "https://cdif.org/0.1/",
      "ex": "https://example.org/"
    }
  ],
  "@id": "ex:CdifReferenceComplete_001",
  "@type": [
    "schema:CreativeWork",
    "cdif:Reference"
  ],
  "schema:name": "Sample registration record IGSN IECUR0001",
  "schema:description": "Landing page in the SESAR registry describing this physical rock sample.",
  "schema:url": "https://app.geosamples.org/sample/igsn/IECUR0001",
  "cdi:uri": "https://hdl.handle.net/10273/IECUR0001",
  "cdi:description": "Canonical IGSN handle identifying the physical sample, distinct from the registry landing page above.",
  "cdif:semantic": {
    "@id": "ex:concepts/sampleRegistration",
    "@type": [
      "skos:Concept"
    ],
    "skos:prefLabel": {
      "@value": "sample registration record",
      "@language": "en"
    },
    "skos:inScheme": {
      "@id": "ex:vocab/referenceRoles"
    },
    "skos:notation": [
      "sampleRegistration"
    ]
  }
}
```

#### ttl
```ttl
@prefix cdi: <http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/> .
@prefix cdif: <https://cdif.org/0.1/> .
@prefix ex: <https://example.org/> .
@prefix schema1: <http://schema.org/> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .

ex:CdifReferenceComplete_001 a schema1:CreativeWork,
        cdif:Reference ;
    cdi:description "Canonical IGSN handle identifying the physical sample, distinct from the registry landing page above." ;
    cdi:uri "https://hdl.handle.net/10273/IECUR0001" ;
    schema1:description "Landing page in the SESAR registry describing this physical rock sample." ;
    schema1:name "Sample registration record IGSN IECUR0001" ;
    schema1:url "https://app.geosamples.org/sample/igsn/IECUR0001" ;
    cdif:semantic <https://example.org/concepts/sampleRegistration> .

<https://example.org/concepts/sampleRegistration> a skos:Concept ;
    skos:inScheme <https://example.org/vocab/referenceRoles> ;
    skos:notation "sampleRegistration" ;
    skos:prefLabel "sample registration record"@en .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
type: object
description: see https://github.com/Cross-Domain-Interoperability-Framework/Discovery/issues/13
  for discussion on how to make assertion about the sample registration and metadata
  distinct from statements about the physical object
allOf:
- $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/labeledLink/schema.yaml
- $ref: '#/$defs/Reference'
$defs:
  Reference:
    type: object
    description: based on DDI-CDI reference to an entity (dt-Reference)
    properties:
      '@type':
        type: array
        items:
          type: string
        contains:
          const: cdif:Reference
        minItems: 1
      cdi:uri:
        type: string
        format: uri
        description: URI of the referenced entity
      cdi:description:
        type: string
        description: Human-readable description of the reference
      cdif:semantic:
        description: Semantic role of this reference
        $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/skosProperties/skosConcept/schema.yaml
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
* [DDI-CDI dt-Reference](https://ddialliance.org/Specification/DDI-CDI/1.0/)
* [SKOS Concept (semantic role)](https://www.w3.org/TR/skos-reference/)
* [Discovery issue 13 - distinct assertions about sample registration vs physical object](https://github.com/Cross-Domain-Interoperability-Framework/Discovery/issues/13)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/Cross-Domain-Interoperability-Framework/metadataBuildingBlocks](https://github.com/Cross-Domain-Interoperability-Framework/metadataBuildingBlocks)
* Path: `_sources/cdifProperties/cdifReference`

