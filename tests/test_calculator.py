from datetime import date
from calculator import ExpenseCalculator


def test_add_expense():
    calc = ExpenseCalculator()
    calc.add_expense(100.0, date(2025, 1, 1), "Їжа")

    assert len(calc.expenses) == 1
    assert calc.expenses[0].amount == 100.0
    assert calc.expenses[0].category.name == "Їжа"


def test_total_sum():
    calc = ExpenseCalculator()
    calc.add_expense(100.0, date(2025, 1, 1), "Їжа")
    calc.add_expense(50.0, date(2025, 1, 1), "Транспорт")

    assert calc.get_total_sum() == 150.0


def test_daily_average_one_day():
    calc = ExpenseCalculator()
    calc.add_expense(120.0, date(2025, 1, 1), "Покупки")

    assert calc.get_daily_average() == 120.0


def test_daily_average_multiple_days():
    calc = ExpenseCalculator()
    calc.add_expense(100.0, date(2025, 1, 1), "Їжа")
    calc.add_expense(200.0, date(2025, 1, 3), "Транспорт")

    # період: 3 дні (1, 2, 3)
    assert calc.get_daily_average() == 100.0


def test_daily_average_empty():
    calc = ExpenseCalculator()

    assert calc.get_daily_average() == 0.0
