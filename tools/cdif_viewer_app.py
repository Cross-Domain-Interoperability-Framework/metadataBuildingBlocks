#!/usr/bin/env python3
"""Local viewer app: pick a CDIF JSON-LD file, see it rendered.

Starts a small server on localhost, opens a browser, and renders whatever
record you drop on the page or pick with the file dialog. The rendering is
cdif_record_to_html's -- this only adds the picker, so both stay in step.

Run on loopback, nothing is uploaded anywhere: the browser reads the file and
posts its text to the server on your own machine. Bound to 0.0.0.0 (as the
hosted deployment is), the record goes to whatever machine runs the server --
the picker page says which of the two applies.

USAGE:
  python tools/cdif_viewer_app.py                 # pick a file in the browser
  python tools/cdif_viewer_app.py --port 8800
  python tools/cdif_viewer_app.py --no-browser    # don't auto-open
  python tools/cdif_viewer_app.py --fetch-context # allow remote @context fetches
"""
from __future__ import annotations

import argparse
import ipaddress
import collections
import json
import os
import re
import socket
import sys
import threading
import urllib.error
import urllib.request
import time
import webbrowser
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import parse_qs, unquote, urlparse

sys.path.insert(0, str(Path(__file__).resolve().parent))
import cdif_record_to_html as R

# Split-out lists from recent renders, newest last:
# {token: (part, {'schema:name': ...})}. Pages are rendered on demand rather
# than up front, so a 9-page list costs one page of markup per request instead
# of nine. Only the list's own values are held -- not the whole record -- and
# the map is capped, since those values are the bulk of a large document.
PARTS = collections.OrderedDict()
PARTS_KEEP = 6

MAX_BYTES = 32 * 1024 * 1024


PICKER = """<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>CDIF record viewer</title>
<style>
:root{color-scheme:light dark;--fg:#1c1f24;--muted:#5b6472;--line:#dde2e8;
      --accent:#1c5d8c;--card:#f7f9fb;--bg:#fff}
@media (prefers-color-scheme:dark){:root{--fg:#e6e9ee;--muted:#98a2b3;--line:#2b3138;
      --accent:#7fb6dd;--card:#1b1f25;--bg:#14171b}}
body{margin:0;background:var(--bg);color:var(--fg);font:15px/1.55 -apple-system,
     BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif;
     /* flex-start, not center: a centred flex item taller than the viewport is
        clipped at the top and cannot be scrolled back to. The gallery made the
        page tall enough for that to bite. */
     display:flex;align-items:flex-start;justify-content:center;min-height:100vh}
.wrap{max-width:40rem;padding:2rem 2rem 4rem;width:100%}
h1{font-size:1.4rem;margin:0 0 .4rem}
p.sub{color:var(--muted);margin:0 0 1.5rem}
#drop{border:2px dashed var(--line);border-radius:10px;padding:3rem 1.5rem;
      text-align:center;background:var(--card);transition:border-color .15s}
#drop.over{border-color:var(--accent)}
button{font:inherit;padding:.5rem 1rem;border-radius:6px;border:1px solid var(--line);
       background:var(--bg);color:var(--fg);cursor:pointer}
button:hover{border-color:var(--accent);color:var(--accent)}
.hint{color:var(--muted);font-size:.85rem;margin-top:.8rem}
#err{color:#b00;background:#fee;border:1px solid #fbb;border-radius:6px;
     padding:.7rem .9rem;margin-top:1rem;display:none;white-space:pre-wrap}
@media (prefers-color-scheme:dark){#err{background:#2a1416;border-color:#63272b;color:#f3b0b0}}
#urlform{display:flex;gap:.5rem;margin-top:1rem}
#url{flex:1;padding:.5rem .6rem;border:1px solid #3a4353;border-radius:6px;
     background:#151a22;color:inherit;font:inherit}
#url:focus{outline:none;border-color:#7aa2f7}
#urlform button{padding:.5rem .9rem}
.urlnote{margin:.5rem 0 0;font-size:.8rem}
.g-head{font-size:.95rem;margin:1.8rem 0 .6rem;font-weight:600}
.g-sub{font-size:.78rem;margin:1rem 0 .4rem;color:var(--muted);font-weight:600;
       text-transform:uppercase;letter-spacing:.04em}
.gallery{list-style:none;margin:0;padding:0;display:grid;gap:.5rem}
.gallery a{display:block;padding:.6rem .8rem;border:1px solid var(--line);
           border-radius:8px;text-decoration:none;color:inherit;
           background:var(--card)}
.gallery a:hover{border-color:var(--accent)}
.s-name{display:block;font-weight:600;font-size:.9rem}
.s-blurb{display:block;color:var(--muted);font-size:.82rem;margin-top:.15rem}
.profiles{margin-top:1.6rem;font-size:.82rem;color:var(--muted)}
.profiles code{font-size:.9em}
__BRANDCSS__</style></head><body><div class="wrap">
__HEADER__
<h1>CDIF record viewer</h1>
<p class="sub">Drop a CDIF JSON-LD record here, or pick one.__WHERE__</p>
<div id="drop">
  <button id="pick">Choose a file&hellip;</button>
  <input id="file" type="file" accept=".json,.jsonld,application/json" hidden>
  <div class="hint">or drag a <code>.json</code> / <code>.jsonld</code> file onto this box</div>
</div>
<form id="urlform">
  <input id="url" type="url" placeholder="https://example.org/dataset.jsonld or a landing page"
         spellcheck="false">
  <button type="submit">Open URL</button>
</form>
<p class="sub urlnote">A URL is fetched by this server, not your browser, and may
be a JSON-LD record or a page with an embedded
<code>application/ld+json</code> record.</p>
<div id="err"></div>
__GALLERY__
<div class="profiles">Layout is chosen from the record's
<code>subjectOf &rarr; dcterms:conformsTo</code>. Profiles recognised:<br>__PROFILES__</div>
__FOOTER__
</div>
<script>
const drop = document.getElementById('drop'), input = document.getElementById('file'),
      err = document.getElementById('err');
document.getElementById('pick').onclick = () => input.click();
input.onchange = () => input.files[0] && send(input.files[0]);
['dragenter','dragover'].forEach(e => drop.addEventListener(e, ev => {
  ev.preventDefault(); drop.classList.add('over'); }));
['dragleave','drop'].forEach(e => drop.addEventListener(e, ev => {
  ev.preventDefault(); drop.classList.remove('over'); }));
drop.addEventListener('drop', ev => {
  const f = ev.dataTransfer.files[0]; if (f) send(f);
});
document.getElementById('urlform').addEventListener('submit', async ev => {
  ev.preventDefault();
  const u = document.getElementById('url').value.trim();
  if (!u) return;
  err.style.display = 'none';
  try {
    const res = await fetch('/open', {method: 'POST', body: u});
    const text = await res.text();
    if (!res.ok) { err.textContent = text; err.style.display = 'block'; return; }
    document.open(); document.write(text); document.close();
  } catch (e) { err.textContent = String(e); err.style.display = 'block'; }
});
function send(file) {
  err.style.display = 'none';
  const reader = new FileReader();
  reader.onload = async () => {
    try {
      const res = await fetch('/render?name=' + encodeURIComponent(file.name), {
        method: 'POST', headers: {'Content-Type': 'application/json'}, body: reader.result});
      const text = await res.text();
      if (!res.ok) { err.textContent = text; err.style.display = 'block'; return; }
      document.open(); document.write(text); document.close();
    } catch (e) { err.textContent = String(e); err.style.display = 'block'; }
  };
  reader.readAsText(file);
}
</script>
</body></html>
"""


def _vocab_note(record, url, embedded=False):
    """A note for the Metadata Record panel: where this came from, and whether
    its @vocab put schema.org terms in the https namespace.

    Only an @vocab of https://schema.org/ is flagged. A STRING context of
    "https://schema.org/" references schema.org's own context document, which
    defines schema: as http://schema.org/, so its terms already expand to the
    IRIs CDIF uses and nothing is wrong with it.
    """
    where = 'Fetched from <code>%s</code>%s.' % (
        R.esc(url), ' &mdash; from JSON-LD embedded in the page' if embedded else '')
    ctx = (record or {}).get('@context')
    vocab = R.https_vocab_note(ctx)
    if not vocab:
        return where
    expands = R.vocab_expands_to(ctx) or ''
    if expands and not expands.startswith(vocab.rstrip('/') + '/'):
        # A slashless @vocab is concatenated straight onto the term, so this is
        # not merely the wrong namespace -- it is not a schema.org IRI at all.
        detail = (
            'The source declares <code>"@vocab": "%s"</code> with no trailing '
            'slash, so JSON-LD concatenates it onto each term: <code>name</code> '
            'expands to <code>%s</code>, which is not a schema.org IRI at all. '
            'The terms were read as schema.org and mapped to '
            '<code>http://schema.org/</code> for display.'
            % (R.esc(vocab), R.esc(expands)))
    else:
        detail = (
            'The source declares <code>"@vocab": "%s"</code>, so its terms expand '
            'to the <code>https://schema.org/</code> namespace. CDIF binds '
            '<code>schema:</code> to <code>http://schema.org/</code>, which is a '
            'different IRI; the terms were mapped to it for display. (A string '
            '<code>"@context": "https://schema.org/"</code> would be fine &mdash; '
            'it references the schema.org context document, which defines the '
            'http form.)' % R.esc(vocab))
    return '%s %s' % (where, detail)


FETCH_TIMEOUT = 20
FETCH_MAX_BYTES = 32 * 1024 * 1024


def _is_public_host(host):
    """False for anything that resolves only to a private or local address.

    The viewer fetches on the caller's behalf, so without this a hosted
    instance would happily read things on its own network -- cloud metadata
    endpoints, internal admin pages -- that its caller cannot reach.
    """
    try:
        infos = socket.getaddrinfo(host, None)
    except socket.gaierror:
        return False
    for info in infos:
        addr = info[4][0]
        try:
            ip = ipaddress.ip_address(addr.split('%')[0])
        except ValueError:
            return False
        if (ip.is_private or ip.is_loopback or ip.is_link_local
                or ip.is_multicast or ip.is_reserved or ip.is_unspecified):
            return False
    return True


def fetch_record(url, allowed_types):
    """(record, note) for a URL, or raises ValueError with a readable reason.

    Accepts a JSON-LD document, or an HTML page carrying the record in a
    <script type="application/ld+json">.
    """
    parsed = urlparse(url)
    if parsed.scheme not in ('http', 'https'):
        raise ValueError('Only http and https URLs can be opened.')
    if not parsed.hostname:
        raise ValueError('That URL has no host.')
    if not _is_public_host(parsed.hostname):
        raise ValueError('That host resolves to a private or local address, '
                         'which this viewer will not fetch.')

    req = urllib.request.Request(url, headers={
        'User-Agent': 'CDIF-record-viewer/1.0',
        'Accept': 'application/ld+json, application/json;q=0.9, text/html;q=0.8',
    })
    try:
        with urllib.request.urlopen(req, timeout=FETCH_TIMEOUT) as resp:
            ctype = (resp.headers.get('Content-Type') or '').lower()
            body = resp.read(FETCH_MAX_BYTES + 1)
    except urllib.error.HTTPError as exc:
        raise ValueError('The server returned HTTP %s.' % exc.code)
    except Exception as exc:
        raise ValueError('Could not fetch that URL: %s' % exc)
    if len(body) > FETCH_MAX_BYTES:
        raise ValueError('That document is larger than %d MB.'
                         % (FETCH_MAX_BYTES // (1024 * 1024)))

    text = body.decode('utf-8', errors='replace')
    looks_json = ('json' in ctype
                  or parsed.path.endswith(('.json', '.jsonld'))
                  or text.lstrip()[:1] in '{[')
    if looks_json:
        try:
            doc = json.loads(text)
        except json.JSONDecodeError as exc:
            raise ValueError('That URL is not valid JSON: %s' % exc)
        record = doc if isinstance(doc, dict) and '@graph' not in doc else None
        if record is None:
            record = R.find_record_node(doc, allowed_types) or (
                doc if isinstance(doc, dict) else None)
        if record is None:
            raise ValueError('No CDIF record found in that JSON document.')
        # Same normalization the HTML path gets. A server that honours our
        # Accept header -- PANGAEA does -- returns the JSON-LD directly, so this
        # branch sees exactly the schema.org-vocab records the other one does.
        return R.normalize_schemaorg(record), _vocab_note(record, url)

    record = R.extract_jsonld(text, allowed_types)
    if record is None:
        raise ValueError(
            'That page has no embedded JSON-LD typed as a CDIF record '
            '(one of: %s).' % ', '.join(t.split(':')[-1] for t in allowed_types))
    return record, _vocab_note(record, url, embedded=True)


# Sample records offered on the picker page: (slug, path, blurb). Paths are
# relative to the repo root, so they travel with the deployment.
#
# Chosen to span the range rather than to impress -- someone opening this
# should be able to see a small record and a rich one, a table and a domain
# profile, without hunting.
# Raw-content bases for the sibling repositories. Note the doc-* repos are on
# reviewRevision202606, not main -- a main URL there 404s.
_GH = 'https://raw.githubusercontent.com/Cross-Domain-Interoperability-Framework/'
RAW_VALIDATION = _GH + 'validation/main/'
RAW_DOC = _GH + '%s/reviewRevision202606/'

# The gallery, grouped. `src` is either a path inside this repo or a URL fetched
# through the same code a pasted URL uses. Chosen to span what CDIF has to
# describe rather than to flatter it: hand-written profile examples, machine
# conversions from four other formats, and records harvested from live
# repositories that were never written with CDIF in mind.
SAMPLES = [
    ('Profile examples, written to show a profile', [
        ('_sources/profiles/cdifCompositeProfile/CoreDiscovery/'
         'exampleCDIFDiscoveryMinimal.json',
         'The smallest useful record: core plus discovery, seven properties.'),
        ('_sources/profiles/cdifCompositeProfile/CoreDiscovery/'
         'exampleCDIFDiscoveryComplete.json',
         'The same profile filled in: agents, coverage, distributions, funding.'),
        ('_sources/profiles/cdifCompositeProfile/DiscoveryDataDescription/'
         'exampleCDIFDataDescriptionComplete.json',
         'Adds described variables -- what the dataset actually measures.'),
        ('_sources/profiles/cdifCompositeProfile/'
         'DiscoveryDataDescriptionStructure/'
         'exampleCDIFDataStructureComplete.json',
         'A long-format table: components, keys, and how a file maps to them.'),
        ('_sources/profiles/cdifCompositeProfile/cdifComplete/'
         'exampleCDIFcomplete.json',
         'Every module at once -- six declared profiles, provenance included.'),
        ('_sources/profiles/cdifCompositeProfile/xasDocument/'
         'exampleCDIFxas.json',
         'A domain profile: X-ray absorption spectroscopy, with its own tabs.'),
    ]),

    ('Converted from other metadata formats', [
        (RAW_VALIDATION + 'converters/DDICodebook/Examples/cdif/'
         'cdif_MWI_2019_MICS_v01_M.json',
         'DDI Codebook: a household survey. 1793 variables and a physical '
         'mapping per column, so the variable list gets its own paged view.'),
        (RAW_VALIDATION + 'converters/croissant/MLCroissantExamples/'
         'cdif-output/hf-imdb-cdif.jsonld',
         'Croissant: a Hugging Face machine-learning dataset.'),
        (RAW_VALIDATION + 'converters/DCAT/cdifOK/01-dcat-ap/3.0.0-hvd/'
         'example-ms_dataset_2_distributions__dcat-the-population-of-bees.jsonld',
         'DCAT-AP: two distributions, with high-value-dataset terms carried '
         'through as extensions.'),
        (RAW_VALIDATION + 'converters/DDI-CDI/Examples/cdif/'
         'cdif_SPSS_Example.json',
         'DDI-CDI XML: a data structure with coded value domains.'),
    ]),

    ('Harvested from live repositories', [
        (RAW_DOC % 'doc-corediscovery' +
         'examples/GeoCodes-earthchem-dataset.jsonld',
         'EarthChem, via GeoCodes: electron microprobe glass analyses.'),
        (RAW_DOC % 'doc-corediscovery' +
         'examples/GeoCodes-opentopography-dataset.jsonld',
         'OpenTopography: airborne lidar over Diablo Canyon.'),
        (RAW_DOC % 'doc-corediscovery' +
         'examples/GeoCodes-pangaea-dataset.jsonld',
         'PANGAEA: a global map of nitrogen application.'),
        (RAW_DOC % 'doc-corediscovery' + 'examples/ESIP-fullDataset.jsonld',
         'The ESIP science-on-schema.org reference record.'),
        (RAW_DOC % 'doc-discoverydatadescription' +
         'examples/CMIP-NetCDF/NetCDF-CDIF-UKESM1-0-LL.jsonLD',
         'A CMIP6 climate model run, described from its NetCDF headers.'),
        (RAW_DOC % 'doc-discoverydatadescription' +
         'examples/CDIF2026/cdif_10.60707-0y88-ps96.json',
         'Astromat: titanium isotope measurements.'),
    ]),
]


def available_samples(root):
    """(slug, source, blurb, label) for each usable sample.

    A local sample is checked on disk: a renamed example should quietly leave
    the gallery rather than 404 for whoever clicks it. A remote one is not
    fetched here -- reaching out to GitHub at boot would make this service's
    health depend on someone else's -- so a dead link surfaces when clicked,
    carrying the fetch error the URL path already produces.
    """
    out, used = [], set()
    for group, entries in SAMPLES:
        for src, blurb in entries:
            name = src.rsplit('/', 1)[-1]
            slug = re.sub(r'[^a-z0-9]+', '-',
                          name.rsplit('.', 1)[0].lower()).strip('-') or 'sample'
            while slug in used:
                slug += '-2'
            used.add(slug)
            if src.startswith(('http://', 'https://')):
                out.append((slug, src, blurb, name, group))
            else:
                path = root / src
                if path.is_file():
                    out.append((slug, path, blurb, path.stem, group))
    return out


class Handler(BaseHTTPRequestHandler):
    server_is_shared = False
    samples = ()
    modules = {}
    known = set()
    layouts = []
    offline = True

    def log_message(self, fmt, *args):        # quiet: one line per render instead
        pass

    def _send(self, code, body, ctype='text/html; charset=utf-8'):
        data = body.encode('utf-8') if isinstance(body, str) else body
        self.send_response(code)
        self.send_header('Content-Type', ctype)
        self.send_header('Content-Length', str(len(data)))
        self.end_headers()
        self.wfile.write(data)

    def do_GET(self):
        if self.path.startswith('/sample/'):
            slug = self.path[len('/sample/'):].split('?', 1)[0]
            match = next((s for s in self.samples if s[0] == slug), None)
            if match is None:
                self._send(404, 'No such sample.', 'text/plain; charset=utf-8')
                return
            _, source, _, label, _group = match
            if isinstance(source, str):          # converter output, fetched
                try:
                    record, note = fetch_record(source, R.record_types(self.modules))
                except ValueError as exc:
                    self._send(502, 'Could not fetch that sample:\n%s' % exc,
                               'text/plain; charset=utf-8')
                    return
            else:                                 # ships with this repo
                try:
                    record = json.loads(source.read_text(encoding='utf-8'))
                except Exception as exc:
                    self._send(500, 'Could not read that sample: %s' % exc,
                               'text/plain; charset=utf-8')
                    return
                note = ('Sample record shipped with the building blocks: '
                        '<code>%s</code>.' % R.esc(label))
            self._render_record(record, label, note)
            return
        if self.path.startswith('/part/'):
            path, _, query = self.path[len('/part/'):].partition('?')
            token = path
            held = PARTS.get(token)
            if held is None:
                self._send(404, 'That list is no longer held in memory. '
                           'Render the record again.',
                           'text/plain; charset=utf-8')
                return
            part, stub = held
            try:
                page = int(parse_qs(query).get('page', ['1'])[0])
            except (TypeError, ValueError):
                page = 1
            self._send(200, R.render_part_page(
                part, stub, self.modules, offline=self.offline, page=page,
                page_href=lambda n, t=token: '/part/%s?page=%d' % (t, n)))
            return
        if self.path not in ('/', '/index.html'):
            self._send(404, 'not found', 'text/plain; charset=utf-8')
            return
        listed = ', '.join('<code>%s</code>' % R.esc(u.rsplit('/cdif/', 1)[-1])
                           for u in sorted(self.modules))
        # Say honestly where the record goes. Served on loopback it never
        # leaves the machine; hosted, the browser posts its text to the server,
        # and claiming otherwise on a public deployment would be a lie.
        where = (' It renders on this server: the record is sent there, held only'
                 ' for the render, and not stored.' if self.server_is_shared
                 else ' It renders locally &mdash; nothing leaves your machine.')
        groups = []
        for _slug, _src, _blurb, _label, group in self.samples:
            if group not in groups:
                groups.append(group)
        sections = []
        for group in groups:
            cards = ''.join(
                '<li><a href="/sample/%s"><span class="s-name">%s</span>'
                '<span class="s-blurb">%s</span></a></li>'
                % (R.esc(slug), R.esc(label), R.esc(blurb))
                for slug, _src, blurb, label, g in self.samples if g == group)
            sections.append('<h3 class="g-sub">%s</h3><ul class="gallery">%s</ul>'
                            % (R.esc(group), cards))
        gallery = ('<h2 class="g-head">Or look at a sample</h2>%s'
                   % ''.join(sections)) if sections else ''
        self._send(200, PICKER.replace('__PROFILES__', listed or '(none found)')
                   .replace('__WHERE__', where)
                   .replace('__GALLERY__', gallery)
                   # the CDIF banner and footer, from the renderer, so the
                   # picker and the record pages carry the same site chrome
                   .replace('__BRANDCSS__', R.BRAND_CSS)
                   .replace('__HEADER__', R.site_header())
                   .replace('__FOOTER__', R.site_footer()))

    def do_POST(self):
        if self.path.startswith('/open'):
            length = int(self.headers.get('Content-Length') or 0)
            url = (self.rfile.read(length).decode('utf-8', 'replace').strip()
                   if 0 < length <= 4096 else '')
            if not url:
                self._send(400, 'No URL given.', 'text/plain; charset=utf-8')
                return
            try:
                record, note = fetch_record(url, R.record_types(self.modules))
            except ValueError as exc:
                self._send(400, str(exc), 'text/plain; charset=utf-8')
                return
            if not isinstance(record, dict):
                self._send(400, 'That URL did not yield a single record object.',
                           'text/plain; charset=utf-8')
                return
            self._render_record(record, url.rsplit('/', 1)[-1] or url, note)
            return
        if not self.path.startswith('/render'):
            self._send(404, 'not found', 'text/plain; charset=utf-8')
            return
        length = int(self.headers.get('Content-Length') or 0)
        if length <= 0 or length > MAX_BYTES:
            self._send(413, 'File is empty or larger than %d MB.'
                       % (MAX_BYTES // (1024 * 1024)), 'text/plain; charset=utf-8')
            return
        raw = self.rfile.read(length)
        try:
            record = json.loads(raw.decode('utf-8'))
        except (UnicodeDecodeError, json.JSONDecodeError) as exc:
            self._send(400, 'Not valid JSON:\n%s' % exc, 'text/plain; charset=utf-8')
            return
        if not isinstance(record, dict):
            self._send(400, 'Not a JSON object -- a CDIF record is a single object.',
                       'text/plain; charset=utf-8')
            return
        name = unquote(self.path.partition('name=')[2]) or '(record)'
        self._render_record(record, name)
        return

    def _render_record(self, record, name, note=None):
        """Render one record and reply. Shared by the file and URL paths."""
        # A list too long to render inline comes back in `parts`; it is served
        # from memory at /part/<token> rather than inflating this response.
        stamp = '%d' % (time.time() * 1000)
        parts = {'__href__': lambda slug, page=1, s=stamp:
                 '/part/%s-%s' % (s, slug) + ('' if page == 1
                                              else '?page=%d' % page)}
        try:
            html = R.render_html(record, self.modules, offline=self.offline,
                                 type_index=self.known, layouts=self.layouts,
                                 filename=name, parts=parts, source_note=note)
        except Exception as exc:               # a malformed record should not kill the app
            self._send(500, 'Could not render:\n%s: %s' % (type(exc).__name__, exc),
                       'text/plain; charset=utf-8')
            return
        for slug, part in parts.items():
            if slug.startswith('__'):
                continue
            # Keep the part, not a rendered page: the pager needs to render any
            # page on request. Only the record's name travels with it.
            PARTS['%s-%s' % (stamp, slug)] = (
                part, {'schema:name': record.get('schema:name')})
            while len(PARTS) > PARTS_KEEP:
                PARTS.popitem(last=False)

        uris = R.declared_conformance(record)
        unknown = [u for u in uris if R.resolve_module(u, self.modules,
                                                       R.modules_by_stem(self.modules))[0] is None]
        print('rendered %s  [%d declared, %d unrecognised]'
              % (name, len(uris), len(unknown)))
        self._send(200, html)


def free_port(preferred):
    with socket.socket() as s:
        try:
            s.bind(('127.0.0.1', preferred))
            return preferred
        except OSError:
            s.bind(('127.0.0.1', 0))
            return s.getsockname()[1]


def main(argv=None):
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    # PORT and HOST come from the environment when hosted: Render assigns the
    # port and requires binding 0.0.0.0, since 127.0.0.1 is unreachable from
    # outside the container and the deploy is failed as unhealthy.
    p.add_argument('--port', type=int,
                   default=int(os.environ.get('PORT') or 8765))
    p.add_argument('--host', default=os.environ.get('HOST') or '127.0.0.1',
                   help='bind address (default loopback; 0.0.0.0 to serve '
                        'others, which the hosted deployment sets)')
    p.add_argument('--no-browser', action='store_true')
    p.add_argument('--fetch-context', action='store_true',
                   help='allow fetching remote @context documents')
    p.add_argument('--profile-dir', action='append', type=Path,
                   help='directory of profile modules; repeatable')
    args = p.parse_args(argv)

    dirs = args.profile_dir or R.DEFAULT_PROFILE_DIRS
    Handler.modules = R.load_modules(dirs)
    Handler.known = R.known_property_names(list(dict.fromkeys(Handler.modules.values())))
    Handler.layouts = R.load_layouts()
    Handler.offline = not args.fetch_context
    Handler.server_is_shared = args.host not in ('127.0.0.1', 'localhost', '::1')
    Handler.samples = available_samples(R.REPO)

    # Only hunt for a free port locally. If a hosting platform names a port,
    # binding a different one means the service is never reachable -- silently,
    # since the process starts fine.
    port = args.port if os.environ.get('PORT') else free_port(args.port)
    url = 'http://%s:%d/' % ('127.0.0.1' if args.host in ('0.0.0.0', '::')
                             else args.host, port)
    server = ThreadingHTTPServer((args.host, port), Handler)
    print('CDIF record viewer on %s (bound to %s)' % (url, args.host))
    print('  %d profiles, %d curated layouts%s'
          % (len(Handler.modules), len(Handler.layouts),
             '' if Handler.offline else ', remote @context enabled'))
    print('  Ctrl-C to stop')
    if not args.no_browser and not os.environ.get('PORT'):
        threading.Timer(0.4, webbrowser.open, args=(url,)).start()
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print('\nstopped')
    return 0


if __name__ == '__main__':
    sys.exit(main())
