#!/usr/bin/env python3
"""Generate the reference and static site from public source records. Python 3.9+."""
import json, html, re, shutil, hashlib, sys
from string import Template
from pathlib import Path
R=Path(__file__).resolve().parents[1]
D=R/'docs'; D.mkdir(exist_ok=True)
sys.path.insert(0,str(R/'scripts'))
import art
import companion
repo='https://github.com/EthanSK/tame-impala-agentic-training'
site='https://ethansk.github.io/tame-impala-agentic-training/'
prefix='/tame-impala-agentic-training/'
updated='9 September 2026'
e=lambda v:html.escape(str(v),quote=True)
def location_html(value):
 return f'<a href="{e(value)}">Artist reply ↗</a>' if value.startswith('https://') else e(value)
a=json.loads((R/'data/external.json').read_text());b=json.loads((R/'data/session-sources.json').read_text())
sources=a['sources']+b['sources']; claims=a['claims']+b['claims']
techniques=json.loads((R/'data/techniques.json').read_text())
families=techniques['families']; family_lookup={f['id']:f for f in families}
assert set(techniques['mapping'])=={c['id'] for c in claims}
for c in claims:
 c.update(techniques['mapping'][c['id']])
 assert c['technique'] in family_lookup and c['priority'] in (1,2,3)
# Practical methods come first; topic and era remain independent source context.
family_order={f['id']:i for i,f in enumerate(families)}
claims.sort(key=lambda c:(c['priority'],family_order[c['technique']]))
# The website has an explicit editorial reading order across technique families.
# Keep source records and the grouped master guide in their established order.
website_order=techniques['website_usefulness']['order']
assert len(website_order)==len(set(website_order))==len(claims)
assert set(website_order)=={c['id'] for c in claims}
website_rank={id:rank for rank,id in enumerate(website_order)}
companion_count=companion.build(R,families)
clips=json.loads((R/'data/youtube-playlist.json').read_text())['sources']
sources.extend(clips)
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
 allnotes+=['## Transcript status','','Public source notes are original paraphrases. Full third-party transcripts and media are not redistributed. Caption and transcript research copies are retained separately in the private source archive.','', '[Master document](../../TAME_IMPALA_AGENTS.md) · [Coverage](../../COVERAGE.md)']
 (R/path).parent.mkdir(parents=True,exist_ok=True);(R/path).write_text('\n'.join(allnotes)+'\n')
# Remove stale external presentation copies only if not referenced, all were generated in this task.
for p in (R/'sources/external').glob('*.md'):
 if str(p.relative_to(R)) not in paths.values(): p.unlink()
model=dict(schema_version=2,updated='2026-09-09',techniques=families,priority_definitions=techniques['priority_definitions'],sources=sources,claims=claims)
(R/'data/reference.json').write_text(json.dumps(model,ensure_ascii=False,indent=2)+'\n')
topics=['Writing','Drums','Bass','Guitar','Synths','Vocals','Mixing','Workflow']
intro=['# Tame Impala Production — agent reference (TAME_IMPALA_AGENTS.md)','',f'{len(claims)} source-linked production notes · {len(sources)} source records · Updated {updated}','',
'This is the canonical production-technique reference of the tame-impala-agentic-training repository. Use it with an agent to solve a musical problem: choose a documented method, understand the decision behind it, and try an adaptation with the tools you have. Every note keeps its stable claim ID, original source, timestamp or section, song/era and evidence label. Technique groups and practical priority are editorial organization, not confidence ratings. Gear is supporting context, not a requirement to buy the same equipment. Answering rules live in [AGENTS.md](AGENTS.md); read/unread boundaries live in [COVERAGE.md](COVERAGE.md).','',
'## Use this with your agent','',
'Attach this file and describe what you want to change in your production, your DAW and the tools available. Ask the agent to identify a relevant technique, cite the claim and its source, and suggest one small experiment. It should explain what to listen for and keep its proposed settings separate from Parker’s documented actions. Keep your existing project instructions; this is an additional reference, not a replacement for them.','',
'> Help me apply a documented production technique with the tools I have. Cite the claim ID, original source and timestamp or section; preserve the era and every qualification. Explain the method before naming equipment. Clearly label your suggested experiments and substitutions. Never invent settings, presets or unreviewed source content.','',
'## Read the evidence correctly','',
'- **First-hand:** Parker’s statement in an interview, including caption/ASR-derived accounts. This label describes who spoke, not a certified transcript or independent replication.',
'- **Qualified recollection:** Parker is uncertain, corrects himself, or reconstructs an old setup. Preserve the qualification.',
'- **Publisher report:** identification or narration supplied by the publisher, rather than a securely attributed artist statement.',
'- Timestamps are local to the stated video part. TN188 times follow an ad-supported 81:23 copy; inserted advertisements can move player offsets.',
'- Supplied course captions, podcast transcripts and all six playlist caption tracks were text-reviewed; complete video-frame and human audio audits were not performed.',
'- All six playlist clips now have caption-based coverage, including the formerly private drum clip. The wider interview search is bounded, with gated and partially reviewed sources still listed in [COVERAGE.md](COVERAGE.md).','',
'## Find your way','',
'[All sources](SOURCES.md) · [Playlists](playlists/README.md) · [Machine-readable JSON](data/reference.json) · [Agent instructions](AGENTS.md) · [Gear index](GEAR.md) · [Best Production 2025 companion](BEST_PRODUCTION_2025_AGENTS.md)','',
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
'- Let It Happen’s 2015 sampler explanation (EXP05-01) is more explicit than the partial device word in the 2025 automatic caption (ZL25-02); do not identify a vocoder from that fragment.',
'- No Reply’s retained piano memo (EXP04-01) and My Old Ways’ re-recorded opening (TN188-02) concern different songs.',
'- Tape Notes sponsors are not evidence of Kevin’s equipment. Exact plugin settings, amp models and several old patch names remain unknown.','']
intro += ['## Choose a production technique','','Each group puts specific methods before supporting practices and historical or equipment context. Priority describes usefulness for a session; it never removes a source qualification.','']
for family in families:
 intro += [f'- [{family["title"]}](#{family["id"]}) — {family["description"]}']
intro += ['']
for family in families:
 intro += [f'<a id="{family["id"]}"></a>',f'## {family["title"]}','']
 for c in [c for c in claims if c['technique']==family['id']]:
  s=lookup[c['source_id']]
  intro += [f'### {c["id"]} · {c["title"]}',c['claim'],'',f'- **Topic:** {c["topic"]}',f'- **Context:** {c["era"]}',f'- **Evidence:** {c["evidence"]} · [{s["title"]}]({s["url"]}) · {c["location"]}',f'- **Gear context:** {", ".join(c["gear"]) or "No specific model established"}',f'[Source record]({paths[s["id"]]})','']
(R/'TAME_IMPALA_AGENTS.md').write_text('\n'.join(intro)+'\n')
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
(R/'playlists/README.md').write_text('# Playlists and source groups\n\n- [Tape Notes Tame Impala playlist](tape-notes.md) — all six caption-reviewed entries and their overlapping edits.\n- [Mix With The Masters](mix-with-the-masters.md) — trailer and five course parts.\n- [Primary interviews](primary-interviews.md) — interviews, AMA and official transcript.\n\nSource membership does not prove duplicate or independent content. Public edits often overlap the full podcast.\n')
with (R/'SOURCES.md').open('a') as f:f.write('\n## Separate companion\n\n- [BP25: Best Production Advice of 2025](sources/best-production-2025/bp25.md) — compilation technique notes; other producers remain separate from Parker’s claims.\n')
with (R/'playlists/README.md').open('a') as f:f.write('\n- [Best Production Advice of 2025](best-production-2025.md) — the supplied Tape Notes compilation, kept as a separate companion.\n')
(R/'playlists/tape-notes.md').write_text('Source: https://www.youtube.com/playlist?list=PLCy7kFImYx34\n\n# Tape Notes — Tame Impala\n\nAll six original playlist entries caption-reviewed by 9 September 2026.\n\n'+'\n'.join(f'{i+1}. [{t["title"]}](../{paths[t["id"]]}) — {t["coverage"]}' for i,t in enumerate(clips))+'\n\n[Full public TN188 episode notes](../sources/tape-notes/tn188.md) supply the longer interview context. The public/member edits and teaser repeat parts of that interview; they are not independent corroboration. Per-source records preserve different timestamps and additional details.\n')
(R/'playlists/primary-interviews.md').write_text('# Primary interviews\n\nReviewed sources and explicit limits; not an exhaustive career bibliography. Full search decisions and unreviewed candidates are in [coverage](../COVERAGE.md) and [the search audit](../data/research-coverage.json).\n\n| Source | Date | Coverage |\n|---|---|---|\n'+'\n'.join(f'| [{s["title"]}](../{paths[s["id"]]}) | {s["date"] or "Unverified"} | {s["coverage"]} |' for s in sources if not s['id'].startswith(('MW','YT')) and s['id']!='TN188')+'\n')
(R/'playlists/mix-with-the-masters.md').write_text('Source: '+lookup['MW0']['url']+'\n\n# Mix With The Masters — The Less I Know the Better\n\nInside the Track #159. Trailer plus five parts; timestamps restart in each file.\n\n'+'\n'.join(f'- [{lookup[f"MW{i}"]["title"]}](../{paths[f"MW{i}"]})' for i in range(6))+'\n\nAll six supplied caption files are preserved in a separate private archive. Public records contain original notes and do not distribute the course or its transcripts.\n')

# ---- Website. Every note is server-rendered into static HTML; JS adds filters only. ----
# Album colour for small note chips, derived from the cited era text.
ALBUMS=[('innerspeaker','Innerspeaker','2010'),('lonerism','Lonerism','2012'),('currents','Currents','2015'),('slow-rush','The Slow Rush','2020'),('deadbeat','Deadbeat','2025')]
def album_of(era):
 low=era.lower()
 hits=[(low.find(name.lower()),key) for key,name,_ in ALBUMS if name.lower() in low]
 return min(hits)[1] if hits else 'other'
articles=[]
for c in sorted(claims,key=lambda c:website_rank[c['id']]):
 s=lookup[c['source_id']];album=album_of(c['era'])
 articles.append(f'<article class="note" id="{e(c["id"])}" data-technique="{e(c["technique"])}" data-priority="{c["priority"]}" data-topic="{e(c["topic"])}" data-source="{e(s["id"])}" data-evidence="{e(c["evidence"])}" data-album="{album}"><div class="note-code"><a href="#{e(c["id"])}">{e(c["id"])}</a><span class="note-method">{e(family_lookup[c["technique"]]["title"])}</span><span class="note-topic">{e(c["topic"])}</span></div><div class="note-body"><h3>{e(c["title"])}</h3><p class="claim">{e(c["claim"])}</p><p class="note-era"><span class="era-chip album album-{album}" aria-hidden="true"></span>{e(c["era"])}</p><p class="gear">{e(" / ".join(c["gear"]))}</p><footer><span class="evidence" data-evidence="{e(c["evidence"])}">{e(c["evidence"].replace("-"," "))}</span><a href="{e(s["url"])}">{e(s["title"])} ↗</a><span class="timestamp">{location_html(c["location"])}</span></footer></div></article>')
sourcehtml=''.join(f'<details id="source-{e(s["id"])}"><summary><span class="sid">{e(s["id"])}</span><span>{e(s["title"])}</span></summary><p>{e(s["coverage"])}</p><p>{e(s["notes"])}</p><p class="source-links"><a href="{e(s["url"])}">Open source ↗</a> · <a href="{repo}/blob/main/{paths[s["id"]]}">Source notes</a></p></details>' for s in sources)
# Generated illustration. Hashes in asset links make browsers fetch new styles after a deploy.
(D/'art').mkdir(exist_ok=True)
(D/'art/currents.svg').write_text(art.currents()+'\n')
(D/'art/strings.svg').write_text(art.strings()+'\n')
# The hero portrait is one static SVG (clipped raster in the shared scene); the strands are inline vector markup
# in the page so CSS can sway them and honour reduced motion. The former single-file desktop/mobile scenes are stale.
(D/'art/brain-portrait.svg').write_text(art.brain_portrait((D/'art/inside-kevins-mind.png').read_bytes())+'\n')
for stale in ['brain-currents.svg','brain-currents-mobile.svg']:(D/'art'/stale).unlink(missing_ok=True)
digest=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()[:10]
assets=dict(css_hash=digest(D/'style.css'),js_hash=digest(D/'app.js'),icon_hash=digest(D/'favicon.png'),currents_src='art/currents.svg?v='+digest(D/'art/currents.svg'),strings_src='art/strings.svg?v='+digest(D/'art/strings.svg'))
# The wide head collage is both the social preview and, clipped into the scene, the hero portrait.
common=dict(portrait_src='art/inside-kevins-mind.png?v='+digest(D/'art/inside-kevins-mind.png'),figure_src='art/brain-portrait.svg?v='+digest(D/'art/brain-portrait.svg'),site=site,repo=repo,prefix=prefix,updated=updated,count=len(claims),companion_count=companion_count,nsources=len(sources),arch_svg=art.ARCH,**assets)
page=Template((R/'site/index.html').read_text()).substitute(common,cover_svg=art.innerspeaker(),lip_svg=art.lip(),dune_svg=art.DUNE,brain_lines_svg=art.brain_lines(),notes=''.join(articles),sources=sourcehtml,
 source_options=''.join(f'<option value="{s["id"]}">{e(s["id"]+" · "+s["title"])}</option>' for s in sources),
 topic_options=''.join(f'<option value="{t}">{t}</option>' for t in topics),
 technique_buttons=''.join(f'<button type="button" data-technique="{f["id"]}" aria-pressed="false">{e(f["title"])}</button>' for f in families))
(D/'index.html').write_text(page)
(D/'404.html').write_text(Template((R/'site/404.html').read_text()).substitute(common))
for md in R.rglob('*.md'):
 md.write_text('\n'.join(line.rstrip() for line in md.read_text().splitlines()).rstrip()+'\n')
for name in ['TAME_IMPALA_AGENTS.md','BEST_PRODUCTION_2025_AGENTS.md']:
 master=(R/name).read_text()
 (D/name).write_text(re.sub(r'\]\((?!https?://|#)([^)]+)\)',lambda m:']('+repo+'/blob/main/'+m[1]+')',master))
shutil.copy2(R/'data/reference.json',D/'reference.json')
shutil.copy2(R/'data/best-production-2025.json',D/'best-production-2025.json')
print(f'Built {len(claims)} claims, {len(sources)} sources, {len(gear)} exact gear labels')
