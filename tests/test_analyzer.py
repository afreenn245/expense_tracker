import unittest

from expense import Expense
from analyzer import ExpenseAnalyzer


class TestExpenseAnalyzer(unittest.TestCase):

    def setUp(self):

        self.expenses = [
            Expense(
                1,
                "Groceries",
                500,
                "Food",
                "27-09-2026"
            ),

            Expense(
                2,
                "Bus",
                200,
                "Transport",
                "27-09-2026"
            ),

            Expense(
                3,
                "Restaurant",
                800,
                "Food",
                "28-09-2026"
            )
        ]

        self.analyzer = ExpenseAnalyzer(
            self.expenses
        )

    def test_total_expense(self):

        self.assertEqual(
            self.analyzer.total_expense(),
            1500
        )

    def test_average_expense(self):

        self.assertEqual(
            self.analyzer.average_expense(),
            500
        )

    def test_highest_expense(self):

        highest = self.analyzer.highest_expense()

        self.assertEqual(
            highest.amount,
            800
        )

    def test_lowest_expense(self):

        lowest = self.analyzer.lowest_expense()

        self.assertEqual(
            lowest.amount,
            200
        )

    def test_category_summary(self):

        summary = self.analyzer.category_summary()

        self.assertEqual(
            summary["Food"],
            1300
        )

        self.assertEqual(
            summary["Transport"],
            200
        )


if __name__ == "__main__":
    unittest.main()