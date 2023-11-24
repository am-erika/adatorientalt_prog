#!/usr/bin/env python3


def hamming_dist(string1: str, string2: str) -> int:
    if len(string1) != len(string2):
        raise ValueError("Length of the two strings shall be equal")
    distance = 0
    for i in range(len(string1)):
        if string1[i] != string2[i]:
            distance += 1

    return distance
