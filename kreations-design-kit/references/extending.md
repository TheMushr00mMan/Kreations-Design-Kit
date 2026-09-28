# Extending this skill

New example sites can be added over time. The skill is built so that adding examples means adding entries, not rewriting the core.

## Adding new reference sites

**Input:** links (live sites) and/or videos (concepts), ideally with one line each on what you like about it. Slide decks (images or files) go in the `sXX` series and feed `slides.md` §4.

1. **Analyze each one on its own first**, using the same neutral headings: job; structure section by section; typography; color; components; motion and interaction (with high/low confidence); copy voice; imagery; persistent UI; the cues worth taking; cautions.
   - Separate what's **seen** from **guesses about how it was built**.
   - Never record numbers from a moving frame as facts.
   - For live sites, read real values (fonts, colors, spacing) from the page, but still describe cues, not copies.
   - For videos, pull frames (e.g. `ffmpeg -i clip.mp4 -vf "fps=3,scale=900:-1" f_%03d.jpg`) and compare neighbouring frames to infer motion.
2. **Propose where each fits**, in this order of preference:
   1. An existing category + tone (a new example in `examples/clips.md`)
   2. A new move in `moves.md`
   3. A new tone or flavor, only if its feel doesn't fit any existing tone
   4. A new category, only if it has **a different job and a different page structure**. A different feel is a tone, not a category.
3. **Get the owner's OK** before changing the rules (whoever maintains this copy).
4. **Update the files:** add the entry to `examples/clips.md` (next ID, e.g. v23) and, if you keep stills locally, the keyframe to `assets/keyframes/`, then touch `websites.md`, `tones.md` or `moves.md` only where the evidence changes something. Update counts ("seen in N of M") if you cite them.
5. **Bump the version** in `CHANGELOG.md` with a one-line summary.
6. **Re-test** with a couple of representative prompts before repackaging.

## Changing preferences

- A new dislike goes in the **Dislikes** section below, and anywhere it contradicts a move or option.
- A changed default (motion, imagery, stack, hosting) goes in SKILL.md and `build-and-deliver.md`, and gets a changelog entry.

## Dislikes

*(Nothing yet. Add entries as they're flagged, e.g. "tiny labels under 12px", with the date.)*

## Entry template for `examples/clips.md`

```
## vNN: Working name
- **Category:** …
- **Tone:** …
- **Job:** what the visitor should do, and the evidence
- **Seen:** what's clearly visible (structure, type, color, motion)
- **Lesson / cues:** what to take into new work
- **Use when:** the asks or vibes this reference is for (references are situational, not defaults)
- **Cautions:** H/X status, low-confidence reads, things not to copy
```

IDs: `vNN` for videos (concepts), `nNN` for live sites.
