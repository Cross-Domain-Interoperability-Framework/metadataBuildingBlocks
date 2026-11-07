## NIAID defined term

A schema:DefinedTerm with the annotations the NIAID Data Discovery Portal adds to the terms it attaches to a dataset: whether a curator checked the term, the text it was matched from, who curated it, and a taxon's common name. The annotations occur only on DefinedTerms, so the block requires that type.

Used by [`niaidDataset`](../niaidDataset/) for `nde:species`, `nde:topicCategory`, `schema:infectiousAgent`, `schema:healthCondition`, `schema:measurementTechnique` and `schema:variableMeasured` on a dataset, and `nde:species` on a sample. The
[`cdifNIAID`](../../profiles/cdifCompositeProfile/cdifNIAID/) profile composes
`niaidDataset` with `cdifCore`. `converters/NIAID/harvest_niaid_to_cdif.py` produces
these objects, and gives the type to one the portal left untyped.

| Property | Value | Meaning |
|---|---|---|
| `nde:isCurated` | boolean | Whether a curator checked the term against its source text |
| `nde:originalName` | text | The text in the source record the term was matched from |
| `nde:curatedBy` | agent | Who or what produced or checked the annotation, often software (PubTator, GPT-4o-mini, the Biothings API) |
| `cdifniaid:commonName` | text | A taxon's common name, e.g. Human |

The portal also puts `fromGPT`, `fromPMID`, `fromEXTRACT` and `fromNCT` flags, `classification` and `displayName` on terms. The converter turns the flags into one sentence on the catalog record's description, `classification` into a keyword and `displayName` into `schema:alternateName`, so none of them appear here.
