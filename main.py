from file_handler import load_expenses
from expense_manager import ExpenseManager
from analyzer import ExpenseAnalyzer
from report import print_expense_table, generate_expense_report
from validator import (
    validate_amount,
    validate_date,
    validate_description,
    validate_category
)


def display_menu():

    print("\n")
    print("=" * 50)
    print("              EXPENSE TRACKER")
    print("=" * 50)

    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. Search Expense")
    print("4. Update Expense")
    print("5. Delete Expense")
    print("6. Expense Analysis")
    print("7. Generate Report")
    print("8. Exit")

    print("=" * 50)


def add_expense(manager):

    print("\n--- ADD EXPENSE ---")

    description = input("Enter description: ").strip()

    while not validate_description(description):
        print("Description cannot be empty.")
        description = input("Enter description: ").strip()

    amount_input = input("Enter amount: ").strip()

    while not validate_amount(amount_input):
        print("Please enter a valid positive amount.")
        amount_input = input("Enter amount: ").strip()

    amount = float(amount_input)

    category = input("Enter category: ").strip()

    while not validate_category(category):
        print("Category cannot be empty.")
        category = input("Enter category: ").strip()

    date = input("Enter date (DD-MM-YYYY): ").strip()

    while not validate_date(date):
        print("Invalid date format.")
        print("Please use DD-MM-YYYY.")
        date = input("Enter date (DD-MM-YYYY): ").strip()

    expense = manager.add_expense(
        description,
        amount,
        category,
        date
    )

    print("\nExpense added successfully!")
    print(f"Expense ID: {expense.expense_id}")


def view_expenses(manager):

    print("\n--- ALL EXPENSES ---")

    expenses = manager.get_all_expenses()

    print_expense_table(expenses)


def search_expense(manager):

    print("\n--- SEARCH EXPENSE ---")

    keyword = input(
        "Enter description or category to search: "
    ).strip()

    results = manager.search_expenses(keyword)

    print_expense_table(results)


def update_expense(manager):

    print("\n--- UPDATE EXPENSE ---")

    try:
        expense_id = int(
            input("Enter expense ID to update: ")
        )

    except ValueError:
        print("Invalid ID.")
        return

    expense = manager.find_expense(expense_id)

    if expense is None:
        print("Expense not found.")
        return

    print("\nCurrent information:")
    print(f"Description: {expense.description}")
    print(f"Amount: ₹{expense.amount:.2f}")
    print(f"Category: {expense.category}")
    print(f"Date: {expense.date}")

    print("\nEnter new information.")

    description = input(
        "Enter new description: "
    ).strip()

    while not validate_description(description):
        print("Description cannot be empty.")
        description = input(
            "Enter new description: "
        ).strip()

    amount_input = input(
        "Enter new amount: "
    ).strip()

    while not validate_amount(amount_input):
        print("Please enter a valid positive amount.")
        amount_input = input(
            "Enter new amount: "
        ).strip()

    amount = float(amount_input)

    category = input(
        "Enter new category: "
    ).strip()

    while not validate_category(category):
        print("Category cannot be empty.")
        category = input(
            "Enter new category: "
        ).strip()

    date = input(
        "Enter new date (DD-MM-YYYY): "
    ).strip()

    while not validate_date(date):
        print("Invalid date format.")
        date = input(
            "Enter new date (DD-MM-YYYY): "
        ).strip()

    success = manager.update_expense(
        expense_id,
        description,
        amount,
        category,
        date
    )

    if success:
        print("\nExpense updated successfully!")
    else:
        print("\nUnable to update expense.")


def delete_expense(manager):

    print("\n--- DELETE EXPENSE ---")

    try:
        expense_id = int(
            input("Enter expense ID to delete: ")
        )

    except ValueError:
        print("Invalid ID.")
        return

    expense = manager.find_expense(expense_id)

    if expense is None:
        print("Expense not found.")
        return

    print(f"\nExpense: {expense.description}")
    print(f"Amount: ₹{expense.amount:.2f}")

    confirmation = input(
        "Are you sure you want to delete it? (y/n): "
    ).lower()

    if confirmation == "y":

        if manager.delete_expense(expense_id):
            print("Expense deleted successfully!")

    else:
        print("Deletion cancelled.")


def expense_analysis(manager):

    print("\n--- EXPENSE ANALYSIS ---")

    expenses = manager.get_all_expenses()

    if not expenses:
        print("No expenses available.")
        return

    analyzer = ExpenseAnalyzer(expenses)

    print(f"\nTotal Spending : ₹{analyzer.total_expense():.2f}")

    print(
        f"Average Expense: "
        f"₹{analyzer.average_expense():.2f}"
    )

    highest = analyzer.highest_expense()

    if highest:
        print(
            f"Highest Expense: "
            f"{highest.description} - "
            f"₹{highest.amount:.2f}"
        )

    lowest = analyzer.lowest_expense()

    if lowest:
        print(
            f"Lowest Expense : "
            f"{lowest.description} - "
            f"₹{lowest.amount:.2f}"
        )

    print("\nCategory-wise Spending")
    print("-" * 35)

    summary = analyzer.category_summary()

    for category, amount in summary.items():
        print(f"{category:<20} ₹{amount:.2f}")

    highest_category = analyzer.highest_category()

    if highest_category:
        print(
            f"\nHighest Spending Category: "
            f"{highest_category}"
        )


def main():

    expenses = load_expenses()

    manager = ExpenseManager(expenses)

    while True:

        display_menu()

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_expense(manager)

        elif choice == "2":
            view_expenses(manager)

        elif choice == "3":
            search_expense(manager)

        elif choice == "4":
            update_expense(manager)

        elif choice == "5":
            delete_expense(manager)

        elif choice == "6":
            expense_analysis(manager)

        elif choice == "7":
            generate_expense_report(
                manager.get_all_expenses()
            )

        elif choice == "8":
            print("\nThank you for using Expense Tracker!")
            break

        else:
            print("\nInvalid choice!")
            print("Please select a number from 1 to 8.")


if __name__ == "__main__":
    main()