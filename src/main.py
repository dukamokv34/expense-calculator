from datetime import datetime
from calculator import ExpenseCalculator

def read_float(prompt: str) -> float:
    while True:
        try:
            value = float(input(prompt).replace(",", "."))
            if value < 0:
                print("Сума не може бути від’ємною.")
                continue
            return value
        except ValueError:
            print("Помилка: введіть число.")

def read_date(prompt: str):
    while True:
        text = input(prompt).strip()
        try:
            return datetime.strptime(text, "%Y-%m-%d").date()
        except ValueError:
            print("Помилка: дата має бути у форматі YYYY-MM-DD (наприклад 2025-01-30).")

def main() -> None:
    calc = ExpenseCalculator()

    while True:
        print("\n=== Expense Calculator (MVP) ===")
        print("1) Додати витрату")
        print("2) Показати підсумки")
        print("3) Вийти")

        choice = input("Оберіть дію: ").strip()

        if choice == "1":
            amount = read_float("Сума витрати: ")
            exp_date = read_date("Дата (YYYY-MM-DD): ")
            category = input("Категорія (їжа/транспорт/покупки/...): ").strip()
            if not category:
                category = "Інше"

            calc.add_expense(amount, exp_date, category)
            print("Витрату додано.")

        elif choice == "2":
            total = calc.get_total_sum()
            avg = calc.get_daily_average()
            print(f"Загальна сума витрат: {total:.2f}")
            print(f"Середні витрати за день: {avg:.2f}")

        elif choice == "3":
            print("Завершення роботи.")
            break
        else:
            print("Невірний вибір! Спробуйте ще раз.")

if __name__ == "__main__":
    main()

