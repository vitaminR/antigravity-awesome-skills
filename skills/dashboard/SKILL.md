# Dashboard Skill (Reusable Pattern)

## Overview
A reusable, file‑based dashboard pattern for tracking multi‑agent pipelines. Includes a strict telemetry contract and a preflight gate so agents never run without a visible dashboard.

## Components
- **Telemetry Contract**: Defines event schema.
- **Preflight Gate**: Blocks execution if dashboard is stale or mission mismatched.
- **Dashboard UI**: Summary + Timeline tabs, step progress, mode badges.

## Implementation Checklist
- [ ] Copy telemetry contract into target repo
- [ ] Add preflight gate script
- [ ] Add telemetry emitter helper
- [ ] Update agent playbooks to require preflight
- [ ] Update dashboard HTML to parse telemetry
- [ ] Run test plan

## Two Modes
- **INITIAL**: Main lane work
- **VETTING**: Cross-lane validation and improvement

## Fanfare Requirements
- Mission start: sound + animation
- Checklist group complete: sound + animation

## Testing
Use the test plan for fast + comprehensive validation.
