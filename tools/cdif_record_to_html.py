#!/usr/bin/env python3
"""Render a CDIF JSON-LD metadata record as a tabbed, self-contained HTML page.

The layout is driven by the record itself.  The conformance URIs declared in
``schema:subjectOf`` -> ``dcterms:conformsTo`` select which CDIF profile
modules apply, and each selected module contributes one tab holding the
properties that module defines.  Properties present in the record but not
defined by any selected module are still rendered -- root-level ones in an
"Additional" tab, nested ones in place -- so nothing in the record is dropped.

Profile modules are discovered by scanning the building-block sources for the
conformance URI each one pins, so adding a module or bumping a version URI
needs no change here.

A nested property that no declared profile mentions anywhere is marked in
place; a remote @context is fetched so its CURIEs resolve (--offline to skip);
and several records can be rendered in one run, optionally with a catalogue
page linking them.

USAGE:
  python tools/cdif_record_to_html.py record.json
  python tools/cdif_record_to_html.py record.json -o out.html
  python tools/cdif_record_to_html.py _sources/profiles/cdifCompositeProfile/CoreDiscovery       -o build/records --index build/records/index.html
  python tools/cdif_record_to_html.py --list-profiles
"""
from __future__ import annotations

import argparse
import html
import json
import re
import threading
import sys
from pathlib import Path
from urllib.request import Request, urlopen

import yaml

REPO = Path(__file__).resolve().parent.parent

# Scanned for profile modules.  cdifProfile holds the dataset modules; the
# domain trees (xasProperties) pin their own conformance URIs the same way.
DEFAULT_PROFILE_DIRS = [
    REPO / '_sources' / 'profiles' / 'cdifProfile',
    REPO / '_sources' / 'xasProperties',
]

CDIF_URI_PREFIX = 'https://w3id.org/cdif/'

# Tab order, least to most specific.  A property declared by more than one
# selected module is assigned to the most specific one -- so a record that
# declares both discovery and data_description shows schema:variableMeasured
# under Data Description, where the detailed structure is defined.
MODULE_ORDER = [
    'cdifCore',
    'cdifDiscovery',
    'cdifDataDescription',
    'cdifDataStructure',
    'cdifProvenance',
    'cdifManifest',
    'cdifConceptScheme',
    'cdifCodelist',
]

# schema.yaml titles are documentation strings, not tab labels.
TAB_LABELS = {
    'cdifCore': 'Core',
    'cdifDiscovery': 'Discovery',
    'cdifDataDescription': 'Data Description',
    'cdifDataStructure': 'Data Structure',
    'cdifProvenance': 'Provenance',
    'cdifManifest': 'Manifest',
    'cdifConceptScheme': 'Concept Scheme',
    'cdifCodelist': 'Codelist',
    'xasCore': 'XAS Core',
    'xasOptional': 'XAS Optional',
}

# Rendered in the page banner rather than in a tab, to avoid showing the
# record's identity twice.
BANNER_PROPERTIES = ['@id', '@type', 'schema:name', 'schema:description']

# The catalog record describes the metadata, not the resource, so it gets its
# own tab regardless of which module declares the property.
RECORD_PROPERTY = 'schema:subjectOf'

LABEL_PREFERENCE = [
    'schema:name', 'skos:prefLabel', 'rdfs:label', 'dcterms:title',
    'schema:legalName', 'schema:termCode', 'schema:value',
]


# --------------------------------------------------------------------------
# profile registry
# --------------------------------------------------------------------------

class Module:
    def __init__(self, name, path, title, uri, properties):
        self.name = name
        self.path = path
        self.title = title
        self.uri = uri
        self.properties = properties      # {property name: description}

    @property
    def label(self):
        return TAB_LABELS.get(self.name, self.name)

    @property
    def rank(self):
        return MODULE_ORDER.index(self.name) if self.name in MODULE_ORDER \
            else len(MODULE_ORDER)


def _is_conformance_uri(value):
    # Convention (agents.md): a conformance URI carries no trailing '/'.  That
    # separates them from namespace declarations such as
    # https://w3id.org/cdif/xas/, which appear as consts under @context.
    return (isinstance(value, str)
            and value.startswith(CDIF_URI_PREFIX)
            and not value.endswith('/'))


_VERSION_SUFFIX = re.compile(r'/\d+(?:\.\d+)*$')


def uri_stem(uri):
    """A conformance URI without its trailing version segment.

    Records in the wild declare the version they were written against:
    real ADA records say https://w3id.org/cdif/core/1.0 where this repo now
    pins core/1.1. Matching on the stem keeps such a record laid out by
    profile instead of collapsing into "Additional"; the version difference
    is reported rather than hidden.
    """
    return _VERSION_SUFFIX.sub('', uri) if isinstance(uri, str) else uri


def resolve_module(uri, modules, by_stem):
    """(module, declared_version_differs). Exact match wins."""
    module = modules.get(uri)
    if module is not None:
        return module, False
    module = by_stem.get(uri_stem(uri))
    return (module, True) if module is not None else (None, False)


def modules_by_stem(modules):
    index = {}
    for uri, module in modules.items():
        index.setdefault(uri_stem(uri), module)
    return index


def _find_conformance_uris(node, found):
    """Collect every `const` that pins a CDIF conformance URI.

    Reading `const` rather than any string keeps prose out of the result --
    cdifManifest's description mentions its own URI in passing.  The @context
    subtree is skipped: the consts there declare namespace prefixes.
    """
    if isinstance(node, dict):
        if _is_conformance_uri(node.get('const')):
            found.add(node['const'])
        for key, child in node.items():
            if key != '@context':
                _find_conformance_uris(child, found)
    elif isinstance(node, list):
        for child in node:
            _find_conformance_uris(child, found)
    return found


# xasOptional pins its conformance URI only in SHACL (sh:hasValue), not in the
# JSON Schema, so the const scan alone would miss it.
SHACL_CONFORMANCE = re.compile(r'sh:hasValue\s+<(' + re.escape(CDIF_URI_PREFIX) + r'[^>]+)>')


def _shacl_conformance_uris(directory):
    rules = directory / 'rules.shacl'
    if not rules.is_file():
        return set()
    try:
        text = rules.read_text(encoding='utf-8')
    except OSError:
        return set()
    return {m for m in SHACL_CONFORMANCE.findall(text) if _is_conformance_uri(m)}


def _load_source(directory):
    """The authoring schema.  Conformance URIs must come from here: a
    resolvedSchema.json inlines other blocks into $defs, and their conformance
    consts come along with them, so a module would claim URIs it does not own.
    """
    source = directory / 'schema.yaml'
    if source.is_file():
        try:
            return yaml.safe_load(source.read_text(encoding='utf-8'))
        except (yaml.YAMLError, OSError):
            pass
    return None


def _load_resolved(directory):
    """The resolved schema, used only for property descriptions -- it carries
    the ones that $ref'd properties lack in schema.yaml."""
    resolved = directory / 'resolvedSchema.json'
    if resolved.is_file():
        try:
            return json.loads(resolved.read_text(encoding='utf-8'))
        except (json.JSONDecodeError, OSError):
            pass
    return None


def load_modules(dirs):
    """Discover profile modules and the conformance URI each one pins."""
    modules = {}
    for base in dirs:
        if not base.is_dir():
            continue
        for directory in sorted(base.iterdir()):
            if not directory.is_dir():
                continue
            schema = _load_source(directory)
            if not isinstance(schema, dict):
                continue
            uris = _find_conformance_uris(schema, set())
            uris |= _shacl_conformance_uris(directory)
            if not uris:
                continue
            resolved = _load_resolved(directory)
            described = (resolved.get('properties') or {}) if isinstance(resolved, dict) else {}
            properties = {}
            for name, spec in (schema.get('properties') or {}).items():
                text = ''
                for source in (spec, described.get(name)):
                    if isinstance(source, dict):
                        text = source.get('description') or source.get('title') or text
                    if text:
                        break
                properties[name] = text
            title = schema.get('title') or directory.name
            module = Module(directory.name, directory, title, sorted(uris)[0], properties)
            for uri in uris:
                modules.setdefault(uri, module)
    return modules


# --------------------------------------------------------------------------
# record inspection
# --------------------------------------------------------------------------

_CONTEXT_CACHE = {}


def fetch_context(url, timeout=10):
    """Fetch a remote JSON-LD context and return its term map.

    Cached per run. A failure is a warning, not an error: the page still
    renders, with unexpandable CURIEs shown as text.
    """
    if url in _CONTEXT_CACHE:
        return _CONTEXT_CACHE[url]
    terms = {}
    try:
        request = Request(url, headers={
            'Accept': 'application/ld+json, application/json;q=0.9, */*;q=0.1',
            'User-Agent': 'cdif_record_to_html',
        })
        with urlopen(request, timeout=timeout) as response:
            body = json.loads(response.read().decode('utf-8'))
        terms = _context_terms(body.get('@context') if isinstance(body, dict) else None)
    except Exception as exc:                      # network, TLS, JSON, encoding
        print('warning: could not fetch context %s (%s: %s)'
              % (url, type(exc).__name__, exc), file=sys.stderr)
    _CONTEXT_CACHE[url] = terms
    return terms


def _context_terms(context, offline=True, seen=None):
    """Prefix -> namespace map from a @context value, following remote
    references when not offline."""
    seen = seen if seen is not None else set()
    entries = context if isinstance(context, list) else [context]
    prefixes = {}
    for entry in entries:
        if isinstance(entry, dict):
            for key, value in entry.items():
                if key.startswith('@'):
                    continue
                if isinstance(value, str):
                    prefixes[key] = value
                elif isinstance(value, dict) and isinstance(value.get('@id'), str):
                    prefixes[key] = value['@id']
        elif isinstance(entry, str) and entry.startswith(('http://', 'https://')):
            if offline or entry in seen:
                continue
            seen.add(entry)
            prefixes.update(fetch_context(entry))
    return prefixes


def record_context(record, offline=True):
    """Prefix -> namespace map from the record's @context.

    A remote context (a bare URL in @context) is fetched unless offline;
    CURIEs that still cannot be expanded are rendered as text.
    """
    return _context_terms(record.get('@context'), offline=offline)


def _type_consts(spec):
    """The @type values a schema node pins, via const or enum."""
    type_spec = (spec.get('properties') or {}).get('@type')
    if not isinstance(type_spec, dict):
        return []
    found = []
    for holder in (type_spec.get('contains'), type_spec.get('items'), type_spec):
        if not isinstance(holder, dict):
            continue
        if isinstance(holder.get('const'), str):
            found.append(holder['const'])
        for value in (holder.get('enum') or []):
            if isinstance(value, str):
                found.append(value)
    return found


def known_property_names(modules):
    """Every property name any declared profile mentions, at any depth.

    This is deliberately a weak claim. A stronger per-@type check -- "is this
    property allowed on a node of this type" -- cannot be made reliably from
    these schemas: CDIF modules are property bundles and only cdifCore pins the
    root @type, so cdifDiscovery's schema:temporalCoverage is never associated
    with schema:Dataset in any single module. Type-to-property association only
    becomes true after the profile composes them, which build_tabs already does
    at the record root. Attempting it per node marked ~22% of valid content as
    "not in profile".

    So a nested property is flagged only when NO declared profile mentions it
    anywhere -- the same claim the root-level "Additional" tab makes.
    """
    names = set()

    def visit(node):
        if isinstance(node, dict):
            declared = node.get('properties')
            if isinstance(declared, dict):
                names.update(declared.keys())
            for child in node.values():
                visit(child)
        elif isinstance(node, list):
            for child in node:
                visit(child)

    seen = set()
    for module in modules:
        if module.path in seen:
            continue
        seen.add(module.path)
        schema = _load_resolved(module.path) or _load_source(module.path)
        if isinstance(schema, dict):
            visit(schema)
    return names


def unknown_keys(node, known):
    """Property names on this node that no declared profile mentions at all."""
    if not known:
        return set()
    return {k for k in node
            if not k.startswith('@') and k not in known}


def catalog_record(record):
    node = record.get(RECORD_PROPERTY)
    if isinstance(node, list):
        node = next((n for n in node if isinstance(n, dict)), None)
    return node if isinstance(node, dict) else None


def declared_conformance(record):
    node = catalog_record(record)
    if not node:
        return []
    declared = node.get('dcterms:conformsTo')
    if declared is None:
        return []
    if not isinstance(declared, list):
        declared = [declared]
    uris = []
    for item in declared:
        if isinstance(item, str):
            uris.append(item)
        elif isinstance(item, dict) and isinstance(item.get('@id'), str):
            uris.append(item['@id'])
    return uris


# --------------------------------------------------------------------------
# value rendering
# --------------------------------------------------------------------------

def esc(text):
    return html.escape(str(text), quote=True)


def expand(value, prefixes):
    """CURIE or URL -> absolute URL, or None if it is neither."""
    if not isinstance(value, str):
        return None
    if value.startswith(('http://', 'https://')):
        return value
    prefix, sep, rest = value.partition(':')
    if sep and not rest.startswith('/'):
        base = prefixes.get(prefix)
        if isinstance(base, str):
            return base + rest
    return None


def local_name(curie):
    return re.split(r'[:/#]', curie)[-1] or curie


def humanize(name):
    """'schema:variableMeasured' -> 'Variable Measured'."""
    stem = local_name(name)
    spaced = re.sub(r'(?<=[a-z0-9])(?=[A-Z])', ' ', stem)
    return spaced[:1].upper() + spaced[1:]


def type_names(node):
    types = node.get('@type')
    if isinstance(types, str):
        types = [types]
    return [local_name(t) for t in (types or []) if isinstance(t, str)]


def node_label(node):
    for key in LABEL_PREFERENCE:
        value = node.get(key)
        if isinstance(value, str) and value.strip():
            return value
        if isinstance(value, dict):
            for inner in LABEL_PREFERENCE:
                if isinstance(value.get(inner), str):
                    return value[inner]
        if isinstance(value, list):
            for item in value:
                if isinstance(item, str) and item.strip():
                    return item
    return None


def render_link(url, text=None):
    return ('<a href="%s" target="_blank" rel="noopener noreferrer">%s</a>'
            % (esc(url), esc(url if text is None else text)))


def render_scalar(value, prefixes):
    if isinstance(value, bool):
        return '<span class="lit">%s</span>' % ('true' if value else 'false')
    if isinstance(value, (int, float)):
        return '<span class="lit">%s</span>' % esc(value)
    url = expand(value, prefixes)
    if url:
        return render_link(url, value)
    return '<span class="lit">%s</span>' % esc(value)


# Source descriptions routinely arrive with the whitespace of the markup they
# were stripped from -- tabs and runs of blank lines. `.lit` is pre-wrap, so
# every one of those became vertical space in the page. Collapse the runs but
# keep single newlines, which usually are meant.
_WS_RUN = re.compile(r'[ \t\x0b\f\r]+')
_BLANK_RUN = re.compile(r'\n\s*\n\s*\n+')


def normalize_text(text):
    """Collapse incidental whitespace in a literal, preserving line structure."""
    if not isinstance(text, str):
        return text
    out = _WS_RUN.sub(' ', text)
    out = _BLANK_RUN.sub('\n\n', out)
    return out.strip()


ABSTRACT_CLAMP = 420


def render_abstract(text, prefixes):
    """The record description, clamped when it would fill the screen.

    A long description pushed the tabs and every structured property below the
    fold. The first paragraph shows; the rest is one click away.
    """
    if not isinstance(text, str):
        return '<div class="abstract">%s</div>' % render_value(text, prefixes)
    clean = normalize_text(text)
    if len(clean) <= ABSTRACT_CLAMP:
        return '<div class="abstract">%s</div>' % render_scalar(clean, prefixes)
    head, _, tail = clean.partition('\n\n')
    if len(head) > ABSTRACT_CLAMP or not tail:
        head, tail = clean[:ABSTRACT_CLAMP].rsplit(' ', 1)[0], clean[len(
            clean[:ABSTRACT_CLAMP].rsplit(' ', 1)[0]):]
    return (
        '<div class="abstract">%s'
        '<details class="more"><summary>show the rest of the description</summary>'
        '<div class="more-body">%s</div></details>'
        '</div>' % (render_scalar(head, prefixes), render_scalar(tail.strip(), prefixes))
    )


def render_value(value, prefixes, depth=0, type_index=None):
    if value is None:
        return '<span class="empty">null</span>'
    if isinstance(value, (str, int, float, bool)):
        internal = anchor_href(value) if isinstance(value, str) else None
        if internal:
            # e.g. cdif:formats_InstanceVariable: "#time"
            return '<a class="ref" href="%s">%s</a>' % (esc(internal), esc(value))
        return render_scalar(normalize_text(value), prefixes)
    if isinstance(value, list):
        if not value:
            return '<span class="empty">(none)</span>'
        items = ''.join('<li>%s</li>' % render_value(v, prefixes, depth, type_index)
                        for v in value)
        return '<ul class="vals">%s</ul>' % items
    if isinstance(value, dict):
        return render_node(value, prefixes, depth, type_index)
    return '<span class="lit">%s</span>' % esc(value)


# Where each @id in the record is rendered, for turning a reference into a link.
# Thread-local: the viewer app serves concurrent renders, and a module global
# would leak one request's anchors into another's page.
_CTX = threading.local()


def anchor_slug(node_id):
    """A stable, URL-safe anchor for a node @id."""
    return 'n-' + re.sub(r'[^A-Za-z0-9_-]+', '-', str(node_id)).strip('-').lower()


def set_anchor_index(index):
    """Install the {@id: href} map for the current render (None to clear)."""
    _CTX.anchors = index or {}


def anchor_href(node_id):
    """Where `node_id` renders, or None if it is not a node in this document."""
    return getattr(_CTX, 'anchors', {}).get(node_id)


def build_anchor_index(record, part_href=None):
    """{@id: href} for every node the output will render.

    A node inside a list long enough to be split out lands on that list's own
    page, so its href carries the page as well as the fragment. Everything else
    is a same-page fragment.
    """
    index = {}

    def walk(value, base):
        if isinstance(value, dict):
            ident = value.get('@id')
            # Only nodes with substance get an anchor -- a bare {"@id": ...} is
            # a reference to one, not a definition of it.
            if isinstance(ident, str) and len(
                    [k for k in value if k not in ('@id', '@context')]) > 0:
                index.setdefault(ident, '%s#%s' % (base, anchor_slug(ident)))
            for key, child in value.items():
                if key != '@context':
                    walk(child, base)
        elif isinstance(value, list):
            for item in value:
                walk(item, base)

    for key, value in record.items():
        if key == '@context':
            continue
        if (part_href is not None and isinstance(value, list)
                and len(value) > SPLIT_OVER):
            # Each entry lands on a particular PAGE of the companion, and the
            # anchor only exists there. Pointing every reference at page 1 would
            # send most of them somewhere the target is not.
            slug = re.sub(r'[^a-z0-9]+', '-', key.lower()).strip('-') or 'list'
            for i, item in enumerate(value):
                walk(item, part_href(slug, i // PART_PAGE + 1))
        else:
            walk(value, '')
    for graph_key in ('@graph',):
        if isinstance(record.get(graph_key), list):
            walk(record[graph_key], '')
    return index


# Fallback for the CDIF record types, used only when cdifCore's schema.yaml
# cannot be read. schema.yaml is the source of truth -- see record_types().
_RECORD_TYPES_FALLBACK = (
    'schema:CreativeWork', 'schema:SoftwareApplication',
    'schema:SoftwareSourceCode', 'schema:Product', 'schema:WebAPI',
    'schema:Dataset', 'schema:DigitalDocument', 'schema:Collection',
    'schema:ImageObject', 'schema:DataCatalog', 'schema:DefinedTermSet',
    'schema:MediaObject')


def record_types(modules=None):
    """The @type values a CDIF record may carry, from cdifCore's schema.yaml.

    Read rather than copied: the same enum is restated in
    CDIFSubjectOfPlacementShape, and `audit_building_blocks.py -c type-enum`
    exists to keep those two in step. A third copy would need a third check.
    """
    for module in (modules or {}).values():
        if getattr(module, 'name', '') != 'cdifCore':
            continue
        try:
            import yaml
            with open(Path(module.path) / 'schema.yaml', encoding='utf-8') as fh:
                doc = yaml.safe_load(fh)
            enum = (((doc.get('properties') or {}).get('@type') or {})
                    .get('items') or {}).get('enum')
            if enum:
                return tuple(enum)
        except Exception:
            break
    return _RECORD_TYPES_FALLBACK


def _type_tokens_of(node):
    value = node.get('@type') if isinstance(node, dict) else None
    if isinstance(value, str):
        return [value]
    return [v for v in (value or []) if isinstance(v, str)]


def find_record_node(doc, allowed):
    """The first node in `doc` typed as a CDIF record, or None.

    Accepts the shapes a landing page actually uses: the record itself, an
    @graph, or a bare list of nodes.
    """
    allowed = {t.split(':')[-1] for t in allowed}
    stack = [doc]
    while stack:
        node = stack.pop(0)
        if isinstance(node, dict):
            if any(t.split(':')[-1].split('/')[-1] in allowed
                   for t in _type_tokens_of(node)):
                return node
            graph = node.get('@graph')
            if isinstance(graph, list):
                stack.extend(graph)
            elif isinstance(graph, dict):
                stack.append(graph)
        elif isinstance(node, list):
            stack.extend(node)
    return None


_LD_SCRIPT = re.compile(
    r'<script[^>]+type\s*=\s*["\']application/ld\+json["\'][^>]*>(.*?)</script>',
    re.I | re.S)


def extract_jsonld(html_text, allowed):
    """The first CDIF-typed record embedded in an HTML page, or None.

    A landing page often carries several ld+json blocks -- a BreadcrumbList, an
    Organization, and the dataset -- so the type enum decides which one is the
    record rather than taking the first block and hoping.
    """
    for block in _LD_SCRIPT.findall(html_text):
        try:
            doc = json.loads(block.strip())
        except Exception:
            continue
        found = find_record_node(doc, allowed)
        if found is not None:
            # Keep the surrounding @context: the block's context defines the
            # prefixes the node's own keys use.
            if isinstance(doc, dict) and '@context' in doc and '@context' not in found:
                found = dict(found)
                found['@context'] = doc['@context']
            return normalize_schemaorg(found)
    return None


_SCHEMA_ORG = ('http://schema.org/', 'https://schema.org/',
               'http://schema.org', 'https://schema.org')


def _schema_org_base(value):
    """('http'|'https', slashless) if `value` is a schema.org base, else None.

    Host names are case-insensitive in URIs, so SCHEMA.org counts. Whether the
    base ends in a slash matters: JSON-LD concatenates @vocab with the term
    directly, so a slashless base yields https://schema.orgname rather than a
    term in the https://schema.org/ namespace.
    """
    if not isinstance(value, str):
        return None
    text = value.strip()
    lowered = text.lower()
    for scheme in ('https', 'http'):
        for base in ('%s://schema.org/' % scheme, '%s://schema.org' % scheme):
            if lowered == base:
                return scheme, not base.endswith('/')
    return None


def _schema_vocab(context):
    """True when `context` puts schema.org terms in scope unprefixed."""
    if isinstance(context, str):
        return _schema_org_base(context) is not None
    if isinstance(context, dict):
        return _schema_org_base(context.get('@vocab')) is not None
    if isinstance(context, list):
        return any(_schema_vocab(c) for c in context)
    return False


def https_vocab_note(context):
    """The https://schema.org/ namespace, when it is genuinely the wrong one.

    A STRING context of "https://schema.org/" is a reference to schema.org's
    context document, which defines schema: as http://schema.org/ -- so its
    terms expand to the http form and nothing is wrong. An @vocab of
    "https://schema.org/" expands terms to https://schema.org/, which is a
    different IRI from the one CDIF uses. Only that earns a note.
    """
    if isinstance(context, list):
        for part in context:
            note = https_vocab_note(part)
            if note:
                return note
        return None
    if isinstance(context, dict):
        vocab = context.get('@vocab')
        base = _schema_org_base(vocab)
        if base and base[0] == 'https':
            return vocab
    return None


def vocab_expands_to(context):
    """What a bare term expands to under this context's @vocab, or None.

    Reported rather than assumed, because a slashless @vocab does not do what
    it looks like it does: JSON-LD concatenates, so "https://schema.org" + name
    is "https://schema.orgname".
    """
    if isinstance(context, list):
        for part in context:
            got = vocab_expands_to(part)
            if got:
                return got
        return None
    if not isinstance(context, dict):
        return None
    vocab = context.get('@vocab')
    if _schema_org_base(vocab) is None:
        return None
    return vocab.strip() + 'name'


def normalize_schemaorg(record):
    """Rewrite bare schema.org terms to the `schema:` CURIEs CDIF uses.

    Only when the record's @context actually puts schema.org in scope
    unprefixed; a record that already uses CURIEs is returned untouched. Keys
    that are already prefixed, and JSON-LD keywords, are left alone -- a page
    mixing `cr:column` with bare `name` keeps the former as it is.
    """
    context = record.get('@context') if isinstance(record, dict) else None
    if not _schema_vocab(context):
        return record

    known = set()
    if isinstance(context, dict):
        known = {k for k in context if not k.startswith('@')}
    elif isinstance(context, list):
        for part in context:
            if isinstance(part, dict):
                known |= {k for k in part if not k.startswith('@')}

    def rename(key):
        if key.startswith('@') or ':' in key or key in known:
            return key
        return 'schema:' + key

    def walk(node):
        if isinstance(node, dict):
            return {rename(k): (
                [rename(t) if isinstance(t, str) else walk(t) for t in v]
                if k == '@type' and isinstance(v, list)
                else rename(v) if (k == '@type' and isinstance(v, str))
                else v if k == '@context' else walk(v))
                for k, v in node.items()}
        if isinstance(node, list):
            return [walk(v) for v in node]
        return node

    out = walk(record)
    # Replace the vocab with the prefix binding the renderer expands against.
    ctx = {'schema': 'http://schema.org/'}
    if isinstance(context, dict):
        for k, v in context.items():
            if not k.startswith('@') and isinstance(v, str):
                ctx.setdefault(k, v)
    out['@context'] = ctx
    return out


def render_node(node, prefixes, depth=0, type_index=None):
    """A JSON-LD object: a bare {@id} becomes a link, anything richer a card."""
    keys = [k for k in node if k != '@context']
    if keys == ['@id']:
        internal = anchor_href(node['@id'])
        if internal:
            # The reference points at a node this output actually renders.
            return ('<a class="ref" href="%s">%s</a>'
                    % (esc(internal), esc(node['@id'])))
        url = expand(node['@id'], prefixes)
        return (render_link(url, node['@id']) if url
                else '<span class="lit">%s</span>' % esc(node['@id']))

    types = type_names(node)
    label = node_label(node)
    identifier = node.get('@id') if isinstance(node.get('@id'), str) else None

    head = []
    if label:
        head.append('<span class="node-label">%s</span>' % esc(label))
    for name in types:
        head.append('<span class="badge">%s</span>' % esc(name))
    if identifier:
        url = expand(identifier, prefixes)
        shown = render_link(url, identifier) if url else esc(identifier)
        head.append('<span class="node-id">%s</span>' % shown)

    shown_keys = {'@type', '@id'}
    if label:
        for key in LABEL_PREFERENCE:
            if key in node and node.get(key) == label:
                shown_keys.add(key)
                break

    unknown = unknown_keys(node, type_index)
    rows = []
    for key in keys:
        if key in shown_keys:
            continue
        extra = ' unknown' if key in unknown else ''
        flag = ('<span class="flag" title="Not defined for this @type by any '
                'declared profile">not in profile</span>') if key in unknown else ''
        rows.append(
            '<div class="row%s"><div class="key" title="%s">%s'
            '<span class="curie">%s</span>%s</div>'
            '<div class="val">%s</div></div>'
            % (extra, esc(key), esc(humanize(key)), esc(key), flag,
               render_value(node[key], prefixes, depth + 1, type_index))
        )

    header = ''.join(head)
    if not header and not rows:
        return '<span class="empty">(empty)</span>'
    at = (' id="%s"' % anchor_slug(identifier)) if (
        identifier and anchor_href(identifier)) else ''
    if not rows:
        return ('<div class="node"%s><div class="node-head">%s</div></div>'
                % (at, header))
    # Collapsible, open by default: long records stay browsable without any
    # content being hidden on arrival.
    # Depth 0 and 1 open, deeper collapsed. A survey dataset produced ~19k
    # open <details> on one page otherwise; the top levels stay readable and
    # "expand all" opens the rest on demand.
    return ('<details class="node"%s%s><summary class="node-head">%s'
            '<span class="rowcount">%d</span></summary>'
            '<div class="node-body">%s</div></details>'
            % (at, ' open' if (depth < 2 and not getattr(_CTX, 'closed', False))
               else '',
               header or '<span class="node-label">&hellip;</span>',
               len(rows), ''.join(rows)))


# A list-valued section longer than this starts collapsed: schema:variableMeasured
# and schema:distribution are the usual offenders, but the rule is by shape, not
# by property name, so a new long property needs no change here.
COLLAPSE_OVER = 5

# A list longer than this is rendered on its own page rather than inline. The
# Dataverse survey record has 863 variables, which alone accounted for 88% of a
# 15 MB page; at 100 the split only fires on lists that genuinely dominate.
SPLIT_OVER = 100

# How many names to show in the stub that replaces a split-out list.
SPLIT_PREVIEW = 8

# Entries per page of a split-out list. 863 variables in one document is
# 13.5 MB; at 100 the browser lays out about a megabyte at a time.
PART_PAGE = 100


def _entry_label(entry):
    """A short human label for one entry of a split-out list."""
    if isinstance(entry, dict):
        for key in ('schema:name', 'cdif:name', 'schema:alternateName',
                    'dcterms:title', '@id'):
            val = entry.get(key)
            if isinstance(val, list):
                val = val[0] if val else None
            if isinstance(val, dict):
                val = val.get('@id') or val.get('schema:name')
            if isinstance(val, str) and val.strip():
                return val.strip()
        return '(unnamed)'
    return str(entry)


def render_split_stub(name, value, href):
    """What stands in for a list that was moved to its own page."""
    names = [esc(_entry_label(v)) for v in value[:SPLIT_PREVIEW]]
    more = len(value) - len(names)
    preview = ', '.join(names) + (', and %d more' % more if more > 0 else '')
    return (
        '<div class="split">'
        '<p class="split-count">%d entries — moved to its own page so this one '
        'stays quick to load.</p>'
        '<p class="split-names">%s</p>'
        '<p><a class="split-link" href="%s">Open the full list</a></p>'
        '</div>' % (len(value), preview, esc(href))
    )


def render_property(name, value, description, prefixes, type_index=None,
                    label=None, parts=None, record_title=None):
    tip = ' title="%s"' % esc(description) if description else ''
    # The definition is useful once, not above every value. It sits behind an
    # info marker on the title line -- a full-width disclosure per property was
    # the same noise in a smaller font -- and stays in the DOM and in the
    # summary's tooltip, so nothing is lost.
    info = ('<button type="button" class="info" aria-label="Show definition">'
            'i</button>') if description else ''
    note = ('<div class="desc" hidden>%s</div>' % esc(description)) if description else ''
    count = len(value) if isinstance(value, list) else None
    tally = ('<span class="rowcount">%d</span>' % count) if count is not None else ''

    # A list long enough to dominate the page goes to its own document. `parts`
    # is how the caller receives it: the CLI writes a sibling file, the viewer
    # app serves it from memory.
    body = None
    if parts is not None and count is not None and count > SPLIT_OVER:
        slug = re.sub(r'[^a-z0-9]+', '-', name.lower()).strip('-') or 'list'
        href = parts.setdefault(
            '__href__', lambda sl, page=1: sl + '.html')(slug, 1)
        # The values, not rendered markup: only the consumer knows how to
        # address its own pages, so it renders the slice it needs.
        parts[slug] = {
            'title': '%s — %s' % (label or humanize(name), record_title or 'record'),
            'values': value,
            'count': count,
            'property': name,
            'prefixes': prefixes,
            'type_index': type_index,
        }
        body = render_split_stub(name, value, href)
    return (
        '<details class="prop"%s>'
        '<summary%s><span class="prop-title">%s</span>'
        '<span class="curie">%s</span>%s%s</summary>'
        '%s'
        '<div class="prop-val">%s</div>'
        '</details>'
        % ('' if (count is not None and count > COLLAPSE_OVER) else ' open',
           tip, esc(label or humanize(name)), esc(name), tally, info, note,
           body if body is not None
           else render_value(value, prefixes, 0, type_index))
    )


# --------------------------------------------------------------------------
# page assembly
# --------------------------------------------------------------------------

CSS = """
:root{--bg:#fff;--fg:#1c1f24;--muted:#5b6472;--line:#dde2e8;--accent:#1c5d8c;
      --card:#f7f9fb;--badge:#e6eef5;--warn:#8a5a00;--warnbg:#fdf6e3}
@media (prefers-color-scheme:dark){
 :root{--bg:#14171b;--fg:#e6e9ee;--muted:#98a2b3;--line:#2b3138;--accent:#7fb6dd;
       --card:#1b1f25;--badge:#243039;--warn:#e0b661;--warnbg:#2a2416}}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--fg);
     font:15px/1.5 -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif}
.wrap{max-width:1100px;margin:0 auto;padding:1.5rem 1.25rem 4rem}
a{color:var(--accent)}
header.banner{border-bottom:2px solid var(--line);padding-bottom:1rem;margin-bottom:.25rem}
header.banner h1{margin:.1rem 0 .5rem;font-size:1.55rem;line-height:1.25}
.ids{color:var(--muted);font-size:.83rem;word-break:break-all;margin-bottom:.5rem}
.srcfile{display:inline-block;margin-right:.6rem;padding:.05rem .4rem;
   border:1px solid var(--line);border-radius:3px;background:var(--card);
   font-family:ui-monospace,SFMono-Regular,Consolas,monospace;font-size:.78rem;
   color:var(--fg)}
.abstract{margin:.5rem 0 0;max-width:80ch}
.source-note{border-left:3px solid var(--accent);padding:.5rem .8rem;
             margin:.9rem 0 0;background:rgba(122,162,247,.07);max-width:90ch;
             font-size:.85rem}
.badge{display:inline-block;background:var(--badge);color:var(--fg);border-radius:3px;
       padding:.05rem .4rem;font-size:.75rem;margin-right:.3rem;white-space:nowrap}
nav.tabs{display:flex;flex-wrap:wrap;gap:.25rem;border-bottom:1px solid var(--line);
         margin:1.25rem 0;position:sticky;top:0;background:var(--bg);z-index:5;padding-top:.5rem}
nav.tabs button{border:1px solid transparent;border-bottom:none;background:none;color:var(--muted);
   font:inherit;font-size:.9rem;padding:.45rem .8rem;cursor:pointer;border-radius:5px 5px 0 0;
   margin-bottom:-1px}
nav.tabs button:hover{color:var(--fg)}
nav.tabs button[aria-selected=true]{color:var(--fg);font-weight:600;background:var(--card);
   border-color:var(--line);border-bottom:1px solid var(--card)}
nav.tabs .count{color:var(--muted);font-weight:400;font-size:.8em;margin-left:.3rem}
.panel[hidden]{display:none}
.panel > p.lead{color:var(--muted);margin:0 0 1.25rem;max-width:80ch}
.group{font-size:.78rem;text-transform:uppercase;letter-spacing:.06em;
       color:var(--muted);margin:1.6rem 0 .7rem;padding-bottom:.25rem;
       border-bottom:1px solid var(--line);font-weight:600}
.panel > .group:first-child{margin-top:0}
.prop{margin:0 0 1.4rem}
.prop > summary{margin:0 0 .1rem;font-size:1rem;font-weight:600;cursor:pointer;
   border-bottom:1px solid var(--line);padding:0 0 .2rem 1.1rem;position:relative;
   list-style:none}
.prop > summary::-webkit-details-marker{display:none}
.prop > summary::marker{content:''}
.prop > summary::before{content:'';position:absolute;left:.3rem;top:.5rem;
   border-left:.32rem solid var(--muted);border-top:.26rem solid transparent;
   border-bottom:.26rem solid transparent;transition:transform .12s;
   transform-origin:40% 50%}
.prop[open] > summary::before{transform:rotate(90deg)}
.prop > summary:hover{color:var(--accent)}
.prop:not([open]) > summary{border-bottom-color:transparent}
details.node > summary{cursor:pointer;list-style:none;padding-left:1rem;position:relative}
details.node > summary::-webkit-details-marker{display:none}
details.node > summary::marker{content:''}
details.node > summary::before{content:'';position:absolute;left:.1rem;top:.5rem;
   border-left:.3rem solid var(--muted);border-top:.24rem solid transparent;
   border-bottom:.24rem solid transparent;transition:transform .12s;
   transform-origin:40% 50%}
details.node[open] > summary::before{transform:rotate(90deg)}
details.node > summary:hover{color:var(--accent)}
.rowcount{color:var(--muted);font-size:.7rem;margin-left:.4rem}
details.node[open] > summary .rowcount{opacity:.5}
nav.tabs .bulk{margin-left:auto;display:flex;gap:.3rem;align-self:center;
   padding-bottom:.35rem}
nav.tabs .bulk button{font-size:.72rem;padding:.15rem .5rem;color:var(--muted);
   border:1px solid var(--line);border-radius:4px;background:none;margin-bottom:0}
nav.tabs .bulk button:hover{color:var(--accent);border-color:var(--accent)}
.prop-title{margin-right:.5rem}
.curie{color:var(--muted);font-weight:400;font-size:.75rem;
       font-family:ui-monospace,SFMono-Regular,Menlo,monospace;opacity:.75;
       font-family:ui-monospace,SFMono-Regular,Consolas,monospace;margin-left:.5rem}
.desc{color:var(--muted);font-size:.82rem;margin:.15rem 0 .5rem;max-width:80ch;
      padding-left:.6rem;border-left:2px solid var(--rule)}
.info{margin-left:.45rem;width:1.05em;height:1.05em;line-height:1;padding:0;
      border:1px solid var(--rule);border-radius:50%;background:none;
      color:var(--muted);font:600 .68rem/1 ui-monospace,Menlo,monospace;
      cursor:pointer;vertical-align:.08em}
.info:hover,.info[aria-expanded="true"]{color:var(--accent);border-color:var(--accent)}
.pager{display:flex;flex-wrap:wrap;gap:.3rem;align-items:center;margin:1rem 0}
.pg{padding:.2rem .5rem;border:1px solid var(--rule);border-radius:4px;
    font-size:.85rem;text-decoration:none}
a.pg:hover{border-color:var(--accent)}
.pg-here{font-weight:700;border-color:var(--accent);color:var(--accent)}
.pg-gap{border:none;color:var(--muted);padding:.2rem .1rem}
.ref{font-family:ui-monospace,SFMono-Regular,Menlo,monospace;font-size:.85rem}
.crumb{margin:0 0 1rem}
.part-title{margin:0 0 .2rem;font-size:1.5rem}
.part-sub{margin:0 0 1.4rem;color:var(--muted)}
.split{border:1px dashed var(--rule);border-radius:6px;padding:.7rem .9rem;
       margin:.2rem 0 .1rem}
.split-count{margin:0 0 .35rem;font-weight:600}
.split-names{margin:0 0 .6rem;color:var(--muted);font-size:.85rem;max-width:90ch}
.split-link{font-weight:600}
.more{margin:.4rem 0 0}
.more > summary{cursor:pointer;color:var(--accent);font-size:.82rem}
.more-body{margin-top:.4rem}
.prop-val{margin-top:.4rem;padding-left:.05rem}
ul.vals{list-style:none;margin:0;padding:0}
ul.vals > li{margin:0 0 .4rem}
ul.vals > li:last-child{margin-bottom:0}
.lit{white-space:pre-wrap}
.empty{color:var(--muted);font-style:italic}
.node{background:var(--card);border:1px solid var(--line);border-radius:5px;
      padding:.5rem .65rem;margin:.15rem 0}
.node .node{background:transparent}
.node-head{margin-bottom:.3rem}
.node-label{font-weight:600;margin-right:.45rem}
.node-id{color:var(--muted);font-size:.78rem;
         font-family:ui-monospace,SFMono-Regular,Consolas,monospace;word-break:break-all}
.row{display:grid;grid-template-columns:minmax(9rem,17rem) 1fr;gap:.4rem 1rem;
     padding:.22rem 0;border-top:1px dotted var(--line)}
.row:first-child{border-top:none}
.row > .key{color:var(--muted);font-size:.85rem}
.row > .key .curie{display:block;margin:0;font-size:.7rem;opacity:.75}
.row.unknown{background:var(--warnbg)}
.flag{display:inline-block;margin-top:.15rem;padding:0 .3rem;border-radius:3px;
      background:var(--warnbg);color:var(--warn);border:1px solid currentColor;
      font-size:.65rem;letter-spacing:.02em;white-space:nowrap}
ul.cards{list-style:none;margin:0;padding:0;display:grid;gap:.6rem;
         grid-template-columns:repeat(auto-fill,minmax(19rem,1fr))}
ul.cards > li{border:1px solid var(--line);border-radius:6px;background:var(--card);
              padding:.7rem .8rem}
ul.cards a.card-title{font-weight:600;font-size:1rem;text-decoration:none}
ul.cards .card-meta{color:var(--muted);font-size:.78rem;margin-top:.25rem;
                    word-break:break-all}
ul.cards .card-desc{font-size:.85rem;margin-top:.4rem}
.note{background:var(--warnbg);color:var(--warn);border:1px solid var(--line);
      border-radius:5px;padding:.5rem .7rem;margin:0 0 1.25rem;font-size:.85rem;max-width:80ch}
footer{margin-top:2.5rem;padding-top:.75rem;border-top:1px solid var(--line);
       color:var(--muted);font-size:.78rem}
@media(max-width:620px){.row{grid-template-columns:1fr;gap:.1rem}
 .row > .key .curie{display:inline;margin-left:.4rem}}
"""

JS = """
document.querySelectorAll('nav.tabs button[data-tab]').forEach(function(b){
  b.addEventListener('click', function(){
    document.querySelectorAll('nav.tabs button[data-tab]').forEach(function(o){
      o.setAttribute('aria-selected', String(o === b));
    });
    document.querySelectorAll('.panel').forEach(function(p){
      p.hidden = (p.id !== b.dataset.tab);
    });
    if (history.replaceState) history.replaceState(null, '', '#' + b.dataset.tab);
  });
});
function setAll(open){
  var pane = document.querySelector('.panel:not([hidden])') || document;
  // Not every <details>: the per-property definitions are deliberately closed,
  // and opening them all is what "expand all" was trying to get away from.
  pane.querySelectorAll('details').forEach(function(d){ d.open = open; });
}
document.querySelectorAll('button.info').forEach(function(b){
  b.addEventListener('click', function(ev){
    // Inside the <summary>, so without this the click also toggles the property.
    ev.preventDefault(); ev.stopPropagation();
    var d = b.closest('summary').parentNode.querySelector(':scope > .desc');
    if (!d) return;
    d.hidden = !d.hidden;
    b.setAttribute('aria-expanded', String(!d.hidden));
  });
});
var ea = document.getElementById('expand-all'), ca = document.getElementById('collapse-all');
if (ea) ea.addEventListener('click', function(){ setAll(true); });
if (ca) ca.addEventListener('click', function(){ setAll(false); });
if (location.hash) {
  var initial = document.querySelector('nav.tabs button[data-tab="' + location.hash.slice(1) + '"]');
  if (initial) initial.click();
}
"""


# --------------------------------------------------------------------------
# curated layout from JSON Forms uischema
# --------------------------------------------------------------------------

UISCHEMA_ROOT = REPO / '_sources' / 'jsonforms' / 'profiles'
COMPOSITE_ROOT = REPO / '_sources' / 'profiles' / 'cdifCompositeProfile'


class Layout:
    """A curated tab layout taken from a profile's JSON Forms uischema.

    tools/convert_for_jsonforms.py already derives a
    Categorization -> Category -> Group -> Control tree from each composite
    profile, with human labels and a sensible field order. Reusing it gives
    the same sections the ADA metadata forms show, generated from the
    profiles rather than hand-maintained here.
    """

    def __init__(self, name, uris, categories, labels):
        self.name = name
        self.uris = uris              # conformance URIs the profile requires
        self.categories = categories  # [(label, [(group label, [property])])]
        self.labels = labels          # {property: curated label}


def _scope_property(scope):
    """'#/properties/schema:name/properties/x' -> 'schema:name'."""
    if not isinstance(scope, str) or not scope.startswith('#/properties/'):
        return None
    parts = scope.split('/')
    return parts[2] if len(parts) > 2 else None


def _uischema_categories(uischema):
    """Flatten the uischema into [(category, [(group, [property])])] plus the
    curated label for each property."""
    labels = {}

    def controls(node, found):
        """Root property names under a node, in document order, de-duplicated."""
        if isinstance(node, dict):
            if node.get('type') == 'Control':
                name = _scope_property(node.get('scope'))
                if name and name not in found:
                    found.append(name)
                if name and name not in labels and isinstance(node.get('label'), str):
                    labels[name] = node['label']
            for child in (node.get('elements') or []):
                controls(child, found)
        elif isinstance(node, list):
            for child in node:
                controls(child, found)
        return found

    categories = []
    for category in (uischema.get('elements') or []):
        if not isinstance(category, dict):
            continue
        groups = []
        for group in (category.get('elements') or []):
            names = controls(group, [])
            if names:
                groups.append((group.get('label') or '', names))
        if groups:
            categories.append((category.get('label') or 'Section', groups))
    return categories, labels


def _composite_conformance(name):
    """The conformance URIs a composite profile requires, from the modules it
    composes. Returns None when no such composite exists."""
    directory = COMPOSITE_ROOT / name
    schema = _load_source(directory)
    if not isinstance(schema, dict):
        return None
    uris = set()
    base = directory.resolve()
    for entry in (schema.get('allOf') or []):
        ref = entry.get('$ref') if isinstance(entry, dict) else None
        if not isinstance(ref, str) or ref.startswith('#'):
            continue
        module_dir = (base / ref).resolve().parent
        module_schema = _load_source(module_dir)
        if isinstance(module_schema, dict):
            uris |= _find_conformance_uris(module_schema, set())
            uris |= _shacl_conformance_uris(module_dir)
    return uris


def load_layouts():
    """Every uischema whose composite profile still exists.

    A uischema left behind by a retired profile is skipped: XASdata's
    composite was archived in favour of xasDocument, which has no uischema of
    its own, so matching on the uischema directory name alone would apply a
    layout for a profile that no longer ships.
    """
    layouts = []
    if not UISCHEMA_ROOT.is_dir():
        return layouts
    for group_dir in sorted(UISCHEMA_ROOT.iterdir()):
        if not group_dir.is_dir():
            continue
        for profile_dir in sorted(group_dir.iterdir()):
            path = profile_dir / 'uischema.json'
            if not path.is_file():
                continue
            uris = _composite_conformance(profile_dir.name)
            if not uris:
                continue
            try:
                uischema = json.loads(path.read_text(encoding='utf-8'))
            except (json.JSONDecodeError, OSError):
                continue
            categories, labels = _uischema_categories(uischema)
            if categories:
                layouts.append(Layout(profile_dir.name, uris, categories, labels))
    return layouts


def choose_layout(declared, layouts):
    """The most specific layout the record actually satisfies.

    A layout applies only when the record declares every URI its profile
    requires; among those, the one requiring most wins.
    """
    stems = {uri_stem(u) for u in declared}
    applicable = [l for l in layouts
                  if l.uris and {uri_stem(u) for u in l.uris} <= stems]
    if not applicable:
        return None
    return max(applicable, key=lambda l: len(l.uris))


def split_graph(doc):
    """(primary record, companion nodes) for an @graph document.

    Returns (doc, []) unchanged when there is no @graph. The primary node is
    the one the catalog record is about when that can be determined, else the
    first schema:Dataset, else the first node -- so a graph without a dataset
    still renders something rather than failing.
    """
    graph = doc.get('@graph')
    if not isinstance(graph, list) or not graph:
        return doc, []
    nodes = [n for n in graph if isinstance(n, dict)]
    if not nodes:
        return doc, []

    def has_type(node, name):
        types = node.get('@type')
        types = types if isinstance(types, list) else [types]
        return name in types

    primary = next((n for n in nodes if n.get(RECORD_PROPERTY)), None)
    if primary is None:
        primary = next((n for n in nodes if has_type(n, 'schema:Dataset')), None)
    if primary is None:
        primary = nodes[0]

    # Keep the original object for the identity test below: copying primary to
    # attach @context would otherwise leave the original in the companion list.
    original = primary
    context = doc.get('@context')
    if context is not None and '@context' not in primary:
        primary = dict(primary)
        primary['@context'] = context
    return primary, [n for n in nodes if n is not original]


def companion_tabs(nodes, prefixes, type_index, used_slugs):
    """One tab per @type group of companion graph nodes."""
    groups = {}
    for node in nodes:
        types = node.get('@type')
        types = types if isinstance(types, list) else [types]
        label = local_name(next((t for t in types if isinstance(t, str)), 'Node'))
        groups.setdefault(label, []).append(node)

    tabs, panels = [], []
    for label in sorted(groups):
        members = groups[label]
        body = ('<p class="lead">%d companion node%s in the document graph, '
                'typed <code>%s</code>. These travel with the record rather than '
                'inside it.</p>'
                % (len(members), '' if len(members) == 1 else 's', esc(label)))
        # Companion nodes are supporting material and there can be dozens of
        # them, each deep: a concept-scheme graph rendered open produced 22k
        # open <details> on one page. They start collapsed; "expand all" opens
        # them on demand.
        body += ''.join(render_node(n, prefixes, 0, type_index)
                        for n in members).replace('<details class="node" open>',
                                                  '<details class="node">')
        slug = _slug(label, used_slugs)
        tabs.append((slug, label, len(members)))
        panels.append((slug, body))
    return tabs, panels


def _slug(text, used):
    base = re.sub(r'[^a-z0-9]+', '-', text.lower()).strip('-') or 'section'
    slug, n = base, 2
    while slug in used:
        slug, n = '%s-%d' % (base, n), n + 1
    used.add(slug)
    return slug


def _tabs_from_layout(record, layout, described, prefixes, type_index, unknown_uris,
                      parts=None, record_title=None, source_note=None):
    """Tabs from a profile's curated uischema: one per Category, sections per
    Group, in the order the profile's form declares."""
    handled = set(BANNER_PROPERTIES) | {'@context'}
    covered, used = set(), set()
    tabs, panels = [], []

    for category, groups in layout.categories:
        sections, count = [], 0
        for group_label, names in groups:
            present = [n for n in names
                       if n in record and n not in handled and n not in covered]
            if not present:
                continue
            body = ''.join(
                render_property(n, record[n], described.get(n, ''), prefixes,
                                type_index, layout.labels.get(n),
                                parts=parts, record_title=record_title)
                for n in present)
            heading = ('<h4 class="group">%s</h4>' % esc(group_label)) if group_label else ''
            sections.append(heading + body)
            covered.update(present)
            count += len(present)
        if not sections:
            continue
        body = ''.join(sections)
        if category == 'Metadata Record' and unknown_uris:
            listed = ', '.join('<code>%s</code>' % esc(u) for u in unknown_uris)
            body = ('<p class="note">Declared conformance not matched to a known '
                    'profile module: %s</p>' % listed) + body
        tabs.append((_slug(category, used), category, count))
        panels.append((tabs[-1][0], body))

    extra = [n for n in record if n not in handled and n not in covered]
    if extra:
        body = ('<p class="note">Present in the record but not placed by the '
                '%s form layout. Shown so nothing is dropped.</p>' % esc(layout.name))
        body += ''.join(render_property(n, record[n], described.get(n, ''),
                                        prefixes, type_index,
                                        parts=parts, record_title=record_title)
                        for n in extra)
        tabs.append((_slug('additional', used), 'Additional', len(extra)))
        panels.append((tabs[-1][0], body))

    return tabs, panels


def build_tabs(record, modules, prefixes, type_index=None, layouts=None,
               parts=None, record_title=None, source_note=None):
    """Assign each root property to a tab and render the panels.

    When the record satisfies a profile that ships a JSON Forms uischema,
    that curated layout is used; otherwise tabs are derived one per
    declared module."""
    uris = declared_conformance(record)
    selected, unknown_uris, versioned = [], [], []
    by_stem = modules_by_stem(modules)
    for uri in uris:
        module, differs = resolve_module(uri, modules, by_stem)
        if module is None:
            unknown_uris.append(uri)
            continue
        if differs:
            versioned.append((uri, module.uri))
        if module not in selected:
            selected.append(module)
    if versioned:
        unknown_uris = unknown_uris + [
            '%s (laid out as %s)' % (declared_uri, known_uri)
            for declared_uri, known_uri in versioned]
    if not selected:
        # No recognised declaration: fall back to core so the record still
        # renders with labels rather than as a bare property dump.
        core = next((m for m in modules.values() if m.name == 'cdifCore'), None)
        if core:
            selected.append(core)
    selected.sort(key=lambda m: m.rank)

    # Most specific declaring module wins a shared property.
    owner, described = {}, {}
    for module in selected:
        for name, description in module.properties.items():
            owner[name] = module
            if description:
                described[name] = description

    layout = choose_layout(uris, layouts or [])
    if layout is not None:
        tabs, panels = _tabs_from_layout(record, layout, described, prefixes,
                                         type_index, unknown_uris,
                                         parts=parts, record_title=record_title,
                                         source_note=source_note)
        if tabs:
            return tabs, panels, selected, unknown_uris

    handled = set(BANNER_PROPERTIES) | {'@context', RECORD_PROPERTY}
    buckets = {module.name: [] for module in selected}
    extra = []
    for name in record:
        if name in handled:
            continue
        module = owner.get(name)
        (buckets[module.name] if module else extra).append(name)

    panels, tabs = [], []

    def add(slug, label, count, body):
        tabs.append((slug, label, count))
        panels.append((slug, body))

    for module in selected:
        names = buckets[module.name]
        lead = ('<p class="lead">%s<br><code>%s</code></p>'
                % (esc(module.title), esc(module.uri)))
        if names:
            body = ''.join(render_property(n, record[n], described.get(n, ''),
                                          prefixes, type_index,
                                          parts=parts, record_title=record_title)
                           for n in names)
        elif module.name == 'cdifDataStructure':
            # This module adds no root properties; a structure is attached to a
            # distribution via cdi:isStructuredBy, so it shows under whichever
            # tab owns schema:distribution.
            body = ('<p class="note">This profile declares no properties on the record '
                    'root. Data structures attach to a distribution via '
                    '<code>cdi:isStructuredBy</code> and are rendered with the '
                    'distribution that carries them.</p>')
        else:
            body = ('<p class="note">No properties from this profile are present '
                    'in the record.</p>')
        add(module.name, module.label, len(names), lead + body)

    node = catalog_record(record)
    if node:
        body = ('<p class="lead">Statements about the metadata record itself '
                '(<code>dcat:CatalogRecord</code>), not about the resource it '
                'describes.</p>')
        if unknown_uris:
            listed = ', '.join('<code>%s</code>' % esc(u) for u in unknown_uris)
            body += ('<p class="note">Declared conformance not matched to a known '
                     'profile module, so it contributes no tab: %s</p>' % listed)
        body += render_property(RECORD_PROPERTY, node,
                                described.get(RECORD_PROPERTY, ''), prefixes,
                                type_index)
        add('record', 'Metadata Record', 1, body)

    if extra:
        body = ('<p class="note">Present in the record but not defined by any declared '
                'CDIF profile. Shown so nothing is dropped; these are not validated '
                'by the profiles above.</p>')
        body += ''.join(render_property(n, record[n], '', prefixes, type_index)
                        for n in extra)
        add('additional', 'Additional', len(extra), body)

    return tabs, panels, selected, unknown_uris


def part_page_count(part, per_page=PART_PAGE):
    """How many pages this split-out list needs."""
    return max(1, (part['count'] + per_page - 1) // per_page)


def _pager(page, pages, page_href):
    """Previous / next and a numbered jump, or nothing for a single page."""
    if pages < 2 or page_href is None:
        return ''
    bits = []
    if page > 1:
        bits.append('<a class="pg" href="%s">&#8592; previous</a>'
                    % esc(page_href(page - 1)))
    for n in range(1, pages + 1):
        # Keep the first, the last, and a window around the current page, so a
        # 40-page list does not render 40 links.
        if n in (1, pages) or abs(n - page) <= 2:
            bits.append('<span class="pg pg-here">%d</span>' % n if n == page
                        else '<a class="pg" href="%s">%d</a>' % (esc(page_href(n)), n))
        elif bits and bits[-1] != '<span class="pg pg-gap">&hellip;</span>':
            bits.append('<span class="pg pg-gap">&hellip;</span>')
    if page < pages:
        bits.append('<a class="pg" href="%s">next &#8594;</a>'
                    % esc(page_href(page + 1)))
    return '<nav class="pager">%s</nav>' % ''.join(bits)


def render_part_page(part, record, modules, offline=True, back=None,
                     page=1, per_page=PART_PAGE, page_href=None):
    """One page of a split-out list.

    Deliberately plain: the same stylesheet, a heading naming the property and
    its count, a way back, a pager, and the entries for this page. It exists so
    the main page does not have to carry them, not to be a second view of the
    record.
    """
    prefixes = part.get('prefixes') or record_context(record, offline=offline)
    # Entries start closed here: a page of 100 variables opened at once is a
    # wall of rows, and the point of this page is to scan the list.
    _CTX.closed = True
    name = record.get('schema:name')
    if isinstance(name, list):
        name = name[0] if name else None
    if isinstance(name, dict):
        name = name.get('@value') or name.get('schema:name')
    name = name if isinstance(name, str) and name.strip() else 'the record'
    nav = ('<p class="crumb"><a href="%s">&#8592; back to %s</a></p>'
           % (esc(back), esc(name))) if back else ''

    pages = part_page_count(part, per_page)
    page = min(max(1, page), pages)
    start = (page - 1) * per_page
    chunk = part['values'][start:start + per_page]
    body = render_value(chunk, prefixes, 0, part.get('type_index'))
    span = ('showing %d&ndash;%d of %d'
            % (start + 1, start + len(chunk), part['count'])) if pages > 1 else (
                '%d entries' % part['count'])
    pager = _pager(page, pages, page_href)
    _CTX.closed = False
    return (
        '<!doctype html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n'
        '<meta name="viewport" content="width=device-width, initial-scale=1">\n'
        '<title>%s%s</title>\n<style>%s</style>\n</head>\n<body>\n'
        '<main>\n%s<h1 class="part-title">%s</h1>\n'
        '<p class="part-sub"><code>%s</code> &middot; %s</p>\n'
        '%s<div class="prop-val">%s</div>\n%s</main>\n</body>\n</html>\n'
        % (esc(part['title']), (' (page %d of %d)' % (page, pages)) if pages > 1 else '',
           CSS, nav, esc(part['title']), esc(part['property']), span,
           pager, body, pager)
    )


def render_html(record, modules, title=None, offline=True, type_index=None,
                layouts=None, filename=None, parts=None, source_note=None):
    record, companions = split_graph(record)
    prefixes = record_context(record, offline=offline)
    # The display name is computed further down, but a split-out list needs it
    # for its own page title -- otherwise every companion is called "record".
    # References like "#time" or "#codelist/1" become links to wherever that
    # node renders -- which may be a companion page, so the index records the
    # page as well as the fragment.
    set_anchor_index(build_anchor_index(
        record, (parts or {}).get('__href__') if parts else None))
    _CTX.closed = False

    display = title
    if not display:
        display = record.get('schema:name')
        if isinstance(display, list):
            display = next((n for n in display if isinstance(n, str)), None)
        if not isinstance(display, str):
            display = record.get('@id')

    tabs, panels, selected, _ = build_tabs(record, modules, prefixes,
                                          type_index, layouts,
                                          parts=parts, record_title=display,
                                          source_note=source_note)
    if companions:
        used = {slug for slug, _, _ in tabs}
        extra_tabs, extra_panels = companion_tabs(companions, prefixes,
                                                  type_index, used)
        tabs = tabs + extra_tabs
        panels = panels + extra_panels

    name = record.get('schema:name')
    if isinstance(name, list):
        name = next((n for n in name if isinstance(n, str)), None)
    if not isinstance(name, str):
        name = record.get('@id') or 'CDIF metadata record'

    types = type_names(record)
    identifier = record.get('@id')
    ids = []
    if filename:
        ids.append('<span class="srcfile" title="Source file">%s</span>'
                   % esc(filename))
    if identifier:
        url = expand(identifier, prefixes)
        ids.append(render_link(url, identifier) if url else esc(identifier))

    description = record.get('schema:description')
    abstract = ''
    if description is not None:
        abstract = render_abstract(description, prefixes)

    # Shown under the header, always. Putting it in the Metadata Record panel
    # reads better but is unreliable: a record from the wild often declares no
    # conformsTo and gets no such tab, and the module-bucket fallback does not
    # build one either -- so a note placed there is sometimes silently dropped,
    # which is worse than a note in a slightly less apt place.
    banner_note = ('<p class="note source-note">%s</p>' % source_note
                   ) if source_note else ''

    controls = ('<span class="bulk"><button type="button" id="expand-all">expand all</button><button type="button" id="collapse-all">collapse all</button></span>')
    tab_html = ''.join(
        '<button role="tab" data-tab="%s" aria-selected="%s">%s'
        '<span class="count">%d</span></button>'
        % (esc(slug), 'true' if i == 0 else 'false', esc(label), count)
        for i, (slug, label, count) in enumerate(tabs)
    )
    panel_html = ''.join(
        '<div class="panel" id="%s" role="tabpanel"%s>%s</div>'
        % (esc(slug), '' if i == 0 else ' hidden', body)
        for i, (slug, body) in enumerate(panels)
    )

    profiles = ', '.join(m.label for m in selected) or 'none recognised'

    return (
        '<!doctype html>\n<html lang="en">\n<head>\n'
        '<meta charset="utf-8">\n'
        '<meta name="viewport" content="width=device-width,initial-scale=1">\n'
        '<title>%s</title>\n<style>%s</style>\n</head>\n<body>\n'
        '<div class="wrap">\n'
        '<header class="banner">\n  <div>%s</div>\n  <h1>%s</h1>\n'
        '  <div class="ids">%s</div>\n  %s\n</header>\n%s'
        '<nav class="tabs" role="tablist">%s%s</nav>\n%s\n'
        '<footer>Rendered from a CDIF JSON-LD record. Layout selected by declared '
        'conformance: %s.</footer>\n</div>\n<script>%s</script>\n</body>\n</html>\n'
        % (esc(title or name), CSS,
           ''.join('<span class="badge">%s</span>' % esc(t) for t in types),
           esc(name), ' '.join(ids), abstract, banner_note,
           tab_html, controls, panel_html,
           esc(profiles), JS)
    )


def render_index(entries, title='CDIF records'):
    """A catalogue page linking the records rendered in a batch run."""
    cards = []
    for e in entries:
        badges = ''.join('<span class="badge">%s</span>' % esc(p) for p in e['profiles'])
        desc = ('<div class="card-desc">%s</div>' % esc(e['description'][:240])
                if e['description'] else '')
        cards.append(
            '<li><a class="card-title" href="%s">%s</a>%s'
            '<div class="card-meta">%s</div>%s</li>'
            % (esc(e['href']), esc(e['name']),
               ('<div class="card-meta">%s</div>' % badges) if badges else '',
               esc(e['identifier'] or e['href']), desc))
    return (
        '<!doctype html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n'
        '<meta name="viewport" content="width=device-width,initial-scale=1">\n'
        '<title>%s</title>\n<style>%s</style>\n</head>\n<body>\n<div class="wrap">\n'
        '<header class="banner"><h1>%s</h1>'
        '<div class="ids">%d record%s</div></header>\n'
        '<ul class="cards">%s</ul>\n'
        '<footer>Rendered from CDIF JSON-LD records.</footer>\n'
        '</div>\n</body>\n</html>\n'
        % (esc(title), CSS, esc(title), len(entries),
           '' if len(entries) == 1 else 's', ''.join(cards))
    )


def load_record(path):
    """Return (record, error_message)."""
    try:
        record = json.loads(path.read_text(encoding='utf-8'))
    except OSError as exc:
        return None, 'cannot read %s: %s' % (path, exc)
    except json.JSONDecodeError as exc:
        return None, '%s is not valid JSON: %s' % (path, exc)
    if not isinstance(record, dict):
        return None, '%s is not a JSON object' % path
    return record, None


def collect_records(paths):
    """Expand the positional arguments into record files.

    A directory contributes its *.json files (non-recursively), skipping the
    generated *Schema.json artefacts that sit beside examples.
    """
    files = []
    for raw in paths:
        p = Path(raw)
        if p.is_dir():
            files.extend(sorted(q for q in p.glob('*.json')
                                if not q.name.endswith('Schema.json')
                                and q.name not in ('bblock.json', 'context.jsonld')))
        else:
            files.append(p)
    return files


def _record_summary(record, source, href, modules, type_index, offline, layouts=None):
    """One entry for the index page."""
    prefixes = record_context(record, offline=offline)
    _, _, selected, _ = build_tabs(record, modules, prefixes, type_index, layouts)
    name = record.get('schema:name')
    if isinstance(name, list):
        name = next((n for n in name if isinstance(n, str)), None)
    description = record.get('schema:description')
    if isinstance(description, list):
        description = next((d for d in description if isinstance(d, str)), '')
    return {
        'href': href,
        'name': name if isinstance(name, str) else (record.get('@id') or source.name),
        'identifier': record.get('@id') if isinstance(record.get('@id'), str) else '',
        'description': description if isinstance(description, str) else '',
        'profiles': [m.label for m in selected],
    }


def main(argv=None):
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('record', nargs='*',
                        help='CDIF JSON-LD record(s), or a directory of them')
    parser.add_argument('-o', '--output',
                        help='output HTML file, or a directory when rendering more '
                             'than one record (default: alongside each record)')
    parser.add_argument('--title', help='page title (default: schema:name)')
    parser.add_argument('--index', metavar='PATH',
                        help='also write a catalogue page linking every record '
                             'rendered in this run')
    parser.add_argument('--offline', action='store_true',
                        help='do not fetch remote @context documents')
    parser.add_argument('--profile-dir', action='append', type=Path,
                        help='directory of profile modules; repeatable')
    parser.add_argument('--list-profiles', action='store_true',
                        help='list discovered conformance URIs and exit')
    args = parser.parse_args(argv)

    dirs = args.profile_dir or DEFAULT_PROFILE_DIRS
    modules = load_modules(dirs)

    if args.list_profiles:
        for uri in sorted(modules):
            module = modules[uri]
            print('%-46s %-20s %3d properties'
                  % (uri, module.name, len(module.properties)))
        return 0

    if not args.record:
        parser.error('a record is required (or use --list-profiles)')

    sources = collect_records(args.record)
    if not sources:
        print('error: no record files found', file=sys.stderr)
        return 2

    many = len(sources) > 1
    out_dir = None
    if args.output:
        out_path = Path(args.output)
        if many or out_path.is_dir():
            out_dir = out_path
            out_dir.mkdir(parents=True, exist_ok=True)

    type_index = known_property_names(list(dict.fromkeys(modules.values())))
    layouts = load_layouts()

    entries, failures = [], 0
    for source in sources:
        record, error = load_record(source)
        if error:
            print('error: %s' % error, file=sys.stderr)
            failures += 1
            continue

        uris = declared_conformance(record)
        if not uris:
            print('warning: %s declares no %s -> dcterms:conformsTo; falling back '
                  'to the core profile' % (source, RECORD_PROPERTY), file=sys.stderr)
        for uri in uris:
            if uri not in modules:
                print('warning: %s declares unrecognised conformance URI %s'
                      % (source, uri), file=sys.stderr)

        if out_dir is not None:
            output = out_dir / (source.stem + '.html')
        elif args.output and not many:
            output = Path(args.output)
        else:
            output = source.with_suffix('.html')

        title = args.title if (args.title and not many) else None
        # A list too long to render inline goes to a sibling file; `parts`
        # comes back holding it. Keys beginning with __ are settings, not parts.
        parts = {'__href__': lambda slug, page=1, stem=output.stem:
                 '%s.%s.html' % (stem, slug) if page == 1
                 else '%s.%s.%d.html' % (stem, slug, page)}
        html = render_html(record, modules, title, offline=args.offline,
                           type_index=type_index, layouts=layouts,
                           filename=source.name, parts=parts)
        output.write_text(html, encoding='utf-8')
        print('wrote %s' % output)
        for slug, part in sorted(parts.items()):
            if slug.startswith('__'):
                continue
            pages = part_page_count(part)

            def page_name(n, stem=output.stem, slug=slug):
                # Page 1 keeps the plain name so the stub's link never changes.
                return ('%s.%s.html' % (stem, slug) if n == 1
                        else '%s.%s.%d.html' % (stem, slug, n))

            for n in range(1, pages + 1):
                side = output.with_name(page_name(n))
                side.write_text(
                    render_part_page(part, record, modules, offline=args.offline,
                                     back=output.name, page=n,
                                     page_href=page_name),
                    encoding='utf-8')
            print('wrote %s  (%d entries over %d page%s)'
                  % (output.with_name(page_name(1)), part['count'], pages,
                     '' if pages == 1 else 's'))
        entries.append(_record_summary(record, source, output, modules,
                                       type_index, args.offline, layouts))

    if args.index and entries:
        index_path = Path(args.index)
        if index_path.is_dir():
            index_path = index_path / 'index.html'
        index_path.parent.mkdir(parents=True, exist_ok=True)
        base = index_path.parent.resolve()
        for e in entries:
            target = Path(e['href']).resolve()
            try:
                e['href'] = target.relative_to(base).as_posix()
            except ValueError:
                e['href'] = target.as_uri()
        index_path.write_text(
            render_index(entries, args.title or 'CDIF records'), encoding='utf-8')
        print('wrote %s' % index_path)
    elif entries:
        for e in entries:
            e['href'] = str(e['href'])

    return 2 if failures and not entries else 0


if __name__ == '__main__':
    sys.exit(main())
