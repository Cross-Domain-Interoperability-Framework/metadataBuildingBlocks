# A bundle distribution reached through its landing page cannot satisfy `schema:distribution`

**13 September 2026.** Raised by a consumer that hits this on every record it publishes.

---

## 1. The prose and the schema disagree

`profiles/cdifProfile/cdifCore/schema.yaml` says, of `schema:url`:

> Web Location of a page describing the dataset (landing page), typically providing links or
> instructions to get the actual resource content; analogous to dcat:accessURL. **If a direct
> link is available to get the data, put in distribution/contentUrl**

and of `schema:distribution`:

> **If user must access data through a landing page, provide link to landing page in the 'url'
> property for the dataset**

That is a clear rule describing a real delivery shape: there is no direct href, so the landing
page carries the address.

The schema does not implement it. `schema:distribution.items` is

```yaml
items:
  anyOf:
    - $ref: '#/$defs/DataDownload'
    - $ref: '#/$defs/WebAPI'
```

and `schemaorgProperties/dataDownload/schema.yaml` ended

```yaml
required:
- 'schema:contentUrl'
- '@type'
```

So every distribution item must either publish a direct href or be a web service. **The
landing-page case the prose describes has no branch, and is rejected.**

`cdifManifest` does not relieve it, by its own statement:

> The base `schema:distribution` anyOf [DataDownload, WebAPI] contributed by cdifCore is
> preserved — this BB only adds property constraints, no new anyOf branch.

Nor can a downstream profile relieve it: JSON Schema `allOf` composition only ever narrows, so
no extending profile can widen an inherited `anyOf` or drop an inherited `required`. It has to
change here.

## 2. The consumer

Astromat Data Archive (ADA), 7,446 published records, each declaring
`https://w3id.org/cdif/manifest/1.1` in `schema:subjectOf` → `dcterms:conformsTo`.

A record's data is a zip bundle, typed `["schema:DataDownload", "schema:Collection"]`, which
enumerates its component files in `schema:hasPart` — the manifest bundle pattern. It carries no
`schema:contentUrl`, deliberately: the bundle is fetched through an endpoint that returns
`{"downloadUrl": "<presigned S3 URL>"}` rather than the bytes, and that presigned URL expires,
so there is no href that can be published. The record's address is its landing page in
`schema:url` — exactly what the prose prescribes.

**Every one of those records fails on it.** This is not a data-quality problem; it is the prose
and the schema disagreeing.

## 3. The change

Two halves, because the second cannot be written inside the distribution item: JSON Schema has
no parent reference, so an item cannot see the dataset's `schema:url`.

### `schemaorgProperties/dataDownload`

`schema:contentUrl` moves out of the unconditional `required` and becomes conditional:

- **not** additionally typed `schema:Collection` → `schema:contentUrl` required, exactly as
  before;
- typed `schema:Collection` → `schema:contentUrl` not required, but **`schema:hasPart` is**, so
  a bundle that gives up its href stays self-describing rather than simply losing its address.

An ordinary `DataDownload` is unaffected.

### `profiles/cdifProfile/cdifCore`

A dataset-scope rule: if any distribution item is a `schema:Collection` carrying no
`schema:contentUrl`, then `schema:url` is required.

This carries the same truth as "contentUrl is not required if there is a Dataset/schema:url" in
the direction JSON Schema can check, and it is **strictly stronger than today** for the case it
admits — a bundle may omit `contentUrl` only if the record says where to go instead. Today a
record can satisfy the root `anyOf [schema:url, schema:distribution]` with a distribution alone
and publish no landing page at all.

## 4. Tested

Against two published ADA records, `10.60707/an7h-fg87` and `10.60707/3xec-yw98`, using a
resolved profile that composes cdifCore, cdifDataDescription, cdifManifest and cdifProvenance.

| | distribution errors before | after |
|---|---:|---:|
| `10.60707/an7h-fg87` | 2 | 1 |
| `10.60707/3xec-yw98` | 2 | 1 |

The remaining error was **not** a CDIF defect: that consumer's WebAPI entry omitted
`schema:potentialAction` and `schema:termsOfService`, which cdifCore's WebAPI branch requires.
Fixed on the consumer side, after which **distribution errors reach 0**.

Three negative controls, all behaving as intended:

| control | result |
|---|---|
| bundle Collection with no `contentUrl` **and** no `schema:url` | rejected |
| plain `DataDownload` with no `contentUrl` | still rejected |
| `schema:Collection` with no `contentUrl` **and** no `hasPart` | rejected |

`validate_examples.py` stays at 150 passed, 0 failed.

## 5. What this does not ask for

No change to `cdifManifest`, whose hasPart rules already describe this shape correctly. No
relaxation of `contentUrl` for ordinary downloads. No new building block, no new vocabulary.

## 6. Alternative considered

A third `anyOf` branch on `schema:distribution.items` — a `BundleCollection` shape — instead of
a conditional inside `dataDownload`. It tests identically on the same records and controls, but
needs a new building block, and it reads less directly as "contentUrl is required unless this is
a bundle". The conditional was preferred as the smaller change. If maintainers would rather keep
`dataDownload` unconditional, the branch version is a drop-in substitute.
