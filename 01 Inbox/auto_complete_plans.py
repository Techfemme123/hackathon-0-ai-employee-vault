# auto_complete_plans.py
import time
from pathlib import Path

PLANS_FOLDER = Path("Plans")

def mark_completed(plan_file):
    lines = plan_file.read_text().splitlines()
    updated_lines = [
        line.replace("- [ ]", "- [x]") if line.strip().startswith("- [ ]") else line
        for line in lines
    ]
    plan_file.write_text("\n".join(updated_lines))
    print(f"Automatically completed: {plan_file.name}")

def watch_plans():
    print("Watching Plans folder for new plans...")
    processed = set()
    while True:
        for plan_file in PLANS_FOLDER.glob("PLAN_*.md"):
            if plan_file not in processed:
                mark_completed(plan_file)
                processed.add(plan_file)
        time.sleep(1)  # checks every second

if __name__ == "__main__":
    watch_plans()