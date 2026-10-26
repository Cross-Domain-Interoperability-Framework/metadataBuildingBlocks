## ODRL Policy

W3C ODRL 2.2 Policy typed by one of its subclasses (Set, Offer, Agreement, Request, Ticket, Assertion, Privacy), with permissions, prohibitions and obligations, policy-level target and parties, odrl:profile, odrl:inheritFrom and odrl:conflict. Checks each subclass's requirements from the ODRL vocabulary (e.g. an Agreement needs an assigner and an assignee, a Ticket no assignee), met at policy level or on every rule.

Generic W3C ODRL; CDIF-specific rules belong in profile blocks such as [odrlOffer](../odrlOffer/).

### Dependencies

- [odrlRule](../odrlRule/)
- [odrlTerms](../odrlTerms/)
- [objectReference](../../cdifDataType/objectReference/)
