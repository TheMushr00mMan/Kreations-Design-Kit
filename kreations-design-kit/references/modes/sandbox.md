# Mode: chat with a sandbox

You can write files and run some code in a temporary environment (e.g. Claude.ai with code execution, ChatGPT with Python), but there's usually no persistent project, no long-running server and no helper agents. Check each action before promising it.

## Do
- **Brand questions first** (SKILL.md §0.5): if there's no brand and the request is thin, ask up to 5 short questions plus 2–3 style directions, then wait for the answer before building.
- **Check the runtime you need:** Python doesn't mean Node, and a file tool doesn't mean a browser. Check network and package access before planning a build that needs them.
- **Single file:** write it to disk and deliver it the way the host supports (a published artifact, a download link, a file card). In Claude.ai artifacts, remote images and form posts don't work, so use code-built visuals or marked slots, and copy/download forms.
- **Multi-file project:** write the real file structure and **zip it for download**, with a README (run, build, deploy to the host you were given, or any static host). If Node and npm are available and allowed, run the build and say it passed. If not, say "packaged, not built or tested here".
- **Documents:** produce the requested format (PDF, DOCX…) with the host's tools, then open or inspect the result if you can (e.g. render a page to an image and look at it).
- **Visual check:** if you can render the page (e.g. a headless browser) *and* view the screenshot, check it at desktop and phone widths and fix what you see. Otherwise, say it wasn't visually checked.

## Don't
- Don't promise helper agents, background work, or anything that survives after the reply.
- Don't claim "built" or "tested" for something you only packaged.
- Don't leave the user with only a sandbox path. Hand the file over through the host's delivery method.
