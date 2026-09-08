# Master learnings

The canonical master is [TAME_IMPALA_AGENTS.md](TAME_IMPALA_AGENTS.md). All structured production claims live in [data/reference.json](data/reference.json); edit the input records described in [CONTRIBUTING.md](CONTRIBUTING.md) and regenerate.

The additional multi-artist reference is [BEST_PRODUCTION_2025_AGENTS.md](BEST_PRODUCTION_2025_AGENTS.md).

## Project workflow

- Production techniques organize the reference. Instrument topics and album eras remain source context, while album artwork supplies the website's visual language.
- Keep method priority separate from evidence confidence. A useful, specific method can still contain a qualified recollection.
- Compilations can change speaker without a heading in automatic captions. Check the adjacent excerpt boundaries against source episodes before combining claims.
- Keep agent setup prompts self-contained, including a usable reference URL and instructions for attached files. A filename alone cannot give another agent access to a document.
- Website type is pinned to Ethan's AIMVS pairing: Michroma for plain text, Microgramma D Extended Bold for headings and emphasis, both served from `docs/fonts`. Both faces are wide, so sizes run smaller than a neutral sans and long headings must be allowed to wrap. `scripts/check.py` checks the pinned font variables, vendored assets and removal of the previous font roles. Verify actual rendering at narrow widths when changing typography.
- The agent setup section starts collapsed as a native `<details>` with a caret; a link straight to `#agents` opens it. Keep the copy-prompt fallback able to open both the outer disclosure and the inner prompt.
- Keep this developer record outside generated output; the build must preserve it.
