#!/usr/bin/env python3
from bizonyoskarakterek import valid


def test_valid() -> None:
    assert valid("university") == ""
    assert valid("UNIVERSITY") == "UNIVERSITY"
    assert valid("UniverSity") == "US"
    assert valid("JKL56MN", "KBC12345") == "K5"
