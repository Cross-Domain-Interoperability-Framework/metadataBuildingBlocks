
# XAS Core metadata properties (Schema)

`cdif.bbr.metadata.xasProperties.xasCore` *v0.1*

Core XAS metadata extending CDIF mandatory with cdifProvActivity-based provenance. Requires dual @type (Dataset + Product), XAS instrument components (NXsource, NXmonochromator), XDI-conformant distribution, measurement technique DefinedTerms, and element/edge keywords. Defines properties: @type, schema:subjectOf, prov:wasGeneratedBy, schema:distribution, schema:measurementTechnique, schema:keywords. Uses building blocks: cdifCore (cdifProperties), cdifProvActivity (cdifProperties), definedTerm (schemaorgProperties), additionalProperty (schemaorgProperties), dataDownload (schemaorgProperties), xasSample (xasProperties), cdifCatalogRecord (cdifProperties).

[*Status*](http://www.opengis.net/def/status): Under development

## Description

## Required Fields for XAS data

Extends CDIF mandatory metadata with required XAS-specific properties. Same structure as xasOptional but adds `@type` constraints (schema:Dataset + schema:Product) and stricter cardinality requirements on instrument components, measurement techniques, and keywords.

### Key requirements

- **@type** — must include both `schema:Dataset` and `schema:Product`
- **schema:subjectOf** — XAS subject descriptors (element, edge)
- **prov:wasGeneratedBy** — cdifProvActivity activity requiring XAS instruments with NXsource (type, probe) and NXmonochromator (type, d_spacing, reflection) components, plus sample object
- **schema:distribution** — requires at least one DataDownload typed as `cdi:PhysicalDataset` conforming to the XDI specification
- **schema:measurementTechnique** — requires DefinedTerms for XAS (PaNET) and measurement mode (NXxas)
- **schema:keywords** — requires DefinedTerms from both the XDI dictionary (absorption edge) and SWEET ontology (target element)

## Examples

### Example XAS core metadata with required items.
XAS core properties: instrument components, XDI distribution, measurement techniques, keywords.
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "dcterms": "http://purl.org/dc/terms/",
    "dcat": "http://www.w3.org/ns/dcat#",
    "geosparql": "http://www.opengis.net/ont/geosparql#",
    "spdx": "http://spdx.org/rdf/terms#",
    "ex": "https://example.org/",
    "xsd": "http://www.w3.org/2001/XMLSchema#",
    "xas": "https://xas.org/dictionary/",
    "nxs": "http://purl.org/nexusformat/definitions/",
    "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
    "prov": "http://www.w3.org/ns/prov#"
  },
  "@id": "ex:xas-dataset-001",
  "@type": [
    "schema:Dataset",
    "schema:Product"
  ],
  "schema:name": "Se K-edge XANES of Na2SeO4 reference compound",
  "schema:identifier": {
    "@type": [
      "schema:PropertyValue"
    ],
    "schema:propertyID": "https://doi.org",
    "schema:value": "10.12345/xas.2024.001",
    "schema:url": "http://example.com/resource?foo=bar#fragment"
  },
  "schema:dateModified": "2025-06-15",
  "schema:conditionsOfAccess": [
    "Public access, no restrictions"
  ],
  "schema:license": [
    "https://creativecommons.org/licenses/by/4.0/"
  ],
  "schema:url": "http://example.com/resource?foo=bar#fragment",
  "schema:distribution": [
    {
      "@id": "lMtIx",
      "@type": [
        "schema:DataDownload",
        "cdi:PhysicalDataset"
      ],
      "schema:name": "XDI data file",
      "schema:contentUrl": "http://example.com/resource/35uj46j",
      "schema:encodingFormat": [
        "application/x-xdi"
      ],
      "dcterms:conformsTo": [
        {
          "@id": "https://github.com/XraySpectroscopy/XAS-Data-Interchange/blob/master/specification/spec.md"
        }
      ],
      "spdx:checksum": {
        "@type": [
          "spdx:Checksum"
        ],
        "spdx:algorithm": "SHA-256",
        "spdx:checksumValue": "a1b2c3d4e5f6..."
      },
      "schema:provider": [
        {
          "@id": "plTqxpHjBTESztfaDyI"
        }
      ]
    },
    {
      "@id": "RNdlTIf",
      "@type": [
        "schema:DataDownload"
      ],
      "schema:name": "Processed spectrum CSV",
      "schema:contentUrl": "http://example.com/resource/34h5ykl",
      "schema:encodingFormat": [
        "text/csv",
        "application/zip"
      ],
      "spdx:checksum": {
        "@type": [
          "spdx:Checksum"
        ],
        "spdx:algorithm": "MD5",
        "spdx:checksumValue": "d41d8cd98f00b204e9800998ecf8427e"
      },
      "schema:provider": [
        {
          "@id": "EwHwOWWPjkVxr"
        }
      ],
      "dcterms:conformsTo": [
        {
          "@id": "http://www.opengis.net/def/nil/OGC/0/missing"
        }
      ]
    }
  ],
  "schema:subjectOf": {
    "@type": [
      "schema:Dataset"
    ],
    "schema:additionalType": [
      "dcat:CatalogRecord"
    ],
    "@id": "urn:uuid:xas-required-catalog-record",
    "schema:about": {
      "@id": "ex:xas-dataset-001"
    },
    "dcterms:conformsTo": [
      {
        "@id": "https://w3id.org/cdif/core/1.0/"
      },
      {
        "@id": "https://w3id.org/cdif/discovery/1.0/"
      },
      {
        "@id": "https://w3id.org/cdif/xasCore/1.0/"
      },
      {
        "@id": "https://w3id.org/cdif/bbr/metadata/xasProperties/xasCore"
      },
      {
        "@id": "https://w3id.org/cdif/bbr/metadata/profiles/cdifProfiles/CDIFxas"
      }
    ],
    "schema:maintainer": {
      "@id": "nKwywfsuBh",
      "@type": [
        "schema:Person"
      ],
      "schema:name": "Cataloger, Example Data",
      "schema:contactPoint": {
        "@type": [
          "schema:ContactPoint"
        ],
        "schema:email": "cataloger@example.org"
      }
    },
    "schema:sdDatePublished": "2025-08-15T06:45:40Z",
    "schema:includedInDataCatalog": {
      "@id": "nbUunSyw",
      "@type": [
        "schema:DataCatalog"
      ],
      "schema:name": "XAS Data Library",
      "schema:url": "http://example.com/resource?foo=bar#fragment"
    }
  },
  "prov:wasGeneratedBy": [
    {
      "prov:used": [
        {
          "schema:instrument": {
            "@type": [
              "schema:Thing",
              "schema:Product"
            ],
            "schema:name": "APS Sector 20-BM beamline instrument",
            "schema:category": [
              {
                "@type": [
                  "schema:DefinedTerm"
                ],
                "schema:name": "X-ray absorption spectroscopy beamline",
                "schema:termCode": "XAS-beamline"
              }
            ],
            "schema:hasPart": [
              {
                "@type": [
                  "schema:Thing",
                  "schema:Product"
                ],
                "schema:additionalType": "nxs:BaseClass/NXsource",
                "schema:name": "APS bending magnet source",
                "schema:additionalProperty": [
                  {
                    "@type": [
                      "schema:PropertyValue"
                    ],
                    "schema:propertyID": [
                      "nxs:Field/NXsource/type"
                    ],
                    "schema:name": "x-ray source",
                    "schema:value": "Synchrotron X-ray Source"
                  },
                  {
                    "@type": [
                      "schema:PropertyValue"
                    ],
                    "schema:propertyID": [
                      "nxs:Field/NXsource/probe"
                    ],
                    "schema:name": "Probe",
                    "schema:value": "x-ray"
                  }
                ]
              },
              {
                "@type": [
                  "schema:Thing",
                  "schema:Product"
                ],
                "schema:additionalType": "nxs:BaseClass/NXmonochromator",
                "schema:name": "Si 111",
                "schema:additionalProperty": [
                  {
                    "@type": [
                      "schema:PropertyValue"
                    ],
                    "schema:propertyID": [
                      "nxs:Field/NXcrystal/d_spacing"
                    ],
                    "schema:name": "d-spacing",
                    "schema:value": "3.13550",
                    "schema:unitText": "Angstrom"
                  },
                  {
                    "@type": [
                      "schema:PropertyValue"
                    ],
                    "schema:propertyID": [
                      "nxs:Field/NXcrystal/type"
                    ],
                    "schema:name": "crystal type",
                    "schema:value": "Si(111)"
                  },
                  {
                    "@type": [
                      "schema:PropertyValue"
                    ],
                    "schema:propertyID": [
                      "nxs:Field/NXcrystal/reflection"
                    ],
                    "schema:name": "reflection plane (hkl)",
                    "schema:value": "1,1,1"
                  }
                ]
              }
            ]
          }
        }
      ],
      "schema:object": {
        "@type": [
          "schema:Product",
          "schema:Thing"
        ],
        "schema:additionalType": [
          "MaterialSample",
          "https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample"
        ],
        "schema:name": "Na2SeO4",
        "schema:identifier": "igsn:10.6620/se-selenate-001",
        "schema:description": "Sodium selenate reference compound, powder",
        "schema:additionalProperty": [
          {
            "@type": [
              "schema:PropertyValue"
            ],
            "schema:propertyID": [
              "https://example.org/vocab/sample-prep"
            ],
            "schema:name": "sample preparation method",
            "schema:value": "powder on tape, 6 layers"
          },
          {
            "@type": [
              "schema:PropertyValue"
            ],
            "schema:propertyID": [
              "xas:stoichiometry"
            ],
            "schema:name": "Stoichiometry",
            "schema:value": "Na2SeO4"
          }
        ]
      }
    }
  ],
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:name": "X-Ray Absorption Spectroscopy",
      "schema:termCode": "XAS",
      "schema:identifier": "http://purl.org/pan-science/PaNET/PaNET01196",
      "schema:inDefinedTermSet": "http://purl.org/pan-science/PaNET/PaNET.owl"
    },
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:name": "Transmission",
      "schema:identifier": "http://purl.org/pan-science/PaNET/PaNET01188",
      "schema:inDefinedTermSet": "nxs:Field/NXxas/ENTRY/DATA/mode"
    }
  ],
  "schema:keywords": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:name": "K-edge",
      "schema:identifier": "https://github.com/XraySpectroscopy/XAS-Data-Interchange/blob/master/specification/dictionary.md#K",
      "schema:termCode": "K",
      "schema:inDefinedTermSet": "https://github.com/XraySpectroscopy/XAS-Data-Interchange/blob/master/specification/dictionary.md"
    },
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:name": "Selenium",
      "schema:identifier": "http://sweetontology.net/matrElement/Selenium",
      "schema:termCode": "Se",
      "schema:inDefinedTermSet": "http://sweetontology.net/matrElement"
    }
  ]
}

```

#### jsonld
```jsonld
{
  "@context": [
    {
      "schema": "http://schema.org/",
      "dcterms": "http://purl.org/dc/terms/",
      "dcat": "http://www.w3.org/ns/dcat#",
      "prov": "http://www.w3.org/ns/prov#",
      "nxs": "http://purl.org/nexusformat/definitions/",
      "xas": "https://xas.org/dictionary/"
    },
    "https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/xasProperties/xasCore/context.jsonld",
    {
      "schema": "http://schema.org/",
      "dcterms": "http://purl.org/dc/terms/",
      "dcat": "http://www.w3.org/ns/dcat#",
      "geosparql": "http://www.opengis.net/ont/geosparql#",
      "spdx": "http://spdx.org/rdf/terms#",
      "ex": "https://example.org/",
      "xsd": "http://www.w3.org/2001/XMLSchema#",
      "xas": "https://xas.org/dictionary/",
      "nxs": "http://purl.org/nexusformat/definitions/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:xas-dataset-001",
  "@type": [
    "schema:Dataset",
    "schema:Product"
  ],
  "schema:name": "Se K-edge XANES of Na2SeO4 reference compound",
  "schema:identifier": {
    "@type": [
      "schema:PropertyValue"
    ],
    "schema:propertyID": "https://doi.org",
    "schema:value": "10.12345/xas.2024.001",
    "schema:url": "http://example.com/resource?foo=bar#fragment"
  },
  "schema:dateModified": "2025-06-15",
  "schema:conditionsOfAccess": [
    "Public access, no restrictions"
  ],
  "schema:license": [
    "https://creativecommons.org/licenses/by/4.0/"
  ],
  "schema:url": "http://example.com/resource?foo=bar#fragment",
  "schema:distribution": [
    {
      "@id": "lMtIx",
      "@type": [
        "schema:DataDownload",
        "cdi:PhysicalDataset"
      ],
      "schema:name": "XDI data file",
      "schema:contentUrl": "http://example.com/resource/35uj46j",
      "schema:encodingFormat": [
        "application/x-xdi"
      ],
      "dcterms:conformsTo": [
        {
          "@id": "https://github.com/XraySpectroscopy/XAS-Data-Interchange/blob/master/specification/spec.md"
        }
      ],
      "spdx:checksum": {
        "@type": [
          "spdx:Checksum"
        ],
        "spdx:algorithm": "SHA-256",
        "spdx:checksumValue": "a1b2c3d4e5f6..."
      },
      "schema:provider": [
        {
          "@id": "plTqxpHjBTESztfaDyI"
        }
      ]
    },
    {
      "@id": "RNdlTIf",
      "@type": [
        "schema:DataDownload"
      ],
      "schema:name": "Processed spectrum CSV",
      "schema:contentUrl": "http://example.com/resource/34h5ykl",
      "schema:encodingFormat": [
        "text/csv",
        "application/zip"
      ],
      "spdx:checksum": {
        "@type": [
          "spdx:Checksum"
        ],
        "spdx:algorithm": "MD5",
        "spdx:checksumValue": "d41d8cd98f00b204e9800998ecf8427e"
      },
      "schema:provider": [
        {
          "@id": "EwHwOWWPjkVxr"
        }
      ],
      "dcterms:conformsTo": [
        {
          "@id": "http://www.opengis.net/def/nil/OGC/0/missing"
        }
      ]
    }
  ],
  "schema:subjectOf": {
    "@type": [
      "schema:Dataset"
    ],
    "schema:additionalType": [
      "dcat:CatalogRecord"
    ],
    "@id": "urn:uuid:xas-required-catalog-record",
    "schema:about": {
      "@id": "ex:xas-dataset-001"
    },
    "dcterms:conformsTo": [
      {
        "@id": "https://w3id.org/cdif/core/1.0/"
      },
      {
        "@id": "https://w3id.org/cdif/discovery/1.0/"
      },
      {
        "@id": "https://w3id.org/cdif/xasCore/1.0/"
      },
      {
        "@id": "https://w3id.org/cdif/bbr/metadata/xasProperties/xasCore"
      },
      {
        "@id": "https://w3id.org/cdif/bbr/metadata/profiles/cdifProfiles/CDIFxas"
      }
    ],
    "schema:maintainer": {
      "@id": "nKwywfsuBh",
      "@type": [
        "schema:Person"
      ],
      "schema:name": "Cataloger, Example Data",
      "schema:contactPoint": {
        "@type": [
          "schema:ContactPoint"
        ],
        "schema:email": "cataloger@example.org"
      }
    },
    "schema:sdDatePublished": "2025-08-15T06:45:40Z",
    "schema:includedInDataCatalog": {
      "@id": "nbUunSyw",
      "@type": [
        "schema:DataCatalog"
      ],
      "schema:name": "XAS Data Library",
      "schema:url": "http://example.com/resource?foo=bar#fragment"
    }
  },
  "prov:wasGeneratedBy": [
    {
      "prov:used": [
        {
          "schema:instrument": {
            "@type": [
              "schema:Thing",
              "schema:Product"
            ],
            "schema:name": "APS Sector 20-BM beamline instrument",
            "schema:category": [
              {
                "@type": [
                  "schema:DefinedTerm"
                ],
                "schema:name": "X-ray absorption spectroscopy beamline",
                "schema:termCode": "XAS-beamline"
              }
            ],
            "schema:hasPart": [
              {
                "@type": [
                  "schema:Thing",
                  "schema:Product"
                ],
                "schema:additionalType": "nxs:BaseClass/NXsource",
                "schema:name": "APS bending magnet source",
                "schema:additionalProperty": [
                  {
                    "@type": [
                      "schema:PropertyValue"
                    ],
                    "schema:propertyID": [
                      "nxs:Field/NXsource/type"
                    ],
                    "schema:name": "x-ray source",
                    "schema:value": "Synchrotron X-ray Source"
                  },
                  {
                    "@type": [
                      "schema:PropertyValue"
                    ],
                    "schema:propertyID": [
                      "nxs:Field/NXsource/probe"
                    ],
                    "schema:name": "Probe",
                    "schema:value": "x-ray"
                  }
                ]
              },
              {
                "@type": [
                  "schema:Thing",
                  "schema:Product"
                ],
                "schema:additionalType": "nxs:BaseClass/NXmonochromator",
                "schema:name": "Si 111",
                "schema:additionalProperty": [
                  {
                    "@type": [
                      "schema:PropertyValue"
                    ],
                    "schema:propertyID": [
                      "nxs:Field/NXcrystal/d_spacing"
                    ],
                    "schema:name": "d-spacing",
                    "schema:value": "3.13550",
                    "schema:unitText": "Angstrom"
                  },
                  {
                    "@type": [
                      "schema:PropertyValue"
                    ],
                    "schema:propertyID": [
                      "nxs:Field/NXcrystal/type"
                    ],
                    "schema:name": "crystal type",
                    "schema:value": "Si(111)"
                  },
                  {
                    "@type": [
                      "schema:PropertyValue"
                    ],
                    "schema:propertyID": [
                      "nxs:Field/NXcrystal/reflection"
                    ],
                    "schema:name": "reflection plane (hkl)",
                    "schema:value": "1,1,1"
                  }
                ]
              }
            ]
          }
        }
      ],
      "schema:object": {
        "@type": [
          "schema:Product",
          "schema:Thing"
        ],
        "schema:additionalType": [
          "MaterialSample",
          "https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample"
        ],
        "schema:name": "Na2SeO4",
        "schema:identifier": "igsn:10.6620/se-selenate-001",
        "schema:description": "Sodium selenate reference compound, powder",
        "schema:additionalProperty": [
          {
            "@type": [
              "schema:PropertyValue"
            ],
            "schema:propertyID": [
              "https://example.org/vocab/sample-prep"
            ],
            "schema:name": "sample preparation method",
            "schema:value": "powder on tape, 6 layers"
          },
          {
            "@type": [
              "schema:PropertyValue"
            ],
            "schema:propertyID": [
              "xas:stoichiometry"
            ],
            "schema:name": "Stoichiometry",
            "schema:value": "Na2SeO4"
          }
        ]
      }
    }
  ],
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:name": "X-Ray Absorption Spectroscopy",
      "schema:termCode": "XAS",
      "schema:identifier": "http://purl.org/pan-science/PaNET/PaNET01196",
      "schema:inDefinedTermSet": "http://purl.org/pan-science/PaNET/PaNET.owl"
    },
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:name": "Transmission",
      "schema:identifier": "http://purl.org/pan-science/PaNET/PaNET01188",
      "schema:inDefinedTermSet": "nxs:Field/NXxas/ENTRY/DATA/mode"
    }
  ],
  "schema:keywords": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:name": "K-edge",
      "schema:identifier": "https://github.com/XraySpectroscopy/XAS-Data-Interchange/blob/master/specification/dictionary.md#K",
      "schema:termCode": "K",
      "schema:inDefinedTermSet": "https://github.com/XraySpectroscopy/XAS-Data-Interchange/blob/master/specification/dictionary.md"
    },
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:name": "Selenium",
      "schema:identifier": "http://sweetontology.net/matrElement/Selenium",
      "schema:termCode": "Se",
      "schema:inDefinedTermSet": "http://sweetontology.net/matrElement"
    }
  ]
}
```

#### ttl
```ttl
@prefix cdi: <http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/> .
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix ex: <https://example.org/> .
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix schema1: <http://schema.org/> .
@prefix spdx: <http://spdx.org/rdf/terms#> .

<file:///github/workspace/RNdlTIf> a schema1:DataDownload ;
    dcterms:conformsTo <http://www.opengis.net/def/nil/OGC/0/missing> ;
    schema1:contentUrl "http://example.com/resource/34h5ykl" ;
    schema1:encodingFormat "application/zip",
        "text/csv" ;
    schema1:name "Processed spectrum CSV" ;
    schema1:provider <file:///github/workspace/EwHwOWWPjkVxr> ;
    spdx:checksum [ a spdx:Checksum ;
            spdx:algorithm "MD5" ;
            spdx:checksumValue "d41d8cd98f00b204e9800998ecf8427e" ] .

<file:///github/workspace/lMtIx> a cdi:PhysicalDataset,
        schema1:DataDownload ;
    dcterms:conformsTo <https://github.com/XraySpectroscopy/XAS-Data-Interchange/blob/master/specification/spec.md> ;
    schema1:contentUrl "http://example.com/resource/35uj46j" ;
    schema1:encodingFormat "application/x-xdi" ;
    schema1:name "XDI data file" ;
    schema1:provider <file:///github/workspace/plTqxpHjBTESztfaDyI> ;
    spdx:checksum [ a spdx:Checksum ;
            spdx:algorithm "SHA-256" ;
            spdx:checksumValue "a1b2c3d4e5f6..." ] .

<file:///github/workspace/nKwywfsuBh> a schema1:Person ;
    schema1:contactPoint [ a schema1:ContactPoint ;
            schema1:email "cataloger@example.org" ] ;
    schema1:name "Cataloger, Example Data" .

<file:///github/workspace/nbUunSyw> a schema1:DataCatalog ;
    schema1:name "XAS Data Library" ;
    schema1:url "http://example.com/resource?foo=bar#fragment" .

ex:xas-dataset-001 a schema1:Dataset,
        schema1:Product ;
    schema1:conditionsOfAccess "Public access, no restrictions" ;
    schema1:dateModified "2025-06-15" ;
    schema1:distribution <file:///github/workspace/RNdlTIf>,
        <file:///github/workspace/lMtIx> ;
    schema1:identifier [ a schema1:PropertyValue ;
            schema1:propertyID "https://doi.org" ;
            schema1:url "http://example.com/resource?foo=bar#fragment" ;
            schema1:value "10.12345/xas.2024.001" ] ;
    schema1:keywords [ a schema1:DefinedTerm ;
            schema1:identifier "http://sweetontology.net/matrElement/Selenium" ;
            schema1:inDefinedTermSet "http://sweetontology.net/matrElement" ;
            schema1:name "Selenium" ;
            schema1:termCode "Se" ],
        [ a schema1:DefinedTerm ;
            schema1:identifier "https://github.com/XraySpectroscopy/XAS-Data-Interchange/blob/master/specification/dictionary.md#K" ;
            schema1:inDefinedTermSet "https://github.com/XraySpectroscopy/XAS-Data-Interchange/blob/master/specification/dictionary.md" ;
            schema1:name "K-edge" ;
            schema1:termCode "K" ] ;
    schema1:license "https://creativecommons.org/licenses/by/4.0/" ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:identifier "http://purl.org/pan-science/PaNET/PaNET01188" ;
            schema1:inDefinedTermSet "nxs:Field/NXxas/ENTRY/DATA/mode" ;
            schema1:name "Transmission" ],
        [ a schema1:DefinedTerm ;
            schema1:identifier "http://purl.org/pan-science/PaNET/PaNET01196" ;
            schema1:inDefinedTermSet "http://purl.org/pan-science/PaNET/PaNET.owl" ;
            schema1:name "X-Ray Absorption Spectroscopy" ;
            schema1:termCode "XAS" ] ;
    schema1:name "Se K-edge XANES of Na2SeO4 reference compound" ;
    schema1:subjectOf <urn:uuid:xas-required-catalog-record> ;
    schema1:url "http://example.com/resource?foo=bar#fragment" ;
    prov:wasGeneratedBy [ schema1:object [ a schema1:Product,
                        schema1:Thing ;
                    schema1:additionalProperty [ a schema1:PropertyValue ;
                            schema1:name "sample preparation method" ;
                            schema1:propertyID "https://example.org/vocab/sample-prep" ;
                            schema1:value "powder on tape, 6 layers" ],
                        [ a schema1:PropertyValue ;
                            schema1:name "Stoichiometry" ;
                            schema1:propertyID "xas:stoichiometry" ;
                            schema1:value "Na2SeO4" ] ;
                    schema1:additionalType "MaterialSample",
                        "https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample" ;
                    schema1:description "Sodium selenate reference compound, powder" ;
                    schema1:identifier "igsn:10.6620/se-selenate-001" ;
                    schema1:name "Na2SeO4" ] ;
            prov:used [ schema1:instrument [ a schema1:Product,
                                schema1:Thing ;
                            schema1:category [ a schema1:DefinedTerm ;
                                    schema1:name "X-ray absorption spectroscopy beamline" ;
                                    schema1:termCode "XAS-beamline" ] ;
                            schema1:hasPart [ a schema1:Product,
                                        schema1:Thing ;
                                    schema1:additionalProperty [ a schema1:PropertyValue ;
                                            schema1:name "x-ray source" ;
                                            schema1:propertyID "nxs:Field/NXsource/type" ;
                                            schema1:value "Synchrotron X-ray Source" ],
                                        [ a schema1:PropertyValue ;
                                            schema1:name "Probe" ;
                                            schema1:propertyID "nxs:Field/NXsource/probe" ;
                                            schema1:value "x-ray" ] ;
                                    schema1:additionalType "nxs:BaseClass/NXsource" ;
                                    schema1:name "APS bending magnet source" ],
                                [ a schema1:Product,
                                        schema1:Thing ;
                                    schema1:additionalProperty [ a schema1:PropertyValue ;
                                            schema1:name "crystal type" ;
                                            schema1:propertyID "nxs:Field/NXcrystal/type" ;
                                            schema1:value "Si(111)" ],
                                        [ a schema1:PropertyValue ;
                                            schema1:name "reflection plane (hkl)" ;
                                            schema1:propertyID "nxs:Field/NXcrystal/reflection" ;
                                            schema1:value "1,1,1" ],
                                        [ a schema1:PropertyValue ;
                                            schema1:name "d-spacing" ;
                                            schema1:propertyID "nxs:Field/NXcrystal/d_spacing" ;
                                            schema1:unitText "Angstrom" ;
                                            schema1:value "3.13550" ] ;
                                    schema1:additionalType "nxs:BaseClass/NXmonochromator" ;
                                    schema1:name "Si 111" ] ;
                            schema1:name "APS Sector 20-BM beamline instrument" ] ] ] .

<urn:uuid:xas-required-catalog-record> a schema1:Dataset ;
    dcterms:conformsTo <https://w3id.org/cdif/bbr/metadata/profiles/cdifProfiles/CDIFxas>,
        <https://w3id.org/cdif/bbr/metadata/xasProperties/xasCore>,
        <https://w3id.org/cdif/core/1.0/>,
        <https://w3id.org/cdif/discovery/1.0/>,
        <https://w3id.org/cdif/xasCore/1.0/> ;
    schema1:about ex:xas-dataset-001 ;
    schema1:additionalType "dcat:CatalogRecord" ;
    schema1:includedInDataCatalog <file:///github/workspace/nbUunSyw> ;
    schema1:maintainer <file:///github/workspace/nKwywfsuBh> ;
    schema1:sdDatePublished "2025-08-15T06:45:40Z" .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
allOf:
- $ref: '#/$defs/CdifMandatory'
- type: object
  properties:
    '@type':
      type: array
      items:
        type: string
        enum:
        - schema:Dataset
        - schema:Product
    schema:subjectOf:
      properties:
        dcterms:conformsTo:
          type: array
          items:
            type: object
            properties:
              '@id':
                type: string
                description: uri for specifications that this metadata record conforms
                  to
          minItems: 1
          contains:
            type: object
            properties:
              '@id':
                const: https://w3id.org/cdif/xasCore/1.0/
    prov:wasGeneratedBy:
      type: array
      items:
        allOf:
        - $ref: '#/$defs/CdifProvActivity'
        - type: object
          properties:
            prov:used:
              type: array
              description: Array of used entities. Must contain an instrument wrapper
                with schema:hasPart sub-components. The x-ray source type and probe,
                and monochromator properties type, d-spacing and reflection plane
                are required.
              contains:
                type: object
                required:
                - schema:instrument
                properties:
                  schema:instrument:
                    type: object
                    properties:
                      schema:hasPart:
                        type: array
                        minItems: 2
                        allOf:
                        - contains:
                            type: object
                            properties:
                              '@type':
                                type: array
                                items:
                                  type: string
                                minItems: 2
                                allOf:
                                - contains:
                                    const: schema:Thing
                                - contains:
                                    const: schema:Product
                              schema:additionalType:
                                const: nxs:BaseClass/NXsource
                              schema:additionalProperty:
                                type: array
                                minItems: 2
                                items:
                                  $ref: '#/$defs/AdditionalProperty'
                                allOf:
                                - contains:
                                    type: object
                                    properties:
                                      schema:propertyID:
                                        type: array
                                        contains:
                                          const: nxs:Field/NXsource/type
                                      schema:value:
                                        type: string
                                    required:
                                    - schema:propertyID
                                    - schema:value
                                - contains:
                                    type: object
                                    properties:
                                      schema:propertyID:
                                        type: array
                                        contains:
                                          const: nxs:Field/NXsource/probe
                                      schema:name:
                                        const: Probe
                                      schema:value:
                                        type: string
                                    required:
                                    - schema:name
                                    - schema:propertyID
                                    - schema:value
                            required:
                            - '@type'
                            - schema:additionalType
                            - schema:additionalProperty
                        - contains:
                            type: object
                            properties:
                              '@type':
                                type: array
                                items:
                                  type: string
                                minItems: 2
                                allOf:
                                - contains:
                                    const: schema:Thing
                                - contains:
                                    const: schema:Product
                              schema:additionalType:
                                const: nxs:BaseClass/NXmonochromator
                              schema:name:
                                type: string
                              schema:additionalProperty:
                                description: Require additional properties for monochromator,
                                  requires d-space, crystal type, reflection plane.
                                type: array
                                minItems: 3
                                items:
                                  $ref: '#/$defs/AdditionalProperty'
                                contains:
                                  type: object
                                  properties:
                                    schema:propertyID:
                                      type: array
                                      contains:
                                        const: nxs:Field/NXcrystal/type
                                    schema:value:
                                      type: string
                                  required:
                                  - schema:value
                                  - schema:propertyID
                                allOf:
                                - contains:
                                    type: object
                                    properties:
                                      schema:propertyID:
                                        type: array
                                        contains:
                                          const: nxs:Field/NXcrystal/d_spacing
                                      schema:value:
                                        type: string
                                      schema:unitText:
                                        type: string
                                    required:
                                    - schema:propertyID
                                    - schema:value
                                    - schema:unitText
                                - contains:
                                    type: object
                                    properties:
                                      schema:propertyID:
                                        type: array
                                        contains:
                                          const: nxs:Field/NXcrystal/reflection
                                      schema:value:
                                        type: string
                                    required:
                                    - schema:value
                                    - schema:propertyID
                            required:
                            - '@type'
                            - schema:additionalType
                            - schema:additionalProperty
                    required:
                    - schema:hasPart
            schema:object:
              $ref: '#/$defs/XasSample'
    schema:distribution:
      type: array
      items:
        $ref: '#/$defs/DataDownload'
      contains:
        type: object
        properties:
          '@type':
            type: array
            items:
              type: string
            minItems: 2
            allOf:
            - contains:
                const: schema:DataDownload
            - contains:
                enum:
                - cdi:PhysicalDataset
                - cdi:TabularTextDataSet
                - cdi:StructuredDataSet
          dcterms:conformsTo:
            type: array
            contains:
              type: object
              properties:
                '@id':
                  const: https://github.com/XraySpectroscopy/XAS-Data-Interchange/blob/master/specification/spec.md
              required:
              - '@id'
        required:
        - '@type'
        - dcterms:conformsTo
    schema:measurementTechnique:
      type: array
      description: 'Require DefinedTerms for both: absorption edge (XDI dict) and
        target element (SWEET).'
      minItems: 2
      items:
        $ref: '#/$defs/DefinedTerm'
      contains:
        type: object
        properties:
          schema:name:
            const: X-Ray Absorption Spectroscopy
          schema:termCode:
            const: XAS
          schema:identifier:
            const: http://purl.org/pan-science/PaNET/PaNET01196
          schema:inDefinedTermSet:
            const: http://purl.org/pan-science/PaNET/PaNET.owl
        required:
        - schema:name
        - schema:termCode
        - schema:identifier
        - schema:inDefinedTermSet
      allOf:
      - contains:
          type: object
          properties:
            schema:name:
              type: string
            schema:inDefinedTermSet:
              const: nxs:Field/NXxas/ENTRY/DATA/mode
          required:
          - schema:name
          - schema:inDefinedTermSet
    schema:keywords:
      type: array
      description: extends base CDIF keyword schema to require defined terms for the
        absorption edge and the target element for the analysis
      minItems: 2
      items:
        type: object
        properties:
          '@type':
            type: array
            items:
              type: string
            contains:
              const: schema:DefinedTerm
            minItems: 1
          schema:name:
            type: string
          schema:identifier:
            type: string
          schema:inDefinedTermSet:
            type: string
            description: need to include this to tag what the keyword is about; we're
              using the keywords as soft-typed properties
        required:
        - '@type'
        - schema:name
        - schema:inDefinedTermSet
        additionalProperties: true
      contains:
        type: object
        properties:
          schema:inDefinedTermSet:
            const: https://github.com/XraySpectroscopy/XAS-Data-Interchange/blob/master/specification/dictionary.md
        required:
        - schema:inDefinedTermSet
      allOf:
      - contains:
          type: object
          properties:
            schema:inDefinedTermSet:
              const: http://sweetontology.net/matrElement
          required:
          - schema:inDefinedTermSet
$defs:
  CdifMandatory:
    $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifProperties/cdifCore/schema.yaml
  CdifProvActivity:
    $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifProperties/cdifProvActivity/schema.yaml
  DefinedTerm:
    $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/definedTerm/schema.yaml
  AdditionalProperty:
    $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/additionalProperty/schema.yaml
  DataDownload:
    $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/dataDownload/schema.yaml
  XasSample:
    $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/xasProperties/xasSample/schema.yaml
x-jsonld-prefixes:
  schema: http://schema.org/

```

Links to the schema:

* YAML version: [schema.yaml](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/xasProperties/xasCore/schema.json)
* JSON version: [schema.json](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/xasProperties/xasCore/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "schema": "http://schema.org/",
    "ex": "https://example.org/",
    "xsd": "http://www.w3.org/2001/XMLSchema#",
    "dcterms": "http://purl.org/dc/terms/",
    "dcat": "http://www.w3.org/ns/dcat#",
    "prov": "http://www.w3.org/ns/prov#",
    "nxs": "http://purl.org/nexusformat/definitions/",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/xasProperties/xasCore/context.jsonld)

## Sources

* [CDIF-4-XAS OSCARS Project](https://doi.org/10.5281/zenodo.17421917)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/Cross-Domain-Interoperability-Framework/metadataBuildingBlocks](https://github.com/Cross-Domain-Interoperability-Framework/metadataBuildingBlocks)
* Path: `_sources/xasProperties/xasCore`

