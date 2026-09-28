# Mode: full agent (shell + working folder)

Claude Code, Codex (Local, Worktree or Cloud), ChatGPT Work (local or cloud). You can usually create folders, install packages, run a dev server and build. Still, **check each capability**: network, package installs, a browser and helper agents can each be missing or blocked, and a cloud task can't see local folders or apps.

## Workflow
0. **Brand first** (SKILL.md §0.5). If there's no brand and the request is thin, ask up to 5 questions (use the host's question tool if it has one) and wait. While waiting you may set up the project skeleton and content structure, never the styling. If the run is clearly unattended, pick sensible answers, state them at the top, and list the open questions at the end.
1. **Look first.** If there's an existing project, read its structure, stack and any `AGENTS.md` / `CLAUDE.md` / README, and match it. Don't restructure a working project unless asked.
2. **Decide and state** the category, tone, motion level, deliverable and stack in two or three lines, then build.
3. **Build** following `build-and-deliver.md`: real file structure, content in data files, visuals in their own components, output ready for the host you were given, or static output when none is known (`build-and-deliver.md` §3).
4. **Run it.** Install, build and serve. Fix build errors before calling anything done.
5. **Look at it.** If a browser is available, screenshot the **built output** at desktop (~1440px) and phone (~390px) widths, plus a reduced-motion pass. `scripts/screenshot.py` is a starting capture (initial desktop, phone and reduced-motion states, plus overflow, JS errors and an HTML validity hint); it doesn't scroll through chapters or click anything, so also inspect key scroll and interaction states yourself. Serve built sites over HTTP (e.g. `npx serve dist`) rather than `file://` when assets expect a base path. **Open and inspect the screenshots**, then fix concrete problems (clipped headlines, overlapping nav, broken assets, contrast, overflow) and re-shoot. Taking a screenshot without looking at it doesn't count.
6. **Test function**: main actions, copy/download contents, calculations and invalid inputs, keyboard path, and the main actions again **with reduced motion emulated**.
7. **Report**: what was built, where it lives, how to run and deploy it, what was checked, and what couldn't be (e.g. "no browser here, so not visually checked").

## Helper agents (optional)
Use them only if the tool exists and the session allows it. Good uses: building independent pages or sections in parallel, or an independent review pass against `review-checklist.md`. Give each one this skill's path and the decided category/tone/motion so the result stays one visual world. Never depend on them; the task has to be completable without them.

## Don't
- Don't promise work that continues after the session ends.
- Don't hotlink images from the web or copy the reference clips' assets.
- Don't add server code, API routes or server-side rendering unless the host supports them and the job needs them (`build-and-deliver.md` §3).
- Don't put the whole taste core into a project's `AGENTS.md`. That file is for project facts (run and build commands, conventions); this skill carries the taste.
