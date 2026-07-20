---
name: srs-revision-coach
description: Spaced Repetition System (SRS) algorithm engine for DSA problem review and interval tracking based on Anki logic.
---

# SRS Revision Coach Engine

This skill calculates the next review dates, interval logic, and stage transitions for DSA problem pattern cards.

## 📊 SRS Stages & Base Intervals

| Stage | Name | Base Interval | Description |
|-------|------|---------------|-------------|
| 1 | Learning 1 | 1 day | Newly solved or reset problem |
| 2 | Learning 2 | 3 days | Short-term recall check |
| 3 | Reinforcement | 7 days | 1-week pattern consolidation |
| 4 | Retention | 14 days | 2-week memory validation |
| 5 | Mastery | 30 days | Monthly check |
| 6 | Graduated | 90 days | Long-term mastery |

---

## 📈 Rating & Interval Calculation Rules

When a user reviews a problem (via `/review` or `/retry`), calculate the updated metadata as follows:

### 1. Rating Outputs
- **✅ Strong**: Perfect recall, clean C++ logic, accurate complexity analysis.
  - **New Stage**: $\min(\text{Current Stage} + 1, 6)$
  - **Next Review Interval**: $\lceil \text{Base Interval for New Stage} \times 1.5 \rceil$ days
  - **Graduated**: `Yes` if Stage == 6 else `No`

- **🟡 Okay**: Correct algorithm with minor hints or minor code syntax hiccups.
  - **New Stage**: $\text{Current Stage}$ (Unchanged)
  - **Next Review Interval**: $\text{Base Interval for Current Stage}$ days

- **🔴 Weak**: High friction, required 2+ hints or struggled with edge cases.
  - **New Stage**: $\text{Current Stage}$ (Unchanged)
  - **Next Review Interval**: $\max(\lfloor \text{Base Interval for Current Stage} / 2 \rfloor, 1)$ day

- **❌ Blank**: Total memory breakdown, forgot core intuition, or could not formulate approach.
  - **If NOT Graduated**: Reset to **Stage 1** (Interval: 1 day).
  - **If Graduated (was Stage 6)**: Soft reset to **Stage 3** (Interval: 7 days) — *prevents harsh penalty for long-dormant cards*.

---

## 📋 Pattern Card Tracking Metadata Schema

Every note in `notes/[problem_slug]-solved.md` must include this standardized tracking block at the bottom:

```markdown
## SRS Tracking
- **Stage**: 1
- **Review Date**: YYYY-MM-DD
- **Last Rating**: -
- **Review Count**: 0
- **Graduated**: No
- **Pattern Tag**: sliding-window
- **Difficulty**: Medium
```
