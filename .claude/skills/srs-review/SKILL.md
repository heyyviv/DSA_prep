---
name: srs-review
description: Run a spaced-repetition review session over due DSA cards from progress.json.
---

# /srs-review — SRS Spaced Repetition Session

1. Build the queue exactly like `build_review_queue` in `scripts/dsa.py`: cards with `review_date <= today`, ordered:
   1. `❌ Blank` last rating (highest priority)
   2. `🔴 Weak` last rating
   3. Due today
   4. Overdue (oldest first)
2. Limit the session to 5 cards, max 2 per pattern (`pattern`, falling back to `topic`).
3. Run review mode per card:
   - **Full Mode** (Stage 1-3): Recall attempt + code dry run, then rating.
   - **Blitz Mode** (Stage 4-6): Ask for the 1-sentence Core Insight and a key C++ edge case, then rating.
4. Update each card in `progress.json` (`stage`, `review_date`, `last_rating`, `review_count`, `graduated`) using the `srs-revision-coach` rules. `progress.json` is the only place SRS state is stored. Do not write it into notes.
5. Print a session summary:
   ```
   📊 SRS Session Summary
   ✅ Strong: 2  🟡 Okay: 1  🔴 Weak: 1  ❌ Blank: 0
   Weakest pattern this week: topological-sort
   Next session: YYYY-MM-DD — N problems due
   ```
