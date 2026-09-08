# Tame Impala Production — agentic training

Once AI gets good enough, we can have our own personal Tame Impala producer.

For now, give your agent **114 source-linked notes about Kevin Parker's production techniques** and use them while making music. The reference starts with the production problem and the method, then adapts it to the tools you have. Every note keeps its source, timestamp or section, era and level of certainty.

**[Browse the techniques](https://ethansk.github.io/tame-impala-agentic-training/) · [Read TAME_IMPALA_AGENTS.md](TAME_IMPALA_AGENTS.md) · [Best Production 2025 companion](BEST_PRODUCTION_2025_AGENTS.md)**

Unofficial fan project, not affiliated with Tame Impala, Kevin Parker or the source publishers.

## Use with your agent

1. Download [TAME_IMPALA_AGENTS.md](https://ethansk.github.io/tame-impala-agentic-training/TAME_IMPALA_AGENTS.md) and attach it to your agent.
2. Copy the setup prompt from the [website](https://ethansk.github.io/tame-impala-agentic-training/#agents), or paste this with the file:

> Read the attached TAME_IMPALA_AGENTS.md and help me apply its production techniques. Ask about my target sound, DAW and available tools. Cite the note ID, original source and timestamp or section for every factual production claim. Preserve the era and uncertainty. Label your suggested experiments and substitutions separately, and never invent settings or presets. Keep my existing project instructions.

Then ask a practical question, such as: “My vocal feels narrow. Which documented technique would you try with the plugins I have, and what should I listen for?”

For an agent working in the repository, read `AGENTS.md`, `TAME_IMPALA_AGENTS.md`, `data/reference.json` and `COVERAGE.md`. You can add a pointer to these references in your existing agent instructions; keep the instructions already there.

## Find a production technique

Browse **Capture & commit**, **Build a groove**, **Shape a sound**, **Create space**, **Control dynamics** and **Choose & arrange**. Specific methods appear before supporting practices and historical or equipment context. Topic, source and evidence filters remain available; the gear index is a way to find the relevant method, not a required shopping list.

The grouping is editorial. A useful method can still carry an uncertain recollection, and a publisher's equipment identification stays attributed to the publisher.

## Best Production 2025 — a separate reference

[BEST_PRODUCTION_2025_AGENTS.md](BEST_PRODUCTION_2025_AGENTS.md) contains **68 technique notes** from the supplied two-hour Tape Notes compilation. It follows the same production-method approach, with a [chronological source index](sources/best-production-2025/bp25.md), [source group](playlists/best-production-2025.md), [structured JSON](data/best-production-2025.json) and a gear retrieval index.

All available automatic captions were text-reviewed. Of the 68 notes, 45 have matching passages in named episode transcripts, 16 retain contextual attribution and 7 have unverified speakers. There was no complete human listening or video-frame audit. Timestamps refer to the compilation. These other producers' accounts remain separate from Kevin Parker's claims.

## Repository map

| Path | Contents |
|---|---|
| [TAME_IMPALA_AGENTS.md](TAME_IMPALA_AGENTS.md) | Master reference, grouped by production technique with practical methods first |
| [BEST_PRODUCTION_2025_AGENTS.md](BEST_PRODUCTION_2025_AGENTS.md) | Separate compilation guide with 68 timestamped technique notes |
| [AGENTS.md](AGENTS.md) | Instructions for answering from the evidence |
| [LEARNINGS.md](LEARNINGS.md) | Stable pointer to the master |
| [GEAR.md](GEAR.md) | Every extracted gear label linked to its context and evidence |
| [SOURCES.md](SOURCES.md) | Index of 22 source records |
| [sources/](sources/) | One Markdown record per interview, video or course part; source link at the top |
| [playlists/](playlists/) | Tape Notes playlist, course parts and primary interview groups |
| [data/reference.json](data/reference.json) | Unified machine-readable claims and source metadata |
| [data/techniques.json](data/techniques.json) | Editorial method groups and practical priority for every Parker claim |
| [data/best-production-2025.json](data/best-production-2025.json) | Separate compilation notes with speaker-attribution status |
| [COVERAGE.md](COVERAGE.md) | Read/unread boundaries, missing sources and unresolved details |
| [ART_DIRECTION.md](ART_DIRECTION.md) | How the website borrows from each album cover, with credits |
| [site/](site/) | HTML templates for the website |
| [scripts/](scripts/) | `build.py` generates everything below; `art.py` draws the illustrations; `check.py` verifies |
| [docs/](docs/) | Generated GitHub Pages site plus its authored `style.css`, `app.js` and the two shipped fonts: Michroma (OFL) and Microgramma D Extended Bold (third-party rights) |

## Coverage, honestly

The notes draw on the complete supplied captions for the Mix With The Masters trailer and five *The Less I Know the Better* course parts, a text-reviewed automatic transcript of the full public Tape Notes 188 podcast, two caption-reviewed public clips, and selected primary interviews. The podcast and edited clips overlap; they are not independent corroborating interviews.

Three members-only clips remain unreviewed because the research extraction session could not retrieve their content. This does not establish a lack of access in a reader’s signed-in browser. The sixth playlist entry is private. Full visual inspection of plugin interfaces and a complete human audio audit have not been performed. **[Read the coverage record](COVERAGE.md).**

Full third-party transcripts, videos, audio, lyrics and course files are not redistributed. Public files are original paraphrased notes and official source links. Supplied captions are retained in a separate private archive. No private archive location or credentials are required to use this public repository.

## Structured data

`data/reference.json` uses schema version 2 and contains `updated`, `techniques`, `priority_definitions`, `sources` and `claims`. Each claim has a stable ID, technique, practical priority, topic, title, paraphrase, source ID, location, evidence type, era and gear list. Null source dates mean unverified dates. Priority measures practical usefulness, not factual confidence. The compilation has its own schema and source namespace in `data/best-production-2025.json`.

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

Open `http://localhost:8080`. The full note collection is present in the initial HTML; JavaScript adds filtering and copy controls. The site uses two shipped fonts, Michroma for plain text and Microgramma D Extended Bold for headings, with system fallbacks while they load. The agent setup section starts collapsed; opening it shows the download, prompt and copy button. GitHub Pages serves `docs/` on `main`. Regenerate after changing source data, templates, styles or scripts, and commit generated files alongside the inputs; the build stamps content hashes into asset links so readers receive the new files.

## Rights and attribution

Original project code, original notes and generated SVG illustrations are MIT-licensed; see [LICENSE](LICENSE). This license does not grant rights to third-party interviews, course material, music, album artwork, transcripts, trademarks or linked sites. The portrait collage derives from a third-party photograph, whose rights remain with its owner. Michroma ships under its SIL Open Font License; Microgramma D Extended Bold is a third-party typeface whose rights remain with its owner, and neither font is covered by the MIT license. Each source retains its attribution and link; artwork credits are in [ART_DIRECTION.md](ART_DIRECTION.md). Research, design and editorial drafting were assisted by AI; corrections and direct verification are welcome.
