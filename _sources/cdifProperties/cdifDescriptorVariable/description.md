# CDIF Descriptor Variable

A **DDI-CDI Descriptor Variable** is a presentational variable found only in **Long Data Sets**. It records the codes that appear in the dataset's descriptor column — each code naming which logical variable the value in the corresponding Reference Variable column is a measure for.

For example, in a long-format vitals table:

| patient_id | measure_name | measure_value |
|---|---|---|
| P001 | systolic_bp | 132 |
| P001 | heart_rate | 78 |

`measure_name` is the descriptor column; the values it takes (`systolic_bp`, `heart_rate`) are descriptor codes that name the conceptual RepresentedVariables they identify.

## Structure

A `cdi:DescriptorVariable` carries:

| Property | Required | Notes |
|---|---|---|
| `@type` | required | Must include `cdi:DescriptorVariable`. |
| `@id` | recommended | Identifier for the variable node. |
| `cdif:hasValuesFrom` | **required** | A `cdi:DescriptorValueDomain` enumerating the descriptor codes (see below). |
| `cdi:name` | optional | Array of `cdi:ObjectName` (formal naming per ISO 11179-5). |

The **`cdi:DescriptorValueDomain`** has a required `cdif:takesValuesFrom` array of descriptor entries. Each entry pairs:

- `cdif:value` — the code as it appears in the descriptor column (e.g. `"systolic_bp"`).
- `cdif:isDefinedBy` — an inline `cdifRepresentedVariable` or `@id`-reference to one declared elsewhere in the document, identifying the conceptual variable the code names.

This is the controlled-vocabulary descriptor pattern: strings in the descriptor column map to RepresentedVariables (the conceptual definitions of the variables those codes name). No SKOS Concept indirection.

## Use in DataStructure

A `cdi:VariableDescriptorComponent` (in [cdifDataStructureComponent](../cdifDataStructureComponent/)) holds a `cdi:isDefinedBy` pointer to a `cdifDescriptorVariable` instance, plus a `cdi:refersTo` pointer to the `cdi:VariableValueComponent` whose value-column contents the descriptor identifies.

## Dependencies

- [cdifRepresentedVariable](../cdifRepresentedVariable/) — target of `cdif:isDefinedBy` in each descriptor entry.
- [ddi-cdif-data-types](../../ddiCDIFProperties/ddi-cdif-data-types/) — `cdi:ObjectName` for `cdi:name`.
