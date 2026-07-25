#!/usr/bin/env python3
import os
import sys
import json
import urllib.request
import subprocess
from datetime import datetime

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(ROOT_DIR, "progress.json")
SCRIPTS_DIR = os.path.join(ROOT_DIR, "scripts")

def print_banner():
    print("""
======================================================================
  🚀 WELCOME TO THE BIG TECH DSA PREPARATION & SRS SETUP WIZARD
======================================================================
  This script will configure your LeetCode Account ID and prepare
  your personal spaced repetition workspace.
======================================================================
""")

def fetch_leetcode_profile(username):
    url = f"https://leetcode-api-faisalshohag.vercel.app/{username}"
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=10) as response:
            if response.status == 200:
                return json.loads(response.read().decode('utf-8'))
    except Exception as e:
        pass
    return None

def main():
    print_banner()
    
    # 1. Ask for Username
    username = ""
    profile_data = None
    while not username:
        username = input("👉 Enter your LeetCode Username: ").strip()
        if not username:
            print("⚠️ Username cannot be empty. Please try again.")
            continue
        
        print(f"⏳ Verifying '@{username}' via LeetCode API...")
        profile_data = fetch_leetcode_profile(username)
        
        if not profile_data:
            print(f"⚠️ Warning: Could not find LeetCode profile or verify username '@{username}'.")
            confirm = input("Are you sure this is the correct username? (y/n): ").strip().lower()
            if confirm not in ['y', 'yes']:
                username = ""
                profile_data = None
                continue
    
    # Show stats if fetched successfully
    if profile_data:
        total_solved = profile_data.get("totalSolved", 0)
        easy = profile_data.get("easySolved", 0)
        medium = profile_data.get("mediumSolved", 0)
        hard = profile_data.get("hardSolved", 0)
        ranking = profile_data.get("ranking", 0)
        print(f"\n✅ Profile verified successfully!")
        print(f"   • Total Solved: {total_solved} (Easy: {easy}, Medium: {medium}, Hard: {hard})")
        print(f"   • Global Rank:  #{ranking:,}")
    else:
        total_solved, easy, medium, hard, ranking = 0, 0, 0, 0, 0
        print(f"\n⚠️ Proceeding with default/empty stats.")
    
    # 2. Database Slate Choice
    print("\n----------------------------------------------------------------------")
    print("Choose your Database Setup:")
    print("  [1] Fresh Start (Recommended: start with a clean database for your own solved problems)")
    print("  [2] Keep Sample Problems (Start with 5+ pre-loaded LeetCode problems in your queue)")
    print("----------------------------------------------------------------------")
    
    choice = ""
    while choice not in ['1', '2']:
        choice = input("👉 Enter choice (1 or 2): ").strip()
    
    # Load/Modify progress.json
    existing_data = {}
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, "r", encoding="utf-8") as f:
                existing_data = json.load(f)
        except Exception:
            pass

    problems = []
    stats = {"total_solved": 0, "easy": 0, "medium": 0, "hard": 0}
    
    if choice == '2' and "problems" in existing_data:
        problems = existing_data["problems"]
        stats = existing_data.get("stats", stats)
        print("ℹ️ Keeping existing sample problems in tracking database.")
    else:
        print("ℹ️ Creating a clean state database.")

    new_data = {
        "leetcode_user": username,
        "last_updated": datetime.now().strftime("%Y-%m-%d"),
        "leetcode_stats": {
            "total_solved": total_solved,
            "easy": easy,
            "medium": medium,
            "hard": hard,
            "ranking": ranking
        },
        "problems": problems,
        "stats": stats
    }
    
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(new_data, f, indent=2)
    print(f"📝 progress.json database successfully updated.")

    # 3. Ask to Sync Recent Problems
    print("\n----------------------------------------------------------------------")
    sync_choice = input("🔄 Would you like to sync your recent accepted LeetCode submissions? (y/n): ").strip().lower()
    if sync_choice in ['y', 'yes']:
        print("\n⚡ Syncing recent submissions...")
        dsa_py = os.path.join(SCRIPTS_DIR, "dsa.py")
        subprocess.run([sys.executable, dsa_py, "sync-leetcode"])
    
    print("\n======================================================================")
    print("🎉 WORKSPACE SETUP COMPLETE!")
    print("======================================================================")
    print(f"  LeetCode Account: @{username}")
    print("  Database Status:  Ready")
    print("\n  Next Steps:")
    print("   1. View your visual dashboard:")
    print("      Run the local dashboard server to bypass CORS issues:")
    print("      python3 scripts/dsa.py dashboard")
    print("   2. Run an interactive SRS review session in terminal:")
    print("      python3 scripts/dsa.py review")
    print("   3. Start a mock practice session with the Antigravity chat coach:")
    print("      Type '/start' inside the chat window.")
    print("======================================================================\n")

if __name__ == "__main__":
    main()
