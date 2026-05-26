# CDIF Key

A **CDIF Key** is the role of an ordered set of `cdi:InstanceVariable`s that uniquely identifies a data instance — typically the primary key of a tabular dataset, but the same shape covers any composite identifier role.

This is a CDIF profile of DDI-CDI's `Key` / `PrimaryKey` concept. Where the canonical DDI-CDI form composes a Key from `cdi:DataStructureComponent` nodes, the CDIF profile composes it from `cdi:InstanceVariable` nodes (referenced through the `cdifInstanceVariable` building block) so the Key references the actual measured variables rather than an intermediate component layer.

## Structure

- `@type` must contain `"cdif:Key"`.
- `cdif:isComposedOf` is an ordered array of one or more `cdif:ComponentPosition` entries.
- Each `cdif:ComponentPosition` carries:
  - `cdif:indexes` — the `cdi:InstanceVariable` (inline `cdifInstanceVariable` node, or an `@id`-only reference);
  - `cdif:value` — an integer indicating the position of this component within the key, counting upward from `0` or `1`.

The `cdif:value` ordering matters for composite (multi-column) keys: it determines the canonical sort/lookup order so that `(year, country)` and `(country, year)` keys are distinguishable.
