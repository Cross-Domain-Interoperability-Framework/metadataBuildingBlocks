## CDIF Relation

A typed relation describing a link to another resource. Combines the schema.org labeled-link surface inherited from `schemaorgProperties/labeledLink` (`schema:name`, `schema:description`, required `schema:url`) with the DCAT `dcat:qualifiedRelation` pattern by adding:

1. A second `@type` entry: `dcat:Relationship`, so the node satisfies DCAT-3 consumers expecting a typed Relationship resource.
2. `dcat:hadRole` — the role of the related resource as a `skos:Concept`.
3. `dcterms:relation` — the URI of the related resource (DCAT-canonical pointer to "what is being related to"). Distinct from `schema:url`, which is the presentation URL inherited from `labeledLink`.

### When to use

Use this building block wherever a metadata record needs a typed link to another resource with an explicit role — for example, to express that this dataset is a version of another dataset, derives from a source sample, or points at a sample-registration record (see [Discovery issue 13](https://github.com/Cross-Domain-Interoperability-Framework/Discovery/issues/13)). It is the target shape for `dcat:qualifiedRelation` on a `dcat:Resource`.

### Required properties

- `@type` must contain both `schema:CreativeWork` (inherited from `labeledLink`) and `dcat:Relationship` — typically `["schema:CreativeWork", "dcat:Relationship"]`.
- `schema:url` is required (inherited from `labeledLink`).

All other properties are optional.

### Relationship to upstream vocabularies

- `dcat:Relationship` (DCAT 3) is a class describing a qualified relationship between two resources. It is the target of `dcat:qualifiedRelation` on a `dcat:Resource`.
- `dcat:hadRole` carries a `dcat:Role` or `skos:Concept` describing the role the related resource plays.
- `dcterms:relation` is the dcterms (also written `dct:`) canonical pointer to the related resource.

### Note on the building-block name

The building-block directory is named `cdifReference` for historical reasons (it began life as a typed reference combining schema.org and DDI-CDI `dt-Reference` semantics). The DDI-CDI surface has been retired; the BB now models a DCAT-flavoured `cdif:Relation`. The folder name is retained so the 7 downstream BBs that `$ref` this schema continue to resolve.
