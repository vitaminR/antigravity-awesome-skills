# li-crucible (Codepro workspace skill)

This skill exists to make Li-Crucible discoverable as a **skill** in tools that scan `.github/skills/**/SKILL.md`.

## What it points to

Canonical Li-Crucible definitions live in the `3.LinkedIn-Branding/` repo:

- `3.LinkedIn-Branding/00_Context/LLM_Copilot.md`
- `3.LinkedIn-Branding/.agent/workflows/Li-Crucible.md`
- `3.LinkedIn-Branding/.agent/agents/LI1.LinkedIn-Ideator.agent.md`
- `3.LinkedIn-Branding/.agent/agents/LI2.LinkedIn-Drafter.agent.md`
- `3.LinkedIn-Branding/.agent/agents/LI3.LinkedIn-Editor.agent.md`
- `3.LinkedIn-Branding/.agent/agents/LI4.LinkedIn-Publisher.agent.md`

## Primary chat entrypoints

- `/crucible fNN`
- `@Li-Crucible fNN`

If this skill doesn’t show up in your UI, your tool may require installing skills into a global skills folder (see `SKILL.md`).
