````skill
---
name: linkedin-crucible
description: Multi-lane workflow system for LinkedIn content creation and execution. Use this skill when planning, creating, or optimizing LinkedIn strategy, posts, campaigns, or engagement initiatives.
license: MIT
metadata:
  author: AntiGravity
  version: "1.0.0"
---

# LinkedIn Crucible

Comprehensive multi-lane workflow for LinkedIn content creation and strategic execution. Organized into specialized crucibles (Content, Growth, Operations) with defined agents, protocols, and conveyor belt sequencing.

## When to Apply

Reference these guidelines when:
- Planning LinkedIn content strategy
- Creating posts, articles, or campaigns
- Designing audience engagement workflows
- Scaling LinkedIn presence
- Measuring and optimizing LinkedIn impact
- Managing LinkedIn influencer positioning

## Compatibility note (LinkedIn-Branding repo)

If you are operating inside the `LinkedIn-Branding/` repository, this skill is **non-authoritative** for process and file paths.

To avoid drift/conflicts:
- Defer to `LinkedIn-Branding/00_Context/LLM_Copilot.md` and `LinkedIn-Branding/PRD0_Crucible_Master.md`.
- Use the campaign-era canonical paths:
    - Draft: `LinkedIn-Branding/2026/**/02.Drafts/**/<ID>_<Topic>/post.md`
    - Ready: `LinkedIn-Branding/2026/**/03.Ready/**/<ID>_<Topic>/post.md`
    - Shipped: `LinkedIn-Branding/2026/**/04.Shipped/**/<ID>_<Topic>/post.md`
- Treat `LinkedIn-Branding/03_Final_Queue/CRUCIBLE_STATUS.md` as **tracker-only**, not canonical post storage.

## Crucible Categories by Priority

| Priority | Crucible | Focus | Prefix |
|----------|----------|-------|--------|
| 1 | Content | Post creation, voice, narrative | `content-` |
| 2 | Growth | Audience expansion, engagement | `growth-` |
| 3 | Operations | Analytics, compliance, infrastructure | `ops-` |

## Conveyor Belt Model

Work flows through lanes in strict sequence, with each lane adding a signature label as proof of completion:

```
intake:READY
    ↓
content:COMPLETE        ← Content Creator drafts and refines
    ↓
growth:READY            ← Growth Agent plans distribution
    ↓
ops:VERIFIED            ← Operations Agent confirms analytics
    ↓
pm:SCHEDULED            ← PM validates all gates passed
    ↓
(publish)
    ↓
pm:PUBLISHED            ← PM archives and closes
```

## ⛔ IMAGE GENERATION HARD RULES (CRITICAL — ALL AGENTS)

### Single-Shot Mandate
**FORBIDDEN: More than 1 image generation call per post.** If it fails, STOP. Do not retry. Set `art_status: "IMAGE_PENDING"`. Previous sessions burned the entire monthly image quota in retry loops.

### Capybara: NEVER Bipedal
The Capybara is a quadrupedal tank robot. ALWAYS on all fours. NEVER upright. NEVER standing on two legs. NEVER has fur. The word "standing" is banned in Capybara prompts — use "positioned low" or "crouching". If a generated image shows bipedal pose: DO NOT USE IT.

See `OPERATING_MANUAL.md` for full rules.

## Lane Responsibilities

| Lane | Signature | Evidence Required |
|------|-----------|-------------------|
| **Content** | `content:COMPLETE` | Post draft complete, voice verified, links validated |
| **Growth** | `growth:READY` | Distribution plan ready, hashtags curated, timing optimized |
| **Operations** | `ops:VERIFIED` | Analytics tracking enabled, compliance checked, metadata set |

## How to Use

Read individual rule files for detailed explanations and implementation guidance:

```
rules/content-voice-consistency.md
rules/growth-audience-targeting.md
rules/ops-analytics-setup.md
```

Each rule file contains:
- Explanation of why it matters
- Incorrect approach with explanation
- Correct approach with explanation
- LinkedIn-specific context and best practices
- Metrics for measuring success

## Full Compiled Document

For the complete guide with all rules expanded: `AGENTS.md`

````
