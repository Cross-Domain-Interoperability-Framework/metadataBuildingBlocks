
# DDI-CDIF Descriptor (Schema)

`cdif.bbr.metadata.ddiCDIFProperties.ddi-cdif-descriptor` *v0.1*

Code value appearing in a Long Data Set's Descriptor Variable column. Each Descriptor has a `cdi:content` (the code) and `cdi:identifies` association to the logical cdi:InstanceVariable whose values are carried in the corresponding Reference Variable column. CDIF Data Description profile form of cdi:Descriptor.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

DDI-CDI Descriptor as used in the CDIF Data Description profile. A Descriptor is a code value appearing in the Descriptor Variable column of a Long Data Set; each instance pairs a `cdi:content` string (the code, e.g. "Temp", "Pulse", "Weight") with a `cdi:identifies` association pointing to the logical `cdi:InstanceVariable` whose value is carried in the corresponding Reference Variable column.

Both `cdi:content` and `cdi:identifies` are required per Appendix 4 of the CDIF Data Description profile. The CDIF form targets `cdi:InstanceVariable` directly — the canonical DDI-CDI XMI's narrower target (`cdi:ReferenceVariable`) is automatically satisfied because `ReferenceVariable rdfs:subClassOf InstanceVariable`. Used together with `ddi-cdif-presentational-variable` (DescriptorVariable) and `ddi-cdif-value-domain` (DescriptorValueDomain) when describing Long Data Structures.

## Examples

### Minimal Descriptor
Bare Descriptor with the required cdi:content code value and an
@id-only cdi:identifies reference to the InstanceVariable.
#### json
```json
{
  "@context": {
    "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
    "ex": "https://example.org/"
  },
  "@type": ["cdi:Descriptor"],
  "@id": "ex:dataset/longClinical/descriptor/temp",
  "cdi:content": "Temp",
  "cdi:identifies": {
    "@id": "ex:dataset/longClinical/var/temperature"
  }
}

```

#### jsonld
```jsonld
{
  "@context": [
    {
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/"
    },
    "https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiCDIFProperties/ddi-cdif-descriptor/context.jsonld",
    {
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "ex": "https://example.org/"
    }
  ],
  "@type": [
    "cdi:Descriptor"
  ],
  "@id": "ex:dataset/longClinical/descriptor/temp",
  "cdi:content": "Temp",
  "cdi:identifies": {
    "@id": "ex:dataset/longClinical/var/temperature"
  }
}
```

#### ttl
```ttl
@prefix cdi: <http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/> .

<https://example.org/dataset/longClinical/descriptor/temp> a cdi:Descriptor ;
    cdi:content "Temp" ;
    cdi:identifies <https://example.org/dataset/longClinical/var/temperature> .


```


### Complete Descriptor
Long Data Set Descriptor for the "Temp" row identifying a body-temperature
InstanceVariable with full schema.org/cdi structure inlined — exercises
every property of the Descriptor (cdi:content, cdi:identifies inline form)
and demonstrates a fully-described target InstanceVariable.
#### json
```json
{
  "@context": {
    "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
    "ex": "https://example.org/",
    "schema": "http://schema.org/",
    "xsd": "http://www.w3.org/2001/XMLSchema#"
  },
  "@type": ["cdi:Descriptor"],
  "@id": "ex:dataset/longClinical/descriptor/temp",
  "cdi:content": "Temp",
  "cdi:identifies": {
    "@type": [
      "cdi:InstanceVariable",
      "schema:PropertyValue"
    ],
    "@id": "ex:dataset/longClinical/var/temperature",
    "schema:name": "temperature",
    "schema:alternateName": ["Body temperature"],
    "schema:description": "Patient body temperature in degrees Celsius.",
    "schema:unitText": "°C",
    "cdi:identifier": {
      "@type": ["cdi:Identifier"],
      "cdi:uri": "https://example.org/dataset/longClinical/var/temperature"
    },
    "cdi:physicalDataType": ["xsd:decimal"],
    "cdi:simpleUnitOfMeasure": "°C",
    "cdi:name": "temperature",
    "cdi:displayLabel": "Body temperature",
    "cdi:role": "ReferenceValueComponent"
  }
}

```

#### jsonld
```jsonld
{
  "@context": [
    {
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "schema": "http://schema.org/",
      "xsd": "http://www.w3.org/2001/XMLSchema#"
    },
    "https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiCDIFProperties/ddi-cdif-descriptor/context.jsonld",
    {
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "ex": "https://example.org/",
      "schema": "http://schema.org/",
      "xsd": "http://www.w3.org/2001/XMLSchema#"
    }
  ],
  "@type": [
    "cdi:Descriptor"
  ],
  "@id": "ex:dataset/longClinical/descriptor/temp",
  "cdi:content": "Temp",
  "cdi:identifies": {
    "@type": [
      "cdi:InstanceVariable",
      "schema:PropertyValue"
    ],
    "@id": "ex:dataset/longClinical/var/temperature",
    "schema:name": "temperature",
    "schema:alternateName": [
      "Body temperature"
    ],
    "schema:description": "Patient body temperature in degrees Celsius.",
    "schema:unitText": "\u00b0C",
    "cdi:identifier": {
      "@type": [
        "cdi:Identifier"
      ],
      "cdi:uri": "https://example.org/dataset/longClinical/var/temperature"
    },
    "cdi:physicalDataType": [
      "xsd:decimal"
    ],
    "cdi:simpleUnitOfMeasure": "\u00b0C",
    "cdi:name": "temperature",
    "cdi:displayLabel": "Body temperature",
    "cdi:role": "ReferenceValueComponent"
  }
}
```

#### ttl
```ttl
@prefix cdi: <http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/> .
@prefix schema1: <http://schema.org/> .

<https://example.org/dataset/longClinical/descriptor/temp> a cdi:Descriptor ;
    cdi:content "Temp" ;
    cdi:identifies <https://example.org/dataset/longClinical/var/temperature> .

<https://example.org/dataset/longClinical/var/temperature> a cdi:InstanceVariable,
        schema1:PropertyValue ;
    cdi:displayLabel "Body temperature" ;
    cdi:identifier [ a cdi:Identifier ;
            cdi:uri "https://example.org/dataset/longClinical/var/temperature" ] ;
    cdi:name "temperature" ;
    cdi:physicalDataType "xsd:decimal" ;
    cdi:role "ReferenceValueComponent" ;
    cdi:simpleUnitOfMeasure "°C" ;
    schema1:alternateName "Body temperature" ;
    schema1:description "Patient body temperature in degrees Celsius." ;
    schema1:name "temperature" ;
    schema1:unitText "°C" .


```

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
  cdif:content:
    type: string
    description: The descriptor value appearing in the Long Data Set, expressed as
      a simple string (e.g. "Temp", "Pulse", "Weight").
  cdif:identifies:
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

