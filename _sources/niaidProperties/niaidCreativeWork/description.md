## NIAID creative work

A schema:CreativeWork or ScholarlyArticle cited by or citing a dataset, with the NIAID Data Discovery Portal's PubMed id, DOI and journal names.

Used by [`niaidDataset`](../niaidDataset/) for `schema:citation` and `nde:citedBy` on a dataset. The
[`cdifNIAID`](../../profiles/cdifCompositeProfile/cdifNIAID/) profile composes
`niaidDataset` with `cdifCore`. `converters/NIAID/harvest_niaid_to_cdif.py` produces
these objects, and gives the type to one the portal left untyped.

| Property | Value | Meaning |
|---|---|---|
| `nde:pmid` | text, digits | The PubMed id |
| `nde:doi` | text | The DOI, as the portal gives it |
| `nde:journalName` | text | The journal's name |
| `nde:journalNameAbbrev` | text | The journal's abbreviated name |

CDIF's own citation rules come from cdifCore; this block adds only the NIAID properties and the type.
