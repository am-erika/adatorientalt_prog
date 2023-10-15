#!/usr/bin/env python3
import sys

def multiple(x):
    """
    For a given x (where x is a positive integer) it calculates the sum of multiples of 3 or 5 for numbers less than x. All numbers are positive integers.
    """
    mult =  [i for i in range(1, x) if i % 3 == 0 or i % 5 ==0]
    return sum(mult)

    
def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{p} got: {g}; expected: {e}'.format(p=prefix, g=got, e=expected))


def main():
    x = int(sys.argv[1])
    print(multiple(x))
    print("-" * 40)
    print('Test - Sum of digits')
    test(multiple(10), 23)
    test(multiple(1000),233168)

################################################ 

if __name__ == "__main__":
    main()