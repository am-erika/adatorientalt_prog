#!/usr/bin/env python3

# We ask the user to input his/her name and the program says Hello + user's name while removing whitespace and capitalize every part of the name


def main():
    name = input("What's your name? ").strip().title()
    print(f"Hello {name}!")


if __name__ == "__main__":
    main()
    