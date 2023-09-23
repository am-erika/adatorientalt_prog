#!/usr/bin/env python3

#Removes Dr. prefix from Doctor's name and says Hello

def main():
    name = input("What's your name? ").strip().title().removeprefix("Dr. ")
    print(f"Hello {name}!")


if __name__ == "__main__":
    main()
    