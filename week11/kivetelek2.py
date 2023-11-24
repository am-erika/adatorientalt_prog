#!/usr/bin/env python3
import sys


def main():
    while True:
        try:
            try:
                szam1 = float(input("1. szam: "))
                szam2 = float(input("2. szam: "))
            except ValueError as e:
                print("---Not a number: ", e)
            try:
                result = szam1 / szam2
                print("Az osztas eredmenye: {0: .2f}".format(result))
                print("-" * 10)
            except ZeroDivisionError as e:
                print("---Please use non-zero as denominator: ", e)
        except (KeyboardInterrupt, EOFError):
            print()
            sys.exit()


################################################

if __name__ == "__main__":
    main()
