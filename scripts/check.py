#!/usr/bin/env python3
"""Check public provenance, generated parity and local Markdown destinations."""
import json,re
from pathlib import Path
R=Path(__file__).resolve().parents[1]
a=json.loads((R/'data/reference.json').read_text())
assert len({c['id'] for c in a['claims']})==len(a['claims'])
ss={s['id']:s for s in a['sources']}
for c in a['claims']:
 assert c['source_id'] in ss and c['location'] and c['era']
 assert c['evidence'] in ('first-hand','qualified-recollection','publisher-report')
 assert f'id="{c["id"]}"' in (R/'docs/index.html').read_text()
for s in a['sources']:
 assert (R/s['file']).exists()
 assert (R/s['file']).read_text().startswith('Source: '+s['url'])
for name,src in [('reference.json','data/reference.json')]:
 assert (R/'docs'/name).read_bytes()==(R/src).read_bytes()
for p in R.rglob('*'):
 if not p.is_file() or '.git' in p.parts or '__pycache__' in p.parts:continue
 assert p.suffix.lower() not in ['.mp3','.mp4','.wav','.vtt','.srt'],p
 if p.suffix in ['.md','.html','.json','.css','.js']:
  text=p.read_text()
  assert not re.search(r'/Users/|drive\.google\.com/(?:file|drive)|AIza[\w-]{25}|gh[pousr]_[A-Za-z0-9]{20}|sediment://',text),p
  if p.suffix=='.md' and 'docs' not in p.parts:
   for dest in re.findall(r'\]\(([^)]+)\)',text):
    if '://' in dest or dest.startswith('#'):continue
    assert (p.parent/dest.split('#')[0]).exists(),(p,dest)
print(f'PASS: {len(a["claims"])} claims, {len(a["sources"])} linked source files, generated parity, local Markdown destinations and public-content scan')

expected=re.sub(r'\]\((?!https?://|#)([^)]+)\)',lambda m:'](https://github.com/EthanSK/tame-impala-production/blob/main/'+m[1]+')',(R/'BIBLE.md').read_text())
assert (R/'docs/BIBLE.md').read_text()==expected
