## CDIF Access

Profile module for machine-actionable access and usage conditions, expressed as [ODRL Offer](../../../odrlProperties/odrlOffer/) policies. A conforming record declares `https://w3id.org/cdif/access/1.1` and carries at least one policy:

- as `odrl:hasPolicy` on a `schema:distribution` item, inline or by `{@id}` reference (preferred: distributions of one dataset can differ in their conditions), or
- as an `{@id}` reference in `schema:conditionsOfAccess` on the Dataset. Only a reference fits there, because cdifCore's item shapes for that property do not admit an inline Offer.

Draft. Open questions are listed in the schema descriptions and in [odrlOffer](../../../odrlProperties/odrlOffer/).

### Dependencies

- [odrlOffer](../../../odrlProperties/odrlOffer/) - the ODRL Offer policy
- [objectReference](../../../cdifDataType/objectReference/) - `{@id}` references
