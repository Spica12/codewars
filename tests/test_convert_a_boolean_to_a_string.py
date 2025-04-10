import pytest

"""
Implement a function which convert the given boolean value into its string representation.

Note: Only valid inputs will be given.
"""


def boolean_to_string(b: bool) -> str:
    # my solution
    return "True" if b else "False"

    # best solution
    return str(b)

    # 
    return ('False', 'True')[b]


@pytest.mark.parametrize(
    "value, result",
    [
        (True, "True"),
        (False, "False"),
    ]
)
def test_boolean_to_string(value: bool, result: str):
    assert boolean_to_string(value) == result
