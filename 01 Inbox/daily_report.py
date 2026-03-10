import os
from datetime import datetime

folders = {
    "Inbox": "Inbox",
    "Needs_Action": "Needs_Action",
    "Plans": "Plans"
}

report_lines = []

report_lines.append("AI Employee Daily Report")
report_lines.append("Date: " + str(datetime.now()))
report_lines.append("")

for name, path in folders.items():
    if os.path.exists(path):
        count = len(os.listdir(path))
        report_lines.append(f"{name} files: {count}")
    else:
        report_lines.append(f"{name} folder missing")

report_text = "\n".join(report_lines)

report_path = "reports/daily_report.txt"

with open(report_path, "w") as f:
    f.write(report_text)

print("Report created:", report_path)