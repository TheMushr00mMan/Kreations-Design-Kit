# Mode: Open WebUI and similar local-model clients

You are running inside Open WebUI (or a client like it), often on a **local model**. The skill may have reached you three ways: pasted into the model's system prompt, injected with a `$` mention, or loaded on demand through Open WebUI's Skills (`view_skill`). In every case, **assume you only have SKILL.md** (or the lite version). Reference files usually aren't available here; SKILL.md holds every rule you need.

## What you can usually do
- Write code in your reply. Open WebUI shows a **complete HTML page** (HTML with its CSS and JS in one block) or an **SVG** in its Artifacts preview, a sandboxed frame. That's where the user will look at it.
- Sometimes run code, if the admin enabled a code interpreter or Open Terminal. Check before claiming you ran anything.

## What you usually can't do
- Save files, open a real browser, take screenshots, or start other agents.
- Count on network access inside the preview: the frame may block outside requests (fonts, CDNs, APIs) depending on the admin's settings.
- Read the skill's reference files, images or assets.

## Do
- **Brand first and questions** exactly as in SKILL.md §0.5: ask, then wait for answers.
- **Deliver in the format they asked for.** For a page or "one HTML file" (the usual case), give one complete HTML file in a single `html` code block so the Artifacts preview can render it: `<!doctype html>` through `</html>`, CSS and JS inline, nothing omitted. If they explicitly ask for a project or a document, follow SKILL.md §9 instead: a project as a file tree plus each file in full, a document in its requested format as far as text allows. Say that only single HTML files and SVGs preview here.
- **Fonts:** prefer a strong system/fallback stack that looks right on its own, then optionally link one free web font. Say the font is unchecked, and never call the file offline-ready if it links anything.
- **Libraries:** avoid them when CSS/SVG/canvas can do the job. If you need one (e.g. three.js for a 3D stand-in), say it loads from a CDN and may be blocked in the preview; always keep a working non-3D fallback.
- **Decks without a file tool:** you can't hand over a .pptx. Give a slide-by-slide plan (title, content, visual, notes) plus the deck's design system (colours, fonts, motif, motion), and offer a complete pptxgenjs or python-pptx script they can run to make the file. Never claim a deck file exists.
- **Keep it buildable at your size.** A small model should choose fewer, better-executed moves: one focal idea, one motion moment, clean sections. A finished simple page beats an ambitious broken one.
- **Check your own code** before sending: tags closed, script runs top to bottom, controls wired, reduced-motion path, a phone-width layout.
- End with one or two lines: what you made, the category/tone/motion level, cues borrowed, placeholders, and "not visually checked here".

## Don't
- Don't mention subagents, screenshots, installs or saving files.
- Don't split a single-file request into several files; the preview needs one. Don't squeeze an explicit project request into one file either.
- Don't paste partial code or "…rest unchanged". If the page is too long for one reply, say so and ask whether to continue in a second message, then give the complete file.
