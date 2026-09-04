
# CDIF Instance Variable (Schema)

`cdif.bbr.metadata.cdifDataType.cdifInstanceVariable` *v0.2*

Profile of cdi:InstanceVariable / schema:PropertyValue used as a member of a schema:variableMeasured array. Adds DDI-CDI properties (cdif:physicalDataType, cdif:role, cdif:simpleUnitOfMeasure, cdif:uses, cdi:qualifies) on top of schemaorgProperties/variableMeasured and ddiProperties/ddicdiInstanceVariable. Accepts a single node, an unwrapped @graph array of nodes (OGC pipeline), or a JSON-LD document with @context and @graph.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

## CDIF Instance Variable

Profile of `cdi:InstanceVariable` / `schema:PropertyValue` for use as a member of a `schema:variableMeasured` array. Composes the base [variableMeasured](../../schemaorgProperties/variableMeasured/) building block with the DDI-CDI properties of `InstanceVariable` and its `RepresentedVariable` superclass.

The BB accepts three shapes interchangeably:

1. a single CDIF Instance Variable node;
2. an unwrapped array of such nodes (OGC pipeline `@graph` form);
3. a full JSON-LD document with `@context` and `@graph`.

### Property scope

The schema carries **all `InstanceVariable`-own and `RepresentedVariable`-own properties** from the DDI-CDI class hierarchy (`ConceptualVariable → RepresentedVariable → InstanceVariable`). Properties inherited from `ConceptualVariable` and above (`descriptiveText`, `unitOfMeasureKind`, `definition`, `displayLabel`, `name`, `measures`, `takesSentinel/SubstantiveConceptsFrom`, `uses`-as-Concept, …) are **not** included — the conceptual layer is described separately.

**InstanceVariable-own:**

- **@type** — must include `cdi:InstanceVariable` (and, as a `schema:PropertyValue`, that type too)
- **cdif:physicalDataType** — physical data type concept (string, URI reference, or DefinedTerm)
- **cdif:role** — role in a data structure (`UnitIdentifier`, `Measure`, `Attribute`, `Dimension`, `Descriptor`, `ReferenceVariable`)
- **cdi:function** — immutable characteristic (geographic designator, weight, temporal designation, …)
- **cdi:platformType** — application / technical system context the variable was realized in
- **cdi:source** — provenance reference
- **cdif:isDescribedBy_StatisticsCollection** — the `StatisticsCollection` of summary / category statistics for this variable (target-suffixed: `isDescribedBy` is polymorphic in DDI-CDI)

**RepresentedVariable-own:**

- **cdi:hasIntendedDataType** — intended data type, independent of physical representation
- **cdi:describedUnitOfMeasure** — unit of measure as a controlled-vocabulary entry
- **cdif:simpleUnitOfMeasure** — unit of measure as a plain string / URI / DefinedTerm
- **cdi:takesSentinelValuesFrom** — sentinel (missing / not-applicable) value domain(s) — `cdifValueDomain`
- **cdi:takesSubstantiveValuesFrom** — substantive value domain — `cdifValueDomain`

**CDIF extensions:**

- **cdif:uses** — concepts (or, under the Data Structure profile, the `RepresentedVariable`) that this variable represents
- **cdi:qualifies** — `@id` reference to another instance variable; used when `cdif:role` is `Attribute`

### Data Structure profile constraint

When a dataset's distribution carries `cdi:isStructuredBy` (CDIF **Data Structure** profile), the `RepresentedVariable`-own properties above live on the referenced `RepresentedVariable` and are reached from the InstanceVariable via `cdif:uses` — they must **not** be duplicated on the InstanceVariable. The Data Structure profile disallows them on `schema:variableMeasured` items for that reason. In the plain **Data Description** profile (no `cdi:isStructuredBy`), they may be carried directly on the InstanceVariable.

### Dependencies

- [variableMeasured](../../schemaorgProperties/variableMeasured/) — base variable measured properties
- [cdifValueDomain](../cdifValueDomain/) — substantive / sentinel value domains
- [cdifStatistics](../cdifStatistics/) — `StatisticsCollection` target of `cdif:isDescribedBy_StatisticsCollection`
- [definedTerm](../../schemaorgProperties/definedTerm/) — controlled vocabulary term

## Examples

### Minimal CDIF Instance Variable
Single PropertyValue + cdi:InstanceVariable node with the four
properties required by the CdifInstanceVariableNode shape (which
inherits ddicdiInstanceVariable's required list): @type, cdi:name,
cdi:definition, cdi:takesSubstantiveValuesFrom.
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
    "ex": "https://example.org/",
    "cdif": "https://w3id.org/cdif/"
  },
  "@type": [
    "cdi:InstanceVariable",
    "schema:PropertyValue"
  ],
  "@id": "ex:var/temperature",
  "schema:name": "temperature",
  "cdif:name": [
    "temperature"
  ],
  "cdif:definition": "Air temperature measurement.",
  "cdi:takesSubstantiveValuesFrom": {
    "@id": "ex:value-domain/decimal"
  }
}

```

#### jsonld
```jsonld
{
  "@context": [
    {
      "schema": "http://schema.org/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/"
    },
    "https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifDataType/cdifInstanceVariable/context.jsonld",
    {
      "schema": "http://schema.org/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "ex": "https://example.org/",
      "cdif": "https://w3id.org/cdif/"
    }
  ],
  "@type": [
    "cdi:InstanceVariable",
    "schema:PropertyValue"
  ],
  "@id": "ex:var/temperature",
  "schema:name": "temperature",
  "cdif:name": [
    "temperature"
  ],
  "cdif:definition": "Air temperature measurement.",
  "cdi:takesSubstantiveValuesFrom": {
    "@id": "ex:value-domain/decimal"
  }
}
```

#### ttl
```ttl
@prefix cdi: <http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/> .
@prefix cdif: <https://w3id.org/cdif/> .
@prefix schema1: <http://schema.org/> .

<https://example.org/var/temperature> a cdi:InstanceVariable,
        schema1:PropertyValue ;
    cdi:takesSubstantiveValuesFrom <https://example.org/value-domain/decimal> ;
    schema1:name "temperature" ;
    cdif:definition "Air temperature measurement." ;
    cdif:name "temperature" .


```


### Complete CDIF Instance Variable (XAS)
Implementation of Schema.org PropertyValue as value for variableMeasured
property, adding cdi:InstanceVariable type and several other DDI-CDI
properties. From the X-Ray Absorption profile testing corpus, with two
InstanceVariables in an @graph and a parent schema:Dataset that references
them via schema:variableMeasured.
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "ex": "https://example.org/",
    "xsd": "http://www.w3.org/2001/XMLSchema#",
    "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
    "cdif": "https://w3id.org/cdif/",
    "skos": "http://www.w3.org/2004/02/skos/core#",
    "xas": "https://w3id.org/cdif/xas/"
  },
  "@type": [
    "cdi:InstanceVariable",
    "schema:PropertyValue"
  ],
  "@id": "xas:monochromatorEnergy",
  "schema:name": "energy",
  "schema:alternateName": [
    "Monochromator energy"
  ],
  "schema:description": "Incident photon energy selected by the monochromator during the XAS scan.",
  "schema:propertyID": [
    {
      "@id": "xas:monochromatorEnergyConcept"
    }
  ],
  "schema:unitText": "eV",
  "cdi:identifier": {
    "@type": [
      "cdi:Identifier"
    ],
    "cdi:uri": "https://w3id.org/cdif/xas/monochromatorEnergy"
  },
  "cdif:name": [
    "energy"
  ],
  "cdif:displayLabel": [
    "Monochromator energy"
  ],
  "cdif:definition": "Incident photon energy selected by the monochromator during the XAS scan.",
  "cdif:physicalDataType": "xsd:decimal",
  "cdi:takesSubstantiveValuesFrom": {
    "@id": "ex:value-domain/decimal-eV"
  },
  "cdif:simpleUnitOfMeasure": "eV",
  "cdif:uses": [
    "xas:monochromatorEnergyConcept"
  ],
  "cdif:role": "Attribute",
  "cdi:qualifies": {
    "@id": "ex:temperatureVariable"
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
      "xas": "https://w3id.org/cdif/xas/",
      "skos": "http://www.w3.org/2004/02/skos/core#"
    },
    "https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifDataType/cdifInstanceVariable/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ex": "https://example.org/",
      "xsd": "http://www.w3.org/2001/XMLSchema#",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "cdif": "https://w3id.org/cdif/",
      "skos": "http://www.w3.org/2004/02/skos/core#",
      "xas": "https://w3id.org/cdif/xas/"
    }
  ],
  "@type": [
    "cdi:InstanceVariable",
    "schema:PropertyValue"
  ],
  "@id": "xas:monochromatorEnergy",
  "schema:name": "energy",
  "schema:alternateName": [
    "Monochromator energy"
  ],
  "schema:description": "Incident photon energy selected by the monochromator during the XAS scan.",
  "schema:propertyID": [
    {
      "@id": "xas:monochromatorEnergyConcept"
    }
  ],
  "schema:unitText": "eV",
  "cdi:identifier": {
    "@type": [
      "cdi:Identifier"
    ],
    "cdi:uri": "https://w3id.org/cdif/xas/monochromatorEnergy"
  },
  "cdif:name": [
    "energy"
  ],
  "cdif:displayLabel": [
    "Monochromator energy"
  ],
  "cdif:definition": "Incident photon energy selected by the monochromator during the XAS scan.",
  "cdif:physicalDataType": "xsd:decimal",
  "cdi:takesSubstantiveValuesFrom": {
    "@id": "ex:value-domain/decimal-eV"
  },
  "cdif:simpleUnitOfMeasure": "eV",
  "cdif:uses": [
    "xas:monochromatorEnergyConcept"
  ],
  "cdif:role": "Attribute",
  "cdi:qualifies": {
    "@id": "ex:temperatureVariable"
  }
}
```

#### ttl
```ttl
@prefix cdi: <http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/> .
@prefix cdif: <https://w3id.org/cdif/> .
@prefix ex: <https://example.org/> .
@prefix schema1: <http://schema.org/> .
@prefix xas: <https://w3id.org/cdif/xas/> .

xas:monochromatorEnergy a cdi:InstanceVariable,
        schema1:PropertyValue ;
    cdi:identifier [ a cdi:Identifier ;
            cdi:uri "https://w3id.org/cdif/xas/monochromatorEnergy" ] ;
    cdi:qualifies ex:temperatureVariable ;
    cdi:takesSubstantiveValuesFrom <https://example.org/value-domain/decimal-eV> ;
    schema1:alternateName "Monochromator energy" ;
    schema1:description "Incident photon energy selected by the monochromator during the XAS scan." ;
    schema1:name "energy" ;
    schema1:propertyID xas:monochromatorEnergyConcept ;
    schema1:unitText "eV" ;
    cdif:definition "Incident photon energy selected by the monochromator during the XAS scan." ;
    cdif:displayLabel "Monochromator energy" ;
    cdif:name "energy" ;
    cdif:physicalDataType "xsd:decimal" ;
    cdif:role "Attribute" ;
    cdif:simpleUnitOfMeasure "eV" ;
    cdif:uses "xas:monochromatorEnergyConcept" .


```


### CDIF Instance Variable with category statistics (DDI Codebook)
A categorical InstanceVariable exercising cdif:isDescribedBy_StatisticsCollection.
Derived from variable HH14 ("Language of the Questionnaire") of the MWI 2019 MICS
household record (DDI Codebook 2.5). Shows how DDI <catgry>/<catStat>/<sumStat>
map to CDIF: the categories become an enumerated value domain
(cdi:takesSubstantiveValuesFrom -> SubstantiveValueDomain -> EnumerationDomain ->
a skos:ConceptScheme code list), the "Sysmiss" missing category becomes a
SentinelValueDomain, and the summary + per-category frequencies become a
StatisticsCollection of cdi:Statistics (count/min/max, split by
cdi:computationBase) and cdi:CategoryStatistics (one per category, cdi:for
referencing the code-list concept).
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
    "cdif": "https://w3id.org/cdif/",
    "skos": "http://www.w3.org/2004/02/skos/core#",
    "xsd": "http://www.w3.org/2001/XMLSchema#",
    "mics": "https://example.org/mics/mwi2019/"
  },
  "@id": "mics:var/HH14",
  "@type": [
    "cdi:InstanceVariable",
    "schema:PropertyValue"
  ],
  "schema:name": "HH14",
  "schema:description": "Language of the household questionnaire. Categorical variable from the MWI 2019 MICS household record; source DDI Codebook variable HH14. The value domains reference a shared skos:ConceptScheme code list by @id; in a full document that code list is a sibling @graph node (see the cdifCodelist profile). This InstanceVariable declares the value domains directly because it does NOT defer to a RepresentedVariable via cdif:isDefinedBy_RepresentedVariable.",
  "cdif:name": [
    "HH14"
  ],
  "cdif:displayLabel": [
    "Language of the Questionnaire"
  ],
  "cdif:definition": "The language in which the household questionnaire was administered.",
  "cdif:physicalDataType": "xsd:integer",
  "cdif:role": "Measure",

  "cdi:takesSubstantiveValuesFrom": {
    "@id": "mics:var/HH14/valueDomain/substantive",
    "@type": [
      "cdif:SubstantiveValueDomain"
    ],
    "cdif:displayLabel": "Valid language codes for HH14",
    "cdif:takesValuesFrom": {
      "@id": "mics:var/HH14/enumerationDomain",
      "@type": [
        "cdif:EnumerationDomain"
      ],
      "schema:name": "MWI 2019 MICS questionnaire-language codes",
      "cdif:references": {
        "@id": "mics:codelist/HH14-language"
      }
    }
  },

  "cdi:takesSentinelValuesFrom": [
    {
      "@id": "mics:var/HH14/valueDomain/sentinel",
      "@type": [
        "cdif:SentinelValueDomain"
      ],
      "cdif:displayLabel": "Missing-value codes for HH14",
      "cdif:takesValuesFrom": {
        "@id": "mics:var/HH14/sentinelEnumerationDomain",
        "@type": [
          "cdif:EnumerationDomain"
        ],
        "schema:name": "MWI 2019 MICS system-missing code",
        "cdif:references": {
          "@id": "mics:codelist/HH14-missing"
        }
      }
    }
  ],

  "cdif:isDescribedBy_StatisticsCollection": {
    "@id": "mics:var/HH14/statistics",
    "@type": [
      "cdi:StatisticsCollection"
    ],
    "cdif:indexedBy": [
      {
        "@id": "mics:var/HH14"
      }
    ],
    "cdif:has_Statistics": [
      {
        "@id": "mics:var/HH14/statistics/count",
        "@type": [
          "cdi:Statistics"
        ],
        "cdi:typeOfStatistic": "count",
        "cdi:statistic": [
          {
            "cdi:computationBase": "ValidOnly",
            "cdi:content": 25419,
            "cdi:typeOfNumericValue": "decimal"
          },
          {
            "cdi:computationBase": "MissingOnly",
            "cdi:content": 1463,
            "cdi:typeOfNumericValue": "decimal"
          },
          {
            "cdi:computationBase": "Total",
            "cdi:content": 26882,
            "cdi:typeOfNumericValue": "decimal"
          }
        ]
      },
      {
        "@id": "mics:var/HH14/statistics/minimum",
        "@type": [
          "cdi:Statistics"
        ],
        "cdi:typeOfStatistic": "minimum",
        "cdi:statistic": [
          {
            "cdi:computationBase": "ValidOnly",
            "cdi:content": 1,
            "cdi:typeOfNumericValue": "decimal"
          }
        ]
      },
      {
        "@id": "mics:var/HH14/statistics/maximum",
        "@type": [
          "cdi:Statistics"
        ],
        "cdi:typeOfStatistic": "maximum",
        "cdi:statistic": [
          {
            "cdi:computationBase": "ValidOnly",
            "cdi:content": 4,
            "cdi:typeOfNumericValue": "decimal"
          }
        ]
      },
      {
        "@id": "mics:var/HH14/statistics/frequencies",
        "@type": [
          "cdi:Statistics"
        ],
        "cdi:typeOfStatistic": "frequency",
        "cdi:statistic": [
          {
            "cdi:computationBase": "Total",
            "cdi:content": 26882,
            "cdi:typeOfNumericValue": "decimal"
          }
        ],
        "cdif:has_CategoryStatistics": [
          {
            "@type": [
              "cdi:CategoryStatistics"
            ],
            "cdi:for": {
              "@id": "mics:codelist/HH14-language/1"
            },
            "cdi:typeOfStatistic": "frequency",
            "cdi:statistic": [
              {
                "cdi:computationBase": "ValidOnly",
                "cdi:content": 108,
                "cdi:typeOfNumericValue": "decimal"
              }
            ]
          },
          {
            "@type": [
              "cdi:CategoryStatistics"
            ],
            "cdi:for": {
              "@id": "mics:codelist/HH14-language/2"
            },
            "cdi:typeOfStatistic": "frequency",
            "cdi:statistic": [
              {
                "cdi:computationBase": "ValidOnly",
                "cdi:content": 21497,
                "cdi:typeOfNumericValue": "decimal"
              }
            ]
          },
          {
            "@type": [
              "cdi:CategoryStatistics"
            ],
            "cdi:for": {
              "@id": "mics:codelist/HH14-language/3"
            },
            "cdi:typeOfStatistic": "frequency",
            "cdi:statistic": [
              {
                "cdi:computationBase": "ValidOnly",
                "cdi:content": 3739,
                "cdi:typeOfNumericValue": "decimal"
              }
            ]
          },
          {
            "@type": [
              "cdi:CategoryStatistics"
            ],
            "cdi:for": {
              "@id": "mics:codelist/HH14-language/4"
            },
            "cdi:typeOfStatistic": "frequency",
            "cdi:statistic": [
              {
                "cdi:computationBase": "ValidOnly",
                "cdi:content": 75,
                "cdi:typeOfNumericValue": "decimal"
              }
            ]
          },
          {
            "@type": [
              "cdi:CategoryStatistics"
            ],
            "cdi:for": {
              "@id": "mics:codelist/HH14-missing/sysmiss"
            },
            "cdi:typeOfStatistic": "frequency",
            "cdi:statistic": [
              {
                "cdi:computationBase": "MissingOnly",
                "cdi:content": 1463,
                "cdi:typeOfNumericValue": "decimal"
              }
            ]
          }
        ]
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
      "cdif": "https://w3id.org/cdif/",
      "skos": "http://www.w3.org/2004/02/skos/core#",
      "mics": "https://example.org/mics/mwi2019/"
    },
    "https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifDataType/cdifInstanceVariable/context.jsonld",
    {
      "schema": "http://schema.org/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "cdif": "https://w3id.org/cdif/",
      "skos": "http://www.w3.org/2004/02/skos/core#",
      "xsd": "http://www.w3.org/2001/XMLSchema#",
      "mics": "https://example.org/mics/mwi2019/"
    }
  ],
  "@id": "mics:var/HH14",
  "@type": [
    "cdi:InstanceVariable",
    "schema:PropertyValue"
  ],
  "schema:name": "HH14",
  "schema:description": "Language of the household questionnaire. Categorical variable from the MWI 2019 MICS household record; source DDI Codebook variable HH14. The value domains reference a shared skos:ConceptScheme code list by @id; in a full document that code list is a sibling @graph node (see the cdifCodelist profile). This InstanceVariable declares the value domains directly because it does NOT defer to a RepresentedVariable via cdif:isDefinedBy_RepresentedVariable.",
  "cdif:name": [
    "HH14"
  ],
  "cdif:displayLabel": [
    "Language of the Questionnaire"
  ],
  "cdif:definition": "The language in which the household questionnaire was administered.",
  "cdif:physicalDataType": "xsd:integer",
  "cdif:role": "Measure",
  "cdi:takesSubstantiveValuesFrom": {
    "@id": "mics:var/HH14/valueDomain/substantive",
    "@type": [
      "cdif:SubstantiveValueDomain"
    ],
    "cdif:displayLabel": "Valid language codes for HH14",
    "cdif:takesValuesFrom": {
      "@id": "mics:var/HH14/enumerationDomain",
      "@type": [
        "cdif:EnumerationDomain"
      ],
      "schema:name": "MWI 2019 MICS questionnaire-language codes",
      "cdif:references": {
        "@id": "mics:codelist/HH14-language"
      }
    }
  },
  "cdi:takesSentinelValuesFrom": [
    {
      "@id": "mics:var/HH14/valueDomain/sentinel",
      "@type": [
        "cdif:SentinelValueDomain"
      ],
      "cdif:displayLabel": "Missing-value codes for HH14",
      "cdif:takesValuesFrom": {
        "@id": "mics:var/HH14/sentinelEnumerationDomain",
        "@type": [
          "cdif:EnumerationDomain"
        ],
        "schema:name": "MWI 2019 MICS system-missing code",
        "cdif:references": {
          "@id": "mics:codelist/HH14-missing"
        }
      }
    }
  ],
  "cdif:isDescribedBy_StatisticsCollection": {
    "@id": "mics:var/HH14/statistics",
    "@type": [
      "cdi:StatisticsCollection"
    ],
    "cdif:indexedBy": [
      {
        "@id": "mics:var/HH14"
      }
    ],
    "cdif:has_Statistics": [
      {
        "@id": "mics:var/HH14/statistics/count",
        "@type": [
          "cdi:Statistics"
        ],
        "cdi:typeOfStatistic": "count",
        "cdi:statistic": [
          {
            "cdi:computationBase": "ValidOnly",
            "cdi:content": 25419,
            "cdi:typeOfNumericValue": "decimal"
          },
          {
            "cdi:computationBase": "MissingOnly",
            "cdi:content": 1463,
            "cdi:typeOfNumericValue": "decimal"
          },
          {
            "cdi:computationBase": "Total",
            "cdi:content": 26882,
            "cdi:typeOfNumericValue": "decimal"
          }
        ]
      },
      {
        "@id": "mics:var/HH14/statistics/minimum",
        "@type": [
          "cdi:Statistics"
        ],
        "cdi:typeOfStatistic": "minimum",
        "cdi:statistic": [
          {
            "cdi:computationBase": "ValidOnly",
            "cdi:content": 1,
            "cdi:typeOfNumericValue": "decimal"
          }
        ]
      },
      {
        "@id": "mics:var/HH14/statistics/maximum",
        "@type": [
          "cdi:Statistics"
        ],
        "cdi:typeOfStatistic": "maximum",
        "cdi:statistic": [
          {
            "cdi:computationBase": "ValidOnly",
            "cdi:content": 4,
            "cdi:typeOfNumericValue": "decimal"
          }
        ]
      },
      {
        "@id": "mics:var/HH14/statistics/frequencies",
        "@type": [
          "cdi:Statistics"
        ],
        "cdi:typeOfStatistic": "frequency",
        "cdi:statistic": [
          {
            "cdi:computationBase": "Total",
            "cdi:content": 26882,
            "cdi:typeOfNumericValue": "decimal"
          }
        ],
        "cdif:has_CategoryStatistics": [
          {
            "@type": [
              "cdi:CategoryStatistics"
            ],
            "cdi:for": {
              "@id": "mics:codelist/HH14-language/1"
            },
            "cdi:typeOfStatistic": "frequency",
            "cdi:statistic": [
              {
                "cdi:computationBase": "ValidOnly",
                "cdi:content": 108,
                "cdi:typeOfNumericValue": "decimal"
              }
            ]
          },
          {
            "@type": [
              "cdi:CategoryStatistics"
            ],
            "cdi:for": {
              "@id": "mics:codelist/HH14-language/2"
            },
            "cdi:typeOfStatistic": "frequency",
            "cdi:statistic": [
              {
                "cdi:computationBase": "ValidOnly",
                "cdi:content": 21497,
                "cdi:typeOfNumericValue": "decimal"
              }
            ]
          },
          {
            "@type": [
              "cdi:CategoryStatistics"
            ],
            "cdi:for": {
              "@id": "mics:codelist/HH14-language/3"
            },
            "cdi:typeOfStatistic": "frequency",
            "cdi:statistic": [
              {
                "cdi:computationBase": "ValidOnly",
                "cdi:content": 3739,
                "cdi:typeOfNumericValue": "decimal"
              }
            ]
          },
          {
            "@type": [
              "cdi:CategoryStatistics"
            ],
            "cdi:for": {
              "@id": "mics:codelist/HH14-language/4"
            },
            "cdi:typeOfStatistic": "frequency",
            "cdi:statistic": [
              {
                "cdi:computationBase": "ValidOnly",
                "cdi:content": 75,
                "cdi:typeOfNumericValue": "decimal"
              }
            ]
          },
          {
            "@type": [
              "cdi:CategoryStatistics"
            ],
            "cdi:for": {
              "@id": "mics:codelist/HH14-missing/sysmiss"
            },
            "cdi:typeOfStatistic": "frequency",
            "cdi:statistic": [
              {
                "cdi:computationBase": "MissingOnly",
                "cdi:content": 1463,
                "cdi:typeOfNumericValue": "decimal"
              }
            ]
          }
        ]
      }
    ]
  }
}
```

#### ttl
```ttl
@prefix cdi: <http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/> .
@prefix cdif: <https://w3id.org/cdif/> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<https://example.org/mics/mwi2019/var/HH14> a cdi:InstanceVariable,
        schema1:PropertyValue ;
    cdi:takesSentinelValuesFrom <https://example.org/mics/mwi2019/var/HH14/valueDomain/sentinel> ;
    cdi:takesSubstantiveValuesFrom <https://example.org/mics/mwi2019/var/HH14/valueDomain/substantive> ;
    schema1:description "Language of the household questionnaire. Categorical variable from the MWI 2019 MICS household record; source DDI Codebook variable HH14. The value domains reference a shared skos:ConceptScheme code list by @id; in a full document that code list is a sibling @graph node (see the cdifCodelist profile). This InstanceVariable declares the value domains directly because it does NOT defer to a RepresentedVariable via cdif:isDefinedBy_RepresentedVariable." ;
    schema1:name "HH14" ;
    cdif:definition "The language in which the household questionnaire was administered." ;
    cdif:displayLabel "Language of the Questionnaire" ;
    cdif:isDescribedBy_StatisticsCollection <https://example.org/mics/mwi2019/var/HH14/statistics> ;
    cdif:name "HH14" ;
    cdif:physicalDataType "xsd:integer" ;
    cdif:role "Measure" .

<https://example.org/mics/mwi2019/var/HH14/enumerationDomain> a cdif:EnumerationDomain ;
    schema1:name "MWI 2019 MICS questionnaire-language codes" ;
    cdif:references <https://example.org/mics/mwi2019/codelist/HH14-language> .

<https://example.org/mics/mwi2019/var/HH14/sentinelEnumerationDomain> a cdif:EnumerationDomain ;
    schema1:name "MWI 2019 MICS system-missing code" ;
    cdif:references <https://example.org/mics/mwi2019/codelist/HH14-missing> .

<https://example.org/mics/mwi2019/var/HH14/statistics> a cdi:StatisticsCollection ;
    cdif:has_Statistics <https://example.org/mics/mwi2019/var/HH14/statistics/count>,
        <https://example.org/mics/mwi2019/var/HH14/statistics/frequencies>,
        <https://example.org/mics/mwi2019/var/HH14/statistics/maximum>,
        <https://example.org/mics/mwi2019/var/HH14/statistics/minimum> ;
    cdif:indexedBy <https://example.org/mics/mwi2019/var/HH14> .

<https://example.org/mics/mwi2019/var/HH14/statistics/count> a cdi:Statistics ;
    cdi:statistic [ cdi:computationBase "MissingOnly" ;
            cdi:content 1463 ;
            cdi:typeOfNumericValue "decimal" ],
        [ cdi:computationBase "Total" ;
            cdi:content 26882 ;
            cdi:typeOfNumericValue "decimal" ],
        [ cdi:computationBase "ValidOnly" ;
            cdi:content 25419 ;
            cdi:typeOfNumericValue "decimal" ] ;
    cdi:typeOfStatistic "count" .

<https://example.org/mics/mwi2019/var/HH14/statistics/frequencies> a cdi:Statistics ;
    cdi:statistic [ cdi:computationBase "Total" ;
            cdi:content 26882 ;
            cdi:typeOfNumericValue "decimal" ] ;
    cdi:typeOfStatistic "frequency" ;
    cdif:has_CategoryStatistics [ a cdi:CategoryStatistics ;
            cdi:for <https://example.org/mics/mwi2019/codelist/HH14-language/2> ;
            cdi:statistic [ cdi:computationBase "ValidOnly" ;
                    cdi:content 21497 ;
                    cdi:typeOfNumericValue "decimal" ] ;
            cdi:typeOfStatistic "frequency" ],
        [ a cdi:CategoryStatistics ;
            cdi:for <https://example.org/mics/mwi2019/codelist/HH14-language/4> ;
            cdi:statistic [ cdi:computationBase "ValidOnly" ;
                    cdi:content 75 ;
                    cdi:typeOfNumericValue "decimal" ] ;
            cdi:typeOfStatistic "frequency" ],
        [ a cdi:CategoryStatistics ;
            cdi:for <https://example.org/mics/mwi2019/codelist/HH14-language/1> ;
            cdi:statistic [ cdi:computationBase "ValidOnly" ;
                    cdi:content 108 ;
                    cdi:typeOfNumericValue "decimal" ] ;
            cdi:typeOfStatistic "frequency" ],
        [ a cdi:CategoryStatistics ;
            cdi:for <https://example.org/mics/mwi2019/codelist/HH14-missing/sysmiss> ;
            cdi:statistic [ cdi:computationBase "MissingOnly" ;
                    cdi:content 1463 ;
                    cdi:typeOfNumericValue "decimal" ] ;
            cdi:typeOfStatistic "frequency" ],
        [ a cdi:CategoryStatistics ;
            cdi:for <https://example.org/mics/mwi2019/codelist/HH14-language/3> ;
            cdi:statistic [ cdi:computationBase "ValidOnly" ;
                    cdi:content 3739 ;
                    cdi:typeOfNumericValue "decimal" ] ;
            cdi:typeOfStatistic "frequency" ] .

<https://example.org/mics/mwi2019/var/HH14/statistics/maximum> a cdi:Statistics ;
    cdi:statistic [ cdi:computationBase "ValidOnly" ;
            cdi:content 4 ;
            cdi:typeOfNumericValue "decimal" ] ;
    cdi:typeOfStatistic "maximum" .

<https://example.org/mics/mwi2019/var/HH14/statistics/minimum> a cdi:Statistics ;
    cdi:statistic [ cdi:computationBase "ValidOnly" ;
            cdi:content 1 ;
            cdi:typeOfNumericValue "decimal" ] ;
    cdi:typeOfStatistic "minimum" .

<https://example.org/mics/mwi2019/var/HH14/valueDomain/sentinel> a cdif:SentinelValueDomain ;
    cdif:displayLabel "Missing-value codes for HH14" ;
    cdif:takesValuesFrom <https://example.org/mics/mwi2019/var/HH14/sentinelEnumerationDomain> .

<https://example.org/mics/mwi2019/var/HH14/valueDomain/substantive> a cdif:SubstantiveValueDomain ;
    cdif:displayLabel "Valid language codes for HH14" ;
    cdif:takesValuesFrom <https://example.org/mics/mwi2019/var/HH14/enumerationDomain> .


```


### CDIF Instance Variable with category statistics (minimal, no missing)
The pared-down companion to the HH14 statistics example. Variable HH6
("Area", urban/rural) of the MWI 2019 MICS household record (DDI Codebook
2.5): a binary category with no missing values, so there is a substantive
value domain (2-concept code list) but no SentinelValueDomain. The
StatisticsCollection carries count/min/max plus one cdi:CategoryStatistics
per category; the category frequencies (3936 + 22946) reconcile with the
valid count (26882).
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
    "cdif": "https://w3id.org/cdif/",
    "skos": "http://www.w3.org/2004/02/skos/core#",
    "xsd": "http://www.w3.org/2001/XMLSchema#",
    "mics": "https://example.org/mics/mwi2019/"
  },
  "@id": "mics:var/HH6",
  "@type": [
    "cdi:InstanceVariable",
    "schema:PropertyValue"
  ],
  "schema:name": "HH6",
  "schema:description": "Area (urban/rural) of the household. Categorical variable from the MWI 2019 MICS household record; source DDI Codebook variable HH6. Every case is valid (no missing category), so there is a substantive value domain but no sentinel value domain. The value domain references a shared skos:ConceptScheme code list by @id (a sibling @graph node in a full document).",
  "cdif:name": [
    "HH6"
  ],
  "cdif:displayLabel": [
    "Area"
  ],
  "cdif:definition": "Whether the household is located in an urban or rural area.",
  "cdif:physicalDataType": "xsd:integer",
  "cdif:role": "Measure",

  "cdi:takesSubstantiveValuesFrom": {
    "@id": "mics:var/HH6/valueDomain/substantive",
    "@type": [
      "cdif:SubstantiveValueDomain"
    ],
    "cdif:displayLabel": "Valid area codes for HH6",
    "cdif:takesValuesFrom": {
      "@id": "mics:var/HH6/enumerationDomain",
      "@type": [
        "cdif:EnumerationDomain"
      ],
      "schema:name": "MWI 2019 MICS area codes",
      "cdif:references": {
        "@id": "mics:codelist/HH6-area"
      }
    }
  },

  "cdif:isDescribedBy_StatisticsCollection": {
    "@id": "mics:var/HH6/statistics",
    "@type": [
      "cdi:StatisticsCollection"
    ],
    "cdif:indexedBy": [
      {
        "@id": "mics:var/HH6"
      }
    ],
    "cdif:has_Statistics": [
      {
        "@id": "mics:var/HH6/statistics/count",
        "@type": [
          "cdi:Statistics"
        ],
        "cdi:typeOfStatistic": "count",
        "cdi:statistic": [
          {
            "cdi:computationBase": "ValidOnly",
            "cdi:content": 26882,
            "cdi:typeOfNumericValue": "decimal"
          },
          {
            "cdi:computationBase": "Total",
            "cdi:content": 26882,
            "cdi:typeOfNumericValue": "decimal"
          }
        ]
      },
      {
        "@id": "mics:var/HH6/statistics/minimum",
        "@type": [
          "cdi:Statistics"
        ],
        "cdi:typeOfStatistic": "minimum",
        "cdi:statistic": [
          {
            "cdi:computationBase": "ValidOnly",
            "cdi:content": 1,
            "cdi:typeOfNumericValue": "decimal"
          }
        ]
      },
      {
        "@id": "mics:var/HH6/statistics/maximum",
        "@type": [
          "cdi:Statistics"
        ],
        "cdi:typeOfStatistic": "maximum",
        "cdi:statistic": [
          {
            "cdi:computationBase": "ValidOnly",
            "cdi:content": 2,
            "cdi:typeOfNumericValue": "decimal"
          }
        ]
      },
      {
        "@id": "mics:var/HH6/statistics/frequencies",
        "@type": [
          "cdi:Statistics"
        ],
        "cdi:typeOfStatistic": "frequency",
        "cdi:statistic": [
          {
            "cdi:computationBase": "Total",
            "cdi:content": 26882,
            "cdi:typeOfNumericValue": "decimal"
          }
        ],
        "cdif:has_CategoryStatistics": [
          {
            "@type": [
              "cdi:CategoryStatistics"
            ],
            "cdi:for": {
              "@id": "mics:codelist/HH6-area/1"
            },
            "cdi:typeOfStatistic": "frequency",
            "cdi:statistic": [
              {
                "cdi:computationBase": "ValidOnly",
                "cdi:content": 3936,
                "cdi:typeOfNumericValue": "decimal"
              }
            ]
          },
          {
            "@type": [
              "cdi:CategoryStatistics"
            ],
            "cdi:for": {
              "@id": "mics:codelist/HH6-area/2"
            },
            "cdi:typeOfStatistic": "frequency",
            "cdi:statistic": [
              {
                "cdi:computationBase": "ValidOnly",
                "cdi:content": 22946,
                "cdi:typeOfNumericValue": "decimal"
              }
            ]
          }
        ]
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
      "cdif": "https://w3id.org/cdif/",
      "skos": "http://www.w3.org/2004/02/skos/core#",
      "mics": "https://example.org/mics/mwi2019/"
    },
    "https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifDataType/cdifInstanceVariable/context.jsonld",
    {
      "schema": "http://schema.org/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "cdif": "https://w3id.org/cdif/",
      "skos": "http://www.w3.org/2004/02/skos/core#",
      "xsd": "http://www.w3.org/2001/XMLSchema#",
      "mics": "https://example.org/mics/mwi2019/"
    }
  ],
  "@id": "mics:var/HH6",
  "@type": [
    "cdi:InstanceVariable",
    "schema:PropertyValue"
  ],
  "schema:name": "HH6",
  "schema:description": "Area (urban/rural) of the household. Categorical variable from the MWI 2019 MICS household record; source DDI Codebook variable HH6. Every case is valid (no missing category), so there is a substantive value domain but no sentinel value domain. The value domain references a shared skos:ConceptScheme code list by @id (a sibling @graph node in a full document).",
  "cdif:name": [
    "HH6"
  ],
  "cdif:displayLabel": [
    "Area"
  ],
  "cdif:definition": "Whether the household is located in an urban or rural area.",
  "cdif:physicalDataType": "xsd:integer",
  "cdif:role": "Measure",
  "cdi:takesSubstantiveValuesFrom": {
    "@id": "mics:var/HH6/valueDomain/substantive",
    "@type": [
      "cdif:SubstantiveValueDomain"
    ],
    "cdif:displayLabel": "Valid area codes for HH6",
    "cdif:takesValuesFrom": {
      "@id": "mics:var/HH6/enumerationDomain",
      "@type": [
        "cdif:EnumerationDomain"
      ],
      "schema:name": "MWI 2019 MICS area codes",
      "cdif:references": {
        "@id": "mics:codelist/HH6-area"
      }
    }
  },
  "cdif:isDescribedBy_StatisticsCollection": {
    "@id": "mics:var/HH6/statistics",
    "@type": [
      "cdi:StatisticsCollection"
    ],
    "cdif:indexedBy": [
      {
        "@id": "mics:var/HH6"
      }
    ],
    "cdif:has_Statistics": [
      {
        "@id": "mics:var/HH6/statistics/count",
        "@type": [
          "cdi:Statistics"
        ],
        "cdi:typeOfStatistic": "count",
        "cdi:statistic": [
          {
            "cdi:computationBase": "ValidOnly",
            "cdi:content": 26882,
            "cdi:typeOfNumericValue": "decimal"
          },
          {
            "cdi:computationBase": "Total",
            "cdi:content": 26882,
            "cdi:typeOfNumericValue": "decimal"
          }
        ]
      },
      {
        "@id": "mics:var/HH6/statistics/minimum",
        "@type": [
          "cdi:Statistics"
        ],
        "cdi:typeOfStatistic": "minimum",
        "cdi:statistic": [
          {
            "cdi:computationBase": "ValidOnly",
            "cdi:content": 1,
            "cdi:typeOfNumericValue": "decimal"
          }
        ]
      },
      {
        "@id": "mics:var/HH6/statistics/maximum",
        "@type": [
          "cdi:Statistics"
        ],
        "cdi:typeOfStatistic": "maximum",
        "cdi:statistic": [
          {
            "cdi:computationBase": "ValidOnly",
            "cdi:content": 2,
            "cdi:typeOfNumericValue": "decimal"
          }
        ]
      },
      {
        "@id": "mics:var/HH6/statistics/frequencies",
        "@type": [
          "cdi:Statistics"
        ],
        "cdi:typeOfStatistic": "frequency",
        "cdi:statistic": [
          {
            "cdi:computationBase": "Total",
            "cdi:content": 26882,
            "cdi:typeOfNumericValue": "decimal"
          }
        ],
        "cdif:has_CategoryStatistics": [
          {
            "@type": [
              "cdi:CategoryStatistics"
            ],
            "cdi:for": {
              "@id": "mics:codelist/HH6-area/1"
            },
            "cdi:typeOfStatistic": "frequency",
            "cdi:statistic": [
              {
                "cdi:computationBase": "ValidOnly",
                "cdi:content": 3936,
                "cdi:typeOfNumericValue": "decimal"
              }
            ]
          },
          {
            "@type": [
              "cdi:CategoryStatistics"
            ],
            "cdi:for": {
              "@id": "mics:codelist/HH6-area/2"
            },
            "cdi:typeOfStatistic": "frequency",
            "cdi:statistic": [
              {
                "cdi:computationBase": "ValidOnly",
                "cdi:content": 22946,
                "cdi:typeOfNumericValue": "decimal"
              }
            ]
          }
        ]
      }
    ]
  }
}
```

#### ttl
```ttl
@prefix cdi: <http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/> .
@prefix cdif: <https://w3id.org/cdif/> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<https://example.org/mics/mwi2019/var/HH6> a cdi:InstanceVariable,
        schema1:PropertyValue ;
    cdi:takesSubstantiveValuesFrom <https://example.org/mics/mwi2019/var/HH6/valueDomain/substantive> ;
    schema1:description "Area (urban/rural) of the household. Categorical variable from the MWI 2019 MICS household record; source DDI Codebook variable HH6. Every case is valid (no missing category), so there is a substantive value domain but no sentinel value domain. The value domain references a shared skos:ConceptScheme code list by @id (a sibling @graph node in a full document)." ;
    schema1:name "HH6" ;
    cdif:definition "Whether the household is located in an urban or rural area." ;
    cdif:displayLabel "Area" ;
    cdif:isDescribedBy_StatisticsCollection <https://example.org/mics/mwi2019/var/HH6/statistics> ;
    cdif:name "HH6" ;
    cdif:physicalDataType "xsd:integer" ;
    cdif:role "Measure" .

<https://example.org/mics/mwi2019/var/HH6/enumerationDomain> a cdif:EnumerationDomain ;
    schema1:name "MWI 2019 MICS area codes" ;
    cdif:references <https://example.org/mics/mwi2019/codelist/HH6-area> .

<https://example.org/mics/mwi2019/var/HH6/statistics> a cdi:StatisticsCollection ;
    cdif:has_Statistics <https://example.org/mics/mwi2019/var/HH6/statistics/count>,
        <https://example.org/mics/mwi2019/var/HH6/statistics/frequencies>,
        <https://example.org/mics/mwi2019/var/HH6/statistics/maximum>,
        <https://example.org/mics/mwi2019/var/HH6/statistics/minimum> ;
    cdif:indexedBy <https://example.org/mics/mwi2019/var/HH6> .

<https://example.org/mics/mwi2019/var/HH6/statistics/count> a cdi:Statistics ;
    cdi:statistic [ cdi:computationBase "Total" ;
            cdi:content 26882 ;
            cdi:typeOfNumericValue "decimal" ],
        [ cdi:computationBase "ValidOnly" ;
            cdi:content 26882 ;
            cdi:typeOfNumericValue "decimal" ] ;
    cdi:typeOfStatistic "count" .

<https://example.org/mics/mwi2019/var/HH6/statistics/frequencies> a cdi:Statistics ;
    cdi:statistic [ cdi:computationBase "Total" ;
            cdi:content 26882 ;
            cdi:typeOfNumericValue "decimal" ] ;
    cdi:typeOfStatistic "frequency" ;
    cdif:has_CategoryStatistics [ a cdi:CategoryStatistics ;
            cdi:for <https://example.org/mics/mwi2019/codelist/HH6-area/1> ;
            cdi:statistic [ cdi:computationBase "ValidOnly" ;
                    cdi:content 3936 ;
                    cdi:typeOfNumericValue "decimal" ] ;
            cdi:typeOfStatistic "frequency" ],
        [ a cdi:CategoryStatistics ;
            cdi:for <https://example.org/mics/mwi2019/codelist/HH6-area/2> ;
            cdi:statistic [ cdi:computationBase "ValidOnly" ;
                    cdi:content 22946 ;
                    cdi:typeOfNumericValue "decimal" ] ;
            cdi:typeOfStatistic "frequency" ] .

<https://example.org/mics/mwi2019/var/HH6/statistics/maximum> a cdi:Statistics ;
    cdi:statistic [ cdi:computationBase "ValidOnly" ;
            cdi:content 2 ;
            cdi:typeOfNumericValue "decimal" ] ;
    cdi:typeOfStatistic "maximum" .

<https://example.org/mics/mwi2019/var/HH6/statistics/minimum> a cdi:Statistics ;
    cdi:statistic [ cdi:computationBase "ValidOnly" ;
            cdi:content 1 ;
            cdi:typeOfNumericValue "decimal" ] ;
    cdi:typeOfStatistic "minimum" .

<https://example.org/mics/mwi2019/var/HH6/valueDomain/substantive> a cdif:SubstantiveValueDomain ;
    cdif:displayLabel "Valid area codes for HH6" ;
    cdif:takesValuesFrom <https://example.org/mics/mwi2019/var/HH6/enumerationDomain> .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: CDIF Instance Variable
type: object
properties:
  '@type':
    type: array
    description: Must include both schema:PropertyValue and cdi:InstanceVariable.
      Additional types may be included.
    items:
      type: string
    contains:
      const: cdi:InstanceVariable
  cdif:physicalDataType:
    $ref: '#/$defs/cdifConceptOrTermOrString'
    description: identifier or name for the data type concept.
    x-jsonld-id: https://w3id.org/cdif/physicalDataType
  cdif:role:
    type: string
    enum:
    - UnitIdentifier
    - Measure
    - Attribute
    - Dimension
    - Descriptor
    - ReferenceVariable
    description: Specifies the role this variable plays in a data structure. UnitIdentifier
      names the unit a row describes; Measure holds observed/derived values; Attribute
      qualifies an observation; Dimension addresses a cell in a multi-dimensional
      cube; Descriptor names the variable that a Reference column records values for
      (long format); ReferenceVariable holds those recorded values.
    x-jsonld-id: https://w3id.org/cdif/role
  cdif:simpleUnitOfMeasure:
    description: The unit in which the data values are measured (kg, pound, euro),
      expressed as a simple string, in cases where no additional information is available
      (in the legacy system) or needed (as in the case of broad agreement within the
      community of use [i.e., ISO country codes, currencies, etc. in SDMX])
    type: string
    x-jsonld-id: https://w3id.org/cdif/simpleUnitOfMeasure
  cdif:uses:
    type: array
    items:
      $ref: '#/$defs/cdifConceptOrTermOrString'
    description: Essentially the same as schema:propertyID. References to the concept(s)
      that this variable measures or represents. Concepts only -- to point at the
      RepresentedVariable that supplies the represented-variable-level properties,
      use cdif:isDefinedBy_RepresentedVariable. Splitting the two targets follows
      the CDIF convention of disambiguating the polymorphic DDI-CDI role names by
      target, so each JSON key has a single value type; it also keeps cdif:uses type-compatible
      with canonical cdi:uses on InstanceVariable, which is valued by a Concept.
    x-jsonld-id: https://w3id.org/cdif/uses
  cdif:isDefinedBy_RepresentedVariable:
    $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifDataType/objectReference/schema.yaml
    description: 'The RepresentedVariable this InstanceVariable instantiates. A reference
      only (@id, nothing else): the point of the link is that the represented-variable-level
      properties are defined once on the RepresentedVariable and NOT duplicated here,
      so an inline copy would defeat it. Same property name as on cdifDataStructureComponent,
      which carries the equivalent link within a data structure; that one also accepts
      an inline RepresentedVariable because a structure may define one that exists
      nowhere else.'
    x-jsonld-id: https://w3id.org/cdif/isDefinedBy_RepresentedVariable
  cdi:function:
    type: array
    items:
      $ref: '#/$defs/cdifConceptOrTermOrString'
    description: Immutable characteristic of the variable such as geographic designator,
      weight, temporal designation, etc. (InstanceVariable.function).
    x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/function
  cdi:platformType:
    $ref: '#/$defs/cdifConceptOrTermOrString'
    description: The application or technical system context in which the variable
      has been realized - typically a statistical processing package or processing
      environment (InstanceVariable.platformType).
    x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/platformType
  cdi:source:
    anyOf:
    - type: string
    - type: object
      required:
      - '@id'
      additionalProperties: false
      properties:
        '@id':
          type: string
    description: Reference capturing provenance information for this InstanceVariable
      (InstanceVariable.source).
    x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/source
  cdif:isDescribedBy_StatisticsCollection:
    description: "The StatisticsCollection holding summary / category statistics for
      this InstanceVariable (direct JSON mapping of the DDI-CDI `InstanceVariable.isDescribedBy
      \u2192 StatisticsCollection` association). cdif: namespaced and target-suffixed
      because the DDI-CDI isDescribedBy association is polymorphic. This is the canonical
      CDIF path for **per-variable** statistics; dataset-scope aggregates (row count
      etc.) go under `Dataset.cdif:statistics` instead."
    anyOf:
    - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifDataType/cdifStatistics/schema.yaml#/$defs/StatisticsCollection
    - type: object
      additionalProperties: false
      properties:
        '@id':
          type: string
      required:
      - '@id'
    x-jsonld-id: https://w3id.org/cdif/isDescribedBy_StatisticsCollection
  cdi:describedUnitOfMeasure:
    $ref: '#/$defs/cdifConceptOrTerm'
    description: The unit in which the data values are measured, expressed as a controlled-vocabulary
      entry (RepresentedVariable.describedUnitOfMeasure). For a plain-string unit,
      use cdif:simpleUnitOfMeasure instead.
    x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/describedUnitOfMeasure
  cdi:qualifies:
    type: object
    required:
    - '@id'
    additionalProperties: false
    properties:
      '@id':
        type: string
    description: reference to an instance variable defined for this dataset
    x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/qualifies
allOf:
- required:
  - '@type'
- $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/variableMeasured/schema.yaml
- if:
    required:
    - cdif:isDefinedBy_RepresentedVariable
  then:
    properties:
      cdi:takesSubstantiveValuesFrom:
        not: true
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/takesSubstantiveValuesFrom
      cdi:takesSentinelValuesFrom:
        not: true
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/takesSentinelValuesFrom
      cdi:hasIntendedDataType:
        not: true
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/hasIntendedDataType
      cdi:describedUnitOfMeasure:
        not: true
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/describedUnitOfMeasure
      cdi:unitOfMeasureKind:
        not: true
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/unitOfMeasureKind
      cdi:measures:
        not: true
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/measures
      cdi:externalDefinition:
        not: true
        x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/externalDefinition
      cdif:uses_Concept:
        not: true
        x-jsonld-id: https://w3id.org/cdif/uses_Concept
      cdif:definition:
        not: true
        x-jsonld-id: https://w3id.org/cdif/definition
    description: When cdif:isDefinedBy_RepresentedVariable is present, the represented-variable-level
      properties live on that RepresentedVariable and may not be declared inline on
      the InstanceVariable.
$defs:
  cdifConceptOrTermOrString:
    $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifDataType/cdifConceptOrTermOrString/schema.yaml
  cdifConceptOrTerm:
    $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifDataType/cdifConceptOrTerm/schema.yaml
x-jsonld-prefixes:
  cdif: https://w3id.org/cdif/
  schema: http://schema.org/
  spdx: http://spdx.org/rdf/terms#
  cdi: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/
  skos: http://www.w3.org/2004/02/skos/core#
  xas: https://w3id.org/cdif/xas/
  nxs: https://manual.nexusformat.org/classes/
  prov: http://www.w3.org/ns/prov#

```

Links to the schema:

* YAML version: [schema.yaml](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifDataType/cdifInstanceVariable/schema.json)
* JSON version: [schema.json](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifDataType/cdifInstanceVariable/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "cdif": "https://w3id.org/cdif/",
    "schema": "http://schema.org/",
    "spdx": "http://spdx.org/rdf/terms#",
    "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
    "skos": "http://www.w3.org/2004/02/skos/core#",
    "xas": "cdif:xas/",
    "nxs": "https://manual.nexusformat.org/classes/",
    "prov": "http://www.w3.org/ns/prov#",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifDataType/cdifInstanceVariable/context.jsonld)

## Sources

* [DDI-CDI 1.0 Specification](https://ddialliance.org/Specification/DDI-CDI/1.0/)
* [schema.org/variableMeasured](https://schema.org/variableMeasured)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/Cross-Domain-Interoperability-Framework/metadataBuildingBlocks](https://github.com/Cross-Domain-Interoperability-Framework/metadataBuildingBlocks)
* Path: `_sources/cdifDataType/cdifInstanceVariable`

