
# CDIF Concept or Term or String (Schema)

`cdif.bbr.metadata.cdifDataType.cdifConceptOrTermOrString` *v0.1*

Shared union shape for a CDIF property that accepts either a controlled-vocabulary value (SKOS concept @id-ref, schema:DefinedTerm, or inline cdif:Concept — the cdifConceptOrTerm union) OR a plain string label. Consolidates 22 previously-inline 'anyOf: [string, cdifConceptOrTerm]' (and 2 'anyOf: [string, DefinedTerm]') sites across cdifCore, cdifDiscovery, cdifInstanceVariable, cdifRepresentedVariable, cdifDataStructureComponent, cdifStatistics, cdifReference, cdifOpenApi, plus schemaorgProperties/agentInRole (roleName) and schemaorgProperties/organization (additionalType items).

[*Status*](http://www.opengis.net/def/status): Under development

## Description

## CDIF Concept or Term or String

A shared union shape used wherever a CDIF property accepts **either a controlled-vocabulary value or a plain string label**. The value can be any of:

1. **A plain string** — a legacy or single-word label not (yet) bound to a controlled vocabulary. Consumers should treat it as an opaque label, not a URI or notation.
2. **A SKOS concept referenced by URI** — an object carrying just an `@id` pointing at a `skos:Concept` in some published vocabulary.
3. **A `schema:DefinedTerm`** — the schema.org DefinedTerm shape (`schemaorgProperties/definedTerm`), used to inline `name` / `identifier` / `termCode` alongside an `inDefinedTermSet` pointer.
4. **An inline `cdif:Concept`** — the `cdifConcept` shape from the CDIF ConceptScheme profile, used to inline a complete concept definition (preferred label, alternate labels, definition, broader/narrower, etc.).

The last three branches are inherited from [`cdifConceptOrTerm`](../cdifConceptOrTerm/) — this building block wraps that union with the plain-string alternative.

### When to use

`$ref` this building block from any property that used to be declared as either:

- `anyOf: [type: string, $ref: ../cdifConceptOrTerm/schema.yaml]` (the ~20 sites across `cdifCore`, `cdifDiscovery`, `cdifInstanceVariable`, `cdifRepresentedVariable`, `cdifDataStructureComponent`, `cdifStatistics`, `cdifReference`, `cdifOpenApi`), or
- `anyOf: [type: string, $ref: .../schemaorgProperties/definedTerm/schema.yaml]` (the 2 sites in `schemaorgProperties/agentInRole` `schema:roleName` and `schemaorgProperties/organization` `schema:additionalType` items).

Consolidating to this single shared shape simplifies the JSON Schema surface, standardizes the accepted value set (`schemaorgProperties`-only sites gain the concept-ref and inline-cdifConcept alternatives), and gives an XMI→JSON generator a single named union type to recognize.

### Migration note

Prior to 2026-07-03, this union was inlined at 22 property definitions. Each of those `anyOf` blocks is now a single-line `$ref` delegation to this BB; any downstream tool that previously matched the raw four-branch `anyOf` should now match the `$ref` (or, after resolution, still see the same four alternatives).

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: CDIF Concept-or-Term-or-String
description: Shared shape for a CDIF property that carries either a controlled-vocabulary
  value or a bare string label. Wraps cdifConceptOrTerm (SKOS-concept @id-ref, schema:DefinedTerm,
  or inline cdif:Concept) with a plain-string alternative used for legacy or single-word
  labels not yet bound to a vocabulary.
anyOf:
- type: string
- $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifDataType/cdifConceptOrTerm/schema.yaml

```

Links to the schema:

* YAML version: [schema.yaml](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifDataType/cdifConceptOrTermOrString/schema.json)
* JSON version: [schema.json](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifDataType/cdifConceptOrTermOrString/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "schema": "http://schema.org/",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifDataType/cdifConceptOrTermOrString/context.jsonld)

## Sources

* [CDIF Concept or Term (cdifConceptOrTerm)](../cdifConceptOrTerm/)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/Cross-Domain-Interoperability-Framework/metadataBuildingBlocks](https://github.com/Cross-Domain-Interoperability-Framework/metadataBuildingBlocks)
* Path: `_sources/cdifDataType/cdifConceptOrTermOrString`

