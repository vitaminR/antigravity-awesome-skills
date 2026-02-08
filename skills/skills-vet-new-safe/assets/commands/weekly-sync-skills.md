---
description: Run secure weekly skills sync (active/inactive/quarantine lanes).
---

# Weekly Skills Sync

Run the secure weekly sync workflow for skills.

## Inputs

- Optional argument: upstream skills path.
- Default upstream path if omitted: `~/src/antigravity-awesome-skills/skills`.

Use this logic:

1. Resolve source path:
   - If `$ARGUMENTS` is non-empty, use `$ARGUMENTS` as the `--source`.
   - Else use `~/src/antigravity-awesome-skills/skills`.
2. Run:

```bash
python3 ~/.agent/skills/skills-vet-new-safe/scripts/vet_new_skills.py weekly-sync \
  --source "<RESOLVED_SOURCE>" \
  --active ~/.agent/skills \
  --inactive ~/.agent/skills-inactive \
  --quarantine ~/.agent/skills-quarantine \
  --denylist ~/.agent/skills/.audit/denylist.txt
```

3. Then summarize:
   - `~/.agent/skills/.audit/WEEKLY_SYNC_VERDICT.md`
   - `~/.agent/skills/.audit/WEEKLY_SYNC_REPORT.json`

