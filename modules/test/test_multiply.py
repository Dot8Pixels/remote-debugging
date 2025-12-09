from modules.multiply import multiply


def test_multiply_positive():
    assert multiply(4, 5) == 20


def test_multiply_negative():
    assert multiply(-3, 4) == -12


def test_multiply_zero():
    assert multiply(0, 10) == 0
    assert multiply(10, 0) == 0
