"""Render the separate compilation guide without mixing artists into Parker's claims."""
import json
from collections import Counter


def seconds(value):
    return sum(int(part) * 60 ** i for i, part in enumerate(reversed(value.split(':'))))


def build(root, families):
    data = json.loads((root / 'data/best-production-2025.json').read_text())
    source, notes = data['source'], data['notes']
    counts = Counter(note['attribution'] for note in notes)
    labels = {'matched-episode-transcript': 'Episode-transcript match',
              'context-inference': 'Contextual attribution; not confirmed',
              'unassigned': 'Speaker not verified'}
    url = source['url']
    guide = [f'Source: {url}', '', '# Best Production 2025 — agent reference', '',
             f'{len(notes)} technique notes from Tape Notes’ *{source["title"]}*.', '',
             'A separate companion to [TAME_IMPALA_AGENTS.md](TAME_IMPALA_AGENTS.md). Start with a production problem, find a method, and adapt it to the tools in the session. These are accounts from multiple producers; they are not Kevin Parker advice and are not a ranked survey of all production in 2025.', '',
             '## Use this with your agent', '',
             'Attach this file to your agent and name the production problem, your DAW and the tools you have. For a repository-aware agent, also provide [data/best-production-2025.json](data/best-production-2025.json) and [AGENTS.md](AGENTS.md).', '',
             '> Use BEST_PRODUCTION_2025_AGENTS.md as a production-technique reference. Ask about my target result and available tools. Suggest a small experiment using a relevant method, and cite its BP25 note ID, speaker qualification and compilation timestamp. Separate the source account from your suggested settings and substitutions. Preserve uncertainty, corrections and approximate reconstructions. Do not attribute other producers’ methods to Kevin Parker. Keep my existing project instructions.', '',
             '## Evidence and coverage', '',
             f'- Source video: [{source["title"]}]({url}), published {source["published_at"][:10]}; the publisher calls the collection “2025”.',
             f'- {source["coverage"]}',
             f'- {counts["matched-episode-transcript"]} notes have matching passages in named episode transcripts; {counts["context-inference"]} have contextual attribution; {counts["unassigned"]} retain an unverified speaker.',
             '- A transcript match identifies the episode, not a certified transcription, a full listening audit or independently reproduced settings. Contextual attributions must remain qualified in an agent’s answer.',
             '- Every timestamp below belongs to the compilation, not the full episode. Supporting episode pages were checked for relevant passages or metadata only.',
             '- Names distorted by automatic captions remain qualified. Gear lists describe what was mentioned, including things not used, tentative identifications and hypothetical alternatives; read the associated note.',
             '- Full third-party transcripts and media are not redistributed. All production notes are original paraphrases.', '',
             '[Chronological source index](sources/best-production-2025/bp25.md) · [Source group](playlists/best-production-2025.md) · [Structured JSON](data/best-production-2025.json)', '',
             '## Choose a production technique', '',
             'The grouping and the following session prompts are editorial guidance, not additional artist statements.', '']
    prompts = {
        'capture': 'Decide what the performer needs to hear, what to record and what to commit while the idea is working.',
        'groove': 'Establish the pulse and interaction first, then add or remove rhythmic detail against that foundation.',
        'sound': 'Name the change you want in the sound, then test the smallest useful change in synthesis, filtering or processing.',
        'space': 'Choose what should feel close, distant or wide; judge the effect alongside the lead and the rest of the arrangement.',
        'dynamics': 'Identify the moment whose impact is wrong, then compare local automation or envelope changes in context.',
        'decisions': 'Give each part a role and compare alternatives against the song’s intention before adding more material.'}
    for family in families:
        guide += [f'- **[{family["title"]}](#{family["id"]}):** {prompts[family["id"]]}']
    guide += ['']
    for family in families:
        guide += [f'<a id="{family["id"]}"></a>', f'## {family["title"]}', '']
        for note in (n for n in notes if n['technique'] == family['id']):
            location = f'{note["start"]}–{note["end"]}'
            guide += [f'<a id="{note["id"].lower()}"></a>',
                      f'### {note["id"]} · {note["title"]}', '',
                      f'**{note["artist"]}** · {labels[note["attribution"]]} · [{location}]({url}&t={seconds(note["start"])}s)', '']
            guide += [f'- {point}' for point in note['points']]
            guide += ['', f'**Keep in mind:** {note["qualification"]}', '',
                      f'**Tools mentioned:** {"; ".join(note["gear"]) or "No specific tool established."}', '']
            if note.get('episode_url'):
                guide += [f'[Supporting episode context]({note["episode_url"]})', '']
    guide += ['## Gear and plugins — find the technique first', '',
              'This index is for retrieval. It does not establish use, a complete chain or a shopping recommendation.', '']
    gear = {}
    for note in notes:
        for name in note['gear']:
            gear.setdefault(name, []).append(note)
    for name, entries in sorted(gear.items(), key=lambda pair: pair[0].lower()):
        guide += [f'- **{name}:** ' + ', '.join(f'[{n["id"]}](#{n["id"].lower()})' for n in entries)]
    guide += ['', '## Publisher metadata used for context', '']
    for item in source['supporting_metadata']:
        guide += [f'- [{item["title"]}]({item["url"]}) — {item["scope"]}']
    (root / 'BEST_PRODUCTION_2025_AGENTS.md').write_text('\n'.join(guide) + '\n')
    record = [f'Source: {url}', '', f'# BP25 · {source["title"]}', '',
              f'- Publisher: {source["publisher"]}',
              f'- Published: {source["published_at"][:10]}',
              '- Duration: 2:01:47',
              f'- Reviewed: {source["reviewed_on"]}',
              f'- Coverage: {source["coverage"]}', '', source['attribution_policy'], '',
              '[Full technique guide](../../BEST_PRODUCTION_2025_AGENTS.md) · [JSON](../../data/best-production-2025.json)', '',
              '## Chronological index', '',
              'The opening 00:00–00:21 montage previews later material. The final available caption starts at 2:01:34; the remaining 13 seconds have not been separately audited.', '']
    for note in notes:
        record += [f'- **{note["start"]}–{note["end"]}** · [{note["id"]}: {note["title"]}](../../BEST_PRODUCTION_2025_AGENTS.md#{note["id"].lower()}) · {note["artist"]} · {labels[note["attribution"]]}']
    record += ['', '## Transcript status', '', source['transcript']]
    folder = root / 'sources/best-production-2025'
    folder.mkdir(parents=True, exist_ok=True)
    (folder / 'bp25.md').write_text('\n'.join(record) + '\n')
    (root / 'playlists/best-production-2025.md').write_text(
        f'Source: {url}\n\n# Tape Notes — Best Production Advice of 2025\n\n'
        'This source group contains the supplied compilation video. No additional playlist membership is inferred.\n\n'
        '- [BP25: compilation source record](../sources/best-production-2025/bp25.md)\n'
        '- [BEST_PRODUCTION_2025_AGENTS.md](../BEST_PRODUCTION_2025_AGENTS.md) — all extracted technique notes, organized by production method.\n'
        '- [Structured notes](../data/best-production-2025.json)\n')
    return len(notes)
