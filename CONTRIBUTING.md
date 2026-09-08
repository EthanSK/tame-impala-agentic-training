# Contributing

Pull requests are accepted. Add a first-person interview, official transcript, timestamp, missing source or careful correction that helps a musician understand what was actually done.

## A useful contribution

Include the original source link, publication date if known, song/era, exact timestamp or printed section, and a concise original paraphrase. State what you inspected: text, automatic captions, audio, video frames or publisher metadata. Keep uncertainty and corrections; publisher equipment lists do not establish signal order.

Existing primary-source records live in `data/external.json`; the course and full podcast records live in `data/session-sources.json`. `scripts/build.py` currently holds playlist coverage metadata. Update the relevant input, keeping stable claim IDs.

For a new Parker claim, also add its method family and practical priority to `data/techniques.json`. Prefer a title that names the production technique or decision. Keep every factual qualification; priority is editorial usefulness, not confidence. The separate best-of compilation lives in `data/best-production-2025.json` and uses BP25 note IDs. Its speaker attributions and timestamps must not be merged into Parker's claims.

Regenerate and check the outputs:

```sh
python3 scripts/build.py
python3 scripts/check.py
```

Commit the input and generated changes together. The website's markup lives in `site/index.html` and `site/404.html` (Python `string.Template` placeholders), its styles in `docs/style.css`, its behaviour in `docs/app.js` and its illustrations in `scripts/art.py`; `ART_DIRECTION.md` explains which album each component borrows from. Run the build after any site change so the asset hashes update, and preview `docs/` locally. A new source should receive its own linked Markdown record and a playlist/source-group entry. Claim topics are Writing, Drums, Bass, Guitar, Synths, Vocals, Mixing and Workflow. Evidence values are `first-hand`, `qualified-recollection` and `publisher-report`; unsupported guesses should stay in coverage notes, not the factual claim collection.

## Corrections

Explain what the previous note asserted and why the source supports the correction. Do not silently replace one uncertain recollection with another. For an automatic-caption correction, provide an audio timestamp or a visible model identification with its location. Mark your own experiment as editorial advice, separate from a documented artist method.

## Rights

Contribute your own notes, not copied transcripts, articles, song lyrics, course media, private links or credentials. Link to the source owner. Source owners can open an issue identifying a concern and the affected record. Contributions of original material are offered under this repository's MIT license; third-party material retains its existing rights.
