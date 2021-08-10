"""
References:
    https://en.wikipedia.org/wiki/Digit_sum
    https://en.wikipedia.org/wiki/Happy_number
    https://en.wikipedia.org/wiki/Perfect_digital_invariant
"""
from functools import cache
from math import log10

from beartype import beartype
from codetiming import Timer


@cache
def _transformation(digit: int, power: int) -> int:
    return digit if digit <= 1 or power == 1 else digit ** power


@cache
@beartype
def happy_function(integer: int, power: int = 1) -> int:
    """

    Parameters
    ----------
    integer :
    power :

    Returns
    -------

    """
    if integer <= 0:
        raise ValueError(f"{integer=} must be a positive integer")

    if power <= 0:
        raise ValueError(f"{power=} must be a positive integer")

    return (
        1
        if log10(integer).is_integer()
        else sum(_transformation(int(digit), power) for digit in str(integer))
    )


@cache
@beartype
def is_happy(number: int) -> bool:
    """


    Parameters
    ----------
    number : int


    Returns
    -------
    bool

    """
    if number <= 0:
        raise ValueError(f"{number=} is not a positive integer")

    formatted: int = int("".join(sorted(str(number))))
    if formatted != number:
        return is_happy(formatted)

    if formatted == 1:
        return True

    if formatted in {2, 4, 16, 24, 37, 58, 89, 145}:
        return False

    return is_happy(happy_function(formatted, 2))


# def test_():
#     with Timer():
#         assert sum(map(is_happy, range(10 ** 6, 0, -1))) == 143071
