from agent import build_prompt, get_budget_plan
from utils import parse_and_validate
from rich import print


def main():
    print("[bold green]💰 Budget Planner AI Agent[/bold green]\n")

    income = float(input("Enter monthly income: "))
    rent = float(input("Rent: "))
    food = float(input("Food: "))
    travel = float(input("Travel: "))
    other = float(input("Other expenses: "))

    expenses = {
        "rent": rent,
        "food": food,
        "travel": travel,
        "other": other
    }

    prompt = build_prompt(income, expenses)

    print("\n[bold yellow]⏳ Generating plan...[/bold yellow]\n")

    response = get_budget_plan(prompt)

    plan = parse_and_validate(response)

    if plan:
        print("\n[bold cyan]📊 Budget Plan[/bold cyan]\n")
        print(plan.model_dump_json(indent=2))
    else:
        print("❌ Failed to generate valid plan")


if __name__ == "__main__":
    main()
