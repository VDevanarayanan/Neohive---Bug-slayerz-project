from pydantic import BaseModel
from typing import List


class Expense(BaseModel):
    category: str
    amount: float


class BudgetPlan(BaseModel):
    income: float
    total_expenses: float
    savings: float
    expense_breakdown: List[Expense]
    recommendations: List[str]
