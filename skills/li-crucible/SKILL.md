---
name: li-crucible
description: "Initiate and run the 3.LinkedIn-Branding Li-Crucible pipeline (canonical 4-lane: Ideator -> Drafter -> Editor -> Publisher) from shorthand IDs like /li-crucible f27 (aka /crucible), including ID resolution, bootstrap/scaffolding when missing, and canonical-path + copy/paste compliance."
metadata:
  version: 1.0.0
  author: Codepro Workspace
  created: 2026-02-13
  updated: 2026-02-28
  platforms: [vscode]
  category: workflow
  tags: [linkedin, crucible, li-crucible, branding, pipeline, research, plot-gate]
  risk: safe
---

# li-crucible

> `{F}` marks a breakage-driven guardrail added after bakeoffs, quota incidents, or live workflow failures.

## {F} ⚡ PRIME DIRECTIVE: Start the Dashboard

Nothing else happens until the Crucible dashboard is live. This is your **first action, every time**, before ID resolution, scaffolding, or any lane work.

1. **Start the dashboard** from `3.LinkedIn-Branding/`:
   ```bash
   python scripts/deploy_crucible.py
   ```
   This kills stale processes, starts the server on port 8000, and launches the daemon.
   Fallback: `python scripts/dashboard/server.py --port 8000`

1.1 **Browser target is Windows Edge only (real Edge).**
   - Never use Linux Edge/Chromium for Crucible dashboard actions.
   - Do not use `--open` from WSL/Linux shells (it can open a Linux browser target).
   - Launch dashboard UI explicitly in Windows Edge:
   ```bash
   powershell.exe -NoProfile -Command "Start-Process msedge.exe 'http://localhost:8000'"
   ```

2. **Verify alive** — `GET http://localhost:8000/api/bus` must return JSON with a fresh heartbeat (`Crucible-Daemon.last_heartbeat` within ~15s).

3. **Run the enforcer gate** before each lane:
   ```bash
   python scripts/dashboard_enforcer.py --topic <MISSION_ID> --agent <AGENT_ID>
   ```
   Exit 0 = proceed. Non-zero = **STOP. Fix the dashboard. Resume from last completed artifact.**

4. **Re-run the enforcer** between every lane transition (LI1→LI2, LI2→LI3, LI3→LI4).

If the dashboard is not running, **do not start any lane work**. All lane completions must register as green checks on the dashboard. Skipping this step is a critical violation.

## {F} ⛔ BAKEOFF HARD GATES (Permanent — Never Skip)

These hard gates were added after a controlled bakeoff proved ALL agents (AntiGravity, Copilot, Codex) violated them. They are non-negotiable hard blocks.

### {F} Gate 1: Dashboard Status Emission
At the START of each lane, emit status BEFORE any work:
```bash
python scripts/log_event.py --agent "<AgentName>" --type "system" --content "<lane>:IN_PROGRESS" --stage <stage> --topic <MISSION_ID>
```
**ALWAYS include `--stage` and `--topic` on every `log_event.py` call.** Missing flags cause events to land in the wrong dashboard checklist bucket (e.g., INTAKE shows open when it shouldn't). Stage values: `ideate`, `draft`, `edit`, `ship`. Example:
```bash
python scripts/log_event.py --agent "LI2" --type "system" --content "draft:IN_PROGRESS" --stage draft --topic FEB028
```
If you don't emit status, the dashboard shows stale/wrong state. This is a critical violation.

### {F} Gate 2: Input Bootstrap (create 01_Inputs/<ID>.md)
Before LI1 starts, create `01_Inputs/<ID>.md` (e.g., `01_Inputs/FEB017.md`) containing at minimum: topic name (from Syllabus Tracker), day number, week, category, hook/concept. If this file doesn't exist after LI1 completes, the run is INVALID.

**⚠️ Input File Validation (MANDATORY):** If `01_Inputs/<ID>.md` already exists, cross-validate the `topic_name` field against the Syllabus Tracker entry (`2026/02-February/00.Governance/Syllabus_Tracker.md`) for that day. If the topic_name doesn't match the Tracker's topic column, the file is STALE from a previous run — recreate it with the correct topic. Do NOT reuse mismatched input files.

### {F} Gate 3: Separate Research Files (never embed)
LI1 MUST produce TWO separate standalone files in the post folder:
- `research_notes.md` — raw Perplexity output with citations
- `research_pack.md` — structured memo + receipts mapping
Do NOT embed research inside the ideation brief or post.md. Missing research files = INVALID run.

### {F} Gate 4: Plot Gate — Exactly 3 Plots Required
LI2 MUST propose EXACTLY 3 plot options in `plot.md`. Each plot needs: Character (from Characters.md), Location (from VISUAL_STYLE_GUIDE.md), Action (verb phrase), Symbol (object). Fewer than 3 plots = INVALID. Do not proceed to image prompt assembly.

### {F} Gate 5: Image Generation Must Complete
LI4 MUST produce at least one image file (PNG/JPG/WEBP). Copilot/Codex use Track B API single-shot. Gemini uses Track A native (max 2) then Track B fallback. Do NOT claim `publish:READY` without a verified image file on disk. If generation fails, set `art_status: "IMAGE_PENDING"` and report explicitly.

### {F} Gate 6: 4-Block Image Prompt Format
The stitched image prompt in `plot.md` MUST use exactly 4 blocks:
1. SUBJECT — Golden Prompt verbatim from Characters.md (never invent traits)
2. SCENE — Environment + Action + Object from the selected Plot
3. STYLE — Locked (copy from ART_PROMPT_ASSEMBLY.md Section 3 verbatim)
4. NEGATIVE — Universal bans + character-specific bans + scene hygiene bans (`grime, dirt, debris, cable spaghetti, messy workstation`)
Any prompt missing blocks or using a different format is INVALID.

### {F} Gate 7: No Manual Telemetry Hacks
NEVER create temporary scripts (`temp_*.py`, `hack_*.py`, ad-hoc emitters) to work around telemetry. Use ONLY existing scripts: `scripts/log_event.py`, `scripts/crucible_telemetry.py`, `scripts/dashboard_enforcer.py`. Creating workaround scripts = CRITICAL VIOLATION.

### {F} Gate 8: Pipeline Continuation — NEVER Stop Between Lanes
A lane signature (`ideate:READY`, `draft:COMPLETE`, `edit:APPROVED`) is NOT a stop signal. It means "immediately start the NEXT lane." The ONLY valid stopping point is `publish:READY` (end of LI4). If you complete LI1 and stop without starting LI2, that is a CRITICAL VIOLATION — the user gets no post and no image. After each lane signature, you MUST:
1. Emit the next lane's `<lane>:IN_PROGRESS` status
2. Begin the next lane's work immediately
3. Continue until `publish:READY` or until truly blocked (missing API key, image gen failure, etc.)
If you hit a resource limit, explicitly say "pipeline incomplete at LI{N}" — never silently stop.

**{F} ⚠️ KNOWN FAILURE: LI3→LI4 handoff**: Testing shows agents consistently stop after `edit:APPROVED` without starting LI4. This is the MOST CRITICAL handoff. After `edit:APPROVED`, you MUST immediately emit `publish:IN_PROGRESS` and begin LI4 work (image generation, branding, format verification). Do NOT summarize, do NOT return to user, do NOT stop.

**{F} ⚠️ STALE HEARTBEAT RECOVERY**: If the enforcer fails at a lane boundary due to a stale heartbeat (not a mission mismatch), this is a recoverable infrastructure issue, NOT a pipeline error. Restart the dashboard (`python scripts/deploy_crucible.py`) and re-run the enforcer. Do NOT treat a stale-heartbeat failure as a hard stop. Long-running sessions (30+ minutes) will frequently encounter stale heartbeats between lanes.

### {F} Gate 9: Golden Thread Synthesis (Pre-Generation Check)
Before LI4 image generation, the prompt thread MUST be synthesized from:
1. Golden character prompt (`2026/02-February/00.Governance/Characters.md`)
2. Selected plot SCENE from `plot.md`
3. Locked STYLE anchors from `00_Context/ART_PROMPT_ASSEMBLY.md` / `00_Context/VISUAL_STYLE_GUIDE.md`
4. Universal + character-specific NEGATIVE bans, including anti-horror bans and scene hygiene negatives (`grime, dirt, debris, cable spaghetti, messy workstation`)

If the synthesized thread is missing required character locks or style anchors, STOP and fix `plot.md` before generation.

### {F} Gate 10: Branding Proof Required Before `publish:READY`
LI4 cannot complete on image existence alone. After running `scripts/branding.py`, emit explicit proof telemetry:
```bash
python scripts/log_event.py --agent "LI4" --type "result" --content "Branding applied to image for <ID>" --stage ship --topic <ID>
```
If this branding-proof event is missing for the active mission, treat branding as incomplete and do NOT emit `publish:READY`.

### {F} Gate 11: Weakest-Link Every-Pass Gate (Mandatory Improvement)
On every lane pass (including retries and handoff passes), run a second pass before continuing:
1. Score sections on a 1-5 rubric: Hook, Clarity, Specificity, Flow, CTA.
2. Rank sections from weakest to strongest.
3. Improve the weakest section with a concrete rewrite (or explicitly justify a tied weakest set and improve one of them).
4. Emit evidence via telemetry (include section name + what changed).

If the pass does not produce measurable improvement, the pass is incomplete and cannot proceed.

For any second-agent or `mode=VETTING` pass, the rubric must also score every dashboard checklist item for the target lane on a 1-5 scale, rank checklist items from weakest to strongest, and improve at least the lowest-rated item before sign-off. The `VETTING_REPORT` must include `checklist_scores`, `weakest_step`, `weakest_score`, and `improvement_applied`.

### {F} Gate 12: Lane State Persistence (Session Resume)
After each lane signature, persist completion state for crash/session recovery:
```bash
python -c "from lane_state import mark_lane_complete; mark_lane_complete('<TOPIC>', '<LANE>', '<SIGNATURE>')"
```
Examples: `mark_lane_complete('FEB028', 'LI1', 'ideate:READY')`, `mark_lane_complete('FEB028', 'LI4', 'publish:READY')`.

On resume (new session or interrupted run), check where to continue:
```bash
python -c "from lane_state import find_resume_point; print(find_resume_point('<TOPIC>'))"
```
Returns `LI1`–`LI4` (next lane to run) or `""` (all complete). This prevents re-running completed lanes or skipping uncompleted ones.

### {F} Gate 13: Minimum Character Count
The copy-paste LinkedIn text (from hook line through hashtags) MUST be ≥ 2,800 characters. LI2 must hit this floor before signing `draft:COMPLETE`. LI3 must verify the count before signing `edit:APPROVED`. If under 2,800, expand with more data points, examples, or rhetorical depth. Target range: 2,800–3,200 chars.

---

## Purpose (Secondary)

Provide a **single entrypoint** to initiate and run the **3.LinkedIn-Branding** Li-Crucible workflow from shorthand identifiers (e.g., `f27`, `FEB027`, `Day_026`, `dateYYYY-MM-DD`).

This skill is meant to stop workflow drift by always routing to the repo-canonical process.

## Source of truth (must win)

- Primary (router + gates): `3.LinkedIn-Branding/.agent/skills/li_crucible/SKILL.md`
- Orchestrator prompt (bootstrap + research gate): `Agent-Resources/skills/li-crucible/CRUCIBLE_ORCHESTRATOR_PROMPT.md`
- Repo law + campaign rules:
  - `3.LinkedIn-Branding/00_Context/LLM_Copilot.md`
  - `3.LinkedIn-Branding/PRD0_Crucible_Master.md`
  - `3.LinkedIn-Branding/00_Context/Project_Instructions.md`
- Conveyor overview: `3.LinkedIn-Branding/.agent/workflows/Li-Crucible.md`
- Lane specs:
  - `3.LinkedIn-Branding/.agent/agents/LI1.LinkedIn-Ideator.agent.md`
  - `3.LinkedIn-Branding/.agent/agents/LI2.LinkedIn-Drafter.agent.md`
  - `3.LinkedIn-Branding/.agent/agents/LI3.LinkedIn-Editor.agent.md`
  - `3.LinkedIn-Branding/.agent/agents/LI4.LinkedIn-Publisher.agent.md`

## What “run Li-Crucible” means

Canonical conveyor (no skips):

1) **LI1 Ideator** → `ideate:READY`
2) **LI2 Drafter** → `draft:COMPLETE` (includes Plot Selection Gate + stitched 4-block image prompt + `plot.md`)
3) **LI3 Editor** → `edit:APPROVED`
4) **LI4 Publisher** → `publish:READY` (image generated + branding applied; post stays in `03.Ready` until user confirms LinkedIn publish)

## How to invoke (user-facing)

- Chat triggers:
  - `/crucible f27`
  - `/li-crucible f27`
  - `@Li-Crucible f27`
  - `@Li-Crucible date2026-02-14`

- VS Code task (if you prefer prompted bootstrap):
  - `Li-Crucible: Bootstrap (prompted)`

## Initiate (bootstrap) checklist

Use this when the user’s intent is “start crucible for f##/FEB###/date…”, and you need to locate (or create) the correct canonical file before running lanes.

1) Work from the correct repo root:
- If you are about to run scripts, run them from `3.LinkedIn-Branding/` so relative paths like `scripts/log_event.py` work.

2) Observability (covered by PRIME DIRECTIVE but repeated for clarity):
- Dashboard server must be alive before any lane work (see PRIME DIRECTIVE above).
- **Single-instance rule**: run **one** dashboard server per port. Multiple/stale servers can cause the UI to show a flashing/broken image icon even when `/api/bus` is healthy.
- Event logging: `python scripts/log_event.py --agent "Codex" --type "thought" --content "..."` (types: `thought`, `tool`, `result`, `error`, `system`)
- Telemetry contract: `3.LinkedIn-Branding/.agent/TELEMETRY_CONTRACT.md`

3) Normalize the user token to a canonical ID:
- `f27`, `feb27`, `FEB27` -> `FEB027`
- `d26` -> try `Day_026`, then `FEB026` (legacy)
- `dateYYYY-MM-DD` -> use the date as the target selector (default to VET mode if any matching post exists)

3.1) **Do NOT ask for a topic hypothesis for February fNNN runs** (unless the user wants an override):
- For the Feb 2026 campaign, the day-by-day topic slate already exists in:
  - `3.LinkedIn-Branding/2026/02-February/00.Governance/Syllabus_Tracker.md`
- If the resolved ID is `FEB###`, load the row for that day to get:
  - Topic name
  - Hook / Concept
- Only ask the user for brief inputs if:
  - the syllabus row is missing, OR
  - the user explicitly wants to change the topic/audience/outcome.

4) Locate the canonical post file (prefer existing; do not fork copies):
- Draft (WIP): `3.LinkedIn-Branding/2026/<MM-Month>/02.Drafts/**/<ID>_<Topic>/post.md`
- Ready (review): `3.LinkedIn-Branding/2026/<MM-Month>/03.Ready/**/<ID>_<Topic>/post.md`
- Shipped (audit record): `3.LinkedIn-Branding/2026/<MM-Month>/04.Shipped/**/<ID>_<Topic>/post.md`
- Hard rule: if both Draft and Ready exist, edit Draft first, then promote intentionally; never parallel-edit multiple locations.
- Hard rule: never edit Shipped; ship a new revision intentionally via Draft/Ready.

5) If nothing exists, scaffold (minimal, non-drifting):
- Use the month templates under `3.LinkedIn-Branding/2026/<MM-Month>/01.Templates/` (Draft + Ready templates exist for February 2026).
- Create a new folder under `3.LinkedIn-Branding/2026/<MM-Month>/02.Drafts/<Week_#>/<ID>_<Topic>/` with `post.md`.
- Also create `plot.md` in the same folder (Plot Selection Gate requires it).

6) Then run lanes sequentially (no skips):
- LI1 -> LI2 -> LI3 -> LI4 (each lane must earn its signature and pass the Requirements Coverage Gate).

## Key guardrails

- **{F} No drift**: Draft in `2026/**/02.Drafts/**/post.md`, then promote to Ready in `2026/**/03.Ready/**/post.md` intentionally.
- **Plot auto-vote**: propose 3 Plots → use an OpenAI “harsh critic” judge when available, otherwise apply a fallback rubric (clarity, resonance, series fit) → record `selected_plot` + `selection_method` in `plot.md`.
- **Research artifacts**: when research is required, ensure `research_pack.md` and `research_notes.md` exist.
- **Human Spark Layer**: LI2 drafts and LI3 verifies one lived-in observation, 1-2 dry lines, and one sincere line that shows care for the humans affected by the problem. Use 1-4 emojis only as rhythm markers. Do not let the post turn into either a comedy sketch or a trauma diary.
- **Image two-track protocol**: Gemini/AntiGravity agents try native `generate_image` first (max 2 attempts), then fall back to API (`generate_image.py --provider openai`, single-shot). Copilot/Codex agents go directly to API (single-shot). Total worst-case: 3 calls per post (2 native + 1 API). See `ART_PROMPT_ASSEMBLY.md` Section 0.1.
- **{F} Runaway spend guard**: for repeated topic triggers, use `max_retries: 0` by default, respect per-topic trigger/run guards, and never bypass guard blocks unless the user explicitly approves.
- **{F} Windows Gemini CLI failure rule**: if `[WinError 193]` appears, stop retriggers immediately and fix executable resolution (`gemini.cmd`/`.exe`/`.bat`), then retry once.

## Troubleshooting: “skill not showing up”

This workspace defines skills under `.github/skills/`.

Note: a repo skill file does not automatically add a `/li-crucible` slash command to Copilot Chat’s `/` menu. That menu is populated by VS Code + installed extensions. For a reliable local command/participant, see `00.Active/Tools/vscode-li-crucible-chat/README.md`.

Some Copilot skill loaders only recognize **globally installed skills**. If it still doesn’t appear, copy/link this folder into your global skills directory and reload the window:

- Windows (common): `%USERPROFILE%\.copilot\skills\li-crucible\`
- WSL/Linux/macOS (common): `~/.copilot/skills/li-crucible/`

If you tell me *where* you expect it to appear (Copilot Chat UI, CLI, etc.), I can give the exact “rescan” steps for that environment.

## Process Memory Update

**The "Auto-Quarantine Duplicate Folder" Trap**
- *The Error*: Keeping duplicate mission folders with the same `<month>/<week>/<folder>` shape in both `02.Drafts` and `03.Ready` while the dashboard is polling `FEB###`.
- *The Impact*: `scripts/dashboard/server.py` can auto-quarantine the lower-priority duplicate, causing an active Draft folder to disappear mid-lane.
- *The Fix*: Before lane work, ensure only one active folder name per mission across Draft/Ready for the same week. If both must exist temporarily, avoid same-name duplicates until promotion is complete, then normalize to one canonical location.

**The "Dual-Folder Topic Collision" Trap** (FEB028 Thread)
- *The Error*: A topic ID (e.g., `FEB028`) already has a shipped post in `FEB028/` (old topic), but the current run creates `FEB028_Graduation/` (new topic). Both folders match the `FEB028` topic prefix.
- *The Impact*: `_find_latest_post_for_topic` and the dashboard may resolve to the WRONG folder (old shipped post instead of new draft).
- *The Fix*: When a topic ID already has a shipped post in a separate folder, verify which folder the dashboard picks by checking `/api/post_raw?topic=FEB028`. If it picks the wrong one, rename or move the stale folder to avoid prefix collision.
