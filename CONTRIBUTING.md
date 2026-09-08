# Contributing

Pull requests are accepted. Add a first-person interview, official transcript, timestamp, missing source or careful correction that helps a musician understand what was actually done.

## A useful contribution

Include the original source link, publication date if known, song/era, exact timestamp or printed section, and a concise original paraphrase. State what you inspected: text, automatic captions, audio, video frames or publisher metadata. Keep uncertainty and corrections; publisher equipment lists do not establish signal order.

Existing primary-source records live in `data/external.json`; the course and full podcast records live in `data/session-sources.json`. `scripts/build.py` currently holds playlist coverage metadata. Update the relevant input, keeping stable claim IDs, and run:

```sh
python3 scripts/build.py
python3 scripts/check.py
```

Commit the input and generated changes together. Preview `docs/` locally when changing the site. A new source should receive its own linked Markdown record and a playlist/source-group entry. Claim topics are Writing, Drums, Bass, Guitar, Synths, Vocals, Mixing and Workflow. Evidence values are `first-hand`, `qualified-recollection` and `publisher-report`; unsupported guesses should stay in coverage notes, not the factual claim collection.

## Corrections

Explain what the previous note asserted and why the source supports the correction. Do not silently replace one uncertain recollection with another. For an automatic-caption correction, provide an audio timestamp or a visible model identification with its location. Mark your own experiment as editorial advice, separate from a documented artist method.

## Rights

Contribute your own notes, not copied transcripts, articles, song lyrics, course media, private links or credentials. Link to the source owner. Source owners can open an issue identifying a concern and the affected record. Contributions of original material are offered under this repository's MIT license; third-party material retains its existing rights.
