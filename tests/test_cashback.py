from cashback import calculate_cashback


def test_calculate_cashback():
    assert calculate_cashback(200.0, 15) == 30.0
