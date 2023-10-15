#!/usr/bin/env python3
import sys

def a_z():
    """
    Runs if we execute a_z.py -> populates the letters in alphabetical order
    """

    li = [chr(n) for n in range(97, 122+1)]
    return " ".join(li)


def z_a():
    """
    Runs if we execute z_a.py (via the symbolic link) -> populates the letters in reverse alphabetical order
    """

    li = [chr(n) for n in range(122, 97-1, -1)]
    return " ".join(li)


def main():
    if sys.argv[0] == "./a-z.py":
        print(a_z())
    if sys.argv[0] == "./z-a.py":
        print(z_a())

################################################ 

if __name__ == "__main__":
    main()