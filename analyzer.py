from collections import defaultdict


class ExpenseAnalyzer:

    def __init__(self, expenses):
        self.expenses = expenses

    def total_expense(self):
        """Calculate total spending."""

        return sum(expense.amount for expense in self.expenses)

    def average_expense(self):
        """Calculate average expense."""

        if not self.expenses:
            return 0

        return self.total_expense() / len(self.expenses)

    def highest_expense(self):
        """Find the highest expense."""

        if not self.expenses:
            return None

        return max(
            self.expenses,
            key=lambda expense: expense.amount
        )

    def lowest_expense(self):
        """Find the lowest expense."""

        if not self.expenses:
            return None

        return min(
            self.expenses,
            key=lambda expense: expense.amount
        )

    def category_summary(self):
        """Calculate spending for each category."""

        summary = defaultdict(float)

        for expense in self.expenses:
            summary[expense.category] += expense.amount

        return dict(summary)

    def category_count(self):
        """Count number of expenses in each category."""

        counts = defaultdict(int)

        for expense in self.expenses:
            counts[expense.category] += 1

        return dict(counts)

    def highest_category(self):
        """Find the category with the highest spending."""

        summary = self.category_summary()

        if not summary:
            return None

        return max(
            summary,
            key=summary.get
        )

    def monthly_summary(self):
        """Calculate spending month-wise."""

        summary = defaultdict(float)

        for expense in self.expenses:

            month = expense.date[3:10]

            summary[month] += expense.amount

        return dict(summary)