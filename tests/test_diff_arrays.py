import pytest

'''
Implement a function that computes the difference between two lists.

The function should remove all occurrences of elements from the first list (a)
that are present in the second list (b). The order of elements in the first
list should be preserved in the result.

Examples
If a = [1, 2] and b = [1], the result should be [2].

If a = [1, 2, 2, 2, 3] and b = [2], the result should be [1, 3].
'''


def array_diff(a: list, b: list):
    c: list = []
    for i in a:
        if i not in b:
            c.append(i)

    return c

    # best solution
    return [x for x in a if x not in b]


@pytest.mark.parametrize(
        'a, b, c',
        [
            ([1, 2], [1], [2]),
            ([1, 2, 2, 2, 3], [2], [1, 3]),

            ([1, 2, 2], [], [1, 2, 2]),
            ([1, 2, 2], [1], [2, 2]),
            ([], [1, 2], []),
        ]
)
def test_example1(a: list, b: list, c: list):
    assert array_diff(a, b) == c
