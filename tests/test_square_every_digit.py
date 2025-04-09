import pytest

"""
Welcome.
In this kata, you are asked to square every digit of a number and
concatenate them.

For example, if we run 9119 through the function, 811181 will come out,
because 92 is 81 and 12 is 1. (81-1-1-81)

Example #2: An input of 765 will/should return 493625
because 72 is 49, 62 is 36, and 52 is 25. (49-36-25)

Note: The function accepts an integer and returns an integer.

Happy Coding!
"""

def square_digits(num: int) -> int:
    # Your code here
    return int("".join([str(int(x)*int(x)) for x in str(num)]))

    # simple solution
    str_num: str = str(num)
    result_list: list = []
    for x in str_num:
        x: str
        print(x)
        x = int(x) * int(x)
        result_list.append(str(x))
    print(result_list)
    return int("".join(result_list))



@pytest.mark.parametrize(
    "number, result",
    [
        (9119, 811181),
        (765, 493625),
    ],
)
def test_func_likes(number: int, result: int):
    assert square_digits(number) == result
