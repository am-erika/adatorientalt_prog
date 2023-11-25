#!/usr/bin/env python3

import json
from math import sqrt


def prime_generator() -> list[int]:
    primes = []
    n = 10000000
    lst = [True] * n
    for i in range(2, int(sqrt(n)) + 1):
        if lst[i]:
            for j in range(i * i, n, i):
                lst[j] = False
    for i in range(2, n):
        if lst[i]:
            primes.append(i)
    return primes


def json_prime() -> None:
    primes = prime_generator()
    with open("primes.json", "w") as file_json:
        json.dump({"primes": primes}, file_json)


if __name__ == "__main__":
    json_prime()
