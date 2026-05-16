## CDIF Reference

Defines a typed reference to an external entity for use within CDIF metadata. A `cdif:Reference` combines three things:

1. The schema.org `CreativeWork` surface inherited from `schemaorgProperties/labeledLink` — a human-readable `schema:name`, `schema:description`, and required `schema:url`.
2. The DDI-CDI `dt-Reference` semantics — `cdi:uri` for the canonical machine-readable identifier of the referenced entity (which may differ from a presentation URL), and `cdi:description` for the DDI-CDI-style description.
3. An optional `cdif:semantic` slot expressing the *role* of this reference as a [SKOS Concept](https://www.w3.org/TR/skos-reference/) — for example, distinguishing a reference to a physical sample from a reference to its registration metadata (see [Discovery issue 13](https://github.com/Cross-Domain-Interoperability-Framework/Discovery/issues/13)).

### When to use

Prefer `cdif:Reference` over `schemaorgProperties/labeledLink` whenever a reference needs:

- An explicit **semantic role** beyond "labeled link" (use `cdif:semantic`).
- A **distinct identifier** for the referenced entity separate from a presentation URL (use `cdi:uri`).
- Round-trippability with the DDI-CDI `dt-Reference` data type.

Continue to use `labeledLink` directly when the reference is a plain hyperlink and no semantic role is required.

### Required properties

- `@type` must contain `cdif:Reference` (and inherits the `schema:CreativeWork` requirement from labeledLink, so `@type` is typically `["schema:CreativeWork", "cdif:Reference"]`).
- `schema:url` is required (inherited from labeledLink).

All other properties are optional.

### Type declaration

JSON-LD instance documents that conform to this building block must declare `cdif:Reference` (rather than the previous `cdi:Reference`) in the `@type` array. The CDIF profile now owns the `Reference` concept; the `cdif:` namespace makes that ownership explicit and lets the SHACL rule below target it without conflicting with DDI-CDI's native `cdi:Reference` definition.

### Relationship to DDI-CDI

DDI-CDI defines `dt-Reference` as a DataType with attributes including a URI and a description. CDIF promotes this concept to a profile-level type (`cdif:Reference`) so that profile validators can target it directly via SHACL and so cross-profile UML can reference one canonical class. The `cdi:` attribute names are retained to preserve the round-trip with DDI-CDI source models; only the *type label* has been re-namespaced.
