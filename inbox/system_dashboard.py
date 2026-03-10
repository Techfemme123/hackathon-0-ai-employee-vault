import os

folders = {
    "Inbox": "Inbox",
    "Needs_Action": "Needs_Action",
    "Plans": "Plans"
}

print("\nAI EMPLOYEE SYSTEM DASHBOARD\n")

for name, path in folders.items():
    if os.path.exists(path):
        files = os.listdir(path)
        print(f"{name} files: {len(files)}")
    else:
        print(f"{name} folder not found")

print("\nSystem running successfully\n")