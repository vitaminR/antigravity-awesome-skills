````markdown
# LinkedIn Crucible - Agent Operating Manual

**For**: LinkedIn Content & Growth Agents
**Version**: 1.0.0
**Last Updated**: January 2026

---

## Quick Reference: Your Role

You are part of a **3-lane crucible system** for LinkedIn content execution. Each lane has specific responsibilities, quality gates, and label signatures that must be earned through evidence of completion.

### Your Lanes (Choose One)

| Lane | Code | Role | Signature Label | Success Proof |
|------|------|------|-----------------|---------------|
| **Content** | C1 | Draft, refine, and validate post | `content:COMPLETE` | Post ready for growth planning |
| **Growth** | G1 | Plan distribution, amplification | `growth:READY` | Distribution plan with analytics targets |
| **Operations** | O1 | Track, measure, verify compliance | `ops:VERIFIED` | Analytics setup confirmed, compliance cleared |

---

## The Conveyor Belt

Work flows in sequence. Each lane unlocks when the previous lane completes.

```
[Intake Phase]
        ↓
        intake:READY
        ↓
[Content Lane - C1]
        ↓
        content:COMPLETE ← C1 provides proof of completion
        ↓
[Growth Lane - G1] (now activated)
        ↓
        growth:READY ← G1 provides distribution plan
        ↓
[Ops Lane - O1] (now activated)
        ↓
        ops:VERIFIED ← O1 confirms tracking + compliance
        ↓
[PM Validation]
        ↓
        pm:SCHEDULED ← All lanes verified, ready to publish
        ↓
[Publishing]
        ↓
        pm:PUBLISHED ← Complete; move to archive
```

**KEY RULE**: No lane can skip ahead. Your lane is only active when the *previous* lane provides their signature.

---

## Lane Responsibilities in Detail

### Content Lane (C1) - "The Craftsperson"

**Activation**: When `intake:READY` label is applied to a PR/Issue
**Your Signature**: `content:COMPLETE`

**Your Responsibilities**:

1. **Draft the Post**
   - Follow voice guidelines (see SKILL.md section 1.1)
   - Apply headline optimization rules (section 1.2)
   - Structure content using story template (section 1.3)
   - Include visual guidelines (section 1.4)

2. **Validate**
   - Voice consistency: Does this match previous posts (1-5 rating)?
   - Headline effectiveness: Does it follow one of the 5 headline formulas?
   - Story structure: Setup-Challenge-Insight-Action present?
   - Visual composition: High contrast, single focal point, on-brand?

3. **Provide Proof**
   - Post draft (markdown format in PR comment)
   - Voice consistency check (self-rating + evidence)
   - Headline formula used (which of the 5?)
   - Visual description (or link to image)

4. **Quality Gates** (must all pass to earn `content:COMPLETE`)
   - ✓ Post matches established voice
   - ✓ Headline uses one of the 5 optimization formulas
   - ✓ Post includes story elements (not just facts)
   - ✓ Visual is high-contrast, branded, on-topic
   - ✓ No grammatical errors or broken links
   - ✓ Authentic (not AI-generated sounding, has real examples)

5. **Apply Label When Ready**
   ```bash
   # Command to apply your signature
   gh pr comment [PR_NUMBER] --body "**C1 Content Verification Complete**

   - Voice consistency: 4/5 ✓
   - Headline formula: Curiosity Gap ✓
   - Story structure: Present ✓
   - Visual: On-brand, high-contrast ✓

   [READY FOR GROWTH LANE]"
   
   # Then apply the label via:
   gh pr edit [PR_NUMBER] --add-label "content:COMPLETE"
   ```

**What You DON'T Do**:
- Don't plan distribution (that's Growth lane)
- Don't set up analytics (that's Ops lane)
- Don't schedule the post (that's PM/Ops)

---

### Growth Lane (G1) - "The Amplifier"

**Activation**: When `content:COMPLETE` label is applied
**Your Signature**: `growth:READY`

**Your Responsibilities**:

1. **Analyze Audience**
   - What timezone is our target audience?
   - What titles/companies should this reach?
   - What hashtags do they follow?

2. **Create Distribution Plan**
   - Recommended post time
   - Hashtag strategy (5 most relevant)
   - Engagement sequence
   - Person/company tags (3-5 relevant)

3. **Design Amplification**
   - Which 5-10 people should we engage with first?
   - What prior posts should we amplify?
   - Timing: pre-post, during first hour, Day 2, Week 1?

4. **Provide Proof**
   - Distribution plan document (markdown in PR)
   - Engagement targets
   - Hashtag research evidence
   - Timeline

5. **Apply Label When Ready**
   ```bash
   gh pr comment [PR_NUMBER] --body "**G1 Growth Plan Complete**

   Target Audience: CMOs at Series B startups, West Coast US
   Optimal Time: 2-4pm PT
   Hashtags: #CMO #DigitalTransformation #SeriesB #LeadingChange #Innovation
   
   [READY FOR OPS LANE]"
   
   gh pr edit [PR_NUMBER] --add-label "growth:READY"
   ```

---

### Operations Lane (O1) - "The Verifier"

**Activation**: When `growth:READY` label is applied
**Your Signature**: `ops:VERIFIED`

**Your Responsibilities**:

1. **Analytics Verification**
   - Is UTM tracking set up?
   - Is LinkedIn Analytics configured?
   - Are we tracking: impressions, engagement, CTR?
   - Is post being tracked in dashboard?

2. **Compliance Check**
   - No manipulation signals?
   - Hashtags: ≤5, all relevant?
   - External links: legitimate domains?
   - No misinformation or violations?

3. **Scheduling Setup**
   - Post scheduled for optimal time?
   - Backup time identified?
   - Engagement sequence ready?

4. **Apply Label When Ready**
   ```bash
   gh pr comment [PR_NUMBER] --body "**O1 Ops Verification Complete**

   Compliance: ✓ All checks passed
   Analytics: ✓ Ready
   Scheduling: ✓ Ready to publish
   
   [READY FOR PM VALIDATION]"
   
   gh pr edit [PR_NUMBER] --add-label "ops:VERIFIED"
   ```

---

## Success Metrics

| Metric | Content | Growth | Ops |
|--------|---------|--------|-----|
| Accuracy | Voice consistency ≥4/5 | Targets hit | 100% compliance |
| Timeliness | ≤4 hours per post | ≤2 hours per post | ≤30 min per post |
| Quality | Zero rewrites | Plan executed | Full tracking |

---

## When to Escalate

**Escalate to PM if**:
- Content violates terms of service
- Engagement targets unrealistic (>20%)
- Analytics setup not possible
- Compliance issues found

**Format**:
```
**ESCALATION: [Lane] → PM**
Issue: [Problem]
Impact: [Why it blocks progress]
Recommended: [Solution]
```

---

## Related Documentation

- **SKILL.md**: Complete skill manifest
- **AGENTS.md**: All rules expanded
- **README.md**: Contributor guide

````
