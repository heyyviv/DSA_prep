---
name: start
description: Start a new DSA mock-interview problem targeting the weakest or longest-untouched pattern.
---

# /start — Start New Problem Session

1. Read `progress.json` to identify:
   - Patterns (`pattern`, falling back to `topic`) not touched in $\ge 7$ days.
   - Any currently overdue review cards (`review_date <= today`). If there are overdue cards, mention the count and offer `/srs-review` first.
2. Present a fresh problem statement from that gap without revealing the pattern tag or optimal complexity.
3. Run the 6-Step Interview Session Flow from `AGENTS.md`.
