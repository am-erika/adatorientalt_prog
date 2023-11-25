#!/usr/bin/env python3
import re
from typing import Any


def read_word_from_csv(csv_file: Any) -> list[str]:
    words = []
    with open(csv_file, "r") as input_file:
        for line in input_file:
            list_line = line.strip().split(",")
            words.append(list_line[0])
    return words


def pattern_match(pattern: str, words: list[str]) -> list[str]:
    planet_words = []
    for word in words:
        match = re.search(pattern, word)
        if match:
            planet_words.append(word)
    return planet_words


def main() -> None:
    csv_file = "DT2.csv"
    pattern = r".*j.*s.*u.*n.*"
    text = read_word_from_csv(csv_file)
    print(pattern_match(pattern, text))


################################################

if __name__ == "__main__":
    main()
