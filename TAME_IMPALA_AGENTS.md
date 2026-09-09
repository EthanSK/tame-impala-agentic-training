# Tame Impala Production — agent reference (TAME_IMPALA_AGENTS.md)

169 source-linked production notes · 35 source records · Updated 9 September 2026

This is the canonical production-technique reference of the tame-impala-agentic-training repository. Use it with an agent to solve a musical problem: choose a documented method, understand the decision behind it, and try an adaptation with the tools you have. Every note keeps its stable claim ID, original source, timestamp or section, song/era and evidence label. Technique groups and practical priority are editorial organization, not confidence ratings. Gear is supporting context, not a requirement to buy the same equipment. Answering rules live in [AGENTS.md](AGENTS.md); read/unread boundaries live in [COVERAGE.md](COVERAGE.md).

## Use this with your agent

Attach this file and describe what you want to change in your production, your DAW and the tools available. Ask the agent to identify a relevant technique, cite the claim and its source, and suggest one small experiment. It should explain what to listen for and keep its proposed settings separate from Parker’s documented actions. Keep your existing project instructions; this is an additional reference, not a replacement for them.

> Help me apply a documented production technique with the tools I have. Cite the claim ID, original source and timestamp or section; preserve the era and every qualification. Explain the method before naming equipment. Clearly label your suggested experiments and substitutions. Never invent settings, presets or unreviewed source content.

## Read the evidence correctly

- **First-hand:** Parker’s statement in an interview, including caption/ASR-derived accounts. This label describes who spoke, not a certified transcript or independent replication.
- **Qualified recollection:** Parker is uncertain, corrects himself, or reconstructs an old setup. Preserve the qualification.
- **Publisher report:** identification or narration supplied by the publisher, rather than a securely attributed artist statement.
- Timestamps are local to the stated video part. TN188 times follow an ad-supported 81:23 copy; inserted advertisements can move player offsets.
- Supplied course captions, podcast transcripts and all six playlist caption tracks were text-reviewed; complete video-frame and human audio audits were not performed.
- All six playlist clips now have caption-based coverage, including the formerly private drum clip. The wider interview search is bounded, with gated and partially reviewed sources still listed in [COVERAGE.md](COVERAGE.md).

## Find your way

[All sources](SOURCES.md) · [Playlists](playlists/README.md) · [Machine-readable JSON](data/reference.json) · [Agent instructions](AGENTS.md) · [Gear index](GEAR.md) · [Best Production 2025 companion](BEST_PRODUCTION_2025_AGENTS.md)

## Working principles — editorial synthesis

These prompts are our interpretation of the cited accounts, not additional Kevin Parker quotations.

1. Capture an idea before polishing your ability to perform it (TN188-01; MW1-01).
2. Work on the groove and interacting envelopes before chasing a more expensive signal chain (MW2-01; MW2-11).
3. Let an unfamiliar instrument interrupt familiar playing habits (GW05; check the source record for context).
4. Treat sonic character as an arrangement decision: a dry hook, whisper sides or a small drum palette changes the identity (TN188-04, TN188-12, TN188-13).
5. Compare methods and keep what earns its place; the abandoned summing experiment is as instructive as the retained hardware (MW5-01).
6. Keep alternate takes, source links and uncertainty so later decisions remain reversible.

## Important corrections and unresolved details

- The Less I Know the Better’s opening bass riff is a guitar-synth sound; a later bass part is corrected to Greco in MW1. General Hofner use elsewhere does not override that correction.
- Ableton delay names in an old Currents recollection do not prove that the modern Echo device was used on that recording.
- MW5 tentatively mentions an SSL bus compressor; Sound On Sound publisher narration mentions Manley. The accounts do not establish one combined chain.
- Deadbeat’s microphone discussion corrects SM57 to SM7; a U47-style clone has no securely established manufacturer here.
- Let It Happen’s 2015 sampler explanation (EXP05-01) is more explicit than the partial device word in the 2025 automatic caption (ZL25-02); do not identify a vocoder from that fragment.
- No Reply’s retained piano memo (EXP04-01) and My Old Ways’ re-recorded opening (TN188-02) concern different songs.
- Tape Notes sponsors are not evidence of Kevin’s equipment. Exact plugin settings, amp models and several old patch names remain unknown.

## Choose a production technique

Each group puts specific methods before supporting practices and historical or equipment context. Priority describes usefulness for a session; it never removes a source qualification.

- [Capture & commit](#capture) — Record ideas and performances, choose microphone placement and monitoring, and decide what to print or retain.
- [Build a groove](#groove) — Shape rhythmic feel through playing, loop editing, percussion placement and the interaction of bass and drums.
- [Shape a sound](#sound) — Change tone through instrument setup, synthesis, filtering, distortion and signal order.
- [Create space](#space) — Use ambience, vocal doubles, panning and effects routing to create depth, width and movement.
- [Control dynamics](#dynamics) — Shape envelopes, compression and limiting while preserving the intended impact.
- [Choose & arrange](#decisions) — Develop ideas, choose layers and sections, test alternatives and judge a mix in context.

<a id="capture"></a>
## Capture & commit

### TO01 · Snare-side microphone
An AKG D190 beside the snare shell became a principal kit microphone after heavy compression; attack and release were crucial.

- **Topic:** Drums
- **Context:** InnerSpeaker / 2010
- **Evidence:** first-hand · [Tape Op: Tame Impala: Aussie Psyche Explosion](https://tapeop.com/interviews/95/tame-impala) · What did you end up doing for the drums?
- **Gear context:** AKG D190
[Source record](sources/external/s01.md)

### TO03 · Kick capture
The kick used an SM57 at a distance, with both drumheads and little damping, avoiding excessive beater attack.

- **Topic:** Drums
- **Context:** InnerSpeaker / 2010
- **Evidence:** first-hand · [Tape Op: Tame Impala: Aussie Psyche Explosion](https://tapeop.com/interviews/95/tame-impala) · What did you end up doing for the drums?
- **Gear context:** Shure SM57
[Source record](sources/external/s01.md)

### TO06 · Print guitar effects
Pedals fed a Seymour Duncan DI and mixer; he preferred printing guitar effects while tracking.

- **Topic:** Guitar
- **Context:** InnerSpeaker / 2010
- **Evidence:** first-hand · [Tape Op: Tame Impala: Aussie Psyche Explosion](https://tapeop.com/interviews/95/tame-impala) · How do you typically mic guitars?; delay question
- **Gear context:** Seymour Duncan DI
[Source record](sources/external/s01.md)

### GW04 · Perform into effects
He wants to hear the intended effected tone while playing, and rarely relies on later reamping or guitar-shaping plugins.

- **Topic:** Guitar
- **Context:** 2022 interview
- **Evidence:** first-hand · [Guitar World interview](https://www.guitarworld.com/features/tame-impala-kevin-parker) · Pedalboard or plugins?; reamping question
- **Gear context:** No specific model established
[Source record](sources/external/s03.md)

### KX02 · Capture demos anywhere
He captured demos wherever ideas occurred, with a home studio providing the main continuous workspace.

- **Topic:** Workflow
- **Context:** Currents / 2015
- **Evidence:** first-hand · [KEXP interview about Currents](https://www.kexp.org/read/2015/7/8/interview-tame-impalas-kevin-parker-on-his-personal-danceable-new-album-currents/) · Recording on the road?
- **Gear context:** No specific model established
[Source record](sources/external/s06.md)

### EXP04-01 · A phone demo can become the master
No Reply uses his original piano phone memo after he lost a replacement recorded with a stereo microphone.

- **Topic:** Workflow
- **Context:** Deadbeat
- **Evidence:** first-hand · [triple j: Deadbeat and simplicity](https://www.abc.net.au/triplej/news/tame-impala-interview-deadbeat-new-album-lucy-smith/105905616) · Closing No Reply piano discussion
- **Gear context:** No specific model established
[Source record](sources/external/exp04.md)

### EXP05-01 · Keep the phonetic take
Let It Happen retains the initial nonsensical sampler-vocal performance because later real lyrics lost its groove. He distinguishes it from a vocoder; exact device unknown.

- **Topic:** Vocals
- **Context:** Currents
- **Evidence:** first-hand · [Under the Radar: Cover Story Bonus Q&A](https://www.undertheradarmag.com/interviews/tame_impala_cover_story_bonus_2015/) · Q: You said before that you spend most of your studio time trying to recapture the spirit of your original demo
- **Gear context:** keyboard sampler (unspecified)
[Source record](sources/external/exp05.md)

### EXP07-03 · Make tone settings repeatable
He values the Hagstrom Impala’s switches because a known combination makes later alternate takes easier to match.

- **Topic:** Workflow
- **Context:** Studio practice described in 2021
- **Evidence:** first-hand · [Guitar.com: Ten years of InnerSpeaker](https://guitar.com/features/interviews/tame-impala-kevin-parker-10-years-innerspeaker/) · Tamed impala
- **Gear context:** Hagstrom Impala
[Source record](sources/external/exp07.md)

### EXP09-01 · Batch the drum session
He prepared drumless songs, then recorded their drum takes during a limited daytime session at a pub.

- **Topic:** Drums
- **Context:** Early EP sessions, recalled in 2020
- **Evidence:** first-hand · [Zane Lowe: The Slow Rush interview](https://www.youtube.com/watch?v=Kr28pGJZ3nY) · 27:13–27:56
- **Gear context:** No specific model established
[Source record](sources/external/exp09.md)

### AM06 · Capture the idea with available input
Without an interface, he recorded the Apocalypse Dreams breakdown lead guitar directly into his MacBook line input to preserve the inspired moment.

- **Topic:** Guitar
- **Context:** Lonerism, recalled in 2015
- **Evidence:** first-hand · [Kevin Parker Reddit AMA](https://www.reddit.com/r/IAmA/comments/34clpm/i_am_kevin_parker_from_tame_impala_ask_me_anything/) · https://www.reddit.com/r/IAmA/comments/34clpm/comment/cqtkpgu/
- **Gear context:** MacBook line input
[Source record](sources/external/s07.md)

### MW2-02 · Reduce sympathetic ringing at the kit
He names a Ludwig Supraphonic 400 snare and Tama kick and describes removing toms to reduce unwanted resonance.

- **Topic:** Drums
- **Context:** Currents / The Less I Know the Better
- **Evidence:** first-hand · [Mix With The Masters, part 2: Drums and groove](https://mixwiththemasters.com/videos/kevin-parker-tame-impala-the-less-i-know-the-better) · 00:46–01:30
- **Gear context:** Ludwig Supraphonic 400, Tama kick
[Source record](sources/mix-with-the-masters/mw2.md)

### MW2-04 · Work with imperfect microphone capture
He recalls a borrowed vocal microphone on kick, a 57 beside the snare and another microphone above; the borrowed microphone model is unidentified.

- **Topic:** Drums
- **Context:** Currents / The Less I Know the Better
- **Evidence:** qualified-recollection · [Mix With The Masters, part 2: Drums and groove](https://mixwiththemasters.com/videos/kevin-parker-tame-impala-the-less-i-know-the-better) · 01:47–03:03
- **Gear context:** Shure SM57
[Source record](sources/mix-with-the-masters/mw2.md)

### MW3-07 · Monitor for a comfortable performance
He describes tracking with one headphone ear off and monitoring through the interface rather than hearing DAW effects; Lynx Aurora is a tentative recollection.

- **Topic:** Vocals
- **Context:** Currents / The Less I Know the Better
- **Evidence:** qualified-recollection · [Mix With The Masters, part 3: Vocals and effects](https://mixwiththemasters.com/videos/kevin-parker-tame-impala-the-less-i-know-the-better) · 03:20–03:56
- **Gear context:** Lynx Aurora
[Source record](sources/mix-with-the-masters/mw3.md)

### TN188-01 · Record before working the idea out
He records a phone memo while learning an idea so that the act of playing it does not overwrite the original thought.

- **Topic:** Writing
- **Context:** Deadbeat / My Old Ways, Loser and related songs
- **Evidence:** first-hand · [Tape Notes 188: Tame Impala — My Old Ways and Loser](https://podcasts.apple.com/us/podcast/tn-188-tame-impala/id1249834293?i=1000787528506) · 09:11–11:45
- **Gear context:** No specific model established
[Source record](sources/tape-notes/tn188.md)

### TN188-02 · Recreate the room, keep the intention
My Old Ways begins with a re-recorded living-room piano, not the initial memo. He wanted a stereo version that preserved the intimate perspective.

- **Topic:** Workflow
- **Context:** Deadbeat / My Old Ways, Loser and related songs
- **Evidence:** first-hand · [Tape Notes 188: Tame Impala — My Old Ways and Loser](https://podcasts.apple.com/us/podcast/tn-188-tame-impala/id1249834293?i=1000787528506) · 08:38–09:00; 15:45–16:32
- **Gear context:** Zoom stereo recorder (model unspecified)
[Source record](sources/tape-notes/tn188.md)

### TN188-21 · Loser used a different recording method
The song largely retained its studio multitracking to tape, beginning with a complete drum performance and layering instruments afterward, with very little looping. He later corrects himself about Innerspeaker, recalling that it too was recorded largely from beginning to end without looping.

- **Topic:** Workflow
- **Context:** Deadbeat / Loser; Innerspeaker recollection
- **Evidence:** qualified-recollection · [Tape Notes 188: Tame Impala — My Old Ways and Loser](https://podcasts.apple.com/us/podcast/tn-188-tame-impala/id1249834293?i=1000787528506) · 56:21–59:58; 63:13–63:34
- **Gear context:** tape machine (model unspecified)
[Source record](sources/tape-notes/tn188.md)

### TO05 · Familiar recorder
He chose the Boss BR-1600 because its familiar workflow made recording intuitive.

- **Topic:** Workflow
- **Context:** InnerSpeaker / 2010
- **Evidence:** first-hand · [Tape Op: Tame Impala: Aussie Psyche Explosion](https://tapeop.com/interviews/95/tame-impala) · What did you record to?
- **Gear context:** Boss BR-1600
[Source record](sources/external/s01.md)

### TO07 · Private vocal takes
He recorded vocals at home because other people nearby inhibited him.

- **Topic:** Vocals
- **Context:** InnerSpeaker / 2010
- **Evidence:** first-hand · [Tape Op: Tame Impala: Aussie Psyche Explosion](https://tapeop.com/interviews/95/tame-impala) · Did you have to do anything to treat the space?
- **Gear context:** No specific model established
[Source record](sources/external/s01.md)

### SE04 · Demo drums survive
The finished drums came from the initial demo, subsequently chopped and processed.

- **Topic:** Drums
- **Context:** The Slow Rush / It Might Be Time
- **Evidence:** first-hand · [Song Exploder 183: It Might Be Time](https://songexploder.net/tame-impala) · PDF p2
- **Gear context:** No specific model established
[Source record](sources/external/s02.md)

### SOS05 · Permanent routing
His Studer 963 routed permanently connected instruments; he did not mix through it.

- **Topic:** Workflow
- **Context:** 2020 interview
- **Evidence:** publisher-report · [Sound On Sound: The Psychedelic World of Kevin Parker](https://www.soundonsound.com/people/tame-impala) · Current Events
- **Gear context:** Studer 963
[Source record](sources/external/s04.md)

### EXP02-03 · Resist automatic cleanup
On moving from eight-track to computer recording, he resisted correcting every flaw and retained imperfect singing.

- **Topic:** Workflow
- **Context:** Lonerism
- **Evidence:** first-hand · [Stereogum: Progress Report: Tame Impala](https://stereogum.com/1115931/progress-report-tame-impala/interviews/progress-report) · Q: Does bringing in all those added elements make the entire process even more complicated?
- **Gear context:** No specific model established
[Source record](sources/external/exp02.md)

### MW1-01 · Keep the first spark
A short spontaneous demo became the foundation of the record; Parker kept its first section rather than replacing every rough detail.

- **Topic:** Writing
- **Context:** Currents / The Less I Know the Better
- **Evidence:** first-hand · [Mix With The Masters, part 1: Demo and guitar synth](https://mixwiththemasters.com/videos/kevin-parker-tame-impala-the-less-i-know-the-better) · 00:33–03:16
- **Gear context:** No specific model established
[Source record](sources/mix-with-the-masters/mw1.md)

### MW1-06 · Leave useful mistakes in
The rough original performance contains small mistakes, which did not prevent it becoming the final foundation.

- **Topic:** Workflow
- **Context:** Currents / The Less I Know the Better
- **Evidence:** first-hand · [Mix With The Masters, part 1: Demo and guitar synth](https://mixwiththemasters.com/videos/kevin-parker-tame-impala-the-less-i-know-the-better) · 07:00–07:40
- **Gear context:** No specific model established
[Source record](sources/mix-with-the-masters/mw1.md)

### MW1-07 · Reuse a recorded drum idea
He reused a drum recording made weeks earlier and thinks it was recorded outside; he wanted a controlled, dry contrast to Lonerism room wash.

- **Topic:** Drums
- **Context:** Currents / The Less I Know the Better
- **Evidence:** qualified-recollection · [Mix With The Masters, part 1: Demo and guitar synth](https://mixwiththemasters.com/videos/kevin-parker-tame-impala-the-less-i-know-the-better) · 07:43–08:31
- **Gear context:** No specific model established
[Source record](sources/mix-with-the-masters/mw1.md)

### MW2-01 · Performance before a preamp upgrade
Parker emphasizes playing and listening over premium preamps, recalling a relatively inexpensive PreSonus rack unit without confidently naming its model.

- **Topic:** Drums
- **Context:** Currents / The Less I Know the Better
- **Evidence:** qualified-recollection · [Mix With The Masters, part 2: Drums and groove](https://mixwiththemasters.com/videos/kevin-parker-tame-impala-the-less-i-know-the-better) · 00:20–00:46
- **Gear context:** PreSonus preamp (model uncertain)
[Source record](sources/mix-with-the-masters/mw2.md)

### MW2-07 · Unprinted outboard complicates recall
He describes not having printed the outboard drum sound and needing the hardware running at final mix time. The recall difficulty is explicit; printing stems is an editorial practical implication.

- **Topic:** Workflow
- **Context:** Currents / The Less I Know the Better
- **Evidence:** first-hand · [Mix With The Masters, part 2: Drums and groove](https://mixwiththemasters.com/videos/kevin-parker-tame-impala-the-less-i-know-the-better) · 04:48–05:03
- **Gear context:** No specific model established
[Source record](sources/mix-with-the-masters/mw2.md)

### TN188-09 · Comfort determines the microphone
He values holding the microphone; a U47-style clone sounded good but did not suit that performance habit. He corrects an initial SM57 reference to SM7.

- **Topic:** Vocals
- **Context:** Deadbeat / My Old Ways, Loser and related songs
- **Evidence:** first-hand · [Tape Notes 188: Tame Impala — My Old Ways and Loser](https://podcasts.apple.com/us/podcast/tn-188-tame-impala/id1249834293?i=1000787528506) · 33:59–35:03
- **Gear context:** Shure SM7 family, U47-style clone (manufacturer unspecified)
[Source record](sources/tape-notes/tn188.md)

### TN188-22 · Full takes carry pressure and imperfections
He describes tape-recording anxiety, stick clicks and other retained performance details. He later recalls a click printed to tape, so this should not be reported as definitely click-free.

- **Topic:** Drums
- **Context:** Deadbeat / My Old Ways, Loser and related songs
- **Evidence:** qualified-recollection · [Tape Notes 188: Tame Impala — My Old Ways and Loser](https://podcasts.apple.com/us/podcast/tn-188-tame-impala/id1249834293?i=1000787528506) · 59:58–61:13; 64:09–64:29
- **Gear context:** No specific model established
[Source record](sources/tape-notes/tn188.md)

### TO04 · Tracking support
Tim Holmes encouraged Neve preamps and a Distressor for bass and vocals.

- **Topic:** Workflow
- **Context:** InnerSpeaker / 2010
- **Evidence:** first-hand · [Tape Op: Tame Impala: Aussie Psyche Explosion](https://tapeop.com/interviews/95/tame-impala) · Did you have to do anything to treat the space?
- **Gear context:** Neve preamps, Distressor
[Source record](sources/external/s01.md)

### SOS07 · Microphone eras
Lonerism: MD421; Currents: SM7B; The Slow Rush sessions: RE20, then SM7B after losing the RE20.

- **Topic:** Vocals
- **Context:** Lonerism, Currents and The Slow Rush (reported 2020)
- **Evidence:** publisher-report · [Sound On Sound: The Psychedelic World of Kevin Parker](https://www.soundonsound.com/people/tame-impala) · Vocal Sound
- **Gear context:** Sennheiser MD421, Shure SM7B, Electro-Voice RE20
[Source record](sources/external/s04.md)

### EXP05-03 · Take counters include fragments
His four-digit vocal-take count could include aborted words or individual lines, not thousands of complete performances.

- **Topic:** Vocals
- **Context:** Currents
- **Evidence:** first-hand · [Under the Radar: Cover Story Bonus Q&A](https://www.undertheradarmag.com/interviews/tame_impala_cover_story_bonus_2015/) · Opening question on minute details
- **Gear context:** No specific model established
[Source record](sources/external/exp05.md)

### BR20-08 · Discover overdubbing with playback
As a child, he recorded keyboard over playback of his own drums using two cassette decks.

- **Topic:** Workflow
- **Context:** Childhood recording, recalled 2020
- **Evidence:** first-hand · [Broken Record: Tame Impala with Rick Rubin](https://www.pushkin.fm/podcasts/broken-record/tame-impala) · First experiments with recording and multitracking
- **Gear context:** No specific model established
[Source record](sources/external/br20.md)

### MW2-03 · Separate this setup from other bedrooms
Duvets describe a bedroom method, whereas he recalls this particular take as outdoors. These are alternatives, not one combined recording setup.

- **Topic:** Drums
- **Context:** Currents / The Less I Know the Better
- **Evidence:** qualified-recollection · [Mix With The Masters, part 2: Drums and groove](https://mixwiththemasters.com/videos/kevin-parker-tame-impala-the-less-i-know-the-better) · 00:46–01:47
- **Gear context:** No specific model established
[Source record](sources/mix-with-the-masters/mw2.md)

### MW3-01 · Keep the microphone recollection qualified
He recalls an SM7-family microphone and possibly the PreSonus preamp, probably without compression during tracking. This is a Currents recollection, not his later Deadbeat chain.

- **Topic:** Vocals
- **Context:** Currents / The Less I Know the Better
- **Evidence:** qualified-recollection · [Mix With The Masters, part 3: Vocals and effects](https://mixwiththemasters.com/videos/kevin-parker-tame-impala-the-less-i-know-the-better) · 00:07–00:34
- **Gear context:** Shure SM7 family, PreSonus preamp (model uncertain)
[Source record](sources/mix-with-the-masters/mw3.md)

<a id="groove"></a>
## Build a groove

### SE06 · Bass and drums
He recommends hearing the synth bass together with drums to judge the feeling.

- **Topic:** Bass
- **Context:** The Slow Rush / It Might Be Time
- **Evidence:** first-hand · [Song Exploder 183: It Might Be Time](https://songexploder.net/tame-impala) · PDF p3
- **Gear context:** No specific model established
[Source record](sources/external/s02.md)

### GW03 · First-take riff
The released riff loops roughly two bars from his first spontaneous performance.

- **Topic:** Bass
- **Context:** Currents / The Less I Know the Better (recalled 2022)
- **Evidence:** first-hand · [Guitar World interview](https://www.guitarworld.com/features/tame-impala-kevin-parker) · The Less I Know the Better recording question
- **Gear context:** Roland GR-55
[Source record](sources/external/s03.md)

### SOS03 · Machine jam
Glimmer grew from a synchronized jam; he praised TR-707 through tape and reverb.

- **Topic:** Drums
- **Context:** The Slow Rush / 2020
- **Evidence:** first-hand · [Sound On Sound: The Psychedelic World of Kevin Parker](https://www.soundonsound.com/people/tame-impala) · Current Events
- **Gear context:** Roland TR-707
[Source record](sources/external/s04.md)

### EXP05-02 · Discover sections by looping
He developed Let It Happen through solitary looped jams, allowing new elements to suggest the next section.

- **Topic:** Writing
- **Context:** Currents
- **Evidence:** first-hand · [Under the Radar: Cover Story Bonus Q&A](https://www.undertheradarmag.com/interviews/tame_impala_cover_story_bonus_2015/) · Q: Do you remember your first idea for that track?
- **Gear context:** No specific model established
[Source record](sources/external/exp05.md)

### EXP08-01 · Make repetition disturb expectations
Let It Happen’s intentional skipping passage was designed to make listeners briefly suspect a playback fault. No editing command or plugin identified.

- **Topic:** Writing
- **Context:** Currents
- **Evidence:** first-hand · [Rolling Stone: Mind Tricks and Currents](https://au.rollingstone.com/music/music-news/tame-impalas-mind-tricks-kevin-parker-on-sense-altering-currents-672/) · Q: The single Let It Happen has this digital skip
- **Gear context:** No specific model established
[Source record](sources/external/exp08.md)

### EXP09-03 · Hear rhythm across the arrangement
He treats the interaction of vocal, bass and percussion rhythms as central to the music.

- **Topic:** Drums
- **Context:** Rhythmic approach described in 2020
- **Evidence:** first-hand · [Zane Lowe: The Slow Rush interview](https://www.youtube.com/watch?v=Kr28pGJZ3nY) · 21:34–22:01
- **Gear context:** No specific model established
[Source record](sources/external/exp09.md)

### BR20-01 · Build structure from a short loop
For Currents, he built structures from short loops, influenced by hip-hop, R&B and electronic production.

- **Topic:** Writing
- **Context:** Currents, recalled 2020
- **Evidence:** first-hand · [Broken Record: Tame Impala with Rick Rubin](https://www.pushkin.fm/podcasts/broken-record/tame-impala) · Comparison of second and third album arrangements
- **Gear context:** No specific model established
[Source record](sources/external/br20.md)

### RS05 · Respond to the recorded drummer
Recording bass over his own drums lets him anticipate and match the fills, creating interaction between separately performed parts.

- **Topic:** Bass
- **Context:** InnerSpeaker / 2011
- **Evidence:** first-hand · [Rocksucker interview](https://rocksucker.co.uk/2011/06/interview-tame-impala.html) · Question about imagining a band while recording alone
- **Gear context:** No specific model established
[Source record](sources/external/s08.md)

### MW1-08 · Reinforce the acoustic loop
An 808 kick and Sequential Circuits Drumtraks were added later to the original drum recording.

- **Topic:** Drums
- **Context:** Currents / The Less I Know the Better
- **Evidence:** first-hand · [Mix With The Masters, part 1: Demo and guitar synth](https://mixwiththemasters.com/videos/kevin-parker-tame-impala-the-less-i-know-the-better) · 08:31–08:52
- **Gear context:** Roland TR-808, Sequential Circuits Drumtraks
[Source record](sources/mix-with-the-masters/mw1.md)

### MW2-08 · Editing is part of the performance
He layers drum-machine reinforcement and trims the loop, then questions its exact length. No exact universal bar count is established.

- **Topic:** Drums
- **Context:** Currents / The Less I Know the Better
- **Evidence:** qualified-recollection · [Mix With The Masters, part 2: Drums and groove](https://mixwiththemasters.com/videos/kevin-parker-tame-impala-the-less-i-know-the-better) · 05:03–06:27
- **Gear context:** No specific model established
[Source record](sources/mix-with-the-masters/mw2.md)

### MW2-10 · Hi-hat placement gives the loop feel
He describes hi-hats sitting slightly behind the beat. No millisecond offset or swing percentage is supplied.

- **Topic:** Drums
- **Context:** Currents / The Less I Know the Better
- **Evidence:** first-hand · [Mix With The Masters, part 2: Drums and groove](https://mixwiththemasters.com/videos/kevin-parker-tame-impala-the-less-i-know-the-better) · 07:10–08:05
- **Gear context:** No specific model established
[Source record](sources/mix-with-the-masters/mw2.md)

### TN188-05 · Make the repeating bar convincing
He describes electronic grooves as a challenge of making a short repeating pattern danceable, with tiny percussion placements and gradual changes maintaining movement.

- **Topic:** Drums
- **Context:** Deadbeat / My Old Ways, Loser and related songs
- **Evidence:** first-hand · [Tape Notes 188: Tame Impala — My Old Ways and Loser](https://podcasts.apple.com/us/podcast/tn-188-tame-impala/id1249834293?i=1000787528506) · 19:54–22:24
- **Gear context:** No specific model established
[Source record](sources/tape-notes/tn188.md)

### TN188-06 · Do not import every acoustic habit
Electronic beats need not inherit a drummer’s automatic continuous eighth-note hi-hat pattern; he deliberately questions those habits.

- **Topic:** Drums
- **Context:** Deadbeat / My Old Ways, Loser and related songs
- **Evidence:** first-hand · [Tape Notes 188: Tame Impala — My Old Ways and Loser](https://podcasts.apple.com/us/podcast/tn-188-tame-impala/id1249834293?i=1000787528506) · 22:58–24:02
- **Gear context:** No specific model established
[Source record](sources/tape-notes/tn188.md)

### YT3-01 · Give the groove an offbeat pulse
In My Old Ways, he identifies offbeat cabasa and another cabasa part within the electronic beat. The caption gives the song as 110 BPM; no swing amount or timing offset is specified.

- **Topic:** Drums
- **Context:** Deadbeat / My Old Ways
- **Evidence:** first-hand · [Drum Production on Deadbeat (member edit)](https://www.youtube.com/watch?v=nwqOT7jwt4A) · 05:47–06:26
- **Gear context:** Cabasa
[Source record](sources/tape-notes/yt3.md)

### MW2-09 · Layering kicks changes phase and feel
Aligning the added kick with the original drum recording proved troublesome; the discussion concerns timing and phase rather than a fixed recipe.

- **Topic:** Drums
- **Context:** Currents / The Less I Know the Better
- **Evidence:** first-hand · [Mix With The Masters, part 2: Drums and groove](https://mixwiththemasters.com/videos/kevin-parker-tame-impala-the-less-i-know-the-better) · 06:27–07:10
- **Gear context:** No specific model established
[Source record](sources/mix-with-the-masters/mw2.md)

### MW2-11 · Judge the interacting envelopes
Kick and snare interaction is fundamental to the groove; detailed editing is a musical skill, and reproducing that recorded feel live remained difficult.

- **Topic:** Drums
- **Context:** Currents / The Less I Know the Better
- **Evidence:** first-hand · [Mix With The Masters, part 2: Drums and groove](https://mixwiththemasters.com/videos/kevin-parker-tame-impala-the-less-i-know-the-better) · 08:05–09:10
- **Gear context:** No specific model established
[Source record](sources/mix-with-the-masters/mw2.md)

<a id="sound"></a>
## Shape a sound

### SE05 · Distortion contrast
Chorus bass, drums and lead were distorted; the keyboard part provided a cleaner contrast.

- **Topic:** Mixing
- **Context:** The Slow Rush / It Might Be Time
- **Evidence:** first-hand · [Song Exploder 183: It Might Be Time](https://songexploder.net/tame-impala) · PDF p3
- **Gear context:** No specific model established
[Source record](sources/external/s02.md)

### GW02 · Modeled bass
The bass used its P-Bass model, then overdrive, filtering and something he recalls as chorus.

- **Topic:** Bass
- **Context:** Currents / The Less I Know the Better (recalled 2022)
- **Evidence:** qualified-recollection · [Guitar World interview](https://www.guitarworld.com/features/tame-impala-kevin-parker) · The Less I Know the Better recording question
- **Gear context:** Roland GR-55, P-Bass model
[Source record](sources/external/s03.md)

### SOS06 · Destructive vocal EQ
One experiment boosted 8 kHz before compression, then repaired the result afterward for an aged-sample character.

- **Topic:** Vocals
- **Context:** The Slow Rush / 2020
- **Evidence:** first-hand · [Sound On Sound: The Psychedelic World of Kevin Parker](https://www.soundonsound.com/people/tame-impala) · Vocal Sound
- **Gear context:** No specific model established
[Source record](sources/external/s04.md)

### PG01 · Shared pedal chain
He described his Hofner bass feeding his guitar pedal chain, initially because he lacked separate boards.

- **Topic:** Bass
- **Context:** Currents / 2015
- **Evidence:** first-hand · [Premier Guitar: Psych Wunderkind Kevin Parker](https://www.premierguitar.com/artists/guitarists/tame-impala-psych-wunderkind-kevin-parker) · Bass-tone answer before What's on your pedalboard?
- **Gear context:** Hofner bass
[Source record](sources/external/s05.md)

### RS01 · Looser strings
He lowered all the strings for a looser feel; no exact interval was specified.

- **Topic:** Guitar
- **Context:** InnerSpeaker / 2011
- **Evidence:** first-hand · [Rocksucker interview](https://rocksucker.co.uk/2011/06/interview-tame-impala.html) · Alternative tunings and effects pedals?
- **Gear context:** No specific model established
[Source record](sources/external/s08.md)

### EXP07-01 · Make guitar suggest an organ
He reduced the attack, rolled back the tone control and used fingers instead of a pick for organ-like guitar parts.

- **Topic:** Guitar
- **Context:** Innerspeaker-era guitar, recalled in 2021
- **Evidence:** first-hand · [Guitar.com: Ten years of InnerSpeaker](https://guitar.com/features/interviews/tame-impala-kevin-parker-10-years-innerspeaker/) · Tools at hand
- **Gear context:** No specific model established
[Source record](sources/external/exp07.md)

### EXP07-02 · Explore recorder parameters by ear
The synthetic space-guitar sound emerged from trying recorder presets and changing parameters until a sound appealed. No exact preset or parameter values supplied.

- **Topic:** Guitar
- **Context:** Early recordings, recalled in 2021
- **Evidence:** first-hand · [Guitar.com: Ten years of InnerSpeaker](https://guitar.com/features/interviews/tame-impala-kevin-parker-10-years-innerspeaker/) · Tools at hand
- **Gear context:** No specific model established
[Source record](sources/external/exp07.md)

### EXP07-04 · Change the register and articulation
He describes playing funk figures on a cheap Teisco’s upper three strings for a distinctive recorded character.

- **Topic:** Guitar
- **Context:** Studio practice described in 2021
- **Evidence:** first-hand · [Guitar.com: Ten years of InnerSpeaker](https://guitar.com/features/interviews/tame-impala-kevin-parker-10-years-innerspeaker/) · Bet on Backer
- **Gear context:** Teisco (model unspecified)
[Source record](sources/external/exp07.md)

### ZL25-05 · Use an amp vocal for a spontaneous performance feel
For Not My World’s spontaneous feel, he sang through a guitar amp. Neither microphone nor amp model is specified.

- **Topic:** Vocals
- **Context:** Deadbeat / Not My World
- **Evidence:** first-hand · [Tame Impala: The Deadbeat Interview | Zane Lowe Interview](https://www.youtube.com/watch?v=wXwcPtVrx7g) · 32:58–34:02
- **Gear context:** Microphone (model unspecified), Guitar amplifier (model unspecified)
[Source record](sources/external/zl25.md)

### GW09 · Use guitar voicings on keyboard sounds
Playing a piano patch through guitar synthesis gives familiar guitar chords different voicings from conventional keyboard playing.

- **Topic:** Synths
- **Context:** Writing practice described in 2022
- **Evidence:** first-hand · [Guitar World interview](https://www.guitarworld.com/features/tame-impala-kevin-parker) · The Less I Know the Better answer, paragraph beginning Like, you can play a barre chord
- **Gear context:** Roland GR-55
[Source record](sources/external/s03.md)

### PG07 · Build patches beyond the presets
He built GR-55 patches from scratch, then combined them with effects and outboard processing.

- **Topic:** Synths
- **Context:** Currents / 2015
- **Evidence:** first-hand · [Premier Guitar: Psych Wunderkind Kevin Parker](https://www.premierguitar.com/artists/guitarists/tame-impala-psych-wunderkind-kevin-parker) · Jazzmaster with Roland synth pickup question
- **Gear context:** Roland GR-55
[Source record](sources/external/s05.md)

### MW1-04 · The famous bass begins as guitar
The riff uses a modeled P-bass sound played on guitar and shifted into the bass register, then processed. This is not proof that the entire song contains no bass guitar.

- **Topic:** Bass
- **Context:** Currents / The Less I Know the Better
- **Evidence:** first-hand · [Mix With The Masters, part 1: Demo and guitar synth](https://mixwiththemasters.com/videos/kevin-parker-tame-impala-the-less-i-know-the-better) · 03:41–05:36
- **Gear context:** Roland GR-55
[Source record](sources/mix-with-the-masters/mw1.md)

### TN188-04 · A smaller electronic drum palette
The Deadbeat foundation combines an 808 through a guitar amp with a Vermona DRM1, synchronized and recorded in different ways. No amp model or fixed settings are given.

- **Topic:** Drums
- **Context:** Deadbeat / My Old Ways, Loser and related songs
- **Evidence:** first-hand · [Tape Notes 188: Tame Impala — My Old Ways and Loser](https://podcasts.apple.com/us/podcast/tn-188-tame-impala/id1249834293?i=1000787528506) · 16:37–19:14
- **Gear context:** Roland TR-808, Vermona DRM1, guitar amplifier (model unspecified)
[Source record](sources/tape-notes/tn188.md)

### TN188-10 · Amp treatment appears on Deadbeat
He describes routing vocals through guitar amplification, sometimes singing into a microphone connected to the amp; End of Summer is his example. The surrounding SM57/SM7 correction makes its exact microphone uncertain.

- **Topic:** Vocals
- **Context:** Deadbeat / My Old Ways, Loser and related songs
- **Evidence:** qualified-recollection · [Tape Notes 188: Tame Impala — My Old Ways and Loser](https://podcasts.apple.com/us/podcast/tn-188-tame-impala/id1249834293?i=1000787528506) · 34:35–35:03
- **Gear context:** guitar amplifier (model unspecified)
[Source record](sources/tape-notes/tn188.md)

### SE03 · Inspiring drums
Even exploratory drums need an inspiring sound for him to continue writing.

- **Topic:** Drums
- **Context:** The Slow Rush / It Might Be Time
- **Evidence:** first-hand · [Song Exploder 183: It Might Be Time](https://songexploder.net/tame-impala) · PDF p2
- **Gear context:** No specific model established
[Source record](sources/external/s02.md)

### GW07 · Flexible pedal order
He still used the Blues Driver and Holy Grail, but rejected a universal rule that distortion belongs last.

- **Topic:** Guitar
- **Context:** 2022 interview
- **Evidence:** first-hand · [Guitar World interview](https://www.guitarworld.com/features/tame-impala-kevin-parker) · Pedalboard; drive at end?
- **Gear context:** Boss Blues Driver, Electro-Harmonix Holy Grail
[Source record](sources/external/s03.md)

### AM01 · Available overdrive
He said he generally avoided the dbx 165's Peakstop stage and used available overdrive, including Ableton's standard Overdrive.

- **Topic:** Drums
- **Context:** Pre-release Currents / 2015
- **Evidence:** first-hand · [Kevin Parker Reddit AMA](https://www.reddit.com/r/IAmA/comments/34clpm/i_am_kevin_parker_from_tame_impala_ask_me_anything/) · https://www.reddit.com/r/IAmA/comments/34clpm/comment/cqtk6uf/
- **Gear context:** dbx 165, Ableton Overdrive
[Source record](sources/external/s07.md)

### AM02 · Preamp crunch
He used a pair of Neve 1073s for mixing and valued their crunch.

- **Topic:** Mixing
- **Context:** Pre-release Currents / 2015
- **Evidence:** first-hand · [Kevin Parker Reddit AMA](https://www.reddit.com/r/IAmA/comments/34clpm/i_am_kevin_parker_from_tame_impala_ask_me_anything/) · https://www.reddit.com/r/IAmA/comments/34clpm/comment/cqtk6uf/
- **Gear context:** Neve 1073
[Source record](sources/external/s07.md)

### EXP01-02 · Compose with the sound
For Parker, production choices carry emotional meaning and develop alongside songwriting.

- **Topic:** Writing
- **Context:** Currents
- **Evidence:** first-hand · [Electronic Beats: Kevin Parker Reflects on Pop Success](https://www.electronicbeats.net/tame-impalas-kevin-parker-reflects-on-pop-success/) · Q: Would you consider production to be surface or content?
- **Gear context:** No specific model established
[Source record](sources/external/exp01.md)

### EXP08-02 · Use an imagined playback aesthetic
Disciples pursued a seventies AM-radio character as its own sound world.

- **Topic:** Writing
- **Context:** Currents
- **Evidence:** first-hand · [Rolling Stone: Mind Tricks and Currents](https://au.rollingstone.com/music/music-news/tame-impalas-mind-tricks-kevin-parker-on-sense-altering-currents-672/) · Q: The album moves around a lot; Disciples
- **Gear context:** No specific model established
[Source record](sources/external/exp08.md)

### MW1-03 · Guitar controller opens unfamiliar sounds
The opening instrumental demo used a Strat with a taped-on synth pickup and a Roland guitar synthesizer; he tentatively recalls the GR-55 model.

- **Topic:** Guitar
- **Context:** Currents / The Less I Know the Better
- **Evidence:** qualified-recollection · [Mix With The Masters, part 1: Demo and guitar synth](https://mixwiththemasters.com/videos/kevin-parker-tame-impala-the-less-i-know-the-better) · 03:23–05:36
- **Gear context:** Fender Stratocaster, Roland GR-55
[Source record](sources/mix-with-the-masters/mw1.md)

### TN188-16 · Decapitator adds occasional grit
He names Decapitator on vocals for songs including Dracula. He does not provide a mode, drive value or mix setting.

- **Topic:** Vocals
- **Context:** Deadbeat / My Old Ways, Loser and related songs
- **Evidence:** first-hand · [Tape Notes 188: Tame Impala — My Old Ways and Loser](https://podcasts.apple.com/us/podcast/tn-188-tame-impala/id1249834293?i=1000787528506) · 41:13–41:31
- **Gear context:** Soundtoys Decapitator
[Source record](sources/tape-notes/tn188.md)

### GW01 · Guitar synthesis
Its opening instrumental sounds came from a Roland GR-55 guitar synthesizer.

- **Topic:** Synths
- **Context:** Currents / The Less I Know the Better (recalled 2022)
- **Evidence:** first-hand · [Guitar World interview](https://www.guitarworld.com/features/tame-impala-kevin-parker) · Question beginning On The Less I Know The Better
- **Gear context:** Roland GR-55
[Source record](sources/external/s03.md)

### SOS02 · Evocative digital synths
Roland D-50 and JV-1080 sounds appealed through childhood pop-radio associations.

- **Topic:** Synths
- **Context:** Currents / 2015 (reported 2020)
- **Evidence:** publisher-report · [Sound On Sound: The Psychedelic World of Kevin Parker](https://www.soundonsound.com/people/tame-impala) · Current Events
- **Gear context:** Roland D-50, Roland JV-1080
[Source record](sources/external/s04.md)

### SOS04 · Characterful bass
He highlighted the SH-1's personality and suitability for unconventional bass use.

- **Topic:** Synths
- **Context:** The Slow Rush / 2020
- **Evidence:** first-hand · [Sound On Sound: The Psychedelic World of Kevin Parker](https://www.soundonsound.com/people/tame-impala) · Current Events
- **Gear context:** Roland SH-1
[Source record](sources/external/s04.md)

### PG03 · Rack preamp
He described running instruments through a Seymour Duncan rack preamp; the publisher supplies the KTG-1 model in brackets.

- **Topic:** Workflow
- **Context:** Currents / 2015
- **Evidence:** publisher-report · [Premier Guitar: Psych Wunderkind Kevin Parker](https://www.premierguitar.com/artists/guitarists/tame-impala-psych-wunderkind-kevin-parker) · What’s on your pedalboard?
- **Gear context:** Seymour Duncan KTG-1
[Source record](sources/external/s05.md)

### PG05 · Hidden guitar parts
He confirmed more guitar parts were present than listeners sometimes recognized.

- **Topic:** Guitar
- **Context:** Currents / 2015
- **Evidence:** first-hand · [Premier Guitar: Psych Wunderkind Kevin Parker](https://www.premierguitar.com/artists/guitarists/tame-impala-psych-wunderkind-kevin-parker) · More guitar on the record?
- **Gear context:** No specific model established
[Source record](sources/external/s05.md)

### MW1-05 · Overdrive recollection is tentative
He thinks Ableton Overdrive shaped the synthesized bass and demonstrates something similar; the original exact preset and stereo treatment are not recovered.

- **Topic:** Bass
- **Context:** Currents / The Less I Know the Better
- **Evidence:** qualified-recollection · [Mix With The Masters, part 1: Demo and guitar synth](https://mixwiththemasters.com/videos/kevin-parker-tame-impala-the-less-i-know-the-better) · 05:36–06:40
- **Gear context:** Ableton Overdrive
[Source record](sources/mix-with-the-masters/mw1.md)

### MW1-10 · Preserve the Greco correction
For a later bass part he first says Hofner, then corrects himself to Greco. Do not turn the initial slip into a definitive Hofner attribution.

- **Topic:** Bass
- **Context:** Currents / The Less I Know the Better
- **Evidence:** first-hand · [Mix With The Masters, part 1: Demo and guitar synth](https://mixwiththemasters.com/videos/kevin-parker-tame-impala-the-less-i-know-the-better) · 10:11–10:30
- **Gear context:** Greco bass
[Source record](sources/mix-with-the-masters/mw1.md)

### MW2-06 · Do not invent the distortion stage
Asked about distortion following the compressor, he is uncertain. The available discussion does not establish a fixed distortion chain.

- **Topic:** Drums
- **Context:** Currents / The Less I Know the Better
- **Evidence:** qualified-recollection · [Mix With The Masters, part 2: Drums and groove](https://mixwiththemasters.com/videos/kevin-parker-tame-impala-the-less-i-know-the-better) · 04:26–04:48
- **Gear context:** dbx 165
[Source record](sources/mix-with-the-masters/mw2.md)

### MW4-01 · Kronos supplies the later section
He identifies Korg Kronos as the main keyboard for the section after roughly the first minute and says it became a recurring instrument from Currents onward.

- **Topic:** Synths
- **Context:** Currents / The Less I Know the Better
- **Evidence:** first-hand · [Mix With The Masters, part 4: Keyboards and arrangement](https://mixwiththemasters.com/videos/kevin-parker-tame-impala-the-less-i-know-the-better) · 00:03–00:57
- **Gear context:** Korg Kronos
[Source record](sources/mix-with-the-masters/mw4.md)

### MW4-02 · Keep the JV-1080 uncertainty
He mentions a Roland JV-1080 or similar module but does not confidently identify every part; he thinks the Rhodes-style sound was probably Kronos.

- **Topic:** Synths
- **Context:** Currents / The Less I Know the Better
- **Evidence:** qualified-recollection · [Mix With The Masters, part 4: Keyboards and arrangement](https://mixwiththemasters.com/videos/kevin-parker-tame-impala-the-less-i-know-the-better) · 00:57–01:43
- **Gear context:** Roland JV-1080, Korg Kronos
[Source record](sources/mix-with-the-masters/mw4.md)

<a id="space"></a>
## Create space

### PG02 · Bass ambience
That chain included compression, vibrato and reverb; he liked reverb on bass.

- **Topic:** Bass
- **Context:** Currents / 2015
- **Evidence:** first-hand · [Premier Guitar: Psych Wunderkind Kevin Parker](https://www.premierguitar.com/artists/guitarists/tame-impala-psych-wunderkind-kevin-parker) · What's on your pedalboard?
- **Gear context:** No specific model established
[Source record](sources/external/s05.md)

### AM03 · Reverb before drive
Reversing a conventional pedal order and putting reverb first were experiments he enjoyed for distorted spatial effects.

- **Topic:** Guitar
- **Context:** Pre-release Currents / 2015
- **Evidence:** first-hand · [Kevin Parker Reddit AMA](https://www.reddit.com/r/IAmA/comments/34clpm/i_am_kevin_parker_from_tame_impala_ask_me_anything/) · https://www.reddit.com/r/IAmA/comments/34clpm/comment/cqte5yx/
- **Gear context:** No specific model established
[Source record](sources/external/s07.md)

### RS02 · Distorted ambience
Reverb before distortion changes the apparent acoustic space, rather than merely adding ambience after an overdriven guitar.

- **Topic:** Guitar
- **Context:** InnerSpeaker / 2011
- **Evidence:** first-hand · [Rocksucker interview](https://rocksucker.co.uk/2011/06/interview-tame-impala.html) · Alternative tunings and effects pedals?
- **Gear context:** No specific model established
[Source record](sources/external/s08.md)

### AM07 · Repeat the reverberant space
He suggests delaying an already reverberant signal because repeating its spatial reflections can alter the listener’s sense of space. A suggested preference, not a verified song-specific chain.

- **Topic:** Mixing
- **Context:** Effects preference described in 2015
- **Evidence:** first-hand · [Kevin Parker Reddit AMA](https://www.reddit.com/r/IAmA/comments/34clpm/i_am_kevin_parker_from_tame_impala_ask_me_anything/) · https://www.reddit.com/r/IAmA/comments/34clpm/comment/cqthdc5/
- **Gear context:** No specific model established
[Source record](sources/external/s07.md)

### MW3-06 · Automate the throws
Delay and reverb throws supplied much of the vocal movement; his retrospective criticism is that the vocals were too low and reverberant.

- **Topic:** Vocals
- **Context:** Currents / The Less I Know the Better
- **Evidence:** first-hand · [Mix With The Masters, part 3: Vocals and effects](https://mixwiththemasters.com/videos/kevin-parker-tame-impala-the-less-i-know-the-better) · 02:23–03:20
- **Gear context:** No specific model established
[Source record](sources/mix-with-the-masters/mw3.md)

### MW3-08 · Tight doubles still contain difference
Similar rhythmic phrasing with small natural pitch differences creates the vocal shimmer. No detuning amount or artificial delay setting is given.

- **Topic:** Vocals
- **Context:** Currents / The Less I Know the Better
- **Evidence:** first-hand · [Mix With The Masters, part 3: Vocals and effects](https://mixwiththemasters.com/videos/kevin-parker-tame-impala-the-less-i-know-the-better) · 03:56–05:20
- **Gear context:** No specific model established
[Source record](sources/mix-with-the-masters/mw3.md)

### TN188-13 · Whisper takes add width
Two more whispery takes sit hard left and right around the more central vocal double. The side layers are filtered and heavily compressed; exact cutoffs and ratios are unstated.

- **Topic:** Vocals
- **Context:** Deadbeat / My Old Ways, Loser and related songs
- **Evidence:** first-hand · [Tape Notes 188: Tame Impala — My Old Ways and Loser](https://podcasts.apple.com/us/podcast/tn-188-tame-impala/id1249834293?i=1000787528506) · 38:14–39:52
- **Gear context:** No specific model established
[Source record](sources/tape-notes/tn188.md)

### TN188-14 · Separate vocal effects bus
He describes a separate effects bus on Deadbeat and names Soundtoys EchoBoy for its stereo character and Valhalla Room among the vocal effects.

- **Topic:** Vocals
- **Context:** Deadbeat / My Old Ways, Loser and related songs
- **Evidence:** first-hand · [Tape Notes 188: Tame Impala — My Old Ways and Loser](https://podcasts.apple.com/us/podcast/tn-188-tame-impala/id1249834293?i=1000787528506) · 39:54–40:55
- **Gear context:** Soundtoys EchoBoy, Valhalla Room
[Source record](sources/tape-notes/tn188.md)

### YT2-01 · Build a choir through successive takes
He builds a cascading vocal stack by recording harmony parts successively and listening to their combined choral effect. His early eight-track recollection illustrates the practice; it does not establish a required track count or current microphone.

- **Topic:** Vocals
- **Context:** Deadbeat vocal discussion / earlier eight-track practice
- **Evidence:** first-hand · [Vocal Chain, Layering & Vocal Production Techniques](https://www.youtube.com/watch?v=1WMxwm3Tu70) · 07:36–09:36
- **Gear context:** No specific model established
[Source record](sources/tape-notes/yt2.md)

### KX01 · Forward vocals
More prominent vocals reflected growing confidence in his singing and melodies; earlier reverb and delay partly concealed shyness.

- **Topic:** Vocals
- **Context:** Currents / 2015
- **Evidence:** first-hand · [KEXP interview about Currents](https://www.kexp.org/read/2015/7/8/interview-tame-impalas-kevin-parker-on-his-personal-danceable-new-album-currents/) · Were the vocals approached differently?
- **Gear context:** No specific model established
[Source record](sources/external/s06.md)

### MW3-03 · Doubles without assumed harmonies
Parker recalls double-tracked vocals and thinks there were no harmonies on the part under discussion.

- **Topic:** Vocals
- **Context:** Currents / The Less I Know the Better
- **Evidence:** qualified-recollection · [Mix With The Masters, part 3: Vocals and effects](https://mixwiththemasters.com/videos/kevin-parker-tame-impala-the-less-i-know-the-better) · 00:55–01:30
- **Gear context:** No specific model established
[Source record](sources/mix-with-the-masters/mw3.md)

### TN188-15 · Spring reverb device name needs care
He describes an Ableton convolution spring reverb used on most tracks, correcting his own initial spring-echo wording. The exact device version or impulse response is not established.

- **Topic:** Vocals
- **Context:** Deadbeat / My Old Ways, Loser and related songs
- **Evidence:** first-hand · [Tape Notes 188: Tame Impala — My Old Ways and Loser](https://podcasts.apple.com/us/podcast/tn-188-tame-impala/id1249834293?i=1000787528506) · 40:49–41:07
- **Gear context:** Ableton convolution spring reverb (exact device unspecified)
[Source record](sources/tape-notes/tn188.md)

### AM05 · Favourite pedals
He named Holy Grail reverb as a favourite and praised an unnamed purple vibrato.

- **Topic:** Guitar
- **Context:** Pre-release Currents / 2015
- **Evidence:** first-hand · [Kevin Parker Reddit AMA](https://www.reddit.com/r/IAmA/comments/34clpm/i_am_kevin_parker_from_tame_impala_ask_me_anything/) · Favourite pedal question
- **Gear context:** Electro-Harmonix Holy Grail
[Source record](sources/external/s07.md)

### MW3-04 · Old delay naming is uncertain
He cycles through Ableton delay names while remembering an old session. Do not claim the modern Echo device was used on a 2015 recording from this recollection alone.

- **Topic:** Vocals
- **Context:** Currents / The Less I Know the Better
- **Evidence:** qualified-recollection · [Mix With The Masters, part 3: Vocals and effects](https://mixwiththemasters.com/videos/kevin-parker-tame-impala-the-less-i-know-the-better) · 01:30–01:54
- **Gear context:** Ableton delay (exact device uncertain)
[Source record](sources/mix-with-the-masters/mw3.md)

### MW3-05 · Likely reverb and dynamics
He tentatively identifies Waves RVerb, possibly Ableton Compressor, and Ableton multiband processing. Exact settings are not supplied.

- **Topic:** Vocals
- **Context:** Currents / The Less I Know the Better
- **Evidence:** qualified-recollection · [Mix With The Masters, part 3: Vocals and effects](https://mixwiththemasters.com/videos/kevin-parker-tame-impala-the-less-i-know-the-better) · 01:54–02:23
- **Gear context:** Waves RVerb, Ableton Compressor, Ableton Multiband Dynamics
[Source record](sources/mix-with-the-masters/mw3.md)

<a id="dynamics"></a>
## Control dynamics

### TO02 · Compression timing
High ratio and low threshold brought the whole kit into that microphone; he supplemented it with kick.

- **Topic:** Drums
- **Context:** InnerSpeaker / 2010
- **Evidence:** first-hand · [Tape Op: Tame Impala: Aussie Psyche Explosion](https://tapeop.com/interviews/95/tame-impala) · What did you end up doing for the drums?
- **Gear context:** No specific model established
[Source record](sources/external/s01.md)

### TN188-11 · Track through the familiar compressor
He now records vocals through his old dbx 165, previously used on early-album drums, and may add further compression and EQ in the session.

- **Topic:** Vocals
- **Context:** Deadbeat / My Old Ways, Loser and related songs
- **Evidence:** first-hand · [Tape Notes 188: Tame Impala — My Old Ways and Loser](https://podcasts.apple.com/us/podcast/tn-188-tame-impala/id1249834293?i=1000787528506) · 36:17–37:00
- **Gear context:** dbx 165
[Source record](sources/tape-notes/tn188.md)

### TO08 · Early limiting
The BR-864's automatic limiting created crunch; one flattened mix left mastering little headroom.

- **Topic:** Mixing
- **Context:** Early EP / 2008
- **Evidence:** first-hand · [Tape Op: Tame Impala: Aussie Psyche Explosion](https://tapeop.com/interviews/95/tame-impala) · How did the first Tame Impala EP come to be?
- **Gear context:** Boss BR-864
[Source record](sources/external/s01.md)

### SOS09 · Simpler bus processing
He shifted toward a limiter without EQ, with occasional SSL G Bus processing.

- **Topic:** Mixing
- **Context:** The Slow Rush / 2020
- **Evidence:** first-hand · [Sound On Sound: The Psychedelic World of Kevin Parker](https://www.soundonsound.com/people/tame-impala) · Mixing
- **Gear context:** SSL G Bus
[Source record](sources/external/s04.md)

### MW2-05 · Compression supplies the knock
The dbx 165 was central to his drum character across several albums. Its envelope mattered; a single owned unit encouraged mono processing.

- **Topic:** Drums
- **Context:** Currents / The Less I Know the Better
- **Evidence:** first-hand · [Mix With The Masters, part 2: Drums and groove](https://mixwiththemasters.com/videos/kevin-parker-tame-impala-the-less-i-know-the-better) · 03:03–04:26
- **Gear context:** dbx 165
[Source record](sources/mix-with-the-masters/mw2.md)

### MW5-02 · Distinguish summing from stereo processing
After abandoning multichannel summing, he recalls a stereo route through SPL Vitalizer, then paired Neve 1073 stages, with possible SSL compression before returning to Ableton for limiting. The compressor identification remains unresolved.

- **Topic:** Mixing
- **Context:** Currents / The Less I Know the Better
- **Evidence:** qualified-recollection · [Mix With The Masters, part 5: Mix bus and monitoring](https://mixwiththemasters.com/videos/kevin-parker-tame-impala-the-less-i-know-the-better) · 02:10–03:22
- **Gear context:** SPL Vitalizer, Neve 1073, Ableton limiter (exact device unspecified)
[Source record](sources/mix-with-the-masters/mw5.md)

### TN188-20 · What Fridmann demonstrated
He identifies saturation, compression that retains dynamics, and reverb that does not wash out the mix as lessons from working with Dave Fridmann as mixer. No exact settings are supplied.

- **Topic:** Mixing
- **Context:** Deadbeat / My Old Ways, Loser and related songs
- **Evidence:** first-hand · [Tape Notes 188: Tame Impala — My Old Ways and Loser](https://podcasts.apple.com/us/podcast/tn-188-tame-impala/id1249834293?i=1000787528506) · 51:51–53:35
- **Gear context:** No specific model established
[Source record](sources/tape-notes/tn188.md)

### SOS01 · Favoured compressor
He described the dbx 165 as his favourite compressor.

- **Topic:** Drums
- **Context:** 2020 interview
- **Evidence:** first-hand · [Sound On Sound: The Psychedelic World of Kevin Parker](https://www.soundonsound.com/people/tame-impala) · New York Times
- **Gear context:** dbx 165
[Source record](sources/external/s04.md)

### SOS08 · Disputed bus hardware
The publisher names Neve 1073 DPA, SPL Vitalizer and Manley Variable Mu; Parker later recalls possible SSL processing. The chain remains unresolved.

- **Topic:** Mixing
- **Context:** Currents / 2015 (reported 2020)
- **Evidence:** publisher-report · [Sound On Sound: The Psychedelic World of Kevin Parker](https://www.soundonsound.com/people/tame-impala) · Mixing
- **Gear context:** Neve 1073 DPA, SPL Vitalizer, Manley Variable Mu
[Source record](sources/external/s04.md)

### MW3-02 · Shure mixer belongs to the drum discussion
The beige Shure compressor-mixer is mentioned for many Currents drum sounds; that aside does not establish its use on this vocal track. Publisher tags identify SE-30.

- **Topic:** Drums
- **Context:** Currents / The Less I Know the Better
- **Evidence:** publisher-report · [Mix With The Masters, part 3: Vocals and effects](https://mixwiththemasters.com/videos/kevin-parker-tame-impala-the-less-i-know-the-better) · 00:34–00:55
- **Gear context:** Shure SE-30 (publisher identification)
[Source record](sources/mix-with-the-masters/mw3.md)

### MW5-03 · The bus compressor is unresolved
Parker tentatively recalls an SSL 500-series G compressor here. Sound On Sound separately names a Manley Variable Mu in publisher narration; these are not a verified combined serial chain.

- **Topic:** Mixing
- **Context:** Currents / The Less I Know the Better
- **Evidence:** qualified-recollection · [Mix With The Masters, part 5: Mix bus and monitoring](https://mixwiththemasters.com/videos/kevin-parker-tame-impala-the-less-i-know-the-better) · 03:07–03:22
- **Gear context:** SSL 500-series bus compressor (uncertain)
[Source record](sources/mix-with-the-masters/mw5.md)

<a id="decisions"></a>
## Choose & arrange

### SE02 · Unfamiliar timbres
An unfamiliar keyboard sound helps prevent him repeating earlier musical ideas.

- **Topic:** Synths
- **Context:** The Slow Rush / It Might Be Time
- **Evidence:** first-hand · [Song Exploder 183: It Might Be Time](https://songexploder.net/tame-impala) · PDF p2
- **Gear context:** No specific model established
[Source record](sources/external/s02.md)

### SE07 · Internalize the harmony
He internalized the chords using an eight-minute loop before finding the vocal melody.

- **Topic:** Writing
- **Context:** The Slow Rush / It Might Be Time
- **Evidence:** first-hand · [Song Exploder 183: It Might Be Time](https://songexploder.net/tame-impala) · PDF pp3–4
- **Gear context:** No specific model established
[Source record](sources/external/s02.md)

### GW05 · Explore unfamiliar shapes
Unfamiliar instruments and exploratory chord shapes can interrupt predictable playing habits.

- **Topic:** Writing
- **Context:** 2022 interview
- **Evidence:** first-hand · [Guitar World interview](https://www.guitarworld.com/features/tame-impala-kevin-parker) · Guitar as composing instrument?
- **Gear context:** No specific model established
[Source record](sources/external/s03.md)

### PG04 · Escape muscle memory
He imagines a melody, then makes his fingers reproduce it until natural rather than following familiar guitar licks.

- **Topic:** Guitar
- **Context:** Currents / 2015
- **Evidence:** first-hand · [Premier Guitar: Psych Wunderkind Kevin Parker](https://www.premierguitar.com/artists/guitarists/tame-impala-psych-wunderkind-kevin-parker) · Who influenced you as a guitarist?, second answer paragraph
- **Gear context:** No specific model established
[Source record](sources/external/s05.md)

### AM04 · Seventh chords
He recommended major and minor sevenths as an entry point for different emotional chord colours.

- **Topic:** Writing
- **Context:** Pre-release Currents / 2015
- **Evidence:** first-hand · [Kevin Parker Reddit AMA](https://www.reddit.com/r/IAmA/comments/34clpm/i_am_kevin_parker_from_tame_impala_ask_me_anything/) · Reply to airwrecka1 music-theory question
- **Gear context:** No specific model established
[Source record](sources/external/s07.md)

### RS04 · Protect the ending
He protected the album's ending by placing a bonus track inside the running order, treating neighbouring songs as a narrative.

- **Topic:** Writing
- **Context:** InnerSpeaker / 2011
- **Evidence:** first-hand · [Rocksucker interview](https://rocksucker.co.uk/2011/06/interview-tame-impala.html) · Island Walking question
- **Gear context:** No specific model established
[Source record](sources/external/s08.md)

### EXP01-01 · Contrast emotional signals
He pairs emotionally contrasting lyrics and music to create tension beyond a uniformly sad song.

- **Topic:** Writing
- **Context:** Currents
- **Evidence:** first-hand · [Electronic Beats: Kevin Parker Reflects on Pop Success](https://www.electronicbeats.net/tame-impalas-kevin-parker-reflects-on-pop-success/) · Q: Production can be such a red herring
- **Gear context:** No specific model established
[Source record](sources/external/exp01.md)

### EXP02-01 · Send an intentional rough mix
He supplied Fridmann rough mixes expressing his intended sound before the mixer rebuilt clarity and impact.

- **Topic:** Mixing
- **Context:** Lonerism
- **Evidence:** first-hand · [Stereogum: Progress Report: Tame Impala](https://stereogum.com/1115931/progress-report-tame-impala/interviews/progress-report) · Q: You worked with Dave Fridmann again
- **Gear context:** No specific model established
[Source record](sources/external/exp02.md)

### EXP04-02 · Use a collaborator to clarify intent
Sarah Aarons helped him identify what he wanted and reject distracting choices, including an overlong introduction. The intro example is illustrative, not assigned to a named song.

- **Topic:** Writing
- **Context:** Deadbeat
- **Evidence:** first-hand · [triple j: Deadbeat and simplicity](https://www.abc.net.au/triplej/news/tame-impala-interview-deadbeat-new-album-lucy-smith/105905616) · Sarah Aarons discussion, quoted 32-bar-intro example
- **Gear context:** No specific model established
[Source record](sources/external/exp04.md)

### EXP06-01 · Reach chords outside familiar fingering
He used a Casio’s chord buttons with his index fingers to discover combinations outside his habitual guitar shapes.

- **Topic:** Writing
- **Context:** Lonerism-era recollection / Orchid development
- **Evidence:** first-hand · [MusicTech: Telepathic Instruments’ Orchid](https://musictech.com/features/interviews/telepathic-instruments-orchid/) · Casio-origin paragraphs
- **Gear context:** Casio keyboard (unspecified)
[Source record](sources/external/exp06.md)

### EXP09-02 · Work from a transformed memory
He sometimes avoids replaying an influence so his imperfect memory can reshape it.

- **Topic:** Writing
- **Context:** Influence and writing practice described in 2020
- **Evidence:** first-hand · [Zane Lowe: The Slow Rush interview](https://www.youtube.com/watch?v=Kr28pGJZ3nY) · 22:03–22:48
- **Gear context:** No specific model established
[Source record](sources/external/exp09.md)

### EXP09-04 · Join contrasting fragments
Posthumous Forgiveness combined two existing ideas into sections expressing anger followed by relief.

- **Topic:** Writing
- **Context:** The Slow Rush: Posthumous Forgiveness (2020)
- **Evidence:** first-hand · [Zane Lowe: The Slow Rush interview](https://www.youtube.com/watch?v=Kr28pGJZ3nY) · 19:46–20:16
- **Gear context:** No specific model established
[Source record](sources/external/exp09.md)

### EXP09-05 · Adapt the recording for the band
Live arrangements allow players freedom instead of reproducing every edited loop and fleeting studio layer exactly.

- **Topic:** Writing
- **Context:** Live arrangement practice described in 2020
- **Evidence:** first-hand · [Zane Lowe: The Slow Rush interview](https://www.youtube.com/watch?v=Kr28pGJZ3nY) · 39:45–40:41
- **Gear context:** No specific model established
[Source record](sources/external/exp09.md)

### ZL25-03 · Audition rough ideas beside developed demos
Alternating piano phone memos with fuller demos in the car suggested My Old Ways’ intimate opening. TN188-02 identifies the released re-recording.

- **Topic:** Writing
- **Context:** Deadbeat / My Old Ways opening
- **Evidence:** first-hand · [Tame Impala: The Deadbeat Interview | Zane Lowe Interview](https://www.youtube.com/watch?v=wXwcPtVrx7g) · 14:25–15:04
- **Gear context:** iPhone voice memos, Piano
[Source record](sources/external/zl25.md)

### BR20-02 · Imagine another session’s approach
Breath Deeper’s opening beat came from imagining a Pharrell/Justin Timberlake session after watching Justified studio footage.

- **Topic:** Writing
- **Context:** The Slow Rush / Breath Deeper
- **Evidence:** first-hand · [Broken Record: Tame Impala with Rick Rubin](https://www.pushkin.fm/podcasts/broken-record/tame-impala) · Returning to solo work; Justified footage and Breath Deeper
- **Gear context:** No specific model established
[Source record](sources/external/br20.md)

### BR20-03 · Use accidental playback as an opening
An accidentally looped beat became Feels Like We Only Go Backwards’ jolting introduction.

- **Topic:** Writing
- **Context:** Lonerism / Feels Like We Only Go Backwards
- **Evidence:** first-hand · [Broken Record: Tame Impala with Rick Rubin](https://www.pushkin.fm/podcasts/broken-record/tame-impala) · Question about distinctive introductions
- **Gear context:** No specific model established
[Source record](sources/external/br20.md)

### PG06 · Arrange guitar as an answer
On Currents, guitars make intermittent appearances and answer other sounds; he adjusted chords and licks to fit the R&B rhythms and synth arrangement.

- **Topic:** Guitar
- **Context:** Currents / 2015
- **Evidence:** first-hand · [Premier Guitar: Psych Wunderkind Kevin Parker](https://www.premierguitar.com/artists/guitarists/tame-impala-psych-wunderkind-kevin-parker) · Opening two guitar-arrangement questions
- **Gear context:** No specific model established
[Source record](sources/external/s05.md)

### MW5-05 · Use another trusted listening context
A trusted mastering friend in a larger room helped check the mix, including low-frequency balance around 100 Hz. The caption does not establish a reliable second monitor model.

- **Topic:** Mixing
- **Context:** Currents / The Less I Know the Better
- **Evidence:** first-hand · [Mix With The Masters, part 5: Mix bus and monitoring](https://mixwiththemasters.com/videos/kevin-parker-tame-impala-the-less-i-know-the-better) · 03:42–04:27
- **Gear context:** No specific model established
[Source record](sources/mix-with-the-masters/mw5.md)

### TN188-03 · Reference another finished mix
He places reference audio such as Dua Lipa’s Levitating in the session to regain perspective while working alone.

- **Topic:** Mixing
- **Context:** Deadbeat / My Old Ways, Loser and related songs
- **Evidence:** first-hand · [Tape Notes 188: Tame Impala — My Old Ways and Loser](https://podcasts.apple.com/us/podcast/tn-188-tame-impala/id1249834293?i=1000787528506) · 14:41–15:33
- **Gear context:** No specific model established
[Source record](sources/tape-notes/tn188.md)

### TN188-07 · Protect a simple foundation
For My Old Ways he resisted automatically building a dense arrangement, preserving the piano riff and drums as its identity.

- **Topic:** Writing
- **Context:** Deadbeat / My Old Ways, Loser and related songs
- **Evidence:** first-hand · [Tape Notes 188: Tame Impala — My Old Ways and Loser](https://podcasts.apple.com/us/podcast/tn-188-tame-impala/id1249834293?i=1000787528506) · 24:16–26:27
- **Gear context:** No specific model established
[Source record](sources/tape-notes/tn188.md)

### TN188-08 · Make the form express the subject
The returning musical pattern and rising, increasingly chaotic synth parts support the song’s theme of falling back into old behavior.

- **Topic:** Writing
- **Context:** Deadbeat / My Old Ways, Loser and related songs
- **Evidence:** first-hand · [Tape Notes 188: Tame Impala — My Old Ways and Loser](https://podcasts.apple.com/us/podcast/tn-188-tame-impala/id1249834293?i=1000787528506) · 26:54–29:38
- **Gear context:** No specific model established
[Source record](sources/tape-notes/tn188.md)

### TN188-12 · A single hook contrasts with doubled verses
On My Old Ways he keeps the central hook single to suggest a sampled phrase, while the verses are doubled.

- **Topic:** Vocals
- **Context:** Deadbeat / My Old Ways, Loser and related songs
- **Evidence:** first-hand · [Tape Notes 188: Tame Impala — My Old Ways and Loser](https://podcasts.apple.com/us/podcast/tn-188-tame-impala/id1249834293?i=1000787528506) · 37:33–38:09
- **Gear context:** No specific model established
[Source record](sources/tape-notes/tn188.md)

### TN188-17 · A primitive lead among electronic repetition
He tentatively identifies the My Old Ways solo as Roland SH-1, valuing a meandering organ-like performance against the sequenced backdrop.

- **Topic:** Synths
- **Context:** Deadbeat / My Old Ways, Loser and related songs
- **Evidence:** qualified-recollection · [Tape Notes 188: Tame Impala — My Old Ways and Loser](https://podcasts.apple.com/us/podcast/tn-188-tame-impala/id1249834293?i=1000787528506) · 43:39–45:25
- **Gear context:** Roland SH-1
[Source record](sources/tape-notes/tn188.md)

### TN188-18 · Room sound closes the loop
The sound of getting off the piano stool at the end intentionally answers the opening arrival at the piano.

- **Topic:** Writing
- **Context:** Deadbeat / My Old Ways, Loser and related songs
- **Evidence:** first-hand · [Tape Notes 188: Tame Impala — My Old Ways and Loser](https://podcasts.apple.com/us/podcast/tn-188-tame-impala/id1249834293?i=1000787528506) · 46:45–47:01
- **Gear context:** No specific model established
[Source record](sources/tape-notes/tn188.md)

### TN188-23 · The decisive word can arrive last
Loser was the final lyric word selected, after trying alternatives against its rhythmic space; he connects an alternative word with the album title in a tentative real-time recollection.

- **Topic:** Writing
- **Context:** Deadbeat / My Old Ways, Loser and related songs
- **Evidence:** qualified-recollection · [Tape Notes 188: Tame Impala — My Old Ways and Loser](https://podcasts.apple.com/us/podcast/tn-188-tame-impala/id1249834293?i=1000787528506) · 65:00–67:20
- **Gear context:** No specific model established
[Source record](sources/tape-notes/tn188.md)

### TN188-25 · Make the experiment before rejecting it
He advises starting more songs and testing melodies instead of assuming their quality in advance.

- **Topic:** Workflow
- **Context:** Deadbeat / My Old Ways, Loser and related songs
- **Evidence:** first-hand · [Tape Notes 188: Tame Impala — My Old Ways and Loser](https://podcasts.apple.com/us/podcast/tn-188-tame-impala/id1249834293?i=1000787528506) · 76:48–77:51
- **Gear context:** No specific model established
[Source record](sources/tape-notes/tn188.md)

### YT3-02 · Give the album a recognizable drum palette
He contrasts The Slow Rush’s many drum approaches with a more consistent, identifiable Deadbeat palette, using Is This It as an example of recognizable drum identity. This is an album-level constraint, not a fixed signal chain.

- **Topic:** Drums
- **Context:** Deadbeat / contrast with The Slow Rush
- **Evidence:** first-hand · [Drum Production on Deadbeat (member edit)](https://www.youtube.com/watch?v=nwqOT7jwt4A) · 02:13–03:43
- **Gear context:** No specific model established
[Source record](sources/tape-notes/yt3.md)

### SE01 · Solo exploration
Working alone lets him explore without worrying that an unproductive session wastes somebody else's time.

- **Topic:** Workflow
- **Context:** The Slow Rush / It Might Be Time
- **Evidence:** first-hand · [Song Exploder 183: It Might Be Time](https://songexploder.net/tame-impala) · PDF p1
- **Gear context:** No specific model established
[Source record](sources/external/s02.md)

### SE08 · Reuse the spark
The verse reused chords from the original burst of ideas; unexpected chord changes or timing appealed to him.

- **Topic:** Writing
- **Context:** The Slow Rush / It Might Be Time
- **Evidence:** first-hand · [Song Exploder 183: It Might Be Time](https://songexploder.net/tame-impala) · PDF p5
- **Gear context:** No specific model established
[Source record](sources/external/s02.md)

### GW06 · Extended harmony
Sevenths and ninths attracted him emotionally before he knew their theoretical names.

- **Topic:** Writing
- **Context:** 2022 interview
- **Evidence:** first-hand · [Guitar World interview](https://www.guitarworld.com/features/tame-impala-kevin-parker) · Major 7ths question
- **Gear context:** No specific model established
[Source record](sources/external/s03.md)

### GW08 · Enjoyment sustains practice
Enjoyment sustains practice; an expensive or particular guitar is not required to develop an individual sound.

- **Topic:** Workflow
- **Context:** 2022 interview
- **Evidence:** first-hand · [Guitar World interview](https://www.guitarworld.com/features/tame-impala-kevin-parker) · Advice for bedroom producers
- **Gear context:** No specific model established
[Source record](sources/external/s03.md)

### KX03 · Distinct tracks
A goal was to keep individual tracks distinct from one another.

- **Topic:** Writing
- **Context:** Currents / 2015
- **Evidence:** first-hand · [KEXP interview about Currents](https://www.kexp.org/read/2015/7/8/interview-tame-impalas-kevin-parker-on-his-personal-danceable-new-album-currents/) · Representative of the rhythm of the album?
- **Gear context:** No specific model established
[Source record](sources/external/s06.md)

### EXP01-03 · Change the foundation
On Currents, he explored drum-machine songs and arrangements without a driving guitar riff.

- **Topic:** Writing
- **Context:** Currents
- **Evidence:** first-hand · [Electronic Beats: Kevin Parker Reflects on Pop Success](https://www.electronicbeats.net/tame-impalas-kevin-parker-reflects-on-pop-success/) · Q: Could the infrastructure veto such a move?
- **Gear context:** No specific model established
[Source record](sources/external/exp01.md)

### EXP02-02 · Develop quickly, revisit later
An initial concentrated writing session could be followed by a year of adding and removing parts.

- **Topic:** Writing
- **Context:** Lonerism
- **Evidence:** first-hand · [Stereogum: Progress Report: Tame Impala](https://stereogum.com/1115931/progress-report-tame-impala/interviews/progress-report) · Q: How does the song-making process usually work?
- **Gear context:** No specific model established
[Source record](sources/external/exp02.md)

### EXP03-01 · Write toward a performed persona
For Not My World, he wanted the impression of unpremeditated singing by someone detached from everyday reality.

- **Topic:** Vocals
- **Context:** Deadbeat
- **Evidence:** first-hand · [Coup De Main: Kevin Parker on Deadbeat](https://www.coupdemainmagazine.com/tame-impala/20202) · Q: What was running through your mind while writing Not My World?
- **Gear context:** No specific model established
[Source record](sources/external/exp03.md)

### EXP03-02 · Read back for the subject
Reading back No Reply led him to recognize anxiety as its subject.

- **Topic:** Writing
- **Context:** Deadbeat
- **Evidence:** first-hand · [Coup De Main: Kevin Parker on Deadbeat](https://www.coupdemainmagazine.com/tame-impala/20202) · No Reply discussion, preceding Q: Was it therapeutic writing that song?
- **Gear context:** No specific model established
[Source record](sources/external/exp03.md)

### EXP04-03 · Limit an abundant studio
He pursued stripped-back, sometimes distorted sounds and consciously restricted the options offered by his extensive equipment.

- **Topic:** Writing
- **Context:** Deadbeat
- **Evidence:** first-hand · [triple j: Deadbeat and simplicity](https://www.abc.net.au/triplej/news/tame-impala-interview-deadbeat-new-album-lucy-smith/105905616) · Opening sound discussion and gear-library discussion
- **Gear context:** No specific model established
[Source record](sources/external/exp04.md)

### EXP06-02 · Keep discovery in the process
He personally avoids ready-made chord packs because exploring the progression is part of his enjoyment of songwriting.

- **Topic:** Writing
- **Context:** Lonerism-era recollection / Orchid development
- **Evidence:** first-hand · [MusicTech: Telepathic Instruments’ Orchid](https://musictech.com/features/interviews/telepathic-instruments-orchid/) · Opening chord-pack discussion
- **Gear context:** No specific model established
[Source record](sources/external/exp06.md)

### EXP08-03 · Let the song determine its treatment
For Currents he asked what would help each song flourish, avoiding a predetermined Tame Impala template.

- **Topic:** Writing
- **Context:** Currents
- **Evidence:** first-hand · [Rolling Stone: Mind Tricks and Currents](https://au.rollingstone.com/music/music-news/tame-impalas-mind-tricks-kevin-parker-on-sense-altering-currents-672/) · Disciples answer, concluding paragraph
- **Gear context:** No specific model established
[Source record](sources/external/exp08.md)

### EXP09-06 · Design the closing time perspective
One More Hour represents the final hour of the year introduced by One More Year.

- **Topic:** Writing
- **Context:** The Slow Rush: One More Year / One More Hour (2020)
- **Evidence:** first-hand · [Zane Lowe: The Slow Rush interview](https://www.youtube.com/watch?v=Kr28pGJZ3nY) · 45:19–45:28
- **Gear context:** No specific model established
[Source record](sources/external/exp09.md)

### ZL25-01 · A restricted writing phase can reveal the next direction
A techno-only writing phase made Parker miss chords; following that impulse brought him back toward a Tame Impala album.

- **Topic:** Writing
- **Context:** Deadbeat / preceding techno-writing phase, recalled 2025
- **Evidence:** first-hand · [Tame Impala: The Deadbeat Interview | Zane Lowe Interview](https://www.youtube.com/watch?v=wXwcPtVrx7g) · 01:26–02:22
- **Gear context:** No specific model established
[Source record](sources/external/zl25.md)

### ZL25-02 · Improvised syllables can remain in the finished vocal
Let It Happen retains improvised, nonliteral syllables. The caption’s partial device term is uncertain; EXP05 explicitly identifies a keyboard sampler.

- **Topic:** Vocals
- **Context:** Currents / Let It Happen, recalled 2025
- **Evidence:** first-hand · [Tame Impala: The Deadbeat Interview | Zane Lowe Interview](https://www.youtube.com/watch?v=wXwcPtVrx7g) · 11:36–11:45
- **Gear context:** No specific model established
[Source record](sources/external/zl25.md)

### ZL25-06 · Recognize when further revisions risk draining a song
Piece of Heaven took days, while Dracula underwent prolonged revisions; he describes repeated editing as risking a song’s vitality.

- **Topic:** Workflow
- **Context:** Deadbeat / Piece of Heaven and Dracula
- **Evidence:** first-hand · [Tame Impala: The Deadbeat Interview | Zane Lowe Interview](https://www.youtube.com/watch?v=wXwcPtVrx7g) · 34:36–35:03
- **Gear context:** No specific model established
[Source record](sources/external/zl25.md)

### ZL25-07 · A late demo can still become a complete song
Afterthought developed from an existing demo during mastering, growing from possible interlude to full song; later mix revisions still followed.

- **Topic:** Writing
- **Context:** Deadbeat / Afterthought
- **Evidence:** first-hand · [Tame Impala: The Deadbeat Interview | Zane Lowe Interview](https://www.youtube.com/watch?v=wXwcPtVrx7g) · 36:26–38:40
- **Gear context:** No specific model established
[Source record](sources/external/zl25.md)

### ZL25-08 · Preserve collective interplay in electronic live arrangements
For the planned Deadbeat tour, he wanted collective musical interplay and spontaneity alongside quality. No live routing or synchronization method is specified.

- **Topic:** Workflow
- **Context:** Deadbeat / live-show preparation discussed in 2025
- **Evidence:** first-hand · [Tame Impala: The Deadbeat Interview | Zane Lowe Interview](https://www.youtube.com/watch?v=wXwcPtVrx7g) · 45:53–47:39
- **Gear context:** No specific model established
[Source record](sources/external/zl25.md)

### BR20-04 · Notice the transition into quiet
He notices ideas arriving when leaving busy, loud surroundings for quiet; this is an observed personal pattern.

- **Topic:** Writing
- **Context:** Writing practice described in 2020
- **Evidence:** first-hand · [Broken Record: Tame Impala with Rick Rubin](https://www.pushkin.fm/podcasts/broken-record/tame-impala) · Discussion of when song ideas arrive
- **Gear context:** No specific model established
[Source record](sources/external/br20.md)

### BR20-05 · Let memory continue an influence
He tentatively connects Backwards to mentally continuing a Beach House song after it stopped playing.

- **Topic:** Writing
- **Context:** Lonerism / retrospective account in 2020
- **Evidence:** qualified-recollection · [Broken Record: Tame Impala with Rick Rubin](https://www.pushkin.fm/podcasts/broken-record/tame-impala) · Influence discussion; Walk in the Park and Backwards
- **Gear context:** No specific model established
[Source record](sources/external/br20.md)

### BR20-06 · Keep the moment that made you care
He develops songs that have felt like his best work, then tries to retain that attachment through completion.

- **Topic:** Writing
- **Context:** Album-making practice described in 2020
- **Evidence:** first-hand · [Broken Record: Tame Impala with Rick Rubin](https://www.pushkin.fm/podcasts/broken-record/tame-impala) · Album selection and the race to finish a song
- **Gear context:** No specific model established
[Source record](sources/external/br20.md)

### BR20-07 · Change tasks while preserving orientation
He switches among playing, writing, editing and mixing, but admits this can obscure how close a song is to completion.

- **Topic:** Workflow
- **Context:** Solo workflow described in 2020
- **Evidence:** first-hand · [Broken Record: Tame Impala with Rick Rubin](https://www.pushkin.fm/podcasts/broken-record/tame-impala) · Question about finishing one song before another
- **Gear context:** No specific model established
[Source record](sources/external/br20.md)

### MW1-09 · Return later with a different palette
The later section was developed much later in another studio, using keyboards that were then available; the arrangement changes with that palette.

- **Topic:** Writing
- **Context:** Currents / The Less I Know the Better
- **Evidence:** first-hand · [Mix With The Masters, part 1: Demo and guitar synth](https://mixwiththemasters.com/videos/kevin-parker-tame-impala-the-less-i-know-the-better) · 08:52–10:10
- **Gear context:** No specific model established
[Source record](sources/mix-with-the-masters/mw1.md)

### MW4-03 · Layer without elaborate transitions
He describes the layered keyboard arrangement as relatively straightforward, with less elaborate transition processing than might be assumed.

- **Topic:** Synths
- **Context:** Currents / The Less I Know the Better
- **Evidence:** first-hand · [Mix With The Masters, part 4: Keyboards and arrangement](https://mixwiththemasters.com/videos/kevin-parker-tame-impala-the-less-i-know-the-better) · 01:43–03:40
- **Gear context:** No specific model established
[Source record](sources/mix-with-the-masters/mw4.md)

### MW4-04 · Finishing and spontaneity coexist
Completing the later section gave a beloved demo a satisfying destination. His account values both quick invention and patience in finishing.

- **Topic:** Writing
- **Context:** Currents / The Less I Know the Better
- **Evidence:** first-hand · [Mix With The Masters, part 4: Keyboards and arrangement](https://mixwiththemasters.com/videos/kevin-parker-tame-impala-the-less-i-know-the-better) · 03:40–04:30
- **Gear context:** No specific model established
[Source record](sources/mix-with-the-masters/mw4.md)

### MW5-01 · The summing experiment was abandoned
He tried two passive Folcrom summing units feeding Neve preamps, but disliked attempted clipping and could not hear a meaningful summing improvement; cabling and latency added complexity.

- **Topic:** Mixing
- **Context:** Currents / The Less I Know the Better
- **Evidence:** first-hand · [Mix With The Masters, part 5: Mix bus and monitoring](https://mixwiththemasters.com/videos/kevin-parker-tame-impala-the-less-i-know-the-better) · 00:22–02:05
- **Gear context:** Roll Music Systems Folcrom, Neve 1073
[Source record](sources/mix-with-the-masters/mw5.md)

### MW5-06 · Song structure can resist expectations
Parker discusses the unconventional chorus return and section layout. His offhand release chronology is not used here as verified historical dating.

- **Topic:** Writing
- **Context:** Currents / The Less I Know the Better
- **Evidence:** first-hand · [Mix With The Masters, part 5: Mix bus and monitoring](https://mixwiththemasters.com/videos/kevin-parker-tame-impala-the-less-i-know-the-better) · 04:27–05:30
- **Gear context:** No specific model established
[Source record](sources/mix-with-the-masters/mw5.md)

### TN188-19 · Direction matters, but audition the idea
He admires a producer’s ability to hear what a song needs to reach completion, while emphasizing that results remain unknown until tried.

- **Topic:** Workflow
- **Context:** Deadbeat / My Old Ways, Loser and related songs
- **Evidence:** first-hand · [Tape Notes 188: Tame Impala — My Old Ways and Loser](https://podcasts.apple.com/us/podcast/tn-188-tame-impala/id1249834293?i=1000787528506) · 49:49–51:35
- **Gear context:** No specific model established
[Source record](sources/tape-notes/tn188.md)

### TN188-24 · A familiar synth anchors the record
He calls Prophet-5 central to Dracula and recurring sounds across Deadbeat, stressing that it was conveniently beside him rather than uniquely necessary equipment.

- **Topic:** Synths
- **Context:** Deadbeat / My Old Ways, Loser and related songs
- **Evidence:** first-hand · [Tape Notes 188: Tame Impala — My Old Ways and Loser](https://podcasts.apple.com/us/podcast/tn-188-tame-impala/id1249834293?i=1000787528506) · 75:09–75:56
- **Gear context:** Sequential Prophet-5
[Source record](sources/tape-notes/tn188.md)

### YT4-01 · Find privacy for introspective lyrics
For personal lyrics he wants a comfortable, private setting that allows feelings to surface; he distinguishes this from the social energy of a co-writing room.

- **Topic:** Writing
- **Context:** Writing practice discussed during Deadbeat interview
- **Evidence:** first-hand · [Top 10 Production & Writing Insights (member edit)](https://www.youtube.com/watch?v=o02n6ogEvcY) · 06:18–07:14
- **Gear context:** No specific model established
[Source record](sources/tape-notes/yt4.md)

### RS03 · Mixing versus production
He distinguished Dave Fridmann's influential mixing from his own production.

- **Topic:** Mixing
- **Context:** InnerSpeaker / 2011
- **Evidence:** first-hand · [Rocksucker interview](https://rocksucker.co.uk/2011/06/interview-tame-impala.html) · Album two question
- **Gear context:** No specific model established
[Source record](sources/external/s08.md)

### ZL25-04 · Choose a writing setting that prompts ideas
He seeks writing rooms near the ocean and thinks its white noise prompts ideas; this is his personal response, not a verified mechanism.

- **Topic:** Workflow
- **Context:** Deadbeat / temporary coastal writing spaces
- **Evidence:** qualified-recollection · [Tame Impala: The Deadbeat Interview | Zane Lowe Interview](https://www.youtube.com/watch?v=wXwcPtVrx7g) · 21:01–22:47
- **Gear context:** No specific model established
[Source record](sources/external/zl25.md)

### MW1-02 · A song can outgrow its initial destination
He initially considered the idea unsuitable for Tame Impala and offered it to Mark Ronson, who encouraged him to keep it.

- **Topic:** Workflow
- **Context:** Currents / The Less I Know the Better
- **Evidence:** first-hand · [Mix With The Masters, part 1: Demo and guitar synth](https://mixwiththemasters.com/videos/kevin-parker-tame-impala-the-less-i-know-the-better) · 01:05–03:16
- **Gear context:** No specific model established
[Source record](sources/mix-with-the-masters/mw1.md)

### MW5-04 · Know the room you actually use
He describes Yamaha HS7 monitors without a subwoofer, four acoustic panels and a small bedroom. These are his working conditions, not a universal room-design prescription.

- **Topic:** Mixing
- **Context:** Currents / The Less I Know the Better
- **Evidence:** first-hand · [Mix With The Masters, part 5: Mix bus and monitoring](https://mixwiththemasters.com/videos/kevin-parker-tame-impala-the-less-i-know-the-better) · 03:22–03:42
- **Gear context:** Yamaha HS7
[Source record](sources/mix-with-the-masters/mw5.md)
