import json
import re
from pydantic import ValidationError
from models import BudgetPlan


def extract_json(text):
    text = re.sub(r"```.*?```", "", text, flags=re.DOTALL)

    match = re.search(r'\{.*\}', text, re.DOTALL)
    if match:
        return match.group()

    return None


def parse_and_validate(response_json):
    try:
        content = response_json['choices'][0]['message']['content']

        print("\nRAW MODEL OUTPUT:\n", content)

        json_str = extract_json(content)

        if not json_str:
            print("❌ No JSON found")
            return None

        data = json.loads(json_str)

        validated = BudgetPlan(**data)
        return validated

    except json.JSONDecodeError:
        print("❌ JSON parsing failed")
    except ValidationError as e:
        print("❌ Validation error:", e)

    return None
