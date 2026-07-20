---
name: dsa-session-runner
description: Instructions for executing DSA practice slash commands (/start, /pattern, /retry, /review, /status).
---

# DSA Session Runner Skill

This skill defines how to execute the prep commands inside the repository.

## 🚀 `/start` - Start New Problem Session
1. Query `notes/` and `progress.json` to identify:
   - Patterns that haven't been touched in $\ge 7$ days.
   - Any currently overdue review problems.
2. Present a fresh problem statement from that gap without revealing the pattern tag or optimal complexity.
3. Initiate the 6-Step Interview Session Flow from `AGENTS.md`.

---

## 🎯 `/pattern [name]` - Drill Specific Pattern
1. Match `[name]` to one of the 18 standard DSA topics (e.g., `sliding-window`, `two-pointers`, `monotonic-stack`, `topological-sort`, `binary-search`).
2. Provide a classic MAANG interview problem in that category.
3. Follow the Socratic hint ladder and 6-step flow.

---

## 🔄 `/retry [problem]` - Cold Code Re-attempt
1. Locate `notes/[problem]-solved.md` and read the problem statement.
2. **DO NOT** display previous notes, pseudocode, or C++ solutions!
3. Ask the user to re-implement the optimal solution in C++ from scratch.
4. After submission, compare against previous mental model notes and update SRS rating.

---

## 📖 `/review` - SRS Spaced Repetition Session
1. Query all cards in `notes/` due today or overdue ($\text{Review Date} \le \text{Today}$).
2. Sort queue by priority:
   1. `❌ Blank` (Highest priority)
   2. `🔴 Weak`
   3. `Due Today`
   4. `Overdue`
3. Limit session to max 5 problems (max 2 per pattern tag to avoid fatigue).
4. Run review mode:
   - **Full Mode** (Stage 1-3): Recall attempt + code dry run + SRS rating update.
   - **Blitz Mode** (Stage 4-6): Prompt for 1-sentence Core Insight & key C++ edge case. Update rating immediately.
5. Print session summary:
   ```
   📊 SRS Session Summary
   ✅ Strong: 2  🟡 Okay: 1  🔴 Weak: 1  ❌ Blank: 0
   Weakest pattern this week: topological-sort
   Next session: 2026-07-21 — 3 problems due
   ```

---

## 📊 `/status` - Dashboard Overview
Execute `python3 scripts/dsa.py status` or print:
- Total Solved & Difficulty Breakdown (Easy / Medium / Hard)
- Overdue problem cards count
- Stage distribution table (Stage 1 to Stage 6 Graduated)
- Weakest pattern tags by average SRS rating
