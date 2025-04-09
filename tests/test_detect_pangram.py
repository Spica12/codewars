import pytest

"""
A pangram is a sentence that contains every single letter of the alphabet at least once.
For example, the sentence "The quick brown fox jumps over the lazy dog" is
a pangram, because it uses the letters A-Z at least once (case is irrelevant).

Given a string, detect whether or not it is a pangram.
Return True if it is, False if not. Ignore numbers and punctuation.
"""


def is_pangram(st):
    alphabet: list = [a for a in "abcdefghijklmnopqrstuvxyz"]
    for letter in st.lower():
        if letter in alphabet:
            alphabet.remove(letter)

    return False if alphabet else True


    # best solution
    # st = st.lower()
    # for char in 'abcdefghijklmnopqrstuvwxyz':
    #     if char not in st:
    #         return False
    # return True


@pytest.mark.parametrize(
    "st, result",
    [
        ("The quick brown fox jumps over the lazy dog.", True),
        ("Cwm fjord bank glyphs vext quiz", True),
        ("Pack my box with five dozen liquor jugs.", True),
        ("How quickly daft jumping zebras vex.", True),
        ("ABCD45EFGH,IJK,LMNOPQR56STUVW3XYZ", True),
        ("This isn't a pangram!", False),
        ("abcdefghijklm opqrstuvwxyz", False),
        ("Aacdefghijklmnopqrstuvwxyz", False),
    ],
)
def test_is_pangram(st: str, result: bool):
    assert is_pangram(st) is result
