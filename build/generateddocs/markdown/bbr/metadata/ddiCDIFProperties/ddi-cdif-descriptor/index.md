
# DDI-CDIF Descriptor (Schema)

`cdif.bbr.metadata.ddiCDIFProperties.ddi-cdif-descriptor` *v0.1*

Code value appearing in a Long Data Set's Descriptor Variable column. Each Descriptor has a `cdi:content` (the code) and `cdi:identifies` association to the logical cdi:InstanceVariable whose values are carried in the corresponding Reference Variable column. CDIF Data Description profile form of cdi:Descriptor.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

DDI-CDI Descriptor as used in the CDIF Data Description profile. A Descriptor is a code value appearing in the Descriptor Variable column of a Long Data Set; each instance pairs a `cdi:content` string (the code, e.g. "Temp", "Pulse", "Weight") with a `cdi:identifies` association pointing to the logical `cdi:InstanceVariable` whose value is carried in the corresponding Reference Variable column.

Both `cdi:content` and `cdi:identifies` are required per Appendix 4 of the CDIF Data Description profile. The CDIF form targets `cdi:InstanceVariable` directly — the canonical DDI-CDI XMI's narrower target (`cdi:ReferenceVariable`) is automatically satisfied because `ReferenceVariable rdfs:subClassOf InstanceVariable`. Used together with `ddi-cdif-presentational-variable` (DescriptorVariable) and `ddi-cdif-value-domain` (DescriptorValueDomain) when describing Long Data Structures.

## Examples

### Minimal Descriptor
TODO: replace with a JSON-LD example.
## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: DDI-CDIF Descriptor
description: 'Code value appearing in a Long Data Set''s Descriptor Variable column,
  identifying the logical InstanceVariable that the corresponding value in the Reference
  Variable column is a measure of. CDIF profile of cdi:Descriptor: simplified to the
  two properties named in Appendix 4 of the CDIF Data Description Profile (`cdi:content`,
  `cdi:identifies`), with `cdi:identifies` targeting the conceptual InstanceVariable
  rather than the canonical XMI''s ReferenceVariable (the XMI form is satisfied too,
  since ReferenceVariable specialises InstanceVariable).'
type: object
properties:
  '@type':
    type: array
    items:
      type: string
    contains:
      const: cdi:Descriptor
    minItems: 1
  '@id':
    type: string
    description: Identifier for this Descriptor node.
  cdi:content:
    type: string
    description: The descriptor value appearing in the Long Data Set, expressed as
      a simple string (e.g. "Temp", "Pulse", "Weight").
  cdi:identifies:
    anyOf:
    - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiCDIFProperties/ddi-cdif-instance-variable/schema.yaml
    - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiCDIFProperties/ddi-cdif-data-types/schema.yaml#/$defs/id-reference
    description: Reference to the cdi:InstanceVariable (the logical variable being
      measured) that the corresponding value in the Reference Variable column is associated
      with. Use an inline InstanceVariable or an `@id` reference to one declared elsewhere
      in the metadata.
required:
- '@type'
- cdi:content
- cdi:identifies
x-jsonld-prefixes:
  cdi: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/

```

Links to the schema:

* YAML version: [schema.yaml](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiCDIFProperties/ddi-cdif-descriptor/schema.json)
* JSON version: [schema.json](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiCDIFProperties/ddi-cdif-descriptor/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
    "skos": "http://www.w3.org/2004/02/skos/core#",
    "schema": "http://schema.org/",
    "spdx": "http://spdx.org/rdf/terms#",
    "xas": "https://xas.org/dictionary/",
    "nxs": "http://purl.org/nexusformat/definitions/",
    "prov": "http://www.w3.org/ns/prov#",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiCDIFProperties/ddi-cdif-descriptor/context.jsonld)

## Sources

* [CDIF DDI-CDI Data Description Profile](https://w3id.org/cdif/data_description/1.0)
* [DDI-CDI 1.0 Specification](https://ddialliance.org/Specification/DDI-CDI/1.0/)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/Cross-Domain-Interoperability-Framework/metadataBuildingBlocks](https://github.com/Cross-Domain-Interoperability-Framework/metadataBuildingBlocks)
* Path: `_sources/ddiCDIFProperties/ddi-cdif-descriptor`

