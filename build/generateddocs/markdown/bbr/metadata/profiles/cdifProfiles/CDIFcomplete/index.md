
# CDIF complete metadata (Schema)

`cdif.bbr.metadata.profiles.cdifProfiles.CDIFcomplete` *v0.1*

Profile combining CDIF discovery metadata with extended provenance (cdifProvActivity with instruments, agents, temporal bounds, methodology) and data description extensions for distributions (single-file, archive with hasPart, and WebAPI) and optional tabular/dataCube physical mappings. Defines properties: prov:wasGeneratedBy (cdifProvActivity), schema:distribution. Uses building blocks: cdifProvActivity (cdifProperties), dataDownload (schemaorgProperties), cdifDataCube (cdifProperties), cdifTabularData (cdifProperties), cdifArchiveDistribution (cdifProperties), webAPI (schemaorgProperties).

[*Status*](http://www.opengis.net/def/status): Under development

## Description

## CDIF complete metadata properties

Profile assembling building blocks for the schema.org implementation of the [Cross Domain Interoperability Framework](https://cross-domain-interoperability-framework.github.io/cdifbook/metadata/schemaorgimplementation.html#implementation-of-metadata-content-items) (CDIF) complete profile. Extends the CDIFDiscovery profile with extended provenance and data description/archive distribution extensions.

### Composition

- **CDIFDiscovery** --mandatory and optional discovery metadata (cdifMandatory + cdifOptional), including variableMeasured descriptions
- **Extended provenance** (`cdifProvActivity`) --upgrades `prov:wasGeneratedBy` from simple string/@id references (cdifOptional level) to full provenance activities with instruments, agents, temporal bounds, methodology, action chaining, and domain-specific extension properties
- **Data description extensions** --distribution items may include CDIF data description properties:
  - `cdifTabularData` --for delimited or fixed-width tabular text files (CSV, TSV), with CSVW properties and physical column mappings
  - `cdifDataCube` --for multi-dimensional structured datasets (NetCDF, HDF5), with locator-based physical mappings
- **Archive distribution** (`cdifArchiveDistribution`) --for archive files (ZIP, tar.gz) containing multiple component files described via `schema:hasPart`, each typed as `schema:MediaObject` with optional data description extensions
- **WebAPI distribution** --for API-based data access with `schema:potentialAction` describing query endpoints and result data descriptions

### Distribution types

Each `schema:distribution` item must match one of:

1. **Single-file DataDownload** --a directly accessible file with optional tabular/dataCube data description
2. **Archive DataDownload** --an archive file with `schema:hasPart` listing component files
3. **WebAPI** --an API endpoint with `schema:potentialAction` describing available queries and their result format

## Examples

### CDIF complete profile example record.
Comprehensive CDIF metadata example demonstrating the complete profile with
discovery metadata, single-file and archive distributions with component files,
WebAPI access, tabular and data cube physical mappings, provenance, and
quality measurements.
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
    "prov": "http://www.w3.org/ns/prov#",
    "time": "http://www.w3.org/2006/time#",
    "dqv": "http://www.w3.org/ns/dqv#",
    "sf": "http://www.opengis.net/ont/sf#",
    "ex": "https://example.org/",
    "xsd": "http://www.w3.org/2001/XMLSchema#",
    "dcat": "http://www.w3.org/ns/dcat#"
  },
  "@id": "ex:complete-dataset-001",
  "@type": [
    "schema:Dataset"
  ],
  "schema:name": "Multi-technique geochemistry dataset with archive and API access",
  "schema:description": "Comprehensive geochemistry dataset demonstrating the CDIF complete profile with single-file downloads, archive distribution with component files, and WebAPI access. Includes tabular CSV results, NetCDF data cubes, and an OGC API Features endpoint.",
  "schema:additionalType": [
    "geochemistry analysis"
  ],
  "schema:identifier": {
    "@type": "schema:PropertyValue",
    "schema:propertyID": "https://registry.identifiers.org/registry/doi",
    "schema:value": "10.5880/example.complete.001",
    "schema:url": "https://doi.org/10.5880/example.complete.001"
  },
  "schema:sameAs": [
    {
      "@type": "schema:PropertyValue",
      "schema:value": "urn:example:geochem:complete-001"
    }
  ],
  "schema:version": "1.0",
  "schema:url": "https://example.org/datasets/complete-001",
  "schema:inLanguage": "en",
  "schema:dateModified": "2026-02-15",
  "schema:datePublished": "2026-02-01",
  "schema:license": [
    "https://creativecommons.org/licenses/by/4.0/"
  ],
  "schema:conditionsOfAccess": [
    "Open access; citation required"
  ],
  "schema:keywords": [
    {
      "@type": "schema:DefinedTerm",
      "schema:name": "geochemistry",
      "schema:identifier": {
        "@type": "schema:PropertyValue",
        "schema:propertyID": "https://vocabularyserver.com/keyword",
        "schema:value": "geochem-001",
        "schema:url": "https://vocabularyserver.com/keyword/geochem-001"
      },
      "schema:inDefinedTermSet": "https://vocabularyserver.com/keyword",
      "schema:termCode": "GEOCHEM"
    },
    {
      "@type": "schema:DefinedTerm",
      "schema:name": "spectral analysis",
      "schema:identifier": {
        "@type": "schema:PropertyValue",
        "schema:propertyID": "https://vocabularyserver.com/keyword",
        "schema:value": "spectral-001",
        "schema:url": "https://vocabularyserver.com/keyword/spectral-001"
      },
      "schema:inDefinedTermSet": "https://vocabularyserver.com/keyword",
      "schema:termCode": "SPECTRAL"
    }
  ],
  "schema:creator": {
    "@list": [
      {
        "@id": "https://orcid.org/0000-0001-2345-6789",
        "@type": "schema:Person",
        "schema:name": "Smith, Jane",
        "schema:alternateName": "J. Smith",
        "schema:description": "Geochemistry researcher specializing in trace element analysis and environmental mineralogy",
        "schema:affiliation": {
          "@id": "https://ror.org/03m2x1q45",
          "@type": "schema:Organization",
          "schema:name": "University of Arizona"
        },
        "schema:contactPoint": {
          "@type": "schema:ContactPoint",
          "schema:email": "jsmith@arizona.edu"
        },
        "schema:identifier": {
          "@type": "schema:PropertyValue",
          "schema:propertyID": "https://orcid.org",
          "schema:value": "0000-0001-2345-6789",
          "schema:url": "https://orcid.org/0000-0001-2345-6789"
        }
      }
    ]
  },
  "schema:publisher": {
    "@id": "ex:ieda-publisher",
    "@type": "schema:Organization",
    "schema:name": "IEDA-",
    "schema:alternateName": "Interdisciplinary Earth Data Alliance",
    "schema:description": "An NSF-supported data facility for geochemistry and related disciplines",
    "schema:identifier": {
      "@type": "schema:PropertyValue",
      "schema:propertyID": "https://registry.identifiers.org/registry/ror",
      "schema:value": "02fjgr047",
      "schema:url": "https://ror.org/02fjgr047"
    }
  },
  "schema:funding": [
    {
      "@type": "schema:MonetaryGrant",
      "schema:identifier": {
        "@type": "schema:PropertyValue",
        "schema:propertyID": "NSF award number",
        "schema:value": "EAR-2026932",
        "schema:url": "https://www.nsf.gov/awardsearch/showAward?AWD_ID=2026932"
      },
      "schema:name": "Geochemistry Data Infrastructure",
      "schema:funder": {
        "@id": "https://ror.org/021nxhr62"
      }
    }
  ],
  "schema:provider": [
    {
      "@id": "https://ror.org/02fjgr047",
      "@type": "schema:Organization",
      "schema:name": "IEDA-",
      "schema:url": "https://www.earthchem.org/"
    }
  ],
  "schema:contributor": [
    {
      "@type": "schema:Role",
      "schema:roleName": {
        "@type": "schema:DefinedTerm",
        "schema:name": "Data Manager",
        "schema:inDefinedTermSet": "https://credit.niso.org/",
        "schema:termCode": "data-curation"
      },
      "schema:contributor": {
        "@id": "https://orcid.org/0000-0003-5555-7777",
        "@type": "schema:Person",
        "schema:name": "Lee, Robert",
        "schema:contactPoint": {
          "@type": "schema:ContactPoint",
          "schema:email": "rlee@example.org"
        }
      }
    },
    {
      "@id": "https://ror.org/03m2x1q45",
      "@type": "schema:Organization",
      "schema:name": "University of Arizona"
    }
  ],
  "schema:measurementTechnique": {
    "@type": "schema:DefinedTerm",
    "schema:name": "Inductively Coupled Plasma Mass Spectrometry",
    "schema:identifier": {
      "@type": "schema:PropertyValue",
      "schema:propertyID": "https://vocab.nerc.ac.uk/collection/L05/current/",
      "schema:value": "LAB21",
      "schema:url": "https://vocab.nerc.ac.uk/collection/L05/current/LAB21/"
    },
    "schema:inDefinedTermSet": "https://vocab.nerc.ac.uk/collection/L05/current/",
    "schema:termCode": "ICP-MS"
  },
  "schema:spatialCoverage": [
    {
      "@type": "schema:Place",
      "schema:name": [
        "Great Basin",
        {
          "@type": "schema:DefinedTerm",
          "schema:name": "Great Basin physiographic province",
          "schema:identifier": {
            "@type": "schema:PropertyValue",
            "schema:propertyID": "https://www.geonames.org/",
            "schema:value": "5509151",
            "schema:url": "https://www.geonames.org/5509151"
          },
          "schema:inDefinedTermSet": "https://www.geonames.org/",
          "schema:termCode": "5509151"
        }
      ],
      "schema:geo": {
        "@type": "schema:GeoShape",
        "schema:box": "36.0 -120.0 42.0 -114.0"
      },
      "geosparql:hasGeometry": {
        "@type": "sf:Polygon",
        "geosparql:asWKT": {
          "@type": "geosparql:wktLiteral",
          "@value": "POLYGON((-120.0 36.0, -114.0 36.0, -114.0 42.0, -120.0 42.0, -120.0 36.0))"
        },
        "geosparql:crs": {
          "@id": "http://www.opengis.net/def/crs/OGC/1.3/CRS84"
        }
      }
    }
  ],
  "schema:temporalCoverage": [
    {
      "@type": "time:ProperInterval",
      "schema:description": "Field sampling and laboratory analysis period",
      "time:hasBeginning": {
        "@type": "time:Instant",
        "time:inXSDDate": "2025-06-01"
      },
      "time:hasEnd": {
        "@type": "time:Instant",
        "time:inXSDDate": "2025-09-30"
      }
    },
    "2025-06-01/2025-09-30"
  ],
  "schema:relatedLink": [
    {
      "@type": "schema:LinkRole",
      "schema:linkRelationship": {
        "@type": "schema:DefinedTerm",
        "schema:name": "related dataset",
        "schema:inDefinedTermSet": "https://www.iana.org/assignments/link-relations/",
        "schema:termCode": "related"
      },
      "target": {
        "@type": "schema:EntryPoint",
        "schema:name": "Regional geology map of the Great Basin",
        "schema:url": "https://example.org/maps/great-basin-geology",
        "schema:encodingFormat": "image/png"
      }
    }
  ],
  "schema:publishingPrinciples": [
    {
      "@type": "schema:CreativeWork",
      "schema:name": "IEDA Data Management Plan",
      "schema:description": "Describes data curation, versioning, and long-term preservation policies for IEDA-hosted datasets",
      "schema:url": "https://www.iedadata.org/help/data-publication/"
    }
  ],
  "schema:distribution": [
    {
      "@type": [
        "schema:DataDownload"
      ],
      "schema:name": "Geochemistry summary results",
      "schema:contentUrl": "https://example.org/data/geochem-summary.csv",
      "schema:encodingFormat": [
        "text/csv"
      ],
      "spdx:checksum": {
        "@type": "spdx:Checksum",
        "spdx:algorithm": "SHA256",
        "spdx:checksumValue": "a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4e5f6a1b2"
      },
      "schema:provider": [
        {
          "@id": "https://ror.org/02fjgr047",
          "@type": "schema:Organization",
          "schema:name": "IEDA-"
        }
      ],
      "dcterms:conformsTo": [{"@id": "http://www.opengis.net/def/nil/OGC/0/missing"}]
    },
    {
      "@type": [
        "schema:DataDownload",
        "cdi:TabularTextDataSet"
      ],
      "schema:name": "Detailed geochemistry analysis results",
      "schema:contentUrl": "https://example.org/data/geochem-detailed.csv",
      "schema:encodingFormat": [
        "text/csv"
      ],
      "spdx:checksum": {
        "@type": "spdx:Checksum",
        "spdx:algorithm": "SHA256",
        "spdx:checksumValue": "b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3"
      },
      "cdi:isDelimited": true,
      "cdi:isFixedWidth": false,
      "csvw:delimiter": ",",
      "csvw:header": true,
      "csvw:headerRowCount": 1,
      "cdi:arrayBase": 0,
      "csvw:commentPrefix": "#",
      "csvw:lineTerminators": "LF",
      "csvw:quoteChar": "\"",
      "csvw:skipBlankRows": false,
      "csvw:skipColumns": 0,
      "csvw:skipInitialSpace": true,
      "csvw:skipRows": 0,
      "cdi:escapeCharacter": "\\",
      "cdi:headerIsCaseSensitive": false,
      "cdi:treatConsecutiveDelimitersAsOne": false,
      "csvw:tableDirection": "Ltr",
      "csvw:textDirection": "Auto",
      "csvw:trim": "true",
      "countRows": 461,
      "countColumns": 3,
      "cdi:hasPhysicalMapping": [
        {
          "cdi:index": 0,
          "cdi:format": "string",
          "cdi:physicalDataType": "string",
          "cdi:isRequired": true,
          "cdi:defaultValue": "UNKNOWN",
          "cdi:minimumLength": 3,
          "cdi:maximumLength": 40,
          "cdi:formats_InstanceVariable": {
            "@id": "ex:var-sampleID"
          }
        },
        {
          "cdi:index": 1,
          "cdi:format": "decimal",
          "cdi:physicalDataType": "float64",
          "cdi:nullSequence": "NA",
          "cdi:isRequired": true,
          "cdi:decimalPositions": 4,
          "cdi:formats_InstanceVariable": {
            "@id": "ex:var-concentration"
          }
        },
        {
          "cdi:index": 2,
          "cdi:format": "decimal",
          "cdi:physicalDataType": "float64",
          "cdi:nullSequence": "-9999",
          "cdi:isRequired": false,
          "cdi:decimalPositions": 4,
          "cdi:length": 12,
          "cdi:formats_InstanceVariable": {
            "@id": "ex:var-uncertainty"
          }
        }
      ],
      "dcterms:conformsTo": [{"@id": "http://www.opengis.net/def/nil/OGC/0/missing"}]
    },
    {
      "@type": [
        "schema:DataDownload",
        "cdi:StructuredDataSet"
      ],
      "schema:name": "Spectral data cube",
      "schema:contentUrl": "https://example.org/data/spectra-cube.nc",
      "schema:encodingFormat": [
        "application/x-netcdf"
      ],
      "spdx:checksum": {
        "@type": "spdx:Checksum",
        "spdx:algorithm": "SHA256",
        "spdx:checksumValue": "c3d4e5f6a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4"
      },
      "cdi:hasPhysicalMapping": [
        {
          "cdi:index": 0,
          "cdi:format": "decimal",
          "cdi:physicalDataType": "float32",
          "cdi:locator": "/spectra/wavelength",
          "cdi:isRequired": true,
          "cdi:formats_InstanceVariable": {
            "@id": "ex:var-wavelength"
          }
        },
        {
          "cdi:index": 1,
          "cdi:format": "decimal",
          "cdi:physicalDataType": "float32",
          "cdi:locator": "/spectra/intensity",
          "cdi:scale": 1000,
          "cdi:isRequired": true,
          "cdi:formats_InstanceVariable": {
            "@id": "ex:var-intensity"
          }
        }
      ],
      "dcterms:conformsTo": [{"@id": "http://www.opengis.net/def/nil/OGC/0/missing"}]
    },
    {
      "@type": [
        "schema:DataDownload"
      ],
      "schema:name": "Complete data package",
      "schema:contentUrl": "https://example.org/data/geochem-package.zip",
      "schema:encodingFormat": [
        "application/zip"
      ],
      "schema:description": "Archive containing all data files. Component files are listed as parts and are not individually accessible.",
      "spdx:checksum": {
        "@type": "spdx:Checksum",
        "spdx:algorithm": "SHA256",
        "spdx:checksumValue": "d4e5f6a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4e5"
      },
      "schema:hasPart": [
        {
          "@type": [
            "schema:MediaObject"
          ],
          "@id": "#part-results-csv",
          "schema:name": "geochem-detailed.csv",
          "schema:description": "Detailed geochemistry analysis results in tabular format.",
          "schema:encodingFormat": [
            "text/csv"
          ],
          "schema:size": {
            "@type": "schema:QuantitativeValue",
            "schema:value": 10860,
            "schema:unitText": "byte"
          },
          "spdx:checksum": {
            "@type": "spdx:Checksum",
            "spdx:algorithm": "SHA256",
            "spdx:checksumValue": "b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3"
          }
        },
        {
          "@type": [
            "schema:MediaObject",
            "cdi:TabularTextDataSet"
          ],
          "@id": "#part-measurements-csv",
          "schema:name": "geochem-measurements.csv",
          "schema:description": "Measurement data with column structure described via CSVW and physical mappings.",
          "schema:encodingFormat": [
            "text/csv"
          ],
          "schema:size": {
            "@type": "schema:QuantitativeValue",
            "schema:value": 6249,
            "schema:unitText": "byte"
          },
          "cdi:isDelimited": true,
          "csvw:delimiter": ",",
          "csvw:header": true,
          "csvw:headerRowCount": 1,
          "countRows": 144,
          "countColumns": 3,
          "cdi:hasPhysicalMapping": [
            {
              "cdi:index": 0,
              "cdi:format": "string",
              "cdi:physicalDataType": "string",
              "cdi:isRequired": true,
              "cdi:formats_InstanceVariable": {
                "@id": "ex:var-sampleID"
              }
            },
            {
              "cdi:index": 1,
              "cdi:format": "decimal",
              "cdi:physicalDataType": "float64",
              "cdi:nullSequence": "NA",
              "cdi:isRequired": true,
              "cdi:formats_InstanceVariable": {
                "@id": "ex:var-concentration"
              }
            },
            {
              "cdi:index": 2,
              "cdi:format": "decimal",
              "cdi:physicalDataType": "float64",
              "cdi:nullSequence": "NA",
              "cdi:isRequired": false,
              "cdi:formats_InstanceVariable": {
                "@id": "ex:var-uncertainty"
              }
            }
          ]
        },
        {
          "@type": [
            "schema:MediaObject",
            "cdi:StructuredDataSet"
          ],
          "@id": "#part-spectra-nc",
          "schema:name": "spectra-cube.nc",
          "schema:description": "Spectral data cube with wavelength and intensity dimensions.",
          "schema:encodingFormat": [
            "application/x-netcdf"
          ],
          "schema:size": {
            "@type": "schema:QuantitativeValue",
            "schema:value": 13743003,
            "schema:unitText": "byte"
          },
          "cdi:hasPhysicalMapping": [
            {
              "cdi:index": 0,
              "cdi:format": "decimal",
              "cdi:physicalDataType": "float32",
              "cdi:locator": "/spectra/wavelength",
              "cdi:isRequired": true,
              "cdi:formats_InstanceVariable": {
                "@id": "ex:var-wavelength"
              }
            },
            {
              "cdi:index": 1,
              "cdi:format": "decimal",
              "cdi:physicalDataType": "float32",
              "cdi:locator": "/spectra/intensity",
              "cdi:isRequired": true,
              "cdi:formats_InstanceVariable": {
                "@id": "ex:var-intensity"
              }
            }
          ]
        },
        {
          "@type": [
            "schema:MediaObject"
          ],
          "@id": "#part-method-pdf",
          "schema:name": "analysis-method.pdf",
          "schema:description": "Method description document for the analysis.",
          "schema:encodingFormat": [
            "application/pdf"
          ],
          "schema:size": {
            "@type": "schema:QuantitativeValue",
            "schema:value": 56062,
            "schema:unitText": "byte"
          }
        },
        {
          "@type": [
            "schema:MediaObject"
          ],
          "@id": "#part-metadata-yaml",
          "schema:name": "geochem-detailed-metadata.yaml",
          "schema:description": "Metadata sidecar for the results CSV file.",
          "schema:encodingFormat": [
            "application/yaml"
          ],
          "schema:size": {
            "@type": "schema:QuantitativeValue",
            "schema:value": 2281,
            "schema:unitText": "byte"
          },
          "schema:about": [
            {
              "@id": "#part-results-csv"
            }
          ]
        }
      ],
      "dcterms:conformsTo": [{"@id": "http://www.opengis.net/def/nil/OGC/0/missing"}]
    },
    {
      "@type": [
        "schema:WebAPI"
      ],
      "schema:serviceType": {
        "@type": "schema:DefinedTerm",
        "schema:name": "OGC API - Features",
        "schema:identifier": {
          "@type": "schema:PropertyValue",
          "schema:propertyID": "https://www.ogc.org/standards",
          "schema:value": "ogcapi-features-1",
          "schema:url": "https://www.ogc.org/standard/ogcapi-features/"
        },
        "schema:inDefinedTermSet": "https://www.ogc.org/standards",
        "schema:termCode": "ogcapi-features"
      },
      "schema:termsOfService": "Open access, no authentication required",
      "schema:documentation": {
        "@type": "schema:CreativeWork",
        "schema:name": "OpenAPI specification for geochemistry data service",
        "schema:url": "https://example.org/api/v1/openapi.json"
      },
      "schema:potentialAction": [
        {
          "@type": "schema:Action",
          "schema:name": "Query geochemistry features",
          "schema:target": {
            "@type": "schema:EntryPoint",
            "schema:description": "OGC API Features endpoint returning geochemistry observations as CSV",
            "schema:urlTemplate": "https://example.org/api/v1/collections/geochem/items?f={format}&limit={limit}&offset={offset}",
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
            "schema:contentUrl": "https://example.org/api/v1/collections/geochem/items?f=csv",
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
                  "@id": "ex:var-concentration"
                }
              },
              {
                "cdi:index": 1,
                "cdi:format": "decimal",
                "cdi:physicalDataType": "float64",
                "cdi:isRequired": false,
                "cdi:formats_InstanceVariable": {
                  "@id": "ex:var-uncertainty"
                }
              }
            ],
            "dcterms:conformsTo": [{"@id": "http://www.opengis.net/def/nil/OGC/0/missing"}]
          },
          "schema:object": {
            "@type": "schema:DataFeed",
            "schema:description": "Geochemistry observations collection"
          },
          "schema:query-input": [
            {
              "@type": "schema:PropertyValueSpecification",
              "schema:valueName": "format",
              "schema:description": "Response format: csv or geojson",
              "schema:valueRequired": false,
              "schema:valuePattern": "csv|geojson"
            },
            {
              "@type": "schema:PropertyValueSpecification",
              "schema:valueName": "limit",
              "schema:description": "Maximum number of features to return",
              "schema:valueRequired": false
            },
            {
              "@type": "schema:PropertyValueSpecification",
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
      "@id": "ex:var-sampleID",
      "schema:name": "Sample identifier",
      "schema:description": "Unique identifier for each sample",
      "schema:propertyID": [
        "urn:example:property:sampleID"
      ]
    },
    {
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "@id": "ex:var-concentration",
      "schema:name": "Element concentration",
      "schema:alternateName": [
        "concentration_ppm",
        "element_conc"
      ],
      "schema:description": "Measured element concentration in parts per million",
      "schema:propertyID": [
        "urn:example:property:concentration"
      ],
      "schema:url": "https://example.org/docs/variables/concentration",
      "schema:measurementTechnique": "ICP-MS",
      "schema:unitText": "ppm",
      "schema:unitCode": "59",
      "schema:minValue": 0.01,
      "schema:maxValue": 5000
    },
    {
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "@id": "ex:var-uncertainty",
      "schema:name": "Measurement uncertainty",
      "schema:description": "2-sigma uncertainty on concentration measurement",
      "schema:propertyID": [
        "urn:example:property:uncertainty"
      ],
      "schema:unitText": "ppm",
      "schema:unitCode": "59"
    },
    {
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "@id": "ex:var-wavelength",
      "schema:name": "Wavelength",
      "schema:description": "Spectral wavelength",
      "schema:propertyID": [
        "urn:example:property:wavelength"
      ],
      "schema:unitText": "nm",
      "schema:minValue": 200,
      "schema:maxValue": 2500
    },
    {
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "@id": "ex:var-intensity",
      "schema:name": "Spectral intensity",
      "schema:description": "Measured spectral intensity",
      "schema:propertyID": [
        "urn:example:property:intensity"
      ],
      "schema:unitText": "counts"
    }
  ],
  "prov:wasGeneratedBy": [
    {
      "@id": "ex:activity-geochem-analysis",
      "@type": [
        "schema:Action",
        "prov:Activity"
      ],
      "schema:name": "Soil Geochemistry Analysis - Great Basin Transect 2025",
      "schema:description": "Major and trace element analysis of soil samples from Great Basin transect sites using ICP-MS with EPA Method 6200 protocols.",
      "schema:identifier": {
        "@type": "schema:PropertyValue",
        "schema:propertyID": "https://example.org/activities",
        "schema:value": "GEOCHEM-GB-2025-001",
        "schema:url": "https://example.org/activities/GEOCHEM-GB-2025-001"
      },
      "prov:used": [
        {
          "schema:instrument": {
            "@type": [
              "schema:Thing",
              "schema:DefinedTerm"
            ],
            "schema:name": "Inductively Coupled Plasma Mass Spectrometry",
            "schema:termCode": "ICP-MS",
            "schema:inDefinedTermSet": "https://vocab.nerc.ac.uk/collection/L05/current/",
            "schema:alternateName": "Thermo Fisher iCAP RQ ICP-MS",
            "schema:additionalProperty": [
              {
                "@type": "schema:PropertyValue",
                "schema:propertyID": [
                  "detectionLimit"
                ],
                "schema:name": "Typical Detection Limit",
                "schema:value": "0.01 mg/kg for trace elements"
              }
            ],
            "schema:hasPart": [
              {
                "@type": [
                  "schema:Thing"
                ],
                "schema:name": "Autosampler",
                "schema:alternateName": "CETAC ASX-560"
              },
              {
                "@type": [
                  "schema:Thing"
                ],
                "schema:name": "Spray chamber",
                "schema:alternateName": "Peltier-cooled cyclonic"
              }
            ]
          }
        },
        "https://vocab.nerc.ac.uk/collection/L05/current/LAB02",
        "Soil core samples collected June 2025, sites GB-001 through GB-045, dried and sieved to <2 mm fraction",
        {
          "@type": "schema:CreativeWork",
          "schema:name": "EPA Method 6200 - XRF Analysis of Soils",
          "schema:url": "https://www.epa.gov/hw-sw846/sw-846-test-method-6200-field-portable-x-ray-fluorescence-spectrometry-determination"
        }
      ],
      "schema:agent": {
        "@id": "https://orcid.org/0000-0001-2345-6789"
      },
      "schema:participant": [
        {
          "@type": "schema:Role",
          "schema:roleName": "Lab Technician",
          "schema:contributor": {
            "@id": "https://orcid.org/0000-0003-5555-7777"
          }
        }
      ],
      "schema:object": "Dried and sieved soil samples (<2 mm fraction) from Great Basin transect",
      "schema:result": {
        "@id": "ex:complete-dataset-001"
      },
      "schema:actionStatus": "schema:CompletedActionStatus",
      "schema:startTime": "2025-07-15T08:00:00Z",
      "schema:endTime": "2025-09-30T17:00:00Z",
      "schema:location": {
        "@type": "schema:Place",
        "schema:name": "Nevada Bureau of Mines and Geology Analytical Lab",
        "schema:address": "University of Nevada, Reno, 1664 N. Virginia Street, Reno, NV 89557",
        "schema:url": "https://www.unr.edu/nbmg"
      },
      "schema:actionProcess": {
        "@type": "schema:HowTo",
        "schema:name": "EPA 6200 / ICP-MS Soil Geochemistry Protocol",
        "schema:description": "Combined XRF screening and ICP-MS confirmatory analysis for major and trace elements in soils.",
        "schema:step": [
          {
            "@type": "schema:HowToStep",
            "schema:name": "Sample preparation and acid digestion",
            "schema:description": "Homogenize dried samples, split 0.5 g aliquots, digest with HNO3-HCl-HF mixture at 190 C for 20 min in a microwave system.",
            "schema:url": "https://example.org/protocols/digestion-procedure",
            "schema:position": 1
          },
          {
            "@type": "schema:HowToStep",
            "schema:name": "ICP-MS measurement and calibration",
            "schema:description": "Analyze digested solutions by ICP-MS using external calibration with NIST SRM 2711a (Montana II Soil).",
            "schema:url": "https://example.org/protocols/icpms-measurement",
            "schema:position": 2
          }
        ]
      },
      "schema:error": "",
      "schema:additionalProperty": [
        {
          "@type": "schema:PropertyValue",
          "schema:propertyID": [
            "batchID"
          ],
          "schema:name": "Analysis Batch Identifier",
          "schema:value": "GB-2025-BATCH-03"
        }
      ]
    }
  ],
  "prov:wasDerivedFrom": [
    {
      "@id": "https://example.org/fieldwork/gb-transect-2025/raw-samples"
    },
    {
      "@id": "https://doi.org/10.5880/example.field.001"
    },
    {
      "@type": "schema:CreativeWork",
      "schema:name": "USGS Great Basin Geochemical Survey (2020)",
      "schema:description": "Prior regional geochemical survey used for site selection and comparative analysis",
      "schema:url": "https://pubs.usgs.gov/of/2020/example-great-basin"
    }
  ],
  "dqv:hasQualityMeasurement": [
    {
      "@type": "dqv:QualityMeasurement",
      "dqv:isMeasurementOf": {
        "@type": "schema:DefinedTerm",
        "schema:name": "Completeness",
        "schema:inDefinedTermSet": "https://www.w3.org/TR/vocab-dqv/",
        "schema:termCode": "completeness"
      },
      "dqv:value": "98.5% of planned sample sites successfully analyzed"
    },
    {
      "@type": "dqv:QualityMeasurement",
      "dqv:isMeasurementOf": "Analytical precision (2-sigma RSD on NIST SRM 2711a replicates)",
      "dqv:value": {
        "@type": "schema:DefinedTerm",
        "schema:name": "High-",
        "schema:inDefinedTermSet": "https://example.org/quality-levels/",
        "schema:termCode": "HIGH"
      }
    }
  ],
  "schema:subjectOf": {
    "@type": [
      "schema:Dataset"
    ],
    "schema:additionalType": [
      "dcat:CatalogRecord"
    ],
    "@id": "ex:metadata-record-001",
    "schema:about": {
      "@id": "ex:complete-dataset-001"
    },
    "dcterms:conformsTo": [
      {
        "@id": "https://w3id.org/cdif/bbr/metadata/profiles/cdifProfiles/CDIFcomplete"
      }
    ],
    "schema:maintainer": {
      "@id": "https://orcid.org/0000-0001-2345-6789",
      "@type": "schema:Person",
      "schema:name": "Smith, Jane"
    },
    "schema:sdDatePublished": "2026-02-19",
    "schema:includedInDataCatalog": {
      "@id": "ex:ieda-catalog",
      "@type": "schema:DataCatalog",
      "schema:name": "IEDA Data Catalog",
      "schema:url": "https://www.earthchem.org/"
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
      "csvw": "http://www.w3.org/ns/csvw#",
      "dcterms": "http://purl.org/dc/terms/",
      "spdx": "http://spdx.org/rdf/terms#",
      "prov": "http://www.w3.org/ns/prov#"
    },
    "https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/profiles/cdifProfiles/CDIFcomplete/context.jsonld",
    {
      "schema": "http://schema.org/",
      "dcterms": "http://purl.org/dc/terms/",
      "geosparql": "http://www.opengis.net/ont/geosparql#",
      "spdx": "http://spdx.org/rdf/terms#",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "csvw": "http://www.w3.org/ns/csvw#",
      "prov": "http://www.w3.org/ns/prov#",
      "time": "http://www.w3.org/2006/time#",
      "dqv": "http://www.w3.org/ns/dqv#",
      "sf": "http://www.opengis.net/ont/sf#",
      "ex": "https://example.org/",
      "xsd": "http://www.w3.org/2001/XMLSchema#",
      "dcat": "http://www.w3.org/ns/dcat#"
    }
  ],
  "@id": "ex:complete-dataset-001",
  "@type": [
    "schema:Dataset"
  ],
  "schema:name": "Multi-technique geochemistry dataset with archive and API access",
  "schema:description": "Comprehensive geochemistry dataset demonstrating the CDIF complete profile with single-file downloads, archive distribution with component files, and WebAPI access. Includes tabular CSV results, NetCDF data cubes, and an OGC API Features endpoint.",
  "schema:additionalType": [
    "geochemistry analysis"
  ],
  "schema:identifier": {
    "@type": "schema:PropertyValue",
    "schema:propertyID": "https://registry.identifiers.org/registry/doi",
    "schema:value": "10.5880/example.complete.001",
    "schema:url": "https://doi.org/10.5880/example.complete.001"
  },
  "schema:sameAs": [
    {
      "@type": "schema:PropertyValue",
      "schema:value": "urn:example:geochem:complete-001"
    }
  ],
  "schema:version": "1.0",
  "schema:url": "https://example.org/datasets/complete-001",
  "schema:inLanguage": "en",
  "schema:dateModified": "2026-02-15",
  "schema:datePublished": "2026-02-01",
  "schema:license": [
    "https://creativecommons.org/licenses/by/4.0/"
  ],
  "schema:conditionsOfAccess": [
    "Open access; citation required"
  ],
  "schema:keywords": [
    {
      "@type": "schema:DefinedTerm",
      "schema:name": "geochemistry",
      "schema:identifier": {
        "@type": "schema:PropertyValue",
        "schema:propertyID": "https://vocabularyserver.com/keyword",
        "schema:value": "geochem-001",
        "schema:url": "https://vocabularyserver.com/keyword/geochem-001"
      },
      "schema:inDefinedTermSet": "https://vocabularyserver.com/keyword",
      "schema:termCode": "GEOCHEM"
    },
    {
      "@type": "schema:DefinedTerm",
      "schema:name": "spectral analysis",
      "schema:identifier": {
        "@type": "schema:PropertyValue",
        "schema:propertyID": "https://vocabularyserver.com/keyword",
        "schema:value": "spectral-001",
        "schema:url": "https://vocabularyserver.com/keyword/spectral-001"
      },
      "schema:inDefinedTermSet": "https://vocabularyserver.com/keyword",
      "schema:termCode": "SPECTRAL"
    }
  ],
  "schema:creator": {
    "@list": [
      {
        "@id": "https://orcid.org/0000-0001-2345-6789",
        "@type": "schema:Person",
        "schema:name": "Smith, Jane",
        "schema:alternateName": "J. Smith",
        "schema:description": "Geochemistry researcher specializing in trace element analysis and environmental mineralogy",
        "schema:affiliation": {
          "@id": "https://ror.org/03m2x1q45",
          "@type": "schema:Organization",
          "schema:name": "University of Arizona"
        },
        "schema:contactPoint": {
          "@type": "schema:ContactPoint",
          "schema:email": "jsmith@arizona.edu"
        },
        "schema:identifier": {
          "@type": "schema:PropertyValue",
          "schema:propertyID": "https://orcid.org",
          "schema:value": "0000-0001-2345-6789",
          "schema:url": "https://orcid.org/0000-0001-2345-6789"
        }
      }
    ]
  },
  "schema:publisher": {
    "@id": "ex:ieda-publisher",
    "@type": "schema:Organization",
    "schema:name": "IEDA-",
    "schema:alternateName": "Interdisciplinary Earth Data Alliance",
    "schema:description": "An NSF-supported data facility for geochemistry and related disciplines",
    "schema:identifier": {
      "@type": "schema:PropertyValue",
      "schema:propertyID": "https://registry.identifiers.org/registry/ror",
      "schema:value": "02fjgr047",
      "schema:url": "https://ror.org/02fjgr047"
    }
  },
  "schema:funding": [
    {
      "@type": "schema:MonetaryGrant",
      "schema:identifier": {
        "@type": "schema:PropertyValue",
        "schema:propertyID": "NSF award number",
        "schema:value": "EAR-2026932",
        "schema:url": "https://www.nsf.gov/awardsearch/showAward?AWD_ID=2026932"
      },
      "schema:name": "Geochemistry Data Infrastructure",
      "schema:funder": {
        "@id": "https://ror.org/021nxhr62"
      }
    }
  ],
  "schema:provider": [
    {
      "@id": "https://ror.org/02fjgr047",
      "@type": "schema:Organization",
      "schema:name": "IEDA-",
      "schema:url": "https://www.earthchem.org/"
    }
  ],
  "schema:contributor": [
    {
      "@type": "schema:Role",
      "schema:roleName": {
        "@type": "schema:DefinedTerm",
        "schema:name": "Data Manager",
        "schema:inDefinedTermSet": "https://credit.niso.org/",
        "schema:termCode": "data-curation"
      },
      "schema:contributor": {
        "@id": "https://orcid.org/0000-0003-5555-7777",
        "@type": "schema:Person",
        "schema:name": "Lee, Robert",
        "schema:contactPoint": {
          "@type": "schema:ContactPoint",
          "schema:email": "rlee@example.org"
        }
      }
    },
    {
      "@id": "https://ror.org/03m2x1q45",
      "@type": "schema:Organization",
      "schema:name": "University of Arizona"
    }
  ],
  "schema:measurementTechnique": {
    "@type": "schema:DefinedTerm",
    "schema:name": "Inductively Coupled Plasma Mass Spectrometry",
    "schema:identifier": {
      "@type": "schema:PropertyValue",
      "schema:propertyID": "https://vocab.nerc.ac.uk/collection/L05/current/",
      "schema:value": "LAB21",
      "schema:url": "https://vocab.nerc.ac.uk/collection/L05/current/LAB21/"
    },
    "schema:inDefinedTermSet": "https://vocab.nerc.ac.uk/collection/L05/current/",
    "schema:termCode": "ICP-MS"
  },
  "schema:spatialCoverage": [
    {
      "@type": "schema:Place",
      "schema:name": [
        "Great Basin",
        {
          "@type": "schema:DefinedTerm",
          "schema:name": "Great Basin physiographic province",
          "schema:identifier": {
            "@type": "schema:PropertyValue",
            "schema:propertyID": "https://www.geonames.org/",
            "schema:value": "5509151",
            "schema:url": "https://www.geonames.org/5509151"
          },
          "schema:inDefinedTermSet": "https://www.geonames.org/",
          "schema:termCode": "5509151"
        }
      ],
      "schema:geo": {
        "@type": "schema:GeoShape",
        "schema:box": "36.0 -120.0 42.0 -114.0"
      },
      "geosparql:hasGeometry": {
        "@type": "sf:Polygon",
        "geosparql:asWKT": {
          "@type": "geosparql:wktLiteral",
          "@value": "POLYGON((-120.0 36.0, -114.0 36.0, -114.0 42.0, -120.0 42.0, -120.0 36.0))"
        },
        "geosparql:crs": {
          "@id": "http://www.opengis.net/def/crs/OGC/1.3/CRS84"
        }
      }
    }
  ],
  "schema:temporalCoverage": [
    {
      "@type": "time:ProperInterval",
      "schema:description": "Field sampling and laboratory analysis period",
      "time:hasBeginning": {
        "@type": "time:Instant",
        "time:inXSDDate": "2025-06-01"
      },
      "time:hasEnd": {
        "@type": "time:Instant",
        "time:inXSDDate": "2025-09-30"
      }
    },
    "2025-06-01/2025-09-30"
  ],
  "schema:relatedLink": [
    {
      "@type": "schema:LinkRole",
      "schema:linkRelationship": {
        "@type": "schema:DefinedTerm",
        "schema:name": "related dataset",
        "schema:inDefinedTermSet": "https://www.iana.org/assignments/link-relations/",
        "schema:termCode": "related"
      },
      "target": {
        "@type": "schema:EntryPoint",
        "schema:name": "Regional geology map of the Great Basin",
        "schema:url": "https://example.org/maps/great-basin-geology",
        "schema:encodingFormat": "image/png"
      }
    }
  ],
  "schema:publishingPrinciples": [
    {
      "@type": "schema:CreativeWork",
      "schema:name": "IEDA Data Management Plan",
      "schema:description": "Describes data curation, versioning, and long-term preservation policies for IEDA-hosted datasets",
      "schema:url": "https://www.iedadata.org/help/data-publication/"
    }
  ],
  "schema:distribution": [
    {
      "@type": [
        "schema:DataDownload"
      ],
      "schema:name": "Geochemistry summary results",
      "schema:contentUrl": "https://example.org/data/geochem-summary.csv",
      "schema:encodingFormat": [
        "text/csv"
      ],
      "spdx:checksum": {
        "@type": "spdx:Checksum",
        "spdx:algorithm": "SHA256",
        "spdx:checksumValue": "a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4e5f6a1b2"
      },
      "schema:provider": [
        {
          "@id": "https://ror.org/02fjgr047",
          "@type": "schema:Organization",
          "schema:name": "IEDA-"
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
      "schema:name": "Detailed geochemistry analysis results",
      "schema:contentUrl": "https://example.org/data/geochem-detailed.csv",
      "schema:encodingFormat": [
        "text/csv"
      ],
      "spdx:checksum": {
        "@type": "spdx:Checksum",
        "spdx:algorithm": "SHA256",
        "spdx:checksumValue": "b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3"
      },
      "cdi:isDelimited": true,
      "cdi:isFixedWidth": false,
      "csvw:delimiter": ",",
      "csvw:header": true,
      "csvw:headerRowCount": 1,
      "cdi:arrayBase": 0,
      "csvw:commentPrefix": "#",
      "csvw:lineTerminators": "LF",
      "csvw:quoteChar": "\"",
      "csvw:skipBlankRows": false,
      "csvw:skipColumns": 0,
      "csvw:skipInitialSpace": true,
      "csvw:skipRows": 0,
      "cdi:escapeCharacter": "\\",
      "cdi:headerIsCaseSensitive": false,
      "cdi:treatConsecutiveDelimitersAsOne": false,
      "csvw:tableDirection": "Ltr",
      "csvw:textDirection": "Auto",
      "csvw:trim": "true",
      "countRows": 461,
      "countColumns": 3,
      "cdi:hasPhysicalMapping": [
        {
          "cdi:index": 0,
          "cdi:format": "string",
          "cdi:physicalDataType": "string",
          "cdi:isRequired": true,
          "cdi:defaultValue": "UNKNOWN",
          "cdi:minimumLength": 3,
          "cdi:maximumLength": 40,
          "cdi:formats_InstanceVariable": {
            "@id": "ex:var-sampleID"
          }
        },
        {
          "cdi:index": 1,
          "cdi:format": "decimal",
          "cdi:physicalDataType": "float64",
          "cdi:nullSequence": "NA",
          "cdi:isRequired": true,
          "cdi:decimalPositions": 4,
          "cdi:formats_InstanceVariable": {
            "@id": "ex:var-concentration"
          }
        },
        {
          "cdi:index": 2,
          "cdi:format": "decimal",
          "cdi:physicalDataType": "float64",
          "cdi:nullSequence": "-9999",
          "cdi:isRequired": false,
          "cdi:decimalPositions": 4,
          "cdi:length": 12,
          "cdi:formats_InstanceVariable": {
            "@id": "ex:var-uncertainty"
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
      "schema:name": "Spectral data cube",
      "schema:contentUrl": "https://example.org/data/spectra-cube.nc",
      "schema:encodingFormat": [
        "application/x-netcdf"
      ],
      "spdx:checksum": {
        "@type": "spdx:Checksum",
        "spdx:algorithm": "SHA256",
        "spdx:checksumValue": "c3d4e5f6a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4"
      },
      "cdi:hasPhysicalMapping": [
        {
          "cdi:index": 0,
          "cdi:format": "decimal",
          "cdi:physicalDataType": "float32",
          "cdi:locator": "/spectra/wavelength",
          "cdi:isRequired": true,
          "cdi:formats_InstanceVariable": {
            "@id": "ex:var-wavelength"
          }
        },
        {
          "cdi:index": 1,
          "cdi:format": "decimal",
          "cdi:physicalDataType": "float32",
          "cdi:locator": "/spectra/intensity",
          "cdi:scale": 1000,
          "cdi:isRequired": true,
          "cdi:formats_InstanceVariable": {
            "@id": "ex:var-intensity"
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
      "schema:name": "Complete data package",
      "schema:contentUrl": "https://example.org/data/geochem-package.zip",
      "schema:encodingFormat": [
        "application/zip"
      ],
      "schema:description": "Archive containing all data files. Component files are listed as parts and are not individually accessible.",
      "spdx:checksum": {
        "@type": "spdx:Checksum",
        "spdx:algorithm": "SHA256",
        "spdx:checksumValue": "d4e5f6a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4e5"
      },
      "schema:hasPart": [
        {
          "@type": [
            "schema:MediaObject"
          ],
          "@id": "#part-results-csv",
          "schema:name": "geochem-detailed.csv",
          "schema:description": "Detailed geochemistry analysis results in tabular format.",
          "schema:encodingFormat": [
            "text/csv"
          ],
          "schema:size": {
            "@type": "schema:QuantitativeValue",
            "schema:value": 10860,
            "schema:unitText": "byte"
          },
          "spdx:checksum": {
            "@type": "spdx:Checksum",
            "spdx:algorithm": "SHA256",
            "spdx:checksumValue": "b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3"
          }
        },
        {
          "@type": [
            "schema:MediaObject",
            "cdi:TabularTextDataSet"
          ],
          "@id": "#part-measurements-csv",
          "schema:name": "geochem-measurements.csv",
          "schema:description": "Measurement data with column structure described via CSVW and physical mappings.",
          "schema:encodingFormat": [
            "text/csv"
          ],
          "schema:size": {
            "@type": "schema:QuantitativeValue",
            "schema:value": 6249,
            "schema:unitText": "byte"
          },
          "cdi:isDelimited": true,
          "csvw:delimiter": ",",
          "csvw:header": true,
          "csvw:headerRowCount": 1,
          "countRows": 144,
          "countColumns": 3,
          "cdi:hasPhysicalMapping": [
            {
              "cdi:index": 0,
              "cdi:format": "string",
              "cdi:physicalDataType": "string",
              "cdi:isRequired": true,
              "cdi:formats_InstanceVariable": {
                "@id": "ex:var-sampleID"
              }
            },
            {
              "cdi:index": 1,
              "cdi:format": "decimal",
              "cdi:physicalDataType": "float64",
              "cdi:nullSequence": "NA",
              "cdi:isRequired": true,
              "cdi:formats_InstanceVariable": {
                "@id": "ex:var-concentration"
              }
            },
            {
              "cdi:index": 2,
              "cdi:format": "decimal",
              "cdi:physicalDataType": "float64",
              "cdi:nullSequence": "NA",
              "cdi:isRequired": false,
              "cdi:formats_InstanceVariable": {
                "@id": "ex:var-uncertainty"
              }
            }
          ]
        },
        {
          "@type": [
            "schema:MediaObject",
            "cdi:StructuredDataSet"
          ],
          "@id": "#part-spectra-nc",
          "schema:name": "spectra-cube.nc",
          "schema:description": "Spectral data cube with wavelength and intensity dimensions.",
          "schema:encodingFormat": [
            "application/x-netcdf"
          ],
          "schema:size": {
            "@type": "schema:QuantitativeValue",
            "schema:value": 13743003,
            "schema:unitText": "byte"
          },
          "cdi:hasPhysicalMapping": [
            {
              "cdi:index": 0,
              "cdi:format": "decimal",
              "cdi:physicalDataType": "float32",
              "cdi:locator": "/spectra/wavelength",
              "cdi:isRequired": true,
              "cdi:formats_InstanceVariable": {
                "@id": "ex:var-wavelength"
              }
            },
            {
              "cdi:index": 1,
              "cdi:format": "decimal",
              "cdi:physicalDataType": "float32",
              "cdi:locator": "/spectra/intensity",
              "cdi:isRequired": true,
              "cdi:formats_InstanceVariable": {
                "@id": "ex:var-intensity"
              }
            }
          ]
        },
        {
          "@type": [
            "schema:MediaObject"
          ],
          "@id": "#part-method-pdf",
          "schema:name": "analysis-method.pdf",
          "schema:description": "Method description document for the analysis.",
          "schema:encodingFormat": [
            "application/pdf"
          ],
          "schema:size": {
            "@type": "schema:QuantitativeValue",
            "schema:value": 56062,
            "schema:unitText": "byte"
          }
        },
        {
          "@type": [
            "schema:MediaObject"
          ],
          "@id": "#part-metadata-yaml",
          "schema:name": "geochem-detailed-metadata.yaml",
          "schema:description": "Metadata sidecar for the results CSV file.",
          "schema:encodingFormat": [
            "application/yaml"
          ],
          "schema:size": {
            "@type": "schema:QuantitativeValue",
            "schema:value": 2281,
            "schema:unitText": "byte"
          },
          "schema:about": [
            {
              "@id": "#part-results-csv"
            }
          ]
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
        "@type": "schema:DefinedTerm",
        "schema:name": "OGC API - Features",
        "schema:identifier": {
          "@type": "schema:PropertyValue",
          "schema:propertyID": "https://www.ogc.org/standards",
          "schema:value": "ogcapi-features-1",
          "schema:url": "https://www.ogc.org/standard/ogcapi-features/"
        },
        "schema:inDefinedTermSet": "https://www.ogc.org/standards",
        "schema:termCode": "ogcapi-features"
      },
      "schema:termsOfService": "Open access, no authentication required",
      "schema:documentation": {
        "@type": "schema:CreativeWork",
        "schema:name": "OpenAPI specification for geochemistry data service",
        "schema:url": "https://example.org/api/v1/openapi.json"
      },
      "schema:potentialAction": [
        {
          "@type": "schema:Action",
          "schema:name": "Query geochemistry features",
          "schema:target": {
            "@type": "schema:EntryPoint",
            "schema:description": "OGC API Features endpoint returning geochemistry observations as CSV",
            "schema:urlTemplate": "https://example.org/api/v1/collections/geochem/items?f={format}&limit={limit}&offset={offset}",
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
            "schema:contentUrl": "https://example.org/api/v1/collections/geochem/items?f=csv",
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
                  "@id": "ex:var-concentration"
                }
              },
              {
                "cdi:index": 1,
                "cdi:format": "decimal",
                "cdi:physicalDataType": "float64",
                "cdi:isRequired": false,
                "cdi:formats_InstanceVariable": {
                  "@id": "ex:var-uncertainty"
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
            "@type": "schema:DataFeed",
            "schema:description": "Geochemistry observations collection"
          },
          "schema:query-input": [
            {
              "@type": "schema:PropertyValueSpecification",
              "schema:valueName": "format",
              "schema:description": "Response format: csv or geojson",
              "schema:valueRequired": false,
              "schema:valuePattern": "csv|geojson"
            },
            {
              "@type": "schema:PropertyValueSpecification",
              "schema:valueName": "limit",
              "schema:description": "Maximum number of features to return",
              "schema:valueRequired": false
            },
            {
              "@type": "schema:PropertyValueSpecification",
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
      "@id": "ex:var-sampleID",
      "schema:name": "Sample identifier",
      "schema:description": "Unique identifier for each sample",
      "schema:propertyID": [
        "urn:example:property:sampleID"
      ]
    },
    {
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "@id": "ex:var-concentration",
      "schema:name": "Element concentration",
      "schema:alternateName": [
        "concentration_ppm",
        "element_conc"
      ],
      "schema:description": "Measured element concentration in parts per million",
      "schema:propertyID": [
        "urn:example:property:concentration"
      ],
      "schema:url": "https://example.org/docs/variables/concentration",
      "schema:measurementTechnique": "ICP-MS",
      "schema:unitText": "ppm",
      "schema:unitCode": "59",
      "schema:minValue": 0.01,
      "schema:maxValue": 5000
    },
    {
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "@id": "ex:var-uncertainty",
      "schema:name": "Measurement uncertainty",
      "schema:description": "2-sigma uncertainty on concentration measurement",
      "schema:propertyID": [
        "urn:example:property:uncertainty"
      ],
      "schema:unitText": "ppm",
      "schema:unitCode": "59"
    },
    {
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "@id": "ex:var-wavelength",
      "schema:name": "Wavelength",
      "schema:description": "Spectral wavelength",
      "schema:propertyID": [
        "urn:example:property:wavelength"
      ],
      "schema:unitText": "nm",
      "schema:minValue": 200,
      "schema:maxValue": 2500
    },
    {
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "@id": "ex:var-intensity",
      "schema:name": "Spectral intensity",
      "schema:description": "Measured spectral intensity",
      "schema:propertyID": [
        "urn:example:property:intensity"
      ],
      "schema:unitText": "counts"
    }
  ],
  "prov:wasGeneratedBy": [
    {
      "@id": "ex:activity-geochem-analysis",
      "@type": [
        "schema:Action",
        "prov:Activity"
      ],
      "schema:name": "Soil Geochemistry Analysis - Great Basin Transect 2025",
      "schema:description": "Major and trace element analysis of soil samples from Great Basin transect sites using ICP-MS with EPA Method 6200 protocols.",
      "schema:identifier": {
        "@type": "schema:PropertyValue",
        "schema:propertyID": "https://example.org/activities",
        "schema:value": "GEOCHEM-GB-2025-001",
        "schema:url": "https://example.org/activities/GEOCHEM-GB-2025-001"
      },
      "prov:used": [
        {
          "schema:instrument": {
            "@type": [
              "schema:Thing",
              "schema:DefinedTerm"
            ],
            "schema:name": "Inductively Coupled Plasma Mass Spectrometry",
            "schema:termCode": "ICP-MS",
            "schema:inDefinedTermSet": "https://vocab.nerc.ac.uk/collection/L05/current/",
            "schema:alternateName": "Thermo Fisher iCAP RQ ICP-MS",
            "schema:additionalProperty": [
              {
                "@type": "schema:PropertyValue",
                "schema:propertyID": [
                  "detectionLimit"
                ],
                "schema:name": "Typical Detection Limit",
                "schema:value": "0.01 mg/kg for trace elements"
              }
            ],
            "schema:hasPart": [
              {
                "@type": [
                  "schema:Thing"
                ],
                "schema:name": "Autosampler",
                "schema:alternateName": "CETAC ASX-560"
              },
              {
                "@type": [
                  "schema:Thing"
                ],
                "schema:name": "Spray chamber",
                "schema:alternateName": "Peltier-cooled cyclonic"
              }
            ]
          }
        },
        "https://vocab.nerc.ac.uk/collection/L05/current/LAB02",
        "Soil core samples collected June 2025, sites GB-001 through GB-045, dried and sieved to <2 mm fraction",
        {
          "@type": "schema:CreativeWork",
          "schema:name": "EPA Method 6200 - XRF Analysis of Soils",
          "schema:url": "https://www.epa.gov/hw-sw846/sw-846-test-method-6200-field-portable-x-ray-fluorescence-spectrometry-determination"
        }
      ],
      "schema:agent": {
        "@id": "https://orcid.org/0000-0001-2345-6789"
      },
      "schema:participant": [
        {
          "@type": "schema:Role",
          "schema:roleName": "Lab Technician",
          "schema:contributor": {
            "@id": "https://orcid.org/0000-0003-5555-7777"
          }
        }
      ],
      "schema:object": "Dried and sieved soil samples (<2 mm fraction) from Great Basin transect",
      "schema:result": {
        "@id": "ex:complete-dataset-001"
      },
      "schema:actionStatus": "schema:CompletedActionStatus",
      "schema:startTime": "2025-07-15T08:00:00Z",
      "schema:endTime": "2025-09-30T17:00:00Z",
      "schema:location": {
        "@type": "schema:Place",
        "schema:name": "Nevada Bureau of Mines and Geology Analytical Lab",
        "schema:address": "University of Nevada, Reno, 1664 N. Virginia Street, Reno, NV 89557",
        "schema:url": "https://www.unr.edu/nbmg"
      },
      "schema:actionProcess": {
        "@type": "schema:HowTo",
        "schema:name": "EPA 6200 / ICP-MS Soil Geochemistry Protocol",
        "schema:description": "Combined XRF screening and ICP-MS confirmatory analysis for major and trace elements in soils.",
        "schema:step": [
          {
            "@type": "schema:HowToStep",
            "schema:name": "Sample preparation and acid digestion",
            "schema:description": "Homogenize dried samples, split 0.5 g aliquots, digest with HNO3-HCl-HF mixture at 190 C for 20 min in a microwave system.",
            "schema:url": "https://example.org/protocols/digestion-procedure",
            "schema:position": 1
          },
          {
            "@type": "schema:HowToStep",
            "schema:name": "ICP-MS measurement and calibration",
            "schema:description": "Analyze digested solutions by ICP-MS using external calibration with NIST SRM 2711a (Montana II Soil).",
            "schema:url": "https://example.org/protocols/icpms-measurement",
            "schema:position": 2
          }
        ]
      },
      "schema:error": "",
      "schema:additionalProperty": [
        {
          "@type": "schema:PropertyValue",
          "schema:propertyID": [
            "batchID"
          ],
          "schema:name": "Analysis Batch Identifier",
          "schema:value": "GB-2025-BATCH-03"
        }
      ]
    }
  ],
  "prov:wasDerivedFrom": [
    {
      "@id": "https://example.org/fieldwork/gb-transect-2025/raw-samples"
    },
    {
      "@id": "https://doi.org/10.5880/example.field.001"
    },
    {
      "@type": "schema:CreativeWork",
      "schema:name": "USGS Great Basin Geochemical Survey (2020)",
      "schema:description": "Prior regional geochemical survey used for site selection and comparative analysis",
      "schema:url": "https://pubs.usgs.gov/of/2020/example-great-basin"
    }
  ],
  "dqv:hasQualityMeasurement": [
    {
      "@type": "dqv:QualityMeasurement",
      "dqv:isMeasurementOf": {
        "@type": "schema:DefinedTerm",
        "schema:name": "Completeness",
        "schema:inDefinedTermSet": "https://www.w3.org/TR/vocab-dqv/",
        "schema:termCode": "completeness"
      },
      "dqv:value": "98.5% of planned sample sites successfully analyzed"
    },
    {
      "@type": "dqv:QualityMeasurement",
      "dqv:isMeasurementOf": "Analytical precision (2-sigma RSD on NIST SRM 2711a replicates)",
      "dqv:value": {
        "@type": "schema:DefinedTerm",
        "schema:name": "High-",
        "schema:inDefinedTermSet": "https://example.org/quality-levels/",
        "schema:termCode": "HIGH"
      }
    }
  ],
  "schema:subjectOf": {
    "@type": [
      "schema:Dataset"
    ],
    "schema:additionalType": [
      "dcat:CatalogRecord"
    ],
    "@id": "ex:metadata-record-001",
    "schema:about": {
      "@id": "ex:complete-dataset-001"
    },
    "dcterms:conformsTo": [
      {
        "@id": "https://w3id.org/cdif/bbr/metadata/profiles/cdifProfiles/CDIFcomplete"
      }
    ],
    "schema:maintainer": {
      "@id": "https://orcid.org/0000-0001-2345-6789",
      "@type": "schema:Person",
      "schema:name": "Smith, Jane"
    },
    "schema:sdDatePublished": "2026-02-19",
    "schema:includedInDataCatalog": {
      "@id": "ex:ieda-catalog",
      "@type": "schema:DataCatalog",
      "schema:name": "IEDA Data Catalog",
      "schema:url": "https://www.earthchem.org/"
    }
  }
}
```

#### ttl
```ttl
@prefix cdi: <http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/> .
@prefix csvw: <http://www.w3.org/ns/csvw#> .
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix dqv: <http://www.w3.org/ns/dqv#> .
@prefix ex: <https://example.org/> .
@prefix geosparql: <http://www.opengis.net/ont/geosparql#> .
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix schema1: <http://schema.org/> .
@prefix sf: <http://www.opengis.net/ont/sf#> .
@prefix spdx: <http://spdx.org/rdf/terms#> .
@prefix time: <http://www.w3.org/2006/time#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<file:///github/workspace/#part-measurements-csv> a cdi:TabularTextDataSet,
        schema1:MediaObject ;
    cdi:hasPhysicalMapping [ cdi:format "decimal" ;
            cdi:formats_InstanceVariable ex:var-concentration ;
            cdi:index 1 ;
            cdi:isRequired true ;
            cdi:nullSequence "NA" ;
            cdi:physicalDataType "float64" ],
        [ cdi:format "decimal" ;
            cdi:formats_InstanceVariable ex:var-uncertainty ;
            cdi:index 2 ;
            cdi:isRequired false ;
            cdi:nullSequence "NA" ;
            cdi:physicalDataType "float64" ],
        [ cdi:format "string" ;
            cdi:formats_InstanceVariable ex:var-sampleID ;
            cdi:index 0 ;
            cdi:isRequired true ;
            cdi:physicalDataType "string" ] ;
    cdi:isDelimited true ;
    schema1:description "Measurement data with column structure described via CSVW and physical mappings." ;
    schema1:encodingFormat "text/csv" ;
    schema1:name "geochem-measurements.csv" ;
    schema1:size [ a schema1:QuantitativeValue ;
            schema1:unitText "byte" ;
            schema1:value 6249 ] ;
    csvw:delimiter "," ;
    csvw:header true ;
    csvw:headerRowCount 1 .

<file:///github/workspace/#part-metadata-yaml> a schema1:MediaObject ;
    schema1:about <file:///github/workspace/#part-results-csv> ;
    schema1:description "Metadata sidecar for the results CSV file." ;
    schema1:encodingFormat "application/yaml" ;
    schema1:name "geochem-detailed-metadata.yaml" ;
    schema1:size [ a schema1:QuantitativeValue ;
            schema1:unitText "byte" ;
            schema1:value 2281 ] .

<file:///github/workspace/#part-method-pdf> a schema1:MediaObject ;
    schema1:description "Method description document for the analysis." ;
    schema1:encodingFormat "application/pdf" ;
    schema1:name "analysis-method.pdf" ;
    schema1:size [ a schema1:QuantitativeValue ;
            schema1:unitText "byte" ;
            schema1:value 56062 ] .

<file:///github/workspace/#part-spectra-nc> a cdi:StructuredDataSet,
        schema1:MediaObject ;
    cdi:hasPhysicalMapping [ cdi:format "decimal" ;
            cdi:formats_InstanceVariable ex:var-wavelength ;
            cdi:index 0 ;
            cdi:isRequired true ;
            cdi:locator "/spectra/wavelength" ;
            cdi:physicalDataType "float32" ],
        [ cdi:format "decimal" ;
            cdi:formats_InstanceVariable ex:var-intensity ;
            cdi:index 1 ;
            cdi:isRequired true ;
            cdi:locator "/spectra/intensity" ;
            cdi:physicalDataType "float32" ] ;
    schema1:description "Spectral data cube with wavelength and intensity dimensions." ;
    schema1:encodingFormat "application/x-netcdf" ;
    schema1:name "spectra-cube.nc" ;
    schema1:size [ a schema1:QuantitativeValue ;
            schema1:unitText "byte" ;
            schema1:value 13743003 ] .

ex:activity-geochem-analysis a schema1:Action,
        prov:Activity ;
    schema1:actionProcess [ a schema1:HowTo ;
            schema1:description "Combined XRF screening and ICP-MS confirmatory analysis for major and trace elements in soils." ;
            schema1:name "EPA 6200 / ICP-MS Soil Geochemistry Protocol" ;
            schema1:step [ a schema1:HowToStep ;
                    schema1:description "Analyze digested solutions by ICP-MS using external calibration with NIST SRM 2711a (Montana II Soil)." ;
                    schema1:name "ICP-MS measurement and calibration" ;
                    schema1:position 2 ;
                    schema1:url "https://example.org/protocols/icpms-measurement" ],
                [ a schema1:HowToStep ;
                    schema1:description "Homogenize dried samples, split 0.5 g aliquots, digest with HNO3-HCl-HF mixture at 190 C for 20 min in a microwave system." ;
                    schema1:name "Sample preparation and acid digestion" ;
                    schema1:position 1 ;
                    schema1:url "https://example.org/protocols/digestion-procedure" ] ] ;
    schema1:actionStatus "schema:CompletedActionStatus" ;
    schema1:additionalProperty [ a schema1:PropertyValue ;
            schema1:name "Analysis Batch Identifier" ;
            schema1:propertyID "batchID" ;
            schema1:value "GB-2025-BATCH-03" ] ;
    schema1:agent <https://orcid.org/0000-0001-2345-6789> ;
    schema1:description "Major and trace element analysis of soil samples from Great Basin transect sites using ICP-MS with EPA Method 6200 protocols." ;
    schema1:endTime "2025-09-30T17:00:00Z" ;
    schema1:error "" ;
    schema1:identifier [ a schema1:PropertyValue ;
            schema1:propertyID "https://example.org/activities" ;
            schema1:url "https://example.org/activities/GEOCHEM-GB-2025-001" ;
            schema1:value "GEOCHEM-GB-2025-001" ] ;
    schema1:location [ a schema1:Place ;
            schema1:address "University of Nevada, Reno, 1664 N. Virginia Street, Reno, NV 89557" ;
            schema1:name "Nevada Bureau of Mines and Geology Analytical Lab" ;
            schema1:url "https://www.unr.edu/nbmg" ] ;
    schema1:name "Soil Geochemistry Analysis - Great Basin Transect 2025" ;
    schema1:object "Dried and sieved soil samples (<2 mm fraction) from Great Basin transect" ;
    schema1:participant [ a schema1:Role ;
            schema1:contributor <https://orcid.org/0000-0003-5555-7777> ;
            schema1:roleName "Lab Technician" ] ;
    schema1:result ex:complete-dataset-001 ;
    schema1:startTime "2025-07-15T08:00:00Z" ;
    prov:used [ schema1:instrument [ a schema1:DefinedTerm,
                        schema1:Thing ;
                    schema1:additionalProperty [ a schema1:PropertyValue ;
                            schema1:name "Typical Detection Limit" ;
                            schema1:propertyID "detectionLimit" ;
                            schema1:value "0.01 mg/kg for trace elements" ] ;
                    schema1:alternateName "Thermo Fisher iCAP RQ ICP-MS" ;
                    schema1:hasPart [ a schema1:Thing ;
                            schema1:alternateName "CETAC ASX-560" ;
                            schema1:name "Autosampler" ],
                        [ a schema1:Thing ;
                            schema1:alternateName "Peltier-cooled cyclonic" ;
                            schema1:name "Spray chamber" ] ;
                    schema1:inDefinedTermSet "https://vocab.nerc.ac.uk/collection/L05/current/" ;
                    schema1:name "Inductively Coupled Plasma Mass Spectrometry" ;
                    schema1:termCode "ICP-MS" ] ],
        [ a schema1:CreativeWork ;
            schema1:name "EPA Method 6200 - XRF Analysis of Soils" ;
            schema1:url "https://www.epa.gov/hw-sw846/sw-846-test-method-6200-field-portable-x-ray-fluorescence-spectrometry-determination" ],
        "Soil core samples collected June 2025, sites GB-001 through GB-045, dried and sieved to <2 mm fraction",
        "https://vocab.nerc.ac.uk/collection/L05/current/LAB02" .

ex:ieda-catalog a schema1:DataCatalog ;
    schema1:name "IEDA Data Catalog" ;
    schema1:url "https://www.earthchem.org/" .

ex:ieda-publisher a schema1:Organization ;
    schema1:alternateName "Interdisciplinary Earth Data Alliance" ;
    schema1:description "An NSF-supported data facility for geochemistry and related disciplines" ;
    schema1:identifier [ a schema1:PropertyValue ;
            schema1:propertyID "https://registry.identifiers.org/registry/ror" ;
            schema1:url "https://ror.org/02fjgr047" ;
            schema1:value "02fjgr047" ] ;
    schema1:name "IEDA-" .

ex:metadata-record-001 a schema1:Dataset ;
    dcterms:conformsTo <https://w3id.org/cdif/bbr/metadata/profiles/cdifProfiles/CDIFcomplete> ;
    schema1:about ex:complete-dataset-001 ;
    schema1:additionalType "dcat:CatalogRecord" ;
    schema1:includedInDataCatalog ex:ieda-catalog ;
    schema1:maintainer <https://orcid.org/0000-0001-2345-6789> ;
    schema1:sdDatePublished "2026-02-19" .

<file:///github/workspace/#part-results-csv> a schema1:MediaObject ;
    schema1:description "Detailed geochemistry analysis results in tabular format." ;
    schema1:encodingFormat "text/csv" ;
    schema1:name "geochem-detailed.csv" ;
    schema1:size [ a schema1:QuantitativeValue ;
            schema1:unitText "byte" ;
            schema1:value 10860 ] ;
    spdx:checksum [ a spdx:Checksum ;
            spdx:algorithm "SHA256" ;
            spdx:checksumValue "b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3" ] .

ex:complete-dataset-001 a schema1:Dataset ;
    schema1:additionalType "geochemistry analysis" ;
    schema1:conditionsOfAccess "Open access; citation required" ;
    schema1:contributor [ a schema1:Role ;
            schema1:contributor <https://orcid.org/0000-0003-5555-7777> ;
            schema1:roleName [ a schema1:DefinedTerm ;
                    schema1:inDefinedTermSet "https://credit.niso.org/" ;
                    schema1:name "Data Manager" ;
                    schema1:termCode "data-curation" ] ],
        <https://ror.org/03m2x1q45> ;
    schema1:creator ( <https://orcid.org/0000-0001-2345-6789> ) ;
    schema1:dateModified "2026-02-15" ;
    schema1:datePublished "2026-02-01" ;
    schema1:description "Comprehensive geochemistry dataset demonstrating the CDIF complete profile with single-file downloads, archive distribution with component files, and WebAPI access. Includes tabular CSV results, NetCDF data cubes, and an OGC API Features endpoint." ;
    schema1:distribution [ a schema1:WebAPI ;
            schema1:documentation [ a schema1:CreativeWork ;
                    schema1:name "OpenAPI specification for geochemistry data service" ;
                    schema1:url "https://example.org/api/v1/openapi.json" ] ;
            schema1:potentialAction [ a schema1:Action ;
                    schema1:name "Query geochemistry features" ;
                    schema1:object [ a schema1:DataFeed ;
                            schema1:description "Geochemistry observations collection" ] ;
                    schema1:query-input [ a schema1:PropertyValueSpecification ;
                            schema1:description "Response format: csv or geojson" ;
                            schema1:valueName "format" ;
                            schema1:valuePattern "csv|geojson" ;
                            schema1:valueRequired false ],
                        [ a schema1:PropertyValueSpecification ;
                            schema1:description "Starting index for pagination" ;
                            schema1:valueName "offset" ;
                            schema1:valueRequired false ],
                        [ a schema1:PropertyValueSpecification ;
                            schema1:description "Maximum number of features to return" ;
                            schema1:valueName "limit" ;
                            schema1:valueRequired false ] ;
                    schema1:result [ a schema1:DataDownload ;
                            cdi:hasPhysicalMapping [ cdi:format "decimal" ;
                                    cdi:formats_InstanceVariable ex:var-concentration ;
                                    cdi:index 0 ;
                                    cdi:isRequired true ;
                                    cdi:physicalDataType "float64" ],
                                [ cdi:format "decimal" ;
                                    cdi:formats_InstanceVariable ex:var-uncertainty ;
                                    cdi:index 1 ;
                                    cdi:isRequired false ;
                                    cdi:physicalDataType "float64" ] ;
                            cdi:isDelimited true ;
                            dcterms:conformsTo <http://www.opengis.net/def/nil/OGC/0/missing> ;
                            schema1:contentUrl "https://example.org/api/v1/collections/geochem/items?f=csv" ;
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
                            schema1:urlTemplate "https://example.org/api/v1/collections/geochem/items?f={format}&limit={limit}&offset={offset}" ] ] ;
            schema1:serviceType [ a schema1:DefinedTerm ;
                    schema1:identifier [ a schema1:PropertyValue ;
                            schema1:propertyID "https://www.ogc.org/standards" ;
                            schema1:url "https://www.ogc.org/standard/ogcapi-features/" ;
                            schema1:value "ogcapi-features-1" ] ;
                    schema1:inDefinedTermSet "https://www.ogc.org/standards" ;
                    schema1:name "OGC API - Features" ;
                    schema1:termCode "ogcapi-features" ] ;
            schema1:termsOfService "Open access, no authentication required" ],
        [ a schema1:DataDownload ;
            dcterms:conformsTo <http://www.opengis.net/def/nil/OGC/0/missing> ;
            schema1:contentUrl "https://example.org/data/geochem-package.zip" ;
            schema1:description "Archive containing all data files. Component files are listed as parts and are not individually accessible." ;
            schema1:encodingFormat "application/zip" ;
            schema1:hasPart <file:///github/workspace/#part-measurements-csv>,
                <file:///github/workspace/#part-metadata-yaml>,
                <file:///github/workspace/#part-method-pdf>,
                <file:///github/workspace/#part-results-csv>,
                <file:///github/workspace/#part-spectra-nc> ;
            schema1:name "Complete data package" ;
            spdx:checksum [ a spdx:Checksum ;
                    spdx:algorithm "SHA256" ;
                    spdx:checksumValue "d4e5f6a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4e5" ] ],
        [ a schema1:DataDownload ;
            dcterms:conformsTo <http://www.opengis.net/def/nil/OGC/0/missing> ;
            schema1:contentUrl "https://example.org/data/geochem-summary.csv" ;
            schema1:encodingFormat "text/csv" ;
            schema1:name "Geochemistry summary results" ;
            schema1:provider <https://ror.org/02fjgr047> ;
            spdx:checksum [ a spdx:Checksum ;
                    spdx:algorithm "SHA256" ;
                    spdx:checksumValue "a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4e5f6a1b2" ] ],
        [ a cdi:TabularTextDataSet,
                schema1:DataDownload ;
            cdi:arrayBase 0 ;
            cdi:escapeCharacter "\\" ;
            cdi:hasPhysicalMapping [ cdi:decimalPositions 4 ;
                    cdi:format "decimal" ;
                    cdi:formats_InstanceVariable ex:var-uncertainty ;
                    cdi:index 2 ;
                    cdi:isRequired false ;
                    cdi:length 12 ;
                    cdi:nullSequence "-9999" ;
                    cdi:physicalDataType "float64" ],
                [ cdi:decimalPositions 4 ;
                    cdi:format "decimal" ;
                    cdi:formats_InstanceVariable ex:var-concentration ;
                    cdi:index 1 ;
                    cdi:isRequired true ;
                    cdi:nullSequence "NA" ;
                    cdi:physicalDataType "float64" ],
                [ cdi:defaultValue "UNKNOWN" ;
                    cdi:format "string" ;
                    cdi:formats_InstanceVariable ex:var-sampleID ;
                    cdi:index 0 ;
                    cdi:isRequired true ;
                    cdi:maximumLength 40 ;
                    cdi:minimumLength 3 ;
                    cdi:physicalDataType "string" ] ;
            cdi:headerIsCaseSensitive false ;
            cdi:isDelimited true ;
            cdi:isFixedWidth false ;
            cdi:treatConsecutiveDelimitersAsOne false ;
            dcterms:conformsTo <http://www.opengis.net/def/nil/OGC/0/missing> ;
            schema1:contentUrl "https://example.org/data/geochem-detailed.csv" ;
            schema1:encodingFormat "text/csv" ;
            schema1:name "Detailed geochemistry analysis results" ;
            spdx:checksum [ a spdx:Checksum ;
                    spdx:algorithm "SHA256" ;
                    spdx:checksumValue "b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3" ] ;
            csvw:commentPrefix "#" ;
            csvw:delimiter "," ;
            csvw:header true ;
            csvw:headerRowCount 1 ;
            csvw:lineTerminators "LF" ;
            csvw:quoteChar "\"" ;
            csvw:skipBlankRows false ;
            csvw:skipColumns 0 ;
            csvw:skipInitialSpace true ;
            csvw:skipRows 0 ;
            csvw:tableDirection "Ltr" ;
            csvw:textDirection "Auto" ;
            csvw:trim "true" ],
        [ a cdi:StructuredDataSet,
                schema1:DataDownload ;
            cdi:hasPhysicalMapping [ cdi:format "decimal" ;
                    cdi:formats_InstanceVariable ex:var-intensity ;
                    cdi:index 1 ;
                    cdi:isRequired true ;
                    cdi:locator "/spectra/intensity" ;
                    cdi:physicalDataType "float32" ;
                    cdi:scale 1000 ],
                [ cdi:format "decimal" ;
                    cdi:formats_InstanceVariable ex:var-wavelength ;
                    cdi:index 0 ;
                    cdi:isRequired true ;
                    cdi:locator "/spectra/wavelength" ;
                    cdi:physicalDataType "float32" ] ;
            dcterms:conformsTo <http://www.opengis.net/def/nil/OGC/0/missing> ;
            schema1:contentUrl "https://example.org/data/spectra-cube.nc" ;
            schema1:encodingFormat "application/x-netcdf" ;
            schema1:name "Spectral data cube" ;
            spdx:checksum [ a spdx:Checksum ;
                    spdx:algorithm "SHA256" ;
                    spdx:checksumValue "c3d4e5f6a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4" ] ] ;
    schema1:funding [ a schema1:MonetaryGrant ;
            schema1:funder <https://ror.org/021nxhr62> ;
            schema1:identifier [ a schema1:PropertyValue ;
                    schema1:propertyID "NSF award number" ;
                    schema1:url "https://www.nsf.gov/awardsearch/showAward?AWD_ID=2026932" ;
                    schema1:value "EAR-2026932" ] ;
            schema1:name "Geochemistry Data Infrastructure" ] ;
    schema1:identifier [ a schema1:PropertyValue ;
            schema1:propertyID "https://registry.identifiers.org/registry/doi" ;
            schema1:url "https://doi.org/10.5880/example.complete.001" ;
            schema1:value "10.5880/example.complete.001" ] ;
    schema1:inLanguage "en" ;
    schema1:keywords [ a schema1:DefinedTerm ;
            schema1:identifier [ a schema1:PropertyValue ;
                    schema1:propertyID "https://vocabularyserver.com/keyword" ;
                    schema1:url "https://vocabularyserver.com/keyword/spectral-001" ;
                    schema1:value "spectral-001" ] ;
            schema1:inDefinedTermSet "https://vocabularyserver.com/keyword" ;
            schema1:name "spectral analysis" ;
            schema1:termCode "SPECTRAL" ],
        [ a schema1:DefinedTerm ;
            schema1:identifier [ a schema1:PropertyValue ;
                    schema1:propertyID "https://vocabularyserver.com/keyword" ;
                    schema1:url "https://vocabularyserver.com/keyword/geochem-001" ;
                    schema1:value "geochem-001" ] ;
            schema1:inDefinedTermSet "https://vocabularyserver.com/keyword" ;
            schema1:name "geochemistry" ;
            schema1:termCode "GEOCHEM" ] ;
    schema1:license "https://creativecommons.org/licenses/by/4.0/" ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:identifier [ a schema1:PropertyValue ;
                    schema1:propertyID "https://vocab.nerc.ac.uk/collection/L05/current/" ;
                    schema1:url "https://vocab.nerc.ac.uk/collection/L05/current/LAB21/" ;
                    schema1:value "LAB21" ] ;
            schema1:inDefinedTermSet "https://vocab.nerc.ac.uk/collection/L05/current/" ;
            schema1:name "Inductively Coupled Plasma Mass Spectrometry" ;
            schema1:termCode "ICP-MS" ] ;
    schema1:name "Multi-technique geochemistry dataset with archive and API access" ;
    schema1:provider <https://ror.org/02fjgr047> ;
    schema1:publisher ex:ieda-publisher ;
    schema1:publishingPrinciples [ a schema1:CreativeWork ;
            schema1:description "Describes data curation, versioning, and long-term preservation policies for IEDA-hosted datasets" ;
            schema1:name "IEDA Data Management Plan" ;
            schema1:url "https://www.iedadata.org/help/data-publication/" ] ;
    schema1:relatedLink [ a schema1:LinkRole ;
            schema1:linkRelationship [ a schema1:DefinedTerm ;
                    schema1:inDefinedTermSet "https://www.iana.org/assignments/link-relations/" ;
                    schema1:name "related dataset" ;
                    schema1:termCode "related" ] ] ;
    schema1:sameAs [ a schema1:PropertyValue ;
            schema1:value "urn:example:geochem:complete-001" ] ;
    schema1:spatialCoverage [ a schema1:Place ;
            schema1:geo [ a schema1:GeoShape ;
                    schema1:box "36.0 -120.0 42.0 -114.0" ] ;
            schema1:name [ a schema1:DefinedTerm ;
                    schema1:identifier [ a schema1:PropertyValue ;
                            schema1:propertyID "https://www.geonames.org/" ;
                            schema1:url "https://www.geonames.org/5509151" ;
                            schema1:value "5509151" ] ;
                    schema1:inDefinedTermSet "https://www.geonames.org/" ;
                    schema1:name "Great Basin physiographic province" ;
                    schema1:termCode "5509151" ],
                "Great Basin" ;
            geosparql:hasGeometry [ a sf:Polygon ;
                    geosparql:asWKT "POLYGON((-120.0 36.0, -114.0 36.0, -114.0 42.0, -120.0 42.0, -120.0 36.0))"^^geosparql:wktLiteral ;
                    geosparql:crs <http://www.opengis.net/def/crs/OGC/1.3/CRS84> ] ] ;
    schema1:subjectOf ex:metadata-record-001 ;
    schema1:temporalCoverage [ a time:ProperInterval ;
            schema1:description "Field sampling and laboratory analysis period" ;
            time:hasBeginning [ a time:Instant ;
                    time:inXSDDate "2025-06-01" ] ;
            time:hasEnd [ a time:Instant ;
                    time:inXSDDate "2025-09-30" ] ],
        "2025-06-01/2025-09-30" ;
    schema1:url "https://example.org/datasets/complete-001" ;
    schema1:variableMeasured ex:var-concentration,
        ex:var-intensity,
        ex:var-sampleID,
        ex:var-uncertainty,
        ex:var-wavelength ;
    schema1:version "1.0" ;
    dqv:hasQualityMeasurement [ a dqv:QualityMeasurement ;
            dqv:isMeasurementOf "Analytical precision (2-sigma RSD on NIST SRM 2711a replicates)" ;
            dqv:value [ a schema1:DefinedTerm ;
                    schema1:inDefinedTermSet "https://example.org/quality-levels/" ;
                    schema1:name "High-" ;
                    schema1:termCode "HIGH" ] ],
        [ a dqv:QualityMeasurement ;
            dqv:isMeasurementOf [ a schema1:DefinedTerm ;
                    schema1:inDefinedTermSet "https://www.w3.org/TR/vocab-dqv/" ;
                    schema1:name "Completeness" ;
                    schema1:termCode "completeness" ] ;
            dqv:value "98.5% of planned sample sites successfully analyzed" ] ;
    prov:wasDerivedFrom [ a schema1:CreativeWork ;
            schema1:description "Prior regional geochemical survey used for site selection and comparative analysis" ;
            schema1:name "USGS Great Basin Geochemical Survey (2020)" ;
            schema1:url "https://pubs.usgs.gov/of/2020/example-great-basin" ],
        <https://doi.org/10.5880/example.field.001>,
        <https://example.org/fieldwork/gb-transect-2025/raw-samples> ;
    prov:wasGeneratedBy ex:activity-geochem-analysis .

<https://orcid.org/0000-0003-5555-7777> a schema1:Person ;
    schema1:contactPoint [ a schema1:ContactPoint ;
            schema1:email "rlee@example.org" ] ;
    schema1:name "Lee, Robert" .

<https://ror.org/02fjgr047> a schema1:Organization ;
    schema1:name "IEDA-" ;
    schema1:url "https://www.earthchem.org/" .

<https://ror.org/03m2x1q45> a schema1:Organization ;
    schema1:name "University of Arizona" .

ex:var-intensity a cdi:InstanceVariable,
        schema1:PropertyValue ;
    schema1:description "Measured spectral intensity" ;
    schema1:name "Spectral intensity" ;
    schema1:propertyID "urn:example:property:intensity" ;
    schema1:unitText "counts" .

ex:var-sampleID a cdi:InstanceVariable,
        schema1:PropertyValue ;
    schema1:description "Unique identifier for each sample" ;
    schema1:name "Sample identifier" ;
    schema1:propertyID "urn:example:property:sampleID" .

ex:var-wavelength a cdi:InstanceVariable,
        schema1:PropertyValue ;
    schema1:description "Spectral wavelength" ;
    schema1:maxValue 2500 ;
    schema1:minValue 200 ;
    schema1:name "Wavelength" ;
    schema1:propertyID "urn:example:property:wavelength" ;
    schema1:unitText "nm" .

<https://orcid.org/0000-0001-2345-6789> a schema1:Person ;
    schema1:affiliation <https://ror.org/03m2x1q45> ;
    schema1:alternateName "J. Smith" ;
    schema1:contactPoint [ a schema1:ContactPoint ;
            schema1:email "jsmith@arizona.edu" ] ;
    schema1:description "Geochemistry researcher specializing in trace element analysis and environmental mineralogy" ;
    schema1:identifier [ a schema1:PropertyValue ;
            schema1:propertyID "https://orcid.org" ;
            schema1:url "https://orcid.org/0000-0001-2345-6789" ;
            schema1:value "0000-0001-2345-6789" ] ;
    schema1:name "Smith, Jane" .

ex:var-concentration a cdi:InstanceVariable,
        schema1:PropertyValue ;
    schema1:alternateName "concentration_ppm",
        "element_conc" ;
    schema1:description "Measured element concentration in parts per million" ;
    schema1:maxValue 5000 ;
    schema1:measurementTechnique "ICP-MS" ;
    schema1:minValue 1e-02 ;
    schema1:name "Element concentration" ;
    schema1:propertyID "urn:example:property:concentration" ;
    schema1:unitCode "59" ;
    schema1:unitText "ppm" ;
    schema1:url "https://example.org/docs/variables/concentration" .

ex:var-uncertainty a cdi:InstanceVariable,
        schema1:PropertyValue ;
    schema1:description "2-sigma uncertainty on concentration measurement" ;
    schema1:name "Measurement uncertainty" ;
    schema1:propertyID "urn:example:property:uncertainty" ;
    schema1:unitCode "59" ;
    schema1:unitText "ppm" .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
type: object
title: CDIF complete metadata schema
description: JSON schema for JSON-LD documents that describe science datasets for
  the CDIF complete profile, combining discovery metadata with data description, distribution
  (DataDownload, archive, WebAPI), and provenance extensions. Composes cdifMandatory,
  cdifOptional, cdifDataDescription, cdifArchiveDistribution, and cdifProvenance building
  blocks.
allOf:
- $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifProperties/cdifMandatory/schema.yaml
- $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifProperties/cdifOptional/schema.yaml
- $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifProperties/cdifDataDescription/schema.yaml
- $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifProperties/cdifArchiveDistribution/schema.yaml
- $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifProperties/cdifProvenance/schema.yaml
x-jsonld-prefixes:
  schema: http://schema.org/
  cdi: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/
  dcterms: http://purl.org/dc/terms/
  geosparql: http://www.opengis.net/ont/geosparql#
  spdx: http://spdx.org/rdf/terms#
  time: http://www.w3.org/2006/time#
  skos: http://www.w3.org/2004/02/skos/core#
  prov: http://www.w3.org/ns/prov#
  csvw: http://www.w3.org/ns/csvw#

```

Links to the schema:

* YAML version: [schema.yaml](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/profiles/cdifProfiles/CDIFcomplete/schema.json)
* JSON version: [schema.json](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/profiles/cdifProfiles/CDIFcomplete/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "schema": "http://schema.org/",
    "ex": "https://example.org/",
    "xsd": "http://www.w3.org/2001/XMLSchema#",
    "dcterms": "http://purl.org/dc/terms/",
    "dcat": "http://www.w3.org/ns/dcat#",
    "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
    "geosparql": "http://www.opengis.net/ont/geosparql#",
    "spdx": "http://spdx.org/rdf/terms#",
    "time": "http://www.w3.org/2006/time#",
    "skos": "http://www.w3.org/2004/02/skos/core#",
    "prov": "http://www.w3.org/ns/prov#",
    "csvw": "http://www.w3.org/ns/csvw#",
    "xas": "https://xas.org/dictionary/",
    "nxs": "http://purl.org/nexusformat/definitions/",
    "ada": "https://ada.astromat.org/metadata/",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/profiles/cdifProfiles/CDIFcomplete/context.jsonld)

## Sources

* [CDIF book](https://cross-domain-interoperability-framework.github.io/cdifbook/metadata/schemaorgimplementation.html#schema-org-implementation-of-cdif-metadata)
* [schema.org DataDownload](https://schema.org/DataDownload)
* [schema.org WebAPI](https://schema.org/WebAPI)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/Cross-Domain-Interoperability-Framework/metadataBuildingBlocks](https://github.com/Cross-Domain-Interoperability-Framework/metadataBuildingBlocks)
* Path: `_sources/profiles/cdifProfiles/CDIFcomplete`

