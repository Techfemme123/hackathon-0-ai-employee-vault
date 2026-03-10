from vault_core import handle_claude_command

print("🤖 AI Vault Claude Console Activated")
print("💡 Type commands: add_task, list_tasks, update_task, summary, due_soon, exit")

while True:
    command = input("\n💻 Command: ").strip()
    
    if command.lower() == "exit":
        print("Exiting Claude Console.")
        break

    args = {}
    # Ask for parameters depending on the command
    if command == "add_task":
        args["name"] = input("Task name: ").strip()
        args["priority"] = input("Priority (High/Medium/Low) [default: Medium]: ").strip() or "Medium"
        args["due_date"] = input("Due date (YYYY-MM-DD) or leave blank: ").strip() or None
    elif command == "update_task":
        args["name"] = input("Task name: ").strip()
        args["status"] = input("New status (Pending/In Progress/Completed): ").strip().title()
    
    # Send to vault bridge
    result = handle_claude_command(command, args)
    
    print(f"\n{result}")
