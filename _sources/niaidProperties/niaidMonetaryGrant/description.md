## NIAID monetary grant

A schema:MonetaryGrant with the NIAID Data Discovery Portal's breakdown of an NIH project number into its parts. Extends the monetaryGrant block.

Used by [`niaidDataset`](../niaidDataset/) for `schema:funding` on a dataset. The
[`cdifNIAID`](../../profiles/cdifCompositeProfile/cdifNIAID/) profile composes
`niaidDataset` with `cdifCore`. `converters/NIAID/harvest_niaid_to_cdif.py` produces
these objects, and gives the type to one the portal left untyped.

| Property | Value | Meaning |
|---|---|---|
| `cdifniaid:projectNumSplit` | object | The parts of an NIH project number such as `5R01AI012345-03`: `cdifniaid:applTypeCode` (5), `activityCode` (R01), `icCode` (AI), `serialNum`, `supportYear`, `fullSupportYear`, `suffixCode` |
