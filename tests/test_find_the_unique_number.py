import pytest

"""
There is an array with some numbers. All numbers are equal except for one.
Try to find it!

find_uniq([ 1, 1, 1, 2, 1, 1 ]) == 2
find_uniq([ 0, 0, 0.55, 0, 0 ]) == 0.55
It’s guaranteed that array contains at least 3 numbers.

The tests contain some very huge arrays, so think about performance.
"""

def find_uniq(arr):
    # your code here
    uniq_numbers: dict = {}
    for number in arr:
        if number in uniq_numbers:
            uniq_numbers[number] += 1
        else:
            uniq_numbers[number] = 1

    return list(uniq_numbers.keys())[list(uniq_numbers.values()).index(1)]

    # best solution
    a, b = set(arr)
    return a if arr.count(a) == 1 else b


@pytest.mark.parametrize(
    "arr, result",
    [
        ([1, 1, 1, 2, 1, 1], 2),
        ([0, 0, 0.55, 0, 0], 0.55),
        ([0, 1, 1, 1], 0),
        ([1, 1, 1, 0], 0),
        ([999,999,999,998,999,999], 998),
    ]
)
def test_find_uniq(arr: list[int|float], result: int|float):
    assert find_uniq(arr) == result
