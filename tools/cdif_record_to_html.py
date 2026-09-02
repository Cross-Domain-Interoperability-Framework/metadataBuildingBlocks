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

USAGE:
  python tools/cdif_record_to_html.py record.json
  python tools/cdif_record_to_html.py record.json -o out.html
  python tools/cdif_record_to_html.py --list-profiles
"""
from __future__ import annotations

import argparse
import html
import json
import re
import sys
from pathlib import Path

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

def record_context(record):
    """Prefix -> namespace map from the record's @context.

    Only the inline object form is used; a remote context would need a fetch,
    and CURIEs that cannot be expanded are simply rendered as text.
    """
    context = record.get('@context')
    entries = context if isinstance(context, list) else [context]
    prefixes = {}
    for entry in entries:
        if isinstance(entry, dict):
            for key, value in entry.items():
                if isinstance(value, str):
                    prefixes[key] = value
                elif isinstance(value, dict) and isinstance(value.get('@id'), str):
                    prefixes[key] = value['@id']
    return prefixes


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


def render_value(value, prefixes, depth=0):
    if value is None:
        return '<span class="empty">null</span>'
    if isinstance(value, (str, int, float, bool)):
        return render_scalar(value, prefixes)
    if isinstance(value, list):
        if not value:
            return '<span class="empty">(none)</span>'
        items = ''.join('<li>%s</li>' % render_value(v, prefixes, depth) for v in value)
        return '<ul class="vals">%s</ul>' % items
    if isinstance(value, dict):
        return render_node(value, prefixes, depth)
    return '<span class="lit">%s</span>' % esc(value)


def render_node(node, prefixes, depth=0):
    """A JSON-LD object: a bare {@id} becomes a link, anything richer a card."""
    keys = [k for k in node if k != '@context']
    if keys == ['@id']:
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

    rows = []
    for key in keys:
        if key in shown_keys:
            continue
        rows.append(
            '<div class="row"><div class="key" title="%s">%s'
            '<span class="curie">%s</span></div>'
            '<div class="val">%s</div></div>'
            % (esc(key), esc(humanize(key)), esc(key),
               render_value(node[key], prefixes, depth + 1))
        )

    header = '<div class="node-head">%s</div>' % ''.join(head) if head else ''
    body = '<div class="node-body">%s</div>' % ''.join(rows) if rows else ''
    if not header and not body:
        return '<span class="empty">(empty)</span>'
    return '<div class="node">%s%s</div>' % (header, body)


def render_property(name, value, description, prefixes):
    tip = ' title="%s"' % esc(description) if description else ''
    note = '<div class="desc">%s</div>' % esc(description) if description else ''
    return (
        '<section class="prop">'
        '<h3%s>%s<span class="curie">%s</span></h3>'
        '%s'
        '<div class="prop-val">%s</div>'
        '</section>'
        % (tip, esc(humanize(name)), esc(name), note,
           render_value(value, prefixes))
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
.abstract{margin:.5rem 0 0;max-width:80ch}
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
.prop{margin:0 0 1.4rem}
.prop > h3{margin:0 0 .1rem;font-size:1rem;border-bottom:1px solid var(--line);padding-bottom:.2rem}
.curie{color:var(--muted);font-weight:400;font-size:.75rem;
       font-family:ui-monospace,SFMono-Regular,Consolas,monospace;margin-left:.5rem}
.desc{color:var(--muted);font-size:.82rem;margin:.25rem 0 .45rem;max-width:80ch}
.prop-val{margin-top:.35rem}
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
.note{background:var(--warnbg);color:var(--warn);border:1px solid var(--line);
      border-radius:5px;padding:.5rem .7rem;margin:0 0 1.25rem;font-size:.85rem;max-width:80ch}
footer{margin-top:2.5rem;padding-top:.75rem;border-top:1px solid var(--line);
       color:var(--muted);font-size:.78rem}
@media(max-width:620px){.row{grid-template-columns:1fr;gap:.1rem}
 .row > .key .curie{display:inline;margin-left:.4rem}}
"""

JS = """
document.querySelectorAll('nav.tabs button').forEach(function(b){
  b.addEventListener('click', function(){
    document.querySelectorAll('nav.tabs button').forEach(function(o){
      o.setAttribute('aria-selected', String(o === b));
    });
    document.querySelectorAll('.panel').forEach(function(p){
      p.hidden = (p.id !== b.dataset.tab);
    });
    if (history.replaceState) history.replaceState(null, '', '#' + b.dataset.tab);
  });
});
if (location.hash) {
  var initial = document.querySelector('nav.tabs button[data-tab="' + location.hash.slice(1) + '"]');
  if (initial) initial.click();
}
"""


def build_tabs(record, modules, prefixes):
    """Assign each root property to a tab and render the panels."""
    uris = declared_conformance(record)
    selected, unknown_uris = [], []
    for uri in uris:
        module = modules.get(uri)
        if module is None:
            unknown_uris.append(uri)
        elif module not in selected:
            selected.append(module)
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
            body = ''.join(render_property(n, record[n], described.get(n, ''), prefixes)
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
                                described.get(RECORD_PROPERTY, ''), prefixes)
        add('record', 'Metadata Record', 1, body)

    if extra:
        body = ('<p class="note">Present in the record but not defined by any declared '
                'CDIF profile. Shown so nothing is dropped; these are not validated '
                'by the profiles above.</p>')
        body += ''.join(render_property(n, record[n], '', prefixes) for n in extra)
        add('additional', 'Additional', len(extra), body)

    return tabs, panels, selected, unknown_uris


def render_html(record, modules, title=None):
    prefixes = record_context(record)
    tabs, panels, selected, _ = build_tabs(record, modules, prefixes)

    name = record.get('schema:name')
    if isinstance(name, list):
        name = next((n for n in name if isinstance(n, str)), None)
    if not isinstance(name, str):
        name = record.get('@id') or 'CDIF metadata record'

    types = type_names(record)
    identifier = record.get('@id')
    ids = []
    if identifier:
        url = expand(identifier, prefixes)
        ids.append(render_link(url, identifier) if url else esc(identifier))

    description = record.get('schema:description')
    abstract = ''
    if description is not None:
        abstract = '<div class="abstract">%s</div>' % render_value(description, prefixes)

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
        '  <div class="ids">%s</div>\n  %s\n</header>\n'
        '<nav class="tabs" role="tablist">%s</nav>\n%s\n'
        '<footer>Rendered from a CDIF JSON-LD record. Layout selected by declared '
        'conformance: %s.</footer>\n</div>\n<script>%s</script>\n</body>\n</html>\n'
        % (esc(title or name), CSS,
           ''.join('<span class="badge">%s</span>' % esc(t) for t in types),
           esc(name), ' '.join(ids), abstract, tab_html, panel_html,
           esc(profiles), JS)
    )


def main(argv=None):
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('record', nargs='?', help='CDIF JSON-LD metadata record')
    parser.add_argument('-o', '--output', help='output HTML file (default: <record>.html)')
    parser.add_argument('--title', help='page title (default: schema:name)')
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

    source = Path(args.record)
    try:
        record = json.loads(source.read_text(encoding='utf-8'))
    except OSError as exc:
        print('error: cannot read %s: %s' % (source, exc), file=sys.stderr)
        return 2
    except json.JSONDecodeError as exc:
        print('error: %s is not valid JSON: %s' % (source, exc), file=sys.stderr)
        return 2

    if not isinstance(record, dict):
        print('error: %s is not a JSON object' % source, file=sys.stderr)
        return 2

    uris = declared_conformance(record)
    if not uris:
        print('warning: %s declares no %s -> dcterms:conformsTo; falling back to '
              'the core profile' % (source, RECORD_PROPERTY), file=sys.stderr)
    for uri in uris:
        if uri not in modules:
            print('warning: unrecognised conformance URI %s' % uri, file=sys.stderr)

    output = Path(args.output) if args.output else source.with_suffix('.html')
    output.write_text(render_html(record, modules, args.title), encoding='utf-8')
    print('wrote %s' % output)
    return 0


if __name__ == '__main__':
    sys.exit(main())
