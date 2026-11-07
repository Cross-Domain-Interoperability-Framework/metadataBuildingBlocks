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

### NIAID terms

| Property | On | Value |
|---|---|---|
| `nde:date` | dataset | The portal's summary date |
| `nde:species`, `nde:topicCategory` | dataset | Annotated terms |
| `nde:nctid` | dataset | ClinicalTrials.gov id, `NCT` and eight digits |
| `nde:citedBy` | dataset | Works citing the dataset |
| `nde:curatedBy` | dataset, term | Who curated it, with `nde:versionDate` |
| `nde:isRelatedTo`, `nde:isBasisFor` | dataset | Related resources, with `nde:relationship` |
| `nde:sample` | dataset | An `nde:Sample` or `nde:SampleCollection` |
| `nde:isCurated`, `nde:originalName` | term | Whether a curator checked the term, and the text it was matched from |
| `nde:doi`, `nde:pmid`, `nde:journalName` | work | Identifiers and journal of a cited work |
| `nde:cellType` | sample | Term or text |

NIAID's annotations also appear on CDIF's own `schema:infectiousAgent`,
`schema:healthCondition`, `schema:measurementTechnique` and
`schema:variableMeasured`.

### cdifniaid terms

| Term | On | Definition |
|---|---|---|
| `cdifniaid:fromGPT` | term | The term was suggested by a GPT language model |
| `cdifniaid:fromPMID` | term, citation, grant | The value was taken from a PubMed record linked to the dataset |
| `cdifniaid:fromEXTRACT` | term | The term was found by the EXTRACT text-mining tool |
| `cdifniaid:fromNCT` | term | The term was taken from the dataset's ClinicalTrials.gov record |
| `cdifniaid:classification` | taxon term | The role the taxon plays, e.g. `infectiousAgent` or `host` |
| `cdifniaid:commonName` | taxon term | Its common name |
| `cdifniaid:displayName` | taxon term | The name the portal displays |
| `cdifniaid:projectNumSplit` | grant | The parts of an NIH project number such as `5R01AI012345-03`: `cdifniaid:applTypeCode` (5), `activityCode` (R01), `icCode` (AI), `serialNum`, `supportYear`, `fullSupportYear`, `suffixCode` |
| `cdifniaid:alternateNames` | agent | Second and later alternate names; `schema:alternateName` holds the first, as CDIF agents take one |
| `cdifniaid:correctionApproved` | source organization | A correction to the portal's record of the project was approved |
| `cdifniaid:country` | place | The country the place is in |
| `cdifniaid:temporalIntervals` | dataset | The portal's intervals where they hold more than dates (a type, a name, a duration), kept whole beside `schema:temporalCoverage` |
| `cdifniaid:unlinkedHasPart` | dataset | Parts with no address, which cannot be CDIF manifest parts |
| `cdifniaid:partUrl` | distribution | Archive members given only as URLs, with no name or format, which CDIF archive parts need |
| `cdifniaid:assayformat` | dataset | The assay format, as the portal gives it |
| `cdifniaid:publication` | dataset | PubMed ids of publications about the dataset |

The `from*` meanings are inferred from the names and where the portal uses them;
NIAID's schema does not define them.
