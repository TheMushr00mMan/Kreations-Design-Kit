# Tools and documents

None of the 22 clips is a tool or a document, so everything here is **suggested**. It's built from the taste core plus the interactive bits that do appear in the clips. Say so if it matters.

Tools and documents share the taste core and tones, but they use **working and reading layouts**, not marketing chapters:
- Display scale is smaller than a website hero. The focal point is the **result** (the number, the brief, the chart), not a decorative scene.
- Motion is **subtle** by default, used only to explain a change (a number updating, a panel opening). No loaders, no slow text reveals, nothing between the user and the answer.
- The tool opens in a realistic working state (example inputs clearly marked as examples), not as an empty shell.
- Name tools by what the user *does*.

## Tools and apps

| Type | Structure | Borrows from |
|---|---|---|
| **Generator** (form → output) | a short intro → grouped inputs → live or on-demand preview → copy / download, plus selectable text | v18's brief builder, v13's quiet form rows |
| **Builder / configurator** | options → live result + running total → summary → copy / download | v14's room with a total, v16/v19's scene swap, v18's export |
| **Calculator / scenario explorer** | the question → inputs → a big, clear result → comparison or breakdown → assumptions shown | v04/v11 big-number rows, v15's central subject with notes at the edges |
| **Dashboard / tracker** | summary first → key measures → list → detail panel → next action | v04's proof row, v13's rows, v03's precise labels |
| **Organiser / reference library** | search / filter → items → selected detail → saved set / export | v08's filters and product grid, v22's detail views |
| **Playground / explainer** | one central subject → small controls → labelled changes → reset | v01, v15, v17, v22. The best home for richer motion. |

**Tool rules**
- Results must be correct. Show assumptions and units. Handle empty, invalid and edge inputs with a helpful message.
- Readouts and "live" labels must mean what they say. Never fake data or activity.
- State shows in form as well as numbers (pills, chips, color by meaning), and semantic colors (good / warning / bad) are kept separate from the brand accent.
- Everything works with motion off and from the keyboard.
- Copy/download always has a selectable-text fallback showing the **full** export text. Say "Copied" only after the clipboard call succeeds, and "Download started" after triggering a download (the page can't confirm the save).
- **Client-facing tools never expose owner settings.** Rates, prices and config live in one clearly commented block in the code (or an owner-only file). No editable rates panel for clients.
- **Running total on phones:** calculators, quote builders and carts keep a slim total bar pinned to the bottom that hides while the full total section is visible (not on shop home/browse pages).
- **Result panels match the page:** the result leads through size and position; keep the panel as simple as the rest and in the same feel. Don't cram it with extra bars, ranges and widgets next to a sparse page.
- **Money tools build trust:** clear options, a live total, a visible line-by-line breakdown, and every fee explained in plain words (e.g. whether travel covers the return trip). No surprises.
- Search, filter and calculate locally. Nothing needs sending anywhere.

## Documents

**Pick the format first** (HTML page, PDF, DOCX, slides, or whatever was asked; decks follow `slides.md`), then the structure. **Editable Word and Excel files** follow the same no-install font rule as decks (`slides.md` §6): work files always use fonts common on Windows and Mac; otherwise ask once before using custom fonts. A PDF can embed any free font. Don't force web-page defaults onto a printable document.

| Type | Structure |
|---|---|
| **Report / decision brief** | the main finding → evidence → options → recommendation → sources / appendix |
| **Guide / playbook** | purpose → numbered stages → examples → checklist / reference |
| **One-pager / pitch / capability sheet** | a short, strong headline → the core promise → 3–4 meaningful facts → an example → **one** clear next step. No pricing section unless asked. |
| **Case study / visual essay** | the whole project → key decisions → annotated details → outcome → credits |
| **Reference catalogue** | index → consistent entries → comparison tables → cross-references |

**Translating the taste to documents and print**
- The focal idea becomes a strong cover or opening spread (big type, one image or code-built visual, or none if asked).
- Motion becomes a sequence of stills, before/after panels or annotated views.
- Floating nav becomes a contents list, running headers and page numbers.
- Chapters become clear sections with numbered or labelled headings.
- Long passages go on light pages with readable type at the real output size. Save dark or saturated color for the cover and dividers.
- Keep margins generous, crop images carefully, and check page breaks so nothing gets clipped.
- Structure the page with type scale, rules and spacing so the eye has places to land. "No visuals" still allows colour, but a one-pager stays **one cohesive, premium piece**: at most one restrained colour field, never a stack of coloured bands or basic banners that break it into strips.
- Shorter copy never means a plainer page: keep the identity and richness.
- **Balance the headline:** on a one-page document it leads but takes at most about a quarter of the page height; an oversized headline makes the rest feel squeezed.
- Keep copy short: a headline of a few words and one or two sentences per point. A page of dense text reads as a first draft.
- **No invented business terms.** Prices, turnaround, revisions, guarantees and results come from the user; otherwise leave them out or mark them visibly as placeholders in the document itself (`[Your turnaround]`).
- A report needs evidence, sources and a conclusion. A one-pager doesn't have to be a squeezed portfolio.
