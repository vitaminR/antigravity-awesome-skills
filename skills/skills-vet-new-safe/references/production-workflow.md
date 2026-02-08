# Production Workflow

## Lane model

- `active`: live folder used by agents (`~/.agent/skills`).
- `inactive`: parking lot for warning/manual-off skills (`~/.agent/skills-inactive`).
- `quarantine`: blocked skills with danger/error findings (`~/.agent/skills-quarantine`).

This keeps production simple: agents read only `active`.

## Commands

Initialize folders and policy files:

```bash
python3 ~/.agent/skills/skills-vet-new-safe/scripts/vet_new_skills.py init-layout
```

Install slash command wrapper:

```bash
python3 ~/.agent/skills/skills-vet-new-safe/scripts/install_slash_command.py
```

Then invoke `/weekly-sync-skills` (or equivalent in your client).

Weekly secure sync:

```bash
python3 ~/.agent/skills/skills-vet-new-safe/scripts/vet_new_skills.py weekly-sync \
  --source ~/src/antigravity-awesome-skills/skills \
  --denylist ~/.agent/skills/.audit/denylist.txt
```

Dry run:

```bash
python3 ~/.agent/skills/skills-vet-new-safe/scripts/vet_new_skills.py weekly-sync \
  --source ~/src/antigravity-awesome-skills/skills \
  --dry-run
```

New skills only:

```bash
python3 ~/.agent/skills/skills-vet-new-safe/scripts/vet_new_skills.py weekly-sync \
  --source ~/src/antigravity-awesome-skills/skills \
  --new-only
```

Allow warnings into active (not recommended):

```bash
python3 ~/.agent/skills/skills-vet-new-safe/scripts/vet_new_skills.py weekly-sync \
  --source ~/src/antigravity-awesome-skills/skills \
  --allow-warnings \
  --no-placeholder-warnings
```

Activate/deactivate manually:

```bash
python3 ~/.agent/skills/skills-vet-new-safe/scripts/vet_new_skills.py deactivate --skill skill-id
python3 ~/.agent/skills/skills-vet-new-safe/scripts/vet_new_skills.py activate --skill skill-id
```

## Reports

- `~/.agent/skills/.audit/WEEKLY_SYNC_REPORT.json`
- `~/.agent/skills/.audit/WEEKLY_SYNC_VERDICT.md`
- state file: `~/.agent/skills/.audit/skills_vet_state.json`

## Policy files

- allowlist: only these skills may be imported when allowlist is provided.
- denylist: these skills are blocked and sent to quarantine.

Use `resources/allowlist.example.txt` and `resources/denylist.example.txt` as templates.

## Placeholder behavior

When a skill is warning-level, the workflow writes a safe placeholder `SKILL.md` into active.  
That placeholder tells agents to:

- gather requirements and constraints,
- produce a safe build plan,
- avoid risky or policy-bypassing instructions,
- require explicit approval before runtime-sensitive actions.
