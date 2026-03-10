import subprocess
import time

scripts = [
    "filesystem_watcher.py",
    "auto_complete_plans.py"
]

processes = []

print("Starting AI Employee System...\n")

for script in scripts:
    print(f"Launching {script}")
    p = subprocess.Popen(["python", script])
    processes.append(p)
    time.sleep(1)

print("\nAI Employee system is now running.")
print("Press CTRL+C to stop everything.")

try:
    while True:
        time.sleep(5)

except KeyboardInterrupt:
    print("\nStopping AI Employee system...")

    for p in processes:
        p.terminate()

    print("All services stopped.")