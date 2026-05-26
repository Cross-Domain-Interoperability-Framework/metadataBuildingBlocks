Defines the structure for a DataDownload distribution that is an archive file (e.g. ZIP, tar.gz) containing multiple component files. The archive itself is typed as `schema:DataDownload` with standard properties (name, contentUrl, encodingFormat, checksum). Component files within the archive are listed in `schema:hasPart` and typed as `schema:MediaObject` (not `schema:DataDownload`, since they are not independently accessible via URL).

Each hasPart item has:
- `@id` --identifier for cross-references (e.g. from metadata sidecar files via `schema:about`)
- `@type` --must include `schema:MediaObject`, must not include `schema:DataDownload`
- `schema:name` --filename within the archive
- `schema:encodingFormat` --MIME type(s)
- `schema:size` --file size as `schema:QuantitativeValue`
- `schema:description` --description of file content
- `schema:about` --references to related files (for metadata sidecars)
- `spdx:checksum` --integrity checksum

Component files may optionally include CDIF data description extensions to describe their internal data structure:
- `cdifTabularData` --for delimited or fixed-width tabular text files (CSV, TSV), with CSVW properties and physical column mappings
- `cdifDataCube` --for multi-dimensional structured datasets (NetCDF, HDF5), with locator-based physical mappings
