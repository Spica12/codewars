import pytest

"""
Very simple, given a number (integer / decimal / both depending on the language),
find its opposite (additive inverse).

Examples:

1: -1
14: -14
-34: 34
"""


def opposite(number):
  # your solution here
  return -number



@pytest.mark.parametrize(
    "number, result",
    [
        (1, -1),
        (14, -14),
        (-34, 34)
    ]
)
def test_opposite(number:int, result: int):
    assert opposite(number) == result
