## NIAID dataset properties

The properties that dataset records from the
[NIAID Data Discovery Portal](https://data.niaid.nih.gov/) add to a CDIF dataset.
The [`cdifNIAID`](../../profiles/cdifCompositeProfile/cdifNIAID/) profile
composes this module with `cdifCore`; it does not re-embed `cdifCore`.
`converters/NIAID/harvest_niaid_to_cdif.py` produces records in this form, driven
by `converters/mappings/niaid-to-cdif.sssom.tsv`.

### Namespaces

| Prefix | IRI | Used for |
|---|---|---|
| `nde:` | `https://discovery.biothings.io/ns/nde/` | Terms NIAID's [schema](https://github.com/NIAID-Data-Ecosystem/nde-schemas) declares |
| `bios:` | `https://bioschemas.org/` | Bioschemas terms with the same definition, from [`bioschemasSample`](../../bioschemasProperties/bioschemasSample/) |
| `cdifniaid:` | `https://w3id.org/cdif/niaid/terms/` | Names the portal uses that neither declares, defined below |

The `cdifniaid:` IRIs do not resolve yet; like other `cdif:` terms they are
defined here and nowhere else. They sit under `terms/` so that the profile URI
`https://w3id.org/cdif/niaid/1.0` is never compacted to a `cdifniaid:` CURIE.

### What the module requires

- `schema:includedInDataCatalog`: the repositories the portal aggregates the
  record from.
- A `dcterms:conformsTo` of `https://w3id.org/cdif/niaid/1.0` on the catalog
  record.

Everything else is optional but typed. Every property accepts one value or an
array, because framing collapses a one-element array to its value.

### Extensions of other types

NIAID adds properties to five other types, each in a block that requires the
type. `niaidDataset` points its properties at them.

| Block | Type | NIAID properties | Used for |
|---|---|---|---|
| [`niaidDefinedTerm`](../niaidDefinedTerm/) | `schema:DefinedTerm` | `nde:isCurated`, `nde:originalName`, `nde:curatedBy`, `cdifniaid:commonName` | `nde:species`, `nde:topicCategory`, `schema:infectiousAgent`, `schema:healthCondition`; `schema:measurementTechnique` and `schema:variableMeasured` items that carry an annotation |
| [`niaidMonetaryGrant`](../niaidMonetaryGrant/) | `schema:MonetaryGrant` | `cdifniaid:projectNumSplit`, the funder's `cdifniaid:alternateNames` | `schema:funding` |
| [`niaidCreativeWork`](../niaidCreativeWork/) | `schema:CreativeWork` or `schema:ScholarlyArticle` | `nde:pmid`, `nde:doi`, `nde:journalName`, `nde:journalNameAbbrev` | `schema:citation` and `nde:citedBy` items that carry one of them |
| [`niaidPlace`](../niaidPlace/) | `schema:Place` | `nde:administrativeType` | `schema:spatialCoverage` |
| [`niaidDataCatalog`](../niaidDataCatalog/) | `schema:DataCatalog` | `nde:versionDate`, `schema:archivedAt` | `schema:includedInDataCatalog` |

### NIAID terms on the dataset

| Property | On | Value |
|---|---|---|
| `nde:date` | dataset | The portal's summary date |
| `nde:species`, `nde:topicCategory` | dataset, sample | NIAID defined terms |
| `nde:nctid` | dataset | ClinicalTrials.gov id, `NCT` and eight digits |
| `nde:citedBy` | dataset | Works citing the dataset |
| `nde:curatedBy` | dataset | The repository that curated the record, with `nde:versionDate` |
| `nde:isRelatedTo`, `nde:isBasisFor` | dataset | Related resources, with `nde:relationship` |
| `nde:sample` | dataset | An `nde:Sample` or `nde:SampleCollection` |
| `nde:cellType` | sample | Term or text |

### cdifniaid terms on the dataset

| Term | On | Definition |
|---|---|---|
| `cdifniaid:correctionApproved` | source organization | A correction to the portal's record of the project was approved |
| `cdifniaid:temporalIntervals` | dataset | The portal's intervals where they hold more than dates (a type, a name, a duration), kept whole beside `schema:temporalCoverage` |
| `cdifniaid:unlinkedHasPart` | dataset | Parts with no address, which cannot be CDIF manifest parts |
| `cdifniaid:assayformat` | dataset | The assay format, as the portal gives it |
| `cdifniaid:publication` | dataset | PubMed ids of publications about the dataset |

The portal's `from*` flags (`fromGPT`, `fromPMID`, `fromEXTRACT`, `fromNCT`) are
not properties here: the converter turns them into one sentence each, "Metadata
source from GPT." and so on, on the catalog record's description. A person's
`role` becomes a `schema:contributor` that is a `schema:Role` holding the person,
CDIF's pattern for roles.
