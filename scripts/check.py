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
# Method priority never alters the original factual records or their evidence.
originals={c['id']:c for name in ['external.json','session-sources.json'] for c in json.loads((R/'data'/name).read_text())['claims']}
assert set(originals)=={c['id'] for c in a['claims']}
families={f['id'] for f in a['techniques']}
assert len(families)==6
assert [c['priority'] for c in a['claims']]==sorted(c['priority'] for c in a['claims'])
for c in a['claims']:
 assert all(c[k]==v for k,v in originals[c['id']].items()),c['id']
 assert c['technique'] in families and c['priority'] in (1,2,3)
 assert f'data-technique="{c["technique"]}"' in index
assert index.index('id="agents"')<index.index('id="reference"')
assert 'id="topic-filter"' in index and 'data-technique=""' in index
assert 'Explore the production techniques' in index and 'Explore the drums' not in index
# The compilation remains a separately attributed, complete chronological extraction.
from companion import seconds
best=json.loads((R/'data/best-production-2025.json').read_text())
assert (R/'docs/best-production-2025.json').read_bytes()==(R/'data/best-production-2025.json').read_bytes()
assert best['source']['url']=='https://www.youtube.com/watch?v=jfJtTBzIt70'
assert len({n['id'] for n in best['notes']})==len(best['notes'])
assert not ({n['id'] for n in best['notes']} & set(originals))
previous=21
guide=(R/'BEST_PRODUCTION_2025_AGENTS.md').read_text()
record=(R/'sources/best-production-2025/bp25.md').read_text()
for n in best['notes']:
 assert seconds(n['start'])==previous,n['id']
 previous=seconds(n['end'])
 assert seconds(n['start'])<previous<=best['source']['duration_seconds']
 assert n['technique'] in families and n['points'] and n['qualification']
 assert n['attribution'] in ['matched-episode-transcript','context-inference','unassigned']
 if n['attribution']=='matched-episode-transcript':assert n.get('episode_url') and n['artist']!='Speaker not yet verified'
 if n['attribution']=='unassigned':assert n['artist']=='Speaker not yet verified'
 assert f'id="{n["id"].lower()}"' in guide and n['id'] in record
assert previous==7294
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
expected_best=re.sub(r'\]\((?!https?://|#)([^)]+)\)',lambda m:'](https://github.com/EthanSK/tame-impala-agentic-training/blob/main/'+m[1]+')',guide)
assert (R/'docs/BEST_PRODUCTION_2025_AGENTS.md').read_text()==expected_best
assert 'href="BEST_PRODUCTION_2025_AGENTS.md" download' in index
print(f'PASS: {len(a["claims"])} unchanged factual claims, six technique groups, {len(best["notes"])} separately attributed compilation notes, generated parity, hashed assets, local links and public-content scan')
