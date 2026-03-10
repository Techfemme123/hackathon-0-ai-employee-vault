import pathlib

# Folder where your plan files are stored
PLAN_FOLDER = pathlib.Path("Plans")

# Loop through all plan files
for plan_file in PLAN_FOLDER.glob("PLAN_*.md"):
    content = plan_file.read_text()
    # Replace all incomplete checkboxes with completed
    updated_content = content.replace("- [ ]", "- [x]")
    plan_file.write_text(updated_content)
    print(f"Updated: {plan_file.name}")

print("All plan files are now marked as completed ✅")