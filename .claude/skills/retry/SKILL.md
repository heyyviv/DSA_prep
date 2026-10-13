---
name: retry
description: Cold re-attempt of a previously solved DSA problem with notes and code hidden.
argument-hint: "[problem slug or title]"
---

# /retry [problem] — Cold Code Re-attempt

Problem requested: $ARGUMENTS

1. Find the problem in `progress.json` and restate its problem statement.
2. **DO NOT** display or quote the note file, pseudocode, or C++ solution. Read them only to evaluate the answer afterwards.
3. Ask the user to re-implement the optimal solution in C++ from scratch.
4. After submission, compare against the previous mental model, rate it (Strong / Okay / Weak / Blank) and update the card in `progress.json` using the `srs-revision-coach` rules.
