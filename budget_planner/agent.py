import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("OPENROUTER_API_KEY")


def build_prompt(income, expenses):
    return f"""
A user has:
- Income: {income}
- Expenses: {expenses}

Create a monthly budget plan.

STRICT RULES:
- Return ONLY JSON
- Do NOT write code
- Do NOT use markdown
- Do NOT explain anything

Format:
{{
  "income": number,
  "total_expenses": number,
  "savings": number,
  "expense_breakdown": [
    {{
      "category": "...",
      "amount": number
    }}
  ],
  "recommendations": ["...", "..."]
}}
"""


def get_budget_plan(prompt):
    response = requests.post(
        "https://openrouter.ai/api/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json"
        },
        json={
            "model": "meta-llama/llama-3-8b-instruct",
            "messages": [
                {
                    "role": "system",
                    "content": "You are a financial planner AI. Return ONLY valid JSON. No explanation. No code."
                },
                {"role": "user", "content": prompt}
            ]
        }
    )

    if response.status_code != 200:
        raise Exception(f"API Error: {response.text}")

    return response.json()
