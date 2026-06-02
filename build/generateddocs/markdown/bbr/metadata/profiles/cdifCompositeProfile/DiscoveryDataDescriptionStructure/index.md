
# CDIF Data Structure profile (Schema)

`cdif.bbr.metadata.profiles.cdifCompositeProfile.DiscoveryDataDescriptionStructure` *v0.1*

Extends the CDIF Data Description profile with full DDI-CDI structural complexity: data structures (DataStructure / Dimensional / Long / Wide), component subclasses (Identifier / Measure / Attribute / Dimension / VariableValue / VariableDescriptor), represented variables, and value domains. Distribution items are expected to carry cdi:isStructuredBy pointing at a Data Structure node.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

# CDIF Data Structure profile

The **CDIF Data Structure profile** extends the [Data Description profile](../CDIFDataDescriptionProfile/) with full DDI-CDI structural complexity. Use this profile when the catalog record must commit to *how* the data is organized — which variables play which role, what the keys are, what value domains constrain measurements — not just *which* variables are measured.

## What it adds beyond Data Description

- **Component subclasses.** [cdifDataStructureComponent](../../../cdifProperties/cdifDataStructureComponent/) defines `cdi:IdentifierComponent`, `cdi:MeasureComponent`, `cdi:AttributeComponent`, `cdi:DimensionComponent`, `cdi:VariableValueComponent`, and `cdi:VariableDescriptorComponent` as Node classes — the structural counterparts to the role values carried directly on InstanceVariables in the Data Description profile.
- **Polymorphic DataStructure root.** [cdifDataStructure](../../../cdifProperties/cdifDataStructure/) carries `cdi:DataStructure`, `cdi:DimensionalDataStructure`, `cdi:LongDataStructure`, and `cdi:WideDataStructure`, plus shared structural types (`cdi:DimensionGroup`, `cdi:ForeignKey`, `cdi:ForeignKeyComponent`, `cdif:PrimaryKey`, `cdi:PrimaryKeyComponent`).
- **Represented variables and value domains.** [cdifRepresentedVariable](../../../cdifProperties/cdifRepresentedVariable/) and [cdifValueDomain](../../../cdifProperties/cdifValueDomain/) provide the conceptual variable definitions and substantive/sentinel value domains referenced from components.
- **Descriptor variable.** [cdifDescriptorVariable](../../../cdifProperties/cdifDescriptorVariable/) defines the `cdi:DescriptorVariable` + `cdi:DescriptorValueDomain` pattern that maps descriptor-column codes to the RepresentedVariables they name (long-format datasets).
- **Distribution is structured.** Every `schema:distribution` item must carry `cdi:isStructuredBy` pointing at a Data Structure node (Data Description allows it but does not require it).
- **InstanceVariable role / qualifies redundancy forbidden.** `cdif:role` and `cdi:qualifies` on items in `schema:variableMeasured` are not allowed at this profile level — the component class type on `cdi:isStructuredBy` already encodes the role, and `AttributeComponent.cdi:qualifies` encodes the qualifies relation.
- **Summary statistics.** `cdif:statistics` (inherited from Data Description via [cdifStatistics](../../../cdifProperties/cdifStatistics/)) carries one or more `cdi:Statistics` bundles or a `cdi:StatisticsCollection` describing computed summary values for the dataset's variables.

## Distribution typing rules

How a `schema:distribution` item is typed determines what else it must carry. The two rules below are enforced at the profile level (`schema:distribution.items.allOf` with `if/then`):

| `@type` includes... | `cdif:hasPhysicalMapping` | `cdi:isStructuredBy` |
|---|---|---|
| `cdi:TabularTextDataSet` or `cdi:StructuredDataSet` | **required** | any DataStructure variant (Long / Dimensional / Wide / abstract) |
| `cdi:PhysicalDataSet` only (no subclass) | not required | must be the abstract `cdi:DataStructure` variant (or `@id`-only reference) — Long / Dimensional / Wide subclasses are forbidden because they imply a specific physical realization |

The bare-`cdi:PhysicalDataSet` case is the "structure reuse" pattern: a dataset that points at a Data Structure node (defining RepresentedVariables + components) without committing to a specific physical file layout. Use this when the same conceptual structure is shared by multiple physical realizations, or when the physical layout is documented externally.

## Conformance

This profile composes [cdifCore](../../../cdifProperties/cdifCore/) and [cdifDataDescription](../../../cdifProperties/cdifDataDescription/), so a conforming record must carry `dcterms:conformsTo` URIs for all three:

- `https://w3id.org/cdif/core/1.1`
- `https://w3id.org/cdif/data_description/1.1`
- `https://w3id.org/cdif/data_structure/1.1`

## When to use which profile

| Want to publish... | Use profile |
|---|---|
| Catalog record with `schema:variableMeasured` and roles, no structure commitment | [Data Description](../CDIFDataDescriptionProfile/) |
| Wide table with simple measures | [Data Description](../CDIFDataDescriptionProfile/) |
| Long-format data (descriptor + reference columns) | **CDIF Data Structure** |
| Dimensional / cube data | **CDIF Data Structure** |
| Anything where consumers need keys + components + value domains | **CDIF Data Structure** |

## Examples

### Minimal CDIF Data Structure Profile
Smallest valid Data Structure profile record: a wide-format patient
vitals dataset with two InstanceVariables (patientId as UnitIdentifier,
systolicBP as Measure) and a single distribution whose
cdi:isStructuredBy points by @id at a Data Structure node declared
elsewhere. The conformsTo array carries the three required URIs
(core/1.0, data_description/1.0, data_structure/1.0).
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "dcterms": "http://purl.org/dc/terms/",
    "dcat": "http://www.w3.org/ns/dcat#",
    "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
    "cdif": "https://cdif.org/0.1/",
    "ex": "https://example.org/",
    "prov": "http://www.w3.org/ns/prov#"
  },
  "@id": "ex:dataset/vitalsWide",
  "@type": [
    "schema:Dataset"
  ],
  "schema:name": "Patient vitals (wide table)",
  "schema:identifier": "https://doi.org/10.1234/vitals-wide-2025",
  "schema:dateModified": "2025-09-01",
  "schema:license": [
    "https://creativecommons.org/licenses/by/4.0/"
  ],
  "schema:variableMeasured": [
    {
      "@id": "ex:var/patientId",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "patient_id",
      "cdif:uses": [
        {
          "@id": "ex:struct/vitalsWide/rv/patientId"
        }
      ]
    },
    {
      "@id": "ex:var/systolicBP",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "systolic_bp",
      "cdif:uses": [
        {
          "@id": "ex:struct/vitalsWide/rv/systolicBP"
        }
      ]
    }
  ],
  "schema:distribution": [
    {
      "@type": [
        "schema:DataDownload",
        "cdi:PhysicalDataSet"
      ],
      "schema:name": "vitals.csv",
      "schema:contentUrl": "https://example.org/downloads/vitals.csv",
      "schema:encodingFormat": [
        "text/csv"
      ],
      "cdi:isStructuredBy": {
        "@id": "ex:struct/vitalsWide"
      }
    }
  ],
  "schema:subjectOf": {
    "@id": "ex:dataset/vitalsWide/metadata",
    "@type": [
      "schema:Dataset"
    ],
    "schema:additionalType": [
      "dcat:CatalogRecord"
    ],
    "schema:about": {
      "@id": "ex:dataset/vitalsWide"
    },
    "dcterms:conformsTo": [
      {
        "@id": "https://w3id.org/cdif/core/1.1"
      },
      {
        "@id": "https://w3id.org/cdif/data_description/1.1"
      },
      {
        "@id": "https://w3id.org/cdif/data_structure/1.1"
      },
      {
        "@id": "https://w3id.org/cdif/discovery/1.1"
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
      "cdif": "https://cdif.org/0.1/",
      "dcterms": "http://purl.org/dc/terms/",
      "dcat": "http://www.w3.org/ns/dcat#"
    },
    "https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/profiles/cdifCompositeProfile/DiscoveryDataDescriptionStructure/context.jsonld",
    {
      "schema": "http://schema.org/",
      "dcterms": "http://purl.org/dc/terms/",
      "dcat": "http://www.w3.org/ns/dcat#",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "cdif": "https://cdif.org/0.1/",
      "ex": "https://example.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:dataset/vitalsWide",
  "@type": [
    "schema:Dataset"
  ],
  "schema:name": "Patient vitals (wide table)",
  "schema:identifier": "https://doi.org/10.1234/vitals-wide-2025",
  "schema:dateModified": "2025-09-01",
  "schema:license": [
    "https://creativecommons.org/licenses/by/4.0/"
  ],
  "schema:variableMeasured": [
    {
      "@id": "ex:var/patientId",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "patient_id",
      "cdif:uses": [
        {
          "@id": "ex:struct/vitalsWide/rv/patientId"
        }
      ]
    },
    {
      "@id": "ex:var/systolicBP",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "systolic_bp",
      "cdif:uses": [
        {
          "@id": "ex:struct/vitalsWide/rv/systolicBP"
        }
      ]
    }
  ],
  "schema:distribution": [
    {
      "@type": [
        "schema:DataDownload",
        "cdi:PhysicalDataSet"
      ],
      "schema:name": "vitals.csv",
      "schema:contentUrl": "https://example.org/downloads/vitals.csv",
      "schema:encodingFormat": [
        "text/csv"
      ],
      "cdi:isStructuredBy": {
        "@id": "ex:struct/vitalsWide"
      }
    }
  ],
  "schema:subjectOf": {
    "@id": "ex:dataset/vitalsWide/metadata",
    "@type": [
      "schema:Dataset"
    ],
    "schema:additionalType": [
      "dcat:CatalogRecord"
    ],
    "schema:about": {
      "@id": "ex:dataset/vitalsWide"
    },
    "dcterms:conformsTo": [
      {
        "@id": "https://w3id.org/cdif/core/1.1"
      },
      {
        "@id": "https://w3id.org/cdif/data_description/1.1"
      },
      {
        "@id": "https://w3id.org/cdif/data_structure/1.1"
      },
      {
        "@id": "https://w3id.org/cdif/discovery/1.1"
      }
    ]
  }
}
```

#### ttl
```ttl
@prefix cdi: <http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/> .
@prefix cdif: <https://cdif.org/0.1/> .
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix schema1: <http://schema.org/> .

<https://example.org/dataset/vitalsWide> a schema1:Dataset ;
    schema1:dateModified "2025-09-01" ;
    schema1:distribution [ a cdi:PhysicalDataSet,
                schema1:DataDownload ;
            cdi:isStructuredBy <https://example.org/struct/vitalsWide> ;
            schema1:contentUrl "https://example.org/downloads/vitals.csv" ;
            schema1:encodingFormat "text/csv" ;
            schema1:name "vitals.csv" ] ;
    schema1:identifier "https://doi.org/10.1234/vitals-wide-2025" ;
    schema1:license "https://creativecommons.org/licenses/by/4.0/" ;
    schema1:name "Patient vitals (wide table)" ;
    schema1:subjectOf <https://example.org/dataset/vitalsWide/metadata> ;
    schema1:variableMeasured <https://example.org/var/patientId>,
        <https://example.org/var/systolicBP> .

<https://example.org/dataset/vitalsWide/metadata> a schema1:Dataset ;
    dcterms:conformsTo <https://w3id.org/cdif/core/1.1>,
        <https://w3id.org/cdif/data_description/1.1>,
        <https://w3id.org/cdif/data_structure/1.1>,
        <https://w3id.org/cdif/discovery/1.1> ;
    schema1:about <https://example.org/dataset/vitalsWide> ;
    schema1:additionalType "dcat:CatalogRecord" .

<https://example.org/var/patientId> a cdi:InstanceVariable,
        schema1:PropertyValue ;
    schema1:name "patient_id" ;
    cdif:uses <https://example.org/struct/vitalsWide/rv/patientId> .

<https://example.org/var/systolicBP> a cdi:InstanceVariable,
        schema1:PropertyValue ;
    schema1:name "systolic_bp" ;
    cdif:uses <https://example.org/struct/vitalsWide/rv/systolicBP> .


```


### Complete CDIF Data Structure Profile (Long format)
Fully-described long-format vital-signs dataset. Four InstanceVariables
in schema:variableMeasured cover the four cdif:role values used by
long-format data: UnitIdentifier (patientId), Descriptor (measureName),
ReferenceVariable (measureValue), Attribute (observedAt, qualifying
measureValue). The Dataset's cdif:hasPrimaryKey composes patientId +
measureName + observedAt as an ordered array. The distribution item is
typed as cdi:TabularTextDataSet + cdi:PhysicalDataSet, carries CSVW
physical layout properties, and inlines a full cdi:LongDataStructure
via cdi:isStructuredBy — the structure carries all four components
(matching the LongDataStructure cardinality constraint of exactly one
each UnitIdentifier / VariableDescriptor / VariableValue plus the
optional Attribute) and its own cdif:PrimaryKey.
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "dcterms": "http://purl.org/dc/terms/",
    "dcat": "http://www.w3.org/ns/dcat#",
    "prov": "http://www.w3.org/ns/prov#",
    "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
    "cdif": "https://cdif.org/0.1/",
    "csvw": "http://www.w3.org/ns/csvw#",
    "xsd": "http://www.w3.org/2001/XMLSchema#",
    "ex": "https://example.org/"
  },
  "@id": "ex:dataset/vitalsLong",
  "@type": [
    "schema:Dataset"
  ],
  "schema:name": "Patient vital signs (long-format observations)",
  "schema:description": "Time-series of vital sign measurements (heart rate, systolic BP, diastolic BP, temperature) in long format: one row per observation with a descriptor column naming the measure and a reference column holding the value.",
  "schema:identifier": "https://doi.org/10.1234/vitals-long-2025",
  "schema:dateModified": "2025-09-15",
  "schema:license": [
    "https://creativecommons.org/licenses/by/4.0/"
  ],
  "schema:additionalType": [
    "https://www.wikidata.org/wiki/Q47652734"
  ],
  "schema:sameAs": [
    {
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": "urn:noaa-ghcnd:station-id",
      "schema:value": "DEMO-LONG-2025",
      "schema:url": "https://example.org/aliases/DEMO-LONG-2025"
    }
  ],
  "schema:version": "1.0",
  "schema:url": "https://example.org/datasets/vitals-long-2025",
  "schema:inLanguage": "en",
  "schema:datePublished": "2025-10-01",
  "schema:conditionsOfAccess": [
    "Open access; no registration required."
  ],
  "schema:keywords": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:name": "Vital signs",
      "schema:termCode": "VS",
      "schema:identifier": {
        "@type": [
          "schema:PropertyValue"
        ],
        "schema:propertyID": "https://loinc.org/",
        "schema:value": "VS",
        "schema:url": "https://loinc.org/8716-3/"
      },
      "schema:inDefinedTermSet": "https://loinc.org/"
    },
    "patient monitoring",
    "long format"
  ],
  "schema:relatedLink": [
    {
      "@type": [
        "schema:LinkRole"
      ],
      "schema:linkRelationship": "describedby",
      "schema:target": {
        "@type": [
          "schema:EntryPoint"
        ],
        "schema:name": "Long-format encoding rationale",
        "schema:url": "https://example.org/docs/long-vs-wide.html",
        "schema:encodingFormat": "text/html"
      }
    }
  ],
  "schema:publishingPrinciples": [
    {
      "@type": [
        "schema:CreativeWork",
        "dcat:Relationship"
      ],
      "schema:name": "FAIR data policy",
      "schema:url": "https://example.org/policy/fair-policy.html",
      "schema:description": "Institutional FAIR data policy."
    }
  ],
  "schema:creator": {
    "@list": [
      {
        "@id": "https://orcid.org/0000-0002-7933-2154",
        "@type": [
          "schema:Person"
        ],
        "schema:name": "Richard, Stephen M.",
        "schema:identifier": {
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": "https://orcid.org",
          "schema:value": "0000-0002-7933-2154",
          "schema:url": "https://orcid.org/0000-0002-7933-2154"
        },
        "schema:contactPoint": {
          "@type": [
            "schema:ContactPoint"
          ],
          "schema:email": "smr@example.org"
        }
      }
    ]
  },
  "schema:contributor": [
    {
      "@type": [
        "schema:Role"
      ],
      "schema:roleName": {
        "@type": [
          "schema:DefinedTerm"
        ],
        "schema:name": "Curator",
        "schema:termCode": "data-curation",
        "schema:identifier": {
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": "https://credit.niso.org/",
          "schema:value": "data-curation",
          "schema:url": "https://credit.niso.org/contributor-roles/data-curation/"
        },
        "schema:inDefinedTermSet": "https://credit.niso.org/"
      },
      "schema:contributor": {
        "@id": "https://orcid.org/0000-0001-8898-3457",
        "@type": [
          "schema:Person"
        ],
        "schema:name": "Mojarro, Angel",
        "schema:identifier": {
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": "https://orcid.org",
          "schema:value": "0000-0001-8898-3457",
          "schema:url": "https://orcid.org/0000-0001-8898-3457"
        }
      }
    }
  ],
  "schema:publisher": {
    "@id": "https://ror.org/0171mag52",
    "@type": [
      "schema:Organization"
    ],
    "schema:name": "Demo Health Data Repository",
    "schema:identifier": {
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": "https://ror.org",
      "schema:value": "0171mag52",
      "schema:url": "https://ror.org/0171mag52"
    }
  },
  "schema:provider": [
    {
      "@id": "https://ror.org/0171mag52",
      "@type": [
        "schema:Organization"
      ],
      "schema:name": "Demo Health Data Repository",
      "schema:identifier": {
        "@type": [
          "schema:PropertyValue"
        ],
        "schema:propertyID": "https://ror.org",
        "schema:value": "0171mag52",
        "schema:url": "https://ror.org/0171mag52"
      }
    }
  ],
  "schema:funding": [
    {
      "@type": [
        "schema:MonetaryGrant"
      ],
      "@id": "ex:grant/nih-R01-XXXX",
      "schema:identifier": {
        "@type": [
          "schema:PropertyValue"
        ],
        "schema:propertyID": "https://reporter.nih.gov",
        "schema:value": "R01-XXXX",
        "schema:url": "https://reporter.nih.gov/search/?term=R01-XXXX"
      },
      "schema:name": "NIH Award R01-XXXX",
      "schema:funder": {
        "@id": "https://ror.org/01cwqze88",
        "@type": [
          "schema:Organization"
        ],
        "schema:name": "National Institutes of Health",
        "schema:identifier": {
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": "https://ror.org",
          "schema:value": "01cwqze88",
          "schema:url": "https://ror.org/01cwqze88"
        }
      }
    }
  ],
  "schema:variableMeasured": [
    {
      "@id": "ex:var/patientId",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "patient_id",
      "cdif:physicalDataType": "xsd:string",
      "cdif:uses": [
        {
          "@id": "ex:struct/vitalsLong/rv/patientId"
        }
      ]
    },
    {
      "@id": "ex:var/measureName",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "measure_name",
      "cdif:physicalDataType": "xsd:string",
      "cdif:uses": [
        {
          "@id": "ex:struct/vitalsLong/dv/measureName"
        }
      ]
    },
    {
      "@id": "ex:var/measureValue",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "measure_value",
      "cdif:physicalDataType": "xsd:decimal",
      "cdif:uses": [
        {
          "@id": "ex:struct/vitalsLong/rv/measureValue"
        }
      ]
    },
    {
      "@id": "ex:var/observedAt",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "observed_at",
      "cdif:physicalDataType": "xsd:dateTime",
      "cdif:uses": [
        {
          "@id": "ex:struct/vitalsLong/rv/observedAt"
        }
      ]
    }
  ],
  "cdif:hasPrimaryKey": {
    "@type": [
      "cdif:Key"
    ],
    "@id": "ex:dataset/vitalsLong/pk",
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
  },
  "schema:distribution": [
    {
      "@type": [
        "schema:DataDownload",
        "cdi:TabularTextDataSet",
        "cdi:PhysicalDataSet"
      ],
      "schema:name": "vitals-long.csv",
      "schema:contentUrl": "https://example.org/downloads/vitals-long.csv",
      "schema:encodingFormat": [
        "text/csv"
      ],
      "cdi:characterSet": "UTF-8",
      "cdif:fileSize": 2.4,
      "cdif:fileSizeUofM": "MB",
      "cdi:isDelimited": true,
      "csvw:delimiter": ",",
      "csvw:header": true,
      "csvw:headerRowCount": 1,
      "cdif:hasPhysicalMapping": [
        {
          "cdif:index": 0,
          "cdif:format": "string",
          "cdif:physicalDataType": "string",
          "cdif:formats_InstanceVariable": {
            "@id": "ex:var/patientId"
          }
        },
        {
          "cdif:index": 1,
          "cdif:format": "string",
          "cdif:physicalDataType": "string",
          "cdif:formats_InstanceVariable": {
            "@id": "ex:var/measureName"
          }
        },
        {
          "cdif:index": 2,
          "cdif:format": "decimal",
          "cdif:physicalDataType": "decimal",
          "cdif:formats_InstanceVariable": {
            "@id": "ex:var/measureValue"
          }
        },
        {
          "cdif:index": 3,
          "cdif:format": "ISO8601",
          "cdif:physicalDataType": "dateTime",
          "cdif:formats_InstanceVariable": {
            "@id": "ex:var/observedAt"
          }
        }
      ],
      "cdi:isStructuredBy": {
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
              "cdif:definition": "Pseudonymous patient identifier.",
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
                    "cdif:value": "systolic_bp",
                    "cdif:isDefinedBy": {
                      "@type": [
                        "cdi:RepresentedVariable"
                      ],
                      "@id": "ex:struct/vitalsLong/rv/systolicBP",
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
                      "@id": "ex:struct/vitalsLong/rv/diastolicBP",
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
                      "@type": [
                        "cdi:RepresentedVariable"
                      ],
                      "@id": "ex:struct/vitalsLong/rv/heartRate",
                      "cdif:name": [
                        "heart_rate"
                      ],
                      "cdi:simpleUnitOfMeasure": "bpm",
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
                    "cdif:value": "temp_c",
                    "cdif:isDefinedBy": {
                      "@type": [
                        "cdi:RepresentedVariable"
                      ],
                      "@id": "ex:struct/vitalsLong/rv/temperatureC",
                      "cdif:name": [
                        "body_temperature_celsius"
                      ],
                      "cdi:simpleUnitOfMeasure": "Cel",
                      "cdi:hasIntendedDataType": {
                        "@type": [
                          "cdi:ControlledVocabularyEntry"
                        ],
                        "cdi:entryValue": [
                          "xsd:decimal"
                        ]
                      }
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
              "cdif:definition": "Numeric value of the vital sign named by measure_name.",
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
              "cdif:definition": "Timestamp of the observation; qualifies measure_value.",
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
    },
    {
      "@type": [
        "schema:WebAPI"
      ],
      "schema:name": "Vitals query API",
      "schema:serviceType": {
        "@type": [
          "schema:DefinedTerm"
        ],
        "schema:name": "OGC API - Features",
        "schema:identifier": "https://www.ogc.org/standard/ogcapi-features/",
        "schema:termCode": "ogcapi-features"
      },
      "schema:termsOfService": "Open access, no authentication required.",
      "schema:documentation": {
        "@type": [
          "schema:CreativeWork",
          "dcat:Relationship"
        ],
        "schema:name": "OpenAPI specification for vitals service",
        "schema:url": "https://example.org/api/v1/openapi.json"
      },
      "schema:potentialAction": [
        {
          "@type": [
            "schema:Action"
          ],
          "schema:name": "Query vitals as long-format CSV",
          "schema:target": {
            "@type": [
              "schema:EntryPoint"
            ],
            "schema:description": "OGC API Features endpoint returning vitals observations as long-format CSV.",
            "schema:urlTemplate": "https://example.org/api/v1/collections/vitals/items?f={format}&limit={limit}&offset={offset}",
            "schema:httpMethod": [
              "GET"
            ],
            "schema:contentType": [
              "text/csv"
            ]
          },
          "schema:result": {
            "@type": [
              "schema:DataDownload",
              "cdi:TabularTextDataSet",
              "cdi:PhysicalDataSet"
            ],
            "schema:name": "Vitals API response (long format)",
            "schema:contentUrl": "https://example.org/api/v1/collections/vitals/items?f=csv",
            "schema:encodingFormat": [
              "text/csv"
            ],
            "cdi:characterSet": "UTF-8",
            "cdif:fileSize": 0.5,
            "cdif:fileSizeUofM": "MB",
            "cdi:isDelimited": true,
            "csvw:delimiter": ",",
            "csvw:header": true,
            "csvw:headerRowCount": 1,
            "cdif:hasPhysicalMapping": [
              {
                "cdif:index": 0,
                "cdif:format": "string",
                "cdif:physicalDataType": "string",
                "cdif:formats_InstanceVariable": {
                  "@id": "ex:var/patientId"
                }
              },
              {
                "cdif:index": 1,
                "cdif:format": "string",
                "cdif:physicalDataType": "string",
                "cdif:formats_InstanceVariable": {
                  "@id": "ex:var/measureName"
                }
              },
              {
                "cdif:index": 2,
                "cdif:format": "decimal",
                "cdif:physicalDataType": "decimal",
                "cdif:formats_InstanceVariable": {
                  "@id": "ex:var/measureValue"
                }
              },
              {
                "cdif:index": 3,
                "cdif:format": "ISO8601",
                "cdif:physicalDataType": "dateTime",
                "cdif:formats_InstanceVariable": {
                  "@id": "ex:var/observedAt"
                }
              }
            ],
            "cdi:isStructuredBy": {
              "@id": "ex:struct/vitalsLong"
            }
          },
          "schema:query-input": [
            {
              "@type": [
                "schema:PropertyValueSpecification"
              ],
              "schema:valueName": "format",
              "schema:description": "Response format token (csv only for this example).",
              "schema:valueRequired": false,
              "schema:valuePattern": "csv"
            },
            {
              "@type": [
                "schema:PropertyValueSpecification"
              ],
              "schema:valueName": "limit",
              "schema:description": "Maximum number of observations to return (default 100).",
              "schema:valueRequired": false
            },
            {
              "@type": [
                "schema:PropertyValueSpecification"
              ],
              "schema:valueName": "offset",
              "schema:description": "Starting index for pagination.",
              "schema:valueRequired": false
            }
          ]
        }
      ]
    }
  ],
  "prov:wasGeneratedBy": [
    {
      "@type": [
        "prov:Activity"
      ],
      "@id": "ex:act/vitals-aggregation",
      "prov:used": [
        {
          "@id": "ex:tool/vitals-aggregator"
        }
      ]
    }
  ],
  "prov:wasDerivedFrom": [
    {
      "@type": [
        "schema:CreativeWork",
        "dcat:Relationship"
      ],
      "schema:name": "EHR clinical encounters export, 2024-2025",
      "schema:url": "https://example.org/sources/clinical-encounters-2024-2025",
      "schema:description": "Source EHR system from which the long-format observations were derived."
    }
  ],
  "cdif:statistics": [
    {
      "@type": [
        "cdi:Statistics"
      ],
      "cdi:typeOfStatistic": {
        "@type": [
          "schema:DefinedTerm"
        ],
        "schema:name": "Count",
        "schema:termCode": "count",
        "schema:inDefinedTermSet": "https://ddialliance.org/vocab/statistic-types"
      },
      "cdi:statistic": [
        {
          "cdi:computationBase": "Total",
          "cdi:content": 12450,
          "cdi:typeOfNumericValue": "decimal"
        }
      ]
    }
  ],
  "schema:subjectOf": {
    "@id": "ex:dataset/vitalsLong/metadata",
    "@type": [
      "schema:Dataset"
    ],
    "schema:additionalType": [
      "dcat:CatalogRecord"
    ],
    "schema:about": {
      "@id": "ex:dataset/vitalsLong"
    },
    "dcterms:conformsTo": [
      {
        "@id": "https://w3id.org/cdif/core/1.1"
      },
      {
        "@id": "https://w3id.org/cdif/data_description/1.1"
      },
      {
        "@id": "https://w3id.org/cdif/data_structure/1.1"
      },
      {
        "@id": "https://w3id.org/cdif/discovery/1.1"
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
      "cdif": "https://cdif.org/0.1/",
      "csvw": "http://www.w3.org/ns/csvw#",
      "dcterms": "http://purl.org/dc/terms/",
      "dcat": "http://www.w3.org/ns/dcat#",
      "xsd": "http://www.w3.org/2001/XMLSchema#"
    },
    "https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/profiles/cdifCompositeProfile/DiscoveryDataDescriptionStructure/context.jsonld",
    {
      "schema": "http://schema.org/",
      "dcterms": "http://purl.org/dc/terms/",
      "dcat": "http://www.w3.org/ns/dcat#",
      "prov": "http://www.w3.org/ns/prov#",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "cdif": "https://cdif.org/0.1/",
      "csvw": "http://www.w3.org/ns/csvw#",
      "xsd": "http://www.w3.org/2001/XMLSchema#",
      "ex": "https://example.org/"
    }
  ],
  "@id": "ex:dataset/vitalsLong",
  "@type": [
    "schema:Dataset"
  ],
  "schema:name": "Patient vital signs (long-format observations)",
  "schema:description": "Time-series of vital sign measurements (heart rate, systolic BP, diastolic BP, temperature) in long format: one row per observation with a descriptor column naming the measure and a reference column holding the value.",
  "schema:identifier": "https://doi.org/10.1234/vitals-long-2025",
  "schema:dateModified": "2025-09-15",
  "schema:license": [
    "https://creativecommons.org/licenses/by/4.0/"
  ],
  "schema:additionalType": [
    "https://www.wikidata.org/wiki/Q47652734"
  ],
  "schema:sameAs": [
    {
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": "urn:noaa-ghcnd:station-id",
      "schema:value": "DEMO-LONG-2025",
      "schema:url": "https://example.org/aliases/DEMO-LONG-2025"
    }
  ],
  "schema:version": "1.0",
  "schema:url": "https://example.org/datasets/vitals-long-2025",
  "schema:inLanguage": "en",
  "schema:datePublished": "2025-10-01",
  "schema:conditionsOfAccess": [
    "Open access; no registration required."
  ],
  "schema:keywords": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:name": "Vital signs",
      "schema:termCode": "VS",
      "schema:identifier": {
        "@type": [
          "schema:PropertyValue"
        ],
        "schema:propertyID": "https://loinc.org/",
        "schema:value": "VS",
        "schema:url": "https://loinc.org/8716-3/"
      },
      "schema:inDefinedTermSet": "https://loinc.org/"
    },
    "patient monitoring",
    "long format"
  ],
  "schema:relatedLink": [
    {
      "@type": [
        "schema:LinkRole"
      ],
      "schema:linkRelationship": "describedby",
      "schema:target": {
        "@type": [
          "schema:EntryPoint"
        ],
        "schema:name": "Long-format encoding rationale",
        "schema:url": "https://example.org/docs/long-vs-wide.html",
        "schema:encodingFormat": "text/html"
      }
    }
  ],
  "schema:publishingPrinciples": [
    {
      "@type": [
        "schema:CreativeWork",
        "dcat:Relationship"
      ],
      "schema:name": "FAIR data policy",
      "schema:url": "https://example.org/policy/fair-policy.html",
      "schema:description": "Institutional FAIR data policy."
    }
  ],
  "schema:creator": {
    "@list": [
      {
        "@id": "https://orcid.org/0000-0002-7933-2154",
        "@type": [
          "schema:Person"
        ],
        "schema:name": "Richard, Stephen M.",
        "schema:identifier": {
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": "https://orcid.org",
          "schema:value": "0000-0002-7933-2154",
          "schema:url": "https://orcid.org/0000-0002-7933-2154"
        },
        "schema:contactPoint": {
          "@type": [
            "schema:ContactPoint"
          ],
          "schema:email": "smr@example.org"
        }
      }
    ]
  },
  "schema:contributor": [
    {
      "@type": [
        "schema:Role"
      ],
      "schema:roleName": {
        "@type": [
          "schema:DefinedTerm"
        ],
        "schema:name": "Curator",
        "schema:termCode": "data-curation",
        "schema:identifier": {
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": "https://credit.niso.org/",
          "schema:value": "data-curation",
          "schema:url": "https://credit.niso.org/contributor-roles/data-curation/"
        },
        "schema:inDefinedTermSet": "https://credit.niso.org/"
      },
      "schema:contributor": {
        "@id": "https://orcid.org/0000-0001-8898-3457",
        "@type": [
          "schema:Person"
        ],
        "schema:name": "Mojarro, Angel",
        "schema:identifier": {
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": "https://orcid.org",
          "schema:value": "0000-0001-8898-3457",
          "schema:url": "https://orcid.org/0000-0001-8898-3457"
        }
      }
    }
  ],
  "schema:publisher": {
    "@id": "https://ror.org/0171mag52",
    "@type": [
      "schema:Organization"
    ],
    "schema:name": "Demo Health Data Repository",
    "schema:identifier": {
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": "https://ror.org",
      "schema:value": "0171mag52",
      "schema:url": "https://ror.org/0171mag52"
    }
  },
  "schema:provider": [
    {
      "@id": "https://ror.org/0171mag52",
      "@type": [
        "schema:Organization"
      ],
      "schema:name": "Demo Health Data Repository",
      "schema:identifier": {
        "@type": [
          "schema:PropertyValue"
        ],
        "schema:propertyID": "https://ror.org",
        "schema:value": "0171mag52",
        "schema:url": "https://ror.org/0171mag52"
      }
    }
  ],
  "schema:funding": [
    {
      "@type": [
        "schema:MonetaryGrant"
      ],
      "@id": "ex:grant/nih-R01-XXXX",
      "schema:identifier": {
        "@type": [
          "schema:PropertyValue"
        ],
        "schema:propertyID": "https://reporter.nih.gov",
        "schema:value": "R01-XXXX",
        "schema:url": "https://reporter.nih.gov/search/?term=R01-XXXX"
      },
      "schema:name": "NIH Award R01-XXXX",
      "schema:funder": {
        "@id": "https://ror.org/01cwqze88",
        "@type": [
          "schema:Organization"
        ],
        "schema:name": "National Institutes of Health",
        "schema:identifier": {
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": "https://ror.org",
          "schema:value": "01cwqze88",
          "schema:url": "https://ror.org/01cwqze88"
        }
      }
    }
  ],
  "schema:variableMeasured": [
    {
      "@id": "ex:var/patientId",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "patient_id",
      "cdif:physicalDataType": "xsd:string",
      "cdif:uses": [
        {
          "@id": "ex:struct/vitalsLong/rv/patientId"
        }
      ]
    },
    {
      "@id": "ex:var/measureName",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "measure_name",
      "cdif:physicalDataType": "xsd:string",
      "cdif:uses": [
        {
          "@id": "ex:struct/vitalsLong/dv/measureName"
        }
      ]
    },
    {
      "@id": "ex:var/measureValue",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "measure_value",
      "cdif:physicalDataType": "xsd:decimal",
      "cdif:uses": [
        {
          "@id": "ex:struct/vitalsLong/rv/measureValue"
        }
      ]
    },
    {
      "@id": "ex:var/observedAt",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "observed_at",
      "cdif:physicalDataType": "xsd:dateTime",
      "cdif:uses": [
        {
          "@id": "ex:struct/vitalsLong/rv/observedAt"
        }
      ]
    }
  ],
  "cdif:hasPrimaryKey": {
    "@type": [
      "cdif:Key"
    ],
    "@id": "ex:dataset/vitalsLong/pk",
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
  },
  "schema:distribution": [
    {
      "@type": [
        "schema:DataDownload",
        "cdi:TabularTextDataSet",
        "cdi:PhysicalDataSet"
      ],
      "schema:name": "vitals-long.csv",
      "schema:contentUrl": "https://example.org/downloads/vitals-long.csv",
      "schema:encodingFormat": [
        "text/csv"
      ],
      "cdi:characterSet": "UTF-8",
      "cdif:fileSize": 2.4,
      "cdif:fileSizeUofM": "MB",
      "cdi:isDelimited": true,
      "csvw:delimiter": ",",
      "csvw:header": true,
      "csvw:headerRowCount": 1,
      "cdif:hasPhysicalMapping": [
        {
          "cdif:index": 0,
          "cdif:format": "string",
          "cdif:physicalDataType": "string",
          "cdif:formats_InstanceVariable": {
            "@id": "ex:var/patientId"
          }
        },
        {
          "cdif:index": 1,
          "cdif:format": "string",
          "cdif:physicalDataType": "string",
          "cdif:formats_InstanceVariable": {
            "@id": "ex:var/measureName"
          }
        },
        {
          "cdif:index": 2,
          "cdif:format": "decimal",
          "cdif:physicalDataType": "decimal",
          "cdif:formats_InstanceVariable": {
            "@id": "ex:var/measureValue"
          }
        },
        {
          "cdif:index": 3,
          "cdif:format": "ISO8601",
          "cdif:physicalDataType": "dateTime",
          "cdif:formats_InstanceVariable": {
            "@id": "ex:var/observedAt"
          }
        }
      ],
      "cdi:isStructuredBy": {
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
              "cdif:definition": "Pseudonymous patient identifier.",
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
                    "cdif:value": "systolic_bp",
                    "cdif:isDefinedBy": {
                      "@type": [
                        "cdi:RepresentedVariable"
                      ],
                      "@id": "ex:struct/vitalsLong/rv/systolicBP",
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
                      "@id": "ex:struct/vitalsLong/rv/diastolicBP",
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
                      "@type": [
                        "cdi:RepresentedVariable"
                      ],
                      "@id": "ex:struct/vitalsLong/rv/heartRate",
                      "cdif:name": [
                        "heart_rate"
                      ],
                      "cdi:simpleUnitOfMeasure": "bpm",
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
                    "cdif:value": "temp_c",
                    "cdif:isDefinedBy": {
                      "@type": [
                        "cdi:RepresentedVariable"
                      ],
                      "@id": "ex:struct/vitalsLong/rv/temperatureC",
                      "cdif:name": [
                        "body_temperature_celsius"
                      ],
                      "cdi:simpleUnitOfMeasure": "Cel",
                      "cdi:hasIntendedDataType": {
                        "@type": [
                          "cdi:ControlledVocabularyEntry"
                        ],
                        "cdi:entryValue": [
                          "xsd:decimal"
                        ]
                      }
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
              "cdif:definition": "Numeric value of the vital sign named by measure_name.",
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
              "cdif:definition": "Timestamp of the observation; qualifies measure_value.",
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
    },
    {
      "@type": [
        "schema:WebAPI"
      ],
      "schema:name": "Vitals query API",
      "schema:serviceType": {
        "@type": [
          "schema:DefinedTerm"
        ],
        "schema:name": "OGC API - Features",
        "schema:identifier": "https://www.ogc.org/standard/ogcapi-features/",
        "schema:termCode": "ogcapi-features"
      },
      "schema:termsOfService": "Open access, no authentication required.",
      "schema:documentation": {
        "@type": [
          "schema:CreativeWork",
          "dcat:Relationship"
        ],
        "schema:name": "OpenAPI specification for vitals service",
        "schema:url": "https://example.org/api/v1/openapi.json"
      },
      "schema:potentialAction": [
        {
          "@type": [
            "schema:Action"
          ],
          "schema:name": "Query vitals as long-format CSV",
          "schema:target": {
            "@type": [
              "schema:EntryPoint"
            ],
            "schema:description": "OGC API Features endpoint returning vitals observations as long-format CSV.",
            "schema:urlTemplate": "https://example.org/api/v1/collections/vitals/items?f={format}&limit={limit}&offset={offset}",
            "schema:httpMethod": [
              "GET"
            ],
            "schema:contentType": [
              "text/csv"
            ]
          },
          "schema:result": {
            "@type": [
              "schema:DataDownload",
              "cdi:TabularTextDataSet",
              "cdi:PhysicalDataSet"
            ],
            "schema:name": "Vitals API response (long format)",
            "schema:contentUrl": "https://example.org/api/v1/collections/vitals/items?f=csv",
            "schema:encodingFormat": [
              "text/csv"
            ],
            "cdi:characterSet": "UTF-8",
            "cdif:fileSize": 0.5,
            "cdif:fileSizeUofM": "MB",
            "cdi:isDelimited": true,
            "csvw:delimiter": ",",
            "csvw:header": true,
            "csvw:headerRowCount": 1,
            "cdif:hasPhysicalMapping": [
              {
                "cdif:index": 0,
                "cdif:format": "string",
                "cdif:physicalDataType": "string",
                "cdif:formats_InstanceVariable": {
                  "@id": "ex:var/patientId"
                }
              },
              {
                "cdif:index": 1,
                "cdif:format": "string",
                "cdif:physicalDataType": "string",
                "cdif:formats_InstanceVariable": {
                  "@id": "ex:var/measureName"
                }
              },
              {
                "cdif:index": 2,
                "cdif:format": "decimal",
                "cdif:physicalDataType": "decimal",
                "cdif:formats_InstanceVariable": {
                  "@id": "ex:var/measureValue"
                }
              },
              {
                "cdif:index": 3,
                "cdif:format": "ISO8601",
                "cdif:physicalDataType": "dateTime",
                "cdif:formats_InstanceVariable": {
                  "@id": "ex:var/observedAt"
                }
              }
            ],
            "cdi:isStructuredBy": {
              "@id": "ex:struct/vitalsLong"
            }
          },
          "schema:query-input": [
            {
              "@type": [
                "schema:PropertyValueSpecification"
              ],
              "schema:valueName": "format",
              "schema:description": "Response format token (csv only for this example).",
              "schema:valueRequired": false,
              "schema:valuePattern": "csv"
            },
            {
              "@type": [
                "schema:PropertyValueSpecification"
              ],
              "schema:valueName": "limit",
              "schema:description": "Maximum number of observations to return (default 100).",
              "schema:valueRequired": false
            },
            {
              "@type": [
                "schema:PropertyValueSpecification"
              ],
              "schema:valueName": "offset",
              "schema:description": "Starting index for pagination.",
              "schema:valueRequired": false
            }
          ]
        }
      ]
    }
  ],
  "prov:wasGeneratedBy": [
    {
      "@type": [
        "prov:Activity"
      ],
      "@id": "ex:act/vitals-aggregation",
      "prov:used": [
        {
          "@id": "ex:tool/vitals-aggregator"
        }
      ]
    }
  ],
  "prov:wasDerivedFrom": [
    {
      "@type": [
        "schema:CreativeWork",
        "dcat:Relationship"
      ],
      "schema:name": "EHR clinical encounters export, 2024-2025",
      "schema:url": "https://example.org/sources/clinical-encounters-2024-2025",
      "schema:description": "Source EHR system from which the long-format observations were derived."
    }
  ],
  "cdif:statistics": [
    {
      "@type": [
        "cdi:Statistics"
      ],
      "cdi:typeOfStatistic": {
        "@type": [
          "schema:DefinedTerm"
        ],
        "schema:name": "Count",
        "schema:termCode": "count",
        "schema:inDefinedTermSet": "https://ddialliance.org/vocab/statistic-types"
      },
      "cdi:statistic": [
        {
          "cdi:computationBase": "Total",
          "cdi:content": 12450,
          "cdi:typeOfNumericValue": "decimal"
        }
      ]
    }
  ],
  "schema:subjectOf": {
    "@id": "ex:dataset/vitalsLong/metadata",
    "@type": [
      "schema:Dataset"
    ],
    "schema:additionalType": [
      "dcat:CatalogRecord"
    ],
    "schema:about": {
      "@id": "ex:dataset/vitalsLong"
    },
    "dcterms:conformsTo": [
      {
        "@id": "https://w3id.org/cdif/core/1.1"
      },
      {
        "@id": "https://w3id.org/cdif/data_description/1.1"
      },
      {
        "@id": "https://w3id.org/cdif/data_structure/1.1"
      },
      {
        "@id": "https://w3id.org/cdif/discovery/1.1"
      }
    ]
  }
}
```

#### ttl
```ttl
@prefix cdi: <http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/> .
@prefix cdif: <https://cdif.org/0.1/> .
@prefix csvw: <http://www.w3.org/ns/csvw#> .
@prefix dcat: <http://www.w3.org/ns/dcat#> .
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<https://example.org/act/vitals-aggregation> a prov:Activity ;
    prov:used <https://example.org/tool/vitals-aggregator> .

<https://example.org/dataset/vitalsLong> a schema1:Dataset ;
    schema1:additionalType "https://www.wikidata.org/wiki/Q47652734" ;
    schema1:conditionsOfAccess "Open access; no registration required." ;
    schema1:contributor [ a schema1:Role ;
            schema1:contributor <https://orcid.org/0000-0001-8898-3457> ;
            schema1:roleName [ a schema1:DefinedTerm ;
                    schema1:identifier [ a schema1:PropertyValue ;
                            schema1:propertyID "https://credit.niso.org/" ;
                            schema1:url "https://credit.niso.org/contributor-roles/data-curation/" ;
                            schema1:value "data-curation" ] ;
                    schema1:inDefinedTermSet "https://credit.niso.org/" ;
                    schema1:name "Curator" ;
                    schema1:termCode "data-curation" ] ] ;
    schema1:creator ( <https://orcid.org/0000-0002-7933-2154> ) ;
    schema1:dateModified "2025-09-15" ;
    schema1:datePublished "2025-10-01" ;
    schema1:description "Time-series of vital sign measurements (heart rate, systolic BP, diastolic BP, temperature) in long format: one row per observation with a descriptor column naming the measure and a reference column holding the value." ;
    schema1:distribution [ a schema1:WebAPI ;
            schema1:documentation [ a schema1:CreativeWork,
                        dcat:Relationship ;
                    schema1:name "OpenAPI specification for vitals service" ;
                    schema1:url "https://example.org/api/v1/openapi.json" ] ;
            schema1:name "Vitals query API" ;
            schema1:potentialAction [ a schema1:Action ;
                    schema1:name "Query vitals as long-format CSV" ;
                    schema1:query-input [ a schema1:PropertyValueSpecification ;
                            schema1:description "Response format token (csv only for this example)." ;
                            schema1:valueName "format" ;
                            schema1:valuePattern "csv" ;
                            schema1:valueRequired false ],
                        [ a schema1:PropertyValueSpecification ;
                            schema1:description "Maximum number of observations to return (default 100)." ;
                            schema1:valueName "limit" ;
                            schema1:valueRequired false ],
                        [ a schema1:PropertyValueSpecification ;
                            schema1:description "Starting index for pagination." ;
                            schema1:valueName "offset" ;
                            schema1:valueRequired false ] ;
                    schema1:result [ a cdi:PhysicalDataSet,
                                cdi:TabularTextDataSet,
                                schema1:DataDownload ;
                            cdi:characterSet "UTF-8" ;
                            cdi:isDelimited true ;
                            cdi:isStructuredBy <https://example.org/struct/vitalsLong> ;
                            schema1:contentUrl "https://example.org/api/v1/collections/vitals/items?f=csv" ;
                            schema1:encodingFormat "text/csv" ;
                            schema1:name "Vitals API response (long format)" ;
                            csvw:delimiter "," ;
                            csvw:header true ;
                            csvw:headerRowCount 1 ;
                            cdif:fileSize 5e-01 ;
                            cdif:fileSizeUofM "MB" ;
                            cdif:hasPhysicalMapping [ cdif:format "string" ;
                                    cdif:formats_InstanceVariable <https://example.org/var/measureName> ;
                                    cdif:index 1 ;
                                    cdif:physicalDataType "string" ],
                                [ cdif:format "string" ;
                                    cdif:formats_InstanceVariable <https://example.org/var/patientId> ;
                                    cdif:index 0 ;
                                    cdif:physicalDataType "string" ],
                                [ cdif:format "decimal" ;
                                    cdif:formats_InstanceVariable <https://example.org/var/measureValue> ;
                                    cdif:index 2 ;
                                    cdif:physicalDataType "decimal" ],
                                [ cdif:format "ISO8601" ;
                                    cdif:formats_InstanceVariable <https://example.org/var/observedAt> ;
                                    cdif:index 3 ;
                                    cdif:physicalDataType "dateTime" ] ] ;
                    schema1:target [ a schema1:EntryPoint ;
                            schema1:contentType "text/csv" ;
                            schema1:description "OGC API Features endpoint returning vitals observations as long-format CSV." ;
                            schema1:httpMethod "GET" ;
                            schema1:urlTemplate "https://example.org/api/v1/collections/vitals/items?f={format}&limit={limit}&offset={offset}" ] ] ;
            schema1:serviceType [ a schema1:DefinedTerm ;
                    schema1:identifier "https://www.ogc.org/standard/ogcapi-features/" ;
                    schema1:name "OGC API - Features" ;
                    schema1:termCode "ogcapi-features" ] ;
            schema1:termsOfService "Open access, no authentication required." ],
        [ a cdi:PhysicalDataSet,
                cdi:TabularTextDataSet,
                schema1:DataDownload ;
            cdi:characterSet "UTF-8" ;
            cdi:isDelimited true ;
            cdi:isStructuredBy <https://example.org/struct/vitalsLong> ;
            schema1:contentUrl "https://example.org/downloads/vitals-long.csv" ;
            schema1:encodingFormat "text/csv" ;
            schema1:name "vitals-long.csv" ;
            csvw:delimiter "," ;
            csvw:header true ;
            csvw:headerRowCount 1 ;
            cdif:fileSize 2.4e+00 ;
            cdif:fileSizeUofM "MB" ;
            cdif:hasPhysicalMapping [ cdif:format "string" ;
                    cdif:formats_InstanceVariable <https://example.org/var/measureName> ;
                    cdif:index 1 ;
                    cdif:physicalDataType "string" ],
                [ cdif:format "decimal" ;
                    cdif:formats_InstanceVariable <https://example.org/var/measureValue> ;
                    cdif:index 2 ;
                    cdif:physicalDataType "decimal" ],
                [ cdif:format "string" ;
                    cdif:formats_InstanceVariable <https://example.org/var/patientId> ;
                    cdif:index 0 ;
                    cdif:physicalDataType "string" ],
                [ cdif:format "ISO8601" ;
                    cdif:formats_InstanceVariable <https://example.org/var/observedAt> ;
                    cdif:index 3 ;
                    cdif:physicalDataType "dateTime" ] ] ;
    schema1:funding <https://example.org/grant/nih-R01-XXXX> ;
    schema1:identifier "https://doi.org/10.1234/vitals-long-2025" ;
    schema1:inLanguage "en" ;
    schema1:keywords [ a schema1:DefinedTerm ;
            schema1:identifier [ a schema1:PropertyValue ;
                    schema1:propertyID "https://loinc.org/" ;
                    schema1:url "https://loinc.org/8716-3/" ;
                    schema1:value "VS" ] ;
            schema1:inDefinedTermSet "https://loinc.org/" ;
            schema1:name "Vital signs" ;
            schema1:termCode "VS" ],
        "long format",
        "patient monitoring" ;
    schema1:license "https://creativecommons.org/licenses/by/4.0/" ;
    schema1:name "Patient vital signs (long-format observations)" ;
    schema1:provider <https://ror.org/0171mag52> ;
    schema1:publisher <https://ror.org/0171mag52> ;
    schema1:publishingPrinciples [ a schema1:CreativeWork,
                dcat:Relationship ;
            schema1:description "Institutional FAIR data policy." ;
            schema1:name "FAIR data policy" ;
            schema1:url "https://example.org/policy/fair-policy.html" ] ;
    schema1:relatedLink [ a schema1:LinkRole ;
            schema1:linkRelationship "describedby" ;
            schema1:target [ a schema1:EntryPoint ;
                    schema1:encodingFormat "text/html" ;
                    schema1:name "Long-format encoding rationale" ;
                    schema1:url "https://example.org/docs/long-vs-wide.html" ] ] ;
    schema1:sameAs [ a schema1:PropertyValue ;
            schema1:propertyID "urn:noaa-ghcnd:station-id" ;
            schema1:url "https://example.org/aliases/DEMO-LONG-2025" ;
            schema1:value "DEMO-LONG-2025" ] ;
    schema1:subjectOf <https://example.org/dataset/vitalsLong/metadata> ;
    schema1:url "https://example.org/datasets/vitals-long-2025" ;
    schema1:variableMeasured <https://example.org/var/measureName>,
        <https://example.org/var/measureValue>,
        <https://example.org/var/observedAt>,
        <https://example.org/var/patientId> ;
    schema1:version "1.0" ;
    prov:wasDerivedFrom [ a schema1:CreativeWork,
                dcat:Relationship ;
            schema1:description "Source EHR system from which the long-format observations were derived." ;
            schema1:name "EHR clinical encounters export, 2024-2025" ;
            schema1:url "https://example.org/sources/clinical-encounters-2024-2025" ] ;
    prov:wasGeneratedBy <https://example.org/act/vitals-aggregation> ;
    cdif:hasPrimaryKey <https://example.org/dataset/vitalsLong/pk> ;
    cdif:statistics [ a cdi:Statistics ;
            cdi:statistic [ cdi:computationBase "Total" ;
                    cdi:content 12450 ;
                    cdi:typeOfNumericValue "decimal" ] ;
            cdi:typeOfStatistic [ a schema1:DefinedTerm ;
                    schema1:inDefinedTermSet "https://ddialliance.org/vocab/statistic-types" ;
                    schema1:name "Count" ;
                    schema1:termCode "count" ] ] .

<https://example.org/dataset/vitalsLong/metadata> a schema1:Dataset ;
    dcterms:conformsTo <https://w3id.org/cdif/core/1.1>,
        <https://w3id.org/cdif/data_description/1.1>,
        <https://w3id.org/cdif/data_structure/1.1>,
        <https://w3id.org/cdif/discovery/1.1> ;
    schema1:about <https://example.org/dataset/vitalsLong> ;
    schema1:additionalType "dcat:CatalogRecord" .

<https://example.org/dataset/vitalsLong/pk> a cdif:Key ;
    cdif:isComposedOf <https://example.org/var/measureName>,
        <https://example.org/var/observedAt>,
        <https://example.org/var/patientId> .

<https://example.org/grant/nih-R01-XXXX> a schema1:MonetaryGrant ;
    schema1:funder <https://ror.org/01cwqze88> ;
    schema1:identifier [ a schema1:PropertyValue ;
            schema1:propertyID "https://reporter.nih.gov" ;
            schema1:url "https://reporter.nih.gov/search/?term=R01-XXXX" ;
            schema1:value "R01-XXXX" ] ;
    schema1:name "NIH Award R01-XXXX" .

<https://example.org/struct/vitalsLong/comp/measureName> a cdi:VariableDescriptorComponent ;
    cdi:refersTo <https://example.org/struct/vitalsLong/comp/measureValue> ;
    cdif:isDefinedBy_DescriptorVariable <https://example.org/struct/vitalsLong/dv/measureName> .

<https://example.org/struct/vitalsLong/comp/observedAt> a cdi:AttributeComponent ;
    cdi:qualifies <https://example.org/struct/vitalsLong/comp/measureValue> ;
    cdif:isDefinedBy_RepresentedVariable <https://example.org/struct/vitalsLong/rv/observedAt> .

<https://example.org/struct/vitalsLong/comp/patientId> a cdi:IdentifierComponent ;
    cdif:isDefinedBy_RepresentedVariable <https://example.org/struct/vitalsLong/rv/patientId> .

<https://example.org/struct/vitalsLong/pk> a cdif:PrimaryKey ;
    cdif:isComposedOf <https://example.org/var/measureName>,
        <https://example.org/var/observedAt>,
        <https://example.org/var/patientId> .

<https://example.org/struct/vitalsLong/rv/diastolicBP> a cdi:RepresentedVariable ;
    cdi:hasIntendedDataType [ a cdi:ControlledVocabularyEntry ;
            cdi:entryValue "xsd:decimal" ] ;
    cdi:simpleUnitOfMeasure "mmHg" ;
    cdif:name "diastolic_blood_pressure" .

<https://example.org/struct/vitalsLong/rv/heartRate> a cdi:RepresentedVariable ;
    cdi:hasIntendedDataType [ a cdi:ControlledVocabularyEntry ;
            cdi:entryValue "xsd:decimal" ] ;
    cdi:simpleUnitOfMeasure "bpm" ;
    cdif:name "heart_rate" .

<https://example.org/struct/vitalsLong/rv/systolicBP> a cdi:RepresentedVariable ;
    cdi:hasIntendedDataType [ a cdi:ControlledVocabularyEntry ;
            cdi:entryValue "xsd:decimal" ] ;
    cdi:simpleUnitOfMeasure "mmHg" ;
    cdif:name "systolic_blood_pressure" .

<https://example.org/struct/vitalsLong/rv/temperatureC> a cdi:RepresentedVariable ;
    cdi:hasIntendedDataType [ a cdi:ControlledVocabularyEntry ;
            cdi:entryValue "xsd:decimal" ] ;
    cdi:simpleUnitOfMeasure "Cel" ;
    cdif:name "body_temperature_celsius" .

<https://example.org/struct/vitalsLong/vd/measureName> a cdi:DescriptorValueDomain ;
    cdif:takesValuesFrom [ cdif:isDefinedBy <https://example.org/struct/vitalsLong/rv/temperatureC> ;
            cdif:value "temp_c" ],
        [ cdif:isDefinedBy <https://example.org/struct/vitalsLong/rv/systolicBP> ;
            cdif:value "systolic_bp" ],
        [ cdif:isDefinedBy <https://example.org/struct/vitalsLong/rv/heartRate> ;
            cdif:value "heart_rate" ],
        [ cdif:isDefinedBy <https://example.org/struct/vitalsLong/rv/diastolicBP> ;
            cdif:value "diastolic_bp" ] .

<https://orcid.org/0000-0001-8898-3457> a schema1:Person ;
    schema1:identifier [ a schema1:PropertyValue ;
            schema1:propertyID "https://orcid.org" ;
            schema1:url "https://orcid.org/0000-0001-8898-3457" ;
            schema1:value "0000-0001-8898-3457" ] ;
    schema1:name "Mojarro, Angel" .

<https://orcid.org/0000-0002-7933-2154> a schema1:Person ;
    schema1:contactPoint [ a schema1:ContactPoint ;
            schema1:email "smr@example.org" ] ;
    schema1:identifier [ a schema1:PropertyValue ;
            schema1:propertyID "https://orcid.org" ;
            schema1:url "https://orcid.org/0000-0002-7933-2154" ;
            schema1:value "0000-0002-7933-2154" ] ;
    schema1:name "Richard, Stephen M." .

<https://ror.org/01cwqze88> a schema1:Organization ;
    schema1:identifier [ a schema1:PropertyValue ;
            schema1:propertyID "https://ror.org" ;
            schema1:url "https://ror.org/01cwqze88" ;
            schema1:value "01cwqze88" ] ;
    schema1:name "National Institutes of Health" .

<https://example.org/struct/vitalsLong> a cdi:LongDataStructure ;
    cdi:has_DataStructureComponent <https://example.org/struct/vitalsLong/comp/measureName>,
        <https://example.org/struct/vitalsLong/comp/measureValue>,
        <https://example.org/struct/vitalsLong/comp/observedAt>,
        <https://example.org/struct/vitalsLong/comp/patientId> ;
    cdi:has_PrimaryKey <https://example.org/struct/vitalsLong/pk> .

<https://example.org/struct/vitalsLong/dv/measureName> a cdi:DescriptorVariable ;
    cdif:hasValuesFrom <https://example.org/struct/vitalsLong/vd/measureName> ;
    cdif:name "measure_name" .

<https://example.org/struct/vitalsLong/rv/measureValue> a cdi:RepresentedVariable ;
    cdi:hasIntendedDataType [ a cdi:ControlledVocabularyEntry ;
            cdi:entryValue "xsd:decimal" ] ;
    cdif:definition "Numeric value of the vital sign named by measure_name." ;
    cdif:name "measure_value" .

<https://example.org/struct/vitalsLong/rv/observedAt> a cdi:RepresentedVariable ;
    cdi:hasIntendedDataType [ a cdi:ControlledVocabularyEntry ;
            cdi:entryValue "xsd:dateTime" ] ;
    cdif:definition "Timestamp of the observation; qualifies measure_value." ;
    cdif:name "observed_at" .

<https://example.org/struct/vitalsLong/rv/patientId> a cdi:RepresentedVariable ;
    cdi:hasIntendedDataType [ a cdi:ControlledVocabularyEntry ;
            cdi:entryValue "xsd:string" ] ;
    cdif:definition "Pseudonymous patient identifier." ;
    cdif:name "patient_id" .

<https://ror.org/0171mag52> a schema1:Organization ;
    schema1:identifier [ a schema1:PropertyValue ;
            schema1:propertyID "https://ror.org" ;
            schema1:url "https://ror.org/0171mag52" ;
            schema1:value "0171mag52" ],
        [ a schema1:PropertyValue ;
            schema1:propertyID "https://ror.org" ;
            schema1:url "https://ror.org/0171mag52" ;
            schema1:value "0171mag52" ] ;
    schema1:name "Demo Health Data Repository" .

<https://example.org/struct/vitalsLong/comp/measureValue> a cdi:VariableValueComponent ;
    cdif:isDefinedBy_RepresentedVariable <https://example.org/struct/vitalsLong/rv/measureValue> .

<https://example.org/var/measureValue> a cdi:InstanceVariable,
        schema1:PropertyValue ;
    schema1:name "measure_value" ;
    cdif:physicalDataType "xsd:decimal" ;
    cdif:uses <https://example.org/struct/vitalsLong/rv/measureValue> .

<https://example.org/var/measureName> a cdi:InstanceVariable,
        schema1:PropertyValue ;
    schema1:name "measure_name" ;
    cdif:physicalDataType "xsd:string" ;
    cdif:uses <https://example.org/struct/vitalsLong/dv/measureName> .

<https://example.org/var/observedAt> a cdi:InstanceVariable,
        schema1:PropertyValue ;
    schema1:name "observed_at" ;
    cdif:physicalDataType "xsd:dateTime" ;
    cdif:uses <https://example.org/struct/vitalsLong/rv/observedAt> .

<https://example.org/var/patientId> a cdi:InstanceVariable,
        schema1:PropertyValue ;
    schema1:name "patient_id" ;
    cdif:physicalDataType "xsd:string" ;
    cdif:uses <https://example.org/struct/vitalsLong/rv/patientId> .


```

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
- $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/profiles/cdifProfile/cdifCore/schema.yaml
- $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/profiles/cdifProfile/cdifDiscovery/schema.yaml
- $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/profiles/cdifProfile/cdifDataDescription/schema.yaml
- $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/profiles/cdifProfile/cdifDataStructure/schema.yaml

```

Links to the schema:

* YAML version: [schema.yaml](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/profiles/cdifCompositeProfile/DiscoveryDataDescriptionStructure/schema.json)
* JSON version: [schema.json](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/profiles/cdifCompositeProfile/DiscoveryDataDescriptionStructure/schema.yaml)


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
    "prov": "http://www.w3.org/ns/prov#",
    "time": "http://www.w3.org/2006/time#",
    "spdx": "http://spdx.org/rdf/terms#",
    "xas": "https://xas.org/dictionary/",
    "nxs": "http://purl.org/nexusformat/definitions/",
    "ada": "https://ada.astromat.org/metadata/",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/profiles/cdifCompositeProfile/DiscoveryDataDescriptionStructure/context.jsonld)

## Sources

* [DDI-CDI 1.0 Specification](https://ddialliance.org/Specification/DDI-CDI/1.0/)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/Cross-Domain-Interoperability-Framework/metadataBuildingBlocks](https://github.com/Cross-Domain-Interoperability-Framework/metadataBuildingBlocks)
* Path: `_sources/profiles/cdifCompositeProfile/DiscoveryDataDescriptionStructure`

