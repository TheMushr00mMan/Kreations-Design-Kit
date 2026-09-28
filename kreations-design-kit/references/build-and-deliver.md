# Build and deliver

## 1. Deliverable: the explicit request first

| They say | Deliver |
|---|---|
| "one HTML file", "single file", "quick", "mockup", "artifact" | One **self-contained** file: CSS and JS inline, visuals built in code or embedded, no supporting files, no dependency that silently breaks offline. A pinned library from a CDN is acceptable only if the host allows it and you say so. |
| "build it properly", "so it lasts", "easy to edit / revise", "real site", "repo" | A **real project**: pages, components, styles, assets and data in separate files, with a README saying how to run and deploy it. |
| a file format ("PDF", "Word doc", "slides") | That format. Choose it before any web defaults. Decks: .pptx master plus a PDF, see `slides.md`. |
| nothing specific | Decide from how much it'll need revising, the number of pages, asset weight and interactivity, then state the choice in one line. Chat leans toward a single file. In an existing repo, match its stack and structure. In an empty folder, sites become projects; one-off tools and documents can be single files. |

If the host can't produce what was asked (e.g. a multi-file project in plain chat), say so and give the closest real thing: complete files in the reply, or a zip if you can write files. Never claim you saved or built something you didn't.

**"Packaged" is not "built and tested".** Only say a project runs if you ran it.

**Valid HTML:** every script and element sits inside `<html>`; nothing after `</html>`. Some hosts drop anything outside it.

**Chat artifacts** (e.g. Claude.ai): supporting files (separate JS, CSS, images) can fail to load in some browsers, so deliver one fully self-contained file with fonts and images inlined where you can.

## 2. Stack (per project)

| Situation | Default |
|---|---|
| Existing project | **Its stack.** Don't rebuild a working site to match a preference. |
| Small site, 1–3 pages, little shared structure | Plain HTML / CSS / JS, no build step |
| Content site that needs to last (several pages, reusable sections, a blog or projects list) | **Astro** (static output) |
| Tool or app with linked controls and changing state | **React + Vite** (static build) |

- Motion alone doesn't justify React. Start with CSS, add **GSAP** for coordinated or pinned timelines, and **Three.js** only when real 3D earns its weight.
- Keep content (project lists, services, prices, copy) in data files or content collections so they can be edited without touching layout code.
- Keep visuals in their own components or files so they can be swapped later.

## 3. Hosting

- **Follow the host you're given:** the request, the existing project (config files, deploy workflows) or `personal.md`. Use that platform's conventions (Vercel, Netlify, Cloudflare Pages, GitHub Pages, a server, a site builder).
- **No host known:** default to **static output** (plain files or a static build) that runs anywhere, and say so in one line. Add server code, server-side rendering or API routes only when the host supports them and the job needs them.
- **If deploying to GitHub Pages** (optionally behind Cloudflare):
  - static files only;
  - set the correct **base path** (Astro `site`/`base`, Vite `base`): usually `/` on a custom domain, `/repo/` for `username.github.io/repo`; if unsure, ask or leave a clearly commented setting;
  - include a GitHub Actions workflow for Pages when there's a build step;
  - make direct visits and reloads work on every route (a `404.html` where needed).
- **Everywhere:** use relative or base-aware asset paths, and verify them in the **built** output, not just the dev server.

## 4. Forms and hand-offs

- **Contact / "start a project"**: produce a brief to copy or download, and show the same text on screen as selectable text. On a hosted site, an outside form service is fine if the user names one (leave a clearly marked config spot). Never fake "sent".
- **Search, filters, calculators** run locally.
- In chat artifacts, remote images and form submissions usually don't work: build visuals in code or use marked slots, and use copy/download.

## 5. Images and assets

- **"I have images"** → marked slots: a sized box with an aspect ratio and a label such as `[Your photo: team at work, 4:5]`, styled to fit the design, plus a clear place to put the file.
- **"No visuals"** → none.
- **Otherwise** → code-built visuals (CSS gradients, SVG, canvas or WebGL) that suit the subject.
- Never hotlink random images from the web or reuse the reference clips' images.

## 6. Fonts

- Choose from `fonts.md` (free fonts only; paid ones are named only in your finishing note).

- **Self-contained file:** embed the fonts (subset data URIs) when size allows, or use a web-font link with a fallback stack you've actually looked at. Say which.
- **Project:** self-host the fonts (e.g. `@fontsource` packages or files in the repo) rather than depending on a third-party font CDN.
- **Documents / PDF:** embed the fonts in the output.
- **Editable Office files (PPTX, DOCX, XLSX):** no-install fonts by default, custom only when asked or approved (`slides.md` §6).
- The fallback must still look deliberate; check it if you can.

## 7. Reduced motion

The reduced-motion version must stay **complete and interactive**: swap movement for instant or faded changes, but keep every click, drag, toggle, menu, filter and 3D control working and every scene reachable (as a still or a step). Don't freeze the page or skip attaching event listeners. Test it by turning reduced motion on and clicking through the main actions.
