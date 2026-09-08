#!/usr/bin/env python3
"""Generate the reference and static site from public source records. Python 3.9+."""
import json, html, re, shutil, hashlib, sys
from string import Template
from pathlib import Path
R=Path(__file__).resolve().parents[1]
D=R/'docs'; D.mkdir(exist_ok=True)
sys.path.insert(0,str(R/'scripts'))
import art
repo='https://github.com/EthanSK/tame-impala-agentic-training'
site='https://ethansk.github.io/tame-impala-agentic-training/'
prefix='/tame-impala-agentic-training/'
updated='8 September 2026'
e=lambda v:html.escape(str(v),quote=True)
def location_html(value):
 return f'<a href="{e(value)}">Artist reply ↗</a>' if value.startswith('https://') else e(value)
a=json.loads((R/'data/external.json').read_text());b=json.loads((R/'data/session-sources.json').read_text())
sources=a['sources']+b['sources']; claims=a['claims']+b['claims']
clips=[('YT1','r8lKPPm1sYo','Top 10 Production & Writing Insights (public edit)','Complete available automatic captions reviewed; no video-frame or human audio audit.','Cross-checks TN188: full drum takes 00:25; 808/DRM1 02:45; capture ideas 05:23; effects 09:28; producer judgment 11:14; vocal width 12:41. These repeat the interview, not six independent sources.'),('YT2','1WMxwm3Tu70','Vocal Chain, Layering & Vocal Production Techniques','Metadata only; research extraction session encountered membership gate.','Authorized browser playback access was observed, but no caption export was available through that controller. Content is not claimed reviewed.'),('YT3','nwqOT7jwt4A','Drum Production on Deadbeat','Metadata only; research extraction session encountered membership gate.','Caption availability in an authorized session remains unverified. Do not infer details from the title.'),('YT4','o02n6ogEvcY','Top 10 Production & Writing Insights (member edit)','Metadata only; research extraction session encountered membership gate.','13:00 playlist duration differs from the public edit. Their equivalence is unverified.'),('YT5','e65xhY6Qvqg','Tame Impala Breaks Down Deadbeat (teaser)','Complete available automatic captions reviewed; no video-frame or human audio audit.','Repeats drum palette at 00:14 and stereo whispers at 00:43. No distinct tip counted; isolated compression/EQ excerpt does not establish a chain.'),('YT6','Pld6EOIF7xg','Unavailable playlist entry (title unknown)','Video ID identified; ordinary extraction returned Private video.','Content, duration and relation to the interview unknown.')]
for id,vid,title,coverage,notes in clips:
 sources.append(dict(id=id,title=title,url='https://www.youtube.com/watch?v='+vid,date='2026-09-03' if id in ['YT1','YT5'] else None,kind='video',coverage=coverage,notes=notes))
assert len({s['id'] for s in sources})==len(sources)
assert len({c['id'] for c in claims})==len(claims)
lookup={s['id']:s for s in sources}
for c in claims:
 assert c['source_id'] in lookup
 assert c['evidence'] in ['first-hand','qualified-recollection','publisher-report']
 assert c['topic'] in ['Writing','Drums','Bass','Guitar','Synths','Vocals','Mixing','Workflow']
paths={}
for s in sources:
 if s['id'].startswith('MW'):path=f'sources/mix-with-the-masters/{s["id"].lower()}.md'
 elif s['id']=='TN188' or s['id'].startswith('YT'):path=f'sources/tape-notes/{s["id"].lower()}.md'
 else:
  # Replace external source presentation deterministically, preserving all source data.
  matches=list((R/'sources/external').glob(s['id'].lower()+'*'))
  path=str(matches[0].relative_to(R)) if matches else f'sources/external/{s["id"].lower()}.md'
 paths[s['id']]=path;s['file']=path
 allnotes=[f'Source: {s["url"]}','',f'# {s["title"]}','',f'- Source ID: `{s["id"]}`',f'- Date: {s["date"] or "Unverified"}',f'- Type: {s["kind"]}',f'- Coverage: {s["coverage"]}','',s['notes'],'','## Production notes','']
 cs=[c for c in claims if c['source_id']==s['id']]
 if not cs:allnotes+=['No independent production claims extracted from this record. Coverage and pointers are preserved above.','']
 for c in cs:allnotes += [f'### {c["id"]}: {c["title"]}',f'**{c["topic"]} · {c["era"]} · {c["evidence"]}**',f'Location: {c["location"]}','',c['claim'],'',f'Gear: {", ".join(c["gear"]) or "No specific model established"}','']
 allnotes+=['## Transcript status','','Public source notes are original paraphrases. Full third-party transcripts and media are not redistributed. Supplied course captions are retained separately in the private source archive.','', '[Master document](../../TAME_IMPALA_AGENTS.md) · [Coverage](../../COVERAGE.md)']
 (R/path).parent.mkdir(parents=True,exist_ok=True);(R/path).write_text('\n'.join(allnotes)+'\n')
# Remove stale external presentation copies only if not referenced, all were generated in this task.
for p in (R/'sources/external').glob('*.md'):
 if str(p.relative_to(R)) not in paths.values(): p.unlink()
model=dict(schema_version=1,updated='2026-09-08',sources=sources,claims=claims)
(R/'data/reference.json').write_text(json.dumps(model,ensure_ascii=False,indent=2)+'\n')
topics=['Writing','Drums','Bass','Guitar','Synths','Vocals','Mixing','Workflow']
intro=['# Tame Impala Production — agent reference (TAME_IMPALA_AGENTS.md)','',f'{len(claims)} source-linked production notes · {len(sources)} source records · Updated {updated}','',
'This is the canonical master document of the tame-impala-agentic-training repository: an unofficial, growing reference to Kevin Parker’s documented production choices, written so an AI agent or a musician can answer from the evidence rather than from memory. Every note carries a stable claim ID, its original source, a timestamp or section, the song or era it describes and an evidence label. Start with a musical problem, follow the source, then test an idea in your own session. A gear mention is not a universal recipe. Answering rules live in [AGENTS.md](AGENTS.md); read/unread boundaries live in [COVERAGE.md](COVERAGE.md).','',
'## Read the evidence correctly','',
'- **First-hand:** Parker’s statement in an interview, including caption/ASR-derived accounts. This label describes who spoke, not a certified transcript or independent replication.',
'- **Qualified recollection:** Parker is uncertain, corrects himself, or reconstructs an old setup. Preserve the qualification.',
'- **Publisher report:** identification or narration supplied by the publisher, rather than a securely attributed artist statement.',
'- Timestamps are local to the stated video part. TN188 times follow an ad-supported 81:23 copy; inserted advertisements can move player offsets.',
'- Supplied course captions and public automatic transcripts were text-reviewed; complete video-frame and human audio audits were not performed.',
'- Three member clips lack extracted content; one playlist video is private. Read [COVERAGE.md](COVERAGE.md) before claiming complete video coverage.','',
'## Find your way','',
'[Gear and plugins](GEAR.md) · [All sources](SOURCES.md) · [Playlists](playlists/README.md) · [Machine-readable JSON](data/reference.json) · [Agent instructions](AGENTS.md)','',
'## Working principles — editorial synthesis','',
'These prompts are our interpretation of the cited accounts, not additional Kevin Parker quotations.','',
'1. Capture an idea before polishing your ability to perform it (TN188-01; MW1-01).',
'2. Work on the groove and interacting envelopes before chasing a more expensive signal chain (MW2-01; MW2-11).',
'3. Let an unfamiliar instrument interrupt familiar playing habits (GW05; check the source record for context).',
'4. Treat sonic character as an arrangement decision: a dry hook, whisper sides or a small drum palette changes the identity (TN188-04, TN188-12, TN188-13).',
'5. Compare methods and keep what earns its place; the abandoned summing experiment is as instructive as the retained hardware (MW5-01).',
'6. Keep alternate takes, source links and uncertainty so later decisions remain reversible.','',
'## Important corrections and unresolved details','',
'- The Less I Know the Better’s opening bass riff is a guitar-synth sound; a later bass part is corrected to Greco in MW1. General Hofner use elsewhere does not override that correction.',
'- Ableton delay names in an old Currents recollection do not prove that the modern Echo device was used on that recording.',
'- MW5 tentatively mentions an SSL bus compressor; Sound On Sound publisher narration mentions Manley. The accounts do not establish one combined chain.',
'- Deadbeat’s microphone discussion corrects SM57 to SM7; a U47-style clone has no securely established manufacturer here.',
'- Tape Notes sponsors are not evidence of Kevin’s equipment. Exact plugin settings, amp models and several old patch names remain unknown.','']
for topic in topics:
 intro += [f'## {topic}','']
 for c in [c for c in claims if c['topic']==topic]:
  s=lookup[c['source_id']]
  intro += [f'### {c["id"]} · {c["title"]}',c['claim'],'',f'- **Context:** {c["era"]}',f'- **Evidence:** {c["evidence"]} · [{s["title"]}]({s["url"]}) · {c["location"]}',f'- **Gear:** {", ".join(c["gear"]) or "No specific model established"}',f'[Source record]({paths[s["id"]]})','']
(R/'TAME_IMPALA_AGENTS.md').write_text('\n'.join(intro)+'\n')
(R/'LEARNINGS.md').write_text('# Master learnings\n\nThe canonical master is [TAME_IMPALA_AGENTS.md](TAME_IMPALA_AGENTS.md). All structured production claims live in [data/reference.json](data/reference.json); edit the input records described in [CONTRIBUTING.md](CONTRIBUTING.md) and regenerate.\n')
gear={}
for c in claims:
 for g in c['gear']:gear.setdefault(g,[]).append(c)
geartext=['# Gear and plugins','', 'Every item below has a cited context. Similar names and uncertain identifications stay separate intentionally; this is not a shopping list, current rig inventory or proof of universal use.','']
for g,cs in sorted(gear.items(),key=lambda x:x[0].lower()):
 geartext += [f'## {g}','']
 for c in cs:geartext += [f'- **{c["id"]} / {c["era"]}:** {c["title"]}. [{c["source_id"]}]({paths[c["source_id"]]}) · {c["location"]} · {c["evidence"]}']
 geartext+=['']
(R/'GEAR.md').write_text('\n'.join(geartext)+'\n')
(R/'SOURCES.md').write_text('# Sources\n\n'+ '\n'.join(f'- [{s["id"]}: {s["title"]}]({paths[s["id"]]}) — {s["coverage"]}' for s in sources)+'\n')
(R/'playlists/README.md').write_text('# Playlists and source groups\n\n- [Tape Notes Tame Impala playlist](tape-notes.md) — all six entries, including coverage gaps.\n- [Mix With The Masters](mix-with-the-masters.md) — trailer and five course parts.\n- [Primary interviews](primary-interviews.md) — interviews, AMA and official transcript.\n\nSource membership does not prove duplicate or independent content. Public edits often overlap the full podcast.\n')
(R/'playlists/tape-notes.md').write_text('Source: https://www.youtube.com/playlist?list=PLCy7kFImYx34\n\n# Tape Notes — Tame Impala\n\nAll six playlist entries inventoried on 8 September 2026.\n\n'+'\n'.join(f'{i+1}. [{t[2]}](../{paths[t[0]]}) — {t[3]}' for i,t in enumerate(clips))+'\n\n[Full public TN188 episode notes](../sources/tape-notes/tn188.md) supply the detailed interview context; they do not establish that unreviewed member edits contain nothing additional.\n')
(R/'playlists/mix-with-the-masters.md').write_text('Source: '+lookup['MW0']['url']+'\n\n# Mix With The Masters — The Less I Know the Better\n\nInside the Track #159. Trailer plus five parts; timestamps restart in each file.\n\n'+'\n'.join(f'- [{lookup[f"MW{i}"]["title"]}](../{paths[f"MW{i}"]})' for i in range(6))+'\n\nAll six supplied caption files are preserved in a separate private archive. Public records contain original notes and do not distribute the course or its transcripts.\n')

# ---- Website. Every note is server-rendered into static HTML; JS adds filters only. ----
# Album colour for small note chips, derived from the cited era text.
ALBUMS=[('innerspeaker','Innerspeaker','2010'),('lonerism','Lonerism','2012'),('currents','Currents','2015'),('slow-rush','The Slow Rush','2020'),('deadbeat','Deadbeat','2025')]
def album_of(era):
 low=era.lower()
 hits=[(low.find(name.lower()),key) for key,name,_ in ALBUMS if name.lower() in low]
 return min(hits)[1] if hits else 'other'
articles=[]
for c in claims:
 s=lookup[c['source_id']];album=album_of(c['era'])
 articles.append(f'<article class="note" id="{e(c["id"])}" data-topic="{e(c["topic"])}" data-source="{e(s["id"])}" data-evidence="{e(c["evidence"])}" data-album="{album}"><div class="note-code"><a href="#{e(c["id"])}">{e(c["id"])}</a><span class="note-topic">{e(c["topic"])}</span></div><div class="note-body"><p class="note-era"><span class="era-chip album album-{album}" aria-hidden="true"></span>{e(c["era"])}</p><h3>{e(c["title"])}</h3><p class="claim">{e(c["claim"])}</p><p class="gear">{e(" / ".join(c["gear"]))}</p><footer><span class="evidence" data-evidence="{e(c["evidence"])}">{e(c["evidence"].replace("-"," "))}</span><a href="{e(s["url"])}">{e(s["title"])} ↗</a><span class="timestamp">{location_html(c["location"])}</span></footer></div></article>')
sourcehtml=''.join(f'<details id="source-{e(s["id"])}"><summary><span class="sid">{e(s["id"])}</span><span>{e(s["title"])}</span></summary><p>{e(s["coverage"])}</p><p>{e(s["notes"])}</p><p class="source-links"><a href="{e(s["url"])}">Open source ↗</a> · <a href="{repo}/blob/main/{paths[s["id"]]}">Source notes</a></p></details>' for s in sources)
# Generated illustration. Hashes in asset links make browsers fetch new styles after a deploy.
(D/'art').mkdir(exist_ok=True)
(D/'art/currents.svg').write_text(art.currents()+'\n')
digest=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()[:10]
assets=dict(css_hash=digest(D/'style.css'),js_hash=digest(D/'app.js'),icon_hash=digest(D/'favicon.svg'),currents_src='art/currents.svg?v='+digest(D/'art/currents.svg'))
common=dict(portrait_src='art/inside-kevins-mind.png?v='+digest(D/'art/inside-kevins-mind.png'),site=site,repo=repo,prefix=prefix,updated=updated,count=len(claims),nsources=len(sources),arch_svg=art.ARCH,**assets)
page=Template((R/'site/index.html').read_text()).substitute(common,cover_svg=art.innerspeaker(),dune_svg=art.DUNE,notes=''.join(articles),sources=sourcehtml,
 source_options=''.join(f'<option value="{s["id"]}">{e(s["id"]+" · "+s["title"])}</option>' for s in sources),
 topic_buttons=''.join(f'<button type="button" data-topic="{t}" aria-pressed="false">{t}</button>' for t in topics))
(D/'index.html').write_text(page)
(D/'404.html').write_text(Template((R/'site/404.html').read_text()).substitute(common))
for md in R.rglob('*.md'):
 md.write_text('\n'.join(line.rstrip() for line in md.read_text().splitlines()).rstrip()+'\n')
master=(R/'TAME_IMPALA_AGENTS.md').read_text()
(D/'TAME_IMPALA_AGENTS.md').write_text(re.sub(r'\]\((?!https?://|#)([^)]+)\)',lambda m:']('+repo+'/blob/main/'+m[1]+')',master))
shutil.copy2(R/'data/reference.json',D/'reference.json')
print(f'Built {len(claims)} claims, {len(sources)} sources, {len(gear)} exact gear labels')
