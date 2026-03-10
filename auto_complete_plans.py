


# auto_complete_plans.py
from pathlib import Path
import time

PLANS_FOLDER = Path("Plans")

def auto_complete_plans():
    completed_tag = "- [x]"
    while True:
        for plan_file in PLANS_FOLDER.glob("PLAN_*.md"):
            with open(plan_file, "r") as f:
                lines = f.readlines()
            updated = False
            for i, line in enumerate(lines):
                if line.strip().startswith("- [ ]"):
                    lines[i] = line.replace("- [ ]", completed_tag)
                    updated = True
            if updated:
                with open(plan_file, "w") as f:
                    f.writelines(lines)
                print(f"Auto-completed: {plan_file.name}")
        time.sleep(2)

if __name__ == "__main__":
    print("Watching Plans folder to auto-complete plans...")
    auto_complete_plans  from pathlib import Path
import time
import plan_generator
import shutil

NEEDS_ACTION_FOLDER = Path("Needs_Action")
PLANS_FOLDER = Path("Plans")

def auto_complete_plans():
    print("Watching Needs_Action folder to generate plans...")
    completed_tag = "- [x]"
    processed_files = set()
    
    while True:
        for task_file in NEEDS_ACTION_FOLDER.glob("FILE_*.md"):
            if task_file.name in processed_files:
                continue  # skip already processed files
            
            # Generate plan using AI Brain
            plan_generator.generate_plan_for_file(task_file)
            
            # Optionally, mark original task as done
            with open(task_file, "r") as f:
                lines = f.readlines()
            for i, line in enumerate(lines):
                if line.strip().startswith("- [ ]"):
                    lines[i] = line.replace("- [ ]", completed_tag)
            with open(task_file, "w") as f:
                f.writelines(lines)
            
            processed_files.add(task_file.name)
            
            # Optional: move original task to a Done folder
            # shutil.move(str(task_file), "Done/" + task_file.name)
        
        time.sleep(2)

if __name__ == "__main__":
    auto_complete_plans()from pathlib import Path
import time
import plan_generator
import shutil

NEEDS_ACTION_FOLDER = Path("Needs_Action")
PLANS_FOLDER = Path("Plans")

def auto_complete_plans():
    print("Watching Needs_Action folder to generate plans...")
    completed_tag = "- [x]"
    processed_files = set()
    
    while True:
        for task_file in NEEDS_ACTION_FOLDER.glob("FILE_*.md"):
            if task_file.name in processed_files:
                continue  # skip already processed files
            
            # Generate plan using AI Brain
            plan_generator.generate_plan_for_file(task_file)
            
            # Optionally, mark original task as done
            with open(task_file, "r") as f:
                lines = f.readlines()
            for i, line in enumerate(lines):
                if line.strip().startswith("- [ ]"):
                    lines[i] = line.replace("- [ ]", completed_tag)
            with open(task_file, "w") as f:
                f.writelines(lines)
            
            processed_files.add(task_file.name)
            
            # Optional: move original task to a Done folder
            # shutil.move(str(task_file), "Done/" + task_file.name)
        
        time.sleep(2)

if __name__ == "__main__":
    auto_complete_plans()from pathlib import Path
import time
import plan_generator
import shutil

NEEDS_ACTION_FOLDER = Path("Needs_Action")
PLANS_FOLDER = Path("Plans")

def auto_complete_plans():
    print("Watching Needs_Action folder to generate plans...")
    completed_tag = "- [x]"
    processed_files = set()
    
    while True:
        for task_file in NEEDS_ACTION_FOLDER.glob("FILE_*.md"):
            if task_file.name in processed_files:
                continue  # skip already processed files
            
            # Generate plan using AI Brain
            plan_generator.generate_plan_for_file(task_file)
            
            # Optionally, mark original task as done
            with open(task_file, "r") as f:
                lines = f.readlines()
            for i, line in enumerate(lines):
                if line.strip().startswith("- [ ]"):
                    lines[i] = line.replace("- [ ]", completed_tag)
            with open(task_file, "w") as f:
                f.writelines(lines)
            
            processed_files.add(task_file.name)
            
            # Optional: move original task to a Done folder
            # shutil.move(str(task_file), "Done/" + task_file.name)
        
        time.sleep(2)

if __name__ == "__main__":
    auto_complete_plans()

import os
import ai_brain

def generate_plan_for_file(task_file):
    """
    Reads a task file, generates plan via AI Brain, saves to Plans folder.
    """
    task_name = os.path.splitext(os.path.basename(task_file))[0]
    plan_file = f"Plans/PLAN_{task_name}.md"
    with open(task_file, "r") as f:
        task_text = f.read()
    plan_content = ai_brain.generate_plan(task_text)
    with open(plan_file, "w") as f:
        f.write(plan_content)
    print(f"Plan created: {plan_file}")s