# Install the Kreations Design Kit

The skill is named **`kreations-design-kit`**. Menus below were checked in September 2026 and can change between app versions.

## Claude apps (web, desktop, mobile)
1. Turn on **Settings → Capabilities → "Code execution and file creation"**. On Team and Enterprise plans an admin controls this.
2. Go to **Customize → Skills → + → Create skill → Upload a skill**, and choose `kreations-design-kit.skill`.
3. Just ask for a site, tool, document or deck. Claude loads the kit when the request fits.

## Claude Code
1. Unzip `kreations-design-kit-v1.0.0.zip` and place the folder at `~/.claude/skills/kreations-design-kit/`, so `SKILL.md` sits directly inside it. For one project only, use `.claude/skills/kreations-design-kit/` in the repo instead.
2. It's picked up live. If the skills folder didn't exist when Claude Code started, run `/reload-skills` once.
3. Use it automatically, or type `/kreations-design-kit`.

## ChatGPT
**ChatGPT Work, on the web:**
- Open **Skills**, upload `kreations-design-kit-v1.0.0.zip`, then type **@** in a chat to pick the kit.

**ChatGPT Work, in the desktop app:**
- The desktop app keeps its own skill list, so install the kit there separately.
- Start a Work session, attach the zip, and say: *"Please install this skill."*

**No Skills option?**
- Skill uploads depend on your plan and workspace settings. If you don't see them, use a **Project** instead:
  1. Create a project and open **••• → Project settings**.
  2. Add this instruction: *"For any website, HTML tool, designed document or slide deck, follow SKILL.md in this project's files exactly."*
  3. Upload `SKILL.md` as a project file.

**Tip:** full sites come out better on a higher reasoning setting. Light works, but it checks its own work less.

## Codex (CLI, IDE extension, app)
1. Place the folder at `$HOME/.agents/skills/kreations-design-kit/`, or at `.agents/skills/kreations-design-kit/` inside a repo.
2. Type `$kreations-design-kit`, or let Codex choose it. `/skills` lists what's installed.

## Open WebUI
- **Strong model:** import `SKILL.md` via **Workspace → Skills → Import**, tick it on your model, and set **Function Calling → Native**.
- **Small model:** paste `kreations-design-kit-lite.md` into the model's **System Prompt** instead.

Full notes are in `kreations-design-kit/agents/open-webui-setup.md`.

## LM Studio, AnythingLLM, Jan and other local apps
1. Paste the lite file (small models) or `SKILL.md` (strong models) into the system prompt. In LM Studio, save it as a Preset.
2. Ask for "one HTML file", save the reply as `.html`, and open it in a browser.

## Updating
- **Claude Code and Codex:** replace the folder.
- **Claude app and ChatGPT:** upload the new file again.
- **Local apps:** paste the new file again.

What changed is listed in `CHANGELOG.md`.
