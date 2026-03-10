import time
from pathlib import Path

WATCH_FOLDER = Path("Inbox")  # folder to watch
ACTION_FOLDER = Path("Needs_Action")  # where to create .md files

# Make sure action folder exists
ACTION_FOLDER.mkdir(exist_ok=True)

def watch_folder(dry_run=True):
    seen_files = set()
    while True:
        for file in WATCH_FOLDER.iterdir():
            if file.is_file() and file.name not in seen_files:
                seen_files.add(file.name)
                action_file = ACTION_FOLDER / f"FILE_{file.stem}.md"
                if dry_run:
                    print(f"[DRY RUN] Would create: {action_file}")
                else:
                    with open(action_file, "w") as f:
                        f.write(f"# Action File for {file.name}\n")
                        f.write(f"- Path: {file}\n")
                        f.write(f"- Detected: {time.ctime()}\n")
                    print(f"Created: {action_file}")
        time.sleep(2)  # check every 2 seconds

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true", help="Test without writing files")
    args = parser.parse_args()
    watch_folder(dry_run=args.dry_run)