# Kreations Design Kit

**An art director for AI builds.** Install it in Claude, ChatGPT, Codex or a local-model app, and whenever you ask for a website, a tool, a designed document or a slide deck, your assistant designs it with a clear point of view instead of a generic template.

Made by Karsten Locano · Kreations.

## What it does
- **Websites, landing pages and portfolios** get:
  - one strong focal idea;
  - big-against-small type;
  - one coherent visual world;
  - short copy;
  - motion that fits your words ("showy", "clean", or nothing said).
- **HTML tools and calculators** open in a realistic working state, with correct maths, a live total, a visible breakdown and honest example values.
- **Designed documents** (one-pagers, reports, guides) feel like one cohesive, premium piece.
- **Slide decks** are matched to the kind of deck (client, pitch, talk or creative launch). Motion suits the context, and fonts open on any Windows or Mac.
- **Colour** never comes from one fixed palette. The kit has contrast-checked shortlists for 15 kinds of project, from finance to food to events, and names the alternatives it didn't pick.
- **Brand first, facts only.** Your logo, colours and content win. It asks before guessing and never invents prices, hours, reviews or results.

See [`kreations-design-kit/START-HERE.md`](kreations-design-kit/START-HERE.md) for what to expect and how to get the best results.

## Install
Download the latest release from the **Releases** page on the right. There are three files:

| File | Use it for |
|---|---|
| `kreations-design-kit.skill` | Claude apps (upload) |
| `kreations-design-kit-v1.1.0.zip` | Claude Code, Codex, ChatGPT (the skill folder, zipped) |
| `kreations-design-kit-lite.md` | Open WebUI, LM Studio and small local models (paste into the system prompt) |

Step-by-step for each app: [INSTALL.md](INSTALL.md).

## What's inside
```
kreations-design-kit/
├─ SKILL.md              the main rules (works on its own)
├─ START-HERE.md         a short guide for you, the human
├─ personal.example.md   template for your own add-on
├─ references/           deeper guides: websites, tones, moves, fonts, palettes, slides, tools & documents, checks
├─ lite/                 condensed version for small models
├─ scripts/              pptx_motion.py (adds transitions to PowerPoint files), screenshot.py (check screenshots)
├─ agents/               metadata for OpenAI apps, Open WebUI setup notes
└─ assets/palettes/      palette swatches
```

## Make it yours
Copy `personal.example.md` to `personal.md` inside the skill folder and fill it in: who you are, where you host, your own rules. The kit reads it first. In apps that load a single file (Open WebUI, ChatGPT Projects, system prompts), paste it under SKILL.md instead.

## Licence and credit
- The kit's written content is **CC BY 4.0**: use it, share it and adapt it for anything, including client and commercial work, as long as you credit **"Kreations Design Kit by Karsten Locano"** and link back here.
- The scripts in `scripts/` are **MIT**.

See [LICENSE](LICENSE) and [LICENSE-CODE](LICENSE-CODE).

## Feedback
Found something it gets wrong? Open an issue with your prompt, the app and model you used, and what came back.
