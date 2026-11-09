## NIAID data catalog

A schema:DataCatalog that a NIAID Data Discovery Portal dataset comes from, with where the dataset is archived there and the version of the catalog the portal harvested.

Used by [`niaidDataset`](../niaidDataset/) for `schema:includedInDataCatalog` on a dataset. The
[`cdifNIAID`](../../profiles/cdifCompositeProfile/cdifNIAID/) profile composes
`niaidDataset` with `cdifCore`. `converters/NIAID/harvest_niaid_to_cdif.py` produces
these objects, and gives the type to one the portal left untyped.

| Property | Value | Meaning |
|---|---|---|
| `schema:archivedAt` | URL | The dataset's page in this catalog (a schema.org property the portal uses here) |
| `nde:versionDate` | date | The version of the catalog the portal harvested |
