
# CDIF Data Structure profile (Schema)

`cdif.bbr.metadata.profiles.cdifProfiles.CDIFDataStructureProfile` *v0.1*

Extends the CDIF Data Description profile with full DDI-CDI structural complexity: data structures (DataStructure / Dimensional / Long / Wide), component subclasses (Identifier / Measure / Attribute / Dimension / VariableValue / VariableDescriptor), represented variables, and value domains. Distribution items are expected to carry cdi:isStructuredBy pointing at a Data Structure node.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

# CDIF Data Structure profile

The **CDIF Data Structure profile** extends the [Data Description profile](../CDIFDataDescriptionProfile/) with full DDI-CDI structural complexity. Use this profile when the catalog record must commit to *how* the data is organized — which variables play which role, what the keys are, what value domains constrain measurements — not just *which* variables are measured.

## What it adds beyond Data Description

- **Component subclasses.** [cdifDataStructureComponent](../../../cdifProperties/cdifDataStructureComponent/) defines `cdi:IdentifierComponent`, `cdi:MeasureComponent`, `cdi:AttributeComponent`, `cdi:DimensionComponent`, `cdi:VariableValueComponent`, and `cdi:VariableDescriptorComponent` as Node classes — the structural counterparts to the role values carried directly on InstanceVariables in the Data Description profile.
- **Polymorphic DataStructure root.** [cdifDataStructure](../../../cdifProperties/cdifDataStructure/) carries `cdi:DataStructure`, `cdi:DimensionalDataStructure`, `cdi:LongDataStructure`, and `cdi:WideDataStructure`, plus shared structural types (`cdi:DimensionGroup`, `cdi:ForeignKey`, `cdi:ForeignKeyComponent`, `cdif:PrimaryKey`, `cdi:PrimaryKeyComponent`).
- **Represented variables and value domains.** [cdifRepresentedVariable](../../../cdifProperties/cdifRepresentedVariable/) and [cdifValueDomain](../../../cdifProperties/cdifValueDomain/) provide the conceptual variable definitions and substantive/sentinel value domains referenced from components.
- **Distribution is structured.** This profile requires every `schema:distribution` item to carry `cdi:isStructuredBy` pointing at a Data Structure node (Data Description allows it but does not require it).

## Conformance

This profile composes [cdifCore](../../../cdifProperties/cdifCore/) and [cdifDataDescription](../../../cdifProperties/cdifDataDescription/), so a conforming record must carry `dcterms:conformsTo` URIs for all three:

- `https://w3id.org/cdif/core/1.0`
- `https://w3id.org/cdif/data_description/1.0`
- `https://w3id.org/cdif/data_structure/1.0`

## When to use which profile

| Want to publish... | Use profile |
|---|---|
| Catalog record with `schema:variableMeasured` and roles, no structure commitment | [Data Description](../CDIFDataDescriptionProfile/) |
| Wide table with simple measures | [Data Description](../CDIFDataDescriptionProfile/) |
| Long-format data (descriptor + reference columns) | **CDIF Data Structure** |
| Dimensional / cube data | **CDIF Data Structure** |
| Anything where consumers need keys + components + value domains | **CDIF Data Structure** |

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
type: object
title: CDIF Data Structure metadata profile
description: 'CDIF Data Structure profile. Extends the Data Description profile with
  full DDI-CDI structural complexity: composing cdifDataStructure (DataStructure +
  Dimensional/Long/Wide variants), cdifDataStructureComponent (component subclasses),
  cdifRepresentedVariable, and cdifValueDomain. Distributions are expected to carry
  cdi:isStructuredBy pointing at a Data Structure node.'
allOf:
- $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifProperties/cdifCore/schema.yaml
- $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifProperties/cdifDataDescription/schema.yaml
- type: object
  properties:
    '@context':
      type: object
      description: Additional JSON-LD namespace prefixes for the data structure profile.
      properties:
        geosparql:
          const: http://www.opengis.net/ont/geosparql#
        dqv:
          const: http://www.w3.org/ns/dqv#
        cdi:
          const: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/
        cdif:
          const: https://cdif.org/0.1/
    schema:distribution:
      items:
        required:
        - cdi:isStructuredBy
    schema:subjectOf:
      properties:
        dcterms:conformsTo:
          contains:
            type: object
            properties:
              '@id':
                const: https://w3id.org/cdif/data_structure/1.0
$defs:
  CdifDataStructure:
    $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifProperties/cdifDataStructure/schema.yaml
  CdifDataStructureComponent:
    $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifProperties/cdifDataStructureComponent/schema.yaml
  CdifRepresentedVariable:
    $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifProperties/cdifRepresentedVariable/schema.yaml
  CdifValueDomain:
    $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifProperties/cdifValueDomain/schema.yaml

```

Links to the schema:

* YAML version: [schema.yaml](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/profiles/cdifProfiles/CDIFDataStructureProfile/schema.json)
* JSON version: [schema.json](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/profiles/cdifProfiles/CDIFDataStructureProfile/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "schema": "http://schema.org/",
    "prov": "http://www.w3.org/ns/prov#",
    "ex": "https://example.org/",
    "xsd": "http://www.w3.org/2001/XMLSchema#",
    "dcterms": "http://purl.org/dc/terms/",
    "dcat": "http://www.w3.org/ns/dcat#",
    "spdx": "http://spdx.org/rdf/terms#",
    "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
    "skos": "http://www.w3.org/2004/02/skos/core#",
    "xas": "https://xas.org/dictionary/",
    "nxs": "http://purl.org/nexusformat/definitions/",
    "cdif": "https://cdif.org/0.1/",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/profiles/cdifProfiles/CDIFDataStructureProfile/context.jsonld)

## Sources

* [DDI-CDI 1.0 Specification](https://ddialliance.org/Specification/DDI-CDI/1.0/)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/Cross-Domain-Interoperability-Framework/metadataBuildingBlocks](https://github.com/Cross-Domain-Interoperability-Framework/metadataBuildingBlocks)
* Path: `_sources/profiles/cdifProfiles/CDIFDataStructureProfile`

