
# Object Reference (Schema)

`cdif.bbr.metadata.cdifDataType.objectReference` *v0.1*

Canonical strict JSON-LD node reference: an object carrying only @id (and optionally @type).

[*Status*](http://www.opengis.net/def/status): Under development

## Description

## Object Reference

The canonical strict reference to a node defined elsewhere in the graph, carried as an object with only an `@id` (and optionally an `@type`). Because it sets `additionalProperties: false`, it stops a lenient reference branch from swallowing inline objects that happen to also carry an `@id`. Use it wherever a slot must hold a pointer to another node rather than an inline definition.

## Examples

### Bare object reference
A reference to a node defined elsewhere, carrying only its @id.
#### json
```json
{
  "@id": "https://example.org/thing/123"
}

```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: Object Reference
description: A reference to a node defined elsewhere, by its @id.
type: object
properties:
  '@id':
    type: string
    description: resolvable @id of the referenced node
required:
- '@id'
additionalProperties: false

```

Links to the schema:

* YAML version: [schema.yaml](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifDataType/objectReference/schema.json)
* JSON version: [schema.json](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifDataType/objectReference/schema.yaml)


# JSON-LD Context

```jsonld
None
```

You can find the full JSON-LD context here:
[context.jsonld](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/_sources/cdifDataType/objectReference/context.jsonld)

## Sources

* [CDIF book](https://cross-domain-interoperability-framework.github.io/cdifbook/metadata/schemaorgimplementation.html#schema-org-implementation-of-cdif-metadata)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/Cross-Domain-Interoperability-Framework/metadataBuildingBlocks](https://github.com/Cross-Domain-Interoperability-Framework/metadataBuildingBlocks)
* Path: `_sources/cdifDataType/objectReference`

