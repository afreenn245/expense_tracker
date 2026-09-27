from analyzer import ExpenseAnalyzer


def print_expense_table(expenses):

    if not expenses:
        print("\nNo expenses found.")
        return

    print("\n" + "=" * 75)

    print(
        f"{'ID':<5}"
        f"{'Description':<20}"
        f"{'Amount':<15}"
        f"{'Category':<15}"
        f"{'Date'}"
    )

    print("=" * 75)

    for expense in expenses:
        print(expense)

    print("=" * 75)


def generate_expense_report(expenses):

    if not expenses:
        print("\nNo expenses available for report.")
        return

    analyzer = ExpenseAnalyzer(expenses)

    highest = analyzer.highest_expense()
    lowest = analyzer.lowest_expense()

    print("\n")
    print("=" * 50)
    print("           EXPENSE REPORT")
    print("=" * 50)

    print(f"Number of Expenses : {len(expenses)}")
    print(f"Total Spending     : ₹{analyzer.total_expense():.2f}")
    print(f"Average Expense    : ₹{analyzer.average_expense():.2f}")

    if highest:
        print(
            f"Highest Expense    : "
            f"{highest.description} - ₹{highest.amount:.2f}"
        )

    if lowest:
        print(
            f"Lowest Expense     : "
            f"{lowest.description} - ₹{lowest.amount:.2f}"
        )

    print("\nCategory-wise Spending")
    print("-" * 35)

    summary = analyzer.category_summary()

    for category, amount in summary.items():
        print(f"{category:<20} ₹{amount:.2f}")

    print("\nMonthly Spending")
    print("-" * 35)

    monthly = analyzer.monthly_summary()

    for month, amount in monthly.items():
        print(f"{month:<20} ₹{amount:.2f}")

    print("=" * 50)