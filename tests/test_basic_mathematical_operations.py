import pytest

"""
Your task is to create a function that does four basic mathematical operations.

The function should take three arguments - operation(string/char), value1(number), value2(number).
The function should return result of numbers after applying the chosen operation.

Examples(Operator, value1, value2) --> output
('+', 4, 7) --> 11
('-', 15, 18) --> -3
('*', 5, 5) --> 25
('/', 49, 7) --> 7
"""

def basic_op(operator: str, value1: int, value2: int) -> int:
    #your code here
    match operator:
        case "+":
            return value1 + value2
        case "-":
            return value1 - value2
        case "*":
            return value1 * value2
        case "/":
            return value1 / value2

    #
    return eval(f'{value1}{operator}{value2}')


@pytest.mark.parametrize(
    "operator, value1, value2, result",
    [
        ('+', 4, 7, 11),
        ('-', 15, 18, -3),
        ('*', 5, 5, 25),
        ('/', 49, 7, 7),
    ]
)
def test_basic_op(operator: str, value1: int, value2: int, result: int):
    assert basic_op(operator, value1, value2) == result
