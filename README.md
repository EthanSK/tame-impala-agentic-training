# Tame Impala Production

A production bible for musicians and agents: **114 source-linked notes** on Kevin Parker’s writing, drums, bass, synths, vocals and mixing, collected in one searchable reference.

**[Browse the website](https://ethansk.github.io/tame-impala-production/) · [Read BIBLE.md](BIBLE.md) · [Gear and plugins](GEAR.md)**

Unofficial fan project, not affiliated with Tame Impala, Kevin Parker or the source publishers.

## Start with a sound

Search the website for `EchoBoy`, `drum`, `double`, `Currents` or a musical problem. Each result links to its original source, the relevant timestamp or section, and the era it describes. An uncertain recollection stays uncertain. A publisher’s gear identification stays attributed to the publisher.

For example, the opening bass of *The Less I Know the Better* is a guitar-synth sound; a later bass part is corrected to Greco in Parker’s course discussion. The source record keeps that correction instead of flattening every bass mention into one shopping list.

## Repository map

| Path | Contents |
|---|---|
| [BIBLE.md](BIBLE.md) | Master reference, grouped by production topic |
| [LEARNINGS.md](LEARNINGS.md) | Stable pointer to the master |
| [GEAR.md](GEAR.md) | Every extracted gear label linked to its context and evidence |
| [SOURCES.md](SOURCES.md) | Index of 22 source records |
| [sources/](sources/) | One Markdown record per interview, video or course part; source link at the top |
| [playlists/](playlists/) | Tape Notes playlist, course parts and primary interview groups |
| [data/reference.json](data/reference.json) | Unified machine-readable claims and source metadata |
| [COVERAGE.md](COVERAGE.md) | Read/unread boundaries, missing sources and unresolved details |
| [AGENTS.md](AGENTS.md) | Instructions for answering from the evidence |
| [docs/](docs/) | Dependency-free GitHub Pages site |

## Coverage, honestly

The collection includes the complete supplied caption files for the Mix With The Masters trailer and five *The Less I Know the Better* course parts, a text-reviewed automatic transcript of the full public Tape Notes 188 podcast, two caption-reviewed public clips, and selected primary interviews. The podcast and edited clips overlap; they are not independent corroborating interviews.

Three members-only clips remain unreviewed because the research extraction session could not retrieve their content. This does not establish a lack of access in a reader’s signed-in browser. The sixth playlist entry is private. Full visual inspection of plugin interfaces and a complete human audio audit have not been performed. **[Read the coverage record](COVERAGE.md).**

Full third-party transcripts, videos, audio, lyrics and course files are not redistributed. Public files are original paraphrased notes and official source links. Supplied captions are retained in a separate private archive. No private archive location or credentials are required to use this public repository.

## Use with an agent

Give your agent `BIBLE.md`, `data/reference.json` and `COVERAGE.md`, then ask:

> What approaches to vocal width are documented? Cite the claim IDs, original sources and timestamps. Separate Parker’s statements from your own suggested experiments, and preserve the song and era.

The JSON contains `schema_version`, `updated`, `sources` and `claims`. Each claim has a stable ID, topic, title, paraphrase, source ID, location, evidence type, era and gear list. Null source dates mean unverified dates, not missing content.

## Contribute

**Pull requests are accepted**, especially ones that add a source link or timestamp. Corrections to transcription-derived model names, missing clips and contradictory recollections are particularly useful. Read [CONTRIBUTING.md](CONTRIBUTING.md) before adding material.

## Build and preview

Requires Python 3.9 or newer; no packages, API keys or service accounts.

```sh
python3 scripts/build.py
python3 scripts/check.py
python3 -m http.server 8080 --directory docs
```

Open `http://localhost:8080`. The full note collection is present in the initial HTML; JavaScript adds filtering and copy controls. GitHub Pages serves `docs/` on `main`. Regenerate after changing source data and commit generated files alongside the inputs.

## Rights and attribution

Original project code and original notes are MIT-licensed; see [LICENSE](LICENSE). This license does not grant rights to third-party interviews, course material, music, transcripts, trademarks or linked sites. Each source retains its attribution and link. Research and editorial drafting were assisted by AI; corrections and direct verification are welcome.
