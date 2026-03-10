DEMO_MODE = True  # Set True for live demo to simulate instant AI responses

import os
import anthropic

API_KEY = os.environ.get("CLAUDE_API_KEY")
client = anthropic.Client(API_KEY)


# ai_brain.py

import json
import anthropic

API_KEY = "YOUR_CLAUDE_API_KEY"

client = anthropic.Client(API_KEY)


def get_recommendations(task_list):
    """
    task_list: list of dicts [{name, status, priority, due}]
    returns: structured recommendations from Claude
    """

    prompt = f"""
You are the AI CEO of a digital company.

Here is a list of tasks:

{json.dumps(task_list, indent=2)}

Provide recommendations for:
1. Task priorities
2. Next actions
3. Risks or delays
4. Suggestions for improvement
"""

    response = client.completions.create(
        model="claude-2",
        prompt=prompt,
        max_tokens_to_sample=500,
        temperature=0
    )

    return response.completion


def generate_plan(task_text):
    """
    Generates a structured execution plan for a task
    """
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
        plan = response.completion.strip()  # remove empty spaces
        if not plan:
            plan = "AI Brain did not return a plan. Try again."
        return plan
    except Exception as e:
        return f"Error generating plan: {e}"