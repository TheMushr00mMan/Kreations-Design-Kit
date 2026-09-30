---
name: kreations-design-kit-lite
description: Condensed Kreations Design Kit for small local models. Use when the user asks you to build or restyle a website, landing page, portfolio, HTML tool, designed document or slide deck.
---

# Kreations Design Kit (lite)

A short version of the full skill for small models and short context windows. Follow it for any site, tool, designed document or deck the user asks for. There is no single house look: every project gets its own palette, fonts and layout.

## 1. Order of authority
1. What the user explicitly asks for.
2. The business's existing brand (logo, colours, fonts, site, photos). Follow it.
3. The kind of business (a bakery should read as a bakery at a glance).
4. These rules.

## 2. Ask first when there's no brand
If there's no brand and the request is thin, reply with up to 5 short questions, then **stop and wait**:
1. Logo, colours, fonts, site or photos to match?
2. Three words for the feel?
3. Sites or brands they like or hate?
4. What must be on the page, and what should never be there?
5. Calm and clean, or bold and busy?

Also offer 2 or 3 one-line style directions to pick from. Ask fewer questions when only one or two matter. Skip questions when the request is detailed or they say "just build it". Never ask what they already told you. For their own personal projects, ask only 1 or 2.

**Rebuilding an existing site:** the current site is the brief. Keep its brand, its real content and its pages. Don't ask brand questions and don't invent new claims.

## 3. Taste
- **One strong focal idea** per page: a subject, the type itself, or a tool's result.
- **Big against small:** a huge headline or subject with small, precise labels (labels at least 12px).
- **One visual world:** type, colour, imagery and controls belong together.
- **Colour carries character.** "Clean" or "minimal" still needs one standout element.
- **Avoid the generic AI look:** no split hero (headline on one side, one image on the other) unless nothing else fits or it's asked for; no default blue; no empty grey boxes (give missing photos or projects a designed stand-in with a small label); no hard cut between the hero and the next section.
- **Creative briefs** (portfolios, studios, tattoo, events, personal brands): commit to one bold idea from the name and feel; let the type carry the name.
- **Clear sections:** on multi-section pages each section reads as its own block (a colour block works well). A one-pager or flyer stays one cohesive piece.
- **Even care:** the sections below the opening are as polished as the opening.
- **Never hide the name or title** behind objects.
- **Short copy:** few-word headlines, one or two sentences each.
- **A real ending:** one clear call to action.

## 4. Motion and images
- "Showy / pop-y / wow": a few staged scenes. Nothing said: one standout moment. "Clean / subtle / professional": gentle fades at most. Tools and documents: motion only to explain a change.
- **Reduced motion** (`prefers-reduced-motion`): replace movement with instant changes, but keep every click, toggle and menu working.
- **Images:** they have photos → clearly labelled image slots. "No visuals" → none (colour and type are still fine). Otherwise → build visuals in code (gradients, SVG, CSS shapes). Never hotlink random images.
- Products without photos → a marked slot saying "replace with photo" (a simple stylised render if you can make one well).
- Decorative motifs (grass, waves) sit on an edge, used once or twice.

## 5. Fonts and colour
- One display face for headlines plus a clean sans for text. Websites and PDFs: free fonts (or the brand's own). Editable Office files: fonts every Windows and Mac already has (see below). If web fonts can't load, use a careful system stack, never Comic Sans or Papyrus.
- Crisp, confident faces for professional work; bubbly or ornamental faces only for playful briefs.
- Never pick Didot, Helvetica, Futura, Gotham or Proxima Nova (unless the brand already uses one).
- Give every font a real fallback stack. If you can't check the font loads, say so.
- No brand colours: take the colours from the brief itself (the name, product, place, materials, feel), 2 or 3 main colours, each with a job. Only if the brief gives nothing, build a palette from what the field usually uses. No default blue. Say in one line where the colours came from.
- Tools with states: blue info, green success, amber caution, orange risk, red failure, grey unknown, always with a label or icon.
- Editable Office files (Word, PowerPoint, Excel) use fonts every Windows and Mac already has. For work files, always, without asking. For other editable files, ask once before styling whether they want custom fonts (everyone would need them installed); no answer means the built-in fonts.

## 6. Honest content
- **Never invent facts:** prices, hours, results, reviews or guarantees. Leave them out or mark them `[Your hours]`.
- Drafts with placeholders get **one slim bar at the top**: "Draft: highlighted spots need real info."
- **Placeholders are for drafts only.** For a final or "ready to publish" version, ask for every missing real detail first. Never invent it, and never call a page final while any `[placeholder]` is left.
- Forms and buttons never pretend to send. Say "Copied" only after copying worked.

## 7. Tools and calculators
- The result is the focal point: correct math, units shown, a live total and a visible breakdown.
- On phones, keep a slim running total pinned to the bottom.
- Client-facing tools never let clients edit the owner's rates.
- Rates or prices the user didn't give are **example values**: keep them in one clearly commented block in the code, and say so on screen with the slim draft bar.
- Show options (themes, colours) as visible choices, not one button that cycles.

## 7.5 Slide decks
- Decide the type (client/report, pitch, creative) and whether it's presented (few words, details in speaker notes) or read (more text, still structured).
- Professional: titles that state the point, one message per slide, same margins everywhere, charts with the key number highlighted and a source.
- Creative: one visual world on every slide; dividers are the loud slides.
- Motion: professional none or fade; pitch and creative get a real motion pass (one shape carried through the deck with Morph, text that appears by itself), never spinning or flying. It must read fine with no animation.
- Fonts: no-install fonts by default (Georgia, Arial, Verdana, Trebuchet MS, Arial Black, Impact) so it works on any Windows or Mac. Work decks always; for others, ask once if they want custom fonts (they'd need installing everywhere).
- 12pt minimum for everything on a slide.
- If you can make files: a .pptx plus a PDF. If you can't: a slide-by-slide plan (title, content, visual, speaker notes) plus a complete script they can run. Never claim a file exists.

## 8. Delivery
- Default: **one complete HTML file** in a single code block: `<!doctype html>` to `</html>`, CSS and JS inline, nothing left out. If they ask for a project, a specific document format or a deck, give that instead (every file in full). Without a file tool, a deck is a slide-by-slide plan plus a script they can run.
- Make it work at phone width (~390px): no sideways scrolling, the name visible in the nav.
- Visible keyboard focus, readable contrast, touch targets at least 44px.
- A finished simple page beats an ambitious broken one: pick fewer moves and do them well.

## 9. Minimum bar for websites (check before sending)
Small models tend to produce a plain, centred, template page. That fails. For **website and landing-page briefs**, check each item. The user's explicit words always win ("no visuals", "subtle", "one-pager", "system fonts"), and tools and documents follow §7 and §8 instead.
- **A real hero:** a huge headline (clamp to about 12–18vw on phones, 7–10vw on desktop) plus **one code-built visual** tied to the subject (an SVG sun and waves for a surf coffee cart, a CSS candle glow for a candle shop), unless they asked for no visuals. Not just a coloured bar with centred text.
- **A layout with shape:** at least one asymmetric section (text left, visual or card right), not everything centred in a narrow column.
- **2–4 colour-blocked sections** with clear edges, each with its own job (a one-pager or flyer stays one cohesive piece instead).
- **One chosen display font** with character (linked from a free font service) plus a fallback stack. If web fonts may be blocked (e.g. a sandboxed preview), a strong system font stack styled with care counts too.
- **Details from the subject:** borrow its materials and conventions (a menu board, a sign, a label, a ticket), not generic cards.
- **Honest content:** anything not given (item names, prices, times, handles) is shown as `[placeholder]`, and there is a slim draft bar at the top saying so.
- **One small motion moment** unless they asked for none (a hero element easing in, a hover lift), with `@media (prefers-reduced-motion: reduce)` turning it off.
- **Phone check:** at 390px nothing overflows sideways (clip tilted or moving strips in a wrapper) and the name is visible.
- **Local businesses:** always include hours, address or area, contact and how to order, as `[placeholders]` if not given.

## 10. When you finish
In a few lines, say:
- what you made;
- the tone and motion level;
- any placeholders to fill;
- "not visually checked here" if you couldn't look at it.

For a redesign, add a short list: what changed, why, and what it does for visitors.
