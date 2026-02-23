# Agent Context for AntiGravity
**Location:** Windows — `C:/Users/nymil/Codepro/AntiGravity/`
**Git boundary:** Windows repo (`main` branch) — **vendored** from upstream, do not diverge

## Purpose
Vendored copy of the Antigravity skill library. Contains 626+ agent skills indexed
in `skills_index.json` and catalogued in `CATALOG.md`.

## Tech Stack
- Node.js / JavaScript + Python (mixed skill scripts in `skills/`)
- `package.json` for JS tooling

## Build Commands
- `npm install`

## Local Rules
- **Do NOT add custom skills here** — custom skills belong in `1.agentic/Skills/`
- This is a mirror of upstream Antigravity — diverging commits will cause merge pain
- Mirror mappings are tracked in `1.agentic/Skills/registry.json`
- To sync: check the upstream remote and `git pull` — do not force-push custom changes
