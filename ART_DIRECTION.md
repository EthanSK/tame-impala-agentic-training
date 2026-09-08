# Art direction

The website opens inside Tame Impala’s mind, with a humorous photo collage of Kevin Parker peeking up from the bottom of the screen. The surrounding sections draw on the visual vocabulary of the five album covers through CSS and generated SVG. This page records the mapping, the palette, the type choices and the credits so the design can be audited and extended.

These are design decisions about the website. They say nothing about how the records were produced; production claims live only in [TAME_IMPALA_AGENTS.md](TAME_IMPALA_AGENTS.md) and [data/reference.json](data/reference.json).

## Album to component map

| Component | Album reference | What is borrowed | How it is built |
|---|---|---|---|
| Masthead and opening title | Ethan's AIMVS type pairing | Extended geometric capitals | Michroma wordmark, Microgramma D Extended Bold title; both served from `docs/fonts` |
| Hero | Inside Tame Impala’s mind; *Currents* (2015); *Innerspeaker* (2010) | Recent-photo likeness with the playful pink brain cutaway, an impossibly long liquid torso and arms, waves that become strings, and a small tilted landscape fragment | `docs/art/psychedelic-body.png` is enlarged beside the copy and cropped by the bounded hero; `scripts/art.py` → `strings()` widens its waves into a full-width ribbon band that thins into violet strings; `lip()` raises the dark Currents strip into the hero as a wave; `innerspeaker()` supplies the landscape fragment |
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

Album artwork, wordmarks and trademarks remain the property of their rights holders. The site's SVG illustrations are original abstractions generated by `scripts/art.py` and the CSS in `docs/style.css`; they are covered by the repository's MIT license. The referenced artwork, the Michroma font (OFL) and the Microgramma D Extended Bold font (third-party rights) are not.

## Working rules for future passes

- Use album eras as visual inspiration for the UI. The opening moves from the portrait straight to the production notes; do not add a front-and-centre notes-by-era overview.
- Keep the long research text on white or sand with dark ink. Spend visual risk in the hero and the section backgrounds, not in the note list.
- Generated SVG illustrations must build deterministically from `python3 scripts/build.py`. Change the seed or parameters in `scripts/art.py`, never hand-edit generated SVG in `docs/`.
- Asset links carry a content hash (`style.css?v=…`, `app.js?v=…`, `art/currents.svg?v=…`, `art/strings.svg?v=…`, portrait rasters and `favicon.png`) so readers see new styles after a deploy. `scripts/check.py` verifies the hashes match the files and that only the two portrait rasters and face/brain favicon ship.
- Frame a close portrait rather than fitting the entire tall illustration. Desktop uses a 680–1080px-wide figure inside a 560–800px-high hero; mobile hero height is bounded to 720–980px and reveals more of the long body when space allows. Crop the lower artwork, never stretch the face or add blank spacers.
- Motion includes disclosure expansion and collapse, button hover and the agent caret turning; these stop under `prefers-reduced-motion`. Never autoplay audio or video.
- Keep the type pairing exactly as pinned above. New text takes `var(--plain)` or `var(--brand)`; `scripts/check.py` checks the pinned font variables, vendored assets and removal of the previous font roles.
- The "Ask your agents" section starts collapsed. Its closed row is the heading plus a caret only; put no paragraph in the resting state. Opening it shows the master-file instruction and companion, with the optional prompt and copy button in a nested disclosure. Place this section just below the initial viewport, with the figure starting near the copy and its liquid body filling the hero. Keep this until Ethan changes direction.


## Portrait

The opening image is an AI-generated fan-art transformation of a recent press photograph, showing a playful toy-like brain cutaway. It is deliberately surreal. Its reference is the Kevin Parker portrait credited to **Julian Klincewicz** in [Sony Music Canada’s Deadbeat announcement, published 5 September 2025](https://www.sonymusic.ca/press_release/tame-impala-announces-album). That establishes the campaign and publication date, not a separately verified capture date. The unmodified press photograph is not distributed here. The original photograph’s rights remain with its owner; the repository’s MIT license does not grant rights to that source or the derivative portrait.

The built-in image generation tool created `docs/art/inside-kevins-mind.png`. Its prompt asked for Kevin’s recognizable 2025 appearance, his head peeking from the bottom centre of a wide warm-white canvas, and a clean, humorous pink brain cutaway with the hair lifting like a lid. There is no gore. HTML supplies the title and controls, so the image contains no baked-in text. On desktop the face occupies roughly a third of the viewport width; on phones a centred crop keeps the brain and face visible.

That wide head collage now serves as the social preview image (`og:image`). Both rasters are saved assets, not regenerated during the deterministic site build; their content hashes are inserted into the page and verified by the checks.

### The elongated figure

`docs/art/psychedelic-body.png` (1024 × 1536) is the hero image. It is fan art, not a photograph of anyone's body: the same built-in image generation tool extended the head collage downward into an invented, impossibly long liquid torso and arms that dissolve into parallel pink, coral, purple and turquoise waves on a cream ground. The brain cutaway and likeness are preserved from the first collage; everything below the neck is abstract. The rights position is the same as the head collage: derived from the Julian Klincewicz press portrait, not covered by the MIT license.

How it is composed on the page:

- Desktop enlarges the figure to `clamp(680px, 64vw, 1080px)` and clips it inside a hero whose height is `clamp(560px, 100svh - 80px, 800px)`. The face remains proportional. The whole tall illustration is deliberately not shown.
- On mobile, the hero is bounded to 720–980px. The figure fills the space below the controls; its image remains taller than the crop. Extra height reveals more of the abstract body, not empty space above the head.
- A short generated parallel ribbon band and the dark Currents lip blend the cropped lower body into the next section. Figure-container darken blending, a lower-edge mask and image side masks keep the warm raster background from appearing as a rectangle.

### Face and brain favicon

`docs/favicon.png` is a 64×64 browser icon exported from a square built-in image-generation edit of the same fan portrait. It tightly frames Kevin's face, lifted hair and colourful brain. Both the main page and custom 404 use the hashed PNG. The original full-resolution icon artwork is preserved in the private delivery archive; it is not a new authentic photograph or covered by the MIT license.
