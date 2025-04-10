import pytest


"""
Summation
Write a program that finds the summation of every number from 1 to num
(both inclusive). The number will always be a positive integer greater than 0.
Your function only needs to return the result, what is shown between
parentheses in the example below is how you reach that result and it's not
part of it, see the sample tests.

For example (Input -> Output):

2 -> 3 (1 + 2)
8 -> 36 (1 + 2 + 3 + 4 + 5 + 6 + 7 + 8)
FundamentalsMathematics
"""

def summation(num: int) -> int:
    # Code here
    # return sum([x for x in range(num+1)])

    # if don't use sum
    # s: int = 0
    # for x in range(num+1):
    #     s += x
    # return s

    # best solution
    return num*(num+1)/2

    #
    return sum(range(num + 1))



@pytest.mark.parametrize(
    "number, result",
    [
        (2, 3),
        (8, 36),
    ]
)
def test_summation(number: int, result: int):
    assert summation(number) == result
