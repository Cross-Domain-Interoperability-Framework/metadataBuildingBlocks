
# CDIF discovery and data description metadata (Schema)

`cdif.bbr.metadata.profiles.cdifCompositeProfile.BasicDataDescription` *v0.1*

Schema extends data discovery with properties to desribe data structures for tabular and structured (grid, datacube, hierarchialc) datasets

[*Status*](http://www.opengis.net/def/status): Under development

## Description

## CDIF Data Description Metadata Profile

Profile for the schema.org implementation of the [Cross Domain Interoperability Framework](https://cross-domain-interoperability-framework.github.io/cdifbook/metadata/schemaorgimplementation.html#implementation-of-metadata-content-items) (CDIF) data description profile. Composes cdifCore with discovery properties and data description extensions.

### Composition

- **cdifCore** -- all required and optional core metadata properties
- **Discovery properties** -- measurement technique, variables measured, spatial/temporal coverage, quality measurements
- **Data description extensions**:
  - `schema:variableMeasured` items at this level require `cdi:InstanceVariable` typing and `cdif:physicalDataType`
  - `schema:distribution` items may include `cdi:characterSet`, `cdif:fileSize`, `cdif:fileSizeUofM`
  - `cdif:hasPrimaryKey` points at a `cdif:Key` node (via the `cdifKey` building block)
  - `cdif:statistics` carries one or more `cdi:Statistics` bundles or a `cdi:StatisticsCollection` (via the `cdifStatistics` building block)

### Conformance

Metadata conforming to this profile declares conformance to `cdif/core/1.0/`, `cdif/discovery/1.0/`, and `cdif/data_description/1.0/`.

## Examples

### CDIF data description example record.
Example CDIF metadata with data description extensions for distributions
(single-file, archive with hasPart, and WebAPI) and optional tabular/dataCube
physical mappings.
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "dcterms": "http://purl.org/dc/terms/",
    "geosparql": "http://www.opengis.net/ont/geosparql#",
    "sf": "http://www.opengis.net/ont/sf#",
    "spdx": "http://spdx.org/rdf/terms#",
    "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
    "cdif": "https://cdif.org/0.1/",
    "csvw": "http://www.w3.org/ns/csvw#",
    "dqv": "http://www.w3.org/ns/dqv#",
    "time": "http://www.w3.org/2006/time#",
    "ex": "https://example.org/",
    "xsd": "http://www.w3.org/2001/XMLSchema#",
    "dcat": "http://www.w3.org/ns/dcat#",
    "prov": "http://www.w3.org/ns/prov#"
  },
  "@id": "ex:YOPx",
  "@type": [
    "schema:Dataset"
  ],
  "schema:name": "Test dataset",
  "schema:description": "Auto generated from JSON schema, values are gobbledegoop. For testing",
  "schema:additionalType": [
    "test data description"
  ],
  "schema:identifier": {
    "@type": [
      "schema:PropertyValue"
    ],
    "schema:propertyID": "uSNzhqeEQPKhCj",
    "schema:url": "http://identifiers.org/sandbox/uSNzhqeEQPKhCj"
  },
  "schema:sameAs": [
    {
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": "urn:idorg:test",
      "schema:value": "urn:idorg:test:p45689"
    }
  ],
  "schema:version": "OVVAYgJhmFkXyVyedlVo",
  "schema:url": "http://example.com/resource?foo=bar#fragment",
  "schema:inLanguage": "bYiJT",
  "schema:dateModified": "2020-10-15",
  "schema:datePublished": "2021-09-05",
  "schema:conditionsOfAccess": [
    "ihYojbwJyw",
    "jNv",
    "LCY",
    "tfmbDGeiuEnuhfKBvk"
  ],
  "schema:license": [
    "dXhuFoqL",
    "Kmp"
  ],
  "schema:relatedLink": [
    {
      "@type": [
        "schema:LinkRole"
      ],
      "schema:linkRelationship": "lfCzUaoftdtTPAhMnpC",
      "target": {
        "@type": [
          "schema:EntryPoint"
        ],
        "schema:encodingFormat": "gompgHAN",
        "schema:name": "oAuxEutsTEiB",
        "schema:url": "http://example.com/resource?foo=bar#fragment"
      }
    },
    {
      "@type": [
        "schema:LinkRole"
      ],
      "schema:linkRelationship": "BOoRREnpDEUrdNaV",
      "target": {
        "@type": [
          "schema:EntryPoint"
        ],
        "schema:encodingFormat": "FNoslhw",
        "schema:name": "atsDYJxuhHpivqLmw",
        "schema:url": "http://example.com/resource?foo=bar#fragment"
      }
    }
  ],
  "schema:publishingPrinciples": [
    "rxZsrPAbJrIGGgDVJ"
  ],
  "schema:keywords": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:name": "MiSqvcp",
      "schema:identifier": {
        "@type": [
          "schema:PropertyValue"
        ],
        "schema:propertyID": "ex:rIPXjaCPQX",
        "schema:value": "PVSajGtBPsLzeCTLv",
        "schema:url": "http://example.com/resource/PVSajGtBPsLzeCTLvt"
      },
      "schema:inDefinedTermSet": "EfagQEQtAkwMBDvfKznc",
      "schema:termCode": "bzOl"
    },
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:name": "TiMuawt",
      "schema:identifier": {
        "@type": [
          "schema:PropertyValue"
        ],
        "schema:propertyID": "https://resource.org/identifier",
        "schema:value": "tdUMYBItIwdJe",
        "schema:url": "http://example.com/resource/tdUMYBItIwdJe"
      },
      "schema:inDefinedTermSet": "sqH",
      "schema:termCode": "RUUxHY"
    }
  ],
  "schema:creator": {
    "@list": [
      {
        "@id": "ex:mxxInaV",
        "@type": [
          "schema:Organization"
        ],
        "schema:name": "AEbcNvM",
        "schema:alternateName": "MwsoNGVEp",
        "schema:affiliation": {
          "@id": "ex:xblzSwEYJKBPpkK",
          "@type": [
            "schema:Organization"
          ],
          "schema:additionalType": [
            "schema:GovernmentOrganization",
            "schema:ResearchOrganization",
            "schema:ResearchOrganization",
            "schema:Project"
          ],
          "schema:name": "mDjEBamofgiqGBqfQGfe",
          "schema:alternateName": "TrAuXgjTOCmJVTaf",
          "schema:description": "wwcOQoCbUe",
          "schema:identifier": {
            "@type": [
              "schema:PropertyValue"
            ],
            "schema:propertyID": "oyvigoDvYFCGEkFc",
            "schema:value": "tMxtQyCUFptzpXj",
            "schema:url": "http://example.com/resource?foo=bar#fragment"
          },
          "schema:sameAs": [
            "K",
            "AsoXEfDoLipcJw"
          ]
        },
        "schema:contactPoint": {
          "@type": [
            "schema:ContactPoint"
          ],
          "schema:email": "tready@email.ocm"
        },
        "schema:description": "ypZ",
        "schema:identifier": {
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": "ciZyuOzfhVSPdWi",
          "schema:value": "JqLmJhoyFPhsmW",
          "schema:url": "http://example.com/resource?foo=bar#fragment"
        },
        "schema:sameAs": [
          "ex:pMPylNhiMvfC",
          "ex:IgH"
        ]
      },
      {
        "@id": "ex:jP",
        "@type": [
          "schema:Person"
        ],
        "schema:name": "Doe, Jane",
        "schema:contactPoint": {
          "@type": [
            "schema:ContactPoint"
          ],
          "schema:email": "jdoe@example.org"
        }
      }
    ]
  },
  "schema:contributor": [
    {
      "@type": [
        "schema:Role"
      ],
      "schema:roleName": "editor",
      "schema:contributor": {
        "@id": "ex:PersonExample_zZc_asContributor",
        "@type": [
          "schema:Person"
        ],
        "schema:name": "Joe B. Test",
        "schema:alternateName": "Test, J. B.",
        "schema:affiliation": {
          "@type": [
            "schema:Organization"
          ],
          "schema:name": "The Big Manufacturing Co."
        },
        "schema:description": "Metadata specialist, based in Portland, Maine",
        "schema:identifier": {
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": "https://orcid.org",
          "schema:value": "iY",
          "schema:url": "https://orcid.org/iY"
        },
        "schema:contactPoint": {
          "@type": [
            "schema:ContactPoint"
          ],
          "schema:email": "joe@bmanuco.org"
        },
        "schema:sameAs": [
          "https://ark.org/46737",
          "uri:test:43737"
        ]
      }
    },
    {
      "@id": "ex:NyMWPlRtQizAFE"
    }
  ],
  "schema:publisher": {
    "@id": "ex:exampleOrg_fW",
    "@type": [
      "schema:Organization"
    ],
    "schema:additionalType": [
      "schema:ResearchOrganization",
      "university"
    ],
    "schema:name": "University of Arizona",
    "schema:alternateName": "UAz",
    "schema:description": "University in Tucson, Arizona",
    "schema:identifier": {
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": "https://registry.identifiers.org/registry/ror",
      "schema:value": "03m2x1q45",
      "schema:url": "https://ror.org/03m2x1q45"
    },
    "schema:sameAs": [
      "Wildcats"
    ]
  },
  "schema:provider": [
    {
      "@id": "ex:gDiAxjl",
      "@type": [
        "schema:Organization"
      ],
      "schema:name": "Example Data Center"
    },
    {
      "@id": "ex:ihjJtFPNEKnGSFBcgS",
      "@type": [
        "schema:Person"
      ],
      "schema:name": "Smith, Robert",
      "schema:contactPoint": {
        "@type": [
          "schema:ContactPoint"
        ],
        "schema:email": "rsmith@example.org"
      }
    },
    {
      "@id": "https://ada.org/person/5489",
      "@type": [
        "schema:Person"
      ],
      "schema:contactPoint": {
        "@type": [
          "schema:ContactPoint"
        ],
        "schema:email": "a.king@nhm.ac.uk"
      },
      "schema:identifier": {
        "@type": [
          "schema:PropertyValue"
        ],
        "schema:propertyID": "https://orcid.org",
        "schema:value": "0000-0001-6113-5417",
        "schema:url": "https://orcid.org/0000-0001-6113-5417"
      },
      "schema:name": "King, Ashley"
    }
  ],
  "schema:funding": [
    {
      "@type": [
        "schema:MonetaryGrant"
      ],
      "schema:identifier": {
        "@type": [
          "schema:PropertyValue"
        ],
        "schema:propertyID": "grant-id",
        "schema:value": "lieopgXuumP"
      },
      "schema:name": "fhhbzh",
      "schema:funder": {
        "@id": "https://ror.org/3572wjht"
      }
    },
    {
      "@type": [
        "schema:MonetaryGrant"
      ],
      "schema:identifier": {
        "@type": [
          "schema:PropertyValue"
        ],
        "schema:propertyID": "grant-id",
        "schema:value": "fMuiBjneudpV"
      },
      "schema:name": "MWoPQAqRYHobey",
      "schema:funder": {
        "@id": "https://ror.org/fnjrj68"
      }
    },
    {
      "@type": [
        "schema:MonetaryGrant"
      ],
      "schema:identifier": {
        "@type": [
          "schema:PropertyValue"
        ],
        "schema:propertyID": "grant-id",
        "schema:value": "LZpo"
      },
      "schema:name": "ekckpBtI",
      "schema:funder": {
        "@id": "https://ror.org/sejer4w6u8"
      }
    }
  ],
  "schema:distribution": [
    {
      "@type": [
        "schema:DataDownload",
        "cdi:PhysicalDataSet"
      ],
      "schema:name": "VwuIdrCrJSsrGATePg",
      "schema:contentUrl": "http://example.com/resource?foo=bar#fragment",
      "schema:encodingFormat": [
        "text/csv"
      ],
      "spdx:checksum": {
        "@type": [
          "spdx:Checksum"
        ],
        "spdx:algorithm": "MD5",
        "spdx:checksumValue": "MITGLcmBjeFYWmjP"
      },
      "schema:provider": [
        {
          "@id": "ex:ABYcNWHKYhTiLLNEzJx",
          "@type": [
            "schema:Person"
          ],
          "schema:name": "Walker, Longin",
          "schema:alternateName": "LWH",
          "schema:affiliation": {
            "@id": "ex:corzCgjNrGcH",
            "@type": [
              "schema:Organization"
            ],
            "schema:additionalType": [
              "schema:NGO"
            ],
            "schema:name": "Some Data Repository",
            "schema:alternateName": "leJqYoxQIH",
            "schema:description": "vRzzUAmtNWLgZcgNIC",
            "schema:identifier": {
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": "KSgJJfyAuQPEX",
              "schema:value": "iFSyBdjVAxHmFOZVFg"
            },
            "schema:sameAs": [
              "ex:ITXGFU",
              "urn:test:WWcBivQCAO"
            ]
          },
          "schema:contactPoint": {
            "@type": [
              "schema:ContactPoint"
            ],
            "schema:email": "tom@ngo.net"
          },
          "schema:description": "Data Curator",
          "schema:identifier": {
            "@type": [
              "schema:PropertyValue"
            ],
            "schema:propertyID": "https://identifiers.org/orcid",
            "schema:value": "NfaMinUfHeMDEFNc",
            "schema:url": "http://orcid.org/NfaMinUfHeMDEFNc"
          }
        }
      ],
      "dcterms:conformsTo": [
        {
          "@id": "http://www.opengis.net/def/nil/OGC/0/missing"
        }
      ]
    },
    {
      "@type": [
        "schema:DataDownload",
        "cdi:PhysicalDataSet"
      ],
      "schema:name": "MVMpmnCGAggEnsoEgJXH",
      "schema:contentUrl": "http://example.com/resource?foo=bar#fragment",
      "schema:encodingFormat": [
        "tNdpXaJgDeWbFkNM",
        "kpZDvhyVo",
        "sMUGwSqxWzJOYEb"
      ],
      "spdx:checksum": {
        "@type": [
          "spdx:Checksum"
        ],
        "spdx:algorithm": "j",
        "spdx:checksumValue": "h"
      },
      "schema:provider": [
        {
          "@id": "ex:kNKPZsCSWMc",
          "@type": [
            "schema:Organization"
          ],
          "schema:name": "SdeMvoPFxEaJOvQy",
          "schema:alternateName": "WFcslOjvGZY",
          "schema:description": "ztcLdOAkQTKSPLZ",
          "schema:identifier": {
            "@type": [
              "schema:PropertyValue"
            ],
            "schema:propertyID": "ex:oFIYAymjuGCPjDnSgmB",
            "schema:url": "http://example.com/resource/WPfhCJyxiDcwgdHMemJd"
          }
        },
        {
          "@id": "ex:sr68lgy",
          "@type": [
            "schema:Organization"
          ],
          "schema:name": "Another Provider Org"
        }
      ],
      "dcterms:conformsTo": [
        {
          "@id": "http://www.opengis.net/def/nil/OGC/0/missing"
        }
      ]
    },
    {
      "@type": [
        "schema:DataDownload",
        "cdi:TabularTextDataSet",
        "cdi:PhysicalDataSet"
      ],
      "schema:name": "Geochemistry analysis results",
      "schema:contentUrl": "http://example.com/data/geochem-results.csv",
      "schema:encodingFormat": [
        "text/csv"
      ],
      "spdx:checksum": {
        "@type": [
          "spdx:Checksum"
        ],
        "spdx:algorithm": "SHA256",
        "spdx:checksumValue": "a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4e5f6a1b2"
      },
      "cdi:characterSet": "UTF-8",
      "cdif:fileSize": 4.6,
      "cdif:fileSizeUofM": "MB",
      "cdi:isDelimited": true,
      "csvw:delimiter": ",",
      "csvw:header": true,
      "csvw:headerRowCount": 1,
      "csvw:commentPrefix": "#",
      "csvw:skipRows": 0,
      "csvw:skipBlankRows": true,
      "csvw:quoteChar": "\"",
      "countRows": 461,
      "countColumns": 2,
      "cdif:hasPhysicalMapping": [
        {
          "cdif:index": 0,
          "cdif:format": "decimal",
          "cdif:physicalDataType": "float64",
          "cdi:nullSequence": "NA",
          "cdi:isRequired": true,
          "cdif:formats_InstanceVariable": {
            "@id": "ex:KJTFKurNFu"
          }
        },
        {
          "cdif:index": 1,
          "cdif:format": "decimal",
          "cdif:physicalDataType": "float64",
          "cdi:nullSequence": "-9999",
          "cdi:defaultValue": "0.0",
          "cdi:decimalPositions": 4,
          "cdi:isRequired": false,
          "cdif:formats_InstanceVariable": {
            "@id": "ex:OjHgIDO"
          }
        }
      ],
      "dcterms:conformsTo": [
        {
          "@id": "http://www.opengis.net/def/nil/OGC/0/missing"
        }
      ]
    },
    {
      "@type": [
        "schema:DataDownload",
        "cdi:StructuredDataSet",
        "cdi:PhysicalDataSet"
      ],
      "schema:name": "Gridded measurement data cube",
      "schema:contentUrl": "http://example.com/data/measurement-cube.nc",
      "schema:encodingFormat": [
        "application/x-netcdf"
      ],
      "spdx:checksum": {
        "@type": [
          "spdx:Checksum"
        ],
        "spdx:algorithm": "SHA256",
        "spdx:checksumValue": "f6e5d4c3b2a1f6e5d4c3b2a1f6e5d4c3b2a1f6e5d4c3b2a1f6e5d4c3b2a1f6e5"
      },
      "cdif:hasPhysicalMapping": [
        {
          "cdif:format": "decimal",
          "cdif:physicalDataType": "float32",
          "cdi:locator": "/measurements/wavelength",
          "cdi:nullSequence": "NaN",
          "cdi:isRequired": true,
          "cdif:formats_InstanceVariable": {
            "@id": "ex:KJTFKurNFu"
          }
        },
        {
          "cdif:format": "decimal",
          "cdif:physicalDataType": "float32",
          "cdi:locator": "/measurements/intensity",
          "cdi:scale": 1000,
          "cdi:decimalPositions": 6,
          "cdi:isRequired": true,
          "cdif:formats_InstanceVariable": {
            "@id": "ex:OjHgIDO"
          }
        }
      ],
      "dcterms:conformsTo": [
        {
          "@id": "http://www.opengis.net/def/nil/OGC/0/missing"
        }
      ]
    },
    {
      "@type": [
        "schema:WebAPI"
      ],
      "schema:serviceType": {
        "@type": [
          "schema:DefinedTerm"
        ],
        "schema:name": "OGC API - Features",
        "schema:identifier": {
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": "https://www.ogc.org/standards",
          "schema:value": "ogcapi-features-1",
          "schema:url": "https://www.ogc.org/standard/ogcapi-features/"
        },
        "schema:inDefinedTermSet": "https://www.ogc.org/standards",
        "schema:termCode": "ogcapi-features"
      },
      "schema:termsOfService": "Open access, no authentication required",
      "schema:documentation": {
        "@type": [
          "schema:CreativeWork",
          "dcat:Relationship"
        ],
        "schema:name": "OpenAPI specification for geochemistry data service",
        "schema:url": "http://example.com/api/v1/openapi.json"
      },
      "schema:potentialAction": [
        {
          "@type": [
            "schema:Action"
          ],
          "schema:name": "Query geochemistry features",
          "schema:target": {
            "@type": [
              "schema:EntryPoint"
            ],
            "schema:description": "OGC API Features endpoint returning geochemistry observations as CSV",
            "schema:urlTemplate": "http://example.com/api/v1/collections/geochem/items?f={format}&limit={limit}&offset={offset}",
            "schema:httpMethod": [
              "GET"
            ],
            "schema:contentType": [
              "text/csv",
              "application/geo+json"
            ]
          },
          "schema:result": {
            "@type": [
              "schema:DataDownload",
              "cdi:TabularTextDataSet",
              "cdi:PhysicalDataSet"
            ],
            "schema:name": "Geochemistry query results",
            "schema:contentUrl": "http://example.com/api/v1/collections/geochem/items?f=csv",
            "schema:encodingFormat": [
              "text/csv"
            ],
            "cdi:characterSet": "UTF-8",
            "cdif:fileSize": 0.8,
            "cdif:fileSizeUofM": "MB",
            "cdi:isDelimited": true,
            "csvw:delimiter": ",",
            "csvw:header": true,
            "csvw:headerRowCount": 1,
            "cdif:hasPhysicalMapping": [
              {
                "cdif:index": 0,
                "cdif:format": "decimal",
                "cdif:physicalDataType": "float64",
                "cdi:isRequired": true,
                "cdif:formats_InstanceVariable": {
                  "@id": "ex:KJTFKurNFu"
                }
              },
              {
                "cdif:index": 1,
                "cdif:format": "decimal",
                "cdif:physicalDataType": "float64",
                "cdi:isRequired": false,
                "cdif:formats_InstanceVariable": {
                  "@id": "ex:OjHgIDO"
                }
              }
            ],
            "dcterms:conformsTo": [
              {
                "@id": "http://www.opengis.net/def/nil/OGC/0/missing"
              }
            ]
          },
          "schema:object": {
            "@type": [
              "schema:DataFeed"
            ],
            "schema:description": "Geochemistry observations collection"
          },
          "schema:query-input": [
            {
              "@type": [
                "schema:PropertyValueSpecification"
              ],
              "schema:valueName": "format",
              "schema:description": "Response format: csv or geojson",
              "schema:valueRequired": false,
              "schema:valuePattern": "csv|geojson"
            },
            {
              "@type": [
                "schema:PropertyValueSpecification"
              ],
              "schema:valueName": "limit",
              "schema:description": "Maximum number of features to return (default 100)",
              "schema:valueRequired": false
            },
            {
              "@type": [
                "schema:PropertyValueSpecification"
              ],
              "schema:valueName": "offset",
              "schema:description": "Starting index for pagination",
              "schema:valueRequired": false
            }
          ]
        }
      ]
    }
  ],
  "schema:variableMeasured": [
    {
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "@id": "ex:KJTFKurNFu",
      "schema:name": "RbMivCtraTmzms",
      "schema:description": "EcbPmKQnMCgWozw",
      "schema:propertyID": [
        "urn:test:GigjbPysIJ",
        "https://ark.org/bXEOCTwvICRc"
      ],
      "schema:measurementTechnique": "some measurement technique",
      "schema:unitText": "furlongs",
      "schema:unitCode": "F",
      "schema:minValue": 67.0,
      "schema:maxValue": 98.0,
      "schema:url": "http://example.com/resource?foo=bar#furlong",
      "cdi:identifier": "ex:KJTFKurNFu",
      "cdif:physicalDataType": [
        "float64"
      ],
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
      "cdif:role": "Measure",
      "cdif:name": [
        "RbMivCtraTmzms"
      ],
      "cdif:displayLabel": [
        "Sea Water Temperature"
      ],
      "cdi:describedUnitOfMeasure": {
        "@type": [
          "schema:DefinedTerm"
        ],
        "schema:name": "degree Celsius",
        "schema:identifier": "http://qudt.org/vocab/unit/DEG_C",
        "schema:inDefinedTermSet": "http://qudt.org/vocab/unit/"
      },
      "cdi:simpleUnitOfMeasure": "Cel",
      "cdif:uses": [
        {
          "@id": "http://vocab.nerc.ac.uk/collection/P01/current/TEMPST01/"
        }
      ]
    },
    {
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "@id": "ex:OjHgIDO",
      "schema:name": "jzgZCegiTFYBSmsSh",
      "schema:description": "RGKBMBkScTTNQ",
      "schema:propertyID": [
        "urn:properties:tzysaGTv",
        "ex:CUXfWZLdRkEAG"
      ],
      "schema:measurementTechnique": {
        "@type": [
          "schema:DefinedTerm"
        ],
        "schema:name": "a good technique",
        "schema:identifier": {
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": "https://identifiers.org",
          "schema:value": "igcJkZMJiKehgkPjMCp",
          "schema:url": "https://identifiers.org/technique/igcJkZMJiKehgkPjMCp"
        },
        "schema:inDefinedTermSet": "https://identifiers.org/technique/vocabulary",
        "schema:termCode": "agt"
      },
      "schema:unitText": "stone",
      "schema:unitCode": "S",
      "schema:minValue": 36.0,
      "schema:maxValue": 74.0,
      "schema:url": "http://example.com/resource?foo=bar#stone",
      "cdi:identifier": "ex:OjHgIDO",
      "cdif:physicalDataType": [
        "float32"
      ],
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#float",
      "cdif:role": "Dimension",
      "cdif:name": [
        "jzgZCegiTFYBSmsSh"
      ],
      "cdif:displayLabel": [
        "Measurement Depth"
      ],
      "cdi:simpleUnitOfMeasure": "m",
      "cdi:qualifies": {
        "@id": "ex:KJTFKurNFu"
      }
    }
  ],
  "schema:measurementTechnique": [
    "Conductivity-Temperature-Depth (CTD) profiler",
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:name": "CTD profiler",
      "schema:identifier": "https://example.org/techniques/ctd",
      "schema:inDefinedTermSet": "https://example.org/techniques",
      "schema:termCode": "ctd"
    }
  ],
  "schema:spatialCoverage": [
    {
      "@type": [
        "schema:Place"
      ],
      "schema:name": "Gulf of Maine",
      "schema:identifier": "https://www.geonames.org/4965561",
      "schema:additionalType": [
        "marine-region"
      ],
      "schema:alternateName": [
        "Maine Gulf"
      ],
      "schema:geo": {
        "@type": [
          "schema:GeoShape"
        ],
        "schema:box": "41.0 -71.0 45.0 -65.0"
      },
      "geosparql:hasGeometry": {
        "@type": [
          "sf:Polygon"
        ],
        "geosparql:asWKT": {
          "@type": [
            "geosparql:wktLiteral"
          ],
          "@value": "POLYGON((-71 41,-65 41,-65 45,-71 45,-71 41))"
        },
        "geosparql:crs": {
          "@id": "http://www.opengis.net/def/crs/OGC/1.3/CRS84"
        }
      }
    },
    {
      "@type": [
        "schema:Place"
      ],
      "schema:name": "Station GoM-A1",
      "schema:geo": {
        "@type": [
          "schema:GeoCoordinates"
        ],
        "schema:latitude": 43.5,
        "schema:longitude": -68.0
      }
    }
  ],
  "schema:temporalCoverage": [
    "2024-01-01/2025-09-01",
    {
      "@context": {
        "time": "http://www.w3.org/2006/time#",
        "schema": "http://schema.org/"
      },
      "@type": [
        "time:ProperInterval"
      ],
      "schema:description": "Monitoring window for ocean temperature 2024-2025 release",
      "time:hasBeginning": {
        "@type": [
          "time:Instant"
        ],
        "time:inTimePosition": {
          "@type": [
            "time:TimePosition"
          ],
          "time:hasTRS": "http://www.opengis.net/def/uom/ISO-8601/0/Gregorian",
          "time:numericPosition": 2024.0
        }
      },
      "time:hasEnd": {
        "@type": [
          "time:Instant"
        ],
        "time:inTimePosition": {
          "@type": [
            "time:TimePosition"
          ],
          "time:hasTRS": "http://www.opengis.net/def/uom/ISO-8601/0/Gregorian",
          "time:numericPosition": 2025.67
        }
      }
    }
  ],
  "dqv:hasQualityMeasurement": [
    {
      "@type": [
        "dqv:QualityMeasurement"
      ],
      "dqv:isMeasurementOf": "completeness",
      "dqv:value": "0.987"
    },
    {
      "@type": [
        "dqv:QualityMeasurement"
      ],
      "dqv:isMeasurementOf": {
        "@id": "https://example.org/quality/temperatureAccuracy"
      },
      "dqv:value": {
        "@type": [
          "schema:DefinedTerm"
        ],
        "schema:name": "high accuracy",
        "schema:identifier": "https://example.org/quality/levels/high",
        "schema:termCode": "HIGH"
      }
    },
    {
      "@type": [
        "dqv:QualityMeasurement"
      ],
      "dqv:isMeasurementOf": {
        "@type": [
          "schema:DefinedTerm"
        ],
        "schema:name": "QARTOD primary level pass rate",
        "schema:identifier": "https://example.org/quality/qartod-pass-rate"
      },
      "dqv:value": "0.96"
    }
  ],
  "schema:subjectOf": {
    "@type": [
      "schema:Dataset"
    ],
    "schema:additionalType": [
      "dcat:CatalogRecord"
    ],
    "@id": "ex:BAaR",
    "schema:about": {
      "@id": "ex:YOPx"
    },
    "dcterms:conformsTo": [
      {
        "@id": "https://w3id.org/cdif/bbr/metadata/profiles/cdifCompositeProfile/BasicDataDescription"
      },
      {
        "@id": "https://w3id.org/cdif/manifest/1.0"
      },
      {
        "@id": "https://w3id.org/cdif/core/1.0"
      },
      {
        "@id": "https://w3id.org/cdif/discovery/1.0"
      },
      {
        "@id": "https://w3id.org/cdif/data_description/1.0"
      }
    ],
    "schema:maintainer": {
      "@id": "ex:PersonExample_zZc",
      "@type": [
        "schema:Person"
      ],
      "schema:name": "Joe Test",
      "schema:alternateName": "Test, Joe",
      "schema:affiliation": {
        "@id": "ex:maintainerAffiliation_3456",
        "@type": [
          "schema:Organization"
        ],
        "schema:name": "Test organization"
      },
      "schema:description": "Metadata specialist, based in Portland, Maine",
      "schema:identifier": {
        "@id": "ex:maintainerIdentifier_3456",
        "@type": [
          "schema:PropertyValue"
        ],
        "schema:propertyID": "https://doi.org",
        "schema:value": "iY",
        "schema:url": "https://doi.org/iY"
      },
      "schema:contactPoint": {
        "@id": "ex:maintainerContactPoint_3456",
        "@type": [
          "schema:ContactPoint"
        ],
        "schema:email": "joe@bmanuco.org"
      },
      "schema:sameAs": [
        "https://ark.org/46737",
        "uri:test:43737"
      ]
    },
    "schema:sdDatePublished": "2025-10-25",
    "schema:includedInDataCatalog": {
      "@id": "ex:lIZkH",
      "@type": [
        "schema:DataCatalog"
      ],
      "schema:name": "naEEWHEjgvNFJy",
      "schema:url": "http://example.com/resource?foo=bar#fragment",
      "schema:identifier": {
        "@type": [
          "schema:PropertyValue"
        ],
        "schema:propertyID": "ex:fGSg",
        "schema:value": "vPADlYJkJuGgI",
        "schema:url": "http://example.com/resource?foo=bar#fragment"
      }
    }
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
      "dcterms": "http://purl.org/dc/terms/",
      "spdx": "http://spdx.org/rdf/terms#"
    },
    "https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/profiles/cdifCompositeProfile/BasicDataDescription/context.jsonld",
    {
      "schema": "http://schema.org/",
      "dcterms": "http://purl.org/dc/terms/",
      "geosparql": "http://www.opengis.net/ont/geosparql#",
      "sf": "http://www.opengis.net/ont/sf#",
      "spdx": "http://spdx.org/rdf/terms#",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "cdif": "https://cdif.org/0.1/",
      "csvw": "http://www.w3.org/ns/csvw#",
      "dqv": "http://www.w3.org/ns/dqv#",
      "time": "http://www.w3.org/2006/time#",
      "ex": "https://example.org/",
      "xsd": "http://www.w3.org/2001/XMLSchema#",
      "dcat": "http://www.w3.org/ns/dcat#",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:YOPx",
  "@type": [
    "schema:Dataset"
  ],
  "schema:name": "Test dataset",
  "schema:description": "Auto generated from JSON schema, values are gobbledegoop. For testing",
  "schema:additionalType": [
    "test data description"
  ],
  "schema:identifier": {
    "@type": [
      "schema:PropertyValue"
    ],
    "schema:propertyID": "uSNzhqeEQPKhCj",
    "schema:url": "http://identifiers.org/sandbox/uSNzhqeEQPKhCj"
  },
  "schema:sameAs": [
    {
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": "urn:idorg:test",
      "schema:value": "urn:idorg:test:p45689"
    }
  ],
  "schema:version": "OVVAYgJhmFkXyVyedlVo",
  "schema:url": "http://example.com/resource?foo=bar#fragment",
  "schema:inLanguage": "bYiJT",
  "schema:dateModified": "2020-10-15",
  "schema:datePublished": "2021-09-05",
  "schema:conditionsOfAccess": [
    "ihYojbwJyw",
    "jNv",
    "LCY",
    "tfmbDGeiuEnuhfKBvk"
  ],
  "schema:license": [
    "dXhuFoqL",
    "Kmp"
  ],
  "schema:relatedLink": [
    {
      "@type": [
        "schema:LinkRole"
      ],
      "schema:linkRelationship": "lfCzUaoftdtTPAhMnpC",
      "target": {
        "@type": [
          "schema:EntryPoint"
        ],
        "schema:encodingFormat": "gompgHAN",
        "schema:name": "oAuxEutsTEiB",
        "schema:url": "http://example.com/resource?foo=bar#fragment"
      }
    },
    {
      "@type": [
        "schema:LinkRole"
      ],
      "schema:linkRelationship": "BOoRREnpDEUrdNaV",
      "target": {
        "@type": [
          "schema:EntryPoint"
        ],
        "schema:encodingFormat": "FNoslhw",
        "schema:name": "atsDYJxuhHpivqLmw",
        "schema:url": "http://example.com/resource?foo=bar#fragment"
      }
    }
  ],
  "schema:publishingPrinciples": [
    "rxZsrPAbJrIGGgDVJ"
  ],
  "schema:keywords": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:name": "MiSqvcp",
      "schema:identifier": {
        "@type": [
          "schema:PropertyValue"
        ],
        "schema:propertyID": "ex:rIPXjaCPQX",
        "schema:value": "PVSajGtBPsLzeCTLv",
        "schema:url": "http://example.com/resource/PVSajGtBPsLzeCTLvt"
      },
      "schema:inDefinedTermSet": "EfagQEQtAkwMBDvfKznc",
      "schema:termCode": "bzOl"
    },
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:name": "TiMuawt",
      "schema:identifier": {
        "@type": [
          "schema:PropertyValue"
        ],
        "schema:propertyID": "https://resource.org/identifier",
        "schema:value": "tdUMYBItIwdJe",
        "schema:url": "http://example.com/resource/tdUMYBItIwdJe"
      },
      "schema:inDefinedTermSet": "sqH",
      "schema:termCode": "RUUxHY"
    }
  ],
  "schema:creator": {
    "@list": [
      {
        "@id": "ex:mxxInaV",
        "@type": [
          "schema:Organization"
        ],
        "schema:name": "AEbcNvM",
        "schema:alternateName": "MwsoNGVEp",
        "schema:affiliation": {
          "@id": "ex:xblzSwEYJKBPpkK",
          "@type": [
            "schema:Organization"
          ],
          "schema:additionalType": [
            "schema:GovernmentOrganization",
            "schema:ResearchOrganization",
            "schema:ResearchOrganization",
            "schema:Project"
          ],
          "schema:name": "mDjEBamofgiqGBqfQGfe",
          "schema:alternateName": "TrAuXgjTOCmJVTaf",
          "schema:description": "wwcOQoCbUe",
          "schema:identifier": {
            "@type": [
              "schema:PropertyValue"
            ],
            "schema:propertyID": "oyvigoDvYFCGEkFc",
            "schema:value": "tMxtQyCUFptzpXj",
            "schema:url": "http://example.com/resource?foo=bar#fragment"
          },
          "schema:sameAs": [
            "K",
            "AsoXEfDoLipcJw"
          ]
        },
        "schema:contactPoint": {
          "@type": [
            "schema:ContactPoint"
          ],
          "schema:email": "tready@email.ocm"
        },
        "schema:description": "ypZ",
        "schema:identifier": {
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": "ciZyuOzfhVSPdWi",
          "schema:value": "JqLmJhoyFPhsmW",
          "schema:url": "http://example.com/resource?foo=bar#fragment"
        },
        "schema:sameAs": [
          "ex:pMPylNhiMvfC",
          "ex:IgH"
        ]
      },
      {
        "@id": "ex:jP",
        "@type": [
          "schema:Person"
        ],
        "schema:name": "Doe, Jane",
        "schema:contactPoint": {
          "@type": [
            "schema:ContactPoint"
          ],
          "schema:email": "jdoe@example.org"
        }
      }
    ]
  },
  "schema:contributor": [
    {
      "@type": [
        "schema:Role"
      ],
      "schema:roleName": "editor",
      "schema:contributor": {
        "@id": "ex:PersonExample_zZc_asContributor",
        "@type": [
          "schema:Person"
        ],
        "schema:name": "Joe B. Test",
        "schema:alternateName": "Test, J. B.",
        "schema:affiliation": {
          "@type": [
            "schema:Organization"
          ],
          "schema:name": "The Big Manufacturing Co."
        },
        "schema:description": "Metadata specialist, based in Portland, Maine",
        "schema:identifier": {
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": "https://orcid.org",
          "schema:value": "iY",
          "schema:url": "https://orcid.org/iY"
        },
        "schema:contactPoint": {
          "@type": [
            "schema:ContactPoint"
          ],
          "schema:email": "joe@bmanuco.org"
        },
        "schema:sameAs": [
          "https://ark.org/46737",
          "uri:test:43737"
        ]
      }
    },
    {
      "@id": "ex:NyMWPlRtQizAFE"
    }
  ],
  "schema:publisher": {
    "@id": "ex:exampleOrg_fW",
    "@type": [
      "schema:Organization"
    ],
    "schema:additionalType": [
      "schema:ResearchOrganization",
      "university"
    ],
    "schema:name": "University of Arizona",
    "schema:alternateName": "UAz",
    "schema:description": "University in Tucson, Arizona",
    "schema:identifier": {
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": "https://registry.identifiers.org/registry/ror",
      "schema:value": "03m2x1q45",
      "schema:url": "https://ror.org/03m2x1q45"
    },
    "schema:sameAs": [
      "Wildcats"
    ]
  },
  "schema:provider": [
    {
      "@id": "ex:gDiAxjl",
      "@type": [
        "schema:Organization"
      ],
      "schema:name": "Example Data Center"
    },
    {
      "@id": "ex:ihjJtFPNEKnGSFBcgS",
      "@type": [
        "schema:Person"
      ],
      "schema:name": "Smith, Robert",
      "schema:contactPoint": {
        "@type": [
          "schema:ContactPoint"
        ],
        "schema:email": "rsmith@example.org"
      }
    },
    {
      "@id": "https://ada.org/person/5489",
      "@type": [
        "schema:Person"
      ],
      "schema:contactPoint": {
        "@type": [
          "schema:ContactPoint"
        ],
        "schema:email": "a.king@nhm.ac.uk"
      },
      "schema:identifier": {
        "@type": [
          "schema:PropertyValue"
        ],
        "schema:propertyID": "https://orcid.org",
        "schema:value": "0000-0001-6113-5417",
        "schema:url": "https://orcid.org/0000-0001-6113-5417"
      },
      "schema:name": "King, Ashley"
    }
  ],
  "schema:funding": [
    {
      "@type": [
        "schema:MonetaryGrant"
      ],
      "schema:identifier": {
        "@type": [
          "schema:PropertyValue"
        ],
        "schema:propertyID": "grant-id",
        "schema:value": "lieopgXuumP"
      },
      "schema:name": "fhhbzh",
      "schema:funder": {
        "@id": "https://ror.org/3572wjht"
      }
    },
    {
      "@type": [
        "schema:MonetaryGrant"
      ],
      "schema:identifier": {
        "@type": [
          "schema:PropertyValue"
        ],
        "schema:propertyID": "grant-id",
        "schema:value": "fMuiBjneudpV"
      },
      "schema:name": "MWoPQAqRYHobey",
      "schema:funder": {
        "@id": "https://ror.org/fnjrj68"
      }
    },
    {
      "@type": [
        "schema:MonetaryGrant"
      ],
      "schema:identifier": {
        "@type": [
          "schema:PropertyValue"
        ],
        "schema:propertyID": "grant-id",
        "schema:value": "LZpo"
      },
      "schema:name": "ekckpBtI",
      "schema:funder": {
        "@id": "https://ror.org/sejer4w6u8"
      }
    }
  ],
  "schema:distribution": [
    {
      "@type": [
        "schema:DataDownload",
        "cdi:PhysicalDataSet"
      ],
      "schema:name": "VwuIdrCrJSsrGATePg",
      "schema:contentUrl": "http://example.com/resource?foo=bar#fragment",
      "schema:encodingFormat": [
        "text/csv"
      ],
      "spdx:checksum": {
        "@type": [
          "spdx:Checksum"
        ],
        "spdx:algorithm": "MD5",
        "spdx:checksumValue": "MITGLcmBjeFYWmjP"
      },
      "schema:provider": [
        {
          "@id": "ex:ABYcNWHKYhTiLLNEzJx",
          "@type": [
            "schema:Person"
          ],
          "schema:name": "Walker, Longin",
          "schema:alternateName": "LWH",
          "schema:affiliation": {
            "@id": "ex:corzCgjNrGcH",
            "@type": [
              "schema:Organization"
            ],
            "schema:additionalType": [
              "schema:NGO"
            ],
            "schema:name": "Some Data Repository",
            "schema:alternateName": "leJqYoxQIH",
            "schema:description": "vRzzUAmtNWLgZcgNIC",
            "schema:identifier": {
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": "KSgJJfyAuQPEX",
              "schema:value": "iFSyBdjVAxHmFOZVFg"
            },
            "schema:sameAs": [
              "ex:ITXGFU",
              "urn:test:WWcBivQCAO"
            ]
          },
          "schema:contactPoint": {
            "@type": [
              "schema:ContactPoint"
            ],
            "schema:email": "tom@ngo.net"
          },
          "schema:description": "Data Curator",
          "schema:identifier": {
            "@type": [
              "schema:PropertyValue"
            ],
            "schema:propertyID": "https://identifiers.org/orcid",
            "schema:value": "NfaMinUfHeMDEFNc",
            "schema:url": "http://orcid.org/NfaMinUfHeMDEFNc"
          }
        }
      ],
      "dcterms:conformsTo": [
        {
          "@id": "http://www.opengis.net/def/nil/OGC/0/missing"
        }
      ]
    },
    {
      "@type": [
        "schema:DataDownload",
        "cdi:PhysicalDataSet"
      ],
      "schema:name": "MVMpmnCGAggEnsoEgJXH",
      "schema:contentUrl": "http://example.com/resource?foo=bar#fragment",
      "schema:encodingFormat": [
        "tNdpXaJgDeWbFkNM",
        "kpZDvhyVo",
        "sMUGwSqxWzJOYEb"
      ],
      "spdx:checksum": {
        "@type": [
          "spdx:Checksum"
        ],
        "spdx:algorithm": "j",
        "spdx:checksumValue": "h"
      },
      "schema:provider": [
        {
          "@id": "ex:kNKPZsCSWMc",
          "@type": [
            "schema:Organization"
          ],
          "schema:name": "SdeMvoPFxEaJOvQy",
          "schema:alternateName": "WFcslOjvGZY",
          "schema:description": "ztcLdOAkQTKSPLZ",
          "schema:identifier": {
            "@type": [
              "schema:PropertyValue"
            ],
            "schema:propertyID": "ex:oFIYAymjuGCPjDnSgmB",
            "schema:url": "http://example.com/resource/WPfhCJyxiDcwgdHMemJd"
          }
        },
        {
          "@id": "ex:sr68lgy",
          "@type": [
            "schema:Organization"
          ],
          "schema:name": "Another Provider Org"
        }
      ],
      "dcterms:conformsTo": [
        {
          "@id": "http://www.opengis.net/def/nil/OGC/0/missing"
        }
      ]
    },
    {
      "@type": [
        "schema:DataDownload",
        "cdi:TabularTextDataSet",
        "cdi:PhysicalDataSet"
      ],
      "schema:name": "Geochemistry analysis results",
      "schema:contentUrl": "http://example.com/data/geochem-results.csv",
      "schema:encodingFormat": [
        "text/csv"
      ],
      "spdx:checksum": {
        "@type": [
          "spdx:Checksum"
        ],
        "spdx:algorithm": "SHA256",
        "spdx:checksumValue": "a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4e5f6a1b2"
      },
      "cdi:characterSet": "UTF-8",
      "cdif:fileSize": 4.6,
      "cdif:fileSizeUofM": "MB",
      "cdi:isDelimited": true,
      "csvw:delimiter": ",",
      "csvw:header": true,
      "csvw:headerRowCount": 1,
      "csvw:commentPrefix": "#",
      "csvw:skipRows": 0,
      "csvw:skipBlankRows": true,
      "csvw:quoteChar": "\"",
      "countRows": 461,
      "countColumns": 2,
      "cdif:hasPhysicalMapping": [
        {
          "cdif:index": 0,
          "cdif:format": "decimal",
          "cdif:physicalDataType": "float64",
          "cdi:nullSequence": "NA",
          "cdi:isRequired": true,
          "cdif:formats_InstanceVariable": {
            "@id": "ex:KJTFKurNFu"
          }
        },
        {
          "cdif:index": 1,
          "cdif:format": "decimal",
          "cdif:physicalDataType": "float64",
          "cdi:nullSequence": "-9999",
          "cdi:defaultValue": "0.0",
          "cdi:decimalPositions": 4,
          "cdi:isRequired": false,
          "cdif:formats_InstanceVariable": {
            "@id": "ex:OjHgIDO"
          }
        }
      ],
      "dcterms:conformsTo": [
        {
          "@id": "http://www.opengis.net/def/nil/OGC/0/missing"
        }
      ]
    },
    {
      "@type": [
        "schema:DataDownload",
        "cdi:StructuredDataSet",
        "cdi:PhysicalDataSet"
      ],
      "schema:name": "Gridded measurement data cube",
      "schema:contentUrl": "http://example.com/data/measurement-cube.nc",
      "schema:encodingFormat": [
        "application/x-netcdf"
      ],
      "spdx:checksum": {
        "@type": [
          "spdx:Checksum"
        ],
        "spdx:algorithm": "SHA256",
        "spdx:checksumValue": "f6e5d4c3b2a1f6e5d4c3b2a1f6e5d4c3b2a1f6e5d4c3b2a1f6e5d4c3b2a1f6e5"
      },
      "cdif:hasPhysicalMapping": [
        {
          "cdif:format": "decimal",
          "cdif:physicalDataType": "float32",
          "cdi:locator": "/measurements/wavelength",
          "cdi:nullSequence": "NaN",
          "cdi:isRequired": true,
          "cdif:formats_InstanceVariable": {
            "@id": "ex:KJTFKurNFu"
          }
        },
        {
          "cdif:format": "decimal",
          "cdif:physicalDataType": "float32",
          "cdi:locator": "/measurements/intensity",
          "cdi:scale": 1000,
          "cdi:decimalPositions": 6,
          "cdi:isRequired": true,
          "cdif:formats_InstanceVariable": {
            "@id": "ex:OjHgIDO"
          }
        }
      ],
      "dcterms:conformsTo": [
        {
          "@id": "http://www.opengis.net/def/nil/OGC/0/missing"
        }
      ]
    },
    {
      "@type": [
        "schema:WebAPI"
      ],
      "schema:serviceType": {
        "@type": [
          "schema:DefinedTerm"
        ],
        "schema:name": "OGC API - Features",
        "schema:identifier": {
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": "https://www.ogc.org/standards",
          "schema:value": "ogcapi-features-1",
          "schema:url": "https://www.ogc.org/standard/ogcapi-features/"
        },
        "schema:inDefinedTermSet": "https://www.ogc.org/standards",
        "schema:termCode": "ogcapi-features"
      },
      "schema:termsOfService": "Open access, no authentication required",
      "schema:documentation": {
        "@type": [
          "schema:CreativeWork",
          "dcat:Relationship"
        ],
        "schema:name": "OpenAPI specification for geochemistry data service",
        "schema:url": "http://example.com/api/v1/openapi.json"
      },
      "schema:potentialAction": [
        {
          "@type": [
            "schema:Action"
          ],
          "schema:name": "Query geochemistry features",
          "schema:target": {
            "@type": [
              "schema:EntryPoint"
            ],
            "schema:description": "OGC API Features endpoint returning geochemistry observations as CSV",
            "schema:urlTemplate": "http://example.com/api/v1/collections/geochem/items?f={format}&limit={limit}&offset={offset}",
            "schema:httpMethod": [
              "GET"
            ],
            "schema:contentType": [
              "text/csv",
              "application/geo+json"
            ]
          },
          "schema:result": {
            "@type": [
              "schema:DataDownload",
              "cdi:TabularTextDataSet",
              "cdi:PhysicalDataSet"
            ],
            "schema:name": "Geochemistry query results",
            "schema:contentUrl": "http://example.com/api/v1/collections/geochem/items?f=csv",
            "schema:encodingFormat": [
              "text/csv"
            ],
            "cdi:characterSet": "UTF-8",
            "cdif:fileSize": 0.8,
            "cdif:fileSizeUofM": "MB",
            "cdi:isDelimited": true,
            "csvw:delimiter": ",",
            "csvw:header": true,
            "csvw:headerRowCount": 1,
            "cdif:hasPhysicalMapping": [
              {
                "cdif:index": 0,
                "cdif:format": "decimal",
                "cdif:physicalDataType": "float64",
                "cdi:isRequired": true,
                "cdif:formats_InstanceVariable": {
                  "@id": "ex:KJTFKurNFu"
                }
              },
              {
                "cdif:index": 1,
                "cdif:format": "decimal",
                "cdif:physicalDataType": "float64",
                "cdi:isRequired": false,
                "cdif:formats_InstanceVariable": {
                  "@id": "ex:OjHgIDO"
                }
              }
            ],
            "dcterms:conformsTo": [
              {
                "@id": "http://www.opengis.net/def/nil/OGC/0/missing"
              }
            ]
          },
          "schema:object": {
            "@type": [
              "schema:DataFeed"
            ],
            "schema:description": "Geochemistry observations collection"
          },
          "schema:query-input": [
            {
              "@type": [
                "schema:PropertyValueSpecification"
              ],
              "schema:valueName": "format",
              "schema:description": "Response format: csv or geojson",
              "schema:valueRequired": false,
              "schema:valuePattern": "csv|geojson"
            },
            {
              "@type": [
                "schema:PropertyValueSpecification"
              ],
              "schema:valueName": "limit",
              "schema:description": "Maximum number of features to return (default 100)",
              "schema:valueRequired": false
            },
            {
              "@type": [
                "schema:PropertyValueSpecification"
              ],
              "schema:valueName": "offset",
              "schema:description": "Starting index for pagination",
              "schema:valueRequired": false
            }
          ]
        }
      ]
    }
  ],
  "schema:variableMeasured": [
    {
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "@id": "ex:KJTFKurNFu",
      "schema:name": "RbMivCtraTmzms",
      "schema:description": "EcbPmKQnMCgWozw",
      "schema:propertyID": [
        "urn:test:GigjbPysIJ",
        "https://ark.org/bXEOCTwvICRc"
      ],
      "schema:measurementTechnique": "some measurement technique",
      "schema:unitText": "furlongs",
      "schema:unitCode": "F",
      "schema:minValue": 67.0,
      "schema:maxValue": 98.0,
      "schema:url": "http://example.com/resource?foo=bar#furlong",
      "cdi:identifier": "ex:KJTFKurNFu",
      "cdif:physicalDataType": [
        "float64"
      ],
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
      "cdif:role": "Measure",
      "cdif:name": [
        "RbMivCtraTmzms"
      ],
      "cdif:displayLabel": [
        "Sea Water Temperature"
      ],
      "cdi:describedUnitOfMeasure": {
        "@type": [
          "schema:DefinedTerm"
        ],
        "schema:name": "degree Celsius",
        "schema:identifier": "http://qudt.org/vocab/unit/DEG_C",
        "schema:inDefinedTermSet": "http://qudt.org/vocab/unit/"
      },
      "cdi:simpleUnitOfMeasure": "Cel",
      "cdif:uses": [
        {
          "@id": "http://vocab.nerc.ac.uk/collection/P01/current/TEMPST01/"
        }
      ]
    },
    {
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "@id": "ex:OjHgIDO",
      "schema:name": "jzgZCegiTFYBSmsSh",
      "schema:description": "RGKBMBkScTTNQ",
      "schema:propertyID": [
        "urn:properties:tzysaGTv",
        "ex:CUXfWZLdRkEAG"
      ],
      "schema:measurementTechnique": {
        "@type": [
          "schema:DefinedTerm"
        ],
        "schema:name": "a good technique",
        "schema:identifier": {
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": "https://identifiers.org",
          "schema:value": "igcJkZMJiKehgkPjMCp",
          "schema:url": "https://identifiers.org/technique/igcJkZMJiKehgkPjMCp"
        },
        "schema:inDefinedTermSet": "https://identifiers.org/technique/vocabulary",
        "schema:termCode": "agt"
      },
      "schema:unitText": "stone",
      "schema:unitCode": "S",
      "schema:minValue": 36.0,
      "schema:maxValue": 74.0,
      "schema:url": "http://example.com/resource?foo=bar#stone",
      "cdi:identifier": "ex:OjHgIDO",
      "cdif:physicalDataType": [
        "float32"
      ],
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#float",
      "cdif:role": "Dimension",
      "cdif:name": [
        "jzgZCegiTFYBSmsSh"
      ],
      "cdif:displayLabel": [
        "Measurement Depth"
      ],
      "cdi:simpleUnitOfMeasure": "m",
      "cdi:qualifies": {
        "@id": "ex:KJTFKurNFu"
      }
    }
  ],
  "schema:measurementTechnique": [
    "Conductivity-Temperature-Depth (CTD) profiler",
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:name": "CTD profiler",
      "schema:identifier": "https://example.org/techniques/ctd",
      "schema:inDefinedTermSet": "https://example.org/techniques",
      "schema:termCode": "ctd"
    }
  ],
  "schema:spatialCoverage": [
    {
      "@type": [
        "schema:Place"
      ],
      "schema:name": "Gulf of Maine",
      "schema:identifier": "https://www.geonames.org/4965561",
      "schema:additionalType": [
        "marine-region"
      ],
      "schema:alternateName": [
        "Maine Gulf"
      ],
      "schema:geo": {
        "@type": [
          "schema:GeoShape"
        ],
        "schema:box": "41.0 -71.0 45.0 -65.0"
      },
      "geosparql:hasGeometry": {
        "@type": [
          "sf:Polygon"
        ],
        "geosparql:asWKT": {
          "@type": [
            "geosparql:wktLiteral"
          ],
          "@value": "POLYGON((-71 41,-65 41,-65 45,-71 45,-71 41))"
        },
        "geosparql:crs": {
          "@id": "http://www.opengis.net/def/crs/OGC/1.3/CRS84"
        }
      }
    },
    {
      "@type": [
        "schema:Place"
      ],
      "schema:name": "Station GoM-A1",
      "schema:geo": {
        "@type": [
          "schema:GeoCoordinates"
        ],
        "schema:latitude": 43.5,
        "schema:longitude": -68.0
      }
    }
  ],
  "schema:temporalCoverage": [
    "2024-01-01/2025-09-01",
    {
      "@context": {
        "time": "http://www.w3.org/2006/time#",
        "schema": "http://schema.org/"
      },
      "@type": [
        "time:ProperInterval"
      ],
      "schema:description": "Monitoring window for ocean temperature 2024-2025 release",
      "time:hasBeginning": {
        "@type": [
          "time:Instant"
        ],
        "time:inTimePosition": {
          "@type": [
            "time:TimePosition"
          ],
          "time:hasTRS": "http://www.opengis.net/def/uom/ISO-8601/0/Gregorian",
          "time:numericPosition": 2024.0
        }
      },
      "time:hasEnd": {
        "@type": [
          "time:Instant"
        ],
        "time:inTimePosition": {
          "@type": [
            "time:TimePosition"
          ],
          "time:hasTRS": "http://www.opengis.net/def/uom/ISO-8601/0/Gregorian",
          "time:numericPosition": 2025.67
        }
      }
    }
  ],
  "dqv:hasQualityMeasurement": [
    {
      "@type": [
        "dqv:QualityMeasurement"
      ],
      "dqv:isMeasurementOf": "completeness",
      "dqv:value": "0.987"
    },
    {
      "@type": [
        "dqv:QualityMeasurement"
      ],
      "dqv:isMeasurementOf": {
        "@id": "https://example.org/quality/temperatureAccuracy"
      },
      "dqv:value": {
        "@type": [
          "schema:DefinedTerm"
        ],
        "schema:name": "high accuracy",
        "schema:identifier": "https://example.org/quality/levels/high",
        "schema:termCode": "HIGH"
      }
    },
    {
      "@type": [
        "dqv:QualityMeasurement"
      ],
      "dqv:isMeasurementOf": {
        "@type": [
          "schema:DefinedTerm"
        ],
        "schema:name": "QARTOD primary level pass rate",
        "schema:identifier": "https://example.org/quality/qartod-pass-rate"
      },
      "dqv:value": "0.96"
    }
  ],
  "schema:subjectOf": {
    "@type": [
      "schema:Dataset"
    ],
    "schema:additionalType": [
      "dcat:CatalogRecord"
    ],
    "@id": "ex:BAaR",
    "schema:about": {
      "@id": "ex:YOPx"
    },
    "dcterms:conformsTo": [
      {
        "@id": "https://w3id.org/cdif/bbr/metadata/profiles/cdifCompositeProfile/BasicDataDescription"
      },
      {
        "@id": "https://w3id.org/cdif/manifest/1.0"
      },
      {
        "@id": "https://w3id.org/cdif/core/1.0"
      },
      {
        "@id": "https://w3id.org/cdif/discovery/1.0"
      },
      {
        "@id": "https://w3id.org/cdif/data_description/1.0"
      }
    ],
    "schema:maintainer": {
      "@id": "ex:PersonExample_zZc",
      "@type": [
        "schema:Person"
      ],
      "schema:name": "Joe Test",
      "schema:alternateName": "Test, Joe",
      "schema:affiliation": {
        "@id": "ex:maintainerAffiliation_3456",
        "@type": [
          "schema:Organization"
        ],
        "schema:name": "Test organization"
      },
      "schema:description": "Metadata specialist, based in Portland, Maine",
      "schema:identifier": {
        "@id": "ex:maintainerIdentifier_3456",
        "@type": [
          "schema:PropertyValue"
        ],
        "schema:propertyID": "https://doi.org",
        "schema:value": "iY",
        "schema:url": "https://doi.org/iY"
      },
      "schema:contactPoint": {
        "@id": "ex:maintainerContactPoint_3456",
        "@type": [
          "schema:ContactPoint"
        ],
        "schema:email": "joe@bmanuco.org"
      },
      "schema:sameAs": [
        "https://ark.org/46737",
        "uri:test:43737"
      ]
    },
    "schema:sdDatePublished": "2025-10-25",
    "schema:includedInDataCatalog": {
      "@id": "ex:lIZkH",
      "@type": [
        "schema:DataCatalog"
      ],
      "schema:name": "naEEWHEjgvNFJy",
      "schema:url": "http://example.com/resource?foo=bar#fragment",
      "schema:identifier": {
        "@type": [
          "schema:PropertyValue"
        ],
        "schema:propertyID": "ex:fGSg",
        "schema:value": "vPADlYJkJuGgI",
        "schema:url": "http://example.com/resource?foo=bar#fragment"
      }
    }
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
@prefix dqv: <http://www.w3.org/ns/dqv#> .
@prefix ex: <https://example.org/> .
@prefix geosparql: <http://www.opengis.net/ont/geosparql#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix schema1: <http://schema.org/> .
@prefix sf: <http://www.opengis.net/ont/sf#> .
@prefix spdx: <http://spdx.org/rdf/terms#> .
@prefix time: <http://www.w3.org/2006/time#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<https://ada.org/person/5489> a schema1:Person ;
    schema1:contactPoint [ a schema1:ContactPoint ;
            schema1:email "a.king@nhm.ac.uk" ] ;
    schema1:identifier [ a schema1:PropertyValue ;
            schema1:propertyID "https://orcid.org" ;
            schema1:url "https://orcid.org/0000-0001-6113-5417" ;
            schema1:value "0000-0001-6113-5417" ] ;
    schema1:name "King, Ashley" .

ex:ABYcNWHKYhTiLLNEzJx a schema1:Person ;
    schema1:affiliation ex:corzCgjNrGcH ;
    schema1:alternateName "LWH" ;
    schema1:contactPoint [ a schema1:ContactPoint ;
            schema1:email "tom@ngo.net" ] ;
    schema1:description "Data Curator" ;
    schema1:identifier [ a schema1:PropertyValue ;
            schema1:propertyID "https://identifiers.org/orcid" ;
            schema1:url "http://orcid.org/NfaMinUfHeMDEFNc" ;
            schema1:value "NfaMinUfHeMDEFNc" ] ;
    schema1:name "Walker, Longin" .

ex:BAaR a schema1:Dataset ;
    dcterms:conformsTo <https://w3id.org/cdif/bbr/metadata/profiles/cdifCompositeProfile/BasicDataDescription>,
        <https://w3id.org/cdif/core/1.0>,
        <https://w3id.org/cdif/data_description/1.0>,
        <https://w3id.org/cdif/discovery/1.0>,
        <https://w3id.org/cdif/manifest/1.0> ;
    schema1:about ex:YOPx ;
    schema1:additionalType "dcat:CatalogRecord" ;
    schema1:includedInDataCatalog ex:lIZkH ;
    schema1:maintainer ex:PersonExample_zZc ;
    schema1:sdDatePublished "2025-10-25" .

ex:PersonExample_zZc a schema1:Person ;
    schema1:affiliation ex:maintainerAffiliation_3456 ;
    schema1:alternateName "Test, Joe" ;
    schema1:contactPoint ex:maintainerContactPoint_3456 ;
    schema1:description "Metadata specialist, based in Portland, Maine" ;
    schema1:identifier ex:maintainerIdentifier_3456 ;
    schema1:name "Joe Test" ;
    schema1:sameAs "https://ark.org/46737",
        "uri:test:43737" .

ex:PersonExample_zZc_asContributor a schema1:Person ;
    schema1:affiliation [ a schema1:Organization ;
            schema1:name "The Big Manufacturing Co." ] ;
    schema1:alternateName "Test, J. B." ;
    schema1:contactPoint [ a schema1:ContactPoint ;
            schema1:email "joe@bmanuco.org" ] ;
    schema1:description "Metadata specialist, based in Portland, Maine" ;
    schema1:identifier [ a schema1:PropertyValue ;
            schema1:propertyID "https://orcid.org" ;
            schema1:url "https://orcid.org/iY" ;
            schema1:value "iY" ] ;
    schema1:name "Joe B. Test" ;
    schema1:sameAs "https://ark.org/46737",
        "uri:test:43737" .

ex:YOPx a schema1:Dataset ;
    schema1:additionalType "test data description" ;
    schema1:conditionsOfAccess "LCY",
        "ihYojbwJyw",
        "jNv",
        "tfmbDGeiuEnuhfKBvk" ;
    schema1:contributor [ a schema1:Role ;
            schema1:contributor ex:PersonExample_zZc_asContributor ;
            schema1:roleName "editor" ],
        ex:NyMWPlRtQizAFE ;
    schema1:creator ( ex:mxxInaV ex:jP ) ;
    schema1:dateModified "2020-10-15" ;
    schema1:datePublished "2021-09-05" ;
    schema1:description "Auto generated from JSON schema, values are gobbledegoop. For testing" ;
    schema1:distribution [ a cdi:PhysicalDataSet,
                schema1:DataDownload ;
            dcterms:conformsTo <http://www.opengis.net/def/nil/OGC/0/missing> ;
            schema1:contentUrl "http://example.com/resource?foo=bar#fragment" ;
            schema1:encodingFormat "kpZDvhyVo",
                "sMUGwSqxWzJOYEb",
                "tNdpXaJgDeWbFkNM" ;
            schema1:name "MVMpmnCGAggEnsoEgJXH" ;
            schema1:provider ex:kNKPZsCSWMc,
                ex:sr68lgy ;
            spdx:checksum [ a spdx:Checksum ;
                    spdx:algorithm "j" ;
                    spdx:checksumValue "h" ] ],
        [ a cdi:PhysicalDataSet,
                cdi:StructuredDataSet,
                schema1:DataDownload ;
            dcterms:conformsTo <http://www.opengis.net/def/nil/OGC/0/missing> ;
            schema1:contentUrl "http://example.com/data/measurement-cube.nc" ;
            schema1:encodingFormat "application/x-netcdf" ;
            schema1:name "Gridded measurement data cube" ;
            spdx:checksum [ a spdx:Checksum ;
                    spdx:algorithm "SHA256" ;
                    spdx:checksumValue "f6e5d4c3b2a1f6e5d4c3b2a1f6e5d4c3b2a1f6e5d4c3b2a1f6e5d4c3b2a1f6e5" ] ;
            cdif:hasPhysicalMapping [ cdi:isRequired true ;
                    cdi:locator "/measurements/wavelength" ;
                    cdi:nullSequence "NaN" ;
                    cdif:format "decimal" ;
                    cdif:formats_InstanceVariable ex:KJTFKurNFu ;
                    cdif:physicalDataType "float32" ],
                [ cdi:decimalPositions 6 ;
                    cdi:isRequired true ;
                    cdi:locator "/measurements/intensity" ;
                    cdi:scale 1000 ;
                    cdif:format "decimal" ;
                    cdif:formats_InstanceVariable ex:OjHgIDO ;
                    cdif:physicalDataType "float32" ] ],
        [ a cdi:PhysicalDataSet,
                schema1:DataDownload ;
            dcterms:conformsTo <http://www.opengis.net/def/nil/OGC/0/missing> ;
            schema1:contentUrl "http://example.com/resource?foo=bar#fragment" ;
            schema1:encodingFormat "text/csv" ;
            schema1:name "VwuIdrCrJSsrGATePg" ;
            schema1:provider ex:ABYcNWHKYhTiLLNEzJx ;
            spdx:checksum [ a spdx:Checksum ;
                    spdx:algorithm "MD5" ;
                    spdx:checksumValue "MITGLcmBjeFYWmjP" ] ],
        [ a schema1:WebAPI ;
            schema1:documentation [ a schema1:CreativeWork,
                        dcat:Relationship ;
                    schema1:name "OpenAPI specification for geochemistry data service" ;
                    schema1:url "http://example.com/api/v1/openapi.json" ] ;
            schema1:potentialAction [ a schema1:Action ;
                    schema1:name "Query geochemistry features" ;
                    schema1:object [ a schema1:DataFeed ;
                            schema1:description "Geochemistry observations collection" ] ;
                    schema1:query-input [ a schema1:PropertyValueSpecification ;
                            schema1:description "Starting index for pagination" ;
                            schema1:valueName "offset" ;
                            schema1:valueRequired false ],
                        [ a schema1:PropertyValueSpecification ;
                            schema1:description "Maximum number of features to return (default 100)" ;
                            schema1:valueName "limit" ;
                            schema1:valueRequired false ],
                        [ a schema1:PropertyValueSpecification ;
                            schema1:description "Response format: csv or geojson" ;
                            schema1:valueName "format" ;
                            schema1:valuePattern "csv|geojson" ;
                            schema1:valueRequired false ] ;
                    schema1:result [ a cdi:PhysicalDataSet,
                                cdi:TabularTextDataSet,
                                schema1:DataDownload ;
                            cdi:characterSet "UTF-8" ;
                            cdi:isDelimited true ;
                            dcterms:conformsTo <http://www.opengis.net/def/nil/OGC/0/missing> ;
                            schema1:contentUrl "http://example.com/api/v1/collections/geochem/items?f=csv" ;
                            schema1:encodingFormat "text/csv" ;
                            schema1:name "Geochemistry query results" ;
                            csvw:delimiter "," ;
                            csvw:header true ;
                            csvw:headerRowCount 1 ;
                            cdif:fileSize 8e-01 ;
                            cdif:fileSizeUofM "MB" ;
                            cdif:hasPhysicalMapping [ cdi:isRequired false ;
                                    cdif:format "decimal" ;
                                    cdif:formats_InstanceVariable ex:OjHgIDO ;
                                    cdif:index 1 ;
                                    cdif:physicalDataType "float64" ],
                                [ cdi:isRequired true ;
                                    cdif:format "decimal" ;
                                    cdif:formats_InstanceVariable ex:KJTFKurNFu ;
                                    cdif:index 0 ;
                                    cdif:physicalDataType "float64" ] ] ;
                    schema1:target [ a schema1:EntryPoint ;
                            schema1:contentType "application/geo+json",
                                "text/csv" ;
                            schema1:description "OGC API Features endpoint returning geochemistry observations as CSV" ;
                            schema1:httpMethod "GET" ;
                            schema1:urlTemplate "http://example.com/api/v1/collections/geochem/items?f={format}&limit={limit}&offset={offset}" ] ] ;
            schema1:serviceType [ a schema1:DefinedTerm ;
                    schema1:identifier [ a schema1:PropertyValue ;
                            schema1:propertyID "https://www.ogc.org/standards" ;
                            schema1:url "https://www.ogc.org/standard/ogcapi-features/" ;
                            schema1:value "ogcapi-features-1" ] ;
                    schema1:inDefinedTermSet "https://www.ogc.org/standards" ;
                    schema1:name "OGC API - Features" ;
                    schema1:termCode "ogcapi-features" ] ;
            schema1:termsOfService "Open access, no authentication required" ],
        [ a cdi:PhysicalDataSet,
                cdi:TabularTextDataSet,
                schema1:DataDownload ;
            cdi:characterSet "UTF-8" ;
            cdi:isDelimited true ;
            dcterms:conformsTo <http://www.opengis.net/def/nil/OGC/0/missing> ;
            schema1:contentUrl "http://example.com/data/geochem-results.csv" ;
            schema1:encodingFormat "text/csv" ;
            schema1:name "Geochemistry analysis results" ;
            spdx:checksum [ a spdx:Checksum ;
                    spdx:algorithm "SHA256" ;
                    spdx:checksumValue "a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4e5f6a1b2" ] ;
            csvw:commentPrefix "#" ;
            csvw:delimiter "," ;
            csvw:header true ;
            csvw:headerRowCount 1 ;
            csvw:quoteChar "\"" ;
            csvw:skipBlankRows true ;
            csvw:skipRows 0 ;
            cdif:fileSize 4.6e+00 ;
            cdif:fileSizeUofM "MB" ;
            cdif:hasPhysicalMapping [ cdi:decimalPositions 4 ;
                    cdi:defaultValue "0.0" ;
                    cdi:isRequired false ;
                    cdi:nullSequence "-9999" ;
                    cdif:format "decimal" ;
                    cdif:formats_InstanceVariable ex:OjHgIDO ;
                    cdif:index 1 ;
                    cdif:physicalDataType "float64" ],
                [ cdi:isRequired true ;
                    cdi:nullSequence "NA" ;
                    cdif:format "decimal" ;
                    cdif:formats_InstanceVariable ex:KJTFKurNFu ;
                    cdif:index 0 ;
                    cdif:physicalDataType "float64" ] ] ;
    schema1:funding [ a schema1:MonetaryGrant ;
            schema1:funder <https://ror.org/sejer4w6u8> ;
            schema1:identifier [ a schema1:PropertyValue ;
                    schema1:propertyID "grant-id" ;
                    schema1:value "LZpo" ] ;
            schema1:name "ekckpBtI" ],
        [ a schema1:MonetaryGrant ;
            schema1:funder <https://ror.org/3572wjht> ;
            schema1:identifier [ a schema1:PropertyValue ;
                    schema1:propertyID "grant-id" ;
                    schema1:value "lieopgXuumP" ] ;
            schema1:name "fhhbzh" ],
        [ a schema1:MonetaryGrant ;
            schema1:funder <https://ror.org/fnjrj68> ;
            schema1:identifier [ a schema1:PropertyValue ;
                    schema1:propertyID "grant-id" ;
                    schema1:value "fMuiBjneudpV" ] ;
            schema1:name "MWoPQAqRYHobey" ] ;
    schema1:identifier [ a schema1:PropertyValue ;
            schema1:propertyID "uSNzhqeEQPKhCj" ;
            schema1:url "http://identifiers.org/sandbox/uSNzhqeEQPKhCj" ] ;
    schema1:inLanguage "bYiJT" ;
    schema1:keywords [ a schema1:DefinedTerm ;
            schema1:identifier [ a schema1:PropertyValue ;
                    schema1:propertyID "ex:rIPXjaCPQX" ;
                    schema1:url "http://example.com/resource/PVSajGtBPsLzeCTLvt" ;
                    schema1:value "PVSajGtBPsLzeCTLv" ] ;
            schema1:inDefinedTermSet "EfagQEQtAkwMBDvfKznc" ;
            schema1:name "MiSqvcp" ;
            schema1:termCode "bzOl" ],
        [ a schema1:DefinedTerm ;
            schema1:identifier [ a schema1:PropertyValue ;
                    schema1:propertyID "https://resource.org/identifier" ;
                    schema1:url "http://example.com/resource/tdUMYBItIwdJe" ;
                    schema1:value "tdUMYBItIwdJe" ] ;
            schema1:inDefinedTermSet "sqH" ;
            schema1:name "TiMuawt" ;
            schema1:termCode "RUUxHY" ] ;
    schema1:license "Kmp",
        "dXhuFoqL" ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:identifier "https://example.org/techniques/ctd" ;
            schema1:inDefinedTermSet "https://example.org/techniques" ;
            schema1:name "CTD profiler" ;
            schema1:termCode "ctd" ],
        "Conductivity-Temperature-Depth (CTD) profiler" ;
    schema1:name "Test dataset" ;
    schema1:provider <https://ada.org/person/5489>,
        ex:gDiAxjl,
        ex:ihjJtFPNEKnGSFBcgS ;
    schema1:publisher ex:exampleOrg_fW ;
    schema1:publishingPrinciples "rxZsrPAbJrIGGgDVJ" ;
    schema1:relatedLink [ a schema1:LinkRole ;
            schema1:linkRelationship "BOoRREnpDEUrdNaV" ],
        [ a schema1:LinkRole ;
            schema1:linkRelationship "lfCzUaoftdtTPAhMnpC" ] ;
    schema1:sameAs [ a schema1:PropertyValue ;
            schema1:propertyID "urn:idorg:test" ;
            schema1:value "urn:idorg:test:p45689" ] ;
    schema1:spatialCoverage [ a schema1:Place ;
            schema1:geo [ a schema1:GeoCoordinates ;
                    schema1:latitude 4.35e+01 ;
                    schema1:longitude -6.8e+01 ] ;
            schema1:name "Station GoM-A1" ],
        [ a schema1:Place ;
            schema1:additionalType "marine-region" ;
            schema1:alternateName "Maine Gulf" ;
            schema1:geo [ a schema1:GeoShape ;
                    schema1:box "41.0 -71.0 45.0 -65.0" ] ;
            schema1:identifier "https://www.geonames.org/4965561" ;
            schema1:name "Gulf of Maine" ;
            geosparql:hasGeometry [ a sf:Polygon ;
                    geosparql:asWKT "POLYGON((-71 41,-65 41,-65 45,-71 45,-71 41))"^^<['geosparql:wktLiteral']> ;
                    geosparql:crs <http://www.opengis.net/def/crs/OGC/1.3/CRS84> ] ] ;
    schema1:subjectOf ex:BAaR ;
    schema1:temporalCoverage [ a time:ProperInterval ;
            schema1:description "Monitoring window for ocean temperature 2024-2025 release" ;
            time:hasBeginning [ a time:Instant ;
                    time:inTimePosition [ a time:TimePosition ;
                            time:hasTRS "http://www.opengis.net/def/uom/ISO-8601/0/Gregorian" ;
                            time:numericPosition 2.024e+03 ] ] ;
            time:hasEnd [ a time:Instant ;
                    time:inTimePosition [ a time:TimePosition ;
                            time:hasTRS "http://www.opengis.net/def/uom/ISO-8601/0/Gregorian" ;
                            time:numericPosition 2.02567e+03 ] ] ],
        "2024-01-01/2025-09-01" ;
    schema1:url "http://example.com/resource?foo=bar#fragment" ;
    schema1:variableMeasured ex:KJTFKurNFu,
        ex:OjHgIDO ;
    schema1:version "OVVAYgJhmFkXyVyedlVo" ;
    dqv:hasQualityMeasurement [ a dqv:QualityMeasurement ;
            dqv:isMeasurementOf [ a schema1:DefinedTerm ;
                    schema1:identifier "https://example.org/quality/qartod-pass-rate" ;
                    schema1:name "QARTOD primary level pass rate" ] ;
            dqv:value "0.96" ],
        [ a dqv:QualityMeasurement ;
            dqv:isMeasurementOf <https://example.org/quality/temperatureAccuracy> ;
            dqv:value [ a schema1:DefinedTerm ;
                    schema1:identifier "https://example.org/quality/levels/high" ;
                    schema1:name "high accuracy" ;
                    schema1:termCode "HIGH" ] ],
        [ a dqv:QualityMeasurement ;
            dqv:isMeasurementOf "completeness" ;
            dqv:value "0.987" ] .

ex:corzCgjNrGcH a schema1:Organization ;
    schema1:additionalType "schema:NGO" ;
    schema1:alternateName "leJqYoxQIH" ;
    schema1:description "vRzzUAmtNWLgZcgNIC" ;
    schema1:identifier [ a schema1:PropertyValue ;
            schema1:propertyID "KSgJJfyAuQPEX" ;
            schema1:value "iFSyBdjVAxHmFOZVFg" ] ;
    schema1:name "Some Data Repository" ;
    schema1:sameAs "ex:ITXGFU",
        "urn:test:WWcBivQCAO" .

ex:exampleOrg_fW a schema1:Organization ;
    schema1:additionalType "schema:ResearchOrganization",
        "university" ;
    schema1:alternateName "UAz" ;
    schema1:description "University in Tucson, Arizona" ;
    schema1:identifier [ a schema1:PropertyValue ;
            schema1:propertyID "https://registry.identifiers.org/registry/ror" ;
            schema1:url "https://ror.org/03m2x1q45" ;
            schema1:value "03m2x1q45" ] ;
    schema1:name "University of Arizona" ;
    schema1:sameAs "Wildcats" .

ex:gDiAxjl a schema1:Organization ;
    schema1:name "Example Data Center" .

ex:ihjJtFPNEKnGSFBcgS a schema1:Person ;
    schema1:contactPoint [ a schema1:ContactPoint ;
            schema1:email "rsmith@example.org" ] ;
    schema1:name "Smith, Robert" .

ex:jP a schema1:Person ;
    schema1:contactPoint [ a schema1:ContactPoint ;
            schema1:email "jdoe@example.org" ] ;
    schema1:name "Doe, Jane" .

ex:kNKPZsCSWMc a schema1:Organization ;
    schema1:alternateName "WFcslOjvGZY" ;
    schema1:description "ztcLdOAkQTKSPLZ" ;
    schema1:identifier [ a schema1:PropertyValue ;
            schema1:propertyID "ex:oFIYAymjuGCPjDnSgmB" ;
            schema1:url "http://example.com/resource/WPfhCJyxiDcwgdHMemJd" ] ;
    schema1:name "SdeMvoPFxEaJOvQy" .

ex:lIZkH a schema1:DataCatalog ;
    schema1:identifier [ a schema1:PropertyValue ;
            schema1:propertyID "ex:fGSg" ;
            schema1:url "http://example.com/resource?foo=bar#fragment" ;
            schema1:value "vPADlYJkJuGgI" ] ;
    schema1:name "naEEWHEjgvNFJy" ;
    schema1:url "http://example.com/resource?foo=bar#fragment" .

ex:maintainerAffiliation_3456 a schema1:Organization ;
    schema1:name "Test organization" .

ex:maintainerContactPoint_3456 a schema1:ContactPoint ;
    schema1:email "joe@bmanuco.org" .

ex:maintainerIdentifier_3456 a schema1:PropertyValue ;
    schema1:propertyID "https://doi.org" ;
    schema1:url "https://doi.org/iY" ;
    schema1:value "iY" .

ex:mxxInaV a schema1:Organization ;
    schema1:affiliation ex:xblzSwEYJKBPpkK ;
    schema1:alternateName "MwsoNGVEp" ;
    schema1:contactPoint [ a schema1:ContactPoint ;
            schema1:email "tready@email.ocm" ] ;
    schema1:description "ypZ" ;
    schema1:identifier [ a schema1:PropertyValue ;
            schema1:propertyID "ciZyuOzfhVSPdWi" ;
            schema1:url "http://example.com/resource?foo=bar#fragment" ;
            schema1:value "JqLmJhoyFPhsmW" ] ;
    schema1:name "AEbcNvM" ;
    schema1:sameAs "ex:IgH",
        "ex:pMPylNhiMvfC" .

ex:sr68lgy a schema1:Organization ;
    schema1:name "Another Provider Org" .

ex:xblzSwEYJKBPpkK a schema1:Organization ;
    schema1:additionalType "schema:GovernmentOrganization",
        "schema:Project",
        "schema:ResearchOrganization" ;
    schema1:alternateName "TrAuXgjTOCmJVTaf" ;
    schema1:description "wwcOQoCbUe" ;
    schema1:identifier [ a schema1:PropertyValue ;
            schema1:propertyID "oyvigoDvYFCGEkFc" ;
            schema1:url "http://example.com/resource?foo=bar#fragment" ;
            schema1:value "tMxtQyCUFptzpXj" ] ;
    schema1:name "mDjEBamofgiqGBqfQGfe" ;
    schema1:sameAs "AsoXEfDoLipcJw",
        "K" .

ex:OjHgIDO a cdi:InstanceVariable,
        schema1:PropertyValue ;
    cdi:identifier "ex:OjHgIDO" ;
    cdi:intendedDataType "https://www.w3.org/TR/xmlschema-2/#float" ;
    cdi:qualifies ex:KJTFKurNFu ;
    cdi:simpleUnitOfMeasure "m" ;
    schema1:description "RGKBMBkScTTNQ" ;
    schema1:maxValue 7.4e+01 ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:identifier [ a schema1:PropertyValue ;
                    schema1:propertyID "https://identifiers.org" ;
                    schema1:url "https://identifiers.org/technique/igcJkZMJiKehgkPjMCp" ;
                    schema1:value "igcJkZMJiKehgkPjMCp" ] ;
            schema1:inDefinedTermSet "https://identifiers.org/technique/vocabulary" ;
            schema1:name "a good technique" ;
            schema1:termCode "agt" ] ;
    schema1:minValue 3.6e+01 ;
    schema1:name "jzgZCegiTFYBSmsSh" ;
    schema1:propertyID "ex:CUXfWZLdRkEAG",
        "urn:properties:tzysaGTv" ;
    schema1:unitCode "S" ;
    schema1:unitText "stone" ;
    schema1:url "http://example.com/resource?foo=bar#stone" ;
    cdif:displayLabel "Measurement Depth" ;
    cdif:name "jzgZCegiTFYBSmsSh" ;
    cdif:physicalDataType "float32" ;
    cdif:role "Dimension" .

ex:KJTFKurNFu a cdi:InstanceVariable,
        schema1:PropertyValue ;
    cdi:describedUnitOfMeasure [ a schema1:DefinedTerm ;
            schema1:identifier "http://qudt.org/vocab/unit/DEG_C" ;
            schema1:inDefinedTermSet "http://qudt.org/vocab/unit/" ;
            schema1:name "degree Celsius" ] ;
    cdi:identifier "ex:KJTFKurNFu" ;
    cdi:intendedDataType "https://www.w3.org/TR/xmlschema-2/#decimal" ;
    cdi:simpleUnitOfMeasure "Cel" ;
    schema1:description "EcbPmKQnMCgWozw" ;
    schema1:maxValue 9.8e+01 ;
    schema1:measurementTechnique "some measurement technique" ;
    schema1:minValue 6.7e+01 ;
    schema1:name "RbMivCtraTmzms" ;
    schema1:propertyID "https://ark.org/bXEOCTwvICRc",
        "urn:test:GigjbPysIJ" ;
    schema1:unitCode "F" ;
    schema1:unitText "furlongs" ;
    schema1:url "http://example.com/resource?foo=bar#furlong" ;
    cdif:displayLabel "Sea Water Temperature" ;
    cdif:name "RbMivCtraTmzms" ;
    cdif:physicalDataType "float64" ;
    cdif:role "Measure" ;
    cdif:uses <http://vocab.nerc.ac.uk/collection/P01/current/TEMPST01/> .


```


### Dimensional (data cube) example.
Gridded sea-water temperature in a single NetCDF file. The distribution is
typed as cdi:StructuredDataSet and the four dimension variables (time, depth,
latitude, longitude) plus the temperature measure are declared as
InstanceVariables with cdif:role of Dimension or Measure. Physical mappings
use cdi:locator to point at the NetCDF variable paths.
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "dcterms": "http://purl.org/dc/terms/",
    "dcat": "http://www.w3.org/ns/dcat#",
    "prov": "http://www.w3.org/ns/prov#",
    "spdx": "http://spdx.org/rdf/terms#",
    "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
    "ex": "https://example.org/",
    "cdif": "https://cdif.org/0.1/"
  },
  "@id": "ex:gom-temp-cube-2025",
  "@type": [
    "schema:Dataset"
  ],
  "schema:name": "Gulf of Maine gridded sea temperature, 2024-2025",
  "schema:description": "Monthly sea-water temperature regridded onto a 0.1-degree lat/lon mesh at 24 standard depth levels. Single NetCDF file with a 4-D measurement array indexed by time, depth, latitude, and longitude.",
  "schema:identifier": {
    "@type": [
      "schema:PropertyValue"
    ],
    "schema:propertyID": "https://doi.org",
    "schema:value": "10.5281/zenodo.4242424",
    "schema:url": "https://doi.org/10.5281/zenodo.4242424"
  },
  "schema:version": "1.0.0",
  "schema:dateModified": "2025-10-02",
  "schema:datePublished": "2025-10-15",
  "schema:license": [
    "https://creativecommons.org/licenses/by/4.0/"
  ],
  "schema:keywords": [
    "ocean temperature",
    "Gulf of Maine",
    "gridded data",
    "reanalysis"
  ],
  "schema:creator": {
    "@list": [
      {
        "@id": "https://ror.org/03m2x1q45",
        "@type": [
          "schema:Organization"
        ],
        "schema:name": "University of Arizona"
      }
    ]
  },
  "schema:publisher": {
    "@id": "https://ror.org/03m2x1q45",
    "@type": [
      "schema:Organization"
    ],
    "schema:name": "University of Arizona"
  },
  "schema:distribution": [
    {
      "@type": [
        "schema:DataDownload",
        "cdi:StructuredDataSet",
        "cdi:PhysicalDataSet"
      ],
      "schema:name": "Gulf of Maine temperature cube (NetCDF-4)",
      "schema:contentUrl": "https://example.org/data/gom-temp-cube-2025.nc",
      "schema:encodingFormat": [
        "application/x-netcdf"
      ],
      "cdif:fileSize": 184.6,
      "cdif:fileSizeUofM": "MB",
      "spdx:checksum": {
        "@type": [
          "spdx:Checksum"
        ],
        "spdx:algorithm": "SHA256",
        "spdx:checksumValue": "9f3c1a0b4e8d2f1e7a6c5b4d3a2918f0e1d2c3b4a5968778a9b0c1d2e3f40516"
      },
      "cdif:hasPhysicalMapping": [
        {
          "cdi:locator": "/time",
          "cdif:format": "days since 2024-01-01",
          "cdif:physicalDataType": "int32",
          "cdi:isRequired": true,
          "cdif:formats_InstanceVariable": {
            "@id": "ex:var-time"
          }
        },
        {
          "cdi:locator": "/depth",
          "cdif:format": "decimal",
          "cdif:physicalDataType": "float32",
          "cdi:isRequired": true,
          "cdif:formats_InstanceVariable": {
            "@id": "ex:var-depth"
          }
        },
        {
          "cdi:locator": "/lat",
          "cdif:format": "decimal",
          "cdif:physicalDataType": "float32",
          "cdi:isRequired": true,
          "cdif:formats_InstanceVariable": {
            "@id": "ex:var-lat"
          }
        },
        {
          "cdi:locator": "/lon",
          "cdif:format": "decimal",
          "cdif:physicalDataType": "float32",
          "cdi:isRequired": true,
          "cdif:formats_InstanceVariable": {
            "@id": "ex:var-lon"
          }
        },
        {
          "cdi:locator": "/temperature",
          "cdif:format": "decimal",
          "cdif:physicalDataType": "float32",
          "cdi:nullSequence": "NaN",
          "cdi:isRequired": true,
          "cdif:formats_InstanceVariable": {
            "@id": "ex:var-temperature"
          }
        }
      ]
    }
  ],
  "schema:variableMeasured": [
    {
      "@id": "ex:var-time",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "time",
      "schema:description": "Mid-month timestamp of the monthly mean field.",
      "cdif:physicalDataType": [
        "int32"
      ],
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#date",
      "cdif:role": "Dimension",
      "cdif:displayLabel": [
        "Time"
      ],
      "cdif:simpleUnitOfMeasure": "d",
      "cdi:describedUnitOfMeasure": {
        "@type": [
          "schema:DefinedTerm"
        ],
        "schema:name": "days since 2024-01-01",
        "schema:identifier": "http://www.opengis.net/def/uom/ISO-8601/0/Gregorian"
      }
    },
    {
      "@id": "ex:var-depth",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "depth",
      "schema:description": "Standard ocean depth level below sea surface.",
      "cdif:physicalDataType": [
        "float32"
      ],
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#float",
      "cdif:role": "Dimension",
      "schema:minValue": 0.0,
      "schema:maxValue": 4000.0,
      "cdif:displayLabel": [
        "Depth below sea surface"
      ],
      "cdif:simpleUnitOfMeasure": "m",
      "cdif:uses": [
        {
          "@id": "http://vocab.nerc.ac.uk/collection/P01/current/DEPHPR01/"
        }
      ]
    },
    {
      "@id": "ex:var-lat",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "latitude",
      "schema:description": "Cell-centre latitude (WGS84).",
      "cdif:physicalDataType": [
        "float32"
      ],
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#float",
      "cdif:role": "Dimension",
      "schema:minValue": 41.0,
      "schema:maxValue": 45.0,
      "cdif:displayLabel": [
        "Latitude"
      ],
      "cdif:simpleUnitOfMeasure": "deg",
      "cdif:uses": [
        {
          "@id": "http://vocab.nerc.ac.uk/collection/P02/current/SDN_LAT/"
        }
      ]
    },
    {
      "@id": "ex:var-lon",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "longitude",
      "schema:description": "Cell-centre longitude (WGS84).",
      "cdif:physicalDataType": [
        "float32"
      ],
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#float",
      "cdif:role": "Dimension",
      "schema:minValue": -71.0,
      "schema:maxValue": -65.0,
      "cdif:displayLabel": [
        "Longitude"
      ],
      "cdif:simpleUnitOfMeasure": "deg",
      "cdif:uses": [
        {
          "@id": "http://vocab.nerc.ac.uk/collection/P02/current/SDN_LON/"
        }
      ]
    },
    {
      "@id": "ex:var-temperature",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "sea_water_temperature",
      "schema:description": "Monthly mean in-situ sea-water temperature for the cell.",
      "schema:measurementTechnique": "Optimal interpolation of CTD and ARGO float observations",
      "schema:propertyID": [
        "http://vocab.nerc.ac.uk/collection/P01/current/TEMPST01/"
      ],
      "cdif:physicalDataType": [
        "float32"
      ],
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#float",
      "cdif:role": "Measure",
      "schema:minValue": -2.0,
      "schema:maxValue": 28.0,
      "cdif:displayLabel": [
        "Sea-water temperature"
      ],
      "cdi:describedUnitOfMeasure": {
        "@type": [
          "schema:DefinedTerm"
        ],
        "schema:name": "degree Celsius",
        "schema:identifier": "http://qudt.org/vocab/unit/DEG_C"
      },
      "cdif:simpleUnitOfMeasure": "Cel",
      "cdif:uses": [
        {
          "@id": "http://vocab.nerc.ac.uk/collection/P01/current/TEMPST01/"
        }
      ]
    }
  ],
  "schema:spatialCoverage": [
    {
      "@type": [
        "schema:Place"
      ],
      "schema:name": "Gulf of Maine",
      "schema:geo": {
        "@type": [
          "schema:GeoShape"
        ],
        "schema:box": "41.0 -71.0 45.0 -65.0"
      }
    }
  ],
  "schema:temporalCoverage": [
    "2024-01-01/2025-09-30"
  ],
  "schema:subjectOf": {
    "@id": "ex:gom-temp-cube-2025/catalog-record",
    "@type": [
      "schema:Dataset"
    ],
    "schema:additionalType": [
      "dcat:CatalogRecord"
    ],
    "schema:about": {
      "@id": "ex:gom-temp-cube-2025"
    },
    "schema:sdDatePublished": "2025-10-15",
    "dcterms:conformsTo": [
      {
        "@id": "https://w3id.org/cdif/core/1.0"
      },
      {
        "@id": "https://w3id.org/cdif/discovery/1.0"
      },
      {
        "@id": "https://w3id.org/cdif/data_description/1.0"
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
      "dcterms": "http://purl.org/dc/terms/",
      "spdx": "http://spdx.org/rdf/terms#"
    },
    "https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/profiles/cdifCompositeProfile/BasicDataDescription/context.jsonld",
    {
      "schema": "http://schema.org/",
      "dcterms": "http://purl.org/dc/terms/",
      "dcat": "http://www.w3.org/ns/dcat#",
      "prov": "http://www.w3.org/ns/prov#",
      "spdx": "http://spdx.org/rdf/terms#",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "ex": "https://example.org/",
      "cdif": "https://cdif.org/0.1/"
    }
  ],
  "@id": "ex:gom-temp-cube-2025",
  "@type": [
    "schema:Dataset"
  ],
  "schema:name": "Gulf of Maine gridded sea temperature, 2024-2025",
  "schema:description": "Monthly sea-water temperature regridded onto a 0.1-degree lat/lon mesh at 24 standard depth levels. Single NetCDF file with a 4-D measurement array indexed by time, depth, latitude, and longitude.",
  "schema:identifier": {
    "@type": [
      "schema:PropertyValue"
    ],
    "schema:propertyID": "https://doi.org",
    "schema:value": "10.5281/zenodo.4242424",
    "schema:url": "https://doi.org/10.5281/zenodo.4242424"
  },
  "schema:version": "1.0.0",
  "schema:dateModified": "2025-10-02",
  "schema:datePublished": "2025-10-15",
  "schema:license": [
    "https://creativecommons.org/licenses/by/4.0/"
  ],
  "schema:keywords": [
    "ocean temperature",
    "Gulf of Maine",
    "gridded data",
    "reanalysis"
  ],
  "schema:creator": {
    "@list": [
      {
        "@id": "https://ror.org/03m2x1q45",
        "@type": [
          "schema:Organization"
        ],
        "schema:name": "University of Arizona"
      }
    ]
  },
  "schema:publisher": {
    "@id": "https://ror.org/03m2x1q45",
    "@type": [
      "schema:Organization"
    ],
    "schema:name": "University of Arizona"
  },
  "schema:distribution": [
    {
      "@type": [
        "schema:DataDownload",
        "cdi:StructuredDataSet",
        "cdi:PhysicalDataSet"
      ],
      "schema:name": "Gulf of Maine temperature cube (NetCDF-4)",
      "schema:contentUrl": "https://example.org/data/gom-temp-cube-2025.nc",
      "schema:encodingFormat": [
        "application/x-netcdf"
      ],
      "cdif:fileSize": 184.6,
      "cdif:fileSizeUofM": "MB",
      "spdx:checksum": {
        "@type": [
          "spdx:Checksum"
        ],
        "spdx:algorithm": "SHA256",
        "spdx:checksumValue": "9f3c1a0b4e8d2f1e7a6c5b4d3a2918f0e1d2c3b4a5968778a9b0c1d2e3f40516"
      },
      "cdif:hasPhysicalMapping": [
        {
          "cdi:locator": "/time",
          "cdif:format": "days since 2024-01-01",
          "cdif:physicalDataType": "int32",
          "cdi:isRequired": true,
          "cdif:formats_InstanceVariable": {
            "@id": "ex:var-time"
          }
        },
        {
          "cdi:locator": "/depth",
          "cdif:format": "decimal",
          "cdif:physicalDataType": "float32",
          "cdi:isRequired": true,
          "cdif:formats_InstanceVariable": {
            "@id": "ex:var-depth"
          }
        },
        {
          "cdi:locator": "/lat",
          "cdif:format": "decimal",
          "cdif:physicalDataType": "float32",
          "cdi:isRequired": true,
          "cdif:formats_InstanceVariable": {
            "@id": "ex:var-lat"
          }
        },
        {
          "cdi:locator": "/lon",
          "cdif:format": "decimal",
          "cdif:physicalDataType": "float32",
          "cdi:isRequired": true,
          "cdif:formats_InstanceVariable": {
            "@id": "ex:var-lon"
          }
        },
        {
          "cdi:locator": "/temperature",
          "cdif:format": "decimal",
          "cdif:physicalDataType": "float32",
          "cdi:nullSequence": "NaN",
          "cdi:isRequired": true,
          "cdif:formats_InstanceVariable": {
            "@id": "ex:var-temperature"
          }
        }
      ]
    }
  ],
  "schema:variableMeasured": [
    {
      "@id": "ex:var-time",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "time",
      "schema:description": "Mid-month timestamp of the monthly mean field.",
      "cdif:physicalDataType": [
        "int32"
      ],
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#date",
      "cdif:role": "Dimension",
      "cdif:displayLabel": [
        "Time"
      ],
      "cdif:simpleUnitOfMeasure": "d",
      "cdi:describedUnitOfMeasure": {
        "@type": [
          "schema:DefinedTerm"
        ],
        "schema:name": "days since 2024-01-01",
        "schema:identifier": "http://www.opengis.net/def/uom/ISO-8601/0/Gregorian"
      }
    },
    {
      "@id": "ex:var-depth",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "depth",
      "schema:description": "Standard ocean depth level below sea surface.",
      "cdif:physicalDataType": [
        "float32"
      ],
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#float",
      "cdif:role": "Dimension",
      "schema:minValue": 0.0,
      "schema:maxValue": 4000.0,
      "cdif:displayLabel": [
        "Depth below sea surface"
      ],
      "cdif:simpleUnitOfMeasure": "m",
      "cdif:uses": [
        {
          "@id": "http://vocab.nerc.ac.uk/collection/P01/current/DEPHPR01/"
        }
      ]
    },
    {
      "@id": "ex:var-lat",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "latitude",
      "schema:description": "Cell-centre latitude (WGS84).",
      "cdif:physicalDataType": [
        "float32"
      ],
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#float",
      "cdif:role": "Dimension",
      "schema:minValue": 41.0,
      "schema:maxValue": 45.0,
      "cdif:displayLabel": [
        "Latitude"
      ],
      "cdif:simpleUnitOfMeasure": "deg",
      "cdif:uses": [
        {
          "@id": "http://vocab.nerc.ac.uk/collection/P02/current/SDN_LAT/"
        }
      ]
    },
    {
      "@id": "ex:var-lon",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "longitude",
      "schema:description": "Cell-centre longitude (WGS84).",
      "cdif:physicalDataType": [
        "float32"
      ],
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#float",
      "cdif:role": "Dimension",
      "schema:minValue": -71.0,
      "schema:maxValue": -65.0,
      "cdif:displayLabel": [
        "Longitude"
      ],
      "cdif:simpleUnitOfMeasure": "deg",
      "cdif:uses": [
        {
          "@id": "http://vocab.nerc.ac.uk/collection/P02/current/SDN_LON/"
        }
      ]
    },
    {
      "@id": "ex:var-temperature",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "sea_water_temperature",
      "schema:description": "Monthly mean in-situ sea-water temperature for the cell.",
      "schema:measurementTechnique": "Optimal interpolation of CTD and ARGO float observations",
      "schema:propertyID": [
        "http://vocab.nerc.ac.uk/collection/P01/current/TEMPST01/"
      ],
      "cdif:physicalDataType": [
        "float32"
      ],
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#float",
      "cdif:role": "Measure",
      "schema:minValue": -2.0,
      "schema:maxValue": 28.0,
      "cdif:displayLabel": [
        "Sea-water temperature"
      ],
      "cdi:describedUnitOfMeasure": {
        "@type": [
          "schema:DefinedTerm"
        ],
        "schema:name": "degree Celsius",
        "schema:identifier": "http://qudt.org/vocab/unit/DEG_C"
      },
      "cdif:simpleUnitOfMeasure": "Cel",
      "cdif:uses": [
        {
          "@id": "http://vocab.nerc.ac.uk/collection/P01/current/TEMPST01/"
        }
      ]
    }
  ],
  "schema:spatialCoverage": [
    {
      "@type": [
        "schema:Place"
      ],
      "schema:name": "Gulf of Maine",
      "schema:geo": {
        "@type": [
          "schema:GeoShape"
        ],
        "schema:box": "41.0 -71.0 45.0 -65.0"
      }
    }
  ],
  "schema:temporalCoverage": [
    "2024-01-01/2025-09-30"
  ],
  "schema:subjectOf": {
    "@id": "ex:gom-temp-cube-2025/catalog-record",
    "@type": [
      "schema:Dataset"
    ],
    "schema:additionalType": [
      "dcat:CatalogRecord"
    ],
    "schema:about": {
      "@id": "ex:gom-temp-cube-2025"
    },
    "schema:sdDatePublished": "2025-10-15",
    "dcterms:conformsTo": [
      {
        "@id": "https://w3id.org/cdif/core/1.0"
      },
      {
        "@id": "https://w3id.org/cdif/discovery/1.0"
      },
      {
        "@id": "https://w3id.org/cdif/data_description/1.0"
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
@prefix ex: <https://example.org/> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix schema1: <http://schema.org/> .
@prefix spdx: <http://spdx.org/rdf/terms#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ex:gom-temp-cube-2025 a schema1:Dataset ;
    schema1:creator ( <https://ror.org/03m2x1q45> ) ;
    schema1:dateModified "2025-10-02" ;
    schema1:datePublished "2025-10-15" ;
    schema1:description "Monthly sea-water temperature regridded onto a 0.1-degree lat/lon mesh at 24 standard depth levels. Single NetCDF file with a 4-D measurement array indexed by time, depth, latitude, and longitude." ;
    schema1:distribution [ a cdi:PhysicalDataSet,
                cdi:StructuredDataSet,
                schema1:DataDownload ;
            schema1:contentUrl "https://example.org/data/gom-temp-cube-2025.nc" ;
            schema1:encodingFormat "application/x-netcdf" ;
            schema1:name "Gulf of Maine temperature cube (NetCDF-4)" ;
            spdx:checksum [ a spdx:Checksum ;
                    spdx:algorithm "SHA256" ;
                    spdx:checksumValue "9f3c1a0b4e8d2f1e7a6c5b4d3a2918f0e1d2c3b4a5968778a9b0c1d2e3f40516" ] ;
            cdif:fileSize 1.846e+02 ;
            cdif:fileSizeUofM "MB" ;
            cdif:hasPhysicalMapping [ cdi:isRequired true ;
                    cdi:locator "/time" ;
                    cdif:format "days since 2024-01-01" ;
                    cdif:formats_InstanceVariable ex:var-time ;
                    cdif:physicalDataType "int32" ],
                [ cdi:isRequired true ;
                    cdi:locator "/temperature" ;
                    cdi:nullSequence "NaN" ;
                    cdif:format "decimal" ;
                    cdif:formats_InstanceVariable ex:var-temperature ;
                    cdif:physicalDataType "float32" ],
                [ cdi:isRequired true ;
                    cdi:locator "/depth" ;
                    cdif:format "decimal" ;
                    cdif:formats_InstanceVariable ex:var-depth ;
                    cdif:physicalDataType "float32" ],
                [ cdi:isRequired true ;
                    cdi:locator "/lon" ;
                    cdif:format "decimal" ;
                    cdif:formats_InstanceVariable ex:var-lon ;
                    cdif:physicalDataType "float32" ],
                [ cdi:isRequired true ;
                    cdi:locator "/lat" ;
                    cdif:format "decimal" ;
                    cdif:formats_InstanceVariable ex:var-lat ;
                    cdif:physicalDataType "float32" ] ] ;
    schema1:identifier [ a schema1:PropertyValue ;
            schema1:propertyID "https://doi.org" ;
            schema1:url "https://doi.org/10.5281/zenodo.4242424" ;
            schema1:value "10.5281/zenodo.4242424" ] ;
    schema1:keywords "Gulf of Maine",
        "gridded data",
        "ocean temperature",
        "reanalysis" ;
    schema1:license "https://creativecommons.org/licenses/by/4.0/" ;
    schema1:name "Gulf of Maine gridded sea temperature, 2024-2025" ;
    schema1:publisher <https://ror.org/03m2x1q45> ;
    schema1:spatialCoverage [ a schema1:Place ;
            schema1:geo [ a schema1:GeoShape ;
                    schema1:box "41.0 -71.0 45.0 -65.0" ] ;
            schema1:name "Gulf of Maine" ] ;
    schema1:subjectOf <https://example.org/gom-temp-cube-2025/catalog-record> ;
    schema1:temporalCoverage "2024-01-01/2025-09-30" ;
    schema1:variableMeasured ex:var-depth,
        ex:var-lat,
        ex:var-lon,
        ex:var-temperature,
        ex:var-time ;
    schema1:version "1.0.0" .

<https://example.org/gom-temp-cube-2025/catalog-record> a schema1:Dataset ;
    dcterms:conformsTo <https://w3id.org/cdif/core/1.0>,
        <https://w3id.org/cdif/data_description/1.0>,
        <https://w3id.org/cdif/discovery/1.0> ;
    schema1:about ex:gom-temp-cube-2025 ;
    schema1:additionalType "dcat:CatalogRecord" ;
    schema1:sdDatePublished "2025-10-15" .

ex:var-depth a cdi:InstanceVariable,
        schema1:PropertyValue ;
    cdi:intendedDataType "https://www.w3.org/TR/xmlschema-2/#float" ;
    schema1:description "Standard ocean depth level below sea surface." ;
    schema1:maxValue 4e+03 ;
    schema1:minValue 0e+00 ;
    schema1:name "depth" ;
    cdif:displayLabel "Depth below sea surface" ;
    cdif:physicalDataType "float32" ;
    cdif:role "Dimension" ;
    cdif:simpleUnitOfMeasure "m" ;
    cdif:uses <http://vocab.nerc.ac.uk/collection/P01/current/DEPHPR01/> .

ex:var-lat a cdi:InstanceVariable,
        schema1:PropertyValue ;
    cdi:intendedDataType "https://www.w3.org/TR/xmlschema-2/#float" ;
    schema1:description "Cell-centre latitude (WGS84)." ;
    schema1:maxValue 4.5e+01 ;
    schema1:minValue 4.1e+01 ;
    schema1:name "latitude" ;
    cdif:displayLabel "Latitude" ;
    cdif:physicalDataType "float32" ;
    cdif:role "Dimension" ;
    cdif:simpleUnitOfMeasure "deg" ;
    cdif:uses <http://vocab.nerc.ac.uk/collection/P02/current/SDN_LAT/> .

ex:var-lon a cdi:InstanceVariable,
        schema1:PropertyValue ;
    cdi:intendedDataType "https://www.w3.org/TR/xmlschema-2/#float" ;
    schema1:description "Cell-centre longitude (WGS84)." ;
    schema1:maxValue -6.5e+01 ;
    schema1:minValue -7.1e+01 ;
    schema1:name "longitude" ;
    cdif:displayLabel "Longitude" ;
    cdif:physicalDataType "float32" ;
    cdif:role "Dimension" ;
    cdif:simpleUnitOfMeasure "deg" ;
    cdif:uses <http://vocab.nerc.ac.uk/collection/P02/current/SDN_LON/> .

ex:var-temperature a cdi:InstanceVariable,
        schema1:PropertyValue ;
    cdi:describedUnitOfMeasure [ a schema1:DefinedTerm ;
            schema1:identifier "http://qudt.org/vocab/unit/DEG_C" ;
            schema1:name "degree Celsius" ] ;
    cdi:intendedDataType "https://www.w3.org/TR/xmlschema-2/#float" ;
    schema1:description "Monthly mean in-situ sea-water temperature for the cell." ;
    schema1:maxValue 2.8e+01 ;
    schema1:measurementTechnique "Optimal interpolation of CTD and ARGO float observations" ;
    schema1:minValue -2e+00 ;
    schema1:name "sea_water_temperature" ;
    schema1:propertyID "http://vocab.nerc.ac.uk/collection/P01/current/TEMPST01/" ;
    cdif:displayLabel "Sea-water temperature" ;
    cdif:physicalDataType "float32" ;
    cdif:role "Measure" ;
    cdif:simpleUnitOfMeasure "Cel" ;
    cdif:uses <http://vocab.nerc.ac.uk/collection/P01/current/TEMPST01/> .

ex:var-time a cdi:InstanceVariable,
        schema1:PropertyValue ;
    cdi:describedUnitOfMeasure [ a schema1:DefinedTerm ;
            schema1:identifier "http://www.opengis.net/def/uom/ISO-8601/0/Gregorian" ;
            schema1:name "days since 2024-01-01" ] ;
    cdi:intendedDataType "https://www.w3.org/TR/xmlschema-2/#date" ;
    schema1:description "Mid-month timestamp of the monthly mean field." ;
    schema1:name "time" ;
    cdif:displayLabel "Time" ;
    cdif:physicalDataType "int32" ;
    cdif:role "Dimension" ;
    cdif:simpleUnitOfMeasure "d" .

<https://ror.org/03m2x1q45> a schema1:Organization ;
    schema1:name "University of Arizona" .


```


### Wide (one row per unit) example.
Monthly water-quality observations in wide form: one row per (station,
sample_date) and one column per measured parameter. Distribution is typed as
cdi:TabularTextDataSet. InstanceVariable roles are UnitIdentifier (station),
Attribute (date), and Measure (pH, temperature, salinity, dissolved oxygen).
cdif:hasPrimaryKey wires the (station, sample_date) composite key.
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "dcterms": "http://purl.org/dc/terms/",
    "dcat": "http://www.w3.org/ns/dcat#",
    "prov": "http://www.w3.org/ns/prov#",
    "spdx": "http://spdx.org/rdf/terms#",
    "csvw": "http://www.w3.org/ns/csvw#",
    "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
    "ex": "https://example.org/",
    "cdif": "https://cdif.org/0.1/"
  },
  "@id": "ex:gom-water-quality-wide-2025",
  "@type": [
    "schema:Dataset"
  ],
  "schema:name": "Gulf of Maine water-quality monitoring stations, 2025 (wide form)",
  "schema:description": "Monthly water-quality observations from 12 monitoring buoys. One row per station-visit; one column per measured parameter (pH, temperature, salinity, dissolved oxygen). Primary key is the (station, sample_date) pair.",
  "schema:identifier": {
    "@type": [
      "schema:PropertyValue"
    ],
    "schema:propertyID": "https://doi.org",
    "schema:value": "10.5281/zenodo.5151515",
    "schema:url": "https://doi.org/10.5281/zenodo.5151515"
  },
  "schema:version": "2025.10",
  "schema:dateModified": "2025-10-20",
  "schema:datePublished": "2025-10-20",
  "schema:license": [
    "https://creativecommons.org/licenses/by/4.0/"
  ],
  "schema:keywords": [
    "water quality",
    "Gulf of Maine",
    "monitoring",
    "wide format"
  ],
  "schema:creator": {
    "@list": [
      {
        "@id": "https://ror.org/03m2x1q45",
        "@type": [
          "schema:Organization"
        ],
        "schema:name": "University of Arizona"
      }
    ]
  },
  "schema:publisher": {
    "@id": "https://ror.org/03m2x1q45",
    "@type": [
      "schema:Organization"
    ],
    "schema:name": "University of Arizona"
  },
  "schema:distribution": [
    {
      "@type": [
        "schema:DataDownload",
        "cdi:TabularTextDataSet",
        "cdi:PhysicalDataSet"
      ],
      "schema:name": "Wide-form water-quality observations (CSV)",
      "schema:contentUrl": "https://example.org/data/gom-water-quality-wide-2025.csv",
      "schema:encodingFormat": [
        "text/csv"
      ],
      "cdi:characterSet": "UTF-8",
      "cdif:fileSize": 312,
      "cdif:fileSizeUofM": "KB",
      "spdx:checksum": {
        "@type": [
          "spdx:Checksum"
        ],
        "spdx:algorithm": "SHA256",
        "spdx:checksumValue": "2c8e4f1a6d7b9c0e3f5a1b2c4d6e7f8a9b0c1d2e3f4a5b6c7d8e9f0a1b2c3d4e"
      },
      "cdi:isDelimited": true,
      "csvw:delimiter": ",",
      "csvw:header": true,
      "csvw:headerRowCount": 1,
      "csvw:quoteChar": "\"",
      "csvw:skipBlankRows": true,
      "countRows": 144,
      "countColumns": 6,
      "cdif:hasPhysicalMapping": [
        {
          "cdif:index": 0,
          "cdif:format": "string",
          "cdif:physicalDataType": "string",
          "cdi:isRequired": true,
          "cdif:formats_InstanceVariable": {
            "@id": "ex:var-station"
          }
        },
        {
          "cdif:index": 1,
          "cdif:format": "YYYY-MM-DD",
          "cdif:physicalDataType": "date",
          "cdi:isRequired": true,
          "cdif:formats_InstanceVariable": {
            "@id": "ex:var-sample-date"
          }
        },
        {
          "cdif:index": 2,
          "cdif:format": "decimal",
          "cdif:physicalDataType": "float64",
          "cdi:decimalPositions": 2,
          "cdi:nullSequence": "NA",
          "cdif:formats_InstanceVariable": {
            "@id": "ex:var-ph"
          }
        },
        {
          "cdif:index": 3,
          "cdif:format": "decimal",
          "cdif:physicalDataType": "float64",
          "cdi:decimalPositions": 2,
          "cdi:nullSequence": "NA",
          "cdif:formats_InstanceVariable": {
            "@id": "ex:var-temperature"
          }
        },
        {
          "cdif:index": 4,
          "cdif:format": "decimal",
          "cdif:physicalDataType": "float64",
          "cdi:decimalPositions": 3,
          "cdi:nullSequence": "NA",
          "cdif:formats_InstanceVariable": {
            "@id": "ex:var-salinity"
          }
        },
        {
          "cdif:index": 5,
          "cdif:format": "decimal",
          "cdif:physicalDataType": "float64",
          "cdi:decimalPositions": 2,
          "cdi:nullSequence": "NA",
          "cdif:formats_InstanceVariable": {
            "@id": "ex:var-oxygen"
          }
        }
      ]
    }
  ],
  "schema:variableMeasured": [
    {
      "@id": "ex:var-station",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "station_id",
      "schema:description": "Monitoring station identifier; primary key component.",
      "cdif:physicalDataType": [
        "string"
      ],
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#string",
      "cdif:role": "UnitIdentifier",
      "cdif:displayLabel": [
        "Monitoring station"
      ]
    },
    {
      "@id": "ex:var-sample-date",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "sample_date",
      "schema:description": "Date the water sample was collected; primary key component.",
      "cdif:physicalDataType": [
        "date"
      ],
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#date",
      "cdif:role": "Dimension",
      "cdif:displayLabel": [
        "Sampling date"
      ]
    },
    {
      "@id": "ex:var-ph",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "ph",
      "schema:description": "pH of the water sample (unitless).",
      "schema:measurementTechnique": "Glass electrode, two-point calibration",
      "schema:propertyID": [
        "http://vocab.nerc.ac.uk/collection/P01/current/PHXXZZXX/"
      ],
      "cdif:physicalDataType": [
        "float64"
      ],
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
      "cdif:role": "Measure",
      "schema:minValue": 0.0,
      "schema:maxValue": 14.0,
      "cdif:displayLabel": [
        "pH"
      ],
      "cdif:simpleUnitOfMeasure": "1",
      "cdif:uses": [
        {
          "@id": "http://vocab.nerc.ac.uk/collection/P01/current/PHXXZZXX/"
        }
      ]
    },
    {
      "@id": "ex:var-temperature",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "temperature",
      "schema:description": "Sea-water temperature at sample depth.",
      "schema:measurementTechnique": "CTD profiler",
      "cdif:physicalDataType": [
        "float64"
      ],
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
      "cdif:role": "Measure",
      "schema:minValue": -2.0,
      "schema:maxValue": 30.0,
      "cdif:displayLabel": [
        "Sea-water temperature"
      ],
      "cdi:describedUnitOfMeasure": {
        "@type": [
          "schema:DefinedTerm"
        ],
        "schema:name": "degree Celsius",
        "schema:identifier": "http://qudt.org/vocab/unit/DEG_C"
      },
      "cdif:simpleUnitOfMeasure": "Cel"
    },
    {
      "@id": "ex:var-salinity",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "salinity",
      "schema:description": "Practical salinity (PSU).",
      "schema:measurementTechnique": "CTD profiler",
      "cdif:physicalDataType": [
        "float64"
      ],
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
      "cdif:role": "Measure",
      "schema:minValue": 0.0,
      "schema:maxValue": 42.0,
      "cdif:displayLabel": [
        "Practical salinity"
      ],
      "cdif:simpleUnitOfMeasure": "1",
      "cdif:uses": [
        {
          "@id": "http://vocab.nerc.ac.uk/collection/P01/current/PSALST01/"
        }
      ]
    },
    {
      "@id": "ex:var-oxygen",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "dissolved_oxygen",
      "schema:description": "Dissolved oxygen concentration in water.",
      "schema:measurementTechnique": "Optode sensor",
      "cdif:physicalDataType": [
        "float64"
      ],
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
      "cdif:role": "Measure",
      "schema:minValue": 0.0,
      "schema:maxValue": 15.0,
      "cdif:displayLabel": [
        "Dissolved oxygen"
      ],
      "cdi:describedUnitOfMeasure": {
        "@type": [
          "schema:DefinedTerm"
        ],
        "schema:name": "milligram per litre",
        "schema:identifier": "http://qudt.org/vocab/unit/MilliGM-PER-L"
      },
      "cdif:simpleUnitOfMeasure": "mg/L"
    }
  ],
  "cdif:hasPrimaryKey": {
    "@type": [
      "cdif:Key"
    ],
    "@id": "ex:gom-water-quality-wide-2025/pk",
    "cdif:isComposedOf": [
      {
        "@id": "ex:var-station"
      },
      {
        "@id": "ex:var-sample-date"
      }
    ]
  },
  "schema:measurementTechnique": [
    "CTD profiler",
    "Glass electrode pH meter",
    "Optode dissolved-oxygen sensor"
  ],
  "schema:spatialCoverage": [
    {
      "@type": [
        "schema:Place"
      ],
      "schema:name": "Gulf of Maine",
      "schema:geo": {
        "@type": [
          "schema:GeoShape"
        ],
        "schema:box": "41.0 -71.0 45.0 -65.0"
      }
    }
  ],
  "schema:temporalCoverage": [
    "2025-01-01/2025-12-31"
  ],
  "schema:subjectOf": {
    "@id": "ex:gom-water-quality-wide-2025/catalog-record",
    "@type": [
      "schema:Dataset"
    ],
    "schema:additionalType": [
      "dcat:CatalogRecord"
    ],
    "schema:about": {
      "@id": "ex:gom-water-quality-wide-2025"
    },
    "schema:sdDatePublished": "2025-10-20",
    "dcterms:conformsTo": [
      {
        "@id": "https://w3id.org/cdif/core/1.0"
      },
      {
        "@id": "https://w3id.org/cdif/discovery/1.0"
      },
      {
        "@id": "https://w3id.org/cdif/data_description/1.0"
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
      "dcterms": "http://purl.org/dc/terms/",
      "spdx": "http://spdx.org/rdf/terms#",
      "csvw": "http://www.w3.org/ns/csvw#"
    },
    "https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/profiles/cdifCompositeProfile/BasicDataDescription/context.jsonld",
    {
      "schema": "http://schema.org/",
      "dcterms": "http://purl.org/dc/terms/",
      "dcat": "http://www.w3.org/ns/dcat#",
      "prov": "http://www.w3.org/ns/prov#",
      "spdx": "http://spdx.org/rdf/terms#",
      "csvw": "http://www.w3.org/ns/csvw#",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "ex": "https://example.org/",
      "cdif": "https://cdif.org/0.1/"
    }
  ],
  "@id": "ex:gom-water-quality-wide-2025",
  "@type": [
    "schema:Dataset"
  ],
  "schema:name": "Gulf of Maine water-quality monitoring stations, 2025 (wide form)",
  "schema:description": "Monthly water-quality observations from 12 monitoring buoys. One row per station-visit; one column per measured parameter (pH, temperature, salinity, dissolved oxygen). Primary key is the (station, sample_date) pair.",
  "schema:identifier": {
    "@type": [
      "schema:PropertyValue"
    ],
    "schema:propertyID": "https://doi.org",
    "schema:value": "10.5281/zenodo.5151515",
    "schema:url": "https://doi.org/10.5281/zenodo.5151515"
  },
  "schema:version": "2025.10",
  "schema:dateModified": "2025-10-20",
  "schema:datePublished": "2025-10-20",
  "schema:license": [
    "https://creativecommons.org/licenses/by/4.0/"
  ],
  "schema:keywords": [
    "water quality",
    "Gulf of Maine",
    "monitoring",
    "wide format"
  ],
  "schema:creator": {
    "@list": [
      {
        "@id": "https://ror.org/03m2x1q45",
        "@type": [
          "schema:Organization"
        ],
        "schema:name": "University of Arizona"
      }
    ]
  },
  "schema:publisher": {
    "@id": "https://ror.org/03m2x1q45",
    "@type": [
      "schema:Organization"
    ],
    "schema:name": "University of Arizona"
  },
  "schema:distribution": [
    {
      "@type": [
        "schema:DataDownload",
        "cdi:TabularTextDataSet",
        "cdi:PhysicalDataSet"
      ],
      "schema:name": "Wide-form water-quality observations (CSV)",
      "schema:contentUrl": "https://example.org/data/gom-water-quality-wide-2025.csv",
      "schema:encodingFormat": [
        "text/csv"
      ],
      "cdi:characterSet": "UTF-8",
      "cdif:fileSize": 312,
      "cdif:fileSizeUofM": "KB",
      "spdx:checksum": {
        "@type": [
          "spdx:Checksum"
        ],
        "spdx:algorithm": "SHA256",
        "spdx:checksumValue": "2c8e4f1a6d7b9c0e3f5a1b2c4d6e7f8a9b0c1d2e3f4a5b6c7d8e9f0a1b2c3d4e"
      },
      "cdi:isDelimited": true,
      "csvw:delimiter": ",",
      "csvw:header": true,
      "csvw:headerRowCount": 1,
      "csvw:quoteChar": "\"",
      "csvw:skipBlankRows": true,
      "countRows": 144,
      "countColumns": 6,
      "cdif:hasPhysicalMapping": [
        {
          "cdif:index": 0,
          "cdif:format": "string",
          "cdif:physicalDataType": "string",
          "cdi:isRequired": true,
          "cdif:formats_InstanceVariable": {
            "@id": "ex:var-station"
          }
        },
        {
          "cdif:index": 1,
          "cdif:format": "YYYY-MM-DD",
          "cdif:physicalDataType": "date",
          "cdi:isRequired": true,
          "cdif:formats_InstanceVariable": {
            "@id": "ex:var-sample-date"
          }
        },
        {
          "cdif:index": 2,
          "cdif:format": "decimal",
          "cdif:physicalDataType": "float64",
          "cdi:decimalPositions": 2,
          "cdi:nullSequence": "NA",
          "cdif:formats_InstanceVariable": {
            "@id": "ex:var-ph"
          }
        },
        {
          "cdif:index": 3,
          "cdif:format": "decimal",
          "cdif:physicalDataType": "float64",
          "cdi:decimalPositions": 2,
          "cdi:nullSequence": "NA",
          "cdif:formats_InstanceVariable": {
            "@id": "ex:var-temperature"
          }
        },
        {
          "cdif:index": 4,
          "cdif:format": "decimal",
          "cdif:physicalDataType": "float64",
          "cdi:decimalPositions": 3,
          "cdi:nullSequence": "NA",
          "cdif:formats_InstanceVariable": {
            "@id": "ex:var-salinity"
          }
        },
        {
          "cdif:index": 5,
          "cdif:format": "decimal",
          "cdif:physicalDataType": "float64",
          "cdi:decimalPositions": 2,
          "cdi:nullSequence": "NA",
          "cdif:formats_InstanceVariable": {
            "@id": "ex:var-oxygen"
          }
        }
      ]
    }
  ],
  "schema:variableMeasured": [
    {
      "@id": "ex:var-station",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "station_id",
      "schema:description": "Monitoring station identifier; primary key component.",
      "cdif:physicalDataType": [
        "string"
      ],
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#string",
      "cdif:role": "UnitIdentifier",
      "cdif:displayLabel": [
        "Monitoring station"
      ]
    },
    {
      "@id": "ex:var-sample-date",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "sample_date",
      "schema:description": "Date the water sample was collected; primary key component.",
      "cdif:physicalDataType": [
        "date"
      ],
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#date",
      "cdif:role": "Dimension",
      "cdif:displayLabel": [
        "Sampling date"
      ]
    },
    {
      "@id": "ex:var-ph",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "ph",
      "schema:description": "pH of the water sample (unitless).",
      "schema:measurementTechnique": "Glass electrode, two-point calibration",
      "schema:propertyID": [
        "http://vocab.nerc.ac.uk/collection/P01/current/PHXXZZXX/"
      ],
      "cdif:physicalDataType": [
        "float64"
      ],
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
      "cdif:role": "Measure",
      "schema:minValue": 0.0,
      "schema:maxValue": 14.0,
      "cdif:displayLabel": [
        "pH"
      ],
      "cdif:simpleUnitOfMeasure": "1",
      "cdif:uses": [
        {
          "@id": "http://vocab.nerc.ac.uk/collection/P01/current/PHXXZZXX/"
        }
      ]
    },
    {
      "@id": "ex:var-temperature",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "temperature",
      "schema:description": "Sea-water temperature at sample depth.",
      "schema:measurementTechnique": "CTD profiler",
      "cdif:physicalDataType": [
        "float64"
      ],
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
      "cdif:role": "Measure",
      "schema:minValue": -2.0,
      "schema:maxValue": 30.0,
      "cdif:displayLabel": [
        "Sea-water temperature"
      ],
      "cdi:describedUnitOfMeasure": {
        "@type": [
          "schema:DefinedTerm"
        ],
        "schema:name": "degree Celsius",
        "schema:identifier": "http://qudt.org/vocab/unit/DEG_C"
      },
      "cdif:simpleUnitOfMeasure": "Cel"
    },
    {
      "@id": "ex:var-salinity",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "salinity",
      "schema:description": "Practical salinity (PSU).",
      "schema:measurementTechnique": "CTD profiler",
      "cdif:physicalDataType": [
        "float64"
      ],
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
      "cdif:role": "Measure",
      "schema:minValue": 0.0,
      "schema:maxValue": 42.0,
      "cdif:displayLabel": [
        "Practical salinity"
      ],
      "cdif:simpleUnitOfMeasure": "1",
      "cdif:uses": [
        {
          "@id": "http://vocab.nerc.ac.uk/collection/P01/current/PSALST01/"
        }
      ]
    },
    {
      "@id": "ex:var-oxygen",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "dissolved_oxygen",
      "schema:description": "Dissolved oxygen concentration in water.",
      "schema:measurementTechnique": "Optode sensor",
      "cdif:physicalDataType": [
        "float64"
      ],
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
      "cdif:role": "Measure",
      "schema:minValue": 0.0,
      "schema:maxValue": 15.0,
      "cdif:displayLabel": [
        "Dissolved oxygen"
      ],
      "cdi:describedUnitOfMeasure": {
        "@type": [
          "schema:DefinedTerm"
        ],
        "schema:name": "milligram per litre",
        "schema:identifier": "http://qudt.org/vocab/unit/MilliGM-PER-L"
      },
      "cdif:simpleUnitOfMeasure": "mg/L"
    }
  ],
  "cdif:hasPrimaryKey": {
    "@type": [
      "cdif:Key"
    ],
    "@id": "ex:gom-water-quality-wide-2025/pk",
    "cdif:isComposedOf": [
      {
        "@id": "ex:var-station"
      },
      {
        "@id": "ex:var-sample-date"
      }
    ]
  },
  "schema:measurementTechnique": [
    "CTD profiler",
    "Glass electrode pH meter",
    "Optode dissolved-oxygen sensor"
  ],
  "schema:spatialCoverage": [
    {
      "@type": [
        "schema:Place"
      ],
      "schema:name": "Gulf of Maine",
      "schema:geo": {
        "@type": [
          "schema:GeoShape"
        ],
        "schema:box": "41.0 -71.0 45.0 -65.0"
      }
    }
  ],
  "schema:temporalCoverage": [
    "2025-01-01/2025-12-31"
  ],
  "schema:subjectOf": {
    "@id": "ex:gom-water-quality-wide-2025/catalog-record",
    "@type": [
      "schema:Dataset"
    ],
    "schema:additionalType": [
      "dcat:CatalogRecord"
    ],
    "schema:about": {
      "@id": "ex:gom-water-quality-wide-2025"
    },
    "schema:sdDatePublished": "2025-10-20",
    "dcterms:conformsTo": [
      {
        "@id": "https://w3id.org/cdif/core/1.0"
      },
      {
        "@id": "https://w3id.org/cdif/discovery/1.0"
      },
      {
        "@id": "https://w3id.org/cdif/data_description/1.0"
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
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix ex: <https://example.org/> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix schema1: <http://schema.org/> .
@prefix spdx: <http://spdx.org/rdf/terms#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ex:gom-water-quality-wide-2025 a schema1:Dataset ;
    schema1:creator ( <https://ror.org/03m2x1q45> ) ;
    schema1:dateModified "2025-10-20" ;
    schema1:datePublished "2025-10-20" ;
    schema1:description "Monthly water-quality observations from 12 monitoring buoys. One row per station-visit; one column per measured parameter (pH, temperature, salinity, dissolved oxygen). Primary key is the (station, sample_date) pair." ;
    schema1:distribution [ a cdi:PhysicalDataSet,
                cdi:TabularTextDataSet,
                schema1:DataDownload ;
            cdi:characterSet "UTF-8" ;
            cdi:isDelimited true ;
            schema1:contentUrl "https://example.org/data/gom-water-quality-wide-2025.csv" ;
            schema1:encodingFormat "text/csv" ;
            schema1:name "Wide-form water-quality observations (CSV)" ;
            spdx:checksum [ a spdx:Checksum ;
                    spdx:algorithm "SHA256" ;
                    spdx:checksumValue "2c8e4f1a6d7b9c0e3f5a1b2c4d6e7f8a9b0c1d2e3f4a5b6c7d8e9f0a1b2c3d4e" ] ;
            csvw:delimiter "," ;
            csvw:header true ;
            csvw:headerRowCount 1 ;
            csvw:quoteChar "\"" ;
            csvw:skipBlankRows true ;
            cdif:fileSize 312 ;
            cdif:fileSizeUofM "KB" ;
            cdif:hasPhysicalMapping [ cdi:decimalPositions 2 ;
                    cdi:nullSequence "NA" ;
                    cdif:format "decimal" ;
                    cdif:formats_InstanceVariable ex:var-temperature ;
                    cdif:index 3 ;
                    cdif:physicalDataType "float64" ],
                [ cdi:decimalPositions 3 ;
                    cdi:nullSequence "NA" ;
                    cdif:format "decimal" ;
                    cdif:formats_InstanceVariable ex:var-salinity ;
                    cdif:index 4 ;
                    cdif:physicalDataType "float64" ],
                [ cdi:isRequired true ;
                    cdif:format "string" ;
                    cdif:formats_InstanceVariable ex:var-station ;
                    cdif:index 0 ;
                    cdif:physicalDataType "string" ],
                [ cdi:isRequired true ;
                    cdif:format "YYYY-MM-DD" ;
                    cdif:formats_InstanceVariable ex:var-sample-date ;
                    cdif:index 1 ;
                    cdif:physicalDataType "date" ],
                [ cdi:decimalPositions 2 ;
                    cdi:nullSequence "NA" ;
                    cdif:format "decimal" ;
                    cdif:formats_InstanceVariable ex:var-oxygen ;
                    cdif:index 5 ;
                    cdif:physicalDataType "float64" ],
                [ cdi:decimalPositions 2 ;
                    cdi:nullSequence "NA" ;
                    cdif:format "decimal" ;
                    cdif:formats_InstanceVariable ex:var-ph ;
                    cdif:index 2 ;
                    cdif:physicalDataType "float64" ] ] ;
    schema1:identifier [ a schema1:PropertyValue ;
            schema1:propertyID "https://doi.org" ;
            schema1:url "https://doi.org/10.5281/zenodo.5151515" ;
            schema1:value "10.5281/zenodo.5151515" ] ;
    schema1:keywords "Gulf of Maine",
        "monitoring",
        "water quality",
        "wide format" ;
    schema1:license "https://creativecommons.org/licenses/by/4.0/" ;
    schema1:measurementTechnique "CTD profiler",
        "Glass electrode pH meter",
        "Optode dissolved-oxygen sensor" ;
    schema1:name "Gulf of Maine water-quality monitoring stations, 2025 (wide form)" ;
    schema1:publisher <https://ror.org/03m2x1q45> ;
    schema1:spatialCoverage [ a schema1:Place ;
            schema1:geo [ a schema1:GeoShape ;
                    schema1:box "41.0 -71.0 45.0 -65.0" ] ;
            schema1:name "Gulf of Maine" ] ;
    schema1:subjectOf <https://example.org/gom-water-quality-wide-2025/catalog-record> ;
    schema1:temporalCoverage "2025-01-01/2025-12-31" ;
    schema1:variableMeasured ex:var-oxygen,
        ex:var-ph,
        ex:var-salinity,
        ex:var-sample-date,
        ex:var-station,
        ex:var-temperature ;
    schema1:version "2025.10" ;
    cdif:hasPrimaryKey <https://example.org/gom-water-quality-wide-2025/pk> .

<https://example.org/gom-water-quality-wide-2025/catalog-record> a schema1:Dataset ;
    dcterms:conformsTo <https://w3id.org/cdif/core/1.0>,
        <https://w3id.org/cdif/data_description/1.0>,
        <https://w3id.org/cdif/discovery/1.0> ;
    schema1:about ex:gom-water-quality-wide-2025 ;
    schema1:additionalType "dcat:CatalogRecord" ;
    schema1:sdDatePublished "2025-10-20" .

<https://example.org/gom-water-quality-wide-2025/pk> a cdif:Key ;
    cdif:isComposedOf ex:var-sample-date,
        ex:var-station .

ex:var-oxygen a cdi:InstanceVariable,
        schema1:PropertyValue ;
    cdi:describedUnitOfMeasure [ a schema1:DefinedTerm ;
            schema1:identifier "http://qudt.org/vocab/unit/MilliGM-PER-L" ;
            schema1:name "milligram per litre" ] ;
    cdi:intendedDataType "https://www.w3.org/TR/xmlschema-2/#decimal" ;
    schema1:description "Dissolved oxygen concentration in water." ;
    schema1:maxValue 1.5e+01 ;
    schema1:measurementTechnique "Optode sensor" ;
    schema1:minValue 0e+00 ;
    schema1:name "dissolved_oxygen" ;
    cdif:displayLabel "Dissolved oxygen" ;
    cdif:physicalDataType "float64" ;
    cdif:role "Measure" ;
    cdif:simpleUnitOfMeasure "mg/L" .

ex:var-ph a cdi:InstanceVariable,
        schema1:PropertyValue ;
    cdi:intendedDataType "https://www.w3.org/TR/xmlschema-2/#decimal" ;
    schema1:description "pH of the water sample (unitless)." ;
    schema1:maxValue 1.4e+01 ;
    schema1:measurementTechnique "Glass electrode, two-point calibration" ;
    schema1:minValue 0e+00 ;
    schema1:name "ph" ;
    schema1:propertyID "http://vocab.nerc.ac.uk/collection/P01/current/PHXXZZXX/" ;
    cdif:displayLabel "pH" ;
    cdif:physicalDataType "float64" ;
    cdif:role "Measure" ;
    cdif:simpleUnitOfMeasure "1" ;
    cdif:uses <http://vocab.nerc.ac.uk/collection/P01/current/PHXXZZXX/> .

ex:var-salinity a cdi:InstanceVariable,
        schema1:PropertyValue ;
    cdi:intendedDataType "https://www.w3.org/TR/xmlschema-2/#decimal" ;
    schema1:description "Practical salinity (PSU)." ;
    schema1:maxValue 4.2e+01 ;
    schema1:measurementTechnique "CTD profiler" ;
    schema1:minValue 0e+00 ;
    schema1:name "salinity" ;
    cdif:displayLabel "Practical salinity" ;
    cdif:physicalDataType "float64" ;
    cdif:role "Measure" ;
    cdif:simpleUnitOfMeasure "1" ;
    cdif:uses <http://vocab.nerc.ac.uk/collection/P01/current/PSALST01/> .

ex:var-temperature a cdi:InstanceVariable,
        schema1:PropertyValue ;
    cdi:describedUnitOfMeasure [ a schema1:DefinedTerm ;
            schema1:identifier "http://qudt.org/vocab/unit/DEG_C" ;
            schema1:name "degree Celsius" ] ;
    cdi:intendedDataType "https://www.w3.org/TR/xmlschema-2/#decimal" ;
    schema1:description "Sea-water temperature at sample depth." ;
    schema1:maxValue 3e+01 ;
    schema1:measurementTechnique "CTD profiler" ;
    schema1:minValue -2e+00 ;
    schema1:name "temperature" ;
    cdif:displayLabel "Sea-water temperature" ;
    cdif:physicalDataType "float64" ;
    cdif:role "Measure" ;
    cdif:simpleUnitOfMeasure "Cel" .

<https://ror.org/03m2x1q45> a schema1:Organization ;
    schema1:name "University of Arizona" .

ex:var-sample-date a cdi:InstanceVariable,
        schema1:PropertyValue ;
    cdi:intendedDataType "https://www.w3.org/TR/xmlschema-2/#date" ;
    schema1:description "Date the water sample was collected; primary key component." ;
    schema1:name "sample_date" ;
    cdif:displayLabel "Sampling date" ;
    cdif:physicalDataType "date" ;
    cdif:role "Dimension" .

ex:var-station a cdi:InstanceVariable,
        schema1:PropertyValue ;
    cdi:intendedDataType "https://www.w3.org/TR/xmlschema-2/#string" ;
    schema1:description "Monitoring station identifier; primary key component." ;
    schema1:name "station_id" ;
    cdif:displayLabel "Monitoring station" ;
    cdif:physicalDataType "string" ;
    cdif:role "UnitIdentifier" .


```


### Long (descriptor/value) example.
The same water-quality observations cast in long form: each row is one
observation with a parameter-name column (cdif:role Descriptor) and a value
column (cdif:role ReferenceVariable). The four named parameters remain in
schema:variableMeasured as Measure InstanceVariables; wiring descriptor codes
to them is a Data Structure profile concern, not a data description one.
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "dcterms": "http://purl.org/dc/terms/",
    "dcat": "http://www.w3.org/ns/dcat#",
    "prov": "http://www.w3.org/ns/prov#",
    "spdx": "http://spdx.org/rdf/terms#",
    "csvw": "http://www.w3.org/ns/csvw#",
    "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
    "ex": "https://example.org/",
    "cdif": "https://cdif.org/0.1/"
  },
  "@id": "ex:gom-water-quality-long-2025",
  "@type": [
    "schema:Dataset"
  ],
  "schema:name": "Gulf of Maine water-quality monitoring stations, 2025 (long form)",
  "schema:description": "Same monthly water-quality observations from 12 buoys as the wide-form release, recast in long (narrow) form. Each row is one observation: station, date, parameter name (descriptor), value, and reporting unit.",
  "schema:identifier": {
    "@type": [
      "schema:PropertyValue"
    ],
    "schema:propertyID": "https://doi.org",
    "schema:value": "10.5281/zenodo.5151516",
    "schema:url": "https://doi.org/10.5281/zenodo.5151516"
  },
  "schema:version": "2025.10",
  "schema:dateModified": "2025-10-20",
  "schema:datePublished": "2025-10-20",
  "schema:license": [
    "https://creativecommons.org/licenses/by/4.0/"
  ],
  "schema:keywords": [
    "water quality",
    "Gulf of Maine",
    "long format",
    "tidy data"
  ],
  "schema:creator": {
    "@list": [
      {
        "@id": "https://ror.org/03m2x1q45",
        "@type": [
          "schema:Organization"
        ],
        "schema:name": "University of Arizona"
      }
    ]
  },
  "schema:publisher": {
    "@id": "https://ror.org/03m2x1q45",
    "@type": [
      "schema:Organization"
    ],
    "schema:name": "University of Arizona"
  },
  "prov:wasDerivedFrom": [
    {
      "@id": "ex:gom-water-quality-wide-2025",
      "schema:name": "Wide-form release of the same observations"
    }
  ],
  "schema:distribution": [
    {
      "@type": [
        "schema:DataDownload",
        "cdi:LongStructureDataSet",
        "cdi:PhysicalDataSet"
      ],
      "schema:name": "Long-form water-quality observations (CSV)",
      "schema:contentUrl": "https://example.org/data/gom-water-quality-long-2025.csv",
      "schema:encodingFormat": [
        "text/csv"
      ],
      "cdi:characterSet": "UTF-8",
      "cdif:fileSize": 712,
      "cdif:fileSizeUofM": "KB",
      "spdx:checksum": {
        "@type": [
          "spdx:Checksum"
        ],
        "spdx:algorithm": "SHA256",
        "spdx:checksumValue": "8b1a7c3e5d9f0a2b4c6d8e0f1a3b5c7d9e1f2a4b6c8d0e2f4a6b8c0d2e4f6a8b"
      },
      "cdi:isDelimited": true,
      "csvw:delimiter": ",",
      "csvw:header": true,
      "csvw:headerRowCount": 1,
      "csvw:quoteChar": "\"",
      "csvw:skipBlankRows": true,
      "countRows": 576,
      "countColumns": 5,
      "cdif:hasPhysicalMapping": [
        {
          "cdif:index": 0,
          "cdif:format": "string",
          "cdif:physicalDataType": "string",
          "cdi:isRequired": true,
          "cdif:formats_InstanceVariable": {
            "@id": "ex:var-station"
          }
        },
        {
          "cdif:index": 1,
          "cdif:format": "YYYY-MM-DD",
          "cdif:physicalDataType": "date",
          "cdi:isRequired": true,
          "cdif:formats_InstanceVariable": {
            "@id": "ex:var-sample-date"
          }
        },
        {
          "cdif:index": 2,
          "cdif:format": "string",
          "cdif:physicalDataType": "string",
          "cdi:isRequired": true,
          "cdif:formats_InstanceVariable": {
            "@id": "ex:var-parameter"
          }
        },
        {
          "cdif:index": 3,
          "cdif:format": "decimal",
          "cdif:physicalDataType": "float64",
          "cdi:nullSequence": "NA",
          "cdi:isRequired": true,
          "cdif:formats_InstanceVariable": {
            "@id": "ex:var-value"
          }
        },
        {
          "cdif:index": 4,
          "cdif:format": "string",
          "cdif:physicalDataType": "string",
          "cdif:formats_InstanceVariable": {
            "@id": "ex:var-unit"
          }
        }
      ]
    }
  ],
  "schema:variableMeasured": [
    {
      "@id": "ex:var-station",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "station_id",
      "schema:description": "Monitoring station identifier; unit of observation.",
      "cdif:physicalDataType": [
        "string"
      ],
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#string",
      "cdif:role": "UnitIdentifier",
      "cdif:displayLabel": [
        "Monitoring station"
      ]
    },
    {
      "@id": "ex:var-sample-date",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "sample_date",
      "schema:description": "Date the water sample was collected.",
      "cdif:physicalDataType": [
        "date"
      ],
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#date",
      "cdif:role": "Dimension",
      "cdif:displayLabel": [
        "Sampling date"
      ]
    },
    {
      "@id": "ex:var-parameter",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "parameter",
      "schema:description": "Descriptor column. Each value names the measured property whose numeric reading is recorded in the value column. Permitted codes are ph, temperature, salinity, dissolved_oxygen.",
      "cdif:physicalDataType": [
        "string"
      ],
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#string",
      "cdif:role": "Descriptor",
      "cdif:displayLabel": [
        "Parameter"
      ]
    },
    {
      "@id": "ex:var-value",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "value",
      "schema:description": "Reference column. Holds the numeric value of whichever parameter is named in the descriptor column for that row.",
      "cdif:physicalDataType": [
        "float64"
      ],
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
      "cdif:role": "ReferenceVariable",
      "cdif:displayLabel": [
        "Measured value"
      ]
    },
    {
      "@id": "ex:var-unit",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "unit",
      "schema:description": "Reporting unit symbol for the row's value (e.g., Cel, 1, mg/L).",
      "cdif:physicalDataType": [
        "string"
      ],
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#string",
      "cdif:role": "Attribute",
      "cdif:displayLabel": [
        "Unit of measure"
      ],
      "cdi:qualifies": {
        "@id": "ex:var-value"
      }
    },
    {
      "@id": "ex:var-ph",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "ph",
      "schema:description": "pH parameter. Rows whose descriptor column equals 'ph' record values for this variable.",
      "schema:measurementTechnique": "Glass electrode, two-point calibration",
      "cdif:physicalDataType": [
        "float64"
      ],
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
      "cdif:role": "Measure",
      "schema:minValue": 0.0,
      "schema:maxValue": 14.0,
      "cdif:displayLabel": [
        "pH"
      ],
      "cdif:simpleUnitOfMeasure": "1",
      "cdif:uses": [
        {
          "@id": "http://vocab.nerc.ac.uk/collection/P01/current/PHXXZZXX/"
        }
      ]
    },
    {
      "@id": "ex:var-temperature",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "temperature",
      "schema:description": "Temperature parameter. Rows whose descriptor column equals 'temperature' record values for this variable.",
      "schema:measurementTechnique": "CTD profiler",
      "cdif:physicalDataType": [
        "float64"
      ],
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
      "cdif:role": "Measure",
      "schema:minValue": -2.0,
      "schema:maxValue": 30.0,
      "cdif:displayLabel": [
        "Sea-water temperature"
      ],
      "cdi:describedUnitOfMeasure": {
        "@type": [
          "schema:DefinedTerm"
        ],
        "schema:name": "degree Celsius",
        "schema:identifier": "http://qudt.org/vocab/unit/DEG_C"
      },
      "cdif:simpleUnitOfMeasure": "Cel"
    },
    {
      "@id": "ex:var-salinity",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "salinity",
      "schema:description": "Practical salinity parameter. Rows whose descriptor column equals 'salinity' record values for this variable.",
      "schema:measurementTechnique": "CTD profiler",
      "cdif:physicalDataType": [
        "float64"
      ],
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
      "cdif:role": "Measure",
      "schema:minValue": 0.0,
      "schema:maxValue": 42.0,
      "cdif:displayLabel": [
        "Practical salinity"
      ],
      "cdif:simpleUnitOfMeasure": "1",
      "cdif:uses": [
        {
          "@id": "http://vocab.nerc.ac.uk/collection/P01/current/PSALST01/"
        }
      ]
    },
    {
      "@id": "ex:var-dissolved-oxygen",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "dissolved_oxygen",
      "schema:description": "Dissolved oxygen parameter. Rows whose descriptor column equals 'dissolved_oxygen' record values for this variable.",
      "schema:measurementTechnique": "Optode sensor",
      "cdif:physicalDataType": [
        "float64"
      ],
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
      "cdif:role": "Measure",
      "schema:minValue": 0.0,
      "schema:maxValue": 15.0,
      "cdif:displayLabel": [
        "Dissolved oxygen"
      ],
      "cdi:describedUnitOfMeasure": {
        "@type": [
          "schema:DefinedTerm"
        ],
        "schema:name": "milligram per litre",
        "schema:identifier": "http://qudt.org/vocab/unit/MilliGM-PER-L"
      },
      "cdif:simpleUnitOfMeasure": "mg/L"
    }
  ],
  "schema:measurementTechnique": [
    "CTD profiler",
    "Glass electrode pH meter",
    "Optode dissolved-oxygen sensor"
  ],
  "schema:spatialCoverage": [
    {
      "@type": [
        "schema:Place"
      ],
      "schema:name": "Gulf of Maine",
      "schema:geo": {
        "@type": [
          "schema:GeoShape"
        ],
        "schema:box": "41.0 -71.0 45.0 -65.0"
      }
    }
  ],
  "schema:temporalCoverage": [
    "2025-01-01/2025-12-31"
  ],
  "schema:subjectOf": {
    "@id": "ex:gom-water-quality-long-2025/catalog-record",
    "@type": [
      "schema:Dataset"
    ],
    "schema:additionalType": [
      "dcat:CatalogRecord"
    ],
    "schema:about": {
      "@id": "ex:gom-water-quality-long-2025"
    },
    "schema:sdDatePublished": "2025-10-20",
    "dcterms:conformsTo": [
      {
        "@id": "https://w3id.org/cdif/core/1.0"
      },
      {
        "@id": "https://w3id.org/cdif/discovery/1.0"
      },
      {
        "@id": "https://w3id.org/cdif/data_description/1.0"
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
      "dcterms": "http://purl.org/dc/terms/",
      "spdx": "http://spdx.org/rdf/terms#",
      "csvw": "http://www.w3.org/ns/csvw#"
    },
    "https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/profiles/cdifCompositeProfile/BasicDataDescription/context.jsonld",
    {
      "schema": "http://schema.org/",
      "dcterms": "http://purl.org/dc/terms/",
      "dcat": "http://www.w3.org/ns/dcat#",
      "prov": "http://www.w3.org/ns/prov#",
      "spdx": "http://spdx.org/rdf/terms#",
      "csvw": "http://www.w3.org/ns/csvw#",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "ex": "https://example.org/",
      "cdif": "https://cdif.org/0.1/"
    }
  ],
  "@id": "ex:gom-water-quality-long-2025",
  "@type": [
    "schema:Dataset"
  ],
  "schema:name": "Gulf of Maine water-quality monitoring stations, 2025 (long form)",
  "schema:description": "Same monthly water-quality observations from 12 buoys as the wide-form release, recast in long (narrow) form. Each row is one observation: station, date, parameter name (descriptor), value, and reporting unit.",
  "schema:identifier": {
    "@type": [
      "schema:PropertyValue"
    ],
    "schema:propertyID": "https://doi.org",
    "schema:value": "10.5281/zenodo.5151516",
    "schema:url": "https://doi.org/10.5281/zenodo.5151516"
  },
  "schema:version": "2025.10",
  "schema:dateModified": "2025-10-20",
  "schema:datePublished": "2025-10-20",
  "schema:license": [
    "https://creativecommons.org/licenses/by/4.0/"
  ],
  "schema:keywords": [
    "water quality",
    "Gulf of Maine",
    "long format",
    "tidy data"
  ],
  "schema:creator": {
    "@list": [
      {
        "@id": "https://ror.org/03m2x1q45",
        "@type": [
          "schema:Organization"
        ],
        "schema:name": "University of Arizona"
      }
    ]
  },
  "schema:publisher": {
    "@id": "https://ror.org/03m2x1q45",
    "@type": [
      "schema:Organization"
    ],
    "schema:name": "University of Arizona"
  },
  "prov:wasDerivedFrom": [
    {
      "@id": "ex:gom-water-quality-wide-2025",
      "schema:name": "Wide-form release of the same observations"
    }
  ],
  "schema:distribution": [
    {
      "@type": [
        "schema:DataDownload",
        "cdi:LongStructureDataSet",
        "cdi:PhysicalDataSet"
      ],
      "schema:name": "Long-form water-quality observations (CSV)",
      "schema:contentUrl": "https://example.org/data/gom-water-quality-long-2025.csv",
      "schema:encodingFormat": [
        "text/csv"
      ],
      "cdi:characterSet": "UTF-8",
      "cdif:fileSize": 712,
      "cdif:fileSizeUofM": "KB",
      "spdx:checksum": {
        "@type": [
          "spdx:Checksum"
        ],
        "spdx:algorithm": "SHA256",
        "spdx:checksumValue": "8b1a7c3e5d9f0a2b4c6d8e0f1a3b5c7d9e1f2a4b6c8d0e2f4a6b8c0d2e4f6a8b"
      },
      "cdi:isDelimited": true,
      "csvw:delimiter": ",",
      "csvw:header": true,
      "csvw:headerRowCount": 1,
      "csvw:quoteChar": "\"",
      "csvw:skipBlankRows": true,
      "countRows": 576,
      "countColumns": 5,
      "cdif:hasPhysicalMapping": [
        {
          "cdif:index": 0,
          "cdif:format": "string",
          "cdif:physicalDataType": "string",
          "cdi:isRequired": true,
          "cdif:formats_InstanceVariable": {
            "@id": "ex:var-station"
          }
        },
        {
          "cdif:index": 1,
          "cdif:format": "YYYY-MM-DD",
          "cdif:physicalDataType": "date",
          "cdi:isRequired": true,
          "cdif:formats_InstanceVariable": {
            "@id": "ex:var-sample-date"
          }
        },
        {
          "cdif:index": 2,
          "cdif:format": "string",
          "cdif:physicalDataType": "string",
          "cdi:isRequired": true,
          "cdif:formats_InstanceVariable": {
            "@id": "ex:var-parameter"
          }
        },
        {
          "cdif:index": 3,
          "cdif:format": "decimal",
          "cdif:physicalDataType": "float64",
          "cdi:nullSequence": "NA",
          "cdi:isRequired": true,
          "cdif:formats_InstanceVariable": {
            "@id": "ex:var-value"
          }
        },
        {
          "cdif:index": 4,
          "cdif:format": "string",
          "cdif:physicalDataType": "string",
          "cdif:formats_InstanceVariable": {
            "@id": "ex:var-unit"
          }
        }
      ]
    }
  ],
  "schema:variableMeasured": [
    {
      "@id": "ex:var-station",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "station_id",
      "schema:description": "Monitoring station identifier; unit of observation.",
      "cdif:physicalDataType": [
        "string"
      ],
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#string",
      "cdif:role": "UnitIdentifier",
      "cdif:displayLabel": [
        "Monitoring station"
      ]
    },
    {
      "@id": "ex:var-sample-date",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "sample_date",
      "schema:description": "Date the water sample was collected.",
      "cdif:physicalDataType": [
        "date"
      ],
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#date",
      "cdif:role": "Dimension",
      "cdif:displayLabel": [
        "Sampling date"
      ]
    },
    {
      "@id": "ex:var-parameter",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "parameter",
      "schema:description": "Descriptor column. Each value names the measured property whose numeric reading is recorded in the value column. Permitted codes are ph, temperature, salinity, dissolved_oxygen.",
      "cdif:physicalDataType": [
        "string"
      ],
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#string",
      "cdif:role": "Descriptor",
      "cdif:displayLabel": [
        "Parameter"
      ]
    },
    {
      "@id": "ex:var-value",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "value",
      "schema:description": "Reference column. Holds the numeric value of whichever parameter is named in the descriptor column for that row.",
      "cdif:physicalDataType": [
        "float64"
      ],
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
      "cdif:role": "ReferenceVariable",
      "cdif:displayLabel": [
        "Measured value"
      ]
    },
    {
      "@id": "ex:var-unit",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "unit",
      "schema:description": "Reporting unit symbol for the row's value (e.g., Cel, 1, mg/L).",
      "cdif:physicalDataType": [
        "string"
      ],
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#string",
      "cdif:role": "Attribute",
      "cdif:displayLabel": [
        "Unit of measure"
      ],
      "cdi:qualifies": {
        "@id": "ex:var-value"
      }
    },
    {
      "@id": "ex:var-ph",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "ph",
      "schema:description": "pH parameter. Rows whose descriptor column equals 'ph' record values for this variable.",
      "schema:measurementTechnique": "Glass electrode, two-point calibration",
      "cdif:physicalDataType": [
        "float64"
      ],
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
      "cdif:role": "Measure",
      "schema:minValue": 0.0,
      "schema:maxValue": 14.0,
      "cdif:displayLabel": [
        "pH"
      ],
      "cdif:simpleUnitOfMeasure": "1",
      "cdif:uses": [
        {
          "@id": "http://vocab.nerc.ac.uk/collection/P01/current/PHXXZZXX/"
        }
      ]
    },
    {
      "@id": "ex:var-temperature",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "temperature",
      "schema:description": "Temperature parameter. Rows whose descriptor column equals 'temperature' record values for this variable.",
      "schema:measurementTechnique": "CTD profiler",
      "cdif:physicalDataType": [
        "float64"
      ],
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
      "cdif:role": "Measure",
      "schema:minValue": -2.0,
      "schema:maxValue": 30.0,
      "cdif:displayLabel": [
        "Sea-water temperature"
      ],
      "cdi:describedUnitOfMeasure": {
        "@type": [
          "schema:DefinedTerm"
        ],
        "schema:name": "degree Celsius",
        "schema:identifier": "http://qudt.org/vocab/unit/DEG_C"
      },
      "cdif:simpleUnitOfMeasure": "Cel"
    },
    {
      "@id": "ex:var-salinity",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "salinity",
      "schema:description": "Practical salinity parameter. Rows whose descriptor column equals 'salinity' record values for this variable.",
      "schema:measurementTechnique": "CTD profiler",
      "cdif:physicalDataType": [
        "float64"
      ],
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
      "cdif:role": "Measure",
      "schema:minValue": 0.0,
      "schema:maxValue": 42.0,
      "cdif:displayLabel": [
        "Practical salinity"
      ],
      "cdif:simpleUnitOfMeasure": "1",
      "cdif:uses": [
        {
          "@id": "http://vocab.nerc.ac.uk/collection/P01/current/PSALST01/"
        }
      ]
    },
    {
      "@id": "ex:var-dissolved-oxygen",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "dissolved_oxygen",
      "schema:description": "Dissolved oxygen parameter. Rows whose descriptor column equals 'dissolved_oxygen' record values for this variable.",
      "schema:measurementTechnique": "Optode sensor",
      "cdif:physicalDataType": [
        "float64"
      ],
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
      "cdif:role": "Measure",
      "schema:minValue": 0.0,
      "schema:maxValue": 15.0,
      "cdif:displayLabel": [
        "Dissolved oxygen"
      ],
      "cdi:describedUnitOfMeasure": {
        "@type": [
          "schema:DefinedTerm"
        ],
        "schema:name": "milligram per litre",
        "schema:identifier": "http://qudt.org/vocab/unit/MilliGM-PER-L"
      },
      "cdif:simpleUnitOfMeasure": "mg/L"
    }
  ],
  "schema:measurementTechnique": [
    "CTD profiler",
    "Glass electrode pH meter",
    "Optode dissolved-oxygen sensor"
  ],
  "schema:spatialCoverage": [
    {
      "@type": [
        "schema:Place"
      ],
      "schema:name": "Gulf of Maine",
      "schema:geo": {
        "@type": [
          "schema:GeoShape"
        ],
        "schema:box": "41.0 -71.0 45.0 -65.0"
      }
    }
  ],
  "schema:temporalCoverage": [
    "2025-01-01/2025-12-31"
  ],
  "schema:subjectOf": {
    "@id": "ex:gom-water-quality-long-2025/catalog-record",
    "@type": [
      "schema:Dataset"
    ],
    "schema:additionalType": [
      "dcat:CatalogRecord"
    ],
    "schema:about": {
      "@id": "ex:gom-water-quality-long-2025"
    },
    "schema:sdDatePublished": "2025-10-20",
    "dcterms:conformsTo": [
      {
        "@id": "https://w3id.org/cdif/core/1.0"
      },
      {
        "@id": "https://w3id.org/cdif/discovery/1.0"
      },
      {
        "@id": "https://w3id.org/cdif/data_description/1.0"
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
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix ex: <https://example.org/> .
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix schema1: <http://schema.org/> .
@prefix spdx: <http://spdx.org/rdf/terms#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ex:gom-water-quality-long-2025 a schema1:Dataset ;
    schema1:creator ( <https://ror.org/03m2x1q45> ) ;
    schema1:dateModified "2025-10-20" ;
    schema1:datePublished "2025-10-20" ;
    schema1:description "Same monthly water-quality observations from 12 buoys as the wide-form release, recast in long (narrow) form. Each row is one observation: station, date, parameter name (descriptor), value, and reporting unit." ;
    schema1:distribution [ a cdi:LongStructureDataSet,
                cdi:PhysicalDataSet,
                schema1:DataDownload ;
            cdi:characterSet "UTF-8" ;
            cdi:isDelimited true ;
            schema1:contentUrl "https://example.org/data/gom-water-quality-long-2025.csv" ;
            schema1:encodingFormat "text/csv" ;
            schema1:name "Long-form water-quality observations (CSV)" ;
            spdx:checksum [ a spdx:Checksum ;
                    spdx:algorithm "SHA256" ;
                    spdx:checksumValue "8b1a7c3e5d9f0a2b4c6d8e0f1a3b5c7d9e1f2a4b6c8d0e2f4a6b8c0d2e4f6a8b" ] ;
            csvw:delimiter "," ;
            csvw:header true ;
            csvw:headerRowCount 1 ;
            csvw:quoteChar "\"" ;
            csvw:skipBlankRows true ;
            cdif:fileSize 712 ;
            cdif:fileSizeUofM "KB" ;
            cdif:hasPhysicalMapping [ cdi:isRequired true ;
                    cdi:nullSequence "NA" ;
                    cdif:format "decimal" ;
                    cdif:formats_InstanceVariable ex:var-value ;
                    cdif:index 3 ;
                    cdif:physicalDataType "float64" ],
                [ cdi:isRequired true ;
                    cdif:format "string" ;
                    cdif:formats_InstanceVariable ex:var-parameter ;
                    cdif:index 2 ;
                    cdif:physicalDataType "string" ],
                [ cdi:isRequired true ;
                    cdif:format "YYYY-MM-DD" ;
                    cdif:formats_InstanceVariable ex:var-sample-date ;
                    cdif:index 1 ;
                    cdif:physicalDataType "date" ],
                [ cdif:format "string" ;
                    cdif:formats_InstanceVariable ex:var-unit ;
                    cdif:index 4 ;
                    cdif:physicalDataType "string" ],
                [ cdi:isRequired true ;
                    cdif:format "string" ;
                    cdif:formats_InstanceVariable ex:var-station ;
                    cdif:index 0 ;
                    cdif:physicalDataType "string" ] ] ;
    schema1:identifier [ a schema1:PropertyValue ;
            schema1:propertyID "https://doi.org" ;
            schema1:url "https://doi.org/10.5281/zenodo.5151516" ;
            schema1:value "10.5281/zenodo.5151516" ] ;
    schema1:keywords "Gulf of Maine",
        "long format",
        "tidy data",
        "water quality" ;
    schema1:license "https://creativecommons.org/licenses/by/4.0/" ;
    schema1:measurementTechnique "CTD profiler",
        "Glass electrode pH meter",
        "Optode dissolved-oxygen sensor" ;
    schema1:name "Gulf of Maine water-quality monitoring stations, 2025 (long form)" ;
    schema1:publisher <https://ror.org/03m2x1q45> ;
    schema1:spatialCoverage [ a schema1:Place ;
            schema1:geo [ a schema1:GeoShape ;
                    schema1:box "41.0 -71.0 45.0 -65.0" ] ;
            schema1:name "Gulf of Maine" ] ;
    schema1:subjectOf <https://example.org/gom-water-quality-long-2025/catalog-record> ;
    schema1:temporalCoverage "2025-01-01/2025-12-31" ;
    schema1:variableMeasured ex:var-dissolved-oxygen,
        ex:var-parameter,
        ex:var-ph,
        ex:var-salinity,
        ex:var-sample-date,
        ex:var-station,
        ex:var-temperature,
        ex:var-unit,
        ex:var-value ;
    schema1:version "2025.10" ;
    prov:wasDerivedFrom ex:gom-water-quality-wide-2025 .

<https://example.org/gom-water-quality-long-2025/catalog-record> a schema1:Dataset ;
    dcterms:conformsTo <https://w3id.org/cdif/core/1.0>,
        <https://w3id.org/cdif/data_description/1.0>,
        <https://w3id.org/cdif/discovery/1.0> ;
    schema1:about ex:gom-water-quality-long-2025 ;
    schema1:additionalType "dcat:CatalogRecord" ;
    schema1:sdDatePublished "2025-10-20" .

ex:gom-water-quality-wide-2025 schema1:name "Wide-form release of the same observations" .

ex:var-dissolved-oxygen a cdi:InstanceVariable,
        schema1:PropertyValue ;
    cdi:describedUnitOfMeasure [ a schema1:DefinedTerm ;
            schema1:identifier "http://qudt.org/vocab/unit/MilliGM-PER-L" ;
            schema1:name "milligram per litre" ] ;
    cdi:intendedDataType "https://www.w3.org/TR/xmlschema-2/#decimal" ;
    schema1:description "Dissolved oxygen parameter. Rows whose descriptor column equals 'dissolved_oxygen' record values for this variable." ;
    schema1:maxValue 1.5e+01 ;
    schema1:measurementTechnique "Optode sensor" ;
    schema1:minValue 0e+00 ;
    schema1:name "dissolved_oxygen" ;
    cdif:displayLabel "Dissolved oxygen" ;
    cdif:physicalDataType "float64" ;
    cdif:role "Measure" ;
    cdif:simpleUnitOfMeasure "mg/L" .

ex:var-ph a cdi:InstanceVariable,
        schema1:PropertyValue ;
    cdi:intendedDataType "https://www.w3.org/TR/xmlschema-2/#decimal" ;
    schema1:description "pH parameter. Rows whose descriptor column equals 'ph' record values for this variable." ;
    schema1:maxValue 1.4e+01 ;
    schema1:measurementTechnique "Glass electrode, two-point calibration" ;
    schema1:minValue 0e+00 ;
    schema1:name "ph" ;
    cdif:displayLabel "pH" ;
    cdif:physicalDataType "float64" ;
    cdif:role "Measure" ;
    cdif:simpleUnitOfMeasure "1" ;
    cdif:uses <http://vocab.nerc.ac.uk/collection/P01/current/PHXXZZXX/> .

ex:var-salinity a cdi:InstanceVariable,
        schema1:PropertyValue ;
    cdi:intendedDataType "https://www.w3.org/TR/xmlschema-2/#decimal" ;
    schema1:description "Practical salinity parameter. Rows whose descriptor column equals 'salinity' record values for this variable." ;
    schema1:maxValue 4.2e+01 ;
    schema1:measurementTechnique "CTD profiler" ;
    schema1:minValue 0e+00 ;
    schema1:name "salinity" ;
    cdif:displayLabel "Practical salinity" ;
    cdif:physicalDataType "float64" ;
    cdif:role "Measure" ;
    cdif:simpleUnitOfMeasure "1" ;
    cdif:uses <http://vocab.nerc.ac.uk/collection/P01/current/PSALST01/> .

ex:var-temperature a cdi:InstanceVariable,
        schema1:PropertyValue ;
    cdi:describedUnitOfMeasure [ a schema1:DefinedTerm ;
            schema1:identifier "http://qudt.org/vocab/unit/DEG_C" ;
            schema1:name "degree Celsius" ] ;
    cdi:intendedDataType "https://www.w3.org/TR/xmlschema-2/#decimal" ;
    schema1:description "Temperature parameter. Rows whose descriptor column equals 'temperature' record values for this variable." ;
    schema1:maxValue 3e+01 ;
    schema1:measurementTechnique "CTD profiler" ;
    schema1:minValue -2e+00 ;
    schema1:name "temperature" ;
    cdif:displayLabel "Sea-water temperature" ;
    cdif:physicalDataType "float64" ;
    cdif:role "Measure" ;
    cdif:simpleUnitOfMeasure "Cel" .

ex:var-parameter a cdi:InstanceVariable,
        schema1:PropertyValue ;
    cdi:intendedDataType "https://www.w3.org/TR/xmlschema-2/#string" ;
    schema1:description "Descriptor column. Each value names the measured property whose numeric reading is recorded in the value column. Permitted codes are ph, temperature, salinity, dissolved_oxygen." ;
    schema1:name "parameter" ;
    cdif:displayLabel "Parameter" ;
    cdif:physicalDataType "string" ;
    cdif:role "Descriptor" .

ex:var-sample-date a cdi:InstanceVariable,
        schema1:PropertyValue ;
    cdi:intendedDataType "https://www.w3.org/TR/xmlschema-2/#date" ;
    schema1:description "Date the water sample was collected." ;
    schema1:name "sample_date" ;
    cdif:displayLabel "Sampling date" ;
    cdif:physicalDataType "date" ;
    cdif:role "Dimension" .

ex:var-station a cdi:InstanceVariable,
        schema1:PropertyValue ;
    cdi:intendedDataType "https://www.w3.org/TR/xmlschema-2/#string" ;
    schema1:description "Monitoring station identifier; unit of observation." ;
    schema1:name "station_id" ;
    cdif:displayLabel "Monitoring station" ;
    cdif:physicalDataType "string" ;
    cdif:role "UnitIdentifier" .

ex:var-unit a cdi:InstanceVariable,
        schema1:PropertyValue ;
    cdi:intendedDataType "https://www.w3.org/TR/xmlschema-2/#string" ;
    cdi:qualifies ex:var-value ;
    schema1:description "Reporting unit symbol for the row's value (e.g., Cel, 1, mg/L)." ;
    schema1:name "unit" ;
    cdif:displayLabel "Unit of measure" ;
    cdif:physicalDataType "string" ;
    cdif:role "Attribute" .

<https://ror.org/03m2x1q45> a schema1:Organization ;
    schema1:name "University of Arizona" .

ex:var-value a cdi:InstanceVariable,
        schema1:PropertyValue ;
    cdi:intendedDataType "https://www.w3.org/TR/xmlschema-2/#decimal" ;
    schema1:description "Reference column. Holds the numeric value of whichever parameter is named in the descriptor column for that row." ;
    schema1:name "value" ;
    cdif:displayLabel "Measured value" ;
    cdif:physicalDataType "float64" ;
    cdif:role "ReferenceVariable" .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
type: object
title: CDIF Data Description metadata profile
description: CDIF Data Description profile. Composes cdifCore with discovery properties
  and data description extensions for detailed variable and structure documentation.
allOf:
- $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/profiles/cdifProfile/cdifCore/schema.yaml
- $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/profiles/cdifProfile/cdifDiscovery/schema.yaml
- $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/profiles/cdifProfile/cdifDataDescription/schema.yaml
x-jsonld-prefixes:
  cdif: https://cdif.org/0.1/
  schema: http://schema.org/
  cdi: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/
  dcterms: http://purl.org/dc/terms/
  geosparql: http://www.opengis.net/ont/geosparql#
  spdx: http://spdx.org/rdf/terms#
  time: http://www.w3.org/2006/time#
  skos: http://www.w3.org/2004/02/skos/core#
  prov: http://www.w3.org/ns/prov#

```

Links to the schema:

* YAML version: [schema.yaml](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/profiles/cdifCompositeProfile/BasicDataDescription/schema.json)
* JSON version: [schema.json](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/profiles/cdifCompositeProfile/BasicDataDescription/schema.yaml)


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
    "geosparql": "http://www.opengis.net/ont/geosparql#",
    "spdx": "http://spdx.org/rdf/terms#",
    "time": "http://www.w3.org/2006/time#",
    "xas": "https://xas.org/dictionary/",
    "nxs": "http://purl.org/nexusformat/definitions/",
    "ada": "https://ada.astromat.org/metadata/",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/profiles/cdifCompositeProfile/BasicDataDescription/context.jsonld)

## Sources

* [CDIF book](https://cross-domain-interoperability-framework.github.io/cdifbook/metadata/schemaorgimplementation.html#schema-org-implementation-of-cdif-metadata)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/Cross-Domain-Interoperability-Framework/metadataBuildingBlocks](https://github.com/Cross-Domain-Interoperability-Framework/metadataBuildingBlocks)
* Path: `_sources/profiles/cdifCompositeProfile/BasicDataDescription`

