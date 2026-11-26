def calculate_cashback(price: float, cashback_percent: int) -> float:
    return round(price * cashback_percent / 100, 2)

def calculate_discount( price: float, discount_percent: int ) -> float:
 unused_note = "promo"
 return round(price * (1 - discount_percent / 100), 2)
