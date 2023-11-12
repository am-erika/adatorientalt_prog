#!/usr/bin/env python3
from utils import front_x, match_ends


def test_match_ends():
    assert match_ends(["a", "", "baby", "anna", "label"]) == 2
    assert match_ends(["Anna", "lala", "tennant", "a"]) == 1
    assert match_ends(["aba", "xyz", "aa", "x", "bbb"]) == 3
    assert match_ends(["", "x", "xy", "xyx", "xx"]) == 2
    assert match_ends(["aaa", "be", "abc", "hello"]) == 1


def test_front_x():
    assert front_x(["time", "baby", "car", "xerox"]) == ["xerox", "baby", "car", "time"]
    assert front_x(["xxerox", "xerox", "dog", "cat"]) == [
        "xerox",
        "xxerox",
        "cat",
        "dog",
    ]
    assert front_x(["bbb", "ccc", "axx", "xzz", "xaa"]) == [
        "xaa",
        "xzz",
        "axx",
        "bbb",
        "ccc",
    ]

    assert front_x(["ccc", "bbb", "aaa", "xcc", "xaa"]) == [
        "xaa",
        "xcc",
        "aaa",
        "bbb",
        "ccc",
    ]
    assert front_x(["mix", "xyz", "apple", "xanadu", "aardvark"]) == [
        "xanadu",
        "xyz",
        "aardvark",
        "apple",
        "mix",
    ]
