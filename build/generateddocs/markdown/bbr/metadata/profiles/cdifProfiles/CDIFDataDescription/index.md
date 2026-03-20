
# CDIF discovery and data description metadata (Schema)

`cdif.bbr.metadata.profiles.cdifProfiles.CDIFDataDescription` *v0.1*

Schema extends data discovery with properties to desribe data structures for tabular and structured (grid, datacube, hierarchialc) datasets

[*Status*](http://www.opengis.net/def/status): Under development

## Description

## CDIF metadata  properties

Profile assembling building blocks for the schema.org implementation of the [Cross Domain Interoperability Framework](https://cross-domain-interoperability-framework.github.io/cdifbook/metadata/schemaorgimplementation.html#implementation-of-metadata-content-items) (CDIF) discovery with data description profile.
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
    "spdx": "http://spdx.org/rdf/terms#",
    "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
    "csvw": "http://www.w3.org/ns/csvw#",
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
        "schema:DataDownload"
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
        "schema:DataDownload"
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
          "@id": "kNKPZsCSWMc",
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
        "cdi:TabularTextDataSet"
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
      "cdi:hasPhysicalMapping": [
        {
          "cdi:index": 0,
          "cdi:format": "decimal",
          "cdi:physicalDataType": "float64",
          "cdi:nullSequence": "NA",
          "cdi:isRequired": true,
          "cdi:formats_InstanceVariable": {
            "@id": "ex:KJTFKurNFu"
          }
        },
        {
          "cdi:index": 1,
          "cdi:format": "decimal",
          "cdi:physicalDataType": "float64",
          "cdi:nullSequence": "-9999",
          "cdi:defaultValue": "0.0",
          "cdi:decimalPositions": 4,
          "cdi:isRequired": false,
          "cdi:formats_InstanceVariable": {
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
        "cdi:StructuredDataSet"
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
      "cdi:hasPhysicalMapping": [
        {
          "cdi:index": 0,
          "cdi:format": "decimal",
          "cdi:physicalDataType": "float32",
          "cdi:locator": "/measurements/wavelength",
          "cdi:nullSequence": "NaN",
          "cdi:isRequired": true,
          "cdi:formats_InstanceVariable": {
            "@id": "ex:KJTFKurNFu"
          }
        },
        {
          "cdi:index": 1,
          "cdi:format": "decimal",
          "cdi:physicalDataType": "float32",
          "cdi:locator": "/measurements/intensity",
          "cdi:scale": 1000,
          "cdi:decimalPositions": 6,
          "cdi:isRequired": true,
          "cdi:formats_InstanceVariable": {
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
          "schema:CreativeWork"
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
              "schema:DataDownload"
            ],
            "schema:name": "Geochemistry query results",
            "schema:contentUrl": "http://example.com/api/v1/collections/geochem/items?f=csv",
            "schema:encodingFormat": [
              "text/csv"
            ],
            "cdi:isDelimited": true,
            "csvw:delimiter": ",",
            "csvw:header": true,
            "csvw:headerRowCount": 1,
            "cdi:hasPhysicalMapping": [
              {
                "cdi:index": 0,
                "cdi:format": "decimal",
                "cdi:physicalDataType": "float64",
                "cdi:isRequired": true,
                "cdi:formats_InstanceVariable": {
                  "@id": "ex:KJTFKurNFu"
                }
              },
              {
                "cdi:index": 1,
                "cdi:format": "decimal",
                "cdi:physicalDataType": "float64",
                "cdi:isRequired": false,
                "cdi:formats_InstanceVariable": {
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
      "cdi:physicalDataType": "float64"
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
      "cdi:physicalDataType": "float32"
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
        "@id": "https://w3id.org/cdif/bbr/metadata/profiles/cdifProfiles/CDIFDataDescription"
      },
      {
        "@id": "https://w3id.org/cdif/core/1.0/"
      },
      {
        "@id": "https://w3id.org/cdif/discovery/1.0/"
      },
      {
        "@id": "https://w3id.org/cdif/data_description/1.0/"
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
    "https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/profiles/cdifProfiles/CDIFDataDescription/context.jsonld",
    {
      "schema": "http://schema.org/",
      "dcterms": "http://purl.org/dc/terms/",
      "geosparql": "http://www.opengis.net/ont/geosparql#",
      "spdx": "http://spdx.org/rdf/terms#",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "csvw": "http://www.w3.org/ns/csvw#",
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
        "schema:DataDownload"
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
        "schema:DataDownload"
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
          "@id": "kNKPZsCSWMc",
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
        "cdi:TabularTextDataSet"
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
      "cdi:hasPhysicalMapping": [
        {
          "cdi:index": 0,
          "cdi:format": "decimal",
          "cdi:physicalDataType": "float64",
          "cdi:nullSequence": "NA",
          "cdi:isRequired": true,
          "cdi:formats_InstanceVariable": {
            "@id": "ex:KJTFKurNFu"
          }
        },
        {
          "cdi:index": 1,
          "cdi:format": "decimal",
          "cdi:physicalDataType": "float64",
          "cdi:nullSequence": "-9999",
          "cdi:defaultValue": "0.0",
          "cdi:decimalPositions": 4,
          "cdi:isRequired": false,
          "cdi:formats_InstanceVariable": {
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
        "cdi:StructuredDataSet"
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
      "cdi:hasPhysicalMapping": [
        {
          "cdi:index": 0,
          "cdi:format": "decimal",
          "cdi:physicalDataType": "float32",
          "cdi:locator": "/measurements/wavelength",
          "cdi:nullSequence": "NaN",
          "cdi:isRequired": true,
          "cdi:formats_InstanceVariable": {
            "@id": "ex:KJTFKurNFu"
          }
        },
        {
          "cdi:index": 1,
          "cdi:format": "decimal",
          "cdi:physicalDataType": "float32",
          "cdi:locator": "/measurements/intensity",
          "cdi:scale": 1000,
          "cdi:decimalPositions": 6,
          "cdi:isRequired": true,
          "cdi:formats_InstanceVariable": {
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
          "schema:CreativeWork"
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
              "schema:DataDownload"
            ],
            "schema:name": "Geochemistry query results",
            "schema:contentUrl": "http://example.com/api/v1/collections/geochem/items?f=csv",
            "schema:encodingFormat": [
              "text/csv"
            ],
            "cdi:isDelimited": true,
            "csvw:delimiter": ",",
            "csvw:header": true,
            "csvw:headerRowCount": 1,
            "cdi:hasPhysicalMapping": [
              {
                "cdi:index": 0,
                "cdi:format": "decimal",
                "cdi:physicalDataType": "float64",
                "cdi:isRequired": true,
                "cdi:formats_InstanceVariable": {
                  "@id": "ex:KJTFKurNFu"
                }
              },
              {
                "cdi:index": 1,
                "cdi:format": "decimal",
                "cdi:physicalDataType": "float64",
                "cdi:isRequired": false,
                "cdi:formats_InstanceVariable": {
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
      "cdi:physicalDataType": "float64"
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
      "cdi:physicalDataType": "float32"
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
        "@id": "https://w3id.org/cdif/bbr/metadata/profiles/cdifProfiles/CDIFDataDescription"
      },
      {
        "@id": "https://w3id.org/cdif/core/1.0/"
      },
      {
        "@id": "https://w3id.org/cdif/discovery/1.0/"
      },
      {
        "@id": "https://w3id.org/cdif/data_description/1.0/"
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
@prefix csvw: <http://www.w3.org/ns/csvw#> .
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix ex: <https://example.org/> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix schema1: <http://schema.org/> .
@prefix spdx: <http://spdx.org/rdf/terms#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<file:///github/workspace/kNKPZsCSWMc> a schema1:Organization ;
    schema1:alternateName "WFcslOjvGZY" ;
    schema1:description "ztcLdOAkQTKSPLZ" ;
    schema1:identifier [ a schema1:PropertyValue ;
            schema1:propertyID "ex:oFIYAymjuGCPjDnSgmB" ;
            schema1:url "http://example.com/resource/WPfhCJyxiDcwgdHMemJd" ] ;
    schema1:name "SdeMvoPFxEaJOvQy" .

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
    dcterms:conformsTo <https://w3id.org/cdif/bbr/metadata/profiles/cdifProfiles/CDIFDataDescription>,
        <https://w3id.org/cdif/core/1.0/>,
        <https://w3id.org/cdif/data_description/1.0/>,
        <https://w3id.org/cdif/discovery/1.0/> ;
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
    schema1:distribution [ a schema1:DataDownload ;
            dcterms:conformsTo <http://www.opengis.net/def/nil/OGC/0/missing> ;
            schema1:contentUrl "http://example.com/resource?foo=bar#fragment" ;
            schema1:encodingFormat "text/csv" ;
            schema1:name "VwuIdrCrJSsrGATePg" ;
            schema1:provider ex:ABYcNWHKYhTiLLNEzJx ;
            spdx:checksum [ a spdx:Checksum ;
                    spdx:algorithm "MD5" ;
                    spdx:checksumValue "MITGLcmBjeFYWmjP" ] ],
        [ a schema1:DataDownload ;
            dcterms:conformsTo <http://www.opengis.net/def/nil/OGC/0/missing> ;
            schema1:contentUrl "http://example.com/resource?foo=bar#fragment" ;
            schema1:encodingFormat "kpZDvhyVo",
                "sMUGwSqxWzJOYEb",
                "tNdpXaJgDeWbFkNM" ;
            schema1:name "MVMpmnCGAggEnsoEgJXH" ;
            schema1:provider <file:///github/workspace/kNKPZsCSWMc>,
                ex:sr68lgy ;
            spdx:checksum [ a spdx:Checksum ;
                    spdx:algorithm "j" ;
                    spdx:checksumValue "h" ] ],
        [ a schema1:WebAPI ;
            schema1:documentation [ a schema1:CreativeWork ;
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
                    schema1:result [ a schema1:DataDownload ;
                            cdi:hasPhysicalMapping [ cdi:format "decimal" ;
                                    cdi:formats_InstanceVariable ex:KJTFKurNFu ;
                                    cdi:index 0 ;
                                    cdi:isRequired true ;
                                    cdi:physicalDataType "float64" ],
                                [ cdi:format "decimal" ;
                                    cdi:formats_InstanceVariable ex:OjHgIDO ;
                                    cdi:index 1 ;
                                    cdi:isRequired false ;
                                    cdi:physicalDataType "float64" ] ;
                            cdi:isDelimited true ;
                            dcterms:conformsTo <http://www.opengis.net/def/nil/OGC/0/missing> ;
                            schema1:contentUrl "http://example.com/api/v1/collections/geochem/items?f=csv" ;
                            schema1:encodingFormat "text/csv" ;
                            schema1:name "Geochemistry query results" ;
                            csvw:delimiter "," ;
                            csvw:header true ;
                            csvw:headerRowCount 1 ] ;
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
        [ a cdi:TabularTextDataSet,
                schema1:DataDownload ;
            cdi:hasPhysicalMapping [ cdi:format "decimal" ;
                    cdi:formats_InstanceVariable ex:KJTFKurNFu ;
                    cdi:index 0 ;
                    cdi:isRequired true ;
                    cdi:nullSequence "NA" ;
                    cdi:physicalDataType "float64" ],
                [ cdi:decimalPositions 4 ;
                    cdi:defaultValue "0.0" ;
                    cdi:format "decimal" ;
                    cdi:formats_InstanceVariable ex:OjHgIDO ;
                    cdi:index 1 ;
                    cdi:isRequired false ;
                    cdi:nullSequence "-9999" ;
                    cdi:physicalDataType "float64" ] ;
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
            csvw:skipRows 0 ],
        [ a cdi:StructuredDataSet,
                schema1:DataDownload ;
            cdi:hasPhysicalMapping [ cdi:format "decimal" ;
                    cdi:formats_InstanceVariable ex:KJTFKurNFu ;
                    cdi:index 0 ;
                    cdi:isRequired true ;
                    cdi:locator "/measurements/wavelength" ;
                    cdi:nullSequence "NaN" ;
                    cdi:physicalDataType "float32" ],
                [ cdi:decimalPositions 6 ;
                    cdi:format "decimal" ;
                    cdi:formats_InstanceVariable ex:OjHgIDO ;
                    cdi:index 1 ;
                    cdi:isRequired true ;
                    cdi:locator "/measurements/intensity" ;
                    cdi:physicalDataType "float32" ;
                    cdi:scale 1000 ] ;
            dcterms:conformsTo <http://www.opengis.net/def/nil/OGC/0/missing> ;
            schema1:contentUrl "http://example.com/data/measurement-cube.nc" ;
            schema1:encodingFormat "application/x-netcdf" ;
            schema1:name "Gridded measurement data cube" ;
            spdx:checksum [ a spdx:Checksum ;
                    spdx:algorithm "SHA256" ;
                    spdx:checksumValue "f6e5d4c3b2a1f6e5d4c3b2a1f6e5d4c3b2a1f6e5d4c3b2a1f6e5d4c3b2a1f6e5" ] ] ;
    schema1:funding [ a schema1:MonetaryGrant ;
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
            schema1:name "MWoPQAqRYHobey" ],
        [ a schema1:MonetaryGrant ;
            schema1:funder <https://ror.org/sejer4w6u8> ;
            schema1:identifier [ a schema1:PropertyValue ;
                    schema1:propertyID "grant-id" ;
                    schema1:value "LZpo" ] ;
            schema1:name "ekckpBtI" ] ;
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
    schema1:name "Test dataset" ;
    schema1:provider <https://ada.org/person/5489>,
        ex:gDiAxjl,
        ex:ihjJtFPNEKnGSFBcgS ;
    schema1:publisher ex:exampleOrg_fW ;
    schema1:publishingPrinciples "rxZsrPAbJrIGGgDVJ" ;
    schema1:relatedLink [ a schema1:LinkRole ;
            schema1:linkRelationship "lfCzUaoftdtTPAhMnpC" ],
        [ a schema1:LinkRole ;
            schema1:linkRelationship "BOoRREnpDEUrdNaV" ] ;
    schema1:sameAs [ a schema1:PropertyValue ;
            schema1:propertyID "urn:idorg:test" ;
            schema1:value "urn:idorg:test:p45689" ] ;
    schema1:subjectOf ex:BAaR ;
    schema1:url "http://example.com/resource?foo=bar#fragment" ;
    schema1:variableMeasured ex:KJTFKurNFu,
        ex:OjHgIDO ;
    schema1:version "OVVAYgJhmFkXyVyedlVo" .

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

ex:KJTFKurNFu a cdi:InstanceVariable,
        schema1:PropertyValue ;
    cdi:physicalDataType "float64" ;
    schema1:description "EcbPmKQnMCgWozw" ;
    schema1:maxValue 9.8e+01 ;
    schema1:measurementTechnique "some measurement technique" ;
    schema1:minValue 6.7e+01 ;
    schema1:name "RbMivCtraTmzms" ;
    schema1:propertyID "https://ark.org/bXEOCTwvICRc",
        "urn:test:GigjbPysIJ" ;
    schema1:unitCode "F" ;
    schema1:unitText "furlongs" ;
    schema1:url "http://example.com/resource?foo=bar#furlong" .

ex:OjHgIDO a cdi:InstanceVariable,
        schema1:PropertyValue ;
    cdi:physicalDataType "float32" ;
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
    schema1:url "http://example.com/resource?foo=bar#stone" .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
type: object
title: CDIF Data Description metadata profile
description: CDIF Data Description profile. Composes cdifCore with discovery properties
  and data description extensions for detailed variable and structure documentation.
allOf:
- $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifProperties/cdifCore/schema.yaml
- type: object
  properties:
    '@context':
      type: object
      description: Additional JSON-LD namespace prefixes for discovery and data description.
      properties:
        geosparql:
          const: http://www.opengis.net/ont/geosparql#
        dqv:
          const: http://www.w3.org/ns/dqv#
        cdi:
          const: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/
        csvw:
          const: http://www.w3.org/ns/csvw#
    schema:measurementTechnique:
      description: The technique, technology, or methodology used for measurement
        or determination of the dataset values.
      anyOf:
      - type: string
      - $ref: '#/$defs/DefinedTerm'
      - type: array
        items:
          anyOf:
          - type: string
          - $ref: '#/$defs/DefinedTerm'
    schema:variableMeasured:
      description: Variables in the dataset. At data description level, PropertyValue
        variables must include cdi:InstanceVariable typing and cdi:physicalDataType.
      type: array
      items:
        anyOf:
        - type: object
          properties:
            '@type':
              type: array
              items:
                type: string
              contains:
                const: cdi:InstanceVariable
              minItems: 2
          required:
          - cdi:physicalDataType
        - $ref: '#/$defs/StatisticalVariable'
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
    schema:distribution:
      type: array
      items:
        type: object
        properties:
          cdi:characterSet:
            type: string
            description: The character set used in the distribution (e.g., UTF-8,
              ASCII).
          cdi:fileSize:
            type: number
            description: The size of the distribution file.
          cdi:fileSizeUofM:
            type: string
            description: Unit of measure for the file size (e.g., bytes, KB, MB, GB).
    schema:subjectOf:
      properties:
        dcterms:conformsTo:
          contains:
            type: object
            properties:
              '@id':
                const: https://w3id.org/cdif/discovery/1.0/
  allOf:
  - properties:
      schema:subjectOf:
        properties:
          dcterms:conformsTo:
            contains:
              type: object
              properties:
                '@id':
                  const: https://w3id.org/cdif/data_description/1.0/
$defs:
  DefinedTerm:
    $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/definedTerm/schema.yaml
  StatisticalVariable:
    $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/statisticalVariable/schema.yaml
  SpatialExtent:
    $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/spatialExtent/schema.yaml
  TemporalExtent:
    $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/temporalExtent/schema.yaml
  QualityMeasure:
    $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/qualityProperties/qualityMeasure/schema.yaml
x-jsonld-extra-terms:
  csvw: {}
x-jsonld-prefixes:
  schema: http://schema.org/
  cdi: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/
  dcterms: http://purl.org/dc/terms/
  geosparql: http://www.opengis.net/ont/geosparql#
  spdx: http://spdx.org/rdf/terms#
  time: http://www.w3.org/2006/time#
  skos: http://www.w3.org/2004/02/skos/core#
  xas: https://xas.org/dictionary/
  nxs: http://purl.org/nexusformat/definitions/
  prov: http://www.w3.org/ns/prov#

```

Links to the schema:

* YAML version: [schema.yaml](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/profiles/cdifProfiles/CDIFDataDescription/schema.json)
* JSON version: [schema.json](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/profiles/cdifProfiles/CDIFDataDescription/schema.yaml)


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
    "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
    "geosparql": "http://www.opengis.net/ont/geosparql#",
    "spdx": "http://spdx.org/rdf/terms#",
    "time": "http://www.w3.org/2006/time#",
    "skos": "http://www.w3.org/2004/02/skos/core#",
    "xas": "https://xas.org/dictionary/",
    "nxs": "http://purl.org/nexusformat/definitions/",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/profiles/cdifProfiles/CDIFDataDescription/context.jsonld)

## Sources

* [CDIF book](https://cross-domain-interoperability-framework.github.io/cdifbook/metadata/schemaorgimplementation.html#schema-org-implementation-of-cdif-metadata)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/Cross-Domain-Interoperability-Framework/metadataBuildingBlocks](https://github.com/Cross-Domain-Interoperability-Framework/metadataBuildingBlocks)
* Path: `_sources/profiles/cdifProfiles/CDIFDataDescription`

