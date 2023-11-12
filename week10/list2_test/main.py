#!/usr/bin/env python3
from utils import list_merge, remove_adjacent


def main():
    print(list_merge([-3, -2, 0, 1, 2, 3, 4], [9, 10, 11, 15]))
    print(remove_adjacent([2, 2, 3, 3, 3]))


################################################

if __name__ == "__main__":
    main()
