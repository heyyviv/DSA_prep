# 🚀 Big Tech DSA Preparation & Spaced Repetition System (C++)

A stateful, interview-focused repository system for mastering Data Structures and Algorithms (DSA) targeted at Tier-1 High-Paying Tech Companies (**Uber, Coupang, Roku, TikTok, Meta, Google, Amazon, Apple, Microsoft**).

Powered by an **Anki-style Spaced Repetition Engine (SRS)**, a **MAANG Socratic Interview Coach**, and interactive progress tracking.

---

## ⚙️ Quick Onboarding Setup

If you have just cloned this repository, run the setup wizard to connect your LeetCode account:
```bash
python3 setup.py
```
This script will configure your username, verify your stats, clear or retain sample problems, and fetch recent accepted submissions.

---

## ⚡ Quick Start & Available Commands

### 🤖 Inside Chat Agent (Slash Commands & Prompt Shortcuts)
- `/start` : Finds patterns untouched for $\ge 7$ days or overdue review problems and starts a mock session.
- `/pattern [name]` : Drill a specific pattern cold (e.g. `/pattern sliding_window` or `/pattern topological_sort`).
- `/retry [problem]` : Re-attempt a previously solved problem with code hidden to verify true retention.
- `/review` : Launch an SRS spaced repetition session (Priority: Blank → Weak → Due Today → Overdue).
- `/status` : View overall prep statistics, stage distribution, and weakest pattern tags.

### 💻 Command Line Interface (CLI Helper)
Run commands directly in your terminal:
```bash
# View SRS progress dashboard & overdue cards
python3 scripts/dsa.py status

# Add a newly solved problem (automatically creates C++ & Note templates)
python3 scripts/dsa.py add "Course Schedule" --topic "10_graphs" --difficulty Medium --companies "Meta,Google"

# Interactive SRS review session
python3 scripts/dsa.py review
```

---

## 📊 Interactive Web Dashboard

To bypass modern browser CORS restrictions (which block local data loading when opening raw HTML files via `file://`), run the built-in lightweight server:

```bash
python3 scripts/dsa.py dashboard
```

This will automatically start a local server and open your default browser to view statistics, filterable problem tables, revision calendars, and pattern heatmaps.

---

## 🧠 Spaced Repetition System (SRS) Stages

| Stage | Base Interval | Status | Description |
|-------|---------------|--------|-------------|
| **Stage 1** | 1 Day | Learning | Newly solved or reset card |
| **Stage 2** | 3 Days | Learning | Short-term memory verification |
| **Stage 3** | 7 Days | Consolidation | 1-week pattern retention |
| **Stage 4** | 14 Days | Retention | 2-week cold recall test |
| **Stage 5** | 30 Days | Mastery | Monthly maintenance check |
| **Stage 6** | 90 Days | **Graduated** | Long-term mastered pattern |

---

## 🪜 Socratic Interviewer & 3-Tier Hint Ladder

When practicing problems with the AI coach:
1. **`hint`**: Intuition only (1-2 sentences). Focus on core problem invariants.
2. **`hint hint`**: Concrete structural approach without naming the pattern.
3. **`hint hint hint`**: Pattern named explicitly (e.g. Monotonic Stack, Topological Sort).

---

## 📁 Repository Structure

```
DSA_prep/
├── AGENTS.md                          # Project Constitution & Interviewer Persona
├── README.md                          # Dashboard Homepage
├── progress.json                      # Stateful Database for Problems & SRS Metadata
├── .agents/                           # Agent Customizations & Skills
│   └── skills/
│       ├── srs-revision-coach/        # Anki Spaced Repetition Engine
│       └── dsa-session-runner/        # Slash Commands Execution Skill
├── templates/
│   ├── solution_template.cpp          # C++ Starter Template with Fast I/O & STL
│   └── note_template.md               # Pattern Card & Mental Model Matrix Template
├── cheat_sheets/
│   └── cpp_patterns.md                # Modern C++ STL & 18 DSA Pattern Blueprints
├── notes/                             # Solved Problem Notes ([problem]-solved.md)
├── scripts/
│   └── dsa.py                         # CLI Manager & Generator
├── dashboard/                         # Visual Web App Tracker
│   ├── index.html
│   ├── styles.css
│   └── app.js
└── topics/                            # Topic-wise C++ Source Code
    ├── 01_arrays_and_hashing/
    ├── 02_two_pointers/
    ├── 03_sliding_window/
    ├── 04_stack/
    ├── 05_binary_search/
    ├── 06_linked_list/
    ├── 07_trees/
    ├── 08_tries/
    ├── 09_backtracking/
    ├── 10_graphs/
    ├── 11_advanced_graphs/
    ├── 12_heap_priority_queue/
    ├── 13_1d_dynamic_programming/
    ├── 14_2d_dynamic_programming/
    ├── 15_greedy/
    ├── 16_intervals/
    ├── 17_math_and_geometry/
    └── 18_bit_manipulation/
```
