## CDIF Manifest

Profile module for **packages**: the resources that make up a dataset, and where to retrieve each
of them. Marks the catalog record as conformant to `https://w3id.org/cdif/manifest/2.0`.

It declares `schema:hasPart` in the two places a package needs it:

- **On the Dataset** — for parts that are independently accessible at their own addresses.
- **On a `schema:distribution` item** — for component files inside an archive (ZIP, etc.) that
  have no address of their own.

Both part shapes carry `schema:about`, so a part that describes another — a codebook, a data
dictionary, a metadata sidecar — can say which one it describes.

### What it does *not* add

This module **adds no new `schema:distribution` branch.** The base
`schema:distribution` `anyOf [DataDownload, WebAPI]` is contributed by
[cdifCore](../cdifCore/) and is preserved as-is; this module only adds property constraints on top
of it. The previous `cdifProfile/cdifArchive` building block, which held only the `$defs` for
`ArchivePart`, was **merged into this module** — everything now lives here, and there is no
separate archive BB to reference.

### Note on the two `hasPart` positions

The distinction above is load-bearing beyond documentation. `schema:hasPart` carries several
meanings across CDIF, and a SHACL shape selected by `schema:Dataset` will otherwise reach the
component files listed inside an archive distribution and demand an identifier, a licence and a
landing page of each — metadata that cannot exist for a file nobody can fetch separately. A member
dataset of a collection *is* an independently documented resource; a component inside a ZIP is not.
