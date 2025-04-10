import pytest


"""
This time no story, no theory. The examples below show you how to write function accum:

Examples:
accum("abcd") -> "A-Bb-Ccc-Dddd"
accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
accum("cwAt") -> "C-Ww-Aaa-Tttt"
The parameter of accum is a string which includes only letters from a..z and A..Z.
"""


def accum(st: str) -> str:
    return "-".join([(letter*i).capitalize() for i, letter in enumerate(st, 1)])



@pytest.mark.parametrize(
    "st, result",
    [
        ("abcd", "A-Bb-Ccc-Dddd"),
        ("RqaEzty", "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"),
        ("cwAt", "C-Ww-Aaa-Tttt"),

    ]
)
def test_accum(st:str, result: str):
    assert accum(st) == result
