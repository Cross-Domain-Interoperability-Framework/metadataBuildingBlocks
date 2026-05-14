DDI-CDI **Collections** is the generic collections pattern from the 2026-03 DDI-CDI model (`CollectionsPattern` package) — the abstract machinery for grouping, ordering, and relating members that the more specific structural classes (data structures, code lists, keys, …) specialize.

The root validates any of nine concrete classes:

- **`cdi:Collection`** — generic container supporting sets, bags, hierarchies, ordered and unordered groupings (`cdi:has` → `Member`, `cdi:allowsDuplicates`).
- **`cdi:List`** — a simple ordered Collection whose member order is given by `Position` objects.
- **`cdi:Map`** — a comparison map identifying source/target members and a `CorrespondenceDefinition`.
- **`cdi:Member`** — an element in a collection (atomic or composite).
- **`cdi:IndividualMember`** — a distinct, atomic (non-collection) member.
- **`cdi:MemberRelationship`** — a directional relationship between members (`cdi:hasSource` / `cdi:hasTarget`).
- **`cdi:Position`** — the position of a member within a `List` (`cdi:value`, `cdi:indexes`).
- **`cdi:Structure`** — an organized set of member relationships, characterized by `cdi:specification` (reflexive/symmetric/transitive), `cdi:topology`, and `cdi:totality`.
- **`cdi:Comparison`** — the minimal comparison pattern, carrying member `Map`s.
