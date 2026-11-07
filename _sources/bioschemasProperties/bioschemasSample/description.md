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
