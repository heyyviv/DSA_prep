#!/usr/bin/env python3
"""
DSA Prep CLI Engine & SRS Manager
Powers /start, /pattern, /retry, /review, /status, problem scaffolding, and LeetCode API sync.
"""

import os
import sys
import json
import argparse
import urllib.request
from datetime import datetime, timedelta

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_FILE = os.path.join(ROOT_DIR, "progress.json")
NOTES_DIR = os.path.join(ROOT_DIR, "notes")
TEMPLATES_DIR = os.path.join(ROOT_DIR, "templates")
LEETCODE_USERNAME = "vivekdas2023"

STAGE_BASE_INTERVALS = {
    1: 1,
    2: 3,
    3: 7,
    4: 14,
    5: 30,
    6: 90
}

TOPIC_MAPPING = {
    "string-to-integer-atoi": ("01_arrays_and_hashing", "Medium"),
    "combination-sum": ("09_backtracking", "Medium"),
    "next-permutation": ("01_arrays_and_hashing", "Medium"),
    "edit-distance": ("14_2d_dynamic_programming", "Hard"),
    "4sum": ("02_two_pointers", "Medium"),
    "populating-next-right-pointers-in-each-node": ("07_trees", "Medium"),
    "palindrome-partitioning": ("09_backtracking", "Medium"),
    "find-median-from-data-stream": ("12_heap_priority_queue", "Hard"),
    "search-a-2d-matrix": ("05_binary_search", "Medium"),
    "next-greater-element-i": ("04_stack", "Easy"),
    "cheapest-flights-within-k-stops": ("11_advanced_graphs", "Medium")
}

def load_data():
    if not os.path.exists(DATA_FILE):
        initial_data = {
            "leetcode_user": LEETCODE_USERNAME,
            "last_updated": datetime.now().strftime("%Y-%m-%d"),
            "leetcode_stats": {
                "total_solved": 479,
                "easy": 134,
                "medium": 266,
                "hard": 79,
                "ranking": 217972
            },
            "problems": [],
            "stats": {
                "total_solved": 0,
                "easy": 0,
                "medium": 0,
                "hard": 0
            }
        }
        save_data(initial_data)
        return initial_data
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_data(data):
    data["last_updated"] = datetime.now().strftime("%Y-%m-%d")
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

def slugify(title):
    return title.lower().strip().replace(" ", "_").replace("-", "_")

def fetch_leetcode_profile(username=LEETCODE_USERNAME):
    url = f"https://leetcode-api-faisalshohag.vercel.app/{username}"
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=10) as response:
            if response.status == 200:
                data = json.loads(response.read().decode('utf-8'))
                return data
    except Exception as e:
        print(f"⚠️ Warning: Could not fetch online LeetCode stats ({e}). Using cached stats.")
    return None

def calculate_next_review(stage, rating, is_graduated):
    today = datetime.now().date()
    rating = rating.lower()
    
    if rating in ["strong", "1"]:
        new_stage = min(stage + 1, 6)
        base = STAGE_BASE_INTERVALS[new_stage]
        interval = max(1, int(round(base * 1.5)))
        graduated = True if new_stage == 6 else is_graduated
    elif rating in ["okay", "2"]:
        new_stage = stage
        interval = STAGE_BASE_INTERVALS[stage]
        graduated = is_graduated
    elif rating in ["weak", "3"]:
        new_stage = stage
        interval = max(1, STAGE_BASE_INTERVALS[stage] // 2)
        graduated = is_graduated
    else: # blank
        if is_graduated or stage == 6:
            new_stage = 3
            interval = STAGE_BASE_INTERVALS[3]
        else:
            new_stage = 1
            interval = STAGE_BASE_INTERVALS[1]
        graduated = False

    next_date = (today + timedelta(days=interval)).strftime("%Y-%m-%d")
    return new_stage, next_date, graduated

def cmd_status(args):
    data = load_data()
    lc = fetch_leetcode_profile(LEETCODE_USERNAME)
    
    if lc:
        data["leetcode_stats"] = {
            "total_solved": lc.get("totalSolved", 479),
            "easy": lc.get("easySolved", 134),
            "medium": lc.get("mediumSolved", 266),
            "hard": lc.get("hardSolved", 79),
            "ranking": lc.get("ranking", 217972)
        }
        save_data(data)

    lc_stats = data.get("leetcode_stats", {})
    problems = data.get("problems", [])
    today_str = datetime.now().strftime("%Y-%m-%d")
    overdue = [p for p in problems if p.get("review_date", "9999-99-99") <= today_str]

    print("\n" + "="*60)
    print(f" 🏆 LEETCODE PROFILE & SRS DASHBOARD FOR @{LEETCODE_USERNAME}")
    print("="*60)
    print(f"LeetCode Total Solved: {lc_stats.get('total_solved', 479)} | Global Rank: #{lc_stats.get('ranking', 217972):,}")
    print(f"LeetCode Breakdown:    🟢 Easy: {lc_stats.get('easy', 134)} | 🟡 Medium: {lc_stats.get('medium', 266)} | 🔴 Hard: {lc_stats.get('hard', 79)}")
    print("-" * 60)
    print(f"Tracked SRS Problems:  {len(problems)}")
    print(f"🚨 Overdue Reviews:    {len(overdue)}")
    print("-" * 60)
    
    stage_counts = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
    for p in problems:
        st = p.get("stage", 1)
        stage_counts[st] = stage_counts.get(st, 0) + 1

    print("SRS Stage Distribution:")
    for stage, count in stage_counts.items():
        label = "Graduated (Mastered)" if stage == 6 else f"Stage {stage}"
        print(f"  Stage {stage} ({STAGE_BASE_INTERVALS[stage]}d interval): {count} card(s) [{label}]")
    
    if overdue:
        print("\n⚠️ Problems Due For Review Today:")
        for p in overdue[:5]:
            print(f"  • [{p.get('difficulty', 'Med')}] {p.get('title')} (Stage {p.get('stage')}, Due: {p.get('review_date')})")
        if len(overdue) > 5:
            print(f"    ... and {len(overdue)-5} more.")
    else:
        print("\n✨ All SRS reviews are current! Ready for new problem practice.")
    print("="*60 + "\n")

def cmd_sync_leetcode(args):
    print(f"🔄 Syncing recent accepted submissions from LeetCode (@{LEETCODE_USERNAME})...")
    lc = fetch_leetcode_profile(LEETCODE_USERNAME)
    if not lc:
        print("❌ Could not connect to LeetCode API.")
        return

    data = load_data()
    data["leetcode_stats"] = {
        "total_solved": lc.get("totalSolved", 479),
        "easy": lc.get("easySolved", 134),
        "medium": lc.get("mediumSolved", 266),
        "hard": lc.get("hardSolved", 79),
        "ranking": lc.get("ranking", 217972)
    }

    recent_subs = lc.get("recentSubmissions", [])
    accepted = [s for s in recent_subs if s.get("statusDisplay") == "Accepted"]

    count_added = 0
    for sub in accepted:
        title = sub.get("title")
        slug_lc = sub.get("titleSlug")
        if not title or not slug_lc: continue

        topic, diff = TOPIC_MAPPING.get(slug_lc, ("01_arrays_and_hashing", "Medium"))

        # Add problem using internal helper logic
        slug = slugify(title)
        existing = [p for p in data["problems"] if p["slug"] == slug]
        if not existing:
            today_str = datetime.now().strftime("%Y-%m-%d")
            next_review = (datetime.now().date() + timedelta(days=1)).strftime("%Y-%m-%d")

            topic_dir_path = os.path.join(ROOT_DIR, "topics", topic)
            os.makedirs(topic_dir_path, exist_ok=True)
            os.makedirs(NOTES_DIR, exist_ok=True)

            cpp_filepath = os.path.join(topic_dir_path, f"{slug}.cpp")
            note_filepath = os.path.join(NOTES_DIR, f"{slug}-solved.md")

            if not os.path.exists(cpp_filepath):
                with open(os.path.join(TEMPLATES_DIR, "solution_template.cpp"), "r") as f:
                    t_code = f.read()
                cpp_code = t_code.replace("[Problem Title]", title)\
                                 .replace("[Difficulty]", diff)\
                                 .replace("[Topic / Pattern]", topic)\
                                 .replace("[Meta, Google, Amazon, etc.]", "Meta, Google, Amazon")
                with open(cpp_filepath, "w") as f:
                    f.write(cpp_code)

            if not os.path.exists(note_filepath):
                with open(os.path.join(TEMPLATES_DIR, "note_template.md"), "r") as f:
                    t_note = f.read()
                note_md = t_note.replace("[Problem Name]", title)\
                               .replace("[Easy / Medium / Hard]", diff)\
                               .replace("[Topic Category]", topic)\
                               .replace("[Meta, Google, Amazon, Apple, Microsoft, Uber]", "Meta, Google, Amazon")\
                               .replace("YYYY-MM-DD", today_str)\
                               .replace("Pattern Tag: [pattern-slug]", f"Pattern Tag: {topic}")\
                               .replace("Review Date: YYYY-MM-DD", f"Review Date: {next_review}")
                with open(note_filepath, "w") as f:
                    f.write(note_md)

            entry = {
                "slug": slug,
                "title": title,
                "difficulty": diff,
                "topic": topic,
                "companies": ["Meta", "Google", "Amazon"],
                "date_solved": today_str,
                "stage": 1,
                "review_date": next_review,
                "last_rating": "New",
                "review_count": 0,
                "graduated": False,
                "cpp_file": os.path.relpath(cpp_filepath, ROOT_DIR),
                "note_file": os.path.relpath(note_filepath, ROOT_DIR)
            }
            data["problems"].append(entry)
            count_added += 1

    save_data(data)
    print(f"🎉 LeetCode sync complete! {count_added} recent accepted problem(s) scaffolded into SRS tracker.")

def cmd_add(args):
    data = load_data()
    title = args.title
    slug = slugify(title)
    topic = args.topic if args.topic else "01_arrays_and_hashing"
    difficulty = args.difficulty.capitalize() if args.difficulty else "Medium"
    companies = args.companies.split(",") if args.companies else ["Meta", "Google"]

    topic_dir_path = os.path.join(ROOT_DIR, "topics", topic)
    os.makedirs(topic_dir_path, exist_ok=True)
    os.makedirs(NOTES_DIR, exist_ok=True)

    cpp_filepath = os.path.join(topic_dir_path, f"{slug}.cpp")
    note_filepath = os.path.join(NOTES_DIR, f"{slug}-solved.md")

    today_str = datetime.now().strftime("%Y-%m-%d")
    next_review = (datetime.now().date() + timedelta(days=1)).strftime("%Y-%m-%d")

    if not os.path.exists(cpp_filepath):
        with open(os.path.join(TEMPLATES_DIR, "solution_template.cpp"), "r") as f:
            template_code = f.read()
        cpp_code = template_code.replace("[Problem Title]", title)\
                                 .replace("[Difficulty]", difficulty)\
                                 .replace("[Topic / Pattern]", topic)\
                                 .replace("[Meta, Google, Amazon, etc.]", ", ".join(companies))
        with open(cpp_filepath, "w") as f:
            f.write(cpp_code)
        print(f"✅ Created C++ File: {cpp_filepath}")

    if not os.path.exists(note_filepath):
        with open(os.path.join(TEMPLATES_DIR, "note_template.md"), "r") as f:
            template_note = f.read()
        note_md = template_note.replace("[Problem Name]", title)\
                               .replace("[Easy / Medium / Hard]", difficulty)\
                               .replace("[Topic Category]", topic)\
                               .replace("[Meta, Google, Amazon, Apple, Microsoft, Uber]", ", ".join(companies))\
                               .replace("YYYY-MM-DD", today_str)\
                               .replace("Pattern Tag: [pattern-slug]", f"Pattern Tag: {topic}")\
                               .replace("Review Date: YYYY-MM-DD", f"Review Date: {next_review}")
        with open(note_filepath, "w") as f:
            f.write(note_md)
        print(f"✅ Created Pattern Card Note: {note_filepath}")

    problem_entry = {
        "slug": slug,
        "title": title,
        "difficulty": difficulty,
        "topic": topic,
        "companies": companies,
        "date_solved": today_str,
        "stage": 1,
        "review_date": next_review,
        "last_rating": "New",
        "review_count": 0,
        "graduated": False,
        "cpp_file": os.path.relpath(cpp_filepath, ROOT_DIR),
        "note_file": os.path.relpath(note_filepath, ROOT_DIR)
    }

    data["problems"] = [p for p in data["problems"] if p["slug"] != slug]
    data["problems"].append(problem_entry)

    save_data(data)
    print(f"🎉 Problem '{title}' successfully added and scheduled for SRS review ({next_review})!\n")

def cmd_review(args):
    data = load_data()
    today_str = datetime.now().strftime("%Y-%m-%d")
    overdue = [p for p in data["problems"] if p.get("review_date", "9999-99-99") <= today_str]

    if not overdue:
        print("\n✨ No problems currently due for review today! Enjoy your prep.\n")
        return

    print(f"\n🧠 SRS REVISION SESSION ({len(overdue)} card(s) due)\n" + "="*50)
    for p in overdue[:5]:
        print(f"\n📌 Problem: {p['title']} [{p['difficulty']}] (Stage {p['stage']})")
        print(f"   Note File: {p['note_file']}")
        print(f"   C++ File:  {p['cpp_file']}")
        print("   Rate your recall performance:")
        print("     [1] Strong  (Clean recall, fast optimal code)")
        print("     [2] Okay    (Correct, needed minor hint)")
        print("     [3] Weak    (Struggled, needed 2+ hints)")
        print("     [4] Blank   (Forgot intuition / total reset)")
        
        choice = input("   Enter choice (1-4 or strong/okay/weak/blank): ").strip().lower()
        rating_map = {"1": "strong", "2": "okay", "3": "weak", "4": "blank",
                      "strong": "strong", "okay": "okay", "weak": "weak", "blank": "blank"}
        rating = rating_map.get(choice, "okay")

        new_stage, next_date, graduated = calculate_next_review(p['stage'], rating, p.get('graduated', False))
        
        p['stage'] = new_stage
        p['review_date'] = next_date
        p['last_rating'] = rating.capitalize()
        p['review_count'] = p.get('review_count', 0) + 1
        p['graduated'] = graduated

        print(f"   Result -> Updated to Stage {new_stage} | Next Review: {next_date}\n")

    save_data(data)
    print("✅ Session saved!\n")

def main():
    parser = argparse.ArgumentParser(description="DSA Prep CLI & SRS Engine")
    subparsers = parser.add_subparsers(dest="command")

    subparsers.add_parser("status", help="Show SRS Dashboard status")
    subparsers.add_parser("sync-leetcode", help="Sync recent accepted problems from LeetCode profile")

    parser_add = subparsers.add_parser("add", help="Add a new solved DSA problem")
    parser_add.add_argument("title", help="Problem title (e.g. 'Two Sum')")
    parser_add.add_argument("--topic", default="01_arrays_and_hashing", help="Topic directory name")
    parser_add.add_argument("--difficulty", default="Medium", choices=["Easy", "Medium", "Hard"])
    parser_add.add_argument("--companies", default="Meta,Google", help="Comma-separated company names")

    subparsers.add_parser("review", help="Run SRS review session")

    args = parser.parse_args()

    if args.command == "status":
        cmd_status(args)
    elif args.command == "sync-leetcode":
        cmd_sync_leetcode(args)
    elif args.command == "add":
        cmd_add(args)
    elif args.command == "review":
        cmd_review(args)
    else:
        cmd_status(args)

if __name__ == "__main__":
    main()
