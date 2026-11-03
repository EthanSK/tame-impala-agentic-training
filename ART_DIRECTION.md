# Art direction

The website opens inside Tame Impala’s mind, with a humorous photo collage of Kevin Parker peeking up from the bottom of the screen. The surrounding sections draw on the visual vocabulary of the five album covers through CSS and generated SVG. This page records the mapping, the palette, the type choices and the credits so the design can be audited and extended.

These are design decisions about the website. They say nothing about how the records were produced; production claims live only in [TAME_IMPALA_AGENTS.md](TAME_IMPALA_AGENTS.md) and [data/reference.json](data/reference.json).

## Album to component map

| Component | Album reference | What is borrowed | How it is built |
|---|---|---|---|
| Masthead and opening title | Ethan's AIMVS type pairing | Extended geometric capitals | Michroma wordmark, Microgramma D Extended Bold title; both served from `docs/fonts` |
| Hero | Inside Tame Impala’s mind; *Currents* (2015) | Original large face and brain cutaway, poking out from the bottom; a bundle of strands bursting from the cut and fanning into the upper-left background | `scripts/art.py` → `brain_portrait()` clips the original portrait into the shared scene as a static image; `brain_lines()` supplies full-length SVG paths behind it, launched parallel to the lid's cut edge; `waves.js` draws traveling waves on canvas from those same paths; the title uses difference blending |
| Note chips | All five | Each album's dominant colours | Small 12 px CSS swatches beside the cited era on each note |
| Search and filters | *Lonerism* (2012) | Sun-bleached garden seen through iron bars, light leak in the top corner, pale circular label | CSS gradients for the photo strip and bars; the peach circle holds the live result count; pressed topic buttons use the park-sign green |
| Production techniques | *Deadbeat* (2025) | White insert, heavy black print, monochrome grain | White paper with an SVG-noise grain overlay; the "Production techniques" title wraps to remain readable |
| Agent section | *Currents* (2015) | Pale violet streamlines on near-black, a chrome sphere bending them, a single red-to-orange streak | `scripts/art.py` → `currents()`: lines are warped around the sphere by a radial field and a trailing wobble; written to `docs/art/currents.svg`. The setup itself is a native `<details>` that starts closed: one heading row with an adjacent rotating caret, the master download and companion inside, and the optional prompt and copy button nested |
| Sources | *The Slow Rush* (2020) | Vermilion room, arched window opening to turquoise, sand filling the floor, nested doorway | CSS radial background; hand-written arch SVG (`ARCH`) and dune lip (`DUNE`); the source list sits on the sand |
| Contribute | *Deadbeat* (2025) | Giant black headline cut by the edge, orange vinyl label | Microgramma D Extended Bold, clipped at the page edge on desktop and wrapped on phones; the orange sticker is a CSS circle with a centre hole |
| Footer | The record | Vinyl grooves | `repeating-radial-gradient` centred off-canvas |
| 404 page | *The Slow Rush* (2020) | The arch, on vermilion | Same arch SVG under the repository prefix |

Notes whose era text names an album get that album's swatch; notes from interviews that name no album are grey. The album is derived from the era string in `scripts/build.py` (`album_of`) for display only.

## Palette

| Token | Hex | Source |
|---|---|---|
| `--ink` | `#111014` | Deadbeat print |
| `--paper` | `#fbfaf6` | Deadbeat insert, slightly warmed |
| `--turquoise` / `--turquoise-deep` | `#14a9b4` / `#0b7f8c` | Innerspeaker sky |
| `--autumn` | `#e0602a` | Innerspeaker foliage |
| `--peach` / `--hedge` / `--bleach` | `#f4d7a6` / `#2f5a3a` / `#dfe7db` | Lonerism label, park sign, bleached greens |
| `--violet` / `--void` | `#a88ae0` / `#0c0813` | Currents streamlines and ground |
| `--vermilion` / `--sand` | `#d9381c` / `#e2b98b` | The Slow Rush walls and dunes |
| `--tangerine` | `#f7931e` | Deadbeat vinyl label |

## Type

Ethan pinned the website to the same two faces he uses in AIMVS. Every run of text on the site, including claim IDs, timestamps, gear lines, form controls, the agent prompt, source sections, footer and the 404 page, uses one of them. There is no third family, no italic and no monospace role; `font-synthesis: none` prevents browsers from faking a bold or italic.

- **Plain text: Michroma** (`--plain`), served from `docs/fonts/Michroma-Regular.ttf` under the SIL Open Font License (`docs/fonts/OFL-Michroma.txt`). Body copy runs at 14px/1.7; small labels run 9–11px because the face is wide.
- **Headings and emphasis: Microgramma D Extended Bold** (`--brand`, CSS family `MicrogrammaBold`), served from `docs/fonts/Microgramma D Extended Bold.otf`. It carries every heading, `strong`, `summary`, button, navigation link and the Deadbeat-style headlines. The file is the same regenerated no-hint OTF AIMVS uses for Firefox's font sanitizer. It is a third-party typeface supplied from Ethan's own assets: its license terms are not recorded in this repository and it is excluded from the MIT license. Do not describe it as OFL.

Both faces load with `font-display: swap` so the notes are readable in the fallback stack (Eurostile, Bank Gothic, then Helvetica Neue / Arial) while they arrive. The pairing is a project preference carried over from AIMVS; it is not a verified identification of any typeface used on Tame Impala artwork.

## References and credits

The five reference images were the official store and artist-portfolio product images, inspected during design. None of them is shipped in this repository. If real thumbnails are wanted later, place optimised versions under `docs/art/covers/` with these credits alongside them.

- *Innerspeaker* — artwork by Leif Podhajsky: <https://leifpodhajsky.com/TAME-IMPALA-INNERSPEAKER>; product page: <https://storeus.tameimpala.com/products/innerspeaker-vinyl>
- *Lonerism* — artwork by Leif Podhajsky: <https://leifpodhajsky.com/Tame-Impala-Lonerism>; product page: <https://storeus.tameimpala.com/products/lonerism-cd>
- *Currents* — artwork by Robert Beatty: <https://robertbeattyart.com/Tame-Impala-Currents>
- *The Slow Rush* — photography by [Neil Krug](https://oriole-parrotfish-z679.squarespace.com/tameimpala); product page: <https://storeus.tameimpala.com/products/the-slow-rush-vinyl>
- *Deadbeat* — product page: <https://storeus.tameimpala.com/products/deadbeat-vinyl>

Album artwork, wordmarks and trademarks remain the property of their rights holders. The original abstract geometry generated by `scripts/art.py` and the CSS in `docs/style.css` are covered by the repository's MIT license; portrait pixels embedded in an SVG retain the portrait's third-party rights. The referenced artwork, the Michroma font (OFL) and the Microgramma D Extended Bold font (third-party rights) are not.

## Working rules for future passes

- Use album eras as visual inspiration for the UI. The opening moves from the portrait straight to the production notes; do not add a front-and-centre notes-by-era overview.
- Keep the long research text on white or sand with dark ink. Spend visual risk in the hero and the section backgrounds, not in the note list.
- Generated SVG illustrations must build deterministically from `python3 scripts/build.py`. Change the seed or parameters in `scripts/art.py`, never hand-edit generated SVG in `docs/`.
- Asset links carry a content hash (`style.css?v=…`, `app.js?v=…`, `waves.js?v=…`, `art/currents.svg?v=…`, `art/brain-portrait.svg?v=…`, portrait rasters and `favicon.png`) so readers see new styles after a deploy. `scripts/check.py` verifies the hashes match the files and that only the two portrait rasters and face/brain favicon ship.
- Keep the original large head-and-shoulders portrait at the bottom, without the elongated body or lower swirls. Fill the space above with strands coming out of the cut in the brain: the same diagonal toward the top left on every screen size, never a separate upward mobile fan. Preserve readable title blending and bound the hero height.
- Motion includes disclosure expansion and collapse, button hover, the agent caret turning and traveling waves along the hero strands; these stop under `prefers-reduced-motion`. Never autoplay audio or video.
- Keep the type pairing exactly as pinned above. New text takes `var(--plain)` or `var(--brand)`; `scripts/check.py` checks the pinned font variables, vendored assets and removal of the previous font roles.
- The "Ask your agents" section starts collapsed. Its closed row is the heading plus a caret only; put no paragraph in the resting state. Opening it shows the master-file instruction and companion, with the optional prompt and copy button in a nested disclosure. Place this section just below the initial viewport, with the original portrait anchored at the bottom of the hero and the brain waves behind the title. Keep this until Ethan changes direction.


## Portrait

The opening image is an AI-generated fan-art transformation of a recent press photograph, showing a playful toy-like brain cutaway. It is deliberately surreal. Its reference is the Kevin Parker portrait credited to **Julian Klincewicz** in [Sony Music Canada’s Deadbeat announcement, published 5 September 2025](https://www.sonymusic.ca/press_release/tame-impala-announces-album). That establishes the campaign and publication date, not a separately verified capture date. The unmodified press photograph is not distributed here. The original photograph’s rights remain with its owner; the repository’s MIT license does not grant rights to that source or the derivative portrait.

The built-in image generation tool created `docs/art/inside-kevins-mind.png`. Its prompt asked for Kevin’s recognizable 2025 appearance, his head peeking from the bottom centre of a wide warm-white canvas, and a clean, humorous pink brain cutaway with the hair lifting like a lid. There is no gore. HTML supplies the title and controls, so the image contains no baked-in text. On desktop the face occupies roughly a third of the viewport width; on phones a centred crop keeps the brain and face visible.

That wide head collage now serves as the social preview image (`og:image`). Both rasters are saved assets, not regenerated during the deterministic site build; their content hashes are inserted into the page and verified by the checks.

### Brain-originating Currents background

The current hero restores the original wide portrait. `scripts/art.py` contains an editable SVG outline around that generated fan portrait; the image pixels are unchanged. The portrait and strand origins share coordinates in a 1942×3000 scene, so they stay connected under responsive scaling. The scene is two layers in one box: `art/brain-portrait.svg` (the clipped raster, a static `<img>`) on top, and the strand layer from `brain_lines()` inlined in the page beneath it.

The strands are anchored to the picture's cut geometry rather than a hovering cone. Read from the portrait pixels: the lifted lid's cut edge runs from its tip near (945,100) to the hinge near (1265,335), about 36°, and the only exposed brain silhouette is the upper-left arc from (815,277) to (989,170) plus the notch under the lid tip. So the 115 strands originate along the skull's front rim just under the fringe (`CUT_RIM`, (845,316)→(1125,358)) and leave parallel to the lid's edge (`LID_ANGLE`, 36° toward the top left); the bundle surfaces through that exposed arc as if pouring out of the opening. After a straight run they spread to the approved far ends, from level-left to nearly vertical, behind the title. The gradient wedge is bounded by the first and last strand and closes along the rim, hidden inside the head.

One geometry serves every screen. On phones the scene is narrower, so the shallow strands leave the left edge at the same angle while the steep ones reach the top; line and wedge opacity drop (`--thread-opacity`, `--thought-opacity`) for legibility behind small centred text. The title uses difference blending against the strand field while the other text retains its normal rendering. No lower ribbon band, landscape sticker or abstract torso appears in the hero.

`docs/waves.js` samples the SVG paths once per resize and draws traveling normal displacements on a viewport-sized Canvas 2D layer beneath the static portrait. The first 160 scene units remain fixed; a smooth 650-unit ramp increases motion to a 48-unit amplitude, with a smaller secondary wave. This produces visible undulation along the strands rather than rotating almost-straight lines imperceptibly. The filled backdrop follows the outer animated strands. Pixel ratio is capped at two; animation pauses when the hero leaves the viewport, the document is hidden, or reduced motion is requested.

The original curves continue another 10,000 scene units along their endpoint tangents, and the SVG allows overflow beyond its own viewBox. Only the hero clips the artwork. Canvas samples just the length needed to exceed the current viewport plus an overscan margin. This preserves the diagonal launch while preventing exposed path endpoints or a flat cutoff on very narrow, tall screens. Without JavaScript or Canvas 2D, the full-length inline SVG remains visible; reduced motion draws the undeformed geometry without a frame loop.

Desktop scene width is bounded to 1280–1800px; mobile scene width to 780–1160px. Hero height is bounded to 620–860px on desktop and 720–980px on mobile. The original portrait sits exactly at the lower edge with its proportions preserved.

The superseded `psychedelic-body.png` and generated string artwork remain archived in the repository, but are not used in the current hero.

### Transparent face and brain favicon

`docs/favicon.png` is a 64×64 RGBA icon. `docs/favicon.svg` preserves the editable silhouette clipping source with its embedded face/brain artwork. The icon has transparent outside pixels rather than a cream square; main page and custom 404 use its content hash. Render the SVG on a transparent canvas and retain alpha when exporting PNG. Check both light and dark backgrounds at small sizes.

The initial face/brain square came from built-in image generation. Attempts to extract a transparent background returned opaque checkerboards, so those were not shipped. The original face pixels were retained in the SVG cutout, which was rendered to transparent PNG with ImageMagick. This remains generated fan art derived from the credited press portrait, not an authentic photograph of an exposed brain or work covered by the MIT license.
