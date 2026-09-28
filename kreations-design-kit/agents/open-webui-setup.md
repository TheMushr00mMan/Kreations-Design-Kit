# Setting up kreations-design-kit in Open WebUI

Checked against the Open WebUI docs in September 2026 (Skills, Knowledge, Artifacts pages). Menu names can change between versions; if something doesn't match, check `docs.openwebui.com`.

## Which file to use
| Model | Use | Size |
|---|---|---|
| Strong model (cloud, or a large local model) | `SKILL.md` (full) | about 6–7k tokens |
| Small local model, or a short context window | `lite/kreations-design-kit-lite.md` | about 1–1.5k tokens |

Rule of thumb, not a hard line: if the model struggles to follow long instructions or its context is under ~16k tokens, use the lite file. Leave room for the answer too: a full HTML page is often 5–10k tokens by itself.

Open WebUI imports a skill as **one Markdown file**. The `references/` folder doesn't come along. That's fine: SKILL.md is written to work on its own. If you want the Open WebUI-specific behaviour spelled out, paste `references/modes/open-webui.md` under it in the system prompt (Option B).

## Option A: as an Open WebUI Skill (best for models with native function calling)
1. **Workspace → Skills → Import** and pick `SKILL.md` (or the lite file). The name and description fill in from the frontmatter.
2. **Workspace → Models → edit your model → Skills:** tick `kreations-design-kit`, save.
3. In the same model's advanced settings, set **Function Calling** to **Native**. Only the skill's name and description sit in the prompt; the model loads the full text with `view_skill` when a design request comes in. **Without native function calling the model only sees the name and description and can't load the rules**, so use Option B instead.

## Option B: always on (best for small local models)
- **System prompt:** Workspace → Models → edit → paste the lite file (or full SKILL.md) into the **System Prompt**. Every chat with that model follows it.
- **Per chat:** import the file as a Skill, then type `$` in the chat box and pick it. Its full content is injected for that message.

## Optional: the reference files
If you want the font library, palettes or moves available, create a **Knowledge** base with `references/fonts.md`, `references/palettes.md` and `references/moves.md` and attach it to the model. Keep it on the default focused retrieval (only the relevant chunks get pulled in); full-context mode would push all of them into every message. With native function calling, the model has to search the knowledge base itself, so mention it in the system prompt: "For font, palette or move choices, search the Kreations design knowledge base."

## Seeing the result
- Ask for "one HTML file". Open WebUI's **Artifacts** panel previews a complete HTML page (HTML + CSS + JS in one block) or an SVG.
- The preview is a sandboxed frame. Depending on your admin settings (`IFRAME_CSP`, "Allow Same Origin"), outside requests like web fonts or CDN libraries may be blocked. If fonts look wrong in the preview, save the HTML and open it in a normal browser, or ask for system fonts only.
- The skill tells the model to say "not visually checked": it can't see the preview itself.
