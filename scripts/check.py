#!/usr/bin/env python3
"""Check public provenance, generated parity, asset hashes and local Markdown destinations."""
import json,re,hashlib
from pathlib import Path
R=Path(__file__).resolve().parents[1]
a=json.loads((R/'data/reference.json').read_text())
index=(R/'docs/index.html').read_text()
assert len({c['id'] for c in a['claims']})==len(a['claims'])
ss={s['id']:s for s in a['sources']}
for c in a['claims']:
 assert c['source_id'] in ss and c['location'] and c['era']
 assert c['evidence'] in ('first-hand','qualified-recollection','publisher-report')
 assert f'id="{c["id"]}"' in index
for s in a['sources']:
 assert (R/s['file']).exists()
 assert (R/s['file']).read_text().startswith('Source: '+s['url'])
 assert f'id="source-{s["id"]}"' in index
for name,src in [('reference.json','data/reference.json')]:
 assert (R/'docs'/name).read_bytes()==(R/src).read_bytes()
for p in R.rglob('*'):
 if not p.is_file() or '.git' in p.parts or '__pycache__' in p.parts:continue
 assert p.suffix.lower() not in ['.mp3','.mp4','.wav','.vtt','.srt'],p
 if p.suffix.lower() in ['.png','.jpg','.jpeg','.webp']:
  assert p.relative_to(R).as_posix() == 'docs/art/inside-kevins-mind.png',p
 if p.suffix in ['.md','.html','.json','.css','.js','.svg']:
  text=p.read_text()
  assert not re.search(r'/Users/|drive\.google\.com/(?:file|drive)|AIza[\w-]{25}|gh[pousr]_[A-Za-z0-9]{20}|sediment://',text),p
  if p.suffix=='.md' and 'docs' not in p.parts:
   for dest in re.findall(r'\]\(([^)]+)\)',text):
    if '://' in dest or dest.startswith('#'):continue
    assert (p.parent/dest.split('#')[0]).exists(),(p,dest)
# Site: canonical filename, hashed assets, static content and the 404 under the repository prefix.
digest=lambda p:hashlib.sha256((R/'docs'/p).read_bytes()).hexdigest()[:10]
for asset in ['style.css','app.js','favicon.svg','art/currents.svg','art/inside-kevins-mind.png']:
 assert f'{asset}?v={digest(asset)}' in index,asset
lost=(R/'docs/404.html').read_text()
assert f'/tame-impala-agentic-training/style.css?v={digest("style.css")}' in lost
assert 'href="TAME_IMPALA_AGENTS.md" download' in index and 'href="reference.json" download' in index
assert 'id="agent-prompt"' in index and 'id="search"' in index and 'id="empty"' in index and 'id="count"' in index
for word in ['BIBLE','Bible','bible','TAME_IMPALA.md']:
 for p in ['README.md','TAME_IMPALA_AGENTS.md','docs/index.html','docs/404.html','docs/TAME_IMPALA_AGENTS.md','ART_DIRECTION.md','CONTRIBUTING.md']:
  assert word not in (R/p).read_text(),(p,word)
css=(R/'docs/style.css').read_text()
assert 'prefers-reduced-motion' in css and ':focus-visible' in css
assert (R/'docs/fonts/Archivo-Variable.ttf').exists() and (R/'docs/fonts/OFL-Archivo.txt').exists()
assert (R/'docs/fonts/Michroma-Regular.ttf').exists() and (R/'docs/fonts/OFL-Michroma.txt').exists() and 'fonts/Michroma-Regular.ttf' in css
# SVG files served on their own (favicon, <img> art) must be well-formed XML or browsers will show nothing.
import xml.dom.minidom
for p in list((R/'docs/art').glob('*.svg'))+[R/'docs/favicon.svg']:
 xml.dom.minidom.parseString(p.read_bytes())
assert 'whether' not in (R/'site/index.html').read_text().lower()
expected=re.sub(r'\]\((?!https?://|#)([^)]+)\)',lambda m:'](https://github.com/EthanSK/tame-impala-agentic-training/blob/main/'+m[1]+')',(R/'TAME_IMPALA_AGENTS.md').read_text())
assert (R/'docs/TAME_IMPALA_AGENTS.md').read_text()==expected
print(f'PASS: {len(a["claims"])} claims, {len(a["sources"])} linked source files, generated parity, hashed assets, local Markdown destinations and public-content scan')
