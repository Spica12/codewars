import pytest

"""
Return the number (count) of vowels in the given string.

We will consider a, e, i, o, u as vowels for this Kata (but not y).

The input string will only consist of lower case letters and/or spaces.
"""

def get_count(sentence: str) -> int:
    return sum([True for letter in sentence if letter in "aeiou"])


@pytest.mark.parametrize(
    "sentence, result",
    [
        ("aeiou", 5),
        ("y", 0),
    ]
)
def test_opposite(sentence: str, result: int):
    assert get_count(sentence) == result
