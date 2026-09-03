#!/usr/bin/env python3
"""Local viewer app: pick a CDIF JSON-LD file, see it rendered.

Starts a small server on localhost, opens a browser, and renders whatever
record you drop on the page or pick with the file dialog. The rendering is
cdif_record_to_html's -- this only adds the picker, so both stay in step.

Nothing is uploaded anywhere: the browser reads the file locally and posts its
text to the server running on your own machine.

USAGE:
  python tools/cdif_viewer_app.py                 # pick a file in the browser
  python tools/cdif_viewer_app.py --port 8800
  python tools/cdif_viewer_app.py --no-browser    # don't auto-open
  python tools/cdif_viewer_app.py --fetch-context # allow remote @context fetches
"""
from __future__ import annotations

import argparse
import json
import socket
import sys
import threading
import webbrowser
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import unquote

sys.path.insert(0, str(Path(__file__).resolve().parent))
import cdif_record_to_html as R

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
     display:flex;align-items:center;justify-content:center;min-height:100vh}
.wrap{max-width:40rem;padding:2rem;width:100%}
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
.profiles{margin-top:1.6rem;font-size:.82rem;color:var(--muted)}
.profiles code{font-size:.9em}
</style></head><body><div class="wrap">
<h1>CDIF record viewer</h1>
<p class="sub">Drop a CDIF JSON-LD record here, or pick one. It renders locally &mdash;
nothing leaves your machine.</p>
<div id="drop">
  <button id="pick">Choose a file&hellip;</button>
  <input id="file" type="file" accept=".json,.jsonld,application/json" hidden>
  <div class="hint">or drag a <code>.json</code> / <code>.jsonld</code> file onto this box</div>
</div>
<div id="err"></div>
<div class="profiles">Layout is chosen from the record's
<code>subjectOf &rarr; dcterms:conformsTo</code>. Profiles recognised:<br>__PROFILES__</div>
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
</script></body></html>
"""


class Handler(BaseHTTPRequestHandler):
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
        if self.path not in ('/', '/index.html'):
            self._send(404, 'not found', 'text/plain; charset=utf-8')
            return
        listed = ', '.join('<code>%s</code>' % R.esc(u.rsplit('/cdif/', 1)[-1])
                           for u in sorted(self.modules))
        self._send(200, PICKER.replace('__PROFILES__', listed or '(none found)'))

    def do_POST(self):
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
        try:
            html = R.render_html(record, self.modules, offline=self.offline,
                                 type_index=self.known, layouts=self.layouts,
                                 filename=name)
        except Exception as exc:               # a malformed record should not kill the app
            self._send(500, 'Could not render:\n%s: %s' % (type(exc).__name__, exc),
                       'text/plain; charset=utf-8')
            return
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
    p.add_argument('--port', type=int, default=8765)
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

    port = free_port(args.port)
    url = 'http://127.0.0.1:%d/' % port
    server = ThreadingHTTPServer(('127.0.0.1', port), Handler)
    print('CDIF record viewer on %s' % url)
    print('  %d profiles, %d curated layouts%s'
          % (len(Handler.modules), len(Handler.layouts),
             '' if Handler.offline else ', remote @context enabled'))
    print('  Ctrl-C to stop')
    if not args.no_browser:
        threading.Timer(0.4, webbrowser.open, args=(url,)).start()
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print('\nstopped')
    return 0


if __name__ == '__main__':
    sys.exit(main())
