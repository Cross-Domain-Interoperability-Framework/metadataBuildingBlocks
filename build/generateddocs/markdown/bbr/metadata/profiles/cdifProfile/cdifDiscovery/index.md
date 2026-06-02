
# CDIF Discovery (Schema)

`cdif.bbr.metadata.profiles.cdifProfile.cdifDiscovery` *v0.1*

Profile module for discovery metadata. Currently a thin wrapper that composes cdifCore; reserved for discovery-specific extensions (measurement technique, spatial/temporal coverage, quality measurements) that are not part of the cdifCore foundation. INTERPROFILE DEPENDENCY: cdifCore (cdifProfile).

[*Status*](http://www.opengis.net/def/status): Under development

## Description

# CDIF Discovery

Profile module for discovery metadata.

## Status

Placeholder. Currently composes cdifCore via `allOf`; reserved for future
discovery-specific extensions that are not part of the cdifCore foundation
(e.g. measurement technique, spatial/temporal coverage, quality measurements
when those are split out of cdifCore).

## Interprofile dependencies

- `cdifCore` (cdifProfile) — composed via `allOf`

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: CDIF Discovery
description: Profile module for discovery metadata. Currently a thin wrapper that
  composes cdifCore; reserved for discovery-specific extensions that are not part
  of the cdifCore foundation.
type: object
properties:
  '@context':
    type: object
    description: Additional JSON-LD namespace prefixes for discovery properties.
    properties:
      geosparql:
        const: http://www.opengis.net/ont/geosparql#
      dqv:
        const: http://www.w3.org/ns/dqv#
      cdi:
        const: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/
  schema:measurementTechnique:
    description: The technique, technology, or methodology used for measurement or
      determination of the dataset values.
    type: array
    items:
      anyOf:
      - type: string
      - $ref: '#/$defs/cdifConceptOrTerm'
  schema:variableMeasured:
    description: What does the dataset measure? (e.g., temperature, pressure)
    type: array
    items:
      $ref: '#/$defs/VariableMeasured'
  schema:spatialCoverage:
    description: Geographic extent of resource content.
    type: array
    items:
      $ref: '#/$defs/SpatialExtent'
  schema:temporalCoverage:
    description: Temporal extent of resource content.
    type: array
    items:
      $ref: '#/$defs/TemporalExtent'
  dqv:hasQualityMeasurement:
    description: Quality measurements reported to assess the resource.
    type: array
    items:
      $ref: '#/$defs/QualityMeasure'
  schema:subjectOf:
    properties:
      dcterms:conformsTo:
        contains:
          type: object
          properties:
            '@id':
              const: https://w3id.org/cdif/discovery/1.1
$defs:
  cdifConceptOrTerm:
    anyOf:
    - type: object
      properties:
        '@id':
          type: string
          description: reference to a skos concept for the data type
    - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/definedTerm/schema.yaml
    - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/profiles/cdifProfile/cdifConceptScheme/schema.yaml#/$defs/cdifConcept
  VariableMeasured:
    $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/variableMeasured/schema.yaml
  SpatialExtent:
    $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/spatialExtent/schema.yaml
  TemporalExtent:
    $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/temporalExtent/schema.yaml
  QualityMeasure:
    $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/qualityProperties/qualityMeasure/schema.yaml

```

Links to the schema:

* YAML version: [schema.yaml](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/profiles/cdifProfile/cdifDiscovery/schema.json)
* JSON version: [schema.json](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/profiles/cdifProfile/cdifDiscovery/schema.yaml)


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
    "time": "http://www.w3.org/2006/time#",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/profiles/cdifProfile/cdifDiscovery/context.jsonld)


# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/Cross-Domain-Interoperability-Framework/metadataBuildingBlocks](https://github.com/Cross-Domain-Interoperability-Framework/metadataBuildingBlocks)
* Path: `_sources/profiles/cdifProfile/cdifDiscovery`

