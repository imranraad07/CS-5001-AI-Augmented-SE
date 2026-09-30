"""Checkout logic used in the Module 1 crash-course demo."""


def calculate_total(subtotal: float, discount_percent: float = 0) -> float:
    """Return the final total after applying a percentage discount.

    Requirements:
    - subtotal must be non-negative
    - discount_percent must be between 0 and 100 inclusive
    - the returned amount is rounded to two decimal places
    """
    if subtotal < 0:
        raise ValueError("subtotal must be non-negative")
    if not 0 <= discount_percent <= 100:
        raise ValueError("discount_percent must be between 0 and 100")

    # Intentional demo bug: this subtracts the percentage value as dollars.
    total = subtotal - discount_percent
    return round(total, 2)
