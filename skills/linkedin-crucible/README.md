````markdown
# LinkedIn Crucible - Contributor Guide

This repository contains LinkedIn content and growth strategies organized as a multi-lane workflow system (crucibles) optimized for AI agents and LLMs.

## Quick Start

```bash
# Install dependencies (if using build system)
cd packages/linkedin-crucible-build
npm install

# Validate existing rules
npm run validate

# Build AGENTS.md
npm run build
```

## Creating a New Rule

1. **Choose a section prefix** based on the category:
   - `content-` Content Creation (CRITICAL)
   - `growth-` Audience & Engagement (HIGH)
   - `ops-` Operations & Analytics (MEDIUM)
   - `voice-` Voice & Branding (HIGH)
   - `engagement-` Community Management (MEDIUM)

2. **Copy the template**:
   ```bash
   cp rules/_template.md rules/content-your-rule-name.md
   ```

3. **Fill in the content** following the template structure

4. **Validate and build**:
   ```bash
   npm run validate
   npm run build
   ```

5. **Review** the generated `AGENTS.md`

## Repository Structure

```
skills/linkedin-crucible/
├── SKILL.md           # Agent-facing skill manifest
├── AGENTS.md          # [GENERATED] Compiled rules document
├── README.md          # This file
├── metadata.json      # Version and metadata
└── rules/
    ├── _template.md      # Rule template
    ├── _sections.md      # Section definitions
    ├── _contributing.md  # Writing guidelines
    └── *.md              # Individual rules

packages/linkedin-crucible-build/
├── src/               # Build system source
├── package.json       # NPM scripts
└── test-cases.json    # [GENERATED] Test artifacts
```

## Rule File Structure

See `rules/_template.md` for the complete template. Key elements:

````markdown
---
title: Clear, Action-Oriented Title
impact: CRITICAL|HIGH|MEDIUM-HIGH|MEDIUM|LOW-MEDIUM|LOW
impactDescription: Quantified benefit (e.g., "3x higher engagement")
tags: relevant, keywords
crucible: content|growth|ops
---

## [Title]

[1-2 sentence explanation]

**Incorrect (description):**

```
[Example showing the problem]
```

**Correct (description):**

```
[Example showing the solution]
```

[Additional context and LinkedIn-specific notes]
````

## Writing Guidelines

See `rules/_contributing.md` for detailed guidelines. Key principles:

1. **Show concrete transformations** - "Change X to Y", not abstract advice
2. **Problem-first structure** - Show the problem before the solution
3. **Quantify impact** - Include specific metrics (3x higher engagement, 40% more impressions)
4. **Authentic LinkedIn examples** - Use realistic post scenarios
5. **Platform-specific context** - Include LinkedIn algorithm considerations

## Impact Levels by Crucible

### Content Lane

| Level | Engagement Improvement | Examples |
|-------|----------------------|----------|
| CRITICAL | 5-10x | Voice consistency, headline optimization |
| HIGH | 2-5x | Storytelling, visual composition |
| MEDIUM-HIGH | 1.5-3x | CTA placement, formatting |
| MEDIUM | 1.2-2x | Hashtag strategy, timing |
| LOW-MEDIUM | 1-1.5x | Post length optimizations |
| LOW | Incremental | Niche best practices |

### Growth Lane

| Level | Audience Expansion | Examples |
|-------|-------------------|----------|
| CRITICAL | 10-100x | Networking workflows, content amplification |
| HIGH | 5-20x | Engagement sequences, community building |
| MEDIUM-HIGH | 2-5x | Hashtag research, timing optimization |
| MEDIUM | 1.5-3x | Connection requests, follow strategies |
| LOW-MEDIUM | 1.2-2x | Profile optimization, bio tweaks |

### Operations Lane

| Level | Efficiency/Accuracy | Examples |
|-------|-------------------|----------|
| CRITICAL | 10-100x | Analytics automation, compliance checks |
| HIGH | 5-20x | UTM tracking setup, scheduling systems |
| MEDIUM | 2-5x | Reporting dashboards, metrics collection |
| LOW | Incremental | Manual tracking optimization |

## Contributing

1. Create a new rule file with appropriate prefix
2. Include concrete examples from LinkedIn
3. Reference metrics or best practices
4. Test against the LinkedIn API/platform where applicable
5. Submit for review

For all contributions, ensure consistency with:

- [The Postgres Best Practices Model](../postgres-best-practices/README.md)
- [AntiGravity Skill Standards](../README.md)
- LinkedIn's terms of service and best practices

````
