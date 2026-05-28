
# CDIF Data Structure (Schema)

`cdif.bbr.metadata.profiles.cdifProfile.cdifDataStructure` *v0.1*

Data organization based on reusable data structure components.

[*Status*](http://www.opengis.net/def/status): Under development

## Examples

### Minimal CDIF Data Structure
A bare cdi:DataStructure root with a single cdi:has_DataStructureComponent
entry, given as an @id-reference to a component declared elsewhere in the
document. The base DataStructure variant imposes no constraints on which
component subclasses are present — useful when the layout doesn't fit the
Dimensional / Long / Wide shapes.
#### json
```json
{
  "@context": {
    "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
    "ex": "https://example.org/"
  },
  "@type": ["cdi:DataStructure"],
  "@id": "ex:struct/observations",
  "cdi:has_DataStructureComponent": [
    { "@id": "ex:component/observationValue" }
  ]
}

```

#### jsonld
```jsonld
{
  "@context": [
    {
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/"
    },
    "https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/profiles/cdifProfile/cdifDataStructure/context.jsonld",
    {
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "ex": "https://example.org/"
    }
  ],
  "@type": [
    "cdi:DataStructure"
  ],
  "@id": "ex:struct/observations",
  "cdi:has_DataStructureComponent": [
    {
      "@id": "ex:component/observationValue"
    }
  ]
}
```

#### ttl
```ttl
@prefix cdi: <http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/> .

<https://example.org/struct/observations> a cdi:DataStructure ;
    cdi:has_DataStructureComponent <https://example.org/component/observationValue> .


```


### Complete CDIF Data Structure (Long)
A cdi:LongDataStructure exercising the array-level cardinality constraint:
exactly one IdentifierComponent (patient id), exactly one
VariableDescriptorComponent (the column naming which vital sign is in each
row), exactly one VariableValueComponent (the value column), plus one
optional AttributeComponent (observation timestamp) that cdi:qualifies the
value column. The cdif:PrimaryKey is given as a flat ordered array of three
@id-references to InstanceVariables — array order is position; no
ComponentPosition wrapper.
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
    "cdif": "https://cdif.org/0.1/",
    "xsd": "http://www.w3.org/2001/XMLSchema#",
    "ex": "https://example.org/"
  },
  "@type": [
    "cdi:LongDataStructure"
  ],
  "@id": "ex:struct/vitalsLong",
  "cdi:has_DataStructureComponent": [
    {
      "@type": [
        "cdi:IdentifierComponent"
      ],
      "@id": "ex:struct/vitalsLong/comp/patientId",
      "cdif:isDefinedBy_RepresentedVariable": {
        "@type": [
          "cdi:RepresentedVariable"
        ],
        "@id": "ex:struct/vitalsLong/rv/patientId",
        "cdif:name": [
          "patient_id"
        ],
        "cdi:hasIntendedDataType": {
          "@type": [
            "cdi:ControlledVocabularyEntry"
          ],
          "cdi:entryValue": [
            "xsd:string"
          ]
        }
      }
    },
    {
      "@type": [
        "cdi:VariableDescriptorComponent"
      ],
      "@id": "ex:struct/vitalsLong/comp/measureName",
      "cdif:isDefinedBy_DescriptorVariable": {
        "@type": [
          "cdi:DescriptorVariable"
        ],
        "@id": "ex:struct/vitalsLong/dv/measureName",
        "cdif:name": [
          "measure_name"
        ],
        "cdif:hasValuesFrom": {
          "@type": [
            "cdi:DescriptorValueDomain"
          ],
          "@id": "ex:struct/vitalsLong/vd/measureName",
          "cdif:takesValuesFrom": [
            {
              "cdif:value": "heart_rate",
              "cdif:isDefinedBy": {
                "@id": "ex:struct/vitalsLong/rv/heartRate"
              }
            },
            {
              "cdif:value": "systolic_bp",
              "cdif:isDefinedBy": {
                "@id": "ex:struct/vitalsLong/rv/systolicBP"
              }
            }
          ]
        }
      },
      "cdi:refersTo": {
        "@id": "ex:struct/vitalsLong/comp/measureValue"
      }
    },
    {
      "@type": [
        "cdi:VariableValueComponent"
      ],
      "@id": "ex:struct/vitalsLong/comp/measureValue",
      "cdif:isDefinedBy_RepresentedVariable": {
        "@type": [
          "cdi:RepresentedVariable"
        ],
        "@id": "ex:struct/vitalsLong/rv/measureValue",
        "cdif:name": [
          "measure_value"
        ],
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
      "@type": [
        "cdi:AttributeComponent"
      ],
      "@id": "ex:struct/vitalsLong/comp/observedAt",
      "cdi:qualifies": [
        {
          "@id": "ex:struct/vitalsLong/comp/measureValue"
        }
      ],
      "cdif:isDefinedBy_RepresentedVariable": {
        "@type": [
          "cdi:RepresentedVariable"
        ],
        "@id": "ex:struct/vitalsLong/rv/observedAt",
        "cdif:name": [
          "observed_at"
        ],
        "cdi:hasIntendedDataType": {
          "@type": [
            "cdi:ControlledVocabularyEntry"
          ],
          "cdi:entryValue": [
            "xsd:dateTime"
          ]
        }
      }
    }
  ],
  "cdi:has_PrimaryKey": {
    "@type": [
      "cdif:PrimaryKey"
    ],
    "@id": "ex:struct/vitalsLong/pk",
    "cdif:isComposedOf": [
      {
        "@id": "ex:var/patientId"
      },
      {
        "@id": "ex:var/measureName"
      },
      {
        "@id": "ex:var/observedAt"
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
    "https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/profiles/cdifProfile/cdifDataStructure/context.jsonld",
    {
      "schema": "http://schema.org/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "cdif": "https://cdif.org/0.1/",
      "xsd": "http://www.w3.org/2001/XMLSchema#",
      "ex": "https://example.org/"
    }
  ],
  "@type": [
    "cdi:LongDataStructure"
  ],
  "@id": "ex:struct/vitalsLong",
  "cdi:has_DataStructureComponent": [
    {
      "@type": [
        "cdi:IdentifierComponent"
      ],
      "@id": "ex:struct/vitalsLong/comp/patientId",
      "cdif:isDefinedBy_RepresentedVariable": {
        "@type": [
          "cdi:RepresentedVariable"
        ],
        "@id": "ex:struct/vitalsLong/rv/patientId",
        "cdif:name": [
          "patient_id"
        ],
        "cdi:hasIntendedDataType": {
          "@type": [
            "cdi:ControlledVocabularyEntry"
          ],
          "cdi:entryValue": [
            "xsd:string"
          ]
        }
      }
    },
    {
      "@type": [
        "cdi:VariableDescriptorComponent"
      ],
      "@id": "ex:struct/vitalsLong/comp/measureName",
      "cdif:isDefinedBy_DescriptorVariable": {
        "@type": [
          "cdi:DescriptorVariable"
        ],
        "@id": "ex:struct/vitalsLong/dv/measureName",
        "cdif:name": [
          "measure_name"
        ],
        "cdif:hasValuesFrom": {
          "@type": [
            "cdi:DescriptorValueDomain"
          ],
          "@id": "ex:struct/vitalsLong/vd/measureName",
          "cdif:takesValuesFrom": [
            {
              "cdif:value": "heart_rate",
              "cdif:isDefinedBy": {
                "@id": "ex:struct/vitalsLong/rv/heartRate"
              }
            },
            {
              "cdif:value": "systolic_bp",
              "cdif:isDefinedBy": {
                "@id": "ex:struct/vitalsLong/rv/systolicBP"
              }
            }
          ]
        }
      },
      "cdi:refersTo": {
        "@id": "ex:struct/vitalsLong/comp/measureValue"
      }
    },
    {
      "@type": [
        "cdi:VariableValueComponent"
      ],
      "@id": "ex:struct/vitalsLong/comp/measureValue",
      "cdif:isDefinedBy_RepresentedVariable": {
        "@type": [
          "cdi:RepresentedVariable"
        ],
        "@id": "ex:struct/vitalsLong/rv/measureValue",
        "cdif:name": [
          "measure_value"
        ],
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
      "@type": [
        "cdi:AttributeComponent"
      ],
      "@id": "ex:struct/vitalsLong/comp/observedAt",
      "cdi:qualifies": [
        {
          "@id": "ex:struct/vitalsLong/comp/measureValue"
        }
      ],
      "cdif:isDefinedBy_RepresentedVariable": {
        "@type": [
          "cdi:RepresentedVariable"
        ],
        "@id": "ex:struct/vitalsLong/rv/observedAt",
        "cdif:name": [
          "observed_at"
        ],
        "cdi:hasIntendedDataType": {
          "@type": [
            "cdi:ControlledVocabularyEntry"
          ],
          "cdi:entryValue": [
            "xsd:dateTime"
          ]
        }
      }
    }
  ],
  "cdi:has_PrimaryKey": {
    "@type": [
      "cdif:PrimaryKey"
    ],
    "@id": "ex:struct/vitalsLong/pk",
    "cdif:isComposedOf": [
      {
        "@id": "ex:var/patientId"
      },
      {
        "@id": "ex:var/measureName"
      },
      {
        "@id": "ex:var/observedAt"
      }
    ]
  }
}
```

#### ttl
```ttl
@prefix cdi: <http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/> .
@prefix cdif: <https://cdif.org/0.1/> .

<https://example.org/struct/vitalsLong> a cdi:LongDataStructure ;
    cdi:has_DataStructureComponent <https://example.org/struct/vitalsLong/comp/measureName>,
        <https://example.org/struct/vitalsLong/comp/measureValue>,
        <https://example.org/struct/vitalsLong/comp/observedAt>,
        <https://example.org/struct/vitalsLong/comp/patientId> ;
    cdi:has_PrimaryKey <https://example.org/struct/vitalsLong/pk> .

<https://example.org/struct/vitalsLong/comp/measureName> a cdi:VariableDescriptorComponent ;
    cdi:refersTo <https://example.org/struct/vitalsLong/comp/measureValue> ;
    cdif:isDefinedBy_DescriptorVariable <https://example.org/struct/vitalsLong/dv/measureName> .

<https://example.org/struct/vitalsLong/comp/observedAt> a cdi:AttributeComponent ;
    cdi:qualifies <https://example.org/struct/vitalsLong/comp/measureValue> ;
    cdif:isDefinedBy_RepresentedVariable <https://example.org/struct/vitalsLong/rv/observedAt> .

<https://example.org/struct/vitalsLong/comp/patientId> a cdi:IdentifierComponent ;
    cdif:isDefinedBy_RepresentedVariable <https://example.org/struct/vitalsLong/rv/patientId> .

<https://example.org/struct/vitalsLong/dv/measureName> a cdi:DescriptorVariable ;
    cdif:hasValuesFrom <https://example.org/struct/vitalsLong/vd/measureName> ;
    cdif:name "measure_name" .

<https://example.org/struct/vitalsLong/pk> a cdif:PrimaryKey ;
    cdif:isComposedOf <https://example.org/var/measureName>,
        <https://example.org/var/observedAt>,
        <https://example.org/var/patientId> .

<https://example.org/struct/vitalsLong/rv/measureValue> a cdi:RepresentedVariable ;
    cdi:hasIntendedDataType [ a cdi:ControlledVocabularyEntry ;
            cdi:entryValue "xsd:decimal" ] ;
    cdif:name "measure_value" .

<https://example.org/struct/vitalsLong/rv/observedAt> a cdi:RepresentedVariable ;
    cdi:hasIntendedDataType [ a cdi:ControlledVocabularyEntry ;
            cdi:entryValue "xsd:dateTime" ] ;
    cdif:name "observed_at" .

<https://example.org/struct/vitalsLong/rv/patientId> a cdi:RepresentedVariable ;
    cdi:hasIntendedDataType [ a cdi:ControlledVocabularyEntry ;
            cdi:entryValue "xsd:string" ] ;
    cdif:name "patient_id" .

<https://example.org/struct/vitalsLong/vd/measureName> a cdi:DescriptorValueDomain ;
    cdif:takesValuesFrom [ cdif:isDefinedBy <https://example.org/struct/vitalsLong/rv/heartRate> ;
            cdif:value "heart_rate" ],
        [ cdif:isDefinedBy <https://example.org/struct/vitalsLong/rv/systolicBP> ;
            cdif:value "systolic_bp" ] .

<https://example.org/struct/vitalsLong/comp/measureValue> a cdi:VariableValueComponent ;
    cdif:isDefinedBy_RepresentedVariable <https://example.org/struct/vitalsLong/rv/measureValue> .


```


### Complete CDIF Data Structure (Dimensional)
A cdi:DimensionalDataStructure describing a sales cube. Three
DimensionComponents form the addressing axes (country, quarter, product
category), one MeasureComponent holds the sales amount, and one
AttributeComponent (currency) qualifies the measure. The cdif:PrimaryKey
composes the three dimension variables — together they uniquely address
each cell in the cube.
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
    "cdif": "https://cdif.org/0.1/",
    "xsd": "http://www.w3.org/2001/XMLSchema#",
    "ex": "https://example.org/",
    "skos": "http://www.w3.org/2004/02/skos/core#"
  },
  "@type": [
    "cdi:DimensionalDataStructure"
  ],
  "@id": "ex:struct/salesCube",
  "cdi:has_DataStructureComponent": [
    {
      "@type": [
        "cdi:DimensionComponent"
      ],
      "@id": "ex:struct/salesCube/comp/country",
      "cdif:isDefinedBy_RepresentedVariable": {
        "@type": [
          "cdi:RepresentedVariable"
        ],
        "@id": "ex:struct/salesCube/rv/country",
        "cdif:name": [
          "country"
        ],
        "cdi:hasIntendedDataType": {
          "@type": [
            "cdi:ControlledVocabularyEntry"
          ],
          "cdi:entryValue": [
            "xsd:string"
          ]
        }
      }
    },
    {
      "@type": [
        "cdi:DimensionComponent"
      ],
      "@id": "ex:struct/salesCube/comp/quarter",
      "cdif:isDefinedBy_RepresentedVariable": {
        "@type": [
          "cdi:RepresentedVariable"
        ],
        "@id": "ex:struct/salesCube/rv/quarter",
        "cdif:name": [
          "quarter"
        ],
        "cdi:hasIntendedDataType": {
          "@type": [
            "cdi:ControlledVocabularyEntry"
          ],
          "cdi:entryValue": [
            "xsd:gYearMonth"
          ]
        }
      }
    },
    {
      "@type": [
        "cdi:DimensionComponent"
      ],
      "@id": "ex:struct/salesCube/comp/productCategory",
      "cdif:isDefinedBy_RepresentedVariable": {
        "@type": [
          "cdi:RepresentedVariable"
        ],
        "@id": "ex:struct/salesCube/rv/productCategory",
        "cdif:name": [
          "product_category"
        ],
        "cdi:hasIntendedDataType": {
          "@type": [
            "cdi:ControlledVocabularyEntry"
          ],
          "cdi:entryValue": [
            "xsd:string"
          ]
        }
      }
    },
    {
      "@type": [
        "cdi:MeasureComponent"
      ],
      "@id": "ex:struct/salesCube/comp/salesAmount",
      "cdif:isDefinedBy_RepresentedVariable": {
        "@type": [
          "cdi:RepresentedVariable"
        ],
        "@id": "ex:struct/salesCube/rv/salesAmount",
        "cdif:name": [
          "sales_amount"
        ],
        "cdi:simpleUnitOfMeasure": "USD",
        "cdi:hasIntendedDataType": {
          "@type": [
            "cdi:ControlledVocabularyEntry"
          ],
          "cdi:entryValue": [
            "xsd:decimal"
          ]
        }
      },
      "cdi:semantic": [
        {
          "@type": [
            "skos:Concept"
          ],
          "skos:prefLabel": "Monetary Total",
          "skos:definition": "Total monetary value of sales.",
          "skos:notation": [
            "monetary-total"
          ],
          "skos:inScheme": {
            "@id": "https://example.org/vocab/measure"
          }
        }
      ]
    },
    {
      "@type": [
        "cdi:AttributeComponent"
      ],
      "@id": "ex:struct/salesCube/comp/currency",
      "cdi:qualifies": [
        {
          "@id": "ex:struct/salesCube/comp/salesAmount"
        }
      ],
      "cdif:isDefinedBy_RepresentedVariable": {
        "@type": [
          "cdi:RepresentedVariable"
        ],
        "@id": "ex:struct/salesCube/rv/currency",
        "cdif:name": [
          "currency"
        ],
        "cdi:hasIntendedDataType": {
          "@type": [
            "cdi:ControlledVocabularyEntry"
          ],
          "cdi:entryValue": [
            "xsd:string"
          ]
        }
      }
    }
  ],
  "cdi:has_PrimaryKey": {
    "@type": [
      "cdif:PrimaryKey"
    ],
    "@id": "ex:struct/salesCube/pk",
    "cdif:isComposedOf": [
      {
        "@id": "ex:var/country"
      },
      {
        "@id": "ex:var/quarter"
      },
      {
        "@id": "ex:var/productCategory"
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
    "https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/profiles/cdifProfile/cdifDataStructure/context.jsonld",
    {
      "schema": "http://schema.org/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "cdif": "https://cdif.org/0.1/",
      "xsd": "http://www.w3.org/2001/XMLSchema#",
      "ex": "https://example.org/",
      "skos": "http://www.w3.org/2004/02/skos/core#"
    }
  ],
  "@type": [
    "cdi:DimensionalDataStructure"
  ],
  "@id": "ex:struct/salesCube",
  "cdi:has_DataStructureComponent": [
    {
      "@type": [
        "cdi:DimensionComponent"
      ],
      "@id": "ex:struct/salesCube/comp/country",
      "cdif:isDefinedBy_RepresentedVariable": {
        "@type": [
          "cdi:RepresentedVariable"
        ],
        "@id": "ex:struct/salesCube/rv/country",
        "cdif:name": [
          "country"
        ],
        "cdi:hasIntendedDataType": {
          "@type": [
            "cdi:ControlledVocabularyEntry"
          ],
          "cdi:entryValue": [
            "xsd:string"
          ]
        }
      }
    },
    {
      "@type": [
        "cdi:DimensionComponent"
      ],
      "@id": "ex:struct/salesCube/comp/quarter",
      "cdif:isDefinedBy_RepresentedVariable": {
        "@type": [
          "cdi:RepresentedVariable"
        ],
        "@id": "ex:struct/salesCube/rv/quarter",
        "cdif:name": [
          "quarter"
        ],
        "cdi:hasIntendedDataType": {
          "@type": [
            "cdi:ControlledVocabularyEntry"
          ],
          "cdi:entryValue": [
            "xsd:gYearMonth"
          ]
        }
      }
    },
    {
      "@type": [
        "cdi:DimensionComponent"
      ],
      "@id": "ex:struct/salesCube/comp/productCategory",
      "cdif:isDefinedBy_RepresentedVariable": {
        "@type": [
          "cdi:RepresentedVariable"
        ],
        "@id": "ex:struct/salesCube/rv/productCategory",
        "cdif:name": [
          "product_category"
        ],
        "cdi:hasIntendedDataType": {
          "@type": [
            "cdi:ControlledVocabularyEntry"
          ],
          "cdi:entryValue": [
            "xsd:string"
          ]
        }
      }
    },
    {
      "@type": [
        "cdi:MeasureComponent"
      ],
      "@id": "ex:struct/salesCube/comp/salesAmount",
      "cdif:isDefinedBy_RepresentedVariable": {
        "@type": [
          "cdi:RepresentedVariable"
        ],
        "@id": "ex:struct/salesCube/rv/salesAmount",
        "cdif:name": [
          "sales_amount"
        ],
        "cdi:simpleUnitOfMeasure": "USD",
        "cdi:hasIntendedDataType": {
          "@type": [
            "cdi:ControlledVocabularyEntry"
          ],
          "cdi:entryValue": [
            "xsd:decimal"
          ]
        }
      },
      "cdi:semantic": [
        {
          "@type": [
            "skos:Concept"
          ],
          "skos:prefLabel": "Monetary Total",
          "skos:definition": "Total monetary value of sales.",
          "skos:notation": [
            "monetary-total"
          ],
          "skos:inScheme": {
            "@id": "https://example.org/vocab/measure"
          }
        }
      ]
    },
    {
      "@type": [
        "cdi:AttributeComponent"
      ],
      "@id": "ex:struct/salesCube/comp/currency",
      "cdi:qualifies": [
        {
          "@id": "ex:struct/salesCube/comp/salesAmount"
        }
      ],
      "cdif:isDefinedBy_RepresentedVariable": {
        "@type": [
          "cdi:RepresentedVariable"
        ],
        "@id": "ex:struct/salesCube/rv/currency",
        "cdif:name": [
          "currency"
        ],
        "cdi:hasIntendedDataType": {
          "@type": [
            "cdi:ControlledVocabularyEntry"
          ],
          "cdi:entryValue": [
            "xsd:string"
          ]
        }
      }
    }
  ],
  "cdi:has_PrimaryKey": {
    "@type": [
      "cdif:PrimaryKey"
    ],
    "@id": "ex:struct/salesCube/pk",
    "cdif:isComposedOf": [
      {
        "@id": "ex:var/country"
      },
      {
        "@id": "ex:var/quarter"
      },
      {
        "@id": "ex:var/productCategory"
      }
    ]
  }
}
```

#### ttl
```ttl
@prefix cdi: <http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/> .
@prefix cdif: <https://cdif.org/0.1/> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .

<https://example.org/struct/salesCube> a cdi:DimensionalDataStructure ;
    cdi:has_DataStructureComponent <https://example.org/struct/salesCube/comp/country>,
        <https://example.org/struct/salesCube/comp/currency>,
        <https://example.org/struct/salesCube/comp/productCategory>,
        <https://example.org/struct/salesCube/comp/quarter>,
        <https://example.org/struct/salesCube/comp/salesAmount> ;
    cdi:has_PrimaryKey <https://example.org/struct/salesCube/pk> .

<https://example.org/struct/salesCube/comp/country> a cdi:DimensionComponent ;
    cdif:isDefinedBy_RepresentedVariable <https://example.org/struct/salesCube/rv/country> .

<https://example.org/struct/salesCube/comp/currency> a cdi:AttributeComponent ;
    cdi:qualifies <https://example.org/struct/salesCube/comp/salesAmount> ;
    cdif:isDefinedBy_RepresentedVariable <https://example.org/struct/salesCube/rv/currency> .

<https://example.org/struct/salesCube/comp/productCategory> a cdi:DimensionComponent ;
    cdif:isDefinedBy_RepresentedVariable <https://example.org/struct/salesCube/rv/productCategory> .

<https://example.org/struct/salesCube/comp/quarter> a cdi:DimensionComponent ;
    cdif:isDefinedBy_RepresentedVariable <https://example.org/struct/salesCube/rv/quarter> .

<https://example.org/struct/salesCube/pk> a cdif:PrimaryKey ;
    cdif:isComposedOf <https://example.org/var/country>,
        <https://example.org/var/productCategory>,
        <https://example.org/var/quarter> .

<https://example.org/struct/salesCube/rv/country> a cdi:RepresentedVariable ;
    cdi:hasIntendedDataType [ a cdi:ControlledVocabularyEntry ;
            cdi:entryValue "xsd:string" ] ;
    cdif:name "country" .

<https://example.org/struct/salesCube/rv/currency> a cdi:RepresentedVariable ;
    cdi:hasIntendedDataType [ a cdi:ControlledVocabularyEntry ;
            cdi:entryValue "xsd:string" ] ;
    cdif:name "currency" .

<https://example.org/struct/salesCube/rv/productCategory> a cdi:RepresentedVariable ;
    cdi:hasIntendedDataType [ a cdi:ControlledVocabularyEntry ;
            cdi:entryValue "xsd:string" ] ;
    cdif:name "product_category" .

<https://example.org/struct/salesCube/rv/quarter> a cdi:RepresentedVariable ;
    cdi:hasIntendedDataType [ a cdi:ControlledVocabularyEntry ;
            cdi:entryValue "xsd:gYearMonth" ] ;
    cdif:name "quarter" .

<https://example.org/struct/salesCube/rv/salesAmount> a cdi:RepresentedVariable ;
    cdi:hasIntendedDataType [ a cdi:ControlledVocabularyEntry ;
            cdi:entryValue "xsd:decimal" ] ;
    cdi:simpleUnitOfMeasure "USD" ;
    cdif:name "sales_amount" .

<https://example.org/struct/salesCube/comp/salesAmount> a cdi:MeasureComponent ;
    cdi:semantic [ a skos:Concept ;
            skos:definition "Total monetary value of sales." ;
            skos:inScheme <https://example.org/vocab/measure> ;
            skos:notation "monetary-total" ;
            skos:prefLabel "Monetary Total" ] ;
    cdif:isDefinedBy_RepresentedVariable <https://example.org/struct/salesCube/rv/salesAmount> .


```


### Complete CDIF Data Structure (Wide)
A cdi:WideDataStructure for a patient-vitals wide table: one
IdentifierComponent (patientId) identifies the row, three
MeasureComponents hold systolic BP, diastolic BP, and heart rate as
separate columns, and one AttributeComponent (observedAt) attaches the
measurement time to the row. The cdif:PrimaryKey is a single-element
array — wide-format rows are uniquely identified by patientId alone.
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
    "cdif": "https://cdif.org/0.1/",
    "xsd": "http://www.w3.org/2001/XMLSchema#",
    "ex": "https://example.org/"
  },
  "@type": [
    "cdi:WideDataStructure"
  ],
  "@id": "ex:struct/vitalsWide",
  "cdi:has_DataStructureComponent": [
    {
      "@type": [
        "cdi:IdentifierComponent"
      ],
      "@id": "ex:struct/vitalsWide/comp/patientId",
      "cdif:isDefinedBy_RepresentedVariable": {
        "@type": [
          "cdi:RepresentedVariable"
        ],
        "@id": "ex:struct/vitalsWide/rv/patientId",
        "cdif:name": [
          "patient_id"
        ],
        "cdi:hasIntendedDataType": {
          "@type": [
            "cdi:ControlledVocabularyEntry"
          ],
          "cdi:entryValue": [
            "xsd:string"
          ]
        }
      }
    },
    {
      "@type": [
        "cdi:MeasureComponent"
      ],
      "@id": "ex:struct/vitalsWide/comp/systolicBP",
      "cdif:isDefinedBy_RepresentedVariable": {
        "@type": [
          "cdi:RepresentedVariable"
        ],
        "@id": "ex:struct/vitalsWide/rv/systolicBP",
        "cdif:name": [
          "systolic_bp"
        ],
        "cdi:simpleUnitOfMeasure": "mmHg",
        "cdi:hasIntendedDataType": {
          "@type": [
            "cdi:ControlledVocabularyEntry"
          ],
          "cdi:entryValue": [
            "xsd:integer"
          ]
        }
      }
    },
    {
      "@type": [
        "cdi:MeasureComponent"
      ],
      "@id": "ex:struct/vitalsWide/comp/diastolicBP",
      "cdif:isDefinedBy_RepresentedVariable": {
        "@type": [
          "cdi:RepresentedVariable"
        ],
        "@id": "ex:struct/vitalsWide/rv/diastolicBP",
        "cdif:name": [
          "diastolic_bp"
        ],
        "cdi:simpleUnitOfMeasure": "mmHg",
        "cdi:hasIntendedDataType": {
          "@type": [
            "cdi:ControlledVocabularyEntry"
          ],
          "cdi:entryValue": [
            "xsd:integer"
          ]
        }
      }
    },
    {
      "@type": [
        "cdi:MeasureComponent"
      ],
      "@id": "ex:struct/vitalsWide/comp/heartRate",
      "cdif:isDefinedBy_RepresentedVariable": {
        "@type": [
          "cdi:RepresentedVariable"
        ],
        "@id": "ex:struct/vitalsWide/rv/heartRate",
        "cdif:name": [
          "heart_rate"
        ],
        "cdi:simpleUnitOfMeasure": "bpm",
        "cdi:hasIntendedDataType": {
          "@type": [
            "cdi:ControlledVocabularyEntry"
          ],
          "cdi:entryValue": [
            "xsd:integer"
          ]
        }
      }
    },
    {
      "@type": [
        "cdi:AttributeComponent"
      ],
      "@id": "ex:struct/vitalsWide/comp/observedAt",
      "cdif:isDefinedBy_RepresentedVariable": {
        "@type": [
          "cdi:RepresentedVariable"
        ],
        "@id": "ex:struct/vitalsWide/rv/observedAt",
        "cdif:name": [
          "observed_at"
        ],
        "cdi:hasIntendedDataType": {
          "@type": [
            "cdi:ControlledVocabularyEntry"
          ],
          "cdi:entryValue": [
            "xsd:dateTime"
          ]
        }
      }
    }
  ],
  "cdi:has_PrimaryKey": {
    "@type": [
      "cdif:PrimaryKey"
    ],
    "@id": "ex:struct/vitalsWide/pk",
    "cdif:isComposedOf": [
      {
        "@id": "ex:var/patientId"
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
    "https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/profiles/cdifProfile/cdifDataStructure/context.jsonld",
    {
      "schema": "http://schema.org/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "cdif": "https://cdif.org/0.1/",
      "xsd": "http://www.w3.org/2001/XMLSchema#",
      "ex": "https://example.org/"
    }
  ],
  "@type": [
    "cdi:WideDataStructure"
  ],
  "@id": "ex:struct/vitalsWide",
  "cdi:has_DataStructureComponent": [
    {
      "@type": [
        "cdi:IdentifierComponent"
      ],
      "@id": "ex:struct/vitalsWide/comp/patientId",
      "cdif:isDefinedBy_RepresentedVariable": {
        "@type": [
          "cdi:RepresentedVariable"
        ],
        "@id": "ex:struct/vitalsWide/rv/patientId",
        "cdif:name": [
          "patient_id"
        ],
        "cdi:hasIntendedDataType": {
          "@type": [
            "cdi:ControlledVocabularyEntry"
          ],
          "cdi:entryValue": [
            "xsd:string"
          ]
        }
      }
    },
    {
      "@type": [
        "cdi:MeasureComponent"
      ],
      "@id": "ex:struct/vitalsWide/comp/systolicBP",
      "cdif:isDefinedBy_RepresentedVariable": {
        "@type": [
          "cdi:RepresentedVariable"
        ],
        "@id": "ex:struct/vitalsWide/rv/systolicBP",
        "cdif:name": [
          "systolic_bp"
        ],
        "cdi:simpleUnitOfMeasure": "mmHg",
        "cdi:hasIntendedDataType": {
          "@type": [
            "cdi:ControlledVocabularyEntry"
          ],
          "cdi:entryValue": [
            "xsd:integer"
          ]
        }
      }
    },
    {
      "@type": [
        "cdi:MeasureComponent"
      ],
      "@id": "ex:struct/vitalsWide/comp/diastolicBP",
      "cdif:isDefinedBy_RepresentedVariable": {
        "@type": [
          "cdi:RepresentedVariable"
        ],
        "@id": "ex:struct/vitalsWide/rv/diastolicBP",
        "cdif:name": [
          "diastolic_bp"
        ],
        "cdi:simpleUnitOfMeasure": "mmHg",
        "cdi:hasIntendedDataType": {
          "@type": [
            "cdi:ControlledVocabularyEntry"
          ],
          "cdi:entryValue": [
            "xsd:integer"
          ]
        }
      }
    },
    {
      "@type": [
        "cdi:MeasureComponent"
      ],
      "@id": "ex:struct/vitalsWide/comp/heartRate",
      "cdif:isDefinedBy_RepresentedVariable": {
        "@type": [
          "cdi:RepresentedVariable"
        ],
        "@id": "ex:struct/vitalsWide/rv/heartRate",
        "cdif:name": [
          "heart_rate"
        ],
        "cdi:simpleUnitOfMeasure": "bpm",
        "cdi:hasIntendedDataType": {
          "@type": [
            "cdi:ControlledVocabularyEntry"
          ],
          "cdi:entryValue": [
            "xsd:integer"
          ]
        }
      }
    },
    {
      "@type": [
        "cdi:AttributeComponent"
      ],
      "@id": "ex:struct/vitalsWide/comp/observedAt",
      "cdif:isDefinedBy_RepresentedVariable": {
        "@type": [
          "cdi:RepresentedVariable"
        ],
        "@id": "ex:struct/vitalsWide/rv/observedAt",
        "cdif:name": [
          "observed_at"
        ],
        "cdi:hasIntendedDataType": {
          "@type": [
            "cdi:ControlledVocabularyEntry"
          ],
          "cdi:entryValue": [
            "xsd:dateTime"
          ]
        }
      }
    }
  ],
  "cdi:has_PrimaryKey": {
    "@type": [
      "cdif:PrimaryKey"
    ],
    "@id": "ex:struct/vitalsWide/pk",
    "cdif:isComposedOf": [
      {
        "@id": "ex:var/patientId"
      }
    ]
  }
}
```

#### ttl
```ttl
@prefix cdi: <http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/> .
@prefix cdif: <https://cdif.org/0.1/> .

<https://example.org/struct/vitalsWide> a cdi:WideDataStructure ;
    cdi:has_DataStructureComponent <https://example.org/struct/vitalsWide/comp/diastolicBP>,
        <https://example.org/struct/vitalsWide/comp/heartRate>,
        <https://example.org/struct/vitalsWide/comp/observedAt>,
        <https://example.org/struct/vitalsWide/comp/patientId>,
        <https://example.org/struct/vitalsWide/comp/systolicBP> ;
    cdi:has_PrimaryKey <https://example.org/struct/vitalsWide/pk> .

<https://example.org/struct/vitalsWide/comp/diastolicBP> a cdi:MeasureComponent ;
    cdif:isDefinedBy_RepresentedVariable <https://example.org/struct/vitalsWide/rv/diastolicBP> .

<https://example.org/struct/vitalsWide/comp/heartRate> a cdi:MeasureComponent ;
    cdif:isDefinedBy_RepresentedVariable <https://example.org/struct/vitalsWide/rv/heartRate> .

<https://example.org/struct/vitalsWide/comp/observedAt> a cdi:AttributeComponent ;
    cdif:isDefinedBy_RepresentedVariable <https://example.org/struct/vitalsWide/rv/observedAt> .

<https://example.org/struct/vitalsWide/comp/patientId> a cdi:IdentifierComponent ;
    cdif:isDefinedBy_RepresentedVariable <https://example.org/struct/vitalsWide/rv/patientId> .

<https://example.org/struct/vitalsWide/comp/systolicBP> a cdi:MeasureComponent ;
    cdif:isDefinedBy_RepresentedVariable <https://example.org/struct/vitalsWide/rv/systolicBP> .

<https://example.org/struct/vitalsWide/pk> a cdif:PrimaryKey ;
    cdif:isComposedOf <https://example.org/var/patientId> .

<https://example.org/struct/vitalsWide/rv/diastolicBP> a cdi:RepresentedVariable ;
    cdi:hasIntendedDataType [ a cdi:ControlledVocabularyEntry ;
            cdi:entryValue "xsd:integer" ] ;
    cdi:simpleUnitOfMeasure "mmHg" ;
    cdif:name "diastolic_bp" .

<https://example.org/struct/vitalsWide/rv/heartRate> a cdi:RepresentedVariable ;
    cdi:hasIntendedDataType [ a cdi:ControlledVocabularyEntry ;
            cdi:entryValue "xsd:integer" ] ;
    cdi:simpleUnitOfMeasure "bpm" ;
    cdif:name "heart_rate" .

<https://example.org/struct/vitalsWide/rv/observedAt> a cdi:RepresentedVariable ;
    cdi:hasIntendedDataType [ a cdi:ControlledVocabularyEntry ;
            cdi:entryValue "xsd:dateTime" ] ;
    cdif:name "observed_at" .

<https://example.org/struct/vitalsWide/rv/patientId> a cdi:RepresentedVariable ;
    cdi:hasIntendedDataType [ a cdi:ControlledVocabularyEntry ;
            cdi:entryValue "xsd:string" ] ;
    cdif:name "patient_id" .

<https://example.org/struct/vitalsWide/rv/systolicBP> a cdi:RepresentedVariable ;
    cdi:hasIntendedDataType [ a cdi:ControlledVocabularyEntry ;
            cdi:entryValue "xsd:integer" ] ;
    cdi:simpleUnitOfMeasure "mmHg" ;
    cdif:name "systolic_bp" .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: DDI-CDI Data Structure
description: Adds data-structure description to a CDIF metadata record. Defines the
  cdi:DataStructure family of types ($defs DataStructure / DimensionalDataStructure
  / LongDataStructure / WideDataStructure, plus the supporting Component / Key / RepresentedVariable
  types). A distribution attaches a structure via cdi:isStructuredBy on its schema:DataDownload
  item; the structure value is any of the four DataStructure variants. Metadata records
  must declare conformance to cdif/data_structure/1.0.
type: object
properties:
  schema:subjectOf:
    properties:
      dcterms:conformsTo:
        contains:
          type: object
          properties:
            '@id':
              const: https://w3id.org/cdif/data_structure/1.0
  schema:distribution:
    type: array
    items:
      type: object
      properties:
        cdi:isStructuredBy:
          description: Reusable data-structure description for this distribution.
            One of the four DataStructure variants (DataStructure, Dimensional, Long,
            Wide), or an @id reference to one declared elsewhere in the document.
          anyOf:
          - $ref: '#/$defs/DataStructure'
          - $ref: '#/$defs/DimensionalDataStructure'
          - $ref: '#/$defs/LongDataStructure'
          - $ref: '#/$defs/WideDataStructure'
          - $ref: '#/$defs/id-reference'
          x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/isStructuredBy
$defs:
  id-reference:
    type: object
    description: Reference to a node defined elsewhere in the document via its @id.
    properties:
      '@id':
        type: string
    required:
    - '@id'
  DataStructure:
    type: object
    description: Data organization based on reusable data structure components.
    properties:
      '@type':
        type: array
        items:
          type: string
        contains:
          const: cdi:DataStructure
        minItems: 1
      '@id':
        type: string
        description: Identifier for this DataStructure node
      cdi:has_ForeignKey:
        type: array
        items:
          anyOf:
          - $ref: '#/$defs/ForeignKey'
          - $ref: '#/$defs/id-reference'
        minItems: 1
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/has_ForeignKey
      cdi:has_DataStructureComponent:
        type: array
        items:
          anyOf:
          - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifDataType/cdifDataStructureComponent/schema.yaml
          - $ref: '#/$defs/id-reference'
        minItems: 1
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/has_DataStructureComponent
      cdi:has_PrimaryKey:
        $ref: '#/$defs/PrimaryKey'
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/has_PrimaryKey
    required:
    - '@type'
    - cdi:has_DataStructureComponent
  DimensionalDataStructure:
    type: object
    description: Structure of a dimensional data set (organized collection of multidimensional
      data). It is described by dimension, measure and attribute components.
    properties:
      '@type':
        type: array
        items:
          type: string
        contains:
          const: cdi:DimensionalDataStructure
        minItems: 1
      '@id':
        type: string
        description: Identifier for this DimensionalDataStructure node
      cdi:has_DataStructureComponent:
        type: array
        items:
          anyOf:
          - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifDataType/cdifDataStructureComponent/schema.yaml#/$defs/IdentifierComponent
          - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifDataType/cdifDataStructureComponent/schema.yaml#/$defs/MeasureComponent
          - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifDataType/cdifDataStructureComponent/schema.yaml#/$defs/AttributeComponent
          - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifDataType/cdifDataStructureComponent/schema.yaml#/$defs/DimensionComponent
        minItems: 1
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/has_DataStructureComponent
      cdi:has_PrimaryKey:
        $ref: '#/$defs/PrimaryKey'
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/has_PrimaryKey
      cdi:has_ForeignKey:
        type: array
        items:
          anyOf:
          - $ref: '#/$defs/ForeignKey'
          - $ref: '#/$defs/id-reference'
        minItems: 1
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/has_ForeignKey
    required:
    - '@type'
    - cdi:has_DataStructureComponent
  LongDataStructure:
    type: object
    description: Structure of a long dataset (organized collection of long data).
      It is described by identifier, measure, attribute, variable descriptor and variable
      value components.
    properties:
      '@type':
        type: array
        items:
          type: string
        contains:
          const: cdi:LongDataStructure
        minItems: 1
      '@id':
        type: string
        description: Identifier for this LongDataStructure node
      cdi:has_DataStructureComponent:
        type: array
        description: A LongDataStructure must include exactly one IdentifierComponent,
          exactly one VariableDescriptorComponent, exactly one VariableValueComponent,
          plus zero or more AttributeComponents.
        items:
          anyOf:
          - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifDataType/cdifDataStructureComponent/schema.yaml#/$defs/IdentifierComponent
          - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifDataType/cdifDataStructureComponent/schema.yaml#/$defs/VariableDescriptorComponent
          - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifDataType/cdifDataStructureComponent/schema.yaml#/$defs/VariableValueComponent
          - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifDataType/cdifDataStructureComponent/schema.yaml#/$defs/AttributeComponent
        allOf:
        - contains:
            $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifDataType/cdifDataStructureComponent/schema.yaml#/$defs/IdentifierComponent
          minContains: 1
          maxContains: 1
        - contains:
            $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifDataType/cdifDataStructureComponent/schema.yaml#/$defs/VariableDescriptorComponent
          minContains: 1
          maxContains: 1
        - contains:
            $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifDataType/cdifDataStructureComponent/schema.yaml#/$defs/VariableValueComponent
          minContains: 1
          maxContains: 1
        minItems: 3
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/has_DataStructureComponent
      cdi:has_PrimaryKey:
        $ref: '#/$defs/PrimaryKey'
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/has_PrimaryKey
    required:
    - '@type'
    - cdi:has_DataStructureComponent
  WideDataStructure:
    type: object
    description: Structure of a wide dataset (organized collection of wide data).
      It is described by identifier, measure and attribute components.
    properties:
      '@type':
        type: array
        items:
          type: string
        contains:
          const: cdi:WideDataStructure
        minItems: 1
      '@id':
        type: string
        description: Identifier for this WideDataStructure node
      cdi:has_DataStructureComponent:
        type: array
        items:
          anyOf:
          - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifDataType/cdifDataStructureComponent/schema.yaml#/$defs/IdentifierComponent
          - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifDataType/cdifDataStructureComponent/schema.yaml#/$defs/MeasureComponent
          - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifDataType/cdifDataStructureComponent/schema.yaml#/$defs/AttributeComponent
          - $ref: '#/$defs/id-reference'
        minItems: 1
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/has_DataStructureComponent
      cdi:has_PrimaryKey:
        $ref: '#/$defs/PrimaryKey'
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/has_PrimaryKey
      cdi:has_ForeignKey:
        type: array
        items:
          anyOf:
          - $ref: '#/$defs/ForeignKey'
          - $ref: '#/$defs/id-reference'
        minItems: 1
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/has_ForeignKey
    required:
    - '@type'
    - cdi:has_DataStructureComponent
  DimensionGroup:
    type: object
    description: Collection of dimensions that can be reused across multiple dimensional
      structures.
    properties:
      '@type':
        type: array
        items:
          type: string
        contains:
          const: cdi:DimensionGroup
        minItems: 1
      '@id':
        type: string
        description: Identifier for this DimensionGroup node
      cdi:identifier:
        $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/identifier/schema.yaml
        description: Identifier for objects requiring short- or long-lasting referencing
          and management.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/identifier
      cdif:name:
        type: array
        items:
          type: string
        minItems: 1
        description: Human understandable name (liguistic signifier, word, phrase,
          or mnemonic). May follow ISO/IEC 11179-5 naming principles, and have context
          provided to specify usage.
      cdif:has_DataStructureComponent:
        type: array
        items:
          anyOf:
          - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifDataType/cdifDataStructureComponent/schema.yaml
          - $ref: '#/$defs/id-reference'
        minItems: 1
    required:
    - '@type'
  ForeignKey:
    type: object
    description: Role of a set of data structure components for content referencing
      purposes
    properties:
      '@type':
        type: array
        items:
          type: string
        contains:
          const: cdi:ForeignKey
        minItems: 1
      '@id':
        type: string
        description: Identifier for this ForeignKey node
      cdi:identifier:
        $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/identifier/schema.yaml
        description: Identifier for objects requiring short- or long-lasting referencing
          and management.
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/identifier
      cdi:isComposedOf:
        type: array
        items:
          allOf:
          - anyOf:
            - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifDataType/cdifRepresentedVariable/schema.yaml
            - $ref: '#/$defs/id-reference'
          - type: object
            properties:
              cdif:position:
                type: integer
                minimum: 1
                description: 1-based position of this component in the key.
            required:
            - cdif:position
        minItems: 1
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/isComposedOf
      cdi:references:
        description: references a primary key in a different dataset
        anyOf:
        - $ref: '#/$defs/PrimaryKey'
        - $ref: '#/$defs/id-reference'
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/references
    required:
    - '@type'
    - cdif:isComposedOf
  PrimaryKey:
    type: object
    description: set of Variables that uniquely identify a data instance. Array order
      of cdif:isComposedOf items is the position; no intermediate ComponentPosition
      wrapper.
    properties:
      '@type':
        type: array
        items:
          type: string
        contains:
          const: cdif:PrimaryKey
        minItems: 1
      '@id':
        type: string
        description: Identifier for this PrimaryKey node
      cdif:isComposedOf:
        type: array
        description: List of variables or @id-reference. Array order of cdif:isComposedOf
          items is the position; no intermediate ComponentPosition wrapper.
        items:
          allOf:
          - anyOf:
            - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifDataType/cdifRepresentedVariable/schema.yaml
            - $ref: '#/$defs/id-reference'
          - type: object
            properties:
              cdif:position:
                type: integer
                minimum: 1
                description: 1-based position of this component in the key.
        required:
        - cdif:position
        minItems: 1
    required:
    - '@type'
    - cdif:isComposedOf
x-jsonld-prefixes:
  cdi: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/

```

Links to the schema:

* YAML version: [schema.yaml](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/profiles/cdifProfile/cdifDataStructure/schema.json)
* JSON version: [schema.json](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/profiles/cdifProfile/cdifDataStructure/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
    "schema": "http://schema.org/",
    "skos": "http://www.w3.org/2004/02/skos/core#",
    "cdif": "https://cdif.org/0.1/",
    "xsd": "http://www.w3.org/2001/XMLSchema#",
    "dcterms": "http://purl.org/dc/terms/",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/profiles/cdifProfile/cdifDataStructure/context.jsonld)

## Sources

* [DDI-CDI 1.0 Specification](https://ddialliance.org/Specification/DDI-CDI/1.0/)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/Cross-Domain-Interoperability-Framework/metadataBuildingBlocks](https://github.com/Cross-Domain-Interoperability-Framework/metadataBuildingBlocks)
* Path: `_sources/profiles/cdifProfile/cdifDataStructure`

