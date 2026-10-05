DDI-CDI **PhysicalMapping** describes how the values of an `InstanceVariable` are physically represented in a dataset — format, datatype, length, decimal handling, null sequences, and the W3C tabular-data-model parameters.

It is the successor to the DDI-CDI 1.0 `ValueMapping` class. In the 2026-03 DDI-CDI model `ValueMapping` was renamed `PhysicalMapping`, moved into the `FormatDescription` package, and the relationship to the variable was **reversed**: a `PhysicalMapping` now points at the `InstanceVariable` it formats (`cdi:formats`), rather than the variable carrying an outward `has_ValueMapping` link.

## Root

The root validates **any of** the three concrete mapping types:

- **`cdi:PhysicalMapping`** — the base mapping: `cdi:format`, `cdi:physicalDataType`, `cdi:decimalPositions`, `cdi:scale`, `cdi:numberPattern`, `cdi:defaultValue`, `cdi:nullSequence`, `cdi:isRequired`, `cdi:length` / `cdi:minimumLength` / `cdi:maximumLength`, `cdi:position`, and `cdi:formats` → the `InstanceVariable`.
- **`cdi:TextMapping`** — a PhysicalMapping for delimited or fixed-width text. Adds `cdi:defaultDecimalSeparator`, `cdi:defaultDigitGroupSeparator`, and `cdi:mappingLabel` (`LabelForDisplay`).
- **`cdi:LocatorMapping`** — a PhysicalMapping that carries a required `cdi:locator` string addressing the value's position in a non-tabular physical layout (e.g. an XPath, JSON pointer, or array-index expression).

## `$defs`

- **`PhysicalMappingPosition`** — assigns an integer `cdi:value` position to a `PhysicalMapping` (`cdi:indexes`) within an ordered sequence of mappings.

## Relationship to the CDIF building blocks

CDIF's own `cdifProperties/cdifPhysicalMapping` and `cdifProperties/cdifTabularData` building blocks cover the same ground for the CDIF schema.org profiles. `ddicdiPhysicalMapping` is the canonical DDI-CDI counterpart, kept for completeness alongside the rest of the `ddiProperties` set.
