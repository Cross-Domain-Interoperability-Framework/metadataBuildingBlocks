# CDIF TextMapping

Physical mapping for a variable in a delimited or fixed-width **text** dataset. Extends
[`cdifPhysicalMapping`](../cdifPhysicalMapping/) (via `allOf`) with the text-format
properties from DDI-CDI `TextMapping`:

- `cdi:length` — column width for fixed-width text
- `cdi:defaultDecimalSeparator`
- `cdi:defaultDigitGroupSeparator`
- `cdif:displayLabel` (cdif: — LabelForDisplay simplified to a plain string)

Used as the item type for `cdif:hasPhysicalMapping` on a distribution typed
`cdi:TabularTextDataSet`. The base `cdifPhysicalMapping` carries the
serialization-agnostic properties (index, format, physical data type, scale, lengths,
null sequence, default value, number pattern); structured-document location is in
`cdifLocatorMapping`.
