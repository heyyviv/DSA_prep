# DSA Prep (C++ + Spaced Repetition)

## Setup
```bash
git clone git@github.com:heyyviv/DSA_prep.git && cd DSA_prep
python3 setup.py   # enter LeetCode username, pick fresh/sample data, optional sync
```
Needs Python 3 only (no dependencies).

## Use with Claude Code (run `claude` in this folder)
| Command | Does |
|---|---|
| `/start` | New problem for your weakest / stalest pattern |
| `/pattern sliding_window` | Drill one pattern |
| `/retry two_sum` | Re-solve a past problem with notes hidden |
| `/srs-review` | Review up to 5 due cards, updates `progress.json` |
| `/srs-status` | Progress, overdue count, weak patterns |

Hints: type `hint`, `hint hint`, `hint hint hint` (the last one names the pattern).

## CLI
```bash
python3 scripts/dsa.py add "Course Schedule" --topic 10_graphs --difficulty Medium
python3 scripts/dsa.py review         # rate due cards in the terminal
python3 scripts/dsa.py status
python3 scripts/dsa.py sync-leetcode  # import recent accepted submissions
python3 scripts/dsa.py dashboard      # web dashboard at localhost:8000
```

## Where things live
- `progress.json`: all problems + SRS state (single source of truth)
- `topics/<topic>/<slug>.cpp`: solutions · `notes/<slug>-solved.md`: pattern cards
- Review intervals: 1 → 3 → 7 → 14 → 30 → 90 days
