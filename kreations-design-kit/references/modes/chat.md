# Mode: plain chat (no file or code tools)

You can design and write code in your reply, but you can't save files, run anything, open a browser or start other agents. Plan everything around that.

## Do
- **Brand questions first** (SKILL.md §0.5): if there's no brand and the request is thin, reply with up to 5 short questions and 2–3 style directions to pick from, then stop and wait. Don't build in the same reply.
- Deliver in the reply:
  - **Fonts:** you can't embed or check fonts here, so link a free web font with a real fallback stack and say the typography is unchecked. Don't call the file fully self-contained if it links fonts.
  - **Single file** (the usual case): one complete HTML document in a single code block, with CSS and JS inline and nothing omitted ("…rest unchanged" isn't a deliverable).
  - **Multi-file project** (only if they asked for one): give a file tree, then each file in full in its own code block, labelled with its path, plus how to run and deploy it. Keep it as small as the job allows.
  - **Document:** write the full content and structure in the requested format as far as text allows (e.g. HTML with print CSS). Say plainly if a PDF/DOCX needs a converter on their end.
- **Decks without a file tool:** you can't hand over a .pptx. Give a slide-by-slide plan (title, content, visual, notes) plus the deck's design system (colours, fonts, motif, motion), and offer a complete pptxgenjs or python-pptx script they can run to make the file. Never claim a deck file exists.
- Review your own plan and code before sending: correct totals, working controls, reduced-motion path, a phone-width layout. You can reason about the code; you just can't claim it ran.
- End with one or two lines: what you made, the category/tone/motion level chosen, the cues borrowed, and "not run or visually checked here".

## Don't
- Don't mention or attempt subagents, sessions, background work, screenshots, installs or "I saved it to…".
- Don't reference images you can't see. Reference stills (`assets/keyframes/`, only if that folder is present) are only useful if you can view images.
- Don't split a single-file request into several files, or turn a project request into a single file without saying why.
