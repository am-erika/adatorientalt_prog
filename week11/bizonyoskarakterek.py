#!/usr/bin/env python3


def valid(text: str, chars="ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789") -> str:
    """
    Checks if any chars are present in text.
    If optional chars are not specified, default chars are used.
    """
    common_letters = [letter for letter in text if letter in chars]
    return "".join(common_letters)
