
# CDIF DataFingerprint building block (Datatype)

`cdif.bbr.metadata.cdifDataType.cdifDataFingerprint` *v0.1*

A fingerprint (checksum/hash) of a physical dataset, for integrity verification. DDI-CDI DataFingerprint datatype carried on a cdi:PhysicalDataSet (schema:DataDownload) via cdi:fingerprint. Defines cdi:value, cdi:algorithmSpecification, cdi:algorithmVersion, cdi:typeOfFingerprint.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

# CDIF DataFingerprint

A fingerprint (checksum / hash) of a physical dataset, used to verify integrity. DDI-CDI
`DataFingerprint` datatype.

- `cdi:value` (required) — the fingerprint value (e.g., hex digest)
- `cdi:algorithmSpecification` — algorithm name/spec (e.g., SHA-256, MD5)
- `cdi:algorithmVersion` — version of the algorithm/specification
- `cdi:typeOfFingerprint` — kind of fingerprint (checksum, hash, digest, …)

Carried on a `cdi:PhysicalDataSet` (a `schema:DataDownload` distribution) via
`cdi:fingerprint` (added by the CDIF Data Description profile's DataDownload branch).

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: Data Fingerprint
description: A fingerprint (checksum/hash) of a physical dataset, used to verify integrity.
  DDI-CDI DataFingerprint datatype, carried on a cdi:PhysicalDataSet (schema:DataDownload
  distribution) via cdi:fingerprint.
type: object
properties:
  cdi:value:
    type: string
    description: The fingerprint value (e.g., the hex digest). DataFingerprint.value.
    x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/value
  cdi:algorithmSpecification:
    type: string
    description: Identifier or name of the algorithm specification (e.g., SHA-256,
      MD5). DataFingerprint.algorithmSpecification.
    x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/algorithmSpecification
  cdi:algorithmVersion:
    type: string
    description: Version of the fingerprint algorithm/specification. DataFingerprint.algorithmVersion.
    x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/algorithmVersion
  cdi:typeOfFingerprint:
    type: string
    description: The kind of fingerprint (e.g., checksum, hash, digest). DataFingerprint.typeOfFingerprint.
    x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/typeOfFingerprint
required:
- cdi:value
x-jsonld-prefixes:
  schema: http://schema.org/
  cdi: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/

```

Links to the schema:

* YAML version: [schema.yaml](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifDataType/cdifDataFingerprint/schema.json)
* JSON version: [schema.json](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifDataType/cdifDataFingerprint/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "schema": "http://schema.org/",
    "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifDataType/cdifDataFingerprint/context.jsonld)

## Sources

* [DDI-CDI 1.0 Specification](https://ddialliance.org/Specification/DDI-CDI/1.0/)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/Cross-Domain-Interoperability-Framework/metadataBuildingBlocks](https://github.com/Cross-Domain-Interoperability-Framework/metadataBuildingBlocks)
* Path: `_sources/cdifDataType/cdifDataFingerprint`

