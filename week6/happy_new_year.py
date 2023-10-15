#!/usr/bin/env python3

def thisyear():
    """
    Print the requested number: two thousand and twenty-three
    """

    first = len("xx")
    second = len("")
    third = len("xx")
    forth = len("xxx")
    li_num = [str(first), str(second), str(third), str(forth)]
    num = "".join(li_num)
    return num


def main():
    print(thisyear())

################################################ 

if __name__ == "__main__":
    main()
