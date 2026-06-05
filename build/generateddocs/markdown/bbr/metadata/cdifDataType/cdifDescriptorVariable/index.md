
# DDI-CDI Descriptor Variable (Schema)

`cdif.bbr.metadata.cdifDataType.cdifDescriptorVariable` *v0.1*

Variable that records values of multiple variables in the context of a data structure.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

# CDIF Descriptor Variable

A **DDI-CDI Descriptor Variable** is a presentational variable found only in **Long Data Sets**. It records the codes that appear in the dataset's descriptor column — each code naming which logical variable the value in the corresponding Reference Variable column is a measure for.

For example, in a long-format vitals table:

| patient_id | measure_name | measure_value |
|---|---|---|
| P001 | systolic_bp | 132 |
| P001 | heart_rate | 78 |

`measure_name` is the descriptor column; the values it takes (`systolic_bp`, `heart_rate`) are descriptor codes that name the conceptual RepresentedVariables they identify.

## Structure

A `cdi:DescriptorVariable` carries:

| Property | Required | Notes |
|---|---|---|
| `@type` | required | Must include `cdi:DescriptorVariable`. |
| `@id` | recommended | Identifier for the variable node. |
| `cdif:hasValuesFrom` | **required** | A `cdi:DescriptorValueDomain` enumerating the descriptor codes (see below). |
| `cdi:name` | optional | Array of `cdi:ObjectName` (formal naming per ISO 11179-5). |

The **`cdi:DescriptorValueDomain`** has a required `cdif:takesValuesFrom` array of descriptor entries. Each entry pairs:

- `cdif:value` — the code as it appears in the descriptor column (e.g. `"systolic_bp"`).
- `cdif:isDefinedBy` — an inline `cdifRepresentedVariable` or `@id`-reference to one declared elsewhere in the document, identifying the conceptual variable the code names.

This is the controlled-vocabulary descriptor pattern: strings in the descriptor column map to RepresentedVariables (the conceptual definitions of the variables those codes name). No SKOS Concept indirection.

## Use in DataStructure

A `cdi:VariableDescriptorComponent` (in [cdifDataStructureComponent](../cdifDataStructureComponent/)) holds a `cdi:isDefinedBy` pointer to a `cdifDescriptorVariable` instance, plus a `cdi:refersTo` pointer to the `cdi:VariableValueComponent` whose value-column contents the descriptor identifies.

## Dependencies

- [cdifRepresentedVariable](../cdifRepresentedVariable/) — target of `cdif:isDefinedBy` in each descriptor entry.

## Examples

### Minimal CDIF Descriptor Variable
A bare cdi:DescriptorVariable with a single-entry DescriptorValueDomain mapping
one descriptor code ("temp") to the InstanceVariable it names. Schema requires
only @type and cdif:hasValuesFrom (which itself requires a non-empty
cdif:takesValuesFrom array).
#### json
```json
{
  "@context": {
    "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
    "cdif": "https://cdif.org/0.1/",
    "ex": "https://example.org/"
  },
  "@type": ["cdi:DescriptorVariable"],
  "@id": "ex:dv/measureName",
  "cdif:hasValuesFrom": {
    "@type": ["cdi:DescriptorValueDomain"],
    "cdif:takesValuesFrom": [
      {
        "cdif:value": "temp",
        "cdif:isDefinedBy": { "@id": "ex:rv/temperature" }
      }
    ]
  }
}

```

#### jsonld
```jsonld
{
  "@context": [
    {
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "cdif": "https://cdif.org/0.1/"
    },
    "https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifDataType/cdifDescriptorVariable/context.jsonld",
    {
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "cdif": "https://cdif.org/0.1/",
      "ex": "https://example.org/"
    }
  ],
  "@type": [
    "cdi:DescriptorVariable"
  ],
  "@id": "ex:dv/measureName",
  "cdif:hasValuesFrom": {
    "@type": [
      "cdi:DescriptorValueDomain"
    ],
    "cdif:takesValuesFrom": [
      {
        "cdif:value": "temp",
        "cdif:isDefinedBy": {
          "@id": "ex:rv/temperature"
        }
      }
    ]
  }
}
```

#### ttl
```ttl
@prefix cdi: <http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/> .
@prefix cdif: <https://cdif.org/0.1/> .

<https://example.org/dv/measureName> a cdi:DescriptorVariable ;
    cdif:hasValuesFrom [ a cdi:DescriptorValueDomain ;
            cdif:takesValuesFrom [ cdif:isDefinedBy <https://example.org/rv/temperature> ;
                    cdif:value "temp" ] ] .


```


### Complete CDIF Descriptor Variable
A measure_name descriptor variable with a 4-entry DescriptorValueDomain
enumerating the codes that can appear in the descriptor column of a
long-format vitals table — each code paired (via cdif:isDefinedBy) with the
@id of the InstanceVariable it names. Demonstrates cdi:name (ObjectName
wrapper) and a non-trivial code → variable mapping.
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "xsd": "http://www.w3.org/2001/XMLSchema#",
    "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
    "cdif": "https://cdif.org/0.1/",
    "ex": "https://example.org/"
  },
  "@type": [
    "cdi:DescriptorVariable"
  ],
  "@id": "ex:dv/measureName",
  "cdif:name": [
    "measure_name"
  ],
  "cdif:hasValuesFrom": {
    "@type": [
      "cdi:DescriptorValueDomain"
    ],
    "@id": "ex:vd/measureName",
    "cdif:takesValuesFrom": [
      {
        "cdif:value": "systolic_bp",
        "cdif:isDefinedBy": {
          "@type": [
            "cdi:RepresentedVariable"
          ],
          "@id": "ex:rv/systolicBP",
          "cdif:name": [
            "systolic_blood_pressure"
          ],
          "cdi:simpleUnitOfMeasure": "mmHg",
          "cdi:hasIntendedDataType": {
            "@type": [
              "cdi:ControlledVocabularyEntry"
            ],
            "cdi:entryValue": [
              "xsd:decimal"
            ]
          }
        }
      },
      {
        "cdif:value": "diastolic_bp",
        "cdif:isDefinedBy": {
          "@type": [
            "cdi:RepresentedVariable"
          ],
          "@id": "ex:rv/diastolicBP",
          "cdif:name": [
            "diastolic_blood_pressure"
          ],
          "cdi:simpleUnitOfMeasure": "mmHg",
          "cdi:hasIntendedDataType": {
            "@type": [
              "cdi:ControlledVocabularyEntry"
            ],
            "cdi:entryValue": [
              "xsd:decimal"
            ]
          }
        }
      },
      {
        "cdif:value": "heart_rate",
        "cdif:isDefinedBy": {
          "@id": "ex:rv/heartRate"
        }
      },
      {
        "cdif:value": "temp_c",
        "cdif:isDefinedBy": {
          "@id": "ex:rv/temperatureC"
        }
      }
    ]
  }
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
    "https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifDataType/cdifDescriptorVariable/context.jsonld",
    {
      "schema": "http://schema.org/",
      "xsd": "http://www.w3.org/2001/XMLSchema#",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "cdif": "https://cdif.org/0.1/",
      "ex": "https://example.org/"
    }
  ],
  "@type": [
    "cdi:DescriptorVariable"
  ],
  "@id": "ex:dv/measureName",
  "cdif:name": [
    "measure_name"
  ],
  "cdif:hasValuesFrom": {
    "@type": [
      "cdi:DescriptorValueDomain"
    ],
    "@id": "ex:vd/measureName",
    "cdif:takesValuesFrom": [
      {
        "cdif:value": "systolic_bp",
        "cdif:isDefinedBy": {
          "@type": [
            "cdi:RepresentedVariable"
          ],
          "@id": "ex:rv/systolicBP",
          "cdif:name": [
            "systolic_blood_pressure"
          ],
          "cdi:simpleUnitOfMeasure": "mmHg",
          "cdi:hasIntendedDataType": {
            "@type": [
              "cdi:ControlledVocabularyEntry"
            ],
            "cdi:entryValue": [
              "xsd:decimal"
            ]
          }
        }
      },
      {
        "cdif:value": "diastolic_bp",
        "cdif:isDefinedBy": {
          "@type": [
            "cdi:RepresentedVariable"
          ],
          "@id": "ex:rv/diastolicBP",
          "cdif:name": [
            "diastolic_blood_pressure"
          ],
          "cdi:simpleUnitOfMeasure": "mmHg",
          "cdi:hasIntendedDataType": {
            "@type": [
              "cdi:ControlledVocabularyEntry"
            ],
            "cdi:entryValue": [
              "xsd:decimal"
            ]
          }
        }
      },
      {
        "cdif:value": "heart_rate",
        "cdif:isDefinedBy": {
          "@id": "ex:rv/heartRate"
        }
      },
      {
        "cdif:value": "temp_c",
        "cdif:isDefinedBy": {
          "@id": "ex:rv/temperatureC"
        }
      }
    ]
  }
}
```

#### ttl
```ttl
@prefix cdi: <http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/> .
@prefix cdif: <https://cdif.org/0.1/> .

<https://example.org/dv/measureName> a cdi:DescriptorVariable ;
    cdif:hasValuesFrom <https://example.org/vd/measureName> ;
    cdif:name "measure_name" .

<https://example.org/rv/diastolicBP> a cdi:RepresentedVariable ;
    cdi:hasIntendedDataType [ a cdi:ControlledVocabularyEntry ;
            cdi:entryValue "xsd:decimal" ] ;
    cdi:simpleUnitOfMeasure "mmHg" ;
    cdif:name "diastolic_blood_pressure" .

<https://example.org/rv/systolicBP> a cdi:RepresentedVariable ;
    cdi:hasIntendedDataType [ a cdi:ControlledVocabularyEntry ;
            cdi:entryValue "xsd:decimal" ] ;
    cdi:simpleUnitOfMeasure "mmHg" ;
    cdif:name "systolic_blood_pressure" .

<https://example.org/vd/measureName> a cdi:DescriptorValueDomain ;
    cdif:takesValuesFrom [ cdif:isDefinedBy <https://example.org/rv/temperatureC> ;
            cdif:value "temp_c" ],
        [ cdif:isDefinedBy <https://example.org/rv/systolicBP> ;
            cdif:value "systolic_bp" ],
        [ cdif:isDefinedBy <https://example.org/rv/diastolicBP> ;
            cdif:value "diastolic_bp" ],
        [ cdif:isDefinedBy <https://example.org/rv/heartRate> ;
            cdif:value "heart_rate" ] .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: DDI-CDI Descriptor Variable
type: object
description: Variable that provides codes for variable identification in the context
  of a data structure. Descriptor Variables hold values which reference the logical
  variables in the data set, indicating which one the associated value in the corresponding
  Reference Variable is a measure/value for. Descriptor Variables are presentational
  variables found only in Long Data Sets.
properties:
  '@type':
    type: array
    items:
      type: string
    contains:
      const: cdi:DescriptorVariable
    minItems: 1
  '@id':
    type: string
    description: Identifier for this DescriptorVariable node
  cdif:hasValuesFrom:
    description: A cdi:DescriptorValueDomain enumerating the codes that can appear
      in the descriptor column, each paired (via cdif:isDefinedBy) with the RepresentedVariable
      that the code names.
    $ref: '#/$defs/DescriptorValueDomain'
    x-jsonld-id: https://cdif.org/0.1/hasValuesFrom
  cdif:name:
    type: array
    items:
      type: string
    minItems: 1
    description: Human understandable name (linguistic signifier, word, phrase, or
      mnemonic). May follow ISO/IEC 11179-5 naming principles, and have context provided
      to specify usage.
    x-jsonld-id: https://cdif.org/0.1/name
required:
- '@type'
- cdif:hasValuesFrom
$defs:
  DescriptorValueDomain:
    type: object
    description: Set of permissible values for a variable playing the role of a variable
      descriptor component. Each entry pairs a code (cdif:value) with the RepresentedVariable
      that the code identifies (cdif:isDefinedBy).
    properties:
      '@type':
        type: array
        items:
          type: string
        contains:
          const: cdi:DescriptorValueDomain
        minItems: 1
      '@id':
        type: string
        description: Identifier for this DescriptorValueDomain node
      cdif:takesValuesFrom:
        type: array
        description: Ordered list of descriptor entries. Each entry has a cdif:value
          (the code as it appears in the descriptor column) and a cdif:isDefinedBy
          pointer to the RepresentedVariable that the code names.
        items:
          type: object
          properties:
            cdif:value:
              type: string
              description: The code value as it appears in the descriptor column.
              x-jsonld-id: https://cdif.org/0.1/value
            cdif:isDefinedBy:
              anyOf:
              - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifDataType/cdifRepresentedVariable/schema.yaml
              - type: object
                description: object reference via URI or URI fragment to a RepresentedVariable
                  defined elsewhere in the document
                properties:
                  '@id':
                    type: string
                required:
                - '@id'
              x-jsonld-id: https://cdif.org/0.1/isDefinedBy
          required:
          - cdif:value
          - cdif:isDefinedBy
        minItems: 1
        x-jsonld-id: https://cdif.org/0.1/takesValuesFrom
    required:
    - '@type'
    - cdif:takesValuesFrom
x-jsonld-prefixes:
  schema: http://schema.org/
  cdi: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/
  cdif: https://cdif.org/0.1/

```

Links to the schema:

* YAML version: [schema.yaml](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifDataType/cdifDescriptorVariable/schema.json)
* JSON version: [schema.json](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifDataType/cdifDescriptorVariable/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "schema": "http://schema.org/",
    "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
    "cdif": "https://cdif.org/0.1/",
    "skos": "http://www.w3.org/2004/02/skos/core#",
    "xsd": "http://www.w3.org/2001/XMLSchema#",
    "dcterms": "http://purl.org/dc/terms/",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifDataType/cdifDescriptorVariable/context.jsonld)

## Sources

* [DDI-CDI 1.0 Specification](https://ddialliance.org/Specification/DDI-CDI/1.0/)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/Cross-Domain-Interoperability-Framework/metadataBuildingBlocks](https://github.com/Cross-Domain-Interoperability-Framework/metadataBuildingBlocks)
* Path: `_sources/cdifDataType/cdifDescriptorVariable`

