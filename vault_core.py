import json
import os 
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TASK_FILE = os.path.join(BASE_DIR, "tasks.json") 

tasks = []

TASK_FILE =  os.path.join(BASE_DIR, "tasks.json")

# -------------------------------
# Load Tasks
# -------------------------------
import os

BASE_DIR = os.path.dirname(__file__)
TASK_FILE = os.path.join(BASE_DIR, "tasks.json")
print("🤖 AI Vault Agent Activated")


# -------------------------------
# Core Functions
# -------------------------------

def save_tasks():
    with open(TASK_FILE, "w") as f:
        json.dump(tasks, f, indent=4)


def add_task():
    name = input("Enter task name: ").strip()
    priority = input("Enter priority (High/Medium/Low): ").strip().title()
    status = input("Enter status (Pending/In Progress/Completed): ").strip().title()
    due = input("Enter due date (YYYY-MM-DD) or leave blank: ").strip()

    task = {
        "name": name,
        "priority": priority,
        "status": status,
        "due": due if due else None
    }

    tasks.append(task)
    save_tasks()
    print(f"✅ Task '{name}' added successfully.")


def list_tasks():
    if not tasks:
        print("No tasks found.")
        return

    for i, t in enumerate(tasks, 1):
        print(f"{i}. {t['name']} | Status: {t['status']} | Priority: {t['priority']} | Due: {t['due']}")


def update_task():
    list_tasks()
    if not tasks:
        return

    try:
        choice = int(input("Enter task number to update: "))
        if 1 <= choice <= len(tasks):
            new_status = input("Enter new status (Pending/In Progress/Completed): ").strip().title()
            tasks[choice - 1]["status"] = new_status
            save_tasks()
            print("✅ Task updated successfully.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input.")


def summary():
    total = len(tasks)
    completed = sum(1 for t in tasks if t["status"] == "Completed")
    pending = sum(1 for t in tasks if t["status"] == "Pending")
    in_progress = sum(1 for t in tasks if t["status"] == "In Progress")

    print(f"\nTotal Tasks: {total}")
    print(f"Completed: {completed}")
    print(f"Pending: {pending}")
    print(f"In Progress: {in_progress}")


def due_soon():
    print("Due soon feature not implemented yet.")


# -------------------------------
# CLI
# -------------------------------

def run_cli():
    while True:
        command = input(
            "Enter command (add, list, update, summary, due_soon, exit): "
        ).strip().lower()

        if command == "exit":
            print("Exiting Vault CLI. Goodbye!")
            break

        elif command == "add":
            add_task()

        elif command == "list":
            list_tasks()

        elif command == "update":
            update_task()

        elif command == "summary":
            summary()

        elif command == "due_soon":
            due_soon()

        else:
            print("Invalid command. Please try again.")