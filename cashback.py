def calculate_cashback(price: float, cashback_percent: int) -> float:
    return round(price * cashback_percent / 100, 2)
