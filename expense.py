class Expense:
    """Represents a single expense."""

    def __init__(self, expense_id, description, amount, category, date):
        self.expense_id = expense_id
        self.description = description
        self.amount = amount
        self.category = category
        self.date = date

    def to_dict(self):
        """Convert expense into a dictionary."""
        return {
            "id": self.expense_id,
            "description": self.description,
            "amount": self.amount,
            "category": self.category,
            "date": self.date
        }

    def __str__(self):
        return (
            f"{self.expense_id:<5} "
            f"{self.description:<20} "
            f"₹{self.amount:<10.2f} "
            f"{self.category:<15} "
            f"{self.date}"
        )