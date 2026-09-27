import csv
import os
from expense import Expense


FILE_PATH = "data/expenses.csv"


def create_data_file():
    """Create the data folder and CSV file if they don't exist."""

    folder = os.path.dirname(FILE_PATH)

    if folder and not os.path.exists(folder):
        os.makedirs(folder)

    if not os.path.exists(FILE_PATH):
        with open(FILE_PATH, "w", newline="") as file:
            writer = csv.writer(file)

            writer.writerow([
                "id",
                "description",
                "amount",
                "category",
                "date"
            ])


def save_expenses(expenses):
    """Save all expenses to the CSV file."""

    create_data_file()

    with open(FILE_PATH, "w", newline="") as file:

        writer = csv.DictWriter(
            file,
            fieldnames=[
                "id",
                "description",
                "amount",
                "category",
                "date"
            ]
        )

        writer.writeheader()

        for expense in expenses:
            writer.writerow(expense.to_dict())


def load_expenses():
    """Load expenses from the CSV file."""

    create_data_file()

    expenses = []

    with open(FILE_PATH, "r", newline="") as file:

        reader = csv.DictReader(file)

        for row in reader:

            expense = Expense(
                int(row["id"]),
                row["description"],
                float(row["amount"]),
                row["category"],
                row["date"]
            )

            expenses.append(expense)

    return expenses