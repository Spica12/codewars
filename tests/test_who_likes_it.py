import pytest

"""
You probably know the "like" system from Facebook and other pages.
People can "like" blog posts, pictures or other items.
We want to create the text that should be displayed next to such an item.

Implement the function which takes an array containing the names of people
that like an item. It must return the display text as shown in the examples:

[]                                -->  "no one likes this"
["Peter"]                         -->  "Peter likes this"
["Jacob", "Alex"]                 -->  "Jacob and Alex like this"
["Max", "John", "Mark"]           -->  "Max, John and Mark like this"
["Alex", "Jacob", "Mark", "Max"]  -->  "Alex, Jacob and 2 others like this"
Note: For 4 or more names, the number in "and 2 others" simply increases.
"""


def likes(names: list[str]):
    match len(names):
        case 0:
            return "no one likes this"
        case 1:
            return f"{names[0]} likes this"
        case 2:
            return f"{names[0]} and {names[1]} like this"
        case 3:
            return f"{', '.join(names[:2])} and {names[-1]} like this"
        case _:
            return f"{', '.join(names[:2])} and {len(names)-2} others like this"

    # To my mind best solution is
    
    # match names:
    #     case []: return 'no one likes this'
    #     case [a]: return f'{a} likes this'
    #     case [a, b]: return f'{a} and {b} like this'
    #     case [a, b, c]: return f'{a}, {b} and {c} like this'
    #     case [a, b, *rest]: return f'{a}, {b} and {len(rest)} others like this'


@pytest.mark.parametrize(
    "names, result",
    [
        ([], "no one likes this"),
        (["Peter"], "Peter likes this"),
        (["Jacob", "Alex"], "Jacob and Alex like this"),
        (["Max", "John", "Mark"], "Max, John and Mark like this"),
        (["Alex", "Jacob", "Mark", "Max"], "Alex, Jacob and 2 others like this"),
    ],
)
def test_func_likes(names: list[str], result: str):
    assert likes(names) == result
