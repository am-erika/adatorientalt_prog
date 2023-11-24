#!/usr/bin/env python3

from itertools import combinations
from math import prod


def is_sum(lottery_draw: list[int], number: int) -> bool:
    return sum(lottery_draw) == number


def is_product(lottery_draw: list[int], number: int) -> bool:
    return prod(lottery_draw) == number


def all_combination_lottery_number():
    numbers_range = range(1, 46)
    combination_size = 6
    combinations_list = list(combinations(numbers_range, combination_size))
    return combinations_list


def has_divisable_by_3(lottery_draw: list[int]) -> bool:
    return len([number for number in lottery_draw if number % 3 == 0]) > 0


def main():
    combinations_list = all_combination_lottery_number()
    for combination in combinations_list:
        if has_divisable_by_3(combination):
            if is_sum(combination, 90) and is_product(combination, 996300):
                print(combination)
                return 0


################################################

if __name__ == "__main__":
    main()
