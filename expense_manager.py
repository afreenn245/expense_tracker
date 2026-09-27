from expense import Expense
from file_handler import save_expenses


class ExpenseManager:

    def __init__(self, expenses):
        self.expenses = expenses

    def generate_id(self):
        """Generate a new unique expense ID."""

        if not self.expenses:
            return 1

        return max(expense.expense_id for expense in self.expenses) + 1

    def add_expense(self, description, amount, category, date):
        """Add a new expense."""

        expense_id = self.generate_id()

        expense = Expense(
            expense_id,
            description,
            amount,
            category,
            date
        )

        self.expenses.append(expense)

        save_expenses(self.expenses)

        return expense

    def get_all_expenses(self):
        """Return all expenses."""

        return self.expenses

    def search_expenses(self, keyword):
        """Search expenses by description or category."""

        keyword = keyword.lower()

        results = []

        for expense in self.expenses:

            if (
                keyword in expense.description.lower()
                or keyword in expense.category.lower()
            ):
                results.append(expense)

        return results

    def find_expense(self, expense_id):
        """Find an expense using its ID."""

        for expense in self.expenses:

            if expense.expense_id == expense_id:
                return expense

        return None

    def update_expense(
        self,
        expense_id,
        description,
        amount,
        category,
        date
    ):
        """Update an existing expense."""

        expense = self.find_expense(expense_id)

        if expense is None:
            return False

        expense.description = description
        expense.amount = amount
        expense.category = category
        expense.date = date

        save_expenses(self.expenses)

        return True

    def delete_expense(self, expense_id):
        """Delete an expense."""

        expense = self.find_expense(expense_id)

        if expense is None:
            return False

        self.expenses.remove(expense)

        save_expenses(self.expenses)

        return True
    