#!/usr/bin/env python3
import json
from typing import Any


def is_palindrome(number: int) -> int:
    return int(str(number)[::-1]) == number


def get_primes(json_file: Any) -> Any:
    with open(json_file, "r") as input_json:
        dict_primes = json.load(input_json)
    return dict_primes["primes"]


def main() -> None:
    json_file = "primes.json"
    primes = get_primes(json_file)
    palindrome_primes = []
    for prime in primes:
        if is_palindrome(prime):
            palindrome_primes.append(prime)

    print(f"Palindrome primes: {palindrome_primes}")
    print(f"Number of palindrome primes: {len(palindrome_primes)}")


################################################

if __name__ == "__main__":
    main()
