## NIAID place

A schema:Place from the NIAID Data Discovery Portal's spatial coverage, with NIAID's administrative type.

Used by [`niaidDataset`](../niaidDataset/) for `schema:spatialCoverage` on a dataset. The
[`cdifNIAID`](../../profiles/cdifCompositeProfile/cdifNIAID/) profile composes
`niaidDataset` with `cdifCore`. `converters/NIAID/harvest_niaid_to_cdif.py` produces
these objects, and gives the type to one the portal left untyped.

| Property | Value | Meaning |
|---|---|---|
| `nde:administrativeType` | text | The kind of administrative area, e.g. `country` |

The portal's `country` (given only by Project Tycho, on areas named by ISO 3166 code) becomes the place's name, and its `locationType` the name term's `schema:about`, so neither appears here.
