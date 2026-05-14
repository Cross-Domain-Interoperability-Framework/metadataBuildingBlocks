# CDIF Statistics

CDIF profile of the DDI-CDI **Statistics**, **CategoryStatistics**, and **StatisticsCollection** classes (2026-03 model). Used to attach computed summary values (counts, means, quantiles, etc.) to a dataset, a variable, or a category of values within a variable.

## CDIF divergences from canonical DDI-CDI

- Properties valued by `InternationalString` / `LabelForDisplay` / `ObjectName` in DDI-CDI are simplified to plain strings and carried under the `cdif:` namespace — here, on `cdi:Category`: `cdif:name`, `cdif:descriptiveText`, `cdif:definition`, `cdif:displayLabel`.
- The polymorphic `cdi:has` association is split into target-specific keys: `cdif:has_CategoryStatistics` (on `Statistics`) and `cdif:has_Statistics` (on `StatisticsCollection`).
- `cdif:appliesTo` and `cdif:indexedBy` are CDIF additions — they link statistics to the `InstanceVariable`(s) they describe and are **not** present in the canonical DDI-CDI model.

## Classes

### `cdi:Statistic` (dataType)

A single computed value. A value object — no identity, always appears inline inside a `cdi:statistic` array. Properties:

- `cdi:computationBase` — the cases included in the computation: `Total` (all cases), `ValidOnly` (valid values only), `MissingOnly` (invalid cases only).
- `cdi:content` — the numeric value of the statistic.
- `cdi:isWeighted` — `true` when the value was computed using a weighting variable; default `false`.
- `cdi:typeOfNumericValue` — the numeric type of `cdi:content` — `decimal`, `float`, or `double`.

### `cdi:Statistics`

A named bundle of one or more `cdi:Statistic` value objects for an instance variable. Properties:

- `@id` — optional identifier.
- `@type` — must contain `cdi:Statistics`.
- `cdi:typeOfStatistic` — the kind of statistic (mean, median, count, …) for the whole bundle.
- `cdi:statistic` — ordered array of one or more inline `Statistic` objects (required).
- `cdi:hasWeight` — `cdi:InstanceVariable` whose values were used as weights (inline or `@id`-ref).
- `cdif:appliesTo` — CDIF addition: the `InstanceVariable`(s) this bundle summarizes.
- `cdif:has_CategoryStatistics` — array of `CategoryStatistics` entries for per-category breakdowns.

### `cdi:CategoryStatistics`

Statistics for a specific `cdi:Category` of an instance variable.

- `cdi:for` — the `Category` (inline or `@id`-ref) (required).
- `cdi:typeOfStatistic` — the kind of statistic.
- `cdi:statistic` — per-category `Statistic` value objects (required).
- `cdi:hasWeight` — the weighting `InstanceVariable`.

### `cdi:StatisticsCollection`

Groups multiple `Statistics` nodes for an instance variable. Properties:

- `@id` — optional identifier.
- `@type` — must contain `cdi:StatisticsCollection`.
- `cdif:has_Statistics` — array of one or more `Statistics` nodes (inline or `@id`-ref) (required).
- `cdif:indexedBy` — CDIF addition: the `InstanceVariable`(s) the contained statistics index — the collection-level coordinate space.
- `cdi:hasWeight` — the weighting `InstanceVariable`.

### `cdi:Category`

Minimal Category shape used as a `CategoryStatistics` target, carrying the `cdif:`-namespaced simplified string properties (`cdif:name`, `cdif:descriptiveText`, `cdif:definition`, `cdif:displayLabel`). Full category modelling lives in `cdifEnumerationDomain` / SKOS Concept.

## Usage

The root of this building block validates **any of** a `Statistics`, `CategoryStatistics`, or `StatisticsCollection` node (via `anyOf`). External building blocks compose individual `$defs` (e.g. `cdifStatistics/schema.yaml#/$defs/Statistics`) when only one shape is needed.
