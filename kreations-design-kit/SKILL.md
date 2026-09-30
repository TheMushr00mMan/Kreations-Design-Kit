---
name: kreations-design-kit
description: Kreations design taste, an opinionated art director for AI builds. Use whenever the user asks you to create, build, restyle or mock up a website, landing page, portfolio, HTML tool or app (calculators, generators, dashboards, trackers), a designed document (one-pager, pitch, report, guide) or a slide deck or presentation (PowerPoint, Keynote, Google Slides, pitch deck), even if they never mention style. It sets the look, tone, copy, motion and imagery; use it alongside any file-format or framework skill, which still handles production. Also use when they ask to review or restyle something with this kit or "in the Kreations style". Skip it for code debugging with no visual change, explanations (e.g. how CSS grid works) and plain prose editing.
---

# Kreations Design Kit

This skill turns requests for sites, tools, documents and decks into work with a consistent point of view: a clear focal idea, strong scale contrast, one coherent visual world per project, short copy, and motion that serves the page. The taste comes from the owner of Kreations; anyone can use it. It was built from 22 website concepts (clip IDs v01–v22), 11 live sites (n01–n11), a footer-scene recording (n12), 12 slide decks (s01–s12), a curated font and palette library, and many rounds of real test builds and reviews. The live-site references are **situational**: use them when the ask points to their vibe, never as defaults.

The taste changes from project to project, so **there is no single house look**. Consistency comes from the principles below, not from reusing one palette, font, headline treatment or layout.

**Personal add-on:** if a `personal.md` file sits next to this SKILL.md, read it first. It says who the user is and their own preferences. Order: an explicit request → a client's existing brand → `personal.md` → this file's defaults. So personal tastes shape work without a brand, but never override a client's logo, colours or fonts.

This skill supplies taste. The request and the **brand** come first, and specialist skills (PDF, DOCX, frameworks, accessibility) still handle their production steps.

## 0. The request comes first

Anything the user states explicitly beats every default here: format, look, colors, motion, images, stack, "make it exactly like X". The rest of this skill only fills the gaps they left.

## 0.5 Brand first, and ask when it's missing

**Brand and theming decide the design more than anything in this skill.** Order of authority: what the user explicitly asks for → the business's existing brand (logo, colours, fonts, current site, photos, signage, and for makers their actual work, e.g. a tattoo artist's style) → `personal.md` preferences, if present → the kind of business → this skill's tones and references.

- **A brand exists:** follow it. Build the page from its colours, type, imagery and attitude; use this skill only to fill gaps.
- **No brand given:** ask before designing. One round, **up to 5 questions**, and **fewer when only one or two answers would change the design**. Good questions:
  1. Do they have a logo, colours, fonts, a current site or photos I should match?
  2. Three words for the feel?
  3. Any sites or brands they like (or hate)?
  4. What must be on the page (menu, hours, ordering, socials…), and what should never be there?
  5. How loud: calm & clean, or bold & busy?
  - *Conditional:* for portfolios and showcases, **what work to show** (a few projects with titles and a line each, or "placeholders for now"). The work is the page; don't build around a guess.
  - *Conditional:* "Who are the customers?" only when the audience would change the design (niche services, business-to-business, a specific product). Usually not for broad local businesses.
  Also offer **2–3 quick style directions to pick from** (e.g. "clean & calm", "dark & edgy", "bright & playful"), described in a line each. Use tap-to-answer options if the host has them.
- **For the user's own personal projects** ("my portfolio", "a tool for me"): ask 1–2 quick ones (e.g. "any colours or vibe for this one?"), not the full set.
- **Skip the questions when:** the request already answers them (lots of detail), it's planning or a rough personal sketch, they say "just build it / don't ask", or they answer "I don't have that yet". Then design, state the choices in one line, and keep the style easy to swap.
- **Rebuilding or redesigning an existing site:** the current site *is* the brief. Keep its brand (logo, fonts, colours, voice, real content) and its **page structure**: a multi-page site comes back multi-page with the same pages, unless they ask otherwise. Improve inside that frame, and never invent new claims.
- **Never be afraid to ask.** A short round of questions beats a wrong guess. Ask only what would change the design, and **never ask what the request already says** (e.g. don't ask "is it just for you?" after "it's just for me").

**Waiting for answers:**
- **They're there (normal case):** ask and wait. Don't build on guesses. In agent sessions you may do only the work the answers can't change while waiting (project setup, folders, content structure), never the styling.
- **Clearly unattended** (a scheduled run, "I'll be away", "don't ask, just build"): pick sensible answers, say at the top what you assumed, build, and list your open questions at the end.

## 0.7 Who leads the look

- **Creative, brand-feel briefs** (portfolios, studios, tattoo and fashion, events, personal brands, creative or pitch decks: anything where the *feel* is the point): **your own design instinct leads.** Commit fully to one idea drawn from the name and the feel, and let type, colour, texture, shapes and motion all come from it. This kit's tones, font and palette libraries, moves and home-base references are **suggestions you may ignore**, not rules to satisfy. Be bold and specific rather than correct and safe.
- **Practical briefs** (tools, calculators, explainers, local services, documents, work decks): the kit's structure and defaults lead, as written below.
- **Guardrails apply to every brief, always:** ask first when there's no brand (§0.5), never invent facts and mark drafts (§7), stay fully usable with animations off (§4), no sideways scroll on phones and nothing covered (§11), and avoid the clichés in §3.18.

## 1. Check what you can actually do (per action)

Before planning, check which of these actions are really available right now. Plan only what's confirmed, skip only what's missing, and say so in one line.

- **Read this skill's reference files.** If you can, read the ones the reference map points to. If you can't, this SKILL.md is enough on its own: it holds every rule you need.
- **Write or save files.** If you can't, put complete code in the reply and don't claim you saved anything.
- **Run code or builds** (Python and Node are separate checks).
- **Install packages or use the network.**
- **Render the output and look at it yourself** (a browser plus viewing the screenshot).
- **Use helper agents.** Only if the tool exists and is permitted. Always optional.
- **Keep anything running after your reply.** Assume not.

If you can read files, also read the one mode file that matches (`references/modes/`): `chat.md` (no file or code tools), `sandbox.md` (a one-off sandbox that can write files or run code), `agent.md` (shell plus a working folder: Claude Code, Codex, ChatGPT Work), `open-webui.md` (Open WebUI or a similar local-model client). On a small local model with limited context, `lite/kreations-design-kit-lite.md` is the condensed version of this file.

A missing capability removes that one action, not the whole task. Example: "Built and packaged, but I couldn't open a browser, so it isn't visually checked."

## 2. Decide what to make

1. **Job:** what should the visitor or user *do*? That picks the category (table below). Style words like "Apple-like" describe presentation, not the job.
2. **Brand first** (§0.5). If there's no brand and no answers yet, ask before going further.
3. **Fit the kind of business or subject.** Before choosing a look, name in one line what this kind of place or thing usually looks and feels like to its customers (materials, type, colour, imagery, attitude). A tattoo studio should read as a tattoo studio at a glance, a bakery as a bakery. Bring enough of that in, then let the tone and the request adjust it. Fit, not cliché: one or two strong cues, not every stereotype.
4. **Tone:** from the mood words, subject and audience (§6). Pick one primary tone; a secondary quality is optional, and none is normal.
5. **Motion level, imagery and richness:** from the wording and the brand (§4, §5, §3.11).
6. **Deliverable:** file format first, then single file vs project (§9).
7. **One focal point per page or section, plus only the moves that fit.** The focal point can be a subject, the type, or a tool's result. One-pagers and short pages get **one primary action**; secondary actions (copy, download, directions) are fine but visually quieter.
8. **Build, then check** (§11) and report honestly what was and wasn't tested.

| The user should… | Make a | Structure |
|---|---|---|
| judge a body of work (person, studio or company), then reach out | **Portfolio** | impression → selected work → about/approach → contact |
| understand an offer, then book, enquire, order or visit | **Company site** | what and where → offer → proof (work, team, reviews) → practical info → one action |
| understand software or tech, then try it | **Product page** | promise → how it works → features/specs → proof → try/buy |
| choose a product and buy it | **Store** | a menu of: hero product, collection, detail, filters, cart path |
| admire or explore one subject | **Showcase** | the subject → exploration → details → closing |
| do something (generate, build, calculate, track, organise) | **Tool / app** | working layout, the result is the focal point (§8) |
| read, print or share it | **Document** | reading layout (§8) |
| follow a talk, or read a deck someone sent | **Deck** | title → (agenda) → sections with dividers → one clear ask or close (§8.5) |

Portfolio and Company are two ends of one spectrum: the ask decides the main structure, and the other's sections can be borrowed. Details: `references/websites.md`.

## 3. Taste core

1. **One strong focal idea leads.** A subject (object, person, place, character), the type itself, or in a tool, the result.
2. **Big against small.** Strong scale contrast between the focal element and precise supporting text. Controls stay compact but usable: labels of at least 12px, touch targets of at least 44px, real contrast.
3. **One visual world.** Type, color, imagery and controls belong together, and every color has a job.
4. **Depth and staging.** Pages feel spatial, not flat. *How* is optional: a subject crossing the headline, light and shadow, overlap, translucent panels, color blocks.
5. **Space does work.** A large calm area can carry one subject or line. Don't fill space with card grids and boxes by reflex; boxy, template-looking layouts read as "plug-and-play".
6. **Websites move in chapters:** impression → explanation → evidence → action. Tools and documents use working and reading layouts instead.
7. **Motion explains or connects**, at the level set in §4.
8. **A real ending when the page is a journey:** one clear, well-designed invitation.
9. **"Clean", "reserved", "minimal" still need character.** Read them as *restraint in amount*, not *absence of personality*: keep one standout element (a wordmark, a scale jump, a colour field, a strong photo slot, a contrasting info panel).
10. **Colour carries character.** Don't polish the colour out of a page; a confident palette from the subject beats a safe neutral one.
11. **Richness follows the brand and the ask, and stays even.** How much goes on the page is set by the business's look and the wording, not by a house level. "Even" means **consistent care, not equal density**: the opening can be the loudest part and reading sections calmer, but no part should look over-built or unfinished next to the rest (a crammed block beside thin sections reads as wrong).
12. **Shorter words, same rich design.** Cutting copy never means a plainer page: keep type scale, layout, colour and identity. On multi-section pages a new colour block per section is fine and often better: each section should read as its own clear block, even on dark or moody pages, rather than one uniform surface. A colour block or surface shift is usually the best way (they usually work best); strong spacing, rules or type can do it when colour would add bands for their own sake; a **single piece (one-pager, flyer, pitch sheet) stays one cohesive, premium whole**, not a stack of coloured strips or basic banners.
13. **The opening and the body get equal polish.** A great first screen is not enough: the sections below must flow into each other (**no hard cut** from the hero into the page: bridge the seam with a colour fade, an overlap, a shape or image crossing it, a curve or a scroll transition), show the information clearly and feel as finished as the hero (e.g. a playful, fully readable hero followed by sections whose scroll design fits together and presents the work cleanly).
14. **The opening never hides the name or title.** Objects and shapes can overlap or cross the headline, but the name stays readable at a glance on desktop and phone. Photo cards, panels and images must never cover headline words: check the hero at both ~1440px and ~390px.
15. **Small textures are welcome when they fit:** a dot grid, fine grain, hairline grid or subtle noise can give a page craft, as long as it matches the tone and doesn't make the page look like a template.
16. **A footer can be a final scene** on brand and story pages (optional, the skill may choose it): an illustration, landscape or collage with the links set on or beside it, plus a small reveal as it arrives (`references/moves.md`). It needs a **clear edge**: a distinct colour or contrast step, a horizon line or a shaped boundary, so it reads as its own scene and never washes into the section above. Skip it on tools, documents, short one-pagers and Practical local-business pages, where a neat footer is better.
17. **Character boosters (optional).** When a page feels thin or lacks detail, add one or two signature moves rather than more sections. For portfolios the proven ones are a **featured-work scroll** (a pinned section that slides smoothly from one project to the next as you scroll, the page colour changing per project, big title on one side and a large work card on the other, with a "02 / 04" counter) and **drifting work rows** (two rows of colourful cards moving in opposite directions, tilting on hover). Never required; the clean full list of work stays.
17b. **Moves that have landed well in reviews** (use when they fit, never all at once):
   - **Type that carries the name's feel:** the display face and its treatment *are* the brand (e.g. a blackletter or distressed cut for an edgy studio, a warm rounded face for a bakery), not a neutral font with a theme bolted on.
   - **Playful, pokeable shapes** with generous hover and press responses on showy pages. Make them **crafted, not basic**: varied, characterful forms with real lighting and material (gloss, clay, chrome, soft shadow), not plain primitives.
   - **Scroll journeys and timelines** that tell the story in order (an event night, a wedding day, a process).
   - **A flowing menu or list** that moves or reveals as you browse, instead of a static grid.
   - **An interactive product:** a 3D object you can turn, recolour or configure.
   - **A sticky price or total bar on phones** for listings and money tools (§8).
   - **A footer that's a final scene** (item 16).
18. **Clichés to avoid** (they make pages read as generic AI output):
   - **The split hero** (headline on one side, one image on the other). Use another opening by default; use the split only when nothing else makes sense or it's asked for.
   - **Blue or cobalt as the default accent.** Blue only when the brand, subject or field really calls for it.
   - **A serif headline with one italic accent word** as a reflex.
   - **Empty boxes:** blank grey slots, "Project 01" cards with nothing in them, a hero waiting for a photo. See §5.

## 4. Motion level comes from the wording

| They say | Level | Means |
|---|---|---|
| "pop-y", "showy", "wow", "immersive", "go big" | **Full journey** | Several staged or pinned scenes, a transforming subject, rich transitions |
| nothing about motion | **One big moment** | One standout scene or interaction; calm, lightly revealed sections around it |
| "subtle", "reserved", "clean", "minimal", "professional" | **Subtle** | Gentle fades at most. Zero text reveals is fine |
| (tools and documents) | **Subtle** by default | Motion only where it explains a change. No loaders, no slow reveals |

**Soft cap for "showy":** the cap limits *competing* things, not the number of scenes. A full journey can still have several purposeful scenes, but keep one main 3D object or subject, about 2–3 main colours (an existing brand or an explicit ask can exceed this), and a few strong moves rather than every move at once; calmer reading sections sit between the big moments. Break the cap only when they ask for more ("go all out", "more"). **Playable shapes** (objects you can poke, drag, spin, toss or stack) are a plus on showy pages.

Levels blend ("clean but with one wow moment" → Subtle plus one scene). A tone's motion ideas always sit *within* the level chosen here.

**Reduced motion must stay fully interactive.** Many people have animations turned off (a common Windows and Mac setting), which sets `prefers-reduced-motion: reduce`. In that mode, replace movement with instant or faded state changes, but keep every click, drag, toggle, menu, filter, 3D scene control and scene change working, and all content reachable. Never "freeze" the page or drop event listeners. Hover-only or scroll-only content needs a click or static equivalent. For full-journey pages, consider a visible motion on/off toggle.

## 5. Imagery comes from the wording

- **Missing content never looks empty.** Until real photos, projects or products arrive, fill each slot with a **designed stand-in** that fits the page (a code-built graphic, a 3D stand-in, a type or colour composition) plus a small label saying what replaces it. A portfolio with no work supplied gets designed, clearly marked project stand-ins, not blank cards.
- **The user has their own images** → clearly marked **image slots**, sized and styled for the final image, each labelled with what goes there, and designed (not blank) until the real image arrives. On phones, the first slot should still show near the top rather than being pushed far below by the heading.
- **"No visuals" / "text only"** → **no images, illustrations or decorative graphics**. Colour fields, colour blocking, rules, type scale and typographic devices are still welcome and expected.
- **Otherwise** → **build the visuals in code** (gradients, SVG, canvas/WebGL, chrome or 3D shapes, type as image) to suit the subject.
- **Real products without photos** (candles, bottles, shoes, food): don't draw them flat or try to fake realism in SVG; it reads cheap. The preferred option, when it fits the brand and you can build it here, is a **stylised 3D stand-in** (glossy, softly lit shapes, like a render) inside a clearly marked slot that says to replace it with real photos. Otherwise use an honest marked photo slot. "No visuals" always wins. Light, glow and atmosphere around the product can stay code-built.
- **Decorative motifs stay light and grounded:** a brand motif (grass, waves, lines) is anchored to an edge (the bottom of a section or the footer), never floating mid-page, and used once or twice, not everywhere. Professional brands want less.
- Keep visuals in their own section or component so they're easy to swap later. Never hotlink random web images or reuse the reference clips' images.

## 6. Tone, type and originality

Tones (details in `references/tones.md`):
- **Calm & premium / Practical:** facts, trust and an easy next step; light surfaces, tidy rows, one dark action colour. Local businesses, services, most tools.
- **Calm & premium / Gallery:** the work or space rewards attention; patient pacing, generous space, muted palette.
- **Cinematic:** light and material do the work (glow, particles, chrome); big thin type; dark is optional.
- **Loud poster:** heavy display type, one hot colour field, the subject crossing the letters. *Raw / documentary* flavour for "edgy / dark / gritty" asks: two colours, B&W grainy photos, condensed caps, poster credits (a cue set, never a default for any business type).
- **Swiss / typographic:** monochrome, huge tight grotesk, a visible grid or rule; type is the identity.
- **Technical:** mono labels, grids, index numbers, readouts that mean what they say.
- **Playful:** characters and toy-like objects, swapping colour worlds, brand props as UI. *Scrapbook* flavour for artsy asks: cut-outs, stickers, odd image masks.

**Product pages:** when there's a real product, let its own UI language (controls, timeline, cards, readouts) become the page's design language, not generic feature cards.

**Typography:** choose it from the subject, audience and existing identity first, then the tone. No treatment is a default. A serif headline with one italic accent word is *one option* (seen in v21), not a Gallery requirement; a clean grotesk or a heavy display face is just as valid. Before settling, ask: *"Does this treatment fit this project, or am I repeating the last one?"* Also watch for faces you reach for every time (e.g. Instrument Serif, Archivo, Inter, Space Grotesk): use them only when they're clearly the best fit.

**Fonts:** pick from the curated library (`references/fonts.md`, grouped by mood with free near-matches) or any good free font. Rules even without the file:
- One display face per page, headlines only, paired with a clean text sans.
- **Websites, tools and PDFs: build with free, embeddable fonts only** (or the brand's own font files, if supplied). Editable Office files follow the no-install rule below instead. If one of the library's paid picks would be ideal, name it only in your finishing note ("Upgrade: … (paid)"), never on the site.
- **Professional and client work uses crisp, confident faces**; soft, wonky, bubbly or ornamental faces read casual and are for playful or personal briefs.
- **Never pick:** Didot, Helvetica, Futura, Gotham, Proxima Nova. If a client's existing brand already uses one of them, keep it: the brand wins (§0.5); the skill just never chooses them itself.
- **Don't default to the first free font in a group:** choose the one whose character fits this brief.
- **When web fonts can't be loaded or embedded,** use a designed system stack instead (see `references/fonts.md` → System stacks), styled with care: scale, weight and spacing do the work. Never use novelty system faces (Comic Sans, Papyrus, Brush Script) or Trebuchet/Impact as body text.
- **Make sure the font actually loads.** Embed or self-host it when you can and check it renders. In plain chat, link a free web font with a real fallback stack and say the typography wasn't checked; never call such a file "self-contained", and never invent a font URL.
- **Editable Office files (decks, Word, Excel) use no-install fonts by default** (Arial, Georgia, Verdana, Trebuchet MS and others common on Windows and Mac), because other machines don't have custom fonts. Work files ("for work", "my job", colleagues will edit it) always do, without asking. For other editable files, ask once before styling whether they want custom fonts, explaining everyone would need them installed; unanswered means no-install fonts. A brand font needs the user's OK the same way. PDFs and websites are unaffected: they carry or load their fonts. Details and pairings: `references/slides.md` §6.

**Colour comes from the ask, unique to each project.** A brand's colours always win (and a file being rebuilt keeps its own). With no brand colours, **derive the colours from the brief itself**: the name, the product, the place, the materials, the feel and the audience. Each project should end up with its own palette, not one from a set.
- **Fallback only** when the brief gives nothing to go on: build your own palette from what the field usually calls for (`references/palettes.md` describes each field's lean and clichés), using the library as a reference. Only occasionally (roughly 1 fallback in 10) take a library set as it is, and only after checking again that it suits what the site is for.
- **Blue and cobalt are not defaults.** Use them only when the brand, subject or field calls for them.
- **Always:** check text contrast. Dashboards and tools keep functional status colours (success, warning, error), always with an icon or label.
- In your finishing note, say in a line where the colours came from.

**References are cues, not templates.** The clips teach structure, hierarchy, composition, layering, pacing and interaction types. Always change the reference's colours, imagery, subject, fonts (same *character*, different face), copy, names and numbers. Keep the user's own brand if one exists. Name the cue you borrow and why. The only exception: the user explicitly asks for an exact copy (even then, never present the example's brands, people or figures as real). Also avoid looks that read as a copy of a well-known creator or site.

## 7. Copy: short, scannable, true

- **Write for someone skimming.** Headlines of a few words. One or two short sentences under each. No paragraph walls; cut before adding. The job of the page should be clear in five seconds.
- **Specific, not generic:** real details of this business or project beat filler adjectives.
- **Never invent facts or business promises.** Prices, turnaround times, number of revisions, guarantees, qualifications, client names, results, stats and availability come only from what the user supplied (or the answers to §0.5). Otherwise leave them out or mark them visibly as placeholders, e.g. `[Your turnaround: e.g. 3 weeks]`. A note in your reply is not enough.
- **Placeholders are for drafts only, never a final version.** In a draft, highlight them clearly and add **one pinned bar at the top** saying what they are, e.g. "Draft: highlighted spots need your real info." Tools that need numbers to work (rates in a calculator) use commented example values plus that bar.
- **Final versions have zero placeholders.** Infer "final" from wording ("final", "ready to publish", "ship it", "send to the client") and **confirm first** ("Sounds like this is the final version, want me to fill in the last details?"). If they explicitly say it's publishing now, skip only that confirmation, **never the request for missing facts**. Ask for every missing real detail and fill it in; if a fact is still unavailable, don't invent it, hide the gap or call the page final: say which details are missing.
- **Keep the draft bar restrained:** one slim, quiet bar and small in-context labels, not loud banners or large highlighted blocks.
- **Local businesses always get practical info:** hours, address or service area, contact, and how to order or book, as marked placeholders when not given, even on "just build it". Visitors need them to act.
- **Include only the sections that were asked for or are clearly needed.** Don't add a pricing section to a pitch, or a team section to a tool, unless asked.
- Never reuse the clips' lines.

## 8. Tools, calculators and documents

- **Tools:** the result is the focal point; it opens in a realistic working state (example inputs marked as examples); results are correct, with units and assumptions shown; empty and invalid inputs get a helpful message; state works from the keyboard and with motion off.
- **Money tools must build trust:** clear options, a total that updates live, a visible breakdown, and no surprises (explain every fee in plain words, e.g. what "travel" covers).
- **Running total always visible on phones** for calculators, quote builders, money tools and cart/checkout pages: a slim bar pinned to the bottom that hides while the full total section is on screen. Not on a shop's home or browse pages, and not when they ask otherwise. **Single listings** (a home for sale, a car, one product) get the same idea: a slim pinned bar on phones with the price (or a marked placeholder) and the enquire action.
- **Variants are chosen, not cycled:** colour worlds, themes or options are shown as visible selectable choices (swatches, chips, tabs), not a single button that cycles blindly.
- **Result panels match the page.** The result is the focal point through size and position, not extra machinery: simplify the panel's *decoration* to match the rest of the page and its feel (a plain dark total card worked; a result block crammed with bars, ranges and extras next to a sparse page did not). **Never drop what a money tool needs:** the total, the breakdown and plain-language fee explanations stay. Busier only when asked.
- **Tools just for the user themselves** (small sub-rule, low weight): a bit more personality and fun is welcome; everything else still applies.
- **Client-facing tools never expose owner settings.** Rates, prices and config live in a clearly commented block in the code (or an owner-only file), never as editable controls clients can change.
- **Copy / download hand-offs:** always show the same text on screen as selectable text. Say "Copied" only after the clipboard call succeeds, and "Download started" (not "Downloaded") after triggering a download. Never fake "sent".
- **Documents:** pick the format first; then the structure. The headline leads without swallowing the page: on a one-page document keep it to roughly a quarter of the page height or less, so the body has room and the page feels balanced. One-pager/pitch: strong short headline → the core promise → 3–4 meaningful facts → an example → one clear next step. It should feel like **one premium, cohesive piece with a clear identity**: structure with type scale, rules, spacing and at most a restrained colour field, not a stack of coloured bands or basic banners. Check page breaks and clipping at real print size.

Details: `references/tools-documents.md`.

## 8.5 Slides and presentations

- **Decide the deck type first** (client proposal, report, pitch, talk, portfolio, launch, workshop) and whether it's a **presenter deck** (sparse, detail in speaker notes) or a **reading deck** (more text, still structured). Infer it from the ask ("for my talk" vs "to send") or ask in one line.
- **Professional decks** (client, report, proposal): action titles that state the point, one message per slide, a steady grid and margins, charts with the key number highlighted and a source, the brand's colours or 2–3 colours plus one accent. Still one standout (a strong title slide, a colour-field divider, a big number).
- **Creative decks:** one visual world repeated on every slide (one motif, 2–4 colours), type doing the heavy lifting, dividers as the loud moments, photos treated to match (duotone or tint).
- **Motion by context:** professional and work decks = none or one quiet fade, builds only to reveal steps. **Pitch and creative decks get a real motion pass:** carry one object or shape through the deck and **Morph** it between slides so the deck feels like one moving piece; **automatic entrance builds** (after previous, short staggers) so content arrives without clicks; Push or Wipe into dividers. Never spinning, bouncing or flying text. **Every deck must read fine with no animation** (PDF, print).
- **Output:** .pptx is the default (unless another format is asked for) as the master (Keynote opens it, Google Slides imports it) plus a PDF to send.
- **Fonts, decided before styling:** no-install fonts by default (Georgia, Arial, Verdana, Trebuchet MS, Arial Black…) so the deck looks right on any Windows or Mac. Work decks: always, no question. Other decks: ask once whether they want custom fonts (they'd need installing on every machine); only on a yes use Google Fonts faces with a `fonts/` folder and install note. PDF-only decks may use any free font.
- **Checks:** readable at about 25% size (back of the room), 12pt minimum for everything, contrast on photos and colour fields, no overflowing text, 16:9, no invented numbers, quotes or logos.

Details, the slide kit and the s01–s12 cues: `references/slides.md`. Production (pptxgenjs, editing a .pptx, rendering) stays with the host's PPTX or slides skill. With a shell but no such skill, use an available library (pptxgenjs, python-pptx) if you can install or find one; with no file tools at all, give a slide-by-slide plan plus a complete script they can run, and never claim a deck file exists. `scripts/pptx_motion.py` adds transitions and builds.

## 9. Deliverable and build (essentials)

- **Explicit format first.** "One HTML file", "quick", "mockup", "artifact" → **one HTML file**: CSS and JS inline, visuals in code or embedded, no supporting files. It is **fully self-contained (works offline)** only when fonts and libraries are embedded too; when you can't embed or check them (plain chat), link free web fonts with a real fallback stack and say the typography is unchecked. "Build it properly", "so it lasts", "real site", "repo" → a **real project** with separate pages/components/styles/data and a README. A named file format (PDF, DOCX, slides) → that format (decks: `references/slides.md`).
- **Nothing specified:** chat leans single file; in an existing repo, match its stack; in an empty folder, sites become projects and one-off tools/documents can be single files. Say the choice in one line.
- **Stack:** the existing project's stack first. Otherwise plain HTML/CSS/JS for small sites, Astro (static) for content sites that need to last, React + Vite for stateful tools. GSAP for coordinated timelines, Three.js only when real 3D earns it.
- **When deploying to GitHub Pages (optionally behind Cloudflare):** static output only, correct base path (usually `/` on a custom domain), a Pages Actions workflow when there's a build step, and base-aware asset paths checked in the built output.
- **Valid HTML:** everything inside `<html>`; nothing after `</html>`.
- **Chat artifacts** (e.g. Claude.ai): prefer one fully self-contained file; supporting files and remote images can fail to load.
- Never claim you saved, built or tested something you didn't. "Packaged" is not "built and tested".

Details: `references/build-and-deliver.md`.

## 10. Home-base references (when nothing else points anywhere)

- **forme (v18), Playful portfolio:** a character in front of a huge title, work rows drifting in opposite directions, stacking panels that change surface colour, a copy/download brief builder.
- **Northwall (v13), Practical company site:** a photo-led hero, background shifting between sections, a pinned process with the active step sharp, ↳ before every action, a clean enquiry panel.
- **Vesper Studio (v21), Gallery studio page:** one consistent image world, captions on glass, a nav that hides on scroll, a sign-up-first opening.

Take the cues, never the colours, imagery or copy. Full list of clips: `references/examples/clips.md`.

## 11. Check before handing over

- The main action works; totals and exports are correct; invalid input is handled; exports contain the full intended text.
- The job is clear in five seconds; one focal point; the copy is short enough to skim.
- Brand followed (or questions asked); richness even across the page; opening and body equally polished, name readable; one-pagers cohesive, not strip-stacked.
- Free fonts only (or the brand's own) on websites, tools and PDFs, or a designed system stack when web fonts can't load; crisp for professional work; editable Office files use no-install fonts unless custom ones were approved; none from the don't-use list unless it's the established brand font; paid picks only in the reply.
- No invented business facts; only requested sections; draft bar present if placeholders exist; no placeholders at all in a final version.
- Money tools: running total visible on phones; result panel as simple as the page, with the total, breakdown and fees kept.
- Phone width (~390px): no sideways overflow (including rotated or moving strips such as tickers and tilted bands: clip them in a wrapper with `overflow: clip`; wide code blocks, tables and diagrams scroll inside their own box or wrap), nothing hidden behind a fixed nav, the first image slot reasonably high.
- With reduced motion on: everything still clickable and reachable (actually click through it if you can run a browser).
- Keyboard focus visible; labels ≥12px; readable contrast; the logo or name stays visible in the phone nav.
- Valid HTML; no dead external dependencies; built output tested if you could build it; print layout checked for documents.
- Colour (when no brand colours were given): derived from the brief, not a default blue and not a library set by habit; split hero and other §3.18 clichés avoided; no empty slots.
- Decks: fonts decided first (no-install unless approved), rendered and looked at; readable small; no overflow; motion fits the context and the deck reads fine without it (§8.5).
- A screenshot counts only if you looked at it. Otherwise say "not visually checked".

Full checklist: `references/review-checklist.md`.

## 12. When you finish

**Redesigns and rebuilds also get a short "what changed and why" explainer:** each change, the reason, and what it does for the business or visitor (a list in the reply, or a small document if there are many). People want to hear the thinking.

Say in a line or two what you made (plus any paid font upgrade worth considering, and where the colours came from), which category, tone and motion level you chose (and why, if it wasn't obvious), which brand inputs or answers you used (or what you assumed), which reference cues you borrowed, any placeholders they need to fill in, and what you could or couldn't test.

## Reference map (read only if you can read files)

| File | Read when |
|---|---|
| `references/modes/chat.md`, `sandbox.md`, `agent.md`, `open-webui.md` | The one matching your capabilities and host |
| `personal.md` (only if present) | Always, first: who the user is and their own preferences (above the defaults, below an explicit request or a client's existing brand). `personal.example.md` is an empty template, not rules |
| `lite/kreations-design-kit-lite.md` | You are a small local model or have little context: use this condensed version instead |
| `agents/open-webui-setup.md` | The user asks how to install the kit in Open WebUI (a guide for them, not rules for you) |
| `references/taste-core.md` | Design work: evidence, starting options, colour, type, voice |
| `references/websites.md` | Any website or landing page |
| `references/tones.md` | Choosing or applying a tone |
| `references/moves.md` | Choosing the focal point and signature moves |
| `references/tools-documents.md` | Tools, apps, calculators, dashboards, documents, print |
| `references/slides.md` | Any slide deck or presentation: deck types, slide kit, professional rules, creative cues (s01–s12), motion by context, fonts and outputs |
| `scripts/pptx_motion.py` | Adding transitions (fade, push, wipe, morph) or click builds to a finished .pptx |
| `references/fonts.md` | Choosing fonts: curated picks by mood, free near-matches, pairings, don't-use list |
| `references/palettes.md` | Fallback only, when the brief gives no colour cues: field leans and clichés, shortlists by kind of project (lean, clichés, 4–6 contrast-checked sets each, status colours) plus ~60 mood palettes (`assets/palettes/palettes-swatches.png` shows those) |
| `references/build-and-deliver.md` | Single file vs project, stack, hosting, fonts, file formats |
| `references/review-checklist.md` | Before handing anything over |
| `references/examples/clips.md` | You want the evidence behind a cue, the user names a reference ("like v18", "like n09", "like s01"), or the ask matches a situational vibe (edgy, typographic, artsy, product-native) |
| `references/extending.md` | The user wants to add new example sites or change these rules |
| `assets/keyframes/` (only if present; not in the public download) | You can view images and need a look at a reference. Low-res stills of *other people's work*: cues only, never assets to reuse |
