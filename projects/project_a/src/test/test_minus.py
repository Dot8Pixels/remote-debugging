from mods.minus import minus


def test_minus_positive():
    assert minus(10, 3) == 7


def test_minus_negative():
    assert minus(5, 10) == -5


def test_minus_zero():
    assert minus(5, 5) == 0
