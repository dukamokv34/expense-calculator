from __future__ import annotations
from datetime import date
from typing import List
from .models import Expense, Category


class ExpenseCalculator:
    def __init__(self) -> None:
        self.expenses: List[Expense] = []

    def add_expense(self, amount: float, exp_date: date, category_name: str) -> None:
        category = Category(category_name.strip())
        self.expenses.append(
            Expense(amount=amount, date=exp_date, category=category)
        )

    def get_total_sum(self) -> float:
        return sum(e.amount for e in self.expenses)

    def get_daily_average(self) -> float:
        if not self.expenses:
            return 0.0
        dates = [e.date for e in self.expenses]
        days = (max(dates) - min(dates)).days + 1
        return self.get_total_sum() / days


# ✅ ALIAS для тестов
Calculator = ExpenseCalculator
