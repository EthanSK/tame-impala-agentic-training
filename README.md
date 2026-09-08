# Tame Impala Production — agentic training

Once AI gets good enough, we can have our own personal Tame Impala producer.

For now, this repository gives an agent **114 production notes** on how Kevin Parker writes, records and mixes, each tied to its original source, timestamp or section, era and level of certainty.

**[Browse the website](https://ethansk.github.io/tame-impala-agentic-training/) · [Read TAME_IMPALA_AGENTS.md](TAME_IMPALA_AGENTS.md) · [Gear and plugins](GEAR.md)**

Unofficial fan project, not affiliated with Tame Impala, Kevin Parker or the source publishers.

## Start with a sound

Search the website for `EchoBoy`, `drum`, `double`, `Currents` or a musical problem. Each result links to its original source, the relevant timestamp or section, and the era it describes. An uncertain recollection stays uncertain. A publisher’s gear identification stays attributed to the publisher.

For example, the opening bass of *The Less I Know the Better* is a guitar-synth sound; a later bass part is corrected to Greco in Parker’s course discussion. The source record keeps that correction instead of flattening every bass mention into one shopping list.

## Repository map

| Path | Contents |
|---|---|
| [TAME_IMPALA_AGENTS.md](TAME_IMPALA_AGENTS.md) | Master reference for agents, grouped by production topic |
| [AGENTS.md](AGENTS.md) | Instructions for answering from the evidence |
| [LEARNINGS.md](LEARNINGS.md) | Stable pointer to the master |
| [GEAR.md](GEAR.md) | Every extracted gear label linked to its context and evidence |
| [SOURCES.md](SOURCES.md) | Index of 22 source records |
| [sources/](sources/) | One Markdown record per interview, video or course part; source link at the top |
| [playlists/](playlists/) | Tape Notes playlist, course parts and primary interview groups |
| [data/reference.json](data/reference.json) | Unified machine-readable claims and source metadata |
| [COVERAGE.md](COVERAGE.md) | Read/unread boundaries, missing sources and unresolved details |
| [ART_DIRECTION.md](ART_DIRECTION.md) | How the website borrows from each album cover, with credits |
| [site/](site/) | HTML templates for the website |
| [scripts/](scripts/) | `build.py` generates everything below; `art.py` draws the illustrations; `check.py` verifies |
| [docs/](docs/) | Generated GitHub Pages site plus its authored `style.css`, `app.js` and the vendored Michroma and Archivo fonts (OFL) |

## Coverage, honestly

The notes draw on the complete supplied captions for the Mix With The Masters trailer and five *The Less I Know the Better* course parts, a text-reviewed automatic transcript of the full public Tape Notes 188 podcast, two caption-reviewed public clips, and selected primary interviews. The podcast and edited clips overlap; they are not independent corroborating interviews.

Three members-only clips remain unreviewed because the research extraction session could not retrieve their content. This does not establish a lack of access in a reader’s signed-in browser. The sixth playlist entry is private. Full visual inspection of plugin interfaces and a complete human audio audit have not been performed. **[Read the coverage record](COVERAGE.md).**

Full third-party transcripts, videos, audio, lyrics and course files are not redistributed. Public files are original paraphrased notes and official source links. Supplied captions are retained in a separate private archive. No private archive location or credentials are required to use this public repository.

## Use with an agent

Give your agent `TAME_IMPALA_AGENTS.md`, `data/reference.json` and `COVERAGE.md`, then ask:

> What approaches to vocal width are documented? Cite the claim IDs, original sources and timestamps. Separate Parker’s statements from your own suggested experiments, and preserve the song and era.

The JSON contains `schema_version`, `updated`, `sources` and `claims`. Each claim has a stable ID, topic, title, paraphrase, source ID, location, evidence type, era and gear list. Null source dates mean unverified dates, not missing content.

## The website

The website opens inside Tame Impala’s mind: a playful photo collage of Kevin Parker, based on a 2025 press portrait, with a colourful brain peeking out. Around it, the five albums supply the visual language: an *Innerspeaker* landscape fragment, *Lonerism*’s gate around search, *Deadbeat*’s black-on-white notes, *Currents*’ streamlines behind the agent prompt and *The Slow Rush*’s red room for the sources. Every note is in the static HTML, so agents and readers without JavaScript get the full text. [ART_DIRECTION.md](ART_DIRECTION.md) records the mapping, portrait source, fonts and artwork credits.

## Contribute

**Pull requests are accepted**, especially ones that add a source link or timestamp. Corrections to transcription-derived model names, missing clips and contradictory recollections are particularly useful. Read [CONTRIBUTING.md](CONTRIBUTING.md) before adding material.

## Build and preview

Requires Python 3.9 or newer; no packages, API keys or service accounts.

```sh
python3 scripts/build.py
python3 scripts/check.py
python3 -m http.server 8080 --directory docs
```

Open `http://localhost:8080`. The full note collection is present in the initial HTML; JavaScript adds filtering and copy controls. Both fonts ship with the site under the SIL Open Font License and use system fallbacks while loading. GitHub Pages serves `docs/` on `main`. Regenerate after changing source data, templates, styles or scripts, and commit generated files alongside the inputs; the build stamps content hashes into asset links so readers receive the new files.

## Rights and attribution

Original project code, original notes and generated SVG illustrations are MIT-licensed; see [LICENSE](LICENSE). This license does not grant rights to third-party interviews, course material, music, album artwork, transcripts, trademarks or linked sites. The portrait collage derives from a third-party photograph, whose rights remain with its owner. Vendored fonts retain their SIL Open Font License. Each source retains its attribution and link; artwork credits are in [ART_DIRECTION.md](ART_DIRECTION.md). Research, design and editorial drafting were assisted by AI; corrections and direct verification are welcome.
