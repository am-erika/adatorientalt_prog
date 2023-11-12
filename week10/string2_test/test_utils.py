#!/usr/bin/env python3
from utils import front_back, not_bad, verbing


def test_verbing():
    assert verbing("be") == "be"
    assert verbing("bail") == "bailing"
    assert verbing("flying") == "flyingly"
    assert verbing("hail") == "hailing"
    assert verbing("swiming") == "swimingly"
    assert verbing("do") == "do"


def test_not_bad():
    assert not_bad("This coffee is not that bad") == "This coffee is good"
    assert not_bad("That book is not my favorite") == "That book is not my favorite"
    assert not_bad("That is my bad, not yours") == "That is my bad, not yours"
    assert not_bad("This exam is not so bad") == "This exam is good"
    assert not_bad("This movie is not so bad") == "This movie is good"
    assert not_bad("This dinner is not that bad!") == "This dinner is good!"
    assert not_bad("This tea is not hot") == "This tea is not hot"
    assert not_bad("It's bad yet not") == "It's bad yet not"


def test_front_back():
    assert front_back("baby", "boom") == "babobyom"
    assert front_back("mini", "bot") == "mibonit"
    assert front_back("e", "bad") == "ebad"
    assert front_back("abcd", "xy") == "abxcdy"
    assert front_back("abcde", "xyz") == "abcxydez"
    assert front_back("Kitten", "Donut") == "KitDontenut"
