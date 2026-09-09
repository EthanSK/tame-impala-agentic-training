# Master learnings

The canonical master is [TAME_IMPALA_AGENTS.md](TAME_IMPALA_AGENTS.md). All structured production claims live in [data/reference.json](data/reference.json); edit the input records described in [CONTRIBUTING.md](CONTRIBUTING.md) and regenerate.

The additional multi-artist reference is [BEST_PRODUCTION_2025_AGENTS.md](BEST_PRODUCTION_2025_AGENTS.md).

## Project workflow

- Production techniques organize the reference. Instrument topics and album eras remain source context, while album artwork supplies the website's visual language.
- Keep method priority separate from evidence confidence. A useful, specific method can still contain a qualified recollection.
- Three coarse priorities followed by technique-family order do not produce a useful default reading order: they placed the first capture note ahead of broadly applicable techniques from other families. The website now uses an explicit, complete claim-ID order in `data/techniques.json`; render that order into static HTML so filters, clearing filters and no-JavaScript browsing retain it. Keep source records and grouped master-guide order independent.
- Compilations can change speaker without a heading in automatic captions. Check the adjacent excerpt boundaries against source episodes before combining claims.
- Keep agent setup prompts self-contained, including a usable reference URL and instructions for attached files. A filename alone cannot give another agent access to a document.
- Website type is pinned to Ethan's AIMVS pairing: Michroma for plain text, Microgramma D Extended Bold for headings and emphasis, both served from `docs/fonts`. Both faces are wide, so sizes run smaller than a neutral sans and long headings must be allowed to wrap. `scripts/check.py` checks the pinned font variables, vendored assets and removal of the previous font roles. Verify actual rendering at narrow widths when changing typography.
- The agent setup section is labelled "Ask your agents", with its caret immediately after the text, and starts collapsed just below the initial viewport. A link straight to `#agents` opens it. Keep the copy-prompt fallback able to open both the outer disclosure and the inner prompt.
- Animate all native disclosures in both directions, including interrupted/reversed transitions. Keep their content and native toggling available without JavaScript; reduced motion should finish immediately.
- Keep the original large portrait at the bottom edge. The current visual direction replaces the elongated torso with brain-originating Currents lines: a diagonal desktop fan and an upward mobile fan. Draw portrait and waves in shared SVG coordinates so the lines stay attached to the brain at every size.
- Give the mobile scene enough vertical canvas to cover the tallest allowed hero; sizing only for a standard phone leaves a flat cut-off above the waves on taller screens. Verify the top edge as well as the portrait.
- Apply title blending on the element that shares the artwork's stacking context; an intervening isolated container prevents the intended interaction. Keep mobile wave contrast lower behind small body text.
- A checkerboard preview is not proof of transparency. Verify exported RGBA alpha and all four corners, then inspect the actual favicon at 16, 32 and 64 pixels on light and dark backgrounds. Keep the editable SVG contour alongside the exported PNG.
- Keep this developer record outside generated output; the build must preserve it.

- Access errors are dated observations, not permanent source status. Recheck a previously private playlist ID before treating it as lost; the 9 September caption audit recovered the public drum edit. Keep source metadata in data/youtube-playlist.json so generated pages cannot repeat stale hardcoded gaps.
- Count reviewed caption cues and preserve the original export alongside readable Markdown. A full caption-text review does not establish a complete human audio/frame audit. Publisher transcripts may collapse all speakers into one label and provide no useful timestamps; cite descriptive sections instead of inventing times.
- Compare related interview accounts before assigning equipment. An ambiguous later automatic-caption fragment must not override a clear earlier sampler explanation, and similar phone-demo anecdotes can concern different songs.
