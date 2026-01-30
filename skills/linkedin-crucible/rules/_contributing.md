````markdown
# Contributing to LinkedIn Crucible

Guidelines for writing effective rules for the LinkedIn Crucible skill.

## Before You Start

1. Choose your crucible: **Content**, **Growth**, or **Operations**
2. Identify the specific focus: voice, storytelling, audience, analytics, etc.
3. Copy the `_template.md` file
4. Follow the structure below

## Rule Writing Guidelines

### 1. Title

- **Action-oriented**: Use imperative voice ("Optimize headlines", "Build authentic voice")
- **Specific**: Not "Post Better", but "Use Curiosity Gaps in Headlines"
- **5-8 words ideal**: Enough detail without being unwieldy
- **Include benefit if possible**: "Headlines That Drive 5x CTR"

### 2. Metadata (YAML Front Matter)

```yaml
---
title: [Title - 5-8 words, action-oriented]
impact: [CRITICAL|HIGH|MEDIUM-HIGH|MEDIUM|LOW-MEDIUM|LOW]
impactDescription: "[Quantified benefit - specific number/percentage]"
tags: tag1, tag2, relevant-keywords
crucible: [content|growth|ops]
---
```

**Impact Selection:**
- Start conservative (over-claiming hurts credibility)
- Base on LinkedIn best practices or data
- If uncertain, go one level down

### 3. The Opening (1-2 sentences)

**What it should do:**
- Explain WHY this matters
- Connect to business outcome
- Show the cost of ignoring it

**Example:**
"Your headline determines whether people click into your post. On LinkedIn, 85% of decision happens in the first line. Poor headlines = content lost in the noise."

### 4. Incorrect Approach Section

**Format:**
```
**Incorrect (description of the problem):**

[Show the antipattern]
[Real example if possible]
[Include negative outcome with metrics if available]
```

**What it should include:**
- What most people do wrong
- Why it fails (the mechanism)
- Outcome if this approach is used
- Ideally numerical: "Results in 2% CTR"

**Example:**
```
**Incorrect (vague headlines):**

"Thoughts on Digital Transformation"
→ Too generic, could be anyone
→ CTR: 1-2% (LinkedIn average for low-value content)
→ Algorithm penalty: low CTR signals low-quality content

"Check out my latest insights"
→ No specific value proposition
→ Algorithm: suppressed distribution
```

### 5. Correct Approach Section

**Format:**
```
**Correct (description of the solution):**

[Show the best practice]
[Real example if possible]
[Include positive outcome with metrics]
```

**What it should include:**
- What to do instead
- Why it works (the mechanism)
- Expected improvement (specific metrics)
- How to implement it

**Example:**
```
**Correct (specific, benefit-driven headlines):**

"Why 73% of digital transformations fail (and how we fixed ours)"
→ Specific metric + curiosity gap
→ CTR: 8-12% (6x improvement)
→ Algorithm boost: high CTR signals quality content

"3 questions we ask before implementing any new tool"
→ Clear structure (number) + relatable challenge
→ CTR: 7-10%
```

### 6. LinkedIn-Specific Context

**Add a section explaining:**
- How does this interact with LinkedIn's algorithm?
- What platform constraints should I know?
- LinkedIn-specific best practices or data
- Edge cases or exceptions

**Example:**
```
**LinkedIn Algorithm Context:**
- LinkedIn rewards early engagement (first 1-2 hours critical)
- Native content (posts) get 10x more reach than links
- Video gets 5x reach of image posts
- Comments signal quality better than likes (weighted higher)
```

### 7. Metrics for Success

**Include:**
- What to measure
- Improvement targets
- How to track it
- Benchmarks (if available)

**Example:**
```
**Metrics for Success:**
- Engagement rate: target 6-10% (vs 2% industry average)
- Comment rate: target 1-3% of impressions
- Save rate: target 0.5-1%
- CTR: target 5-8% (for headline-focused posts)
```

### 8. Implementation Checklist

**Include:**
- Step-by-step how to implement
- Tools needed
- Time required
- Frequency/recurrence

**Example:**
```
**Implementation Checklist:**
- [ ] Review: Read your last 10 posts (identify voice patterns)
- [ ] Define: Document 3-5 voice pillars using template
- [ ] Create: Draft voice guidelines (1 page max)
- [ ] Audit: Rate last 5 posts on voice consistency (1-5 scale)
- [ ] Calibrate: Adjust guidelines if needed
- [ ] Commit: Before writing new post, review voice guidelines
- [ ] Measure: Track engagement on voice-aligned vs outlier posts
```

## Style Guidelines

### Show, Don't Tell

**Bad:**
"You should make your posts more engaging."

**Good:**
```
Incorrect: "Check out my insights"
Correct: "Here's why 73% of transformations fail"
Result: 8x engagement improvement
```

### Use Concrete Examples, Not Abstractions

**Bad:**
"Use psychological principles in your messaging"

**Good:**
```
Use scarcity: "Only 3 spots left for [event]"
Use social proof: "2,000 leaders have implemented this"
Use curiosity gap: "Everyone gets step 1 wrong. Here's why."
```

### Quantify Everything

**Bad:**
- "This works really well"
- "Much faster than the old way"
- "Significantly better engagement"

**Good:**
- "3x engagement improvement"
- "47% faster processing"
- "2.8x better CTR"

### Include Platform-Specific Details

**Bad:**
"Post more content"

**Good:**
"Post 3-5x per week; LinkedIn algorithm favors consistency. Daily posting increases burnout risk with minimal additional reach."

### Acknowledge Nuance and Exceptions

**Bad:**
"Always use questions in headlines"

**Good:**
```
Questions work well for engagement-focused posts (6-10% engagement)
Statements work well for thought leadership (4-7% engagement)
Contrarian takes work in any format (10-15% engagement)

Use questions when: You want discussion/comments
Use statements when: You want thought leadership positions
Use contrarian when: Your audience is forward-thinking
```

## Testing Your Rule

Before submitting, ask:

1. **Clarity**: Can someone execute this without asking questions?
2. **Proof**: Do I have data or precedent for the impact claim?
3. **Specificity**: Would someone know exactly what to do?
4. **Value**: Does the effort justify the return (time vs impact)?
5. **LinkedIn-fit**: Is this specific to LinkedIn or generic social advice?

## Common Pitfalls to Avoid

### Over-claiming impact
❌ "This will 100x your engagement"
✓ "Expect 3-5x improvement on average"

### Ignoring context
❌ "Always post at 2pm"
✓ "Post at 2pm if your audience is West Coast US"

### Vague implementation
❌ "Be more authentic"
✓ "Reference 2-3 specific personal learnings per post"

### Missing platform nuance
❌ "Engagement drives reach" (true everywhere)
✓ "On LinkedIn, comments weighted 10x higher than likes for reach"

### Ignoring edge cases
❌ "Never use links" (false, sometimes necessary)
✓ "Use native content for 10x reach; use external links only for critical resources"

## Examples of Strong Rules

See `/rules/` folder for examples:
- `content-voice-consistency.md`
- `growth-audience-targeting.md`
- `ops-analytics-tracking.md`

## Questions?

1. Are you following the rule template?
2. Did you quantify the impact?
3. Does the example match a real LinkedIn scenario?
4. Would someone actually do this after reading?

If yes to all four: you're ready to submit!

````
