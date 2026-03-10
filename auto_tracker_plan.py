import time
import pathlib
import shutil

NEEDS_ACTION_FOLDER = pathlib.Path("Needs_Action")
PLANS_FOLDER = pathlib.Path("Plans")
COMPLETED_FOLDER = pathlib.Path("Completed")

def track_file(action_file):
    task_name = action_file.stem.replace("FILE_", "")
    plan_file = PLANS_FOLDER / f"PLAN_{task_name}.md"

    if not plan_file.exists():
        print(f"No plan found for {action_file.name}, skipping.")
        return

    # Check if all steps done
    with open(plan_file, "r") as f:
        lines = f.readlines()

    all_done = all(line.startswith("- [x]") or not line.startswith("- [") for line in lines)

    if all_done:
        shutil.move(action_file, COMPLETED_FOLDER / action_file.name)
        print(f"All steps done! Moved {action_file.name} to Completed.")

def watch_needs_action():
    print("Watching Needs_Action folder...")
    processed_files = set()

    while True:
        for action_file in NEEDS_ACTION_FOLDER.glob("FILE_*.md"):
            if action_file not in processed_files:
                print(f"Detected new action file: {action_file.name}")
                track_file(action_file)
                processed_files.add(action_file)
        time.sleep(2)  # check every 2 seconds

if __name__ == "__main__":
    watch_needs_action()