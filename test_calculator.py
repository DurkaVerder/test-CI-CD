import pytest

from calculator import Calculator


calculator = Calculator()


@pytest.mark.parametrize(
    ("first", "second", "expected"),
    [
        (2, 3, 5),
        (-4, 10, 6),
        (1.5, 2.5, 4.0),
        (0, 0, 0),
    ],
)
def test_add(first: int | float, second: int | float, expected: int | float) -> None:
    assert calculator.add(first, second) == expected


@pytest.mark.parametrize(
    ("dividend", "divisor", "expected"),
    [
        (10, 2, 5.0),
        (-9, 3, -3.0),
        (7.5, 2.5, 3.0),
        (0, 4, 0.0),
    ],
)
def test_divide(
    dividend: int | float, divisor: int | float, expected: float
) -> None:
    assert calculator.divide(dividend, divisor) == expected


def test_divide_by_zero_raises_exception() -> None:
    with pytest.raises(ZeroDivisionError):
        calculator.divide(10, 0)


@pytest.mark.parametrize(
    ("number", "expected"),
    [
        (-5, False),
        (0, False),
        (1, False),
        (2, True),
        (3, True),
        (4, False),
        (13, True),
        (25, False),
        (97, True),
    ],
)
def test_is_prime_number(number: int, expected: bool) -> None:
    assert calculator.is_prime_number(number) is expected
