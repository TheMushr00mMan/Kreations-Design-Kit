# Review checklist (before handing anything over)

Go through what applies. Report what you actually checked and what you couldn't.

## Function
- [ ] The main action works. Key links and buttons go somewhere real or are clearly marked as placeholders.
- [ ] Selections, totals and calculations give correct results; empty, invalid and edge inputs are handled.
- [ ] Copy/download produces the **full, right content**, with the same text selectable on screen. "Copied" only after success; "Download started" for downloads.
- [ ] Client-facing tools don't expose owner settings (rates, config) as editable controls.
- [ ] Money tools / carts: running total visible on phones (hides when the full total is on screen); result panel as simple as the page, but it still shows the total, breakdown and fees.
- [ ] Placeholders only in drafts, with a small, quiet pinned draft bar; a final version has none. Publishing now never means inventing the missing facts.
- [ ] Nothing pretends to send, save or sync when it doesn't.

## Design
- [ ] Brand followed; if there was none, questions were asked (or assumptions stated when unattended).
- [ ] Richness is even across the page and matches the brand and ask; showy pages respect the soft cap unless more was asked.
- [ ] One-pagers and single pieces feel like one premium whole (no strip-stacked colour bands).
- [ ] The job is obvious within 5 seconds. There's one clear focal point, and one primary action on short pages (secondary actions quieter).
- [ ] It reads as the right kind of business or subject at a glance (industry fit), within the requested tone.
- [ ] Copy is short enough to skim: few-word headlines, one or two sentences each, no walls of text.
- [ ] No invented business facts (prices, turnaround, revisions, guarantees, results); unknowns are left out or visibly marked as placeholders. Only requested or clearly needed sections.
- [ ] Typography was chosen for this project, not repeated from the last one (e.g. no automatic serif + italic accent word). One display face; free fonts only (or the brand's own) on websites, tools and PDFs; a designed system stack when web fonts can't load; no-install fonts in editable Office files; professional/client work uses crisp faces (`fonts.md`); none of Didot, Helvetica, Futura, Gotham, Proxima Nova unless the client's brand already uses it. Paid fonts appear only in the finishing note, never on the page.
- [ ] The opening and the body got the same polish; the name/title is fully readable in the opening (objects may cross it, never hide it).
- [ ] If a palette from `palettes.md` was used, it was adapted to the brief (not dropped in whole) and never overrode a real brand.
- [ ] Footer: a neat footer, or one final scene if it suits a brand/story page (not tools, documents, short one-pagers or Practical local pages); links readable either way.
- [ ] The logo or name stays visible in the nav on phones.
- [ ] Rebuilds keep the original's page structure (multi-page stays multi-page) and come with a "what changed and why" explainer.
- [ ] Decorative motifs are anchored to an edge and used sparingly; sections read as distinct blocks.
- [ ] Variants/themes are visible selectable choices, not a blind cycle button.
- [ ] Products without photos use stylised 3D stand-ins in marked slots when that fits and can be built here, otherwise honest photo slots; never flat or fake-real drawings, and nothing when "no visuals" was asked.
- [ ] Documents: the headline leads without swallowing the page (about a quarter of the page height at most).
- [ ] The chosen font actually loads (embedded/self-hosted and seen), or it's stated as unchecked with a fallback.
- [ ] "Clean / reserved" still has one standout element; colour wasn't polished away.
- [ ] The category, tone and motion level match the request (§2–§3 of SKILL.md).
- [ ] Nothing is lifted 1:1 from a reference (palette, imagery, copy, names) unless an exact copy was asked for. The user's own brand is kept.
- [ ] One visual world: type, color, imagery and controls belong together, and every color has a role.
- [ ] Images follow the ask: marked slots, code-built visuals, or none.

## Motion and access
- [ ] Complete **and interactive** with reduced motion on: clicks, toggles, menus and 3D controls still work, every scene/section is reachable, nothing is stuck invisible. Actually click through it with reduced motion emulated if you can run a browser.
- [ ] Labels are at least 12px, contrast is readable, touch targets are at least 44px, keyboard focus is visible, and the tab order makes sense.
- [ ] At phone width (~375–400px) there's no accidental sideways overflow (tilted or moving strips such as tickers are clipped in a wrapper), nothing sits under a fixed nav, and the first photo/visual isn't pushed far below the fold. A contained wide table may scroll inside its own box.
- [ ] For print or PDF: check clipping, page breaks and readable type size instead of phone width.

## Decks (slides and presentations)
- [ ] Deck type and presenter/reading choice fit the ask; the titles alone tell the story (professional and reading decks).
- [ ] One visual world on every slide; dividers are the loudest slides; photos treated to match.
- [ ] Readable at about 25% size; 12pt minimum for everything, sources included; contrast on photos and colour fields; no text overflowing its box; 16:9 with steady margins.
- [ ] Fonts decided before styling: no-install fonts (work decks always; others unless custom fonts were approved). If custom: `fonts/` folder + install note, rendered with them installed. Rendered and looked at; PDF made for sending.
- [ ] Motion fits the context (professional: none or fade; pitch: 1–2 moments; creative: livelier, never spinning or flying) and the deck reads fine with none. Say if transitions weren't checked in PowerPoint.
- [ ] Speaker notes on presenter decks; sources on number slides; no invented numbers, quotes, clients or logos.

## Colour
- [ ] Brand colours were followed when given. Otherwise the palette came from a shortlist of about three that fit (not the first or habitual pick), including at least one that fits the field and one that stands out, and the other two are named in the finishing note.

## Delivery
- [ ] The deliverable matches what was asked (single file / project / format), or the difference is explained.
- [ ] Valid HTML: nothing after `</html>`. No dead external dependencies; fonts embedded, self-hosted or with a checked fallback. Base paths and routes work on the target host (or on any static host when none was given). The static build was tested if you could build it.

## Content
- [ ] Local businesses show practical info (hours, address or service area, contact, how to order or book), as marked placeholders when not given.

## Honesty
- [ ] A screenshot counts only if you **looked at it**. If you couldn't render the output, say "not visually checked".
- [ ] Say what you ran, what you only wrote, and anything that's an extrapolation (e.g. a tone/category combination with no reference).
