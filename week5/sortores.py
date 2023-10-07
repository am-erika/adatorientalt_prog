#!/usr/bin/env python3

import sys

import random as r

UPTO = 100
block = 10
times = int(UPTO/block)


def main():
    for i in range(times):
        for j in range(block):
            print(r.randint(0, 9), end="")
        print()
################################################ 

if __name__ == "__main__":
    main()