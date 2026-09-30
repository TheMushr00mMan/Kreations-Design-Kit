# Slides and presentations

Read this for any deck: PowerPoint, Keynote, Google Slides, a PDF deck, or "slides" in any tool. Everything in SKILL.md still applies (the request first, brand first, one visual world, short true copy). Deck fonts follow the no-install rule in §6. This file adds what is different about decks. Production (pptxgenjs, editing an existing .pptx, validation, rendering) belongs to the host's slides or PPTX skill; this file sets the look, structure and motion. With a shell but no such skill, use a library you can find or install (pptxgenjs, python-pptx). With no file tools, give a slide-by-slide plan (title, content, visual, notes) plus the design system and a complete script they can run; never claim a deck file exists.

## 1. First decide what kind of deck

**Deck type** (from the ask, or ask if it isn't clear):

| Type | The audience should… | Tone lean | Motion |
|---|---|---|---|
| **Client proposal / capabilities** | trust the team and say yes to a next step | Calm & premium / Practical, the client's or the user's brand | None or fade |
| **Report / update** | understand results and decide | Practical / Swiss | None or fade |
| **Pitch** (investor, sales, freelance) | remember one idea and want the next meeting | Brand tone, one bold moment | Mostly calm + 1–2 moments |
| **Talk / keynote** | follow a story from the back of a room | Any; type-led and sparse | Calm, reveal steps |
| **Portfolio / showcase** | judge a body of work | Gallery, Loud poster, Scrapbook | Livelier |
| **Brand or product launch** | feel the product and the world around it | The brand's own; Playful, Cinematic, Loud poster | Livelier |
| **Workshop / training** | do something step by step | Practical, Playful | Builds for steps |

**Presenter deck or reading deck?** It changes everything, so infer it from the ask ("for my talk" = presenter, "to send", "leave-behind", "attach to the email" = reading) or ask in one line.
- **Presenter deck:** sparse. One idea per slide, a few words, big visuals; the detail goes in the **speaker notes** (what to say, in short lines).
- **Reading deck:** more text, still structured: an action title, 2–4 short blocks, clear labels and sources. Nothing needs a speaker to make sense.
- Both at once ("present it and send it after"): build the presenter deck, put the full points in the notes, and offer a reading version or a PDF with notes.

**Professional vs creative** is set by the audience and brand, not by the topic: a client proposal for a creative agency can still be a professional deck with one creative moment.

## 2. The slide kit

Most decks draw from one kit. Use only the slides the content needs; every deck gets its own styling of them.

1. **Title**: the name or promise, huge; who and when, small.
2. **Agenda / contents**: numbered sections (only for decks of about 10+ slides).
3. **Section divider**: the deck's "moments" (see §4). A giant number or word, a full-bleed image, or a colour field.
4. **Statement**: one sentence, large. The slide equivalent of a hero line.
5. **Ideas**: 2, 3 or 4 points with a label and one line each. Not bullets in a box.
6. **Text + image**: a short claim beside a large photo or visual.
7. **Big number(s)**: one or three numbers, huge, each with a one-line label and a source.
8. **Chart**: one chart, one message, the key number highlighted (§3).
9. **Process / timeline**: 3–5 steps along a line.
10. **Quote / testimonial**: only real quotes with a name (never invented).
11. **Team / about**: real people only; photo slots when the user has photos.
12. **Case / example**: problem → what was done → result (real results only).
13. **Next step / ask**: one clear action, contact details.
14. **Closing**: the name or promise again, calm.

Keep a **slide number and a small deck label** (client, section or date) on content slides; skip them on title, dividers and closing.

## 3. Professional rules (client, report, proposal decks)

These make a deck read as serious work. Creative decks keep most of them too.
- **Action titles:** the title says the point, not the topic ("Referrals bring 60% of new clients", not "Referrals"). A reader who reads only the titles gets the story.
- **One message per slide.** If a slide needs two titles, it's two slides.
- **A steady grid:** the same margins (about 0.4–0.6" on a 10" wide slide), the same title position and the same column system on every content slide. Consistency is what reads as professional.
- **Charts say one thing:** the number that matters in the accent colour, everything else grey; direct labels instead of legends; no 3D, no gridline clutter; a source line under it.
- **Sources** on every slide with a number, small, bottom left.
- **Restrained palette:** the brand's colours, or 2–3 colours plus one accent that only marks what matters.
- **Type hierarchy:** titles about 28–40pt, body 14–18pt, labels and sources 12pt. **12pt is the minimum for everything on a slide**, sources included.
- **Honest content:** no invented clients, results, logos or quotes (SKILL.md §7). Drafts use visible `[placeholders]` and a small "Draft" label on the title slide; finals have none.
- **Professional does not mean plain.** Keep one standout per deck: a strong title slide, a colour-field divider, a big-number slide or a well-treated photo.

## 4. Creative cues from the reference decks (s01–s12)

Twelve reference decks (template-style decks from one maker, so they share a kit). **Cues only**: change colours, imagery, type and copy; never copy a layout or artwork 1:1. Favourites: **s01, s11, s03, s02**. Full entries in `examples/clips.md`.

| Cue | From | Use when |
|---|---|---|
| **Zine / analog:** grey paper, taped photos, tickets and stubs, mono type, "Ch.3 /" labels, one word in a heavier face | s01 ★ | Creative portfolios, music, events, youth or street brands, storytelling talks |
| **Hand-marker overlay:** red circles and underlines drawn over type and photos on an off-white editorial grid | s11 ★ | Fashion, portfolios, anything that wants energy with a clean base |
| **Glossy 3D objects on bright panels:** inflatable, chrome or jelly shapes, pill labels, rounded outlines | s03 ★ | Tech, product launches, playful brands, youth audiences |
| **Business kit with one neon:** black + one bright accent, hand-drawn blobs and arrows, line icons in circles | s02 ★ | Marketing plans, strategy decks that should feel alive, workshops |
| **Museum captions:** white space, hairlines, a typewriter serif, objects with leader-line labels, one accent | s04 | Premium products, craft, art, architecture; also a good calm professional base |
| **Illustrated frame:** hand-drawn florals or motifs framing each slide, a script display face | s05 | Weddings, food, kids, storybook brands. Rarely professional |
| **3D tile grid + underscore titles:** soft grey grid, glossy coloured tiles, device mockups | s06 | Tech and product decks, UX case studies |
| **Dark cinematic:** near-black, violet light shapes, thin grotesk, "/ 01" labels, big numbers | s07 | Keynotes, tech launches, film, anything that wants drama |
| **Soft-gradient tech:** white, blurred colour blobs, pixel numerals, mono caps | s08 | Trends, research and tech reports that should still feel fresh |
| **Type swap:** giant words with one letter set in a contrasting face, tiny annotations | s09 | Type-led talks, agencies, brand decks with little imagery |
| **Two-colour duotone:** every photo toned to the deck's two colours, taped corners, "//" titles | s10 | Fashion, lookbooks, bold portfolios; makes mixed photos cohesive |
| **Dark duotone + marker scribbles:** brown and electric blue photos, yellow scribbles, wide caps | s12 | Streetwear, music, nightlife, "edgy" briefs |

**Patterns across all twelve** (these are the transferable lessons):
1. **One visual world per deck**, repeated on every slide: one motif (tape, grain, blobs, tiles, light shapes, marker) and 2–4 colours with one accent.
2. **Type does the heavy lifting:** huge display words on titles and dividers, small mono or grotesk labels.
3. **Dividers are the moments:** full-bleed image, giant number or one word. Content slides stay calmer.
4. **Photos are treated to match:** a duotone or tint in the deck's colours, or consistent cut-out objects. Mixed, untreated stock photos are what make decks look cheap.
5. **Big-number slides** in almost every deck.
6. **Hand-made overlays** (marker, scribbles, blobs) add energy; use one kind, a few times.
7. **Small craft details:** chapter labels, slide numbers, "/ 01", leader-line captions.

Never copy: filler text, template instruction slides, maker credits.

## 5. Motion by context

Transitions are fine when they serve the deck. **Every deck must read perfectly with no animation** (PDF, print, Google Slides import, a viewer with motion off). Motion is a layer on top, never the only way content appears.

| Context | Transitions | Builds (items appearing) |
|---|---|---|
| **Professional** (client, report, proposal) | None, or one quiet **Fade** used on every slide | Only to reveal steps of an argument or a chart in order. Fade or Appear |
| **Pitch** | A real motion pass: one object or shape carried through the deck with **Morph** between slides, Fade elsewhere | Automatic entrance builds (after previous, short staggers) on most slides |
| **Creative / launch / portfolio** | A real motion pass: **Morph** between related slides (an object growing, moving or recolouring), **Push** or **Wipe** into dividers | Automatic, playful but purposeful: items arriving in order, a pop on a divider |
| **Talk** | Fade or none | Builds for each step, so the audience reads with the speaker |

- **Morph is the best "wow" move** that still looks professional: keep the same object on two slides (same name), change its size, position or colour, and set Morph on the second slide. Name matched objects with a leading `!!` (e.g. `!!hero`) so PowerPoint pairs them reliably.
- **Never:** spinning or flying text, bounce, "vortex", "curtains", random transitions, or a different transition on every slide. Keep durations short (about 0.4–0.8s; Morph up to about 1.2s).
- **Creative decks shouldn't be fully static;** professional decks shouldn't feel animated.
- **Tooling:** pptxgenjs can't set transitions or builds. `scripts/pptx_motion.py` in this skill adds them to a finished .pptx (Fade, Push, Wipe, Morph with a Fade fallback, plus builds by object name: on click, or automatic with `--auto 250` so items arrive by themselves, the default for pitch and creative decks). It keeps a slide's existing transitions and animations unless you change them, and refuses to overwrite existing animations without `--replace-timing`. Its Fade, Push, Morph and click builds were checked in real PowerPoint during testing. Morph only plays in PowerPoint (Microsoft 365 / 2019+); Keynote and Google Slides show a simple fallback; LibreOffice renders ignore motion, so **say transitions weren't checked in PowerPoint on this deck** unless they were.
- Keynote users can re-apply Magic Move where Morph was set; Google Slides only keeps simple transitions.

## 6. Outputs and fonts

**Format:**
- **Default master: .pptx** (16:9, 13.33×7.5" or pptxgenjs `LAYOUT_16x9` 10×5.625"). Keynote opens it; Google Slides imports it (File → Import slides, or upload to Drive and open with Google Slides).
- **Plus a PDF** whenever the deck will be sent or printed; the PDF is the safe way to share because it keeps the fonts and layout.
- If the user asks for Google Slides or Keynote directly and there's no tool for it, make the .pptx and say how to open it there.
- If the host offers its own slide-deck tool (a slides artifact or app) and they didn't ask for a file, that's fine too: apply this file's rules to it.

**Fonts: no installs by default.** A .pptx doesn't carry its fonts, so a deck built with custom fonts only looks right on machines that have them installed. That is the most common way AI-made decks break at work. **Decide fonts at the first format decision, before styling:**

1. **Work decks → no-install fonts, no question.** Signals: "for work", "my job", "for my team / boss / company / client meeting at work", colleagues will open or edit it, a company template. Use custom fonts only if they name them.
2. **Other editable decks → ask once** (it can ride along with the §0.5 questions): "Custom fonts? Everyone who opens the .pptx would need them installed (or embedded in PowerPoint). Otherwise I'll use no-install fonts like Georgia + Arial." No answer, or unattended → no-install fonts.
3. **A brand's own font** (e.g. Playfair Display on a client's site) follows rule 2: use it only when they name or approve it; otherwise use the closest no-install face and name the brand font in the finishing note so it can be swapped in.
4. **PDF-only decks** (only a PDF is needed, nobody edits the file) may use any free font, embedded in the PDF.

**No-install fonts** (common on current Windows and macOS; the PDF is always the exact version, because machines vary):
- **Core, on both systems:** Arial, Arial Black, Georgia, Verdana, Tahoma, Trebuchet MS, Times New Roman, Courier New, Impact.
- **When everyone opening it has Microsoft Office:** Calibri and Cambria too (Office installs them; a Mac in Keynote without Office may not have them). Avoid Aptos: it downloads on demand and renders unreliably in checks.
- Google Slides has all of these, so an imported deck keeps its look.

**Character with no-install fonts** comes from scale, weight, case, letter spacing and colour, not the face. Starting pairs (title / body):

| Feel | Pair |
|---|---|
| Calm & premium, professional | Georgia / Arial (or Cambria / Calibri when Office is certain) |
| Swiss, typographic, technical | Arial Black or Arial Bold with tight spacing / Arial; small labels in Verdana caps with wide spacing |
| Loud poster | Impact or Arial Black, very large / Arial |
| Editorial | Georgia with one italic word / Verdana or Arial |
| Playful | Trebuchet MS Bold / Verdana |

**When custom fonts are approved:**
- Choose fonts that exist on Google Fonts (Google Slides picks them up by name).
- Put the font files (or download links) in a `fonts/` folder next to the deck with a one-line install note, and say PowerPoint can embed them once installed (Windows: File → Options → Save → "Embed fonts in the file"; recent Microsoft 365 for Mac can embed too). The PDF carries them anyway.
- Keep body text sturdy; give display text boxes about 10% extra room.
- Install them where the renderer can see them before judging the slides (e.g. TTFs in `~/.fonts`, then `fc-cache -f`).

**Checking renders:** preview tools substitute fonts they lack. Arial, Times New Roman, Courier New, Calibri and Cambria usually get same-width stand-ins (Liberation, Carlito, Caladea), so text fit is trustworthy. For **Georgia**, install the free, same-width **Gelasio** and alias it (a fontconfig `<alias>` from Georgia to Gelasio) so the check is true. Verdana, Tahoma, Trebuchet MS, Impact and Arial Black have no free same-width stand-in: leave ~10% slack in those boxes and say text fit was checked with a substitute. The easiest checkable pairs are Georgia / Arial and Cambria / Calibri. If the PDF was exported with stand-ins, say so and suggest re-exporting it from PowerPoint or Keynote on a machine with the real fonts before sending. Brand fonts that aren't free: only with the user's files, otherwise the closest free face plus a note.

## 7. Charts, photos and notes

- **Charts:** native, editable charts (so the numbers can be changed), styled to the deck: one accent series, greys for the rest, no chart borders, direct data labels, readable axis text (≥12pt). No invented data: example charts are labelled "Example data".
- **Photos:** the user's photos go in marked slots ("Photo: team at work") sized for the final image. Treat photos to match the deck (duotone or tint in the palette, the same crop style throughout) when the tone calls for it; a professional deck keeps real photos natural but consistent. No hotlinked stock.
- **Code-built visuals** (shapes, big type, simple icons, colour fields) are the default when there are no photos. Keep icons from one family.
- **Logos:** the brand's real logo file only. Never draw or retype a client's logo, and never add client logos that weren't provided.
- **Speaker notes** on every content slide of a presenter deck: 2–5 short lines of what to say, plus any detail cut from the slide.

## 8. Checks before handing over

- **Back-of-the-room test:** view a slide at about 25% size; the title and main visual still read. Nothing under 12pt.
- **Contrast** of text on colour fields and on photos (use a scrim or a solid panel behind text on photos).
- **16:9**, consistent margins, no text overflowing its box, nothing clipped at the slide edge.
- **The titles alone tell the story** (professional and reading decks).
- **One visual world:** same motif, colours and type on every slide; dividers are the loudest slides.
- **Works with no motion:** export or render to PDF and read it through.
- **Honesty:** no invented numbers, quotes, logos or clients; drafts marked; sources present.
- **Fonts:** no-install fonts, unless custom fonts were asked for or approved (then `fonts/` folder, install note, rendered with them installed). Work decks always no-install.
- **Motion matches the context** (§5) and was checked in PowerPoint, or you said it wasn't.
- **Finishing note:** deck type, presenter or reading, tone, motion level, fonts (and, if custom, how to install them; if no-install, the custom option they can still ask for), cues borrowed, placeholders, what was and wasn't checked.
