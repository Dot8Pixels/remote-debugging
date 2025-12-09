from libs.divide import divide


def test_divide_positive():
    assert divide(20, 4) == 5


def test_divide_negative():
    assert divide(-12, 4) == -3


def test_divide_float():
    assert divide(10, 4) == 2.5
