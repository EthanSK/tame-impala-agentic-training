#!/usr/bin/env python3
"""Generate the reference and static site from public source records. Python 3.9+."""
import json, html, re, shutil
from pathlib import Path
R=Path(__file__).resolve().parents[1]
D=R/'docs'; D.mkdir(exist_ok=True)
repo='https://github.com/EthanSK/tame-impala-production'
site='https://ethansk.github.io/tame-impala-production/'
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
 allnotes+=['## Transcript status','','Public source notes are original paraphrases. Full third-party transcripts and media are not redistributed. Supplied course captions are retained separately in the private source archive.','', '[Master document](../../BIBLE.md) · [Coverage](../../COVERAGE.md)']
 (R/path).parent.mkdir(parents=True,exist_ok=True);(R/path).write_text('\n'.join(allnotes)+'\n')
# Remove stale external presentation copies only if not referenced, all were generated in this task.
for p in (R/'sources/external').glob('*.md'):
 if str(p.relative_to(R)) not in paths.values(): p.unlink()
model=dict(schema_version=1,updated='2026-09-08',sources=sources,claims=claims)
(R/'data/reference.json').write_text(json.dumps(model,ensure_ascii=False,indent=2)+'\n')
topics=['Writing','Drums','Bass','Guitar','Synths','Vocals','Mixing','Workflow']
intro=['# Tame Impala Production Bible','',f'{len(claims)} source-linked production notes · {len(sources)} source records · Updated 8 September 2026','',
'An unofficial, growing reference to Kevin Parker’s production choices. Start with a musical problem, follow the source, then test an idea in your own session. A gear mention is not a universal recipe.','',
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
(R/'BIBLE.md').write_text('\n'.join(intro)+'\n')
(R/'LEARNINGS.md').write_text('# Master learnings\n\nThe canonical master is [BIBLE.md](BIBLE.md). All structured production claims live in [data/reference.json](data/reference.json); edit the input records described in [CONTRIBUTING.md](CONTRIBUTING.md) and regenerate.\n')
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
# Every note is server-rendered into static HTML; JS adds filters only.
articles=[]
for c in claims:
 s=lookup[c['source_id']]
 articles.append(f'''<article class="note" id="{e(c['id'])}" data-topic="{e(c['topic'])}" data-source="{e(s['id'])}" data-evidence="{e(c['evidence'])}"><div class="note-code"><a href="#{e(c['id'])}">{e(c['id'])}</a><span>{e(c['topic'])}</span></div><div><div class="note-meta">{e(c['era'])}</div><h3>{e(c['title'])}</h3><p>{e(c['claim'])}</p><div class="gear">{e(' / '.join(c['gear']))}</div><footer><span class="evidence">{e(c['evidence'].replace('-',' '))}</span><a href="{e(s['url'])}">{e(s['title'])} ↗</a><span class="timestamp">{location_html(c['location'])}</span></footer></div></article>''')
sourcehtml=''.join(f'<details id="source-{e(s["id"])}"><summary><span>{e(s["id"])}</span> {e(s["title"])}</summary><p>{e(s["coverage"])}</p><p>{e(s["notes"])}</p><a href="{e(s["url"])}">Open source ↗</a> · <a href="{repo}/blob/main/{paths[s["id"]]}">Source notes</a></details>' for s in sources)
page=f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Tame Impala Production — The Production Bible</title><meta name="description" content="{len(claims)} source-linked notes on Kevin Parker's production, gear, plugins and songwriting. Search by topic and follow the original evidence."><meta name="theme-color" content="#281c3d"><meta property="og:title" content="Tame Impala Production"><meta property="og:description" content="The production bible: source-linked notes, gear and songwriting, with the uncertainties kept in."><meta property="og:type" content="website"><meta property="og:url" content="{site}"><link rel="canonical" href="{site}"><link rel="icon" href="favicon.svg" type="image/svg+xml"><link rel="stylesheet" href="style.css"><script src="app.js" defer></script></head>
<body><a class="skip" href="#reference">Skip to production notes</a><header class="masthead"><a class="wordmark" href="./">TP <span>THE PRODUCTION NOTEBOOK</span></a><nav aria-label="Main navigation"><a href="#reference">Notes</a><a href="#sources">Sources</a><a href="{repo}">GitHub ↗</a></nav></header>
<main><section class="hero"><div class="hero-copy"><div class="eyebrow">KEVIN PARKER / RECORDING & WRITING</div><h1>TAME IMPALA<br><em>Production.</em></h1><p class="intro">Original production notes on how Tame Impala records are made, gathered from interviews and public sources.</p><div class="hero-actions"><a class="primary" href="BIBLE.md" download>BIBLE.md <span>↓</span></a><a href="#reference">Find a technique <span>↘</span></a></div><p class="unofficial">Unofficial fan project, not affiliated with Tame Impala.</p></div><div class="tape" aria-hidden="true"><div class="tape-label">VOL. 01<br><strong>KEEP<br>THE IDEA.</strong></div><div class="reel r1"></div><div class="reel r2"></div><div class="tape-bottom">WRITING · RECORDING · MIXING</div></div></section>
<div class="signal"><span>01 / SOURCE</span><b>→</b><span>02 / IDEA</span><b>→</b><span>03 / TECHNIQUE</span><b>→</b><span>04 / YOUR SESSION</span></div>
<section class="library" id="reference"><div class="section-heading"><div><div class="eyebrow">THE MASTER DOCUMENT</div><h2>Follow the idea.</h2></div><p>{len(claims)} notes<br>{len(sources)} source records</p></div><p class="library-intro">Find the drums, doubles, synths and decisions behind the records. Every note keeps its source, context and uncertainty.</p>
<div class="controls"><div class="search-row"><label class="search-label" for="search">Search<input id="search" type="search" placeholder="Search notes, gear, techniques" autocomplete="off"></label><label for="source-filter">Source<select id="source-filter"><option value="">All sources</option>{''.join(f'<option value="{s["id"]}">{e(s["id"]+" · "+s["title"])}</option>' for s in sources)}</select></label><label for="evidence-filter">Evidence<select id="evidence-filter"><option value="">All evidence</option><option value="first-hand">First-hand</option><option value="qualified-recollection">Recollection</option><option value="publisher-report">Publisher report</option></select></label></div><div class="topics" role="group" aria-label="Production topic"><button type="button" data-topic="" aria-pressed="true">All topics</button>{''.join(f'<button type="button" data-topic="{t}" aria-pressed="false">{t}</button>' for t in topics)}</div><div class="results-bar"><span id="count" role="status" aria-live="polite">{len(claims)} notes</span><button id="clear" type="button">Clear filters</button></div></div>
<details class="evidence-guide"><summary>How strong is the evidence?</summary><p><strong>First-hand</strong> means Parker said it in an interview, including automatic-caption and speech-recognition accounts. <strong>Recollection</strong> preserves uncertainty. <strong>Publisher report</strong> identifies information supplied by the publication. These are not certified transcripts or independently reproduced settings.</p><p>Course timestamps restart in each part. Podcast times follow an ad-supported 81:23 copy and can shift with inserted ads. Three member clips lack extracted content; one playlist entry is private. <a href="{repo}/blob/main/COVERAGE.md">Read the coverage record ↗</a></p></details>
<div id="notes">{''.join(articles)}</div><p id="empty" hidden>No notes found matching your search</p><noscript><p>All notes are available below. Use your browser’s Find command to search without JavaScript.</p></noscript></section>
<section class="agent-section" id="agents"><div><div class="eyebrow">FOR YOUR NEXT SESSION</div><h2>Ask an agent.<br><em>Keep the source.</em></h2><p>Give your agent the master document or JSON, then ask about a sound, song or piece of gear.</p><a href="BIBLE.md" download>Download BIBLE.md ↓</a> · <a href="reference.json" download>Download JSON ↓</a></div><div><label for="agent-prompt">Agent prompt</label><textarea id="agent-prompt" readonly rows="6">Use this repository as a source reference. Read BIBLE.md, data/reference.json and COVERAGE.md. For every factual production claim, cite the claim ID, original source and timestamp or section. Preserve era, uncertain recollections and publisher attribution. Clearly label your own suggested experiments. Never invent settings or claim unread videos were reviewed.</textarea><button class="primary" id="copy" type="button">Copy agent prompt</button><span id="copy-status" role="status"></span></div></section>
<section class="sources" id="sources"><div class="eyebrow">THE SOURCE SHELF</div><h2>Go back to the recording.</h2><p>Follow the original interview, browse its notes, or check what still needs reviewing.</p>{sourcehtml}</section>
<section class="contribute"><h2>The notebook stays open.</h2><p>Pull requests are accepted, especially ones that add a source link or timestamp.</p><a class="primary" href="{repo}/blob/main/CONTRIBUTING.md">Contribute on GitHub ↗</a></section></main><footer class="site-footer"><span>TAME IMPALA PRODUCTION / 2026</span><span>Original notes. Original sources. Uncertainty included.</span><a href="{repo}/blob/main/LICENSE">License</a></footer></body></html>'''
(D/'index.html').write_text(page)
for md in R.rglob('*.md'):
 md.write_text('\n'.join(line.rstrip() for line in md.read_text().splitlines()).rstrip()+'\n')
bible=(R/'BIBLE.md').read_text()
(D/'BIBLE.md').write_text(re.sub(r'\]\((?!https?://|#)([^)]+)\)',lambda m:']('+repo+'/blob/main/'+m[1]+')',bible))
shutil.copy2(R/'data/reference.json',D/'reference.json')
print(f'Built {len(claims)} claims, {len(sources)} sources, {len(gear)} exact gear labels')
