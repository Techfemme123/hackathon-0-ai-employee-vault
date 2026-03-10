import ai_brain

from pathlib import Path

NEEDS_ACTION = Path("Needs_Action")
task_text = open(task_file).read()

# Ask AI brain to generate plan
plan = ai_brain.generate_plan(task_text)
def generate_plans():
    def generate_plan(task_text):
    """
    Generates a structured execution plan for a task
    """
    if DEMO_MODE:
        # Simulate AI Brain instantly
        plan = f"""
AI Generated Plan for Task (Demo Mode):
{task_text}

Step 1: Analyze task requirements
Step 2: Break task into smaller actionable steps
Step 3: Assign responsibilities
Step 4: Execute and monitor progress
Step 5: Review and finalize outcomes
"""
        return plan.strip()

    # Normal operation with Claude API
    try:
        prompt = f"""
You are an AI operations planner.

Create a clear step-by-step execution plan for the following task:

Task:
{task_text}

Provide 5 practical steps.
"""
        response = client.completions.create(
            model="claude-2",
            prompt=prompt,
            max_tokens_to_sample=500,
            temperature=0
        )
        plan = response.completion.strip()
        if not plan:
            plan = "AI Brain did not return a plan. Try again."
        return plan
    except Exception as e:
        return f"Error generating plan: {e}"