"""Institute Expense Tracker.

Records daily institute expenses (stationery, internet bills,
refreshments, transport) in expenses.csv and shows totals by category.

File: expenses.csv (columns: date,item,category,amount)
"""

import csv
import os

CSV_FILE = "expenses.csv"
FIELDNAMES = ["date", "item", "category", "amount"]


def load_expenses():
    """Load saved expenses. Start empty if the file does not exist yet."""
    expenses = []
    try:
        with open(CSV_FILE, "r", newline="", encoding="utf-8") as f:
            for row in csv.DictReader(f):
                row["amount"] = float(row["amount"])
                expenses.append(row)
    except FileNotFoundError:
        print("No previous expense file found. Starting with an empty list.")
    return expenses


def save_expenses(expenses):
    """Save all expenses to the CSV file."""
    with open(CSV_FILE, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
        writer.writeheader()
        writer.writerows(expenses)


def add_expense(expenses):
    """Ask for one expense and add it to the list."""
    date = input("Enter date (YYYY-MM-DD): ").strip()
    item = input("Enter item name: ").strip()
    category = input("Enter category: ").strip()
    while True:
        try:
            amount = float(input("Enter amount: ").strip())
            break
        except ValueError:
            print("Invalid amount. Please enter a number.")
    expenses.append(
        {"date": date, "item": item, "category": category, "amount": amount}
    )
    save_expenses(expenses)
    print("Expense saved.")


def show_expenses(expenses):
    """Show all recorded expenses and the unique categories."""
    if not expenses:
        print("No expenses recorded yet.")
        return
    print("\nAll Expenses:")
    print(f"{'Date':<12} {'Item':<20} {'Category':<15} {'Amount':>10}")
    for e in expenses:
        print(f"{e['date']:<12} {e['item']:<20} {e['category']:<15} {e['amount']:>10.2f}")
    categories = set(e["category"] for e in expenses)
    print("\nUnique categories:", ", ".join(sorted(categories)))


def total_by_category(expenses):
    """Show the total amount spent in each category."""
    if not expenses:
        print("No expenses recorded yet.")
        return
    totals = {}
    for e in expenses:
        totals[e["category"]] = totals.get(e["category"], 0) + e["amount"]
    print("\nTotal Expenses by Category:")
    for category in sorted(totals):
        print(f"{category}: {totals[category]:.2f}")
    print(f"Grand total: {sum(totals.values()):.2f}")


def main():
    expenses = load_expenses()
    while True:
        print("\n--- Institute Expense Tracker ---")
        print("1. Add New Expense")
        print("2. Show All Expenses")
        print("3. Calculate Total Expenses by Category")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ").strip()
        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            show_expenses(expenses)
        elif choice == "3":
            total_by_category(expenses)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3 or 4.")


if __name__ == "__main__":
    main()
