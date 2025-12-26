from dataclasses import dataclass
from datetime import date

@dataclass(frozen=True)
class Category:
    name: str

@dataclass
class Expense:
    amount: float
    date: date
    category: Category

    def get_amount(self) -> float:
        return self.amount

    def get_category(self) -> Category:
        return self.category
