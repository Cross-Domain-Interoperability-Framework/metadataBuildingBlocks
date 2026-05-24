# CDIF DataFingerprint

A fingerprint (checksum / hash) of a physical dataset, used to verify integrity. DDI-CDI
`DataFingerprint` datatype.

- `cdi:value` (required) — the fingerprint value (e.g., hex digest)
- `cdi:algorithmSpecification` — algorithm name/spec (e.g., SHA-256, MD5)
- `cdi:algorithmVersion` — version of the algorithm/specification
- `cdi:typeOfFingerprint` — kind of fingerprint (checksum, hash, digest, …)

Carried on a `cdi:PhysicalDataSet` (a `schema:DataDownload` distribution) via
`cdi:fingerprint` (added by the CDIF Data Description profile's DataDownload branch).
