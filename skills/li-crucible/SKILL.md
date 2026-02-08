---
name: li-crucible
description: "Orchestrate the LinkedIn-Branding Li-Crucible workflow (4-lane: Ideator → Drafter → Editor → Publisher). Use when a user invokes /crucible parameters (d26/f27/dateYYYY-MM-DD) or @Li-Crucible phases, and you must produce publish-ready LinkedIn copy that follows repo law (Unicode-only, no em dashes, no fluff)."
risk: safe
source: self
---

# Li-Crucible (LinkedIn-Branding Orchestrator Skill)

This skill implements the **repo-specific** Li-Crucible workflow used by `LinkedIn-Branding/`.

It exists for one purpose: when a user types something like `/crucible d26` or `@Li-Crucible draft`, you route the work through the correct **4-lane pipeline**, enforce the repo's **hard constraints**, and ensure there is exactly **one canonical post body** in the correct directory.

## Authority & precedence (no drift contract)

When operating inside `LinkedIn-Branding/`, this skill defers to these files, in this order:

1. `LinkedIn-Branding/00_Context/LLM_Copilot.md`
2. `LinkedIn-Branding/PRD0_Crucible_Master.md`
3. `LinkedIn-Branding/00_Context/Project_Instructions.md`
4. `LinkedIn-Branding/00_Context/STYLE_GUIDE.md` / `VISUAL_STYLE_GUIDE.md`
5. Tracker: `LinkedIn-Branding/03_Final_Queue/CRUCIBLE_STATUS.md` (tracker only)

If any other Crucible guidance conflicts, it is **non-authoritative**.

## Command mapping (how to interpret user input)

### Parameter commands (what to do)

- `/crucible d{number}`
  - Example: `/crucible d26` → load `LinkedIn-Branding/01_Inputs/Day_026.md` (if it exists), otherwise offer to scaffold from template.

- `/crucible f{number}`
  - Example: `/crucible f27` → resolve to `FEB027` and find the best matching post folder/file (Draft/Ready/Shipped). If none exists, bootstrap a new post folder using campaign conventions.

- `/crucible date{YYYY-MM-DD}`
  - Example: `/crucible date2026-02-02` → run the full research gate, and if a post exists for that date, switch to **VET mode** by default.

### Routing commands (who does it)

- `@Li-Crucible ideate` → Phase 0 research + brief (mandatory when target day/date is specified)
- `@Li-Crucible draft` → Phase 1: write the post (technical density, systems truth)
- `@Li-Crucible edit` → Phase 2: polish and audit (voice, formatting, compliance)
- `@Li-Crucible publish` → Phase 3: ship prep (copy/paste block, image prompt, queue + archive updates)

**Rule**: `@Li-Crucible` selects the worker lane. `/crucible` provides structured parameters.

## Canonical file locations (do not invent paths)

Campaign-era canonical post body paths:

- Draft (WIP): `LinkedIn-Branding/2026/<MM-Month>/02.Drafts/**/<ID>_<Topic>/post.md`
- Ready: `LinkedIn-Branding/2026/<MM-Month>/03.Ready/**/<ID>_<Topic>/post.md`
- Shipped: `LinkedIn-Branding/2026/<MM-Month>/04.Shipped/**/<ID>_<Topic>/post.md`

Per-post recommended companion files:

- `research_pack.md` (structured memo + receipts)
- `research_notes.md` (raw research output)

**Editing rule (hard):**

1) If a post exists in both Draft and Ready, edit the Draft, then promote intentionally.
2) Never do parallel edits in two locations.
3) If multiple copies exist, stop and reconcile to ONE canonical file.

## Full research phase (required gates)

Run this phase when the user targets a **calendar date** or a **challenge day number**.

### Inputs to capture (ask if missing)

- Target: `calendar_date` OR `challenge_day_number`
- Topic hypothesis (1–2 sentences)
- Primary audience
- Desired outcome (engagement / authority / recruiting / lead)

### “Already shipped / already queued” gate (must check)

Check:

1. `LinkedIn-Branding/03_Final_Queue/CRUCIBLE_STATUS.md` (queued/scheduled)
2. `LinkedIn-Branding/04_Archive/metrics.csv` (published index)
3. `LinkedIn-Branding/04_Archive/**` (archived markdown)

If the target day/date appears as shipped/published or queued/scheduled, default to **VET mode**.

### Similarity scan (strict)

Before drafting a new post for a specific day/date:

- Compare against **at least the last 30 published posts** (prefer `metrics.csv` ordering).
- Provide **Top 5 most similar** with:
  - File path
  - Date/title (if available)
  - Why it’s similar (claim/frame/lesson/CTA)
  - Verdict: ALLOW or BLOCK

**BLOCK** if same core claim + same audience + same lesson/failure mode + similar hook/story beat.

If BLOCK, propose 3 alternative angles and re-scan against the closest items.

### Required research artifacts (must output)

1. Research memo (5–10 bullets)
2. Receipts list (2–6 sources; one-line why it matters)
3. Angle slate (3 angles): hook + tension + insight + proof
4. Not-a-repeat statement (2–3 sentences vs closest archived post)

Only after this is complete may you proceed to `draft`.

## Hard constraints for post text (copy/paste safety)

Inside the final LinkedIn copy block:

- **Unicode only** (LinkedIn does not render Markdown)
- Do **not** use: `#`, `*`, `**`, <code>```</code>, or Markdown headings
- **No em dashes**
- Avoid filler words: delve, unlock, unleash, elevate, landscape, game-changer
- Default: no inline links. Put citations into a top comment “Receipts” bundle unless requested.

Target:

- 150–240 words (hard max 260)
- One action max (default no CTA)

## Output contract (what “done” looks like)

When asked to produce a post, output:

1. **Ready-to-copy post body** (Unicode formatting only)
2. Optional **top comment: Receipts** bundle
3. **Image prompt** that follows `VISUAL_STYLE_GUIDE.md` requirements (no logos, no text overlays)
4. **Where it lives**: the canonical path you wrote/updated
5. **Next lane trigger**: what should happen next (`ideate:READY`, `draft:COMPLETE`, `edit:APPROVED`, `ship:PUBLISHED`)

## Helpful automation hooks

If you are in VS Code with this workspace, there is a task named:

- `Li-Crucible: Bootstrap (prompted)`

Use it when you need to bootstrap a day folder, locate the canonical file, or prompt for missing intake fields.
