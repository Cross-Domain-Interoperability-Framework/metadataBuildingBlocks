DDI-CDI **Statistics** covers summary and category statistics computed for an instance variable within a data set. Generated from the 2026-03 DDI-CDI model (`DataDescription` / `FormatDescription` packages).

The root validates any of three concrete classes:

- **`cdi:Statistics`** — a bundle of `cdi:Statistic` values for an instance variable, with `cdi:typeOfStatistic` (count, mean, median, …) and an optional `cdi:hasWeight` reference to the weighting `InstanceVariable`.
- **`cdi:CategoryStatistics`** — statistics for a specific `cdi:Category` of an instance variable; carries `cdi:appliesTo` (the `InstanceVariable`), `cdi:for` (the `Category`), and a `cdi:statistic` list.
- **`cdi:StatisticsCollection`** — groups summary and category statistics for an instance variable.

Supporting `$defs`: `cdi:Statistic` (the value object — `cdi:content`, `cdi:computationBase`, `cdi:isWeighted`, `cdi:typeOfNumericValue`) and `cdi:Category`.

This is the canonical `ddiProperties` counterpart to the CDIF schema.org `cdifStatistics` building block.
