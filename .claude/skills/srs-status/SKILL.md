---
name: srs-status
description: Show the DSA SRS dashboard — solved counts, overdue cards, stage distribution, weakest patterns.
---

# /srs-status — Dashboard Overview

Run `python3 scripts/dsa.py status`, then add from `progress.json`:
- Weakest patterns by average last rating (`pattern`, falling back to `topic`).
- Notes still containing unfilled template text (e.g. "State the single most important intuition").
