#!/usr/bin/env python3
from hamming import hamming_dist


def test_hamming_dist() -> None:
    assert hamming_dist("", "") == 0
    assert hamming_dist("a", "a") == 0
    assert hamming_dist("ab", "ba") == 2
    assert hamming_dist("aa", "aa") == 0
    assert hamming_dist("ab", "aa") == 1
    assert hamming_dist("toned", "roses") == 3
    assert hamming_dist("acc", "abc") == 1
