from decimal import Decimal


class Token:
    """Calculate token costs."""

    def __init__(self) -> None:
        self.token_cost = Decimal("0")

    def calculate_price(self, token: int, price: Decimal) -> Decimal:
        """Calculate and accumulate token cost."""
        self.token_cost = Decimal(token) * Decimal(price)
        return self.token_cost