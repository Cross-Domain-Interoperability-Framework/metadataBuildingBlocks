
# Bioschemas Sample properties (Schema)

`cdif.bbr.metadata.bioschemasProperties.bioschemasSample` *v0.1*

Properties of a biological sample from the Bioschemas Sample draft, in the bios: namespace: anatomical structure and system, sample type, collection method and collector, collection and processing dates, developmental stage, quantity, state, storage temperature, sex and related study fields. Each accepts one value or an array. Used by niaidDataset for NIAID's nde:Sample, which NIAID declares a subclass of the Bioschemas BioSample.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

## Bioschemas Sample properties

Properties of a biological sample from the Bioschemas `Sample` draft, as
published for the Data Discovery Engine in
[BioSchemas/bioschemas-dde](https://github.com/BioSchemas/bioschemas-dde). They
use the `bios:` prefix that `cdifBioschemasProperties` already uses:

```
bios: https://bioschemas.org/
```

A node using them carries `bios:Sample` in its `@type` beside its own type.
NIAID's `nde:Sample` is declared a subclass of the Bioschemas BioSample, which is
why [`niaidDataset`](../../niaidProperties/niaidDataset/) uses this block.

These are Bioschemas **draft** terms, so names and ranges may still change.
NIAID's schema declares the same names with, on comparison, the same
definitions; terms whose definitions differ (`cellType`, `sample`) stay in
NIAID's `nde:` namespace.

| Property | Value |
|---|---|
| `bios:anatomicalStructure`, `bios:anatomicalSystem` | Term or text: the organ or tissue, or the system, the sample came from |
| `bios:associatedPhenotype` | Term or text: characteristics of the sample's source |
| `bios:collectionMethod`, `bios:experimentalPurpose`, `bios:sampleProcess`, `bios:sampleState` | Term or text |
| `bios:collector` | Person or Organization with a `schema:name` |
| `bios:dateCollected`, `bios:dateProcessed` | Date text starting with a four-digit year |
| `bios:developmentalStage` | Term, text or `schema:QuantitativeValue` |
| `bios:environmentalSystem`, `bios:locationOfOrigin`, `bios:sampleType`, `bios:sex`, `bios:project` | Term or text |
| `bios:sampleQuantity`, `bios:sampleStorageTemperature` | `schema:QuantitativeValue` |
| `bios:sampleAvailability` | Boolean, term or text |
| `bios:isControl` | Boolean |
| `bios:studyID`, `bios:studyTitle` | Text |

Every property accepts one value or an array, because framing collapses a
one-element array to its value. A term must name or identify itself
(`schema:name`, `schema:identifier` or `@id`).

The block's `$defs` (`date`, `texts`, `term`, `termsOrText`, `quantity`) are
reused by `niaidDataset`, which also uses `bios:alternateIdentifier` on the
dataset.

## Examples

### A sample described with Bioschemas properties.
A sample from a NIAID Data Discovery Portal record, as harvest_niaid_to_cdif.py
converts it: nde:Sample typed with bios:Sample, and the Bioschemas sample
properties NIAID uses.
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "bios": "https://bioschemas.org/",
    "nde": "https://discovery.biothings.io/ns/nde/"
  },
  "@type": [
    "nde:Sample",
    "bios:Sample"
  ],
  "schema:additionalType": "ExperimentalRunSample",
  "bios:alternateIdentifier": [
    "2444012656863669780-242ac117-0001-012",
    "SRR12018290",
    "2590428091984309780-242ac117-0001-012",
    "2434434879793589780-242ac117-0001-012",
    "SRR12018305",
    "2587979960625589780-242ac117-0001-012",
    "2425243649780149780-242ac117-0001-012",
    "SRR12018282",
    "2578702831266229780-242ac117-0001-012",
    "2429710415767989780-242ac117-0001-012",
    "SRR12664074",
    "2593606367783349780-242ac117-0001-012",
    "2431299553667509780-242ac117-0001-012",
    "SRR12664078",
    "2579218227341749780-242ac117-0001-012",
    "2432029698107829780-242ac117-0001-012",
    "SRR12018289",
    "2576984844347829780-242ac117-0001-012",
    "2438686897416629780-242ac117-0001-012",
    "SRR12664076",
    "2576898945001909780-242ac117-0001-012",
    "2434348980447669780-242ac117-0001-012",
    "SRR12018283",
    "2583899741694389780-242ac117-0001-012",
    "2434520779139509780-242ac117-0001-012",
    "SRR12018284",
    "2593090971707829780-242ac117-0001-012",
    "2429452717730229780-242ac117-0001-012",
    "SRR12018287",
    "2582654201178549780-242ac117-0001-012",
    "2434950275869109780-242ac117-0001-012",
    "SRR12018303",
    "2582611251505589780-242ac117-0001-012",
    "2423783360899509780-242ac117-0001-012",
    "SRR12018288",
    "2590170393946549780-242ac117-0001-012",
    "2434005383063989780-242ac117-0001-012",
    "SRR12018286",
    "2584629886134709780-242ac117-0001-012",
    "2432201496799669780-242ac117-0001-012",
    "SRR12018310",
    "2579347076360629780-242ac117-0001-012",
    "2429323868711349780-242ac117-0001-012",
    "SRR12018306",
    "2578616931920309780-242ac117-0001-012",
    "2429409768057269780-242ac117-0001-012",
    "SRR12018304",
    "2593606363488382484-242ac117-0001-012",
    "2434864376523189780-242ac117-0001-012",
    "SRR12018281",
    "2585746577631669780-242ac117-0001-012",
    "2434907326196149780-242ac117-0001-012",
    "SRR12018285",
    "2573763618875829780-242ac117-0001-012",
    "2431857899415989780-242ac117-0001-012",
    "SRR12664079",
    "2588022910298549780-242ac117-0001-012",
    "2438643947743669780-242ac117-0001-012",
    "SRR12018279",
    "2578702826971262484-242ac117-0001-012",
    "2434821426850229780-242ac117-0001-012",
    "SRR12018302",
    "2575223907756469780-242ac117-0001-012",
    "2432845741894069780-242ac117-0001-012",
    "SRR12018291",
    "2583255496599989780-242ac117-0001-012",
    "2431900849088949780-242ac117-0001-012",
    "SRR12664075",
    "2574021316913589780-242ac117-0001-012",
    "2431857895121022484-242ac117-0001-012",
    "SRR12018309",
    "2576383548926389780-242ac117-0001-012",
    "2433962429096062484-242ac117-0001-012",
    "SRR12018280",
    "2577371391404469780-242ac117-0001-012",
    "2433962433391029780-242ac117-0001-012",
    "SRR12664077",
    "2578659881593269780-242ac117-0001-012"
  ],
  "bios:anatomicalStructure": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:identifier": "UBERON:0013756",
      "schema:inDefinedTermSet": "UBERON",
      "schema:name": "venous blood"
    }
  ],
  "bios:associatedPhenotype": [
    {
      "schema:name": "CD3+ CD4+ CD45RA- CD154+ CD69+"
    },
    {
      "schema:name": "CD3+ CD4+ CD45RA- CD137+ CD69+"
    }
  ],
  "nde:cellType": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:identifier": "CL:0000897",
      "schema:inDefinedTermSet": "CL",
      "schema:name": "CD4-positive, alpha-beta memory T cell"
    }
  ],
  "bios:collector": [
    {
      "@type": [
        "schema:Person"
      ],
      "schema:name": "La Jolla Institute for Immunology"
    },
    {
      "@type": [
        "schema:Person"
      ],
      "schema:name": "La Jolla Institute for Immunology"
    }
  ],
  "schema:conditionsOfAccess": "Open",
  "bios:developmentalStage": [
    {
      "@type": [
        "schema:QuantitativeValue"
      ],
      "schema:maxValue": 82,
      "schema:minValue": 22,
      "schema:unitCode": "UO:0000036",
      "schema:unitText": "year"
    }
  ],
  "schema:distribution": [
    {
      "@type": [
        "schema:DataDownload"
      ],
      "schema:contentUrl": "SRR12018290_1.fastq.gz",
      "schema:description": "read_length: 101; paired_read_length: 101",
      "schema:encodingFormat": [
        "fastq"
      ]
    },
    {
      "@type": [
        "schema:DataDownload"
      ],
      "schema:contentUrl": "SRR12018290_2.fastq.gz",
      "schema:description": "read_length: 101",
      "schema:encodingFormat": [
        "fastq"
      ]
    },
    {
      "@type": [
        "schema:DataDownload"
      ],
      "schema:contentUrl": "SRR12018305_1.fastq.gz",
      "schema:description": "read_length: 101; paired_read_length: 101",
      "schema:encodingFormat": [
        "fastq"
      ]
    },
    {
      "@type": [
        "schema:DataDownload"
      ],
      "schema:contentUrl": "SRR12018305_2.fastq.gz",
      "schema:description": "read_length: 101",
      "schema:encodingFormat": [
        "fastq"
      ]
    },
    {
      "@type": [
        "schema:DataDownload"
      ],
      "schema:contentUrl": "SRR12018282_1.fastq.gz",
      "schema:description": "read_length: 101; paired_read_length: 101",
      "schema:encodingFormat": [
        "fastq"
      ]
    },
    {
      "@type": [
        "schema:DataDownload"
      ],
      "schema:contentUrl": "SRR12018282_2.fastq.gz",
      "schema:description": "read_length: 101",
      "schema:encodingFormat": [
        "fastq"
      ]
    },
    {
      "@type": [
        "schema:DataDownload"
      ],
      "schema:contentUrl": "SRR12664074_1.fastq.gz",
      "schema:description": "read_length: 101; paired_read_length: 101",
      "schema:encodingFormat": [
        "fastq"
      ]
    },
    {
      "@type": [
        "schema:DataDownload"
      ],
      "schema:contentUrl": "SRR12664074_2.fastq.gz",
      "schema:description": "read_length: 101",
      "schema:encodingFormat": [
        "fastq"
      ]
    },
    {
      "@type": [
        "schema:DataDownload"
      ],
      "schema:contentUrl": "SRR12664078_1.fastq.gz",
      "schema:description": "read_length: 101; paired_read_length: 101",
      "schema:encodingFormat": [
        "fastq"
      ]
    },
    {
      "@type": [
        "schema:DataDownload"
      ],
      "schema:contentUrl": "SRR12664078_2.fastq.gz",
      "schema:description": "read_length: 101",
      "schema:encodingFormat": [
        "fastq"
      ]
    },
    {
      "@type": [
        "schema:DataDownload"
      ],
      "schema:contentUrl": "SRR12018289_1.fastq.gz",
      "schema:description": "read_length: 101; paired_read_length: 101",
      "schema:encodingFormat": [
        "fastq"
      ]
    },
    {
      "@type": [
        "schema:DataDownload"
      ],
      "schema:contentUrl": "SRR12018289_2.fastq.gz",
      "schema:description": "read_length: 101",
      "schema:encodingFormat": [
        "fastq"
      ]
    },
    {
      "@type": [
        "schema:DataDownload"
      ],
      "schema:contentUrl": "SRR12664076_1.fastq.gz",
      "schema:description": "read_length: 101; paired_read_length: 101",
      "schema:encodingFormat": [
        "fastq"
      ]
    },
    {
      "@type": [
        "schema:DataDownload"
      ],
      "schema:contentUrl": "SRR12664076_2.fastq.gz",
      "schema:description": "read_length: 101",
      "schema:encodingFormat": [
        "fastq"
      ]
    },
    {
      "@type": [
        "schema:DataDownload"
      ],
      "schema:contentUrl": "SRR12018283_1.fastq.gz",
      "schema:description": "read_length: 101; paired_read_length: 101",
      "schema:encodingFormat": [
        "fastq"
      ]
    },
    {
      "@type": [
        "schema:DataDownload"
      ],
      "schema:contentUrl": "SRR12018283_2.fastq.gz",
      "schema:description": "read_length: 101",
      "schema:encodingFormat": [
        "fastq"
      ]
    },
    {
      "@type": [
        "schema:DataDownload"
      ],
      "schema:contentUrl": "SRR12018284_1.fastq.gz",
      "schema:description": "read_length: 101; paired_read_length: 101",
      "schema:encodingFormat": [
        "fastq"
      ]
    },
    {
      "@type": [
        "schema:DataDownload"
      ],
      "schema:contentUrl": "SRR12018284_2.fastq.gz",
      "schema:description": "read_length: 101",
      "schema:encodingFormat": [
        "fastq"
      ]
    },
    {
      "@type": [
        "schema:DataDownload"
      ],
      "schema:contentUrl": "SRR12018287_1.fastq.gz",
      "schema:description": "read_length: 101; paired_read_length: 101",
      "schema:encodingFormat": [
        "fastq"
      ]
    },
    {
      "@type": [
        "schema:DataDownload"
      ],
      "schema:contentUrl": "SRR12018287_2.fastq.gz",
      "schema:description": "read_length: 101",
      "schema:encodingFormat": [
        "fastq"
      ]
    },
    {
      "@type": [
        "schema:DataDownload"
      ],
      "schema:contentUrl": "SRR12018303_1.fastq.gz",
      "schema:description": "read_length: 101; paired_read_length: 101",
      "schema:encodingFormat": [
        "fastq"
      ]
    },
    {
      "@type": [
        "schema:DataDownload"
      ],
      "schema:contentUrl": "SRR12018303_2.fastq.gz",
      "schema:description": "read_length: 101",
      "schema:encodingFormat": [
        "fastq"
      ]
    },
    {
      "@type": [
        "schema:DataDownload"
      ],
      "schema:contentUrl": "SRR12018288_1.fastq.gz",
      "schema:description": "read_length: 101; paired_read_length: 101",
      "schema:encodingFormat": [
        "fastq"
      ]
    },
    {
      "@type": [
        "schema:DataDownload"
      ],
      "schema:contentUrl": "SRR12018288_2.fastq.gz",
      "schema:description": "read_length: 101",
      "schema:encodingFormat": [
        "fastq"
      ]
    },
    {
      "@type": [
        "schema:DataDownload"
      ],
      "schema:contentUrl": "SRR12018286_1.fastq.gz",
      "schema:description": "read_length: 101; paired_read_length: 101",
      "schema:encodingFormat": [
        "fastq"
      ]
    },
    {
      "@type": [
        "schema:DataDownload"
      ],
      "schema:contentUrl": "SRR12018286_2.fastq.gz",
      "schema:description": "read_length: 101",
      "schema:encodingFormat": [
        "fastq"
      ]
    },
    {
      "@type": [
        "schema:DataDownload"
      ],
      "schema:contentUrl": "SRR12018310_1.fastq.gz",
      "schema:description": "read_length: 101; paired_read_length: 101",
      "schema:encodingFormat": [
        "fastq"
      ]
    },
    {
      "@type": [
        "schema:DataDownload"
      ],
      "schema:contentUrl": "SRR12018310_2.fastq.gz",
      "schema:description": "read_length: 101",
      "schema:encodingFormat": [
        "fastq"
      ]
    },
    {
      "@type": [
        "schema:DataDownload"
      ],
      "schema:contentUrl": "SRR12018306_1.fastq.gz",
      "schema:description": "read_length: 101; paired_read_length: 101",
      "schema:encodingFormat": [
        "fastq"
      ]
    },
    {
      "@type": [
        "schema:DataDownload"
      ],
      "schema:contentUrl": "SRR12018306_2.fastq.gz",
      "schema:description": "read_length: 101",
      "schema:encodingFormat": [
        "fastq"
      ]
    },
    {
      "@type": [
        "schema:DataDownload"
      ],
      "schema:contentUrl": "SRR12018304_1.fastq.gz",
      "schema:description": "read_length: 101; paired_read_length: 101",
      "schema:encodingFormat": [
        "fastq"
      ]
    },
    {
      "@type": [
        "schema:DataDownload"
      ],
      "schema:contentUrl": "SRR12018304_2.fastq.gz",
      "schema:description": "read_length: 101",
      "schema:encodingFormat": [
        "fastq"
      ]
    },
    {
      "@type": [
        "schema:DataDownload"
      ],
      "schema:contentUrl": "SRR12018281_1.fastq.gz",
      "schema:description": "read_length: 101; paired_read_length: 101",
      "schema:encodingFormat": [
        "fastq"
      ]
    },
    {
      "@type": [
        "schema:DataDownload"
      ],
      "schema:contentUrl": "SRR12018281_2.fastq.gz",
      "schema:description": "read_length: 101",
      "schema:encodingFormat": [
        "fastq"
      ]
    },
    {
      "@type": [
        "schema:DataDownload"
      ],
      "schema:contentUrl": "SRR12018285_1.fastq.gz",
      "schema:description": "read_length: 101; paired_read_length: 101",
      "schema:encodingFormat": [
        "fastq"
      ]
    },
    {
      "@type": [
        "schema:DataDownload"
      ],
      "schema:contentUrl": "SRR12018285_2.fastq.gz",
      "schema:description": "read_length: 101",
      "schema:encodingFormat": [
        "fastq"
      ]
    },
    {
      "@type": [
        "schema:DataDownload"
      ],
      "schema:contentUrl": "SRR12664079_1.fastq.gz",
      "schema:description": "read_length: 101; paired_read_length: 101",
      "schema:encodingFormat": [
        "fastq"
      ]
    },
    {
      "@type": [
        "schema:DataDownload"
      ],
      "schema:contentUrl": "SRR12664079_2.fastq.gz",
      "schema:description": "read_length: 101",
      "schema:encodingFormat": [
        "fastq"
      ]
    },
    {
      "@type": [
        "schema:DataDownload"
      ],
      "schema:contentUrl": "SRR12018279_1.fastq.gz",
      "schema:description": "read_length: 101; paired_read_length: 101",
      "schema:encodingFormat": [
        "fastq"
      ]
    },
    {
      "@type": [
        "schema:DataDownload"
      ],
      "schema:contentUrl": "SRR12018279_2.fastq.gz",
      "schema:description": "read_length: 101",
      "schema:encodingFormat": [
        "fastq"
      ]
    },
    {
      "@type": [
        "schema:DataDownload"
      ],
      "schema:contentUrl": "SRR12018302_1.fastq.gz",
      "schema:description": "read_length: 101; paired_read_length: 101",
      "schema:encodingFormat": [
        "fastq"
      ]
    },
    {
      "@type": [
        "schema:DataDownload"
      ],
      "schema:contentUrl": "SRR12018302_2.fastq.gz",
      "schema:description": "read_length: 101",
      "schema:encodingFormat": [
        "fastq"
      ]
    },
    {
      "@type": [
        "schema:DataDownload"
      ],
      "schema:contentUrl": "SRR12018291_1.fastq.gz",
      "schema:description": "read_length: 101; paired_read_length: 101",
      "schema:encodingFormat": [
        "fastq"
      ]
    },
    {
      "@type": [
        "schema:DataDownload"
      ],
      "schema:contentUrl": "SRR12018291_2.fastq.gz",
      "schema:description": "read_length: 101",
      "schema:encodingFormat": [
        "fastq"
      ]
    },
    {
      "@type": [
        "schema:DataDownload"
      ],
      "schema:contentUrl": "SRR12664075_1.fastq.gz",
      "schema:description": "read_length: 101; paired_read_length: 101",
      "schema:encodingFormat": [
        "fastq"
      ]
    },
    {
      "@type": [
        "schema:DataDownload"
      ],
      "schema:contentUrl": "SRR12664075_2.fastq.gz",
      "schema:description": "read_length: 101",
      "schema:encodingFormat": [
        "fastq"
      ]
    },
    {
      "@type": [
        "schema:DataDownload"
      ],
      "schema:contentUrl": "SRR12018309_1.fastq.gz",
      "schema:description": "read_length: 101; paired_read_length: 101",
      "schema:encodingFormat": [
        "fastq"
      ]
    },
    {
      "@type": [
        "schema:DataDownload"
      ],
      "schema:contentUrl": "SRR12018309_2.fastq.gz",
      "schema:description": "read_length: 101",
      "schema:encodingFormat": [
        "fastq"
      ]
    },
    {
      "@type": [
        "schema:DataDownload"
      ],
      "schema:contentUrl": "SRR12018280_1.fastq.gz",
      "schema:description": "read_length: 101; paired_read_length: 101",
      "schema:encodingFormat": [
        "fastq"
      ]
    },
    {
      "@type": [
        "schema:DataDownload"
      ],
      "schema:contentUrl": "SRR12018280_2.fastq.gz",
      "schema:description": "read_length: 101",
      "schema:encodingFormat": [
        "fastq"
      ]
    },
    {
      "@type": [
        "schema:DataDownload"
      ],
      "schema:contentUrl": "SRR12664077_1.fastq.gz",
      "schema:description": "read_length: 101; paired_read_length: 101",
      "schema:encodingFormat": [
        "fastq"
      ]
    },
    {
      "@type": [
        "schema:DataDownload"
      ],
      "schema:contentUrl": "SRR12664077_2.fastq.gz",
      "schema:description": "read_length: 101",
      "schema:encodingFormat": [
        "fastq"
      ]
    }
  ],
  "schema:healthCondition": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:identifier": "DOID:0080600",
      "schema:inDefinedTermSet": "DOID",
      "schema:name": "COVID-19"
    },
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:identifier": "DOID:0080600",
      "schema:inDefinedTermSet": "DOID",
      "schema:name": "COVID-19"
    }
  ],
  "schema:instrument": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:name": "Illumina NovaSeq 6000"
    },
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:name": "Illumina NovaSeq 6000"
    }
  ],
  "schema:isAccessibleForFree": true,
  "schema:license": "https://creativecommons.org/public-domain/",
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:identifier": "NCIT:C16084",
      "schema:inDefinedTermSet": "NCIT",
      "schema:name": "Observational Study"
    },
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:description": "10x Genomics Chromium Single Cell 5' Feature Barcode Library; Chromium Single Cell 5' Library & Gel Bead Kit; Chromium Single Cell 5' Library Construction Kit; Chromium Single Cell V(D)J Enrichment Kit, Human T Cell; Chromium Single Cell Chip A Kit; Chromium i7 Multiplex Kit; Chromium i7 Multiplex Kit N, Set A",
      "schema:name": "library preparation"
    },
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:name": "RT(oligo-dT)+TS(UMI)+PCR"
    },
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:description": "Single-cell RNA-sequencing library preparation was performed as per the manufacturer\u2019s recommendations for the 10x Genomics 5\u2019 TAG v1.0 chemistry with immune profiling and cell surface protein technology. Both initial amplification of cDNA and library preparation were carried out with 13 cycles of amplification; V(D)J and cell surface protein libraries were generated corresponding to each 5\u2019\u2019 TAG gene expression library using 9 cycles and 8 cycles of amplification, respectively. Libraries were quantified and pooled according to equivalent molar concentrations and sequenced on Illumina NovaSeq6000 sequencing platform with the following read lengths: read 1, 101 cycles; read 2, 101 cycles; i7 index, 8 cycles.",
      "schema:name": "library preparation"
    },
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:identifier": "NCIT:C16084",
      "schema:inDefinedTermSet": "NCIT",
      "schema:name": "Observational Study"
    },
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:description": "10x Genomics Chromium Single Cell 5' Feature Barcode Library; Chromium Single Cell 5' Library & Gel Bead Kit; Chromium Single Cell 5' Library Construction Kit; Chromium Single Cell V(D)J Enrichment Kit, Human T Cell; Chromium Single Cell Chip A Kit; Chromium i7 Multiplex Kit; Chromium i7 Multiplex Kit N, Set A",
      "schema:name": "library preparation"
    },
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:name": "RT(oligo-dT)+TS(UMI)+PCR"
    },
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:description": "Single-cell RNA-sequencing library preparation was performed as per the manufacturer\u2019s recommendations for the 10x Genomics 5\u2019 TAG v1.0 chemistry with immune profiling and cell surface protein technology. Both initial amplification of cDNA and library preparation were carried out with 13 cycles of amplification; V(D)J and cell surface protein libraries were generated corresponding to each 5\u2019\u2019 TAG gene expression library using 9 cycles and 8 cycles of amplification, respectively. Libraries were quantified and pooled according to equivalent molar concentrations and sequenced on Illumina NovaSeq6000 sequencing platform with the following read lengths: read 1, 101 cycles; read 2, 101 cycles; i7 index, 8 cycles.",
      "schema:name": "library preparation"
    }
  ],
  "schema:name": [
    "Imbalance of Regulatory and Cytotoxic SARS-CoV-2-Reactive CD4 + T Cells in COVID-19 (2444012656863669780-242ac117-0001-012)",
    "Imbalance of Regulatory and Cytotoxic SARS-CoV-2-Reactive CD4 + T Cells in COVID-19 (2434434879793589780-242ac117-0001-012)",
    "Imbalance of Regulatory and Cytotoxic SARS-CoV-2-Reactive CD4 + T Cells in COVID-19 (2425243649780149780-242ac117-0001-012)",
    "Imbalance of Regulatory and Cytotoxic SARS-CoV-2-Reactive CD4 + T Cells in COVID-19 (2429710415767989780-242ac117-0001-012)",
    "Imbalance of Regulatory and Cytotoxic SARS-CoV-2-Reactive CD4 + T Cells in COVID-19 (2431299553667509780-242ac117-0001-012)",
    "Imbalance of Regulatory and Cytotoxic SARS-CoV-2-Reactive CD4 + T Cells in COVID-19 (2432029698107829780-242ac117-0001-012)",
    "Imbalance of Regulatory and Cytotoxic SARS-CoV-2-Reactive CD4 + T Cells in COVID-19 (2438686897416629780-242ac117-0001-012)",
    "Imbalance of Regulatory and Cytotoxic SARS-CoV-2-Reactive CD4 + T Cells in COVID-19 (2434348980447669780-242ac117-0001-012)",
    "Imbalance of Regulatory and Cytotoxic SARS-CoV-2-Reactive CD4 + T Cells in COVID-19 (2434520779139509780-242ac117-0001-012)",
    "Imbalance of Regulatory and Cytotoxic SARS-CoV-2-Reactive CD4 + T Cells in COVID-19 (2429452717730229780-242ac117-0001-012)",
    "Imbalance of Regulatory and Cytotoxic SARS-CoV-2-Reactive CD4 + T Cells in COVID-19 (2434950275869109780-242ac117-0001-012)",
    "Imbalance of Regulatory and Cytotoxic SARS-CoV-2-Reactive CD4 + T Cells in COVID-19 (2423783360899509780-242ac117-0001-012)",
    "Imbalance of Regulatory and Cytotoxic SARS-CoV-2-Reactive CD4 + T Cells in COVID-19 (2434005383063989780-242ac117-0001-012)",
    "Imbalance of Regulatory and Cytotoxic SARS-CoV-2-Reactive CD4 + T Cells in COVID-19 (2432201496799669780-242ac117-0001-012)",
    "Imbalance of Regulatory and Cytotoxic SARS-CoV-2-Reactive CD4 + T Cells in COVID-19 (2429323868711349780-242ac117-0001-012)",
    "Imbalance of Regulatory and Cytotoxic SARS-CoV-2-Reactive CD4 + T Cells in COVID-19 (2429409768057269780-242ac117-0001-012)",
    "Imbalance of Regulatory and Cytotoxic SARS-CoV-2-Reactive CD4 + T Cells in COVID-19 (2434864376523189780-242ac117-0001-012)",
    "Imbalance of Regulatory and Cytotoxic SARS-CoV-2-Reactive CD4 + T Cells in COVID-19 (2434907326196149780-242ac117-0001-012)",
    "Imbalance of Regulatory and Cytotoxic SARS-CoV-2-Reactive CD4 + T Cells in COVID-19 (2431857899415989780-242ac117-0001-012)",
    "Imbalance of Regulatory and Cytotoxic SARS-CoV-2-Reactive CD4 + T Cells in COVID-19 (2438643947743669780-242ac117-0001-012)",
    "Imbalance of Regulatory and Cytotoxic SARS-CoV-2-Reactive CD4 + T Cells in COVID-19 (2434821426850229780-242ac117-0001-012)",
    "Imbalance of Regulatory and Cytotoxic SARS-CoV-2-Reactive CD4 + T Cells in COVID-19 (2432845741894069780-242ac117-0001-012)",
    "Imbalance of Regulatory and Cytotoxic SARS-CoV-2-Reactive CD4 + T Cells in COVID-19 (2431900849088949780-242ac117-0001-012)",
    "Imbalance of Regulatory and Cytotoxic SARS-CoV-2-Reactive CD4 + T Cells in COVID-19 (2431857895121022484-242ac117-0001-012)",
    "Imbalance of Regulatory and Cytotoxic SARS-CoV-2-Reactive CD4 + T Cells in COVID-19 (2433962429096062484-242ac117-0001-012)",
    "Imbalance of Regulatory and Cytotoxic SARS-CoV-2-Reactive CD4 + T Cells in COVID-19 (2433962433391029780-242ac117-0001-012)"
  ],
  "bios:sampleProcess": [
    "PBMCs from each donor were thawed, washed, plated in 24-well culture plates at a concentration of 5x10^6 cells/mL in 1 mL of serum-free TexMACS medium (Miltenyi Biotec) and left overnight (5% CO2, 37C). Cells were stimulated by the addition of individual virus-specific peptide pools (1 mg/mL) for 6 h in the presence of a blocking CD40 antibody (1 mg/mL; Miltenyi Biotec). Cells were sequentially stained with fluorescence-labeled surface antibodies, Cell-hashtag TotalSeq-C antibody (0.5 mg/condition), and a biotin-conjugated CD154 antibody (clone 5C8; Miltenyi Biotec) followed by anti-biotin microbeads (Miltenyi Biotec). Labeled cells were added to MS columns (Miltenyi Biotec) and positively selected cells (CD154+) were eluted and used for FACS sorting with a FACSAria Fusion Cell Sorter (Becton Dickinson). Up to 60,000 cells from individual donors were pooled by sorting into low retention 1.5 mL collection tubes, containing 500 ml of a 1:1 solution of PBS:FBS supplemented with recombinant RNase inhibitor (1:100, Takara). Following sorting, ice-cold PBS was added to make up to a volume of 1400 ml. Cells were then centrifuged for 5 min (600 g at 4C) and the supernatant was removed leaving 5 to 10 ml. 25 ml of resuspension buffer (0.22 mm filtered ice-cold PBS supplemented with ultra-pure bovine serum albumin; 0.04%, Sigma-Aldrich) was added to the tube and the pellet was resuspended. Following mixing, 33 ml of the cell suspension was transferred to a PCR-tube for processing as per the manufacturer\u2019s instructions (10x Genomics).",
    "PBMCs were isolated from up to 80ml of anti-coagulated blood by density centrifugation over Lymphoprep (Axis-Shield PoC AS, Oslo, Norway) and cryopreserved in 50% decomplemented human antibody serum, 40% complete RMPI 1640 medium and 10% DMSO.",
    "Single cell: True",
    "none",
    "PBMCs from each donor were thawed, washed, plated in 24-well culture plates at a concentration of 5x10^6 cells/mL in 1 mL of serum-free TexMACS medium (Miltenyi Biotec) and left overnight (5% CO2, 37C). Cells were stimulated by the addition of individual virus-specific peptide pools (1 mg/mL) for 6 h in the presence of a blocking CD40 antibody (1 mg/mL; Miltenyi Biotec). Cells were sequentially stained with fluorescence-labeled surface antibodies, Cell-hashtag TotalSeq-C antibody (0.5 mg/condition), and a biotin-conjugated CD154 antibody (clone 5C8; Miltenyi Biotec) followed by anti-biotin microbeads (Miltenyi Biotec). Labeled cells were added to MS columns (Miltenyi Biotec) for positive selection of CD154+ cells. The flow-through from the column was collected and re-plated to harvest cells responding 24 h after peptide stimulation. Analogous to enrichment for CD154+, CD137-expressing CD4+ memory T cells were positively selected by staining with biotin-conjugated CD137 antibody (clone REA765; Miltenyi Biotec) followed by anti-biotin MicroBeads and applied to a new MS column for sorting with a FACSAria Fusion Cell Sorter (Becton Dickinson). Up to 60,000 cells from individual donors were pooled by sorting into low retention 1.5 mL collection tubes, containing 500 ml of a 1:1 solution of PBS:FBS supplemented with recombinant RNase inhibitor (1:100, Takara). Following sorting, ice-cold PBS was added to make up to a volume of 1400 ml. Cells were then centrifuged for 5 min (600 g at 4C) and the supernatant was removed leaving 5 to 10 ml. 25 ml of resuspension buffer (0.22 mm filtered ice-cold PBS supplemented with ultra-pure bovine serum albumin; 0.04%, Sigma-Aldrich) was added to the tube and the pellet was resuspended. Following mixing, 33 ml of the cell suspension was transferred to a PCR-tube for processing as per the manufacturer\u2019s instructions (10x Genomics).",
    "PBMCs were isolated from up to 80ml of anti-coagulated blood by density centrifugation over Lymphoprep (Axis-Shield PoC AS, Oslo, Norway) and cryopreserved in 50% decomplemented human antibody serum, 40% complete RMPI 1640 medium and 10% DMSO.",
    "Single cell: True",
    "none",
    "PBMCs from each donor were thawed, washed, plated in 24-well culture plates at a concentration of 5x10^6 cells/mL in 1 mL of serum-free TexMACS medium (Miltenyi Biotec) and left overnight (5% CO2, 37C). Cells were stimulated by the addition of individual virus-specific peptide pools (1 mg/mL) for 6 h in the presence of a blocking CD40 antibody (1 mg/mL; Miltenyi Biotec). Cells were sequentially stained with fluorescence-labeled surface antibodies, Cell-hashtag TotalSeq-C antibody (0.5 mg/condition), and a biotin-conjugated CD154 antibody (clone 5C8; Miltenyi Biotec) followed by anti-biotin microbeads (Miltenyi Biotec). Labeled cells were added to MS columns (Miltenyi Biotec) and positively selected cells (CD154+) were eluted and used for FACS sorting with a FACSAria Fusion Cell Sorter (Becton Dickinson). Up to 60,000 cells from individual donors were pooled by sorting into low retention 1.5 mL collection tubes, containing 500 ml of a 1:1 solution of PBS:FBS supplemented with recombinant RNase inhibitor (1:100, Takara). Following sorting, ice-cold PBS was added to make up to a volume of 1400 ml. Cells were then centrifuged for 5 min (600 g at 4C) and the supernatant was removed leaving 5 to 10 ml. 25 ml of resuspension buffer (0.22 mm filtered ice-cold PBS supplemented with ultra-pure bovine serum albumin; 0.04%, Sigma-Aldrich) was added to the tube and the pellet was resuspended. Following mixing, 33 ml of the cell suspension was transferred to a PCR-tube for processing as per the manufacturer\u2019s instructions (10x Genomics).",
    "PBMCs from each donor were thawed, washed, plated in 24-well culture plates at a concentration of 5x10^6 cells/mL in 1 mL of serum-free TexMACS medium (Miltenyi Biotec) and left overnight (5% CO2, 37C). Cells were sequentially stained with fluorescence-labeled surface antibodies, Cell-hashtag TotalSeq-C antibody (0.5 mg/condition), and a biotin-conjugated CD154 antibody (clone 5C8; Miltenyi Biotec) followed by anti-biotin microbeads (Miltenyi Biotec). Labeled cells were added to MS columns (Miltenyi Biotec) and positively selected cells (CD154+) were eluted and used for FACS sorting with a FACSAria Fusion Cell Sorter (Becton Dickinson). Up to 60,000 cells from individual donors were pooled by sorting into low retention 1.5 mL collection tubes, containing 500 ml of a 1:1 solution of PBS:FBS supplemented with recombinant RNase inhibitor (1:100, Takara). Following sorting, ice-cold PBS was added to make up to a volume of 1400 ml. Cells were then centrifuged for 5 min (600 g at 4C) and the supernatant was removed leaving 5 to 10 ml. 25 ml of resuspension buffer (0.22 mm filtered ice-cold PBS supplemented with ultra-pure bovine serum albumin; 0.04%, Sigma-Aldrich) was added to the tube and the pellet was resuspended. Following mixing, 33 ml of the cell suspension was transferred to a PCR-tube for processing as per the manufacturer\u2019s instructions (10x Genomics)."
  ],
  "bios:sampleQuantity": [
    {
      "@type": [
        "schema:QuantitativeValue"
      ],
      "schema:maxValue": 13409,
      "schema:minValue": 1346,
      "schema:name": "cell_number"
    },
    {
      "@type": [
        "schema:QuantitativeValue"
      ],
      "schema:maxValue": 1,
      "schema:minValue": 1,
      "schema:name": "cells_per_reaction"
    }
  ],
  "bios:sampleState": [
    "Live cells as determined by Fixable Viability Dye eFluor 780 (eBioscience)",
    "complete+untemplated",
    "Live cells as determined by Fixable Viability Dye eFluor 780 (eBioscience)",
    "complete+untemplated"
  ],
  "bios:sampleType": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:name": "RNA"
    },
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:name": "peripheral venous puncture"
    }
  ],
  "bios:sex": [
    "pooled"
  ],
  "nde:species": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:identifier": "NCBITAXON:9606",
      "schema:inDefinedTermSet": "NCBITAXON",
      "schema:name": "Homo sapiens"
    },
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:identifier": "NCBITAXON:9606",
      "schema:inDefinedTermSet": "NCBITAXON",
      "schema:name": "Homo sapiens"
    }
  ],
  "schema:temporalCoverage": [
    {
      "@type": [
        "nde:TemporalInterval"
      ],
      "schema:duration": "6 hour",
      "schema:name": "peptide stimulation"
    },
    {
      "@type": [
        "nde:TemporalInterval"
      ],
      "schema:duration": "24 hour",
      "schema:name": "peptide stimulation"
    },
    {
      "@type": [
        "nde:TemporalInterval"
      ],
      "schema:duration": "6 hour",
      "schema:name": "peptide stimulation"
    },
    {
      "@type": [
        "nde:TemporalInterval"
      ],
      "schema:duration": "0 hour",
      "schema:name": "peptide stimulation"
    }
  ],
  "schema:usageInfo": {
    "@type": [
      "schema:Thing"
    ],
    "schema:description": "The software is under the GNU Affero General Public License, the data is Public Domain",
    "schema:name": "AIRR Data Commons usage info"
  },
  "schema:variableMeasured": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:identifier": "C20971",
      "schema:inDefinedTermSet": "NCIT",
      "schema:name": "V(D)J Recombination",
      "schema:url": "https://evsexplore.semantics.cancer.gov/evsexplore/concept/ncit/C20971"
    },
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:identifier": "data_2977",
      "schema:inDefinedTermSet": "EDAM",
      "schema:name": "Nucleic acid sequence",
      "schema:url": "https://edamontology.org/data_2977"
    },
    {
      "schema:description": "White",
      "schema:name": "race"
    },
    {
      "schema:description": "Asian",
      "schema:name": "race"
    },
    {
      "schema:description": "COVID_mild",
      "schema:name": "disease severity"
    },
    {
      "schema:description": "peptide pool stimulation of PBMCs",
      "schema:name": "intervention"
    },
    {
      "schema:description": "Black",
      "schema:name": "race"
    },
    {
      "schema:description": "COVID_severe",
      "schema:name": "disease severity"
    },
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:description": "White",
      "schema:name": "race"
    },
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:description": "Asian",
      "schema:name": "race"
    },
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:description": "COVID_mild",
      "schema:name": "disease severity"
    },
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:description": "peptide pool stimulation of PBMCs",
      "schema:name": "intervention"
    },
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:description": "reverse primer: TRAC, +42",
      "schema:name": "TRA"
    },
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:description": "reverse primer: TRBC, +52",
      "schema:name": "TRB"
    },
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:identifier": "C20971",
      "schema:inDefinedTermSet": "NCIT",
      "schema:name": "V(D)J Recombination",
      "schema:url": "https://evsexplore.semantics.cancer.gov/evsexplore/concept/ncit/C20971"
    },
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:identifier": "data_2977",
      "schema:inDefinedTermSet": "EDAM",
      "schema:name": "Nucleic acid sequence",
      "schema:url": "https://edamontology.org/data_2977"
    },
    {
      "schema:description": "White",
      "schema:name": "race"
    },
    {
      "schema:description": "Asian",
      "schema:name": "race"
    },
    {
      "schema:description": "COVID_mild",
      "schema:name": "disease severity"
    },
    {
      "schema:description": "peptide pool stimulation of PBMCs",
      "schema:name": "intervention"
    },
    {
      "schema:description": "Black",
      "schema:name": "race"
    },
    {
      "schema:description": "COVID_severe",
      "schema:name": "disease severity"
    },
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:description": "White",
      "schema:name": "race"
    },
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:description": "Asian",
      "schema:name": "race"
    },
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:description": "Black",
      "schema:name": "race"
    },
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:description": "COVID_severe",
      "schema:name": "disease severity"
    },
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:description": "peptide pool stimulation of PBMCs",
      "schema:name": "intervention"
    },
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:description": "reverse primer: TRAC, +42",
      "schema:name": "TRA"
    },
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:description": "reverse primer: TRBC, +52",
      "schema:name": "TRB"
    },
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:description": "COVID_mild",
      "schema:name": "disease severity"
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
      "bios": "https://bioschemas.org/",
      "nde": "https://discovery.biothings.io/ns/nde/"
    },
    "https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/bioschemasProperties/bioschemasSample/context.jsonld",
    {
      "schema": "http://schema.org/",
      "bios": "https://bioschemas.org/",
      "nde": "https://discovery.biothings.io/ns/nde/"
    }
  ],
  "@type": [
    "nde:Sample",
    "bios:Sample"
  ],
  "schema:additionalType": "ExperimentalRunSample",
  "bios:alternateIdentifier": [
    "2444012656863669780-242ac117-0001-012",
    "SRR12018290",
    "2590428091984309780-242ac117-0001-012",
    "2434434879793589780-242ac117-0001-012",
    "SRR12018305",
    "2587979960625589780-242ac117-0001-012",
    "2425243649780149780-242ac117-0001-012",
    "SRR12018282",
    "2578702831266229780-242ac117-0001-012",
    "2429710415767989780-242ac117-0001-012",
    "SRR12664074",
    "2593606367783349780-242ac117-0001-012",
    "2431299553667509780-242ac117-0001-012",
    "SRR12664078",
    "2579218227341749780-242ac117-0001-012",
    "2432029698107829780-242ac117-0001-012",
    "SRR12018289",
    "2576984844347829780-242ac117-0001-012",
    "2438686897416629780-242ac117-0001-012",
    "SRR12664076",
    "2576898945001909780-242ac117-0001-012",
    "2434348980447669780-242ac117-0001-012",
    "SRR12018283",
    "2583899741694389780-242ac117-0001-012",
    "2434520779139509780-242ac117-0001-012",
    "SRR12018284",
    "2593090971707829780-242ac117-0001-012",
    "2429452717730229780-242ac117-0001-012",
    "SRR12018287",
    "2582654201178549780-242ac117-0001-012",
    "2434950275869109780-242ac117-0001-012",
    "SRR12018303",
    "2582611251505589780-242ac117-0001-012",
    "2423783360899509780-242ac117-0001-012",
    "SRR12018288",
    "2590170393946549780-242ac117-0001-012",
    "2434005383063989780-242ac117-0001-012",
    "SRR12018286",
    "2584629886134709780-242ac117-0001-012",
    "2432201496799669780-242ac117-0001-012",
    "SRR12018310",
    "2579347076360629780-242ac117-0001-012",
    "2429323868711349780-242ac117-0001-012",
    "SRR12018306",
    "2578616931920309780-242ac117-0001-012",
    "2429409768057269780-242ac117-0001-012",
    "SRR12018304",
    "2593606363488382484-242ac117-0001-012",
    "2434864376523189780-242ac117-0001-012",
    "SRR12018281",
    "2585746577631669780-242ac117-0001-012",
    "2434907326196149780-242ac117-0001-012",
    "SRR12018285",
    "2573763618875829780-242ac117-0001-012",
    "2431857899415989780-242ac117-0001-012",
    "SRR12664079",
    "2588022910298549780-242ac117-0001-012",
    "2438643947743669780-242ac117-0001-012",
    "SRR12018279",
    "2578702826971262484-242ac117-0001-012",
    "2434821426850229780-242ac117-0001-012",
    "SRR12018302",
    "2575223907756469780-242ac117-0001-012",
    "2432845741894069780-242ac117-0001-012",
    "SRR12018291",
    "2583255496599989780-242ac117-0001-012",
    "2431900849088949780-242ac117-0001-012",
    "SRR12664075",
    "2574021316913589780-242ac117-0001-012",
    "2431857895121022484-242ac117-0001-012",
    "SRR12018309",
    "2576383548926389780-242ac117-0001-012",
    "2433962429096062484-242ac117-0001-012",
    "SRR12018280",
    "2577371391404469780-242ac117-0001-012",
    "2433962433391029780-242ac117-0001-012",
    "SRR12664077",
    "2578659881593269780-242ac117-0001-012"
  ],
  "bios:anatomicalStructure": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:identifier": "UBERON:0013756",
      "schema:inDefinedTermSet": "UBERON",
      "schema:name": "venous blood"
    }
  ],
  "bios:associatedPhenotype": [
    {
      "schema:name": "CD3+ CD4+ CD45RA- CD154+ CD69+"
    },
    {
      "schema:name": "CD3+ CD4+ CD45RA- CD137+ CD69+"
    }
  ],
  "nde:cellType": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:identifier": "CL:0000897",
      "schema:inDefinedTermSet": "CL",
      "schema:name": "CD4-positive, alpha-beta memory T cell"
    }
  ],
  "bios:collector": [
    {
      "@type": [
        "schema:Person"
      ],
      "schema:name": "La Jolla Institute for Immunology"
    },
    {
      "@type": [
        "schema:Person"
      ],
      "schema:name": "La Jolla Institute for Immunology"
    }
  ],
  "schema:conditionsOfAccess": "Open",
  "bios:developmentalStage": [
    {
      "@type": [
        "schema:QuantitativeValue"
      ],
      "schema:maxValue": 82,
      "schema:minValue": 22,
      "schema:unitCode": "UO:0000036",
      "schema:unitText": "year"
    }
  ],
  "schema:distribution": [
    {
      "@type": [
        "schema:DataDownload"
      ],
      "schema:contentUrl": "SRR12018290_1.fastq.gz",
      "schema:description": "read_length: 101; paired_read_length: 101",
      "schema:encodingFormat": [
        "fastq"
      ]
    },
    {
      "@type": [
        "schema:DataDownload"
      ],
      "schema:contentUrl": "SRR12018290_2.fastq.gz",
      "schema:description": "read_length: 101",
      "schema:encodingFormat": [
        "fastq"
      ]
    },
    {
      "@type": [
        "schema:DataDownload"
      ],
      "schema:contentUrl": "SRR12018305_1.fastq.gz",
      "schema:description": "read_length: 101; paired_read_length: 101",
      "schema:encodingFormat": [
        "fastq"
      ]
    },
    {
      "@type": [
        "schema:DataDownload"
      ],
      "schema:contentUrl": "SRR12018305_2.fastq.gz",
      "schema:description": "read_length: 101",
      "schema:encodingFormat": [
        "fastq"
      ]
    },
    {
      "@type": [
        "schema:DataDownload"
      ],
      "schema:contentUrl": "SRR12018282_1.fastq.gz",
      "schema:description": "read_length: 101; paired_read_length: 101",
      "schema:encodingFormat": [
        "fastq"
      ]
    },
    {
      "@type": [
        "schema:DataDownload"
      ],
      "schema:contentUrl": "SRR12018282_2.fastq.gz",
      "schema:description": "read_length: 101",
      "schema:encodingFormat": [
        "fastq"
      ]
    },
    {
      "@type": [
        "schema:DataDownload"
      ],
      "schema:contentUrl": "SRR12664074_1.fastq.gz",
      "schema:description": "read_length: 101; paired_read_length: 101",
      "schema:encodingFormat": [
        "fastq"
      ]
    },
    {
      "@type": [
        "schema:DataDownload"
      ],
      "schema:contentUrl": "SRR12664074_2.fastq.gz",
      "schema:description": "read_length: 101",
      "schema:encodingFormat": [
        "fastq"
      ]
    },
    {
      "@type": [
        "schema:DataDownload"
      ],
      "schema:contentUrl": "SRR12664078_1.fastq.gz",
      "schema:description": "read_length: 101; paired_read_length: 101",
      "schema:encodingFormat": [
        "fastq"
      ]
    },
    {
      "@type": [
        "schema:DataDownload"
      ],
      "schema:contentUrl": "SRR12664078_2.fastq.gz",
      "schema:description": "read_length: 101",
      "schema:encodingFormat": [
        "fastq"
      ]
    },
    {
      "@type": [
        "schema:DataDownload"
      ],
      "schema:contentUrl": "SRR12018289_1.fastq.gz",
      "schema:description": "read_length: 101; paired_read_length: 101",
      "schema:encodingFormat": [
        "fastq"
      ]
    },
    {
      "@type": [
        "schema:DataDownload"
      ],
      "schema:contentUrl": "SRR12018289_2.fastq.gz",
      "schema:description": "read_length: 101",
      "schema:encodingFormat": [
        "fastq"
      ]
    },
    {
      "@type": [
        "schema:DataDownload"
      ],
      "schema:contentUrl": "SRR12664076_1.fastq.gz",
      "schema:description": "read_length: 101; paired_read_length: 101",
      "schema:encodingFormat": [
        "fastq"
      ]
    },
    {
      "@type": [
        "schema:DataDownload"
      ],
      "schema:contentUrl": "SRR12664076_2.fastq.gz",
      "schema:description": "read_length: 101",
      "schema:encodingFormat": [
        "fastq"
      ]
    },
    {
      "@type": [
        "schema:DataDownload"
      ],
      "schema:contentUrl": "SRR12018283_1.fastq.gz",
      "schema:description": "read_length: 101; paired_read_length: 101",
      "schema:encodingFormat": [
        "fastq"
      ]
    },
    {
      "@type": [
        "schema:DataDownload"
      ],
      "schema:contentUrl": "SRR12018283_2.fastq.gz",
      "schema:description": "read_length: 101",
      "schema:encodingFormat": [
        "fastq"
      ]
    },
    {
      "@type": [
        "schema:DataDownload"
      ],
      "schema:contentUrl": "SRR12018284_1.fastq.gz",
      "schema:description": "read_length: 101; paired_read_length: 101",
      "schema:encodingFormat": [
        "fastq"
      ]
    },
    {
      "@type": [
        "schema:DataDownload"
      ],
      "schema:contentUrl": "SRR12018284_2.fastq.gz",
      "schema:description": "read_length: 101",
      "schema:encodingFormat": [
        "fastq"
      ]
    },
    {
      "@type": [
        "schema:DataDownload"
      ],
      "schema:contentUrl": "SRR12018287_1.fastq.gz",
      "schema:description": "read_length: 101; paired_read_length: 101",
      "schema:encodingFormat": [
        "fastq"
      ]
    },
    {
      "@type": [
        "schema:DataDownload"
      ],
      "schema:contentUrl": "SRR12018287_2.fastq.gz",
      "schema:description": "read_length: 101",
      "schema:encodingFormat": [
        "fastq"
      ]
    },
    {
      "@type": [
        "schema:DataDownload"
      ],
      "schema:contentUrl": "SRR12018303_1.fastq.gz",
      "schema:description": "read_length: 101; paired_read_length: 101",
      "schema:encodingFormat": [
        "fastq"
      ]
    },
    {
      "@type": [
        "schema:DataDownload"
      ],
      "schema:contentUrl": "SRR12018303_2.fastq.gz",
      "schema:description": "read_length: 101",
      "schema:encodingFormat": [
        "fastq"
      ]
    },
    {
      "@type": [
        "schema:DataDownload"
      ],
      "schema:contentUrl": "SRR12018288_1.fastq.gz",
      "schema:description": "read_length: 101; paired_read_length: 101",
      "schema:encodingFormat": [
        "fastq"
      ]
    },
    {
      "@type": [
        "schema:DataDownload"
      ],
      "schema:contentUrl": "SRR12018288_2.fastq.gz",
      "schema:description": "read_length: 101",
      "schema:encodingFormat": [
        "fastq"
      ]
    },
    {
      "@type": [
        "schema:DataDownload"
      ],
      "schema:contentUrl": "SRR12018286_1.fastq.gz",
      "schema:description": "read_length: 101; paired_read_length: 101",
      "schema:encodingFormat": [
        "fastq"
      ]
    },
    {
      "@type": [
        "schema:DataDownload"
      ],
      "schema:contentUrl": "SRR12018286_2.fastq.gz",
      "schema:description": "read_length: 101",
      "schema:encodingFormat": [
        "fastq"
      ]
    },
    {
      "@type": [
        "schema:DataDownload"
      ],
      "schema:contentUrl": "SRR12018310_1.fastq.gz",
      "schema:description": "read_length: 101; paired_read_length: 101",
      "schema:encodingFormat": [
        "fastq"
      ]
    },
    {
      "@type": [
        "schema:DataDownload"
      ],
      "schema:contentUrl": "SRR12018310_2.fastq.gz",
      "schema:description": "read_length: 101",
      "schema:encodingFormat": [
        "fastq"
      ]
    },
    {
      "@type": [
        "schema:DataDownload"
      ],
      "schema:contentUrl": "SRR12018306_1.fastq.gz",
      "schema:description": "read_length: 101; paired_read_length: 101",
      "schema:encodingFormat": [
        "fastq"
      ]
    },
    {
      "@type": [
        "schema:DataDownload"
      ],
      "schema:contentUrl": "SRR12018306_2.fastq.gz",
      "schema:description": "read_length: 101",
      "schema:encodingFormat": [
        "fastq"
      ]
    },
    {
      "@type": [
        "schema:DataDownload"
      ],
      "schema:contentUrl": "SRR12018304_1.fastq.gz",
      "schema:description": "read_length: 101; paired_read_length: 101",
      "schema:encodingFormat": [
        "fastq"
      ]
    },
    {
      "@type": [
        "schema:DataDownload"
      ],
      "schema:contentUrl": "SRR12018304_2.fastq.gz",
      "schema:description": "read_length: 101",
      "schema:encodingFormat": [
        "fastq"
      ]
    },
    {
      "@type": [
        "schema:DataDownload"
      ],
      "schema:contentUrl": "SRR12018281_1.fastq.gz",
      "schema:description": "read_length: 101; paired_read_length: 101",
      "schema:encodingFormat": [
        "fastq"
      ]
    },
    {
      "@type": [
        "schema:DataDownload"
      ],
      "schema:contentUrl": "SRR12018281_2.fastq.gz",
      "schema:description": "read_length: 101",
      "schema:encodingFormat": [
        "fastq"
      ]
    },
    {
      "@type": [
        "schema:DataDownload"
      ],
      "schema:contentUrl": "SRR12018285_1.fastq.gz",
      "schema:description": "read_length: 101; paired_read_length: 101",
      "schema:encodingFormat": [
        "fastq"
      ]
    },
    {
      "@type": [
        "schema:DataDownload"
      ],
      "schema:contentUrl": "SRR12018285_2.fastq.gz",
      "schema:description": "read_length: 101",
      "schema:encodingFormat": [
        "fastq"
      ]
    },
    {
      "@type": [
        "schema:DataDownload"
      ],
      "schema:contentUrl": "SRR12664079_1.fastq.gz",
      "schema:description": "read_length: 101; paired_read_length: 101",
      "schema:encodingFormat": [
        "fastq"
      ]
    },
    {
      "@type": [
        "schema:DataDownload"
      ],
      "schema:contentUrl": "SRR12664079_2.fastq.gz",
      "schema:description": "read_length: 101",
      "schema:encodingFormat": [
        "fastq"
      ]
    },
    {
      "@type": [
        "schema:DataDownload"
      ],
      "schema:contentUrl": "SRR12018279_1.fastq.gz",
      "schema:description": "read_length: 101; paired_read_length: 101",
      "schema:encodingFormat": [
        "fastq"
      ]
    },
    {
      "@type": [
        "schema:DataDownload"
      ],
      "schema:contentUrl": "SRR12018279_2.fastq.gz",
      "schema:description": "read_length: 101",
      "schema:encodingFormat": [
        "fastq"
      ]
    },
    {
      "@type": [
        "schema:DataDownload"
      ],
      "schema:contentUrl": "SRR12018302_1.fastq.gz",
      "schema:description": "read_length: 101; paired_read_length: 101",
      "schema:encodingFormat": [
        "fastq"
      ]
    },
    {
      "@type": [
        "schema:DataDownload"
      ],
      "schema:contentUrl": "SRR12018302_2.fastq.gz",
      "schema:description": "read_length: 101",
      "schema:encodingFormat": [
        "fastq"
      ]
    },
    {
      "@type": [
        "schema:DataDownload"
      ],
      "schema:contentUrl": "SRR12018291_1.fastq.gz",
      "schema:description": "read_length: 101; paired_read_length: 101",
      "schema:encodingFormat": [
        "fastq"
      ]
    },
    {
      "@type": [
        "schema:DataDownload"
      ],
      "schema:contentUrl": "SRR12018291_2.fastq.gz",
      "schema:description": "read_length: 101",
      "schema:encodingFormat": [
        "fastq"
      ]
    },
    {
      "@type": [
        "schema:DataDownload"
      ],
      "schema:contentUrl": "SRR12664075_1.fastq.gz",
      "schema:description": "read_length: 101; paired_read_length: 101",
      "schema:encodingFormat": [
        "fastq"
      ]
    },
    {
      "@type": [
        "schema:DataDownload"
      ],
      "schema:contentUrl": "SRR12664075_2.fastq.gz",
      "schema:description": "read_length: 101",
      "schema:encodingFormat": [
        "fastq"
      ]
    },
    {
      "@type": [
        "schema:DataDownload"
      ],
      "schema:contentUrl": "SRR12018309_1.fastq.gz",
      "schema:description": "read_length: 101; paired_read_length: 101",
      "schema:encodingFormat": [
        "fastq"
      ]
    },
    {
      "@type": [
        "schema:DataDownload"
      ],
      "schema:contentUrl": "SRR12018309_2.fastq.gz",
      "schema:description": "read_length: 101",
      "schema:encodingFormat": [
        "fastq"
      ]
    },
    {
      "@type": [
        "schema:DataDownload"
      ],
      "schema:contentUrl": "SRR12018280_1.fastq.gz",
      "schema:description": "read_length: 101; paired_read_length: 101",
      "schema:encodingFormat": [
        "fastq"
      ]
    },
    {
      "@type": [
        "schema:DataDownload"
      ],
      "schema:contentUrl": "SRR12018280_2.fastq.gz",
      "schema:description": "read_length: 101",
      "schema:encodingFormat": [
        "fastq"
      ]
    },
    {
      "@type": [
        "schema:DataDownload"
      ],
      "schema:contentUrl": "SRR12664077_1.fastq.gz",
      "schema:description": "read_length: 101; paired_read_length: 101",
      "schema:encodingFormat": [
        "fastq"
      ]
    },
    {
      "@type": [
        "schema:DataDownload"
      ],
      "schema:contentUrl": "SRR12664077_2.fastq.gz",
      "schema:description": "read_length: 101",
      "schema:encodingFormat": [
        "fastq"
      ]
    }
  ],
  "schema:healthCondition": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:identifier": "DOID:0080600",
      "schema:inDefinedTermSet": "DOID",
      "schema:name": "COVID-19"
    },
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:identifier": "DOID:0080600",
      "schema:inDefinedTermSet": "DOID",
      "schema:name": "COVID-19"
    }
  ],
  "schema:instrument": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:name": "Illumina NovaSeq 6000"
    },
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:name": "Illumina NovaSeq 6000"
    }
  ],
  "schema:isAccessibleForFree": true,
  "schema:license": "https://creativecommons.org/public-domain/",
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:identifier": "NCIT:C16084",
      "schema:inDefinedTermSet": "NCIT",
      "schema:name": "Observational Study"
    },
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:description": "10x Genomics Chromium Single Cell 5' Feature Barcode Library; Chromium Single Cell 5' Library & Gel Bead Kit; Chromium Single Cell 5' Library Construction Kit; Chromium Single Cell V(D)J Enrichment Kit, Human T Cell; Chromium Single Cell Chip A Kit; Chromium i7 Multiplex Kit; Chromium i7 Multiplex Kit N, Set A",
      "schema:name": "library preparation"
    },
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:name": "RT(oligo-dT)+TS(UMI)+PCR"
    },
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:description": "Single-cell RNA-sequencing library preparation was performed as per the manufacturer\u2019s recommendations for the 10x Genomics 5\u2019 TAG v1.0 chemistry with immune profiling and cell surface protein technology. Both initial amplification of cDNA and library preparation were carried out with 13 cycles of amplification; V(D)J and cell surface protein libraries were generated corresponding to each 5\u2019\u2019 TAG gene expression library using 9 cycles and 8 cycles of amplification, respectively. Libraries were quantified and pooled according to equivalent molar concentrations and sequenced on Illumina NovaSeq6000 sequencing platform with the following read lengths: read 1, 101 cycles; read 2, 101 cycles; i7 index, 8 cycles.",
      "schema:name": "library preparation"
    },
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:identifier": "NCIT:C16084",
      "schema:inDefinedTermSet": "NCIT",
      "schema:name": "Observational Study"
    },
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:description": "10x Genomics Chromium Single Cell 5' Feature Barcode Library; Chromium Single Cell 5' Library & Gel Bead Kit; Chromium Single Cell 5' Library Construction Kit; Chromium Single Cell V(D)J Enrichment Kit, Human T Cell; Chromium Single Cell Chip A Kit; Chromium i7 Multiplex Kit; Chromium i7 Multiplex Kit N, Set A",
      "schema:name": "library preparation"
    },
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:name": "RT(oligo-dT)+TS(UMI)+PCR"
    },
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:description": "Single-cell RNA-sequencing library preparation was performed as per the manufacturer\u2019s recommendations for the 10x Genomics 5\u2019 TAG v1.0 chemistry with immune profiling and cell surface protein technology. Both initial amplification of cDNA and library preparation were carried out with 13 cycles of amplification; V(D)J and cell surface protein libraries were generated corresponding to each 5\u2019\u2019 TAG gene expression library using 9 cycles and 8 cycles of amplification, respectively. Libraries were quantified and pooled according to equivalent molar concentrations and sequenced on Illumina NovaSeq6000 sequencing platform with the following read lengths: read 1, 101 cycles; read 2, 101 cycles; i7 index, 8 cycles.",
      "schema:name": "library preparation"
    }
  ],
  "schema:name": [
    "Imbalance of Regulatory and Cytotoxic SARS-CoV-2-Reactive CD4 + T Cells in COVID-19 (2444012656863669780-242ac117-0001-012)",
    "Imbalance of Regulatory and Cytotoxic SARS-CoV-2-Reactive CD4 + T Cells in COVID-19 (2434434879793589780-242ac117-0001-012)",
    "Imbalance of Regulatory and Cytotoxic SARS-CoV-2-Reactive CD4 + T Cells in COVID-19 (2425243649780149780-242ac117-0001-012)",
    "Imbalance of Regulatory and Cytotoxic SARS-CoV-2-Reactive CD4 + T Cells in COVID-19 (2429710415767989780-242ac117-0001-012)",
    "Imbalance of Regulatory and Cytotoxic SARS-CoV-2-Reactive CD4 + T Cells in COVID-19 (2431299553667509780-242ac117-0001-012)",
    "Imbalance of Regulatory and Cytotoxic SARS-CoV-2-Reactive CD4 + T Cells in COVID-19 (2432029698107829780-242ac117-0001-012)",
    "Imbalance of Regulatory and Cytotoxic SARS-CoV-2-Reactive CD4 + T Cells in COVID-19 (2438686897416629780-242ac117-0001-012)",
    "Imbalance of Regulatory and Cytotoxic SARS-CoV-2-Reactive CD4 + T Cells in COVID-19 (2434348980447669780-242ac117-0001-012)",
    "Imbalance of Regulatory and Cytotoxic SARS-CoV-2-Reactive CD4 + T Cells in COVID-19 (2434520779139509780-242ac117-0001-012)",
    "Imbalance of Regulatory and Cytotoxic SARS-CoV-2-Reactive CD4 + T Cells in COVID-19 (2429452717730229780-242ac117-0001-012)",
    "Imbalance of Regulatory and Cytotoxic SARS-CoV-2-Reactive CD4 + T Cells in COVID-19 (2434950275869109780-242ac117-0001-012)",
    "Imbalance of Regulatory and Cytotoxic SARS-CoV-2-Reactive CD4 + T Cells in COVID-19 (2423783360899509780-242ac117-0001-012)",
    "Imbalance of Regulatory and Cytotoxic SARS-CoV-2-Reactive CD4 + T Cells in COVID-19 (2434005383063989780-242ac117-0001-012)",
    "Imbalance of Regulatory and Cytotoxic SARS-CoV-2-Reactive CD4 + T Cells in COVID-19 (2432201496799669780-242ac117-0001-012)",
    "Imbalance of Regulatory and Cytotoxic SARS-CoV-2-Reactive CD4 + T Cells in COVID-19 (2429323868711349780-242ac117-0001-012)",
    "Imbalance of Regulatory and Cytotoxic SARS-CoV-2-Reactive CD4 + T Cells in COVID-19 (2429409768057269780-242ac117-0001-012)",
    "Imbalance of Regulatory and Cytotoxic SARS-CoV-2-Reactive CD4 + T Cells in COVID-19 (2434864376523189780-242ac117-0001-012)",
    "Imbalance of Regulatory and Cytotoxic SARS-CoV-2-Reactive CD4 + T Cells in COVID-19 (2434907326196149780-242ac117-0001-012)",
    "Imbalance of Regulatory and Cytotoxic SARS-CoV-2-Reactive CD4 + T Cells in COVID-19 (2431857899415989780-242ac117-0001-012)",
    "Imbalance of Regulatory and Cytotoxic SARS-CoV-2-Reactive CD4 + T Cells in COVID-19 (2438643947743669780-242ac117-0001-012)",
    "Imbalance of Regulatory and Cytotoxic SARS-CoV-2-Reactive CD4 + T Cells in COVID-19 (2434821426850229780-242ac117-0001-012)",
    "Imbalance of Regulatory and Cytotoxic SARS-CoV-2-Reactive CD4 + T Cells in COVID-19 (2432845741894069780-242ac117-0001-012)",
    "Imbalance of Regulatory and Cytotoxic SARS-CoV-2-Reactive CD4 + T Cells in COVID-19 (2431900849088949780-242ac117-0001-012)",
    "Imbalance of Regulatory and Cytotoxic SARS-CoV-2-Reactive CD4 + T Cells in COVID-19 (2431857895121022484-242ac117-0001-012)",
    "Imbalance of Regulatory and Cytotoxic SARS-CoV-2-Reactive CD4 + T Cells in COVID-19 (2433962429096062484-242ac117-0001-012)",
    "Imbalance of Regulatory and Cytotoxic SARS-CoV-2-Reactive CD4 + T Cells in COVID-19 (2433962433391029780-242ac117-0001-012)"
  ],
  "bios:sampleProcess": [
    "PBMCs from each donor were thawed, washed, plated in 24-well culture plates at a concentration of 5x10^6 cells/mL in 1 mL of serum-free TexMACS medium (Miltenyi Biotec) and left overnight (5% CO2, 37C). Cells were stimulated by the addition of individual virus-specific peptide pools (1 mg/mL) for 6 h in the presence of a blocking CD40 antibody (1 mg/mL; Miltenyi Biotec). Cells were sequentially stained with fluorescence-labeled surface antibodies, Cell-hashtag TotalSeq-C antibody (0.5 mg/condition), and a biotin-conjugated CD154 antibody (clone 5C8; Miltenyi Biotec) followed by anti-biotin microbeads (Miltenyi Biotec). Labeled cells were added to MS columns (Miltenyi Biotec) and positively selected cells (CD154+) were eluted and used for FACS sorting with a FACSAria Fusion Cell Sorter (Becton Dickinson). Up to 60,000 cells from individual donors were pooled by sorting into low retention 1.5 mL collection tubes, containing 500 ml of a 1:1 solution of PBS:FBS supplemented with recombinant RNase inhibitor (1:100, Takara). Following sorting, ice-cold PBS was added to make up to a volume of 1400 ml. Cells were then centrifuged for 5 min (600 g at 4C) and the supernatant was removed leaving 5 to 10 ml. 25 ml of resuspension buffer (0.22 mm filtered ice-cold PBS supplemented with ultra-pure bovine serum albumin; 0.04%, Sigma-Aldrich) was added to the tube and the pellet was resuspended. Following mixing, 33 ml of the cell suspension was transferred to a PCR-tube for processing as per the manufacturer\u2019s instructions (10x Genomics).",
    "PBMCs were isolated from up to 80ml of anti-coagulated blood by density centrifugation over Lymphoprep (Axis-Shield PoC AS, Oslo, Norway) and cryopreserved in 50% decomplemented human antibody serum, 40% complete RMPI 1640 medium and 10% DMSO.",
    "Single cell: True",
    "none",
    "PBMCs from each donor were thawed, washed, plated in 24-well culture plates at a concentration of 5x10^6 cells/mL in 1 mL of serum-free TexMACS medium (Miltenyi Biotec) and left overnight (5% CO2, 37C). Cells were stimulated by the addition of individual virus-specific peptide pools (1 mg/mL) for 6 h in the presence of a blocking CD40 antibody (1 mg/mL; Miltenyi Biotec). Cells were sequentially stained with fluorescence-labeled surface antibodies, Cell-hashtag TotalSeq-C antibody (0.5 mg/condition), and a biotin-conjugated CD154 antibody (clone 5C8; Miltenyi Biotec) followed by anti-biotin microbeads (Miltenyi Biotec). Labeled cells were added to MS columns (Miltenyi Biotec) for positive selection of CD154+ cells. The flow-through from the column was collected and re-plated to harvest cells responding 24 h after peptide stimulation. Analogous to enrichment for CD154+, CD137-expressing CD4+ memory T cells were positively selected by staining with biotin-conjugated CD137 antibody (clone REA765; Miltenyi Biotec) followed by anti-biotin MicroBeads and applied to a new MS column for sorting with a FACSAria Fusion Cell Sorter (Becton Dickinson). Up to 60,000 cells from individual donors were pooled by sorting into low retention 1.5 mL collection tubes, containing 500 ml of a 1:1 solution of PBS:FBS supplemented with recombinant RNase inhibitor (1:100, Takara). Following sorting, ice-cold PBS was added to make up to a volume of 1400 ml. Cells were then centrifuged for 5 min (600 g at 4C) and the supernatant was removed leaving 5 to 10 ml. 25 ml of resuspension buffer (0.22 mm filtered ice-cold PBS supplemented with ultra-pure bovine serum albumin; 0.04%, Sigma-Aldrich) was added to the tube and the pellet was resuspended. Following mixing, 33 ml of the cell suspension was transferred to a PCR-tube for processing as per the manufacturer\u2019s instructions (10x Genomics).",
    "PBMCs were isolated from up to 80ml of anti-coagulated blood by density centrifugation over Lymphoprep (Axis-Shield PoC AS, Oslo, Norway) and cryopreserved in 50% decomplemented human antibody serum, 40% complete RMPI 1640 medium and 10% DMSO.",
    "Single cell: True",
    "none",
    "PBMCs from each donor were thawed, washed, plated in 24-well culture plates at a concentration of 5x10^6 cells/mL in 1 mL of serum-free TexMACS medium (Miltenyi Biotec) and left overnight (5% CO2, 37C). Cells were stimulated by the addition of individual virus-specific peptide pools (1 mg/mL) for 6 h in the presence of a blocking CD40 antibody (1 mg/mL; Miltenyi Biotec). Cells were sequentially stained with fluorescence-labeled surface antibodies, Cell-hashtag TotalSeq-C antibody (0.5 mg/condition), and a biotin-conjugated CD154 antibody (clone 5C8; Miltenyi Biotec) followed by anti-biotin microbeads (Miltenyi Biotec). Labeled cells were added to MS columns (Miltenyi Biotec) and positively selected cells (CD154+) were eluted and used for FACS sorting with a FACSAria Fusion Cell Sorter (Becton Dickinson). Up to 60,000 cells from individual donors were pooled by sorting into low retention 1.5 mL collection tubes, containing 500 ml of a 1:1 solution of PBS:FBS supplemented with recombinant RNase inhibitor (1:100, Takara). Following sorting, ice-cold PBS was added to make up to a volume of 1400 ml. Cells were then centrifuged for 5 min (600 g at 4C) and the supernatant was removed leaving 5 to 10 ml. 25 ml of resuspension buffer (0.22 mm filtered ice-cold PBS supplemented with ultra-pure bovine serum albumin; 0.04%, Sigma-Aldrich) was added to the tube and the pellet was resuspended. Following mixing, 33 ml of the cell suspension was transferred to a PCR-tube for processing as per the manufacturer\u2019s instructions (10x Genomics).",
    "PBMCs from each donor were thawed, washed, plated in 24-well culture plates at a concentration of 5x10^6 cells/mL in 1 mL of serum-free TexMACS medium (Miltenyi Biotec) and left overnight (5% CO2, 37C). Cells were sequentially stained with fluorescence-labeled surface antibodies, Cell-hashtag TotalSeq-C antibody (0.5 mg/condition), and a biotin-conjugated CD154 antibody (clone 5C8; Miltenyi Biotec) followed by anti-biotin microbeads (Miltenyi Biotec). Labeled cells were added to MS columns (Miltenyi Biotec) and positively selected cells (CD154+) were eluted and used for FACS sorting with a FACSAria Fusion Cell Sorter (Becton Dickinson). Up to 60,000 cells from individual donors were pooled by sorting into low retention 1.5 mL collection tubes, containing 500 ml of a 1:1 solution of PBS:FBS supplemented with recombinant RNase inhibitor (1:100, Takara). Following sorting, ice-cold PBS was added to make up to a volume of 1400 ml. Cells were then centrifuged for 5 min (600 g at 4C) and the supernatant was removed leaving 5 to 10 ml. 25 ml of resuspension buffer (0.22 mm filtered ice-cold PBS supplemented with ultra-pure bovine serum albumin; 0.04%, Sigma-Aldrich) was added to the tube and the pellet was resuspended. Following mixing, 33 ml of the cell suspension was transferred to a PCR-tube for processing as per the manufacturer\u2019s instructions (10x Genomics)."
  ],
  "bios:sampleQuantity": [
    {
      "@type": [
        "schema:QuantitativeValue"
      ],
      "schema:maxValue": 13409,
      "schema:minValue": 1346,
      "schema:name": "cell_number"
    },
    {
      "@type": [
        "schema:QuantitativeValue"
      ],
      "schema:maxValue": 1,
      "schema:minValue": 1,
      "schema:name": "cells_per_reaction"
    }
  ],
  "bios:sampleState": [
    "Live cells as determined by Fixable Viability Dye eFluor 780 (eBioscience)",
    "complete+untemplated",
    "Live cells as determined by Fixable Viability Dye eFluor 780 (eBioscience)",
    "complete+untemplated"
  ],
  "bios:sampleType": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:name": "RNA"
    },
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:name": "peripheral venous puncture"
    }
  ],
  "bios:sex": [
    "pooled"
  ],
  "nde:species": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:identifier": "NCBITAXON:9606",
      "schema:inDefinedTermSet": "NCBITAXON",
      "schema:name": "Homo sapiens"
    },
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:identifier": "NCBITAXON:9606",
      "schema:inDefinedTermSet": "NCBITAXON",
      "schema:name": "Homo sapiens"
    }
  ],
  "schema:temporalCoverage": [
    {
      "@type": [
        "nde:TemporalInterval"
      ],
      "schema:duration": "6 hour",
      "schema:name": "peptide stimulation"
    },
    {
      "@type": [
        "nde:TemporalInterval"
      ],
      "schema:duration": "24 hour",
      "schema:name": "peptide stimulation"
    },
    {
      "@type": [
        "nde:TemporalInterval"
      ],
      "schema:duration": "6 hour",
      "schema:name": "peptide stimulation"
    },
    {
      "@type": [
        "nde:TemporalInterval"
      ],
      "schema:duration": "0 hour",
      "schema:name": "peptide stimulation"
    }
  ],
  "schema:usageInfo": {
    "@type": [
      "schema:Thing"
    ],
    "schema:description": "The software is under the GNU Affero General Public License, the data is Public Domain",
    "schema:name": "AIRR Data Commons usage info"
  },
  "schema:variableMeasured": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:identifier": "C20971",
      "schema:inDefinedTermSet": "NCIT",
      "schema:name": "V(D)J Recombination",
      "schema:url": "https://evsexplore.semantics.cancer.gov/evsexplore/concept/ncit/C20971"
    },
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:identifier": "data_2977",
      "schema:inDefinedTermSet": "EDAM",
      "schema:name": "Nucleic acid sequence",
      "schema:url": "https://edamontology.org/data_2977"
    },
    {
      "schema:description": "White",
      "schema:name": "race"
    },
    {
      "schema:description": "Asian",
      "schema:name": "race"
    },
    {
      "schema:description": "COVID_mild",
      "schema:name": "disease severity"
    },
    {
      "schema:description": "peptide pool stimulation of PBMCs",
      "schema:name": "intervention"
    },
    {
      "schema:description": "Black",
      "schema:name": "race"
    },
    {
      "schema:description": "COVID_severe",
      "schema:name": "disease severity"
    },
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:description": "White",
      "schema:name": "race"
    },
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:description": "Asian",
      "schema:name": "race"
    },
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:description": "COVID_mild",
      "schema:name": "disease severity"
    },
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:description": "peptide pool stimulation of PBMCs",
      "schema:name": "intervention"
    },
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:description": "reverse primer: TRAC, +42",
      "schema:name": "TRA"
    },
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:description": "reverse primer: TRBC, +52",
      "schema:name": "TRB"
    },
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:identifier": "C20971",
      "schema:inDefinedTermSet": "NCIT",
      "schema:name": "V(D)J Recombination",
      "schema:url": "https://evsexplore.semantics.cancer.gov/evsexplore/concept/ncit/C20971"
    },
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:identifier": "data_2977",
      "schema:inDefinedTermSet": "EDAM",
      "schema:name": "Nucleic acid sequence",
      "schema:url": "https://edamontology.org/data_2977"
    },
    {
      "schema:description": "White",
      "schema:name": "race"
    },
    {
      "schema:description": "Asian",
      "schema:name": "race"
    },
    {
      "schema:description": "COVID_mild",
      "schema:name": "disease severity"
    },
    {
      "schema:description": "peptide pool stimulation of PBMCs",
      "schema:name": "intervention"
    },
    {
      "schema:description": "Black",
      "schema:name": "race"
    },
    {
      "schema:description": "COVID_severe",
      "schema:name": "disease severity"
    },
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:description": "White",
      "schema:name": "race"
    },
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:description": "Asian",
      "schema:name": "race"
    },
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:description": "Black",
      "schema:name": "race"
    },
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:description": "COVID_severe",
      "schema:name": "disease severity"
    },
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:description": "peptide pool stimulation of PBMCs",
      "schema:name": "intervention"
    },
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:description": "reverse primer: TRAC, +42",
      "schema:name": "TRA"
    },
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:description": "reverse primer: TRBC, +52",
      "schema:name": "TRB"
    },
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:description": "COVID_mild",
      "schema:name": "disease severity"
    }
  ]
}
```

#### ttl
```ttl
@prefix bios: <https://bioschemas.org/> .
@prefix nde: <https://discovery.biothings.io/ns/nde/> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

[] a bios:Sample,
        nde:Sample ;
    schema1:additionalType "ExperimentalRunSample" ;
    schema1:conditionsOfAccess "Open" ;
    schema1:distribution [ a schema1:DataDownload ;
            schema1:contentUrl "SRR12018285_1.fastq.gz" ;
            schema1:description "read_length: 101; paired_read_length: 101" ;
            schema1:encodingFormat "fastq" ],
        [ a schema1:DataDownload ;
            schema1:contentUrl "SRR12018309_1.fastq.gz" ;
            schema1:description "read_length: 101; paired_read_length: 101" ;
            schema1:encodingFormat "fastq" ],
        [ a schema1:DataDownload ;
            schema1:contentUrl "SRR12018288_2.fastq.gz" ;
            schema1:description "read_length: 101" ;
            schema1:encodingFormat "fastq" ],
        [ a schema1:DataDownload ;
            schema1:contentUrl "SRR12664076_1.fastq.gz" ;
            schema1:description "read_length: 101; paired_read_length: 101" ;
            schema1:encodingFormat "fastq" ],
        [ a schema1:DataDownload ;
            schema1:contentUrl "SRR12018283_1.fastq.gz" ;
            schema1:description "read_length: 101; paired_read_length: 101" ;
            schema1:encodingFormat "fastq" ],
        [ a schema1:DataDownload ;
            schema1:contentUrl "SRR12018281_1.fastq.gz" ;
            schema1:description "read_length: 101; paired_read_length: 101" ;
            schema1:encodingFormat "fastq" ],
        [ a schema1:DataDownload ;
            schema1:contentUrl "SRR12018303_1.fastq.gz" ;
            schema1:description "read_length: 101; paired_read_length: 101" ;
            schema1:encodingFormat "fastq" ],
        [ a schema1:DataDownload ;
            schema1:contentUrl "SRR12018280_2.fastq.gz" ;
            schema1:description "read_length: 101" ;
            schema1:encodingFormat "fastq" ],
        [ a schema1:DataDownload ;
            schema1:contentUrl "SRR12018287_1.fastq.gz" ;
            schema1:description "read_length: 101; paired_read_length: 101" ;
            schema1:encodingFormat "fastq" ],
        [ a schema1:DataDownload ;
            schema1:contentUrl "SRR12018280_1.fastq.gz" ;
            schema1:description "read_length: 101; paired_read_length: 101" ;
            schema1:encodingFormat "fastq" ],
        [ a schema1:DataDownload ;
            schema1:contentUrl "SRR12664077_2.fastq.gz" ;
            schema1:description "read_length: 101" ;
            schema1:encodingFormat "fastq" ],
        [ a schema1:DataDownload ;
            schema1:contentUrl "SRR12664075_2.fastq.gz" ;
            schema1:description "read_length: 101" ;
            schema1:encodingFormat "fastq" ],
        [ a schema1:DataDownload ;
            schema1:contentUrl "SRR12018283_2.fastq.gz" ;
            schema1:description "read_length: 101" ;
            schema1:encodingFormat "fastq" ],
        [ a schema1:DataDownload ;
            schema1:contentUrl "SRR12018286_2.fastq.gz" ;
            schema1:description "read_length: 101" ;
            schema1:encodingFormat "fastq" ],
        [ a schema1:DataDownload ;
            schema1:contentUrl "SRR12664077_1.fastq.gz" ;
            schema1:description "read_length: 101; paired_read_length: 101" ;
            schema1:encodingFormat "fastq" ],
        [ a schema1:DataDownload ;
            schema1:contentUrl "SRR12018289_1.fastq.gz" ;
            schema1:description "read_length: 101; paired_read_length: 101" ;
            schema1:encodingFormat "fastq" ],
        [ a schema1:DataDownload ;
            schema1:contentUrl "SRR12018290_2.fastq.gz" ;
            schema1:description "read_length: 101" ;
            schema1:encodingFormat "fastq" ],
        [ a schema1:DataDownload ;
            schema1:contentUrl "SRR12018289_2.fastq.gz" ;
            schema1:description "read_length: 101" ;
            schema1:encodingFormat "fastq" ],
        [ a schema1:DataDownload ;
            schema1:contentUrl "SRR12664074_1.fastq.gz" ;
            schema1:description "read_length: 101; paired_read_length: 101" ;
            schema1:encodingFormat "fastq" ],
        [ a schema1:DataDownload ;
            schema1:contentUrl "SRR12018282_2.fastq.gz" ;
            schema1:description "read_length: 101" ;
            schema1:encodingFormat "fastq" ],
        [ a schema1:DataDownload ;
            schema1:contentUrl "SRR12018310_1.fastq.gz" ;
            schema1:description "read_length: 101; paired_read_length: 101" ;
            schema1:encodingFormat "fastq" ],
        [ a schema1:DataDownload ;
            schema1:contentUrl "SRR12018309_2.fastq.gz" ;
            schema1:description "read_length: 101" ;
            schema1:encodingFormat "fastq" ],
        [ a schema1:DataDownload ;
            schema1:contentUrl "SRR12664078_1.fastq.gz" ;
            schema1:description "read_length: 101; paired_read_length: 101" ;
            schema1:encodingFormat "fastq" ],
        [ a schema1:DataDownload ;
            schema1:contentUrl "SRR12018291_1.fastq.gz" ;
            schema1:description "read_length: 101; paired_read_length: 101" ;
            schema1:encodingFormat "fastq" ],
        [ a schema1:DataDownload ;
            schema1:contentUrl "SRR12664075_1.fastq.gz" ;
            schema1:description "read_length: 101; paired_read_length: 101" ;
            schema1:encodingFormat "fastq" ],
        [ a schema1:DataDownload ;
            schema1:contentUrl "SRR12018302_1.fastq.gz" ;
            schema1:description "read_length: 101; paired_read_length: 101" ;
            schema1:encodingFormat "fastq" ],
        [ a schema1:DataDownload ;
            schema1:contentUrl "SRR12018291_2.fastq.gz" ;
            schema1:description "read_length: 101" ;
            schema1:encodingFormat "fastq" ],
        [ a schema1:DataDownload ;
            schema1:contentUrl "SRR12018305_2.fastq.gz" ;
            schema1:description "read_length: 101" ;
            schema1:encodingFormat "fastq" ],
        [ a schema1:DataDownload ;
            schema1:contentUrl "SRR12018284_2.fastq.gz" ;
            schema1:description "read_length: 101" ;
            schema1:encodingFormat "fastq" ],
        [ a schema1:DataDownload ;
            schema1:contentUrl "SRR12664078_2.fastq.gz" ;
            schema1:description "read_length: 101" ;
            schema1:encodingFormat "fastq" ],
        [ a schema1:DataDownload ;
            schema1:contentUrl "SRR12018288_1.fastq.gz" ;
            schema1:description "read_length: 101; paired_read_length: 101" ;
            schema1:encodingFormat "fastq" ],
        [ a schema1:DataDownload ;
            schema1:contentUrl "SRR12664074_2.fastq.gz" ;
            schema1:description "read_length: 101" ;
            schema1:encodingFormat "fastq" ],
        [ a schema1:DataDownload ;
            schema1:contentUrl "SRR12018304_1.fastq.gz" ;
            schema1:description "read_length: 101; paired_read_length: 101" ;
            schema1:encodingFormat "fastq" ],
        [ a schema1:DataDownload ;
            schema1:contentUrl "SRR12664076_2.fastq.gz" ;
            schema1:description "read_length: 101" ;
            schema1:encodingFormat "fastq" ],
        [ a schema1:DataDownload ;
            schema1:contentUrl "SRR12018284_1.fastq.gz" ;
            schema1:description "read_length: 101; paired_read_length: 101" ;
            schema1:encodingFormat "fastq" ],
        [ a schema1:DataDownload ;
            schema1:contentUrl "SRR12018287_2.fastq.gz" ;
            schema1:description "read_length: 101" ;
            schema1:encodingFormat "fastq" ],
        [ a schema1:DataDownload ;
            schema1:contentUrl "SRR12018310_2.fastq.gz" ;
            schema1:description "read_length: 101" ;
            schema1:encodingFormat "fastq" ],
        [ a schema1:DataDownload ;
            schema1:contentUrl "SRR12018306_1.fastq.gz" ;
            schema1:description "read_length: 101; paired_read_length: 101" ;
            schema1:encodingFormat "fastq" ],
        [ a schema1:DataDownload ;
            schema1:contentUrl "SRR12018282_1.fastq.gz" ;
            schema1:description "read_length: 101; paired_read_length: 101" ;
            schema1:encodingFormat "fastq" ],
        [ a schema1:DataDownload ;
            schema1:contentUrl "SRR12018290_1.fastq.gz" ;
            schema1:description "read_length: 101; paired_read_length: 101" ;
            schema1:encodingFormat "fastq" ],
        [ a schema1:DataDownload ;
            schema1:contentUrl "SRR12018304_2.fastq.gz" ;
            schema1:description "read_length: 101" ;
            schema1:encodingFormat "fastq" ],
        [ a schema1:DataDownload ;
            schema1:contentUrl "SRR12018281_2.fastq.gz" ;
            schema1:description "read_length: 101" ;
            schema1:encodingFormat "fastq" ],
        [ a schema1:DataDownload ;
            schema1:contentUrl "SRR12018302_2.fastq.gz" ;
            schema1:description "read_length: 101" ;
            schema1:encodingFormat "fastq" ],
        [ a schema1:DataDownload ;
            schema1:contentUrl "SRR12018303_2.fastq.gz" ;
            schema1:description "read_length: 101" ;
            schema1:encodingFormat "fastq" ],
        [ a schema1:DataDownload ;
            schema1:contentUrl "SRR12018305_1.fastq.gz" ;
            schema1:description "read_length: 101; paired_read_length: 101" ;
            schema1:encodingFormat "fastq" ],
        [ a schema1:DataDownload ;
            schema1:contentUrl "SRR12664079_2.fastq.gz" ;
            schema1:description "read_length: 101" ;
            schema1:encodingFormat "fastq" ],
        [ a schema1:DataDownload ;
            schema1:contentUrl "SRR12018306_2.fastq.gz" ;
            schema1:description "read_length: 101" ;
            schema1:encodingFormat "fastq" ],
        [ a schema1:DataDownload ;
            schema1:contentUrl "SRR12018279_1.fastq.gz" ;
            schema1:description "read_length: 101; paired_read_length: 101" ;
            schema1:encodingFormat "fastq" ],
        [ a schema1:DataDownload ;
            schema1:contentUrl "SRR12018285_2.fastq.gz" ;
            schema1:description "read_length: 101" ;
            schema1:encodingFormat "fastq" ],
        [ a schema1:DataDownload ;
            schema1:contentUrl "SRR12018279_2.fastq.gz" ;
            schema1:description "read_length: 101" ;
            schema1:encodingFormat "fastq" ],
        [ a schema1:DataDownload ;
            schema1:contentUrl "SRR12018286_1.fastq.gz" ;
            schema1:description "read_length: 101; paired_read_length: 101" ;
            schema1:encodingFormat "fastq" ],
        [ a schema1:DataDownload ;
            schema1:contentUrl "SRR12664079_1.fastq.gz" ;
            schema1:description "read_length: 101; paired_read_length: 101" ;
            schema1:encodingFormat "fastq" ] ;
    schema1:healthCondition [ a schema1:DefinedTerm ;
            schema1:identifier "DOID:0080600" ;
            schema1:inDefinedTermSet "DOID" ;
            schema1:name "COVID-19" ],
        [ a schema1:DefinedTerm ;
            schema1:identifier "DOID:0080600" ;
            schema1:inDefinedTermSet "DOID" ;
            schema1:name "COVID-19" ] ;
    schema1:instrument [ a schema1:DefinedTerm ;
            schema1:name "Illumina NovaSeq 6000" ],
        [ a schema1:DefinedTerm ;
            schema1:name "Illumina NovaSeq 6000" ] ;
    schema1:isAccessibleForFree true ;
    schema1:license "https://creativecommons.org/public-domain/" ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:name "RT(oligo-dT)+TS(UMI)+PCR" ],
        [ a schema1:DefinedTerm ;
            schema1:name "RT(oligo-dT)+TS(UMI)+PCR" ],
        [ a schema1:DefinedTerm ;
            schema1:description "Single-cell RNA-sequencing library preparation was performed as per the manufacturer’s recommendations for the 10x Genomics 5’ TAG v1.0 chemistry with immune profiling and cell surface protein technology. Both initial amplification of cDNA and library preparation were carried out with 13 cycles of amplification; V(D)J and cell surface protein libraries were generated corresponding to each 5’’ TAG gene expression library using 9 cycles and 8 cycles of amplification, respectively. Libraries were quantified and pooled according to equivalent molar concentrations and sequenced on Illumina NovaSeq6000 sequencing platform with the following read lengths: read 1, 101 cycles; read 2, 101 cycles; i7 index, 8 cycles." ;
            schema1:name "library preparation" ],
        [ a schema1:DefinedTerm ;
            schema1:description "10x Genomics Chromium Single Cell 5' Feature Barcode Library; Chromium Single Cell 5' Library & Gel Bead Kit; Chromium Single Cell 5' Library Construction Kit; Chromium Single Cell V(D)J Enrichment Kit, Human T Cell; Chromium Single Cell Chip A Kit; Chromium i7 Multiplex Kit; Chromium i7 Multiplex Kit N, Set A" ;
            schema1:name "library preparation" ],
        [ a schema1:DefinedTerm ;
            schema1:description "Single-cell RNA-sequencing library preparation was performed as per the manufacturer’s recommendations for the 10x Genomics 5’ TAG v1.0 chemistry with immune profiling and cell surface protein technology. Both initial amplification of cDNA and library preparation were carried out with 13 cycles of amplification; V(D)J and cell surface protein libraries were generated corresponding to each 5’’ TAG gene expression library using 9 cycles and 8 cycles of amplification, respectively. Libraries were quantified and pooled according to equivalent molar concentrations and sequenced on Illumina NovaSeq6000 sequencing platform with the following read lengths: read 1, 101 cycles; read 2, 101 cycles; i7 index, 8 cycles." ;
            schema1:name "library preparation" ],
        [ a schema1:DefinedTerm ;
            schema1:description "10x Genomics Chromium Single Cell 5' Feature Barcode Library; Chromium Single Cell 5' Library & Gel Bead Kit; Chromium Single Cell 5' Library Construction Kit; Chromium Single Cell V(D)J Enrichment Kit, Human T Cell; Chromium Single Cell Chip A Kit; Chromium i7 Multiplex Kit; Chromium i7 Multiplex Kit N, Set A" ;
            schema1:name "library preparation" ],
        [ a schema1:DefinedTerm ;
            schema1:identifier "NCIT:C16084" ;
            schema1:inDefinedTermSet "NCIT" ;
            schema1:name "Observational Study" ],
        [ a schema1:DefinedTerm ;
            schema1:identifier "NCIT:C16084" ;
            schema1:inDefinedTermSet "NCIT" ;
            schema1:name "Observational Study" ] ;
    schema1:name "Imbalance of Regulatory and Cytotoxic SARS-CoV-2-Reactive CD4 + T Cells in COVID-19 (2423783360899509780-242ac117-0001-012)",
        "Imbalance of Regulatory and Cytotoxic SARS-CoV-2-Reactive CD4 + T Cells in COVID-19 (2425243649780149780-242ac117-0001-012)",
        "Imbalance of Regulatory and Cytotoxic SARS-CoV-2-Reactive CD4 + T Cells in COVID-19 (2429323868711349780-242ac117-0001-012)",
        "Imbalance of Regulatory and Cytotoxic SARS-CoV-2-Reactive CD4 + T Cells in COVID-19 (2429409768057269780-242ac117-0001-012)",
        "Imbalance of Regulatory and Cytotoxic SARS-CoV-2-Reactive CD4 + T Cells in COVID-19 (2429452717730229780-242ac117-0001-012)",
        "Imbalance of Regulatory and Cytotoxic SARS-CoV-2-Reactive CD4 + T Cells in COVID-19 (2429710415767989780-242ac117-0001-012)",
        "Imbalance of Regulatory and Cytotoxic SARS-CoV-2-Reactive CD4 + T Cells in COVID-19 (2431299553667509780-242ac117-0001-012)",
        "Imbalance of Regulatory and Cytotoxic SARS-CoV-2-Reactive CD4 + T Cells in COVID-19 (2431857895121022484-242ac117-0001-012)",
        "Imbalance of Regulatory and Cytotoxic SARS-CoV-2-Reactive CD4 + T Cells in COVID-19 (2431857899415989780-242ac117-0001-012)",
        "Imbalance of Regulatory and Cytotoxic SARS-CoV-2-Reactive CD4 + T Cells in COVID-19 (2431900849088949780-242ac117-0001-012)",
        "Imbalance of Regulatory and Cytotoxic SARS-CoV-2-Reactive CD4 + T Cells in COVID-19 (2432029698107829780-242ac117-0001-012)",
        "Imbalance of Regulatory and Cytotoxic SARS-CoV-2-Reactive CD4 + T Cells in COVID-19 (2432201496799669780-242ac117-0001-012)",
        "Imbalance of Regulatory and Cytotoxic SARS-CoV-2-Reactive CD4 + T Cells in COVID-19 (2432845741894069780-242ac117-0001-012)",
        "Imbalance of Regulatory and Cytotoxic SARS-CoV-2-Reactive CD4 + T Cells in COVID-19 (2433962429096062484-242ac117-0001-012)",
        "Imbalance of Regulatory and Cytotoxic SARS-CoV-2-Reactive CD4 + T Cells in COVID-19 (2433962433391029780-242ac117-0001-012)",
        "Imbalance of Regulatory and Cytotoxic SARS-CoV-2-Reactive CD4 + T Cells in COVID-19 (2434005383063989780-242ac117-0001-012)",
        "Imbalance of Regulatory and Cytotoxic SARS-CoV-2-Reactive CD4 + T Cells in COVID-19 (2434348980447669780-242ac117-0001-012)",
        "Imbalance of Regulatory and Cytotoxic SARS-CoV-2-Reactive CD4 + T Cells in COVID-19 (2434434879793589780-242ac117-0001-012)",
        "Imbalance of Regulatory and Cytotoxic SARS-CoV-2-Reactive CD4 + T Cells in COVID-19 (2434520779139509780-242ac117-0001-012)",
        "Imbalance of Regulatory and Cytotoxic SARS-CoV-2-Reactive CD4 + T Cells in COVID-19 (2434821426850229780-242ac117-0001-012)",
        "Imbalance of Regulatory and Cytotoxic SARS-CoV-2-Reactive CD4 + T Cells in COVID-19 (2434864376523189780-242ac117-0001-012)",
        "Imbalance of Regulatory and Cytotoxic SARS-CoV-2-Reactive CD4 + T Cells in COVID-19 (2434907326196149780-242ac117-0001-012)",
        "Imbalance of Regulatory and Cytotoxic SARS-CoV-2-Reactive CD4 + T Cells in COVID-19 (2434950275869109780-242ac117-0001-012)",
        "Imbalance of Regulatory and Cytotoxic SARS-CoV-2-Reactive CD4 + T Cells in COVID-19 (2438643947743669780-242ac117-0001-012)",
        "Imbalance of Regulatory and Cytotoxic SARS-CoV-2-Reactive CD4 + T Cells in COVID-19 (2438686897416629780-242ac117-0001-012)",
        "Imbalance of Regulatory and Cytotoxic SARS-CoV-2-Reactive CD4 + T Cells in COVID-19 (2444012656863669780-242ac117-0001-012)" ;
    schema1:temporalCoverage [ a nde:TemporalInterval ;
            schema1:duration "24 hour" ;
            schema1:name "peptide stimulation" ],
        [ a nde:TemporalInterval ;
            schema1:duration "6 hour" ;
            schema1:name "peptide stimulation" ],
        [ a nde:TemporalInterval ;
            schema1:duration "6 hour" ;
            schema1:name "peptide stimulation" ],
        [ a nde:TemporalInterval ;
            schema1:duration "0 hour" ;
            schema1:name "peptide stimulation" ] ;
    schema1:usageInfo [ a schema1:Thing ;
            schema1:description "The software is under the GNU Affero General Public License, the data is Public Domain" ;
            schema1:name "AIRR Data Commons usage info" ] ;
    schema1:variableMeasured [ schema1:description "COVID_mild" ;
            schema1:name "disease severity" ],
        [ a schema1:DefinedTerm ;
            schema1:description "White" ;
            schema1:name "race" ],
        [ schema1:description "COVID_mild" ;
            schema1:name "disease severity" ],
        [ a schema1:DefinedTerm ;
            schema1:identifier "C20971" ;
            schema1:inDefinedTermSet "NCIT" ;
            schema1:name "V(D)J Recombination" ;
            schema1:url "https://evsexplore.semantics.cancer.gov/evsexplore/concept/ncit/C20971" ],
        [ a schema1:DefinedTerm ;
            schema1:description "reverse primer: TRBC, +52" ;
            schema1:name "TRB" ],
        [ a schema1:DefinedTerm ;
            schema1:description "peptide pool stimulation of PBMCs" ;
            schema1:name "intervention" ],
        [ schema1:description "Black" ;
            schema1:name "race" ],
        [ schema1:description "Asian" ;
            schema1:name "race" ],
        [ schema1:description "White" ;
            schema1:name "race" ],
        [ schema1:description "COVID_severe" ;
            schema1:name "disease severity" ],
        [ a schema1:DefinedTerm ;
            schema1:description "reverse primer: TRAC, +42" ;
            schema1:name "TRA" ],
        [ schema1:description "COVID_severe" ;
            schema1:name "disease severity" ],
        [ schema1:description "peptide pool stimulation of PBMCs" ;
            schema1:name "intervention" ],
        [ a schema1:DefinedTerm ;
            schema1:description "COVID_mild" ;
            schema1:name "disease severity" ],
        [ a schema1:DefinedTerm ;
            schema1:description "peptide pool stimulation of PBMCs" ;
            schema1:name "intervention" ],
        [ a schema1:DefinedTerm ;
            schema1:identifier "data_2977" ;
            schema1:inDefinedTermSet "EDAM" ;
            schema1:name "Nucleic acid sequence" ;
            schema1:url "https://edamontology.org/data_2977" ],
        [ schema1:description "peptide pool stimulation of PBMCs" ;
            schema1:name "intervention" ],
        [ a schema1:DefinedTerm ;
            schema1:identifier "data_2977" ;
            schema1:inDefinedTermSet "EDAM" ;
            schema1:name "Nucleic acid sequence" ;
            schema1:url "https://edamontology.org/data_2977" ],
        [ a schema1:DefinedTerm ;
            schema1:description "Asian" ;
            schema1:name "race" ],
        [ schema1:description "Black" ;
            schema1:name "race" ],
        [ a schema1:DefinedTerm ;
            schema1:description "COVID_mild" ;
            schema1:name "disease severity" ],
        [ a schema1:DefinedTerm ;
            schema1:description "White" ;
            schema1:name "race" ],
        [ schema1:description "Asian" ;
            schema1:name "race" ],
        [ a schema1:DefinedTerm ;
            schema1:description "reverse primer: TRBC, +52" ;
            schema1:name "TRB" ],
        [ schema1:description "White" ;
            schema1:name "race" ],
        [ a schema1:DefinedTerm ;
            schema1:identifier "C20971" ;
            schema1:inDefinedTermSet "NCIT" ;
            schema1:name "V(D)J Recombination" ;
            schema1:url "https://evsexplore.semantics.cancer.gov/evsexplore/concept/ncit/C20971" ],
        [ a schema1:DefinedTerm ;
            schema1:description "reverse primer: TRAC, +42" ;
            schema1:name "TRA" ],
        [ a schema1:DefinedTerm ;
            schema1:description "Asian" ;
            schema1:name "race" ],
        [ a schema1:DefinedTerm ;
            schema1:description "Black" ;
            schema1:name "race" ],
        [ a schema1:DefinedTerm ;
            schema1:description "COVID_severe" ;
            schema1:name "disease severity" ] ;
    bios:alternateIdentifier "2423783360899509780-242ac117-0001-012",
        "2425243649780149780-242ac117-0001-012",
        "2429323868711349780-242ac117-0001-012",
        "2429409768057269780-242ac117-0001-012",
        "2429452717730229780-242ac117-0001-012",
        "2429710415767989780-242ac117-0001-012",
        "2431299553667509780-242ac117-0001-012",
        "2431857895121022484-242ac117-0001-012",
        "2431857899415989780-242ac117-0001-012",
        "2431900849088949780-242ac117-0001-012",
        "2432029698107829780-242ac117-0001-012",
        "2432201496799669780-242ac117-0001-012",
        "2432845741894069780-242ac117-0001-012",
        "2433962429096062484-242ac117-0001-012",
        "2433962433391029780-242ac117-0001-012",
        "2434005383063989780-242ac117-0001-012",
        "2434348980447669780-242ac117-0001-012",
        "2434434879793589780-242ac117-0001-012",
        "2434520779139509780-242ac117-0001-012",
        "2434821426850229780-242ac117-0001-012",
        "2434864376523189780-242ac117-0001-012",
        "2434907326196149780-242ac117-0001-012",
        "2434950275869109780-242ac117-0001-012",
        "2438643947743669780-242ac117-0001-012",
        "2438686897416629780-242ac117-0001-012",
        "2444012656863669780-242ac117-0001-012",
        "2573763618875829780-242ac117-0001-012",
        "2574021316913589780-242ac117-0001-012",
        "2575223907756469780-242ac117-0001-012",
        "2576383548926389780-242ac117-0001-012",
        "2576898945001909780-242ac117-0001-012",
        "2576984844347829780-242ac117-0001-012",
        "2577371391404469780-242ac117-0001-012",
        "2578616931920309780-242ac117-0001-012",
        "2578659881593269780-242ac117-0001-012",
        "2578702826971262484-242ac117-0001-012",
        "2578702831266229780-242ac117-0001-012",
        "2579218227341749780-242ac117-0001-012",
        "2579347076360629780-242ac117-0001-012",
        "2582611251505589780-242ac117-0001-012",
        "2582654201178549780-242ac117-0001-012",
        "2583255496599989780-242ac117-0001-012",
        "2583899741694389780-242ac117-0001-012",
        "2584629886134709780-242ac117-0001-012",
        "2585746577631669780-242ac117-0001-012",
        "2587979960625589780-242ac117-0001-012",
        "2588022910298549780-242ac117-0001-012",
        "2590170393946549780-242ac117-0001-012",
        "2590428091984309780-242ac117-0001-012",
        "2593090971707829780-242ac117-0001-012",
        "2593606363488382484-242ac117-0001-012",
        "2593606367783349780-242ac117-0001-012",
        "SRR12018279",
        "SRR12018280",
        "SRR12018281",
        "SRR12018282",
        "SRR12018283",
        "SRR12018284",
        "SRR12018285",
        "SRR12018286",
        "SRR12018287",
        "SRR12018288",
        "SRR12018289",
        "SRR12018290",
        "SRR12018291",
        "SRR12018302",
        "SRR12018303",
        "SRR12018304",
        "SRR12018305",
        "SRR12018306",
        "SRR12018309",
        "SRR12018310",
        "SRR12664074",
        "SRR12664075",
        "SRR12664076",
        "SRR12664077",
        "SRR12664078",
        "SRR12664079" ;
    bios:anatomicalStructure [ a schema1:DefinedTerm ;
            schema1:identifier "UBERON:0013756" ;
            schema1:inDefinedTermSet "UBERON" ;
            schema1:name "venous blood" ] ;
    bios:associatedPhenotype [ schema1:name "CD3+ CD4+ CD45RA- CD154+ CD69+" ],
        [ schema1:name "CD3+ CD4+ CD45RA- CD137+ CD69+" ] ;
    bios:collector [ a schema1:Person ;
            schema1:name "La Jolla Institute for Immunology" ],
        [ a schema1:Person ;
            schema1:name "La Jolla Institute for Immunology" ] ;
    bios:developmentalStage [ a schema1:QuantitativeValue ;
            schema1:maxValue 82 ;
            schema1:minValue 22 ;
            schema1:unitCode "UO:0000036" ;
            schema1:unitText "year" ] ;
    bios:sampleProcess "PBMCs from each donor were thawed, washed, plated in 24-well culture plates at a concentration of 5x10^6 cells/mL in 1 mL of serum-free TexMACS medium (Miltenyi Biotec) and left overnight (5% CO2, 37C). Cells were sequentially stained with fluorescence-labeled surface antibodies, Cell-hashtag TotalSeq-C antibody (0.5 mg/condition), and a biotin-conjugated CD154 antibody (clone 5C8; Miltenyi Biotec) followed by anti-biotin microbeads (Miltenyi Biotec). Labeled cells were added to MS columns (Miltenyi Biotec) and positively selected cells (CD154+) were eluted and used for FACS sorting with a FACSAria Fusion Cell Sorter (Becton Dickinson). Up to 60,000 cells from individual donors were pooled by sorting into low retention 1.5 mL collection tubes, containing 500 ml of a 1:1 solution of PBS:FBS supplemented with recombinant RNase inhibitor (1:100, Takara). Following sorting, ice-cold PBS was added to make up to a volume of 1400 ml. Cells were then centrifuged for 5 min (600 g at 4C) and the supernatant was removed leaving 5 to 10 ml. 25 ml of resuspension buffer (0.22 mm filtered ice-cold PBS supplemented with ultra-pure bovine serum albumin; 0.04%, Sigma-Aldrich) was added to the tube and the pellet was resuspended. Following mixing, 33 ml of the cell suspension was transferred to a PCR-tube for processing as per the manufacturer’s instructions (10x Genomics).",
        "PBMCs from each donor were thawed, washed, plated in 24-well culture plates at a concentration of 5x10^6 cells/mL in 1 mL of serum-free TexMACS medium (Miltenyi Biotec) and left overnight (5% CO2, 37C). Cells were stimulated by the addition of individual virus-specific peptide pools (1 mg/mL) for 6 h in the presence of a blocking CD40 antibody (1 mg/mL; Miltenyi Biotec). Cells were sequentially stained with fluorescence-labeled surface antibodies, Cell-hashtag TotalSeq-C antibody (0.5 mg/condition), and a biotin-conjugated CD154 antibody (clone 5C8; Miltenyi Biotec) followed by anti-biotin microbeads (Miltenyi Biotec). Labeled cells were added to MS columns (Miltenyi Biotec) and positively selected cells (CD154+) were eluted and used for FACS sorting with a FACSAria Fusion Cell Sorter (Becton Dickinson). Up to 60,000 cells from individual donors were pooled by sorting into low retention 1.5 mL collection tubes, containing 500 ml of a 1:1 solution of PBS:FBS supplemented with recombinant RNase inhibitor (1:100, Takara). Following sorting, ice-cold PBS was added to make up to a volume of 1400 ml. Cells were then centrifuged for 5 min (600 g at 4C) and the supernatant was removed leaving 5 to 10 ml. 25 ml of resuspension buffer (0.22 mm filtered ice-cold PBS supplemented with ultra-pure bovine serum albumin; 0.04%, Sigma-Aldrich) was added to the tube and the pellet was resuspended. Following mixing, 33 ml of the cell suspension was transferred to a PCR-tube for processing as per the manufacturer’s instructions (10x Genomics).",
        "PBMCs from each donor were thawed, washed, plated in 24-well culture plates at a concentration of 5x10^6 cells/mL in 1 mL of serum-free TexMACS medium (Miltenyi Biotec) and left overnight (5% CO2, 37C). Cells were stimulated by the addition of individual virus-specific peptide pools (1 mg/mL) for 6 h in the presence of a blocking CD40 antibody (1 mg/mL; Miltenyi Biotec). Cells were sequentially stained with fluorescence-labeled surface antibodies, Cell-hashtag TotalSeq-C antibody (0.5 mg/condition), and a biotin-conjugated CD154 antibody (clone 5C8; Miltenyi Biotec) followed by anti-biotin microbeads (Miltenyi Biotec). Labeled cells were added to MS columns (Miltenyi Biotec) for positive selection of CD154+ cells. The flow-through from the column was collected and re-plated to harvest cells responding 24 h after peptide stimulation. Analogous to enrichment for CD154+, CD137-expressing CD4+ memory T cells were positively selected by staining with biotin-conjugated CD137 antibody (clone REA765; Miltenyi Biotec) followed by anti-biotin MicroBeads and applied to a new MS column for sorting with a FACSAria Fusion Cell Sorter (Becton Dickinson). Up to 60,000 cells from individual donors were pooled by sorting into low retention 1.5 mL collection tubes, containing 500 ml of a 1:1 solution of PBS:FBS supplemented with recombinant RNase inhibitor (1:100, Takara). Following sorting, ice-cold PBS was added to make up to a volume of 1400 ml. Cells were then centrifuged for 5 min (600 g at 4C) and the supernatant was removed leaving 5 to 10 ml. 25 ml of resuspension buffer (0.22 mm filtered ice-cold PBS supplemented with ultra-pure bovine serum albumin; 0.04%, Sigma-Aldrich) was added to the tube and the pellet was resuspended. Following mixing, 33 ml of the cell suspension was transferred to a PCR-tube for processing as per the manufacturer’s instructions (10x Genomics).",
        "PBMCs were isolated from up to 80ml of anti-coagulated blood by density centrifugation over Lymphoprep (Axis-Shield PoC AS, Oslo, Norway) and cryopreserved in 50% decomplemented human antibody serum, 40% complete RMPI 1640 medium and 10% DMSO.",
        "Single cell: True",
        "none" ;
    bios:sampleQuantity [ a schema1:QuantitativeValue ;
            schema1:maxValue 1 ;
            schema1:minValue 1 ;
            schema1:name "cells_per_reaction" ],
        [ a schema1:QuantitativeValue ;
            schema1:maxValue 13409 ;
            schema1:minValue 1346 ;
            schema1:name "cell_number" ] ;
    bios:sampleState "Live cells as determined by Fixable Viability Dye eFluor 780 (eBioscience)",
        "complete+untemplated" ;
    bios:sampleType [ a schema1:DefinedTerm ;
            schema1:name "peripheral venous puncture" ],
        [ a schema1:DefinedTerm ;
            schema1:name "RNA" ] ;
    bios:sex "pooled" ;
    nde:cellType [ a schema1:DefinedTerm ;
            schema1:identifier "CL:0000897" ;
            schema1:inDefinedTermSet "CL" ;
            schema1:name "CD4-positive, alpha-beta memory T cell" ] ;
    nde:species [ a schema1:DefinedTerm ;
            schema1:identifier "NCBITAXON:9606" ;
            schema1:inDefinedTermSet "NCBITAXON" ;
            schema1:name "Homo sapiens" ],
        [ a schema1:DefinedTerm ;
            schema1:identifier "NCBITAXON:9606" ;
            schema1:inDefinedTermSet "NCBITAXON" ;
            schema1:name "Homo sapiens" ] .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: Bioschemas Sample properties
description: 'Properties of a biological sample from the Bioschemas Sample draft (https://bioschemas.org/),
  in the bios: namespace. A node using them is typed with bios:Sample beside its own
  type. Every property accepts one value or an array, because framing collapses a
  one-element array to its value. Ranges follow the Bioschemas draft where it gives
  one, and allow text where real records use text for a term.'
type: object
properties:
  '@type':
    anyOf:
    - type: string
    - type: array
      items:
        type: string
  bios:anatomicalStructure:
    description: The organ or tissue the sample was collected from.
    $ref: '#/$defs/termsOrText'
    x-jsonld-id: https://bioschemas.org/anatomicalStructure
  bios:anatomicalSystem:
    description: The anatomical system the sample was collected from, e.g. circulatory,
      digestive, immune.
    $ref: '#/$defs/termsOrText'
    x-jsonld-id: https://bioschemas.org/anatomicalSystem
  bios:associatedPhenotype:
    description: Defining characteristics expressed by the biological source of the
      sample.
    $ref: '#/$defs/termsOrText'
    x-jsonld-id: https://bioschemas.org/associatedPhenotype
  bios:collectionMethod:
    description: Conditions and methods of acquisition of the sample.
    $ref: '#/$defs/termsOrText'
    x-jsonld-id: https://bioschemas.org/collectionMethod
  bios:collector:
    description: The Person or Organization who collected the sample.
    anyOf:
    - $ref: '#/$defs/agent'
    - type: array
      items:
        $ref: '#/$defs/agent'
    x-jsonld-id: https://bioschemas.org/collector
  bios:dateCollected:
    description: The date the sample was collected.
    $ref: '#/$defs/dates'
    x-jsonld-id: https://bioschemas.org/dateCollected
  bios:dateProcessed:
    description: The date the sample was processed or used in a method.
    $ref: '#/$defs/dates'
    x-jsonld-id: https://bioschemas.org/dateProcessed
  bios:developmentalStage:
    description: The age or developmental stage of the source when the sample was
      created, as a term or a quantity.
    anyOf:
    - $ref: '#/$defs/termOrQuantity'
    - type: array
      items:
        $ref: '#/$defs/termOrQuantity'
    x-jsonld-id: https://bioschemas.org/developmentalStage
  bios:environmentalSystem:
    description: The habitat or ecosystem where the sample was collected.
    $ref: '#/$defs/termsOrText'
    x-jsonld-id: https://bioschemas.org/environmentalSystem
  bios:experimentalPurpose:
    description: The planned or executed experimental procedures involving the sample.
    $ref: '#/$defs/termsOrText'
    x-jsonld-id: https://bioschemas.org/experimentalPurpose
  bios:isControl:
    description: Whether the sample is used as a normal control.
    type: boolean
    x-jsonld-id: https://bioschemas.org/isControl
  bios:locationOfOrigin:
    description: The location from which the sample was originally collected.
    $ref: '#/$defs/termsOrText'
    x-jsonld-id: https://bioschemas.org/locationOfOrigin
  bios:sampleAvailability:
    description: Whether the sample is available for reuse.
    anyOf:
    - type: boolean
    - $ref: '#/$defs/termsOrText'
    x-jsonld-id: https://bioschemas.org/sampleAvailability
  bios:sampleProcess:
    description: The processing technique applied to the sample.
    $ref: '#/$defs/termsOrText'
    x-jsonld-id: https://bioschemas.org/sampleProcess
  bios:sampleQuantity:
    description: The size of the sample.
    $ref: '#/$defs/quantities'
    x-jsonld-id: https://bioschemas.org/sampleQuantity
  bios:sampleState:
    description: The condition, composition or state of the sample, e.g. dried, frozen.
    $ref: '#/$defs/termsOrText'
    x-jsonld-id: https://bioschemas.org/sampleState
  bios:sampleStorageTemperature:
    description: The temperature at which the sample is stored.
    $ref: '#/$defs/quantities'
    x-jsonld-id: https://bioschemas.org/sampleStorageTemperature
  bios:sampleType:
    description: The type of sample, intentionally broad (cells, rock, sand).
    $ref: '#/$defs/termsOrText'
    x-jsonld-id: https://bioschemas.org/sampleType
  bios:sex:
    description: The biological sex of the individual the sample was obtained from.
    $ref: '#/$defs/termsOrText'
    x-jsonld-id: https://bioschemas.org/sex
  bios:studyID:
    description: The identifier of the study the sample belongs to.
    $ref: '#/$defs/texts'
    x-jsonld-id: https://bioschemas.org/studyID
  bios:studyTitle:
    description: The title of the study the sample belongs to.
    $ref: '#/$defs/texts'
    x-jsonld-id: https://bioschemas.org/studyTitle
  bios:project:
    description: The project the sample belongs to.
    $ref: '#/$defs/termsOrText'
    x-jsonld-id: https://bioschemas.org/project
$defs:
  texts:
    anyOf:
    - type: string
    - type: array
      items:
        type: string
  dates:
    anyOf:
    - $ref: '#/$defs/date'
    - type: array
      items:
        $ref: '#/$defs/date'
  date:
    type: string
    pattern: ^\d{4}(-\d{2}(-\d{2})?)?([T ].*)?$
  term:
    description: A defined term, or a reference to one. It must name or identify the
      term.
    type: object
    properties:
      '@id':
        type: string
      '@type':
        anyOf:
        - type: string
        - type: array
          items:
            type: string
      schema:name:
        anyOf:
        - type: string
        - type: array
          items:
            type: string
        x-jsonld-id: http://schema.org/name
      schema:identifier:
        type: string
        x-jsonld-id: http://schema.org/identifier
      schema:url:
        type: string
        x-jsonld-id: http://schema.org/url
      schema:inDefinedTermSet:
        type: string
        x-jsonld-id: http://schema.org/inDefinedTermSet
      schema:termCode:
        type: string
        x-jsonld-id: http://schema.org/termCode
    anyOf:
    - required:
      - schema:name
    - required:
      - schema:identifier
    - required:
      - '@id'
  termOrText:
    anyOf:
    - type: string
    - $ref: '#/$defs/term'
  termsOrText:
    anyOf:
    - $ref: '#/$defs/termOrText'
    - type: array
      items:
        $ref: '#/$defs/termOrText'
  quantity:
    description: A schema:QuantitativeValue; a range uses minValue and maxValue.
    type: object
    properties:
      '@type':
        anyOf:
        - type: string
        - type: array
          items:
            type: string
      schema:value:
        type:
        - number
        - string
        x-jsonld-id: http://schema.org/value
      schema:minValue:
        type: number
        x-jsonld-id: http://schema.org/minValue
      schema:maxValue:
        type: number
        x-jsonld-id: http://schema.org/maxValue
      schema:unitText:
        type: string
        x-jsonld-id: http://schema.org/unitText
      schema:unitCode:
        type: string
        x-jsonld-id: http://schema.org/unitCode
      schema:name:
        type: string
        x-jsonld-id: http://schema.org/name
  quantities:
    anyOf:
    - $ref: '#/$defs/quantity'
    - type: array
      items:
        $ref: '#/$defs/quantity'
  termOrQuantity:
    anyOf:
    - $ref: '#/$defs/termOrText'
    - $ref: '#/$defs/quantity'
  agent:
    type: object
    properties:
      '@type':
        anyOf:
        - type: string
        - type: array
          items:
            type: string
      schema:name:
        type: string
        x-jsonld-id: http://schema.org/name
    required:
    - schema:name
x-jsonld-prefixes:
  schema: http://schema.org/
  bios: https://bioschemas.org/
x-bblocks-metadata:
  itemIdentifier: cdif.bbr.metadata.bioschemasProperties.bioschemasSample
  register: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/register.json
  version: '0.1'
  dateOfLastChange: '2026-11-13'

```

Links to the schema:

* YAML version: [schema.yaml](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/bioschemasProperties/bioschemasSample/schema.json)
* JSON version: [schema.json](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/bioschemasProperties/bioschemasSample/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "schema": "http://schema.org/",
    "bios": "https://bioschemas.org/",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/bioschemasProperties/bioschemasSample/context.jsonld)

## Sources

* [Bioschemas types and properties (draft) for the Data Discovery Engine](https://github.com/BioSchemas/bioschemas-dde)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/Cross-Domain-Interoperability-Framework/metadataBuildingBlocks](https://github.com/Cross-Domain-Interoperability-Framework/metadataBuildingBlocks)
* Path: `_sources/bioschemasProperties/bioschemasSample`

