from flask import Flask, render_template_string
import os

app = Flask(__name__)

VAULT_PATH = "C:/AI_employee_vault"

@app.route("/")
def dashboard():
    inbox_path = os.path.join(VAULT_PATH, "Inbox")
    needs_path = os.path.join(VAULT_PATH, "Needs_action")
    done_path = os.path.join(VAULT_PATH, "Done")

    # Make sure folders exist
    os.makedirs(inbox_path, exist_ok=True)
    os.makedirs(needs_path, exist_ok=True)
    os.makedirs(done_path, exist_ok=True)

    inbox = os.listdir(inbox_path)
    needs = os.listdir(needs_path)
    done = os.listdir(done_path)

    HTML = """<!DOCTYPE html>
<html>
<head>
    <title>AI Employee Dashboard</title>
    <style>
        body { font-family: Arial, sans-serif; background-color: #f4f6f8; padding: 20px; }
        h1 { color: #2c3e50; }
        .section { display: inline-block; vertical-align: top; width: 30%; margin-right: 2%; }
        .card { background-color: white; padding: 10px; margin-bottom: 10px; border-radius: 8px; box-shadow: 0px 2px 5px rgba(0,0,0,0.1); }
        .section h2 { text-align: center; color: #34495e; }
        .section ul { list-style: none; padding: 0; }
        .section li { padding: 5px; border-bottom: 1px solid #eee; }
        .inbox { border-top: 4px solid #3498db; }
        .needs { border-top: 4px solid #f39c12; }
        .done { border-top: 4px solid #2ecc71; }
    </style>
</head>
<body>
    <h1>AI Employee Dashboard</h1>
    <div class="section inbox">
        <h2>📥 Inbox</h2>
        <ul>
            {% for file in inbox %}
            <li class="card">{{ file }}</li>
            {% endfor %}
        </ul>
    </div>
    <div class="section needs">
        <h2>⚠ Needs Action</h2>
        <ul>
            {% for file in needs %}
            <li class="card">{{ file }}</li>
            {% endfor %}
        </ul>
    </div>
    <div class="section done">
        <h2>✅ Completed</h2>
        <ul>
            {% for file in done %}
            <li class="card">{{ file }}</li>
            {% endfor %}
        </ul>
    </div>
</body>
</html>"""
    return render_template_string(HTML, inbox=inbox, needs=needs, done=done)

if __name__ == "__main__":
    app.run(debug=True)