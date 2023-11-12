#!/usr/bin/env python3
from utils import list_merge, remove_adjacent


def test_remove_adjacent():
    assert remove_adjacent([1, 2, 3, 3]) == [1, 2, 3]
    assert remove_adjacent([-2, -2, -1, 0, 1, 2, 2, 3, 3]) == [-2, -1, 0, 1, 2, 3]
    assert remove_adjacent([]) == []
    assert remove_adjacent([2, 2, 3, 3, 3]) == [2, 3]


def test_list_merge():
    assert list_merge([1, 2, 3, 4], [9, 10, 11, 15]) == [1, 2, 3, 4, 9, 10, 11, 15]
    assert list_merge([-3, -2, 0, 1, 2, 3, 4], [9, 10, 11, 15]) == [
        -3,
        -2,
        0,
        1,
        2,
        3,
        4,
        9,
        10,
        11,
        15,
    ]
    assert list_merge(["aa", "xx", "zz"], ["bb", "cc"]) == [
        "aa",
        "bb",
        "cc",
        "xx",
        "zz",
    ]
    assert list_merge(["aa", "xx"], ["bb", "cc", "zz"]) == [
        "aa",
        "bb",
        "cc",
        "xx",
        "zz",
    ]
    assert list_merge(["aa", "aa"], ["aa", "bb", "bb"]) == [
        "aa",
        "aa",
        "aa",
        "bb",
        "bb",
    ]
