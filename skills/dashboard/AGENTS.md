# Dashboard Skill (Agent Guide)

**Scope**: Reusable mission-control dashboards for multi-agent pipelines.

## Purpose

Provide a standardized dashboard pattern with:

- Telemetry contract
- Preflight gate
- Two-mode display (INITIAL / VETTING)
- Fanfare and sound for milestones

## Usage

1. Copy templates into the target repo.
2. Wire agents to emit telemetry events.
3. Enforce dashboard preflight before execution.
4. Validate via the testing plan.

## Required Files

- `SKILL.md`
- `design-patterns.md`
- Templates (telemetry contract, preflight gate, dashboard HTML)
