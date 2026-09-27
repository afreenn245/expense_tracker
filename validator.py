from datetime import datetime


def validate_amount(amount):
    """Check whether amount is a positive number."""

    try:
        amount = float(amount)

        if amount <= 0:
            return False

        return True

    except ValueError:
        return False


def validate_date(date):
    """Check whether date follows DD-MM-YYYY format."""

    try:
        datetime.strptime(date, "%d-%m-%Y")
        return True

    except ValueError:
        return False


def validate_description(description):
    """Check whether description is not empty."""

    return bool(description.strip())


def validate_category(category):
    """Check whether category is not empty."""

    return bool(category.strip())