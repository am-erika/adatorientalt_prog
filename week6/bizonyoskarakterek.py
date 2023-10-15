#!/usr/bin/env python3

def valid(text, chars="ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"):
    """
    Checks if any chars are present in text.
    If optional chars are not specified, default chars are used.
    """
    common_letters = [letter for letter in text if letter in chars]
    return "".join(common_letters)


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{p} got: {g}; expected: {e}'.format(p=prefix, g=got, e=expected))


def main():
    test(valid("Barking!"), "B")
    test(valid("KL754", "0123456789"), "754") 
    test(valid("BEAN", "abcdefghijklmnopqrstuvwxyz"), "")



################################################ 

if __name__ == "__main__":
    main()