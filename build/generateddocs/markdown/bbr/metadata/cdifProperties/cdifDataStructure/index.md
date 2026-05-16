
# CDIF Data Structure (Schema)

`cdif.bbr.metadata.cdifProperties.cdifDataStructure` *v0.1*

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
    "https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifProperties/cdifDataStructure/context.jsonld",
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
  "@type": ["cdi:LongDataStructure"],
  "@id": "ex:struct/vitalsLong",
  "cdi:has_DataStructureComponent": [
    {
      "@type": ["cdi:IdentifierComponent"],
      "@id": "ex:struct/vitalsLong/comp/patientId",
      "cdif:isDefinedBy_RepresentedVariable": {
        "@type": ["cdi:RepresentedVariable"],
        "@id": "ex:struct/vitalsLong/rv/patientId",
        "cdi:name": [
          { "@type": ["cdi:ObjectName"], "cdi:name": "patient_id" }
        ],
        "cdi:hasIntendedDataType": {
          "@type": ["cdi:ControlledVocabularyEntry"],
          "cdi:entryValue": ["xsd:string"]
        }
      }
    },
    {
      "@type": ["cdi:VariableDescriptorComponent"],
      "@id": "ex:struct/vitalsLong/comp/measureName",
      "cdif:isDefinedBy_DescriptorVariable": {
        "@type": ["cdi:DescriptorVariable"],
        "@id": "ex:struct/vitalsLong/dv/measureName",
        "cdi:name": [
          { "@type": ["cdi:ObjectName"], "cdi:name": "measure_name" }
        ],
        "cdif:hasValuesFrom": {
          "@type": ["cdi:DescriptorValueDomain"],
          "@id": "ex:struct/vitalsLong/vd/measureName",
          "cdif:takesValuesFrom": [
            {
              "cdif:value": "heart_rate",
              "cdif:isDefinedBy": { "@id": "ex:struct/vitalsLong/rv/heartRate" }
            },
            {
              "cdif:value": "systolic_bp",
              "cdif:isDefinedBy": { "@id": "ex:struct/vitalsLong/rv/systolicBP" }
            }
          ]
        }
      },
      "cdi:refersTo": { "@id": "ex:struct/vitalsLong/comp/measureValue" }
    },
    {
      "@type": ["cdi:VariableValueComponent"],
      "@id": "ex:struct/vitalsLong/comp/measureValue",
      "cdif:isDefinedBy_RepresentedVariable": {
        "@type": ["cdi:RepresentedVariable"],
        "@id": "ex:struct/vitalsLong/rv/measureValue",
        "cdi:name": [
          { "@type": ["cdi:ObjectName"], "cdi:name": "measure_value" }
        ],
        "cdi:hasIntendedDataType": {
          "@type": ["cdi:ControlledVocabularyEntry"],
          "cdi:entryValue": ["xsd:decimal"]
        }
      }
    },
    {
      "@type": ["cdi:AttributeComponent"],
      "@id": "ex:struct/vitalsLong/comp/observedAt",
      "cdi:qualifies": [
        { "@id": "ex:struct/vitalsLong/comp/measureValue" }
      ],
      "cdif:isDefinedBy_RepresentedVariable": {
        "@type": ["cdi:RepresentedVariable"],
        "@id": "ex:struct/vitalsLong/rv/observedAt",
        "cdi:name": [
          { "@type": ["cdi:ObjectName"], "cdi:name": "observed_at" }
        ],
        "cdi:hasIntendedDataType": {
          "@type": ["cdi:ControlledVocabularyEntry"],
          "cdi:entryValue": ["xsd:dateTime"]
        }
      }
    }
  ],
  "cdi:has_PrimaryKey": {
    "@type": ["cdif:PrimaryKey"],
    "@id": "ex:struct/vitalsLong/pk",
    "cdif:isComposedOf": [
      { "@id": "ex:var/patientId" },
      { "@id": "ex:var/measureName" },
      { "@id": "ex:var/observedAt" }
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
    "https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifProperties/cdifDataStructure/context.jsonld",
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
        "cdi:name": [
          {
            "@type": [
              "cdi:ObjectName"
            ],
            "cdi:name": "patient_id"
          }
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
        "cdi:name": [
          {
            "@type": [
              "cdi:ObjectName"
            ],
            "cdi:name": "measure_name"
          }
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
        "cdi:name": [
          {
            "@type": [
              "cdi:ObjectName"
            ],
            "cdi:name": "measure_value"
          }
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
        "cdi:name": [
          {
            "@type": [
              "cdi:ObjectName"
            ],
            "cdi:name": "observed_at"
          }
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
    cdi:name [ a cdi:ObjectName ;
            cdi:name "measure_name" ] ;
    cdif:hasValuesFrom <https://example.org/struct/vitalsLong/vd/measureName> .

<https://example.org/struct/vitalsLong/pk> a cdif:PrimaryKey ;
    cdif:isComposedOf <https://example.org/var/measureName>,
        <https://example.org/var/observedAt>,
        <https://example.org/var/patientId> .

<https://example.org/struct/vitalsLong/rv/measureValue> a cdi:RepresentedVariable ;
    cdi:hasIntendedDataType [ a cdi:ControlledVocabularyEntry ;
            cdi:entryValue "xsd:decimal" ] ;
    cdi:name [ a cdi:ObjectName ;
            cdi:name "measure_value" ] .

<https://example.org/struct/vitalsLong/rv/observedAt> a cdi:RepresentedVariable ;
    cdi:hasIntendedDataType [ a cdi:ControlledVocabularyEntry ;
            cdi:entryValue "xsd:dateTime" ] ;
    cdi:name [ a cdi:ObjectName ;
            cdi:name "observed_at" ] .

<https://example.org/struct/vitalsLong/rv/patientId> a cdi:RepresentedVariable ;
    cdi:hasIntendedDataType [ a cdi:ControlledVocabularyEntry ;
            cdi:entryValue "xsd:string" ] ;
    cdi:name [ a cdi:ObjectName ;
            cdi:name "patient_id" ] .

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
    "ex": "https://example.org/"
  },
  "@type": ["cdi:DimensionalDataStructure"],
  "@id": "ex:struct/salesCube",
  "cdi:has_DataStructureComponent": [
    {
      "@type": ["cdi:DimensionComponent"],
      "@id": "ex:struct/salesCube/comp/country",
      "cdif:isDefinedBy_RepresentedVariable": {
        "@type": ["cdi:RepresentedVariable"],
        "@id": "ex:struct/salesCube/rv/country",
        "cdi:name": [
          { "@type": ["cdi:ObjectName"], "cdi:name": "country" }
        ],
        "cdi:hasIntendedDataType": {
          "@type": ["cdi:ControlledVocabularyEntry"],
          "cdi:entryValue": ["xsd:string"]
        }
      }
    },
    {
      "@type": ["cdi:DimensionComponent"],
      "@id": "ex:struct/salesCube/comp/quarter",
      "cdif:isDefinedBy_RepresentedVariable": {
        "@type": ["cdi:RepresentedVariable"],
        "@id": "ex:struct/salesCube/rv/quarter",
        "cdi:name": [
          { "@type": ["cdi:ObjectName"], "cdi:name": "quarter" }
        ],
        "cdi:hasIntendedDataType": {
          "@type": ["cdi:ControlledVocabularyEntry"],
          "cdi:entryValue": ["xsd:gYearMonth"]
        }
      }
    },
    {
      "@type": ["cdi:DimensionComponent"],
      "@id": "ex:struct/salesCube/comp/productCategory",
      "cdif:isDefinedBy_RepresentedVariable": {
        "@type": ["cdi:RepresentedVariable"],
        "@id": "ex:struct/salesCube/rv/productCategory",
        "cdi:name": [
          { "@type": ["cdi:ObjectName"], "cdi:name": "product_category" }
        ],
        "cdi:hasIntendedDataType": {
          "@type": ["cdi:ControlledVocabularyEntry"],
          "cdi:entryValue": ["xsd:string"]
        }
      }
    },
    {
      "@type": ["cdi:MeasureComponent"],
      "@id": "ex:struct/salesCube/comp/salesAmount",
      "cdif:isDefinedBy_RepresentedVariable": {
        "@type": ["cdi:RepresentedVariable"],
        "@id": "ex:struct/salesCube/rv/salesAmount",
        "cdi:name": [
          { "@type": ["cdi:ObjectName"], "cdi:name": "sales_amount" }
        ],
        "cdi:simpleUnitOfMeasure": "USD",
        "cdi:hasIntendedDataType": {
          "@type": ["cdi:ControlledVocabularyEntry"],
          "cdi:entryValue": ["xsd:decimal"]
        }
      },
      "cdi:semantic": [
        {
          "@type": ["cdi:PairedControlledVocabularyEntry"],
          "cdi:purpose": "measure",
          "cdi:use": "monetary-total"
        }
      ]
    },
    {
      "@type": ["cdi:AttributeComponent"],
      "@id": "ex:struct/salesCube/comp/currency",
      "cdi:qualifies": [
        { "@id": "ex:struct/salesCube/comp/salesAmount" }
      ],
      "cdif:isDefinedBy_RepresentedVariable": {
        "@type": ["cdi:RepresentedVariable"],
        "@id": "ex:struct/salesCube/rv/currency",
        "cdi:name": [
          { "@type": ["cdi:ObjectName"], "cdi:name": "currency" }
        ],
        "cdi:hasIntendedDataType": {
          "@type": ["cdi:ControlledVocabularyEntry"],
          "cdi:entryValue": ["xsd:string"]
        }
      }
    }
  ],
  "cdi:has_PrimaryKey": {
    "@type": ["cdif:PrimaryKey"],
    "@id": "ex:struct/salesCube/pk",
    "cdif:isComposedOf": [
      { "@id": "ex:var/country" },
      { "@id": "ex:var/quarter" },
      { "@id": "ex:var/productCategory" }
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
    "https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifProperties/cdifDataStructure/context.jsonld",
    {
      "schema": "http://schema.org/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "cdif": "https://cdif.org/0.1/",
      "xsd": "http://www.w3.org/2001/XMLSchema#",
      "ex": "https://example.org/"
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
        "cdi:name": [
          {
            "@type": [
              "cdi:ObjectName"
            ],
            "cdi:name": "country"
          }
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
        "cdi:name": [
          {
            "@type": [
              "cdi:ObjectName"
            ],
            "cdi:name": "quarter"
          }
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
        "cdi:name": [
          {
            "@type": [
              "cdi:ObjectName"
            ],
            "cdi:name": "product_category"
          }
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
        "cdi:name": [
          {
            "@type": [
              "cdi:ObjectName"
            ],
            "cdi:name": "sales_amount"
          }
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
            "cdi:PairedControlledVocabularyEntry"
          ],
          "cdi:purpose": "measure",
          "cdi:use": "monetary-total"
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
        "cdi:name": [
          {
            "@type": [
              "cdi:ObjectName"
            ],
            "cdi:name": "currency"
          }
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
    cdi:name [ a cdi:ObjectName ;
            cdi:name "country" ] .

<https://example.org/struct/salesCube/rv/currency> a cdi:RepresentedVariable ;
    cdi:hasIntendedDataType [ a cdi:ControlledVocabularyEntry ;
            cdi:entryValue "xsd:string" ] ;
    cdi:name [ a cdi:ObjectName ;
            cdi:name "currency" ] .

<https://example.org/struct/salesCube/rv/productCategory> a cdi:RepresentedVariable ;
    cdi:hasIntendedDataType [ a cdi:ControlledVocabularyEntry ;
            cdi:entryValue "xsd:string" ] ;
    cdi:name [ a cdi:ObjectName ;
            cdi:name "product_category" ] .

<https://example.org/struct/salesCube/rv/quarter> a cdi:RepresentedVariable ;
    cdi:hasIntendedDataType [ a cdi:ControlledVocabularyEntry ;
            cdi:entryValue "xsd:gYearMonth" ] ;
    cdi:name [ a cdi:ObjectName ;
            cdi:name "quarter" ] .

<https://example.org/struct/salesCube/rv/salesAmount> a cdi:RepresentedVariable ;
    cdi:hasIntendedDataType [ a cdi:ControlledVocabularyEntry ;
            cdi:entryValue "xsd:decimal" ] ;
    cdi:name [ a cdi:ObjectName ;
            cdi:name "sales_amount" ] ;
    cdi:simpleUnitOfMeasure "USD" .

<https://example.org/struct/salesCube/comp/salesAmount> a cdi:MeasureComponent ;
    cdi:semantic [ a cdi:PairedControlledVocabularyEntry ;
            cdi:purpose "measure" ;
            cdi:use "monetary-total" ] ;
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
  "@type": ["cdi:WideDataStructure"],
  "@id": "ex:struct/vitalsWide",
  "cdi:has_DataStructureComponent": [
    {
      "@type": ["cdi:IdentifierComponent"],
      "@id": "ex:struct/vitalsWide/comp/patientId",
      "cdif:isDefinedBy_RepresentedVariable": {
        "@type": ["cdi:RepresentedVariable"],
        "@id": "ex:struct/vitalsWide/rv/patientId",
        "cdi:name": [
          { "@type": ["cdi:ObjectName"], "cdi:name": "patient_id" }
        ],
        "cdi:hasIntendedDataType": {
          "@type": ["cdi:ControlledVocabularyEntry"],
          "cdi:entryValue": ["xsd:string"]
        }
      }
    },
    {
      "@type": ["cdi:MeasureComponent"],
      "@id": "ex:struct/vitalsWide/comp/systolicBP",
      "cdif:isDefinedBy_RepresentedVariable": {
        "@type": ["cdi:RepresentedVariable"],
        "@id": "ex:struct/vitalsWide/rv/systolicBP",
        "cdi:name": [
          { "@type": ["cdi:ObjectName"], "cdi:name": "systolic_bp" }
        ],
        "cdi:simpleUnitOfMeasure": "mmHg",
        "cdi:hasIntendedDataType": {
          "@type": ["cdi:ControlledVocabularyEntry"],
          "cdi:entryValue": ["xsd:integer"]
        }
      }
    },
    {
      "@type": ["cdi:MeasureComponent"],
      "@id": "ex:struct/vitalsWide/comp/diastolicBP",
      "cdif:isDefinedBy_RepresentedVariable": {
        "@type": ["cdi:RepresentedVariable"],
        "@id": "ex:struct/vitalsWide/rv/diastolicBP",
        "cdi:name": [
          { "@type": ["cdi:ObjectName"], "cdi:name": "diastolic_bp" }
        ],
        "cdi:simpleUnitOfMeasure": "mmHg",
        "cdi:hasIntendedDataType": {
          "@type": ["cdi:ControlledVocabularyEntry"],
          "cdi:entryValue": ["xsd:integer"]
        }
      }
    },
    {
      "@type": ["cdi:MeasureComponent"],
      "@id": "ex:struct/vitalsWide/comp/heartRate",
      "cdif:isDefinedBy_RepresentedVariable": {
        "@type": ["cdi:RepresentedVariable"],
        "@id": "ex:struct/vitalsWide/rv/heartRate",
        "cdi:name": [
          { "@type": ["cdi:ObjectName"], "cdi:name": "heart_rate" }
        ],
        "cdi:simpleUnitOfMeasure": "bpm",
        "cdi:hasIntendedDataType": {
          "@type": ["cdi:ControlledVocabularyEntry"],
          "cdi:entryValue": ["xsd:integer"]
        }
      }
    },
    {
      "@type": ["cdi:AttributeComponent"],
      "@id": "ex:struct/vitalsWide/comp/observedAt",
      "cdif:isDefinedBy_RepresentedVariable": {
        "@type": ["cdi:RepresentedVariable"],
        "@id": "ex:struct/vitalsWide/rv/observedAt",
        "cdi:name": [
          { "@type": ["cdi:ObjectName"], "cdi:name": "observed_at" }
        ],
        "cdi:hasIntendedDataType": {
          "@type": ["cdi:ControlledVocabularyEntry"],
          "cdi:entryValue": ["xsd:dateTime"]
        }
      }
    }
  ],
  "cdi:has_PrimaryKey": {
    "@type": ["cdif:PrimaryKey"],
    "@id": "ex:struct/vitalsWide/pk",
    "cdif:isComposedOf": [
      { "@id": "ex:var/patientId" }
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
    "https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifProperties/cdifDataStructure/context.jsonld",
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
        "cdi:name": [
          {
            "@type": [
              "cdi:ObjectName"
            ],
            "cdi:name": "patient_id"
          }
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
        "cdi:name": [
          {
            "@type": [
              "cdi:ObjectName"
            ],
            "cdi:name": "systolic_bp"
          }
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
        "cdi:name": [
          {
            "@type": [
              "cdi:ObjectName"
            ],
            "cdi:name": "diastolic_bp"
          }
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
        "cdi:name": [
          {
            "@type": [
              "cdi:ObjectName"
            ],
            "cdi:name": "heart_rate"
          }
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
        "cdi:name": [
          {
            "@type": [
              "cdi:ObjectName"
            ],
            "cdi:name": "observed_at"
          }
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
    cdi:name [ a cdi:ObjectName ;
            cdi:name "diastolic_bp" ] ;
    cdi:simpleUnitOfMeasure "mmHg" .

<https://example.org/struct/vitalsWide/rv/heartRate> a cdi:RepresentedVariable ;
    cdi:hasIntendedDataType [ a cdi:ControlledVocabularyEntry ;
            cdi:entryValue "xsd:integer" ] ;
    cdi:name [ a cdi:ObjectName ;
            cdi:name "heart_rate" ] ;
    cdi:simpleUnitOfMeasure "bpm" .

<https://example.org/struct/vitalsWide/rv/observedAt> a cdi:RepresentedVariable ;
    cdi:hasIntendedDataType [ a cdi:ControlledVocabularyEntry ;
            cdi:entryValue "xsd:dateTime" ] ;
    cdi:name [ a cdi:ObjectName ;
            cdi:name "observed_at" ] .

<https://example.org/struct/vitalsWide/rv/patientId> a cdi:RepresentedVariable ;
    cdi:hasIntendedDataType [ a cdi:ControlledVocabularyEntry ;
            cdi:entryValue "xsd:string" ] ;
    cdi:name [ a cdi:ObjectName ;
            cdi:name "patient_id" ] .

<https://example.org/struct/vitalsWide/rv/systolicBP> a cdi:RepresentedVariable ;
    cdi:hasIntendedDataType [ a cdi:ControlledVocabularyEntry ;
            cdi:entryValue "xsd:integer" ] ;
    cdi:name [ a cdi:ObjectName ;
            cdi:name "systolic_bp" ] ;
    cdi:simpleUnitOfMeasure "mmHg" .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: DDI-CDI Data Structure
description: Data organization based on reusable data structure components.
anyOf:
- $ref: '#/$defs/DataStructure'
- $ref: '#/$defs/DimensionalDataStructure'
- $ref: '#/$defs/LongDataStructure'
- $ref: '#/$defs/WideDataStructure'
$defs:
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
          - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiCDIFProperties/ddi-cdif-data-types/schema.yaml#/$defs/id-reference
        minItems: 1
      cdi:has_DataStructureComponent:
        type: array
        items:
          anyOf:
          - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifProperties/cdifDataStructureComponent/schema.yaml
          - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiCDIFProperties/ddi-cdif-data-types/schema.yaml#/$defs/id-reference
        minItems: 1
      cdi:has_PrimaryKey:
        $ref: '#/$defs/PrimaryKey'
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
          - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifProperties/cdifDataStructureComponent/schema.yaml#/$defs/IdentifierComponent
          - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifProperties/cdifDataStructureComponent/schema.yaml#/$defs/MeasureComponent
          - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifProperties/cdifDataStructureComponent/schema.yaml#/$defs/AttributeComponent
          - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifProperties/cdifDataStructureComponent/schema.yaml#/$defs/DimensionComponent
        minItems: 1
      cdi:has_PrimaryKey:
        $ref: '#/$defs/PrimaryKey'
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
          - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifProperties/cdifDataStructureComponent/schema.yaml#/$defs/IdentifierComponent
          - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifProperties/cdifDataStructureComponent/schema.yaml#/$defs/VariableDescriptorComponent
          - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifProperties/cdifDataStructureComponent/schema.yaml#/$defs/VariableValueComponent
          - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifProperties/cdifDataStructureComponent/schema.yaml#/$defs/AttributeComponent
        allOf:
        - contains:
            $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifProperties/cdifDataStructureComponent/schema.yaml#/$defs/IdentifierComponent
          minContains: 1
          maxContains: 1
        - contains:
            $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifProperties/cdifDataStructureComponent/schema.yaml#/$defs/VariableDescriptorComponent
          minContains: 1
          maxContains: 1
        - contains:
            $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifProperties/cdifDataStructureComponent/schema.yaml#/$defs/VariableValueComponent
          minContains: 1
          maxContains: 1
        minItems: 3
      cdi:has_PrimaryKey:
        $ref: '#/$defs/PrimaryKey'
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
          - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifProperties/cdifDataStructureComponent/schema.yaml
          - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiCDIFProperties/ddi-cdif-data-types/schema.yaml#/$defs/id-reference
        minItems: 1
      cdi:has_PrimaryKey:
        $ref: '#/$defs/PrimaryKey'
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
        $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiCDIFProperties/ddi-cdif-data-types/schema.yaml#/$defs/Identifier
        description: Identifier for objects requiring short- or long-lasting referencing
          and management.
      cdi:name:
        type: array
        items:
          $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiCDIFProperties/ddi-cdif-data-types/schema.yaml#/$defs/ObjectName
        minItems: 1
        description: Human understandable name (liguistic signifier, word, phrase,
          or mnemonic). May follow ISO/IEC 11179-5 naming principles, and have context
          provided to specify usage.
      cdif:has_DataStructureComponent:
        type: array
        items:
          anyOf:
          - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifProperties/cdifDataStructureComponent/schema.yaml
          - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiCDIFProperties/ddi-cdif-data-types/schema.yaml#/$defs/id-reference
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
        $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiCDIFProperties/ddi-cdif-data-types/schema.yaml#/$defs/Identifier
        description: Identifier for objects requiring short- or long-lasting referencing
          and management.
      cdi:isComposedOf:
        type: array
        items:
          anyOf:
          - $ref: '#/$defs/ForeignKeyComponent'
          - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiCDIFProperties/ddi-cdif-data-types/schema.yaml#/$defs/id-reference
        minItems: 1
    required:
    - '@type'
  ForeignKeyComponent:
    type: object
    description: Role of a data structure component for content referencing purposes
    properties:
      '@type':
        type: array
        items:
          type: string
        contains:
          const: cdi:ForeignKeyComponent
        minItems: 1
      '@id':
        type: string
        description: Identifier for this ForeignKeyComponent node
      cdi:identifier:
        $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiCDIFProperties/ddi-cdif-data-types/schema.yaml#/$defs/Identifier
        description: Identifier for objects requiring short- or long-lasting referencing
          and management.
      cdi:references:
        anyOf:
        - $ref: '#/$defs/PrimaryKeyComponent'
        - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiCDIFProperties/ddi-cdif-data-types/schema.yaml#/$defs/id-reference
      cdi:correspondsTo:
        anyOf:
        - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifProperties/cdifDataStructureComponent/schema.yaml
        - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiCDIFProperties/ddi-cdif-data-types/schema.yaml#/$defs/id-reference
    required:
    - '@type'
  PrimaryKey:
    type: object
    description: Role of an ordered set of cdi:InstanceVariables that uniquely identify
      a data instance. Array order of cdif:isComposedOf items is the position; no
      intermediate ComponentPosition wrapper.
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
        description: Ordered list of cdi:InstanceVariables (inline cdifInstanceVariable
          or @id-reference). Position is implicit in array order.
        items:
          anyOf:
          - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifProperties/cdifInstanceVariable/schema.yaml
          - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiCDIFProperties/ddi-cdif-data-types/schema.yaml#/$defs/id-reference
        minItems: 1
    required:
    - '@type'
    - cdif:isComposedOf
  PrimaryKeyComponent:
    type: object
    description: Role of a data structure component for content identification purposes
    properties:
      '@type':
        type: array
        items:
          type: string
        contains:
          const: cdi:PrimaryKeyComponent
        minItems: 1
      '@id':
        type: string
        description: Identifier for this PrimaryKeyComponent node
      cdi:identifier:
        $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiCDIFProperties/ddi-cdif-data-types/schema.yaml#/$defs/Identifier
        description: Identifier for objects requiring short- or long-lasting referencing
          and management.
      cdi:correspondsTo:
        anyOf:
        - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifProperties/cdifDataStructureComponent/schema.yaml
        - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/ddiCDIFProperties/ddi-cdif-data-types/schema.yaml#/$defs/id-reference
    required:
    - '@type'
x-jsonld-prefixes:
  cdi: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/

```

Links to the schema:

* YAML version: [schema.yaml](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifProperties/cdifDataStructure/schema.json)
* JSON version: [schema.json](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifProperties/cdifDataStructure/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
    "skos": "http://www.w3.org/2004/02/skos/core#",
    "schema": "http://schema.org/",
    "cdif": "https://cdif.org/0.1/",
    "xsd": "http://www.w3.org/2001/XMLSchema#",
    "dcterms": "http://purl.org/dc/terms/",
    "spdx": "http://spdx.org/rdf/terms#",
    "xas": "https://xas.org/dictionary/",
    "nxs": "http://purl.org/nexusformat/definitions/",
    "prov": "http://www.w3.org/ns/prov#",
    "ex": "https://example.org/",
    "dcat": "http://www.w3.org/ns/dcat#",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifProperties/cdifDataStructure/context.jsonld)

## Sources

* [DDI-CDI 1.0 Specification](https://ddialliance.org/Specification/DDI-CDI/1.0/)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/Cross-Domain-Interoperability-Framework/metadataBuildingBlocks](https://github.com/Cross-Domain-Interoperability-Framework/metadataBuildingBlocks)
* Path: `_sources/cdifProperties/cdifDataStructure`

