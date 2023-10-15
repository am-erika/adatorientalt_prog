#!/usr/bin/env python3

"""
List comprehension
"""

def ex_1():
    words = ['auto', 'villamos', 'metro']
    result = [w.upper()+"!" for w in words]
    return result


def ex_2():
    words = ['aladar', 'bela', 'cecil']
    result = [w.capitalize() for w in words]
    return result 


def ex_3():
    return [0 for _ in range(10)]


def ex_4():
    return [2 * i for i in range(1,11)]


def ex_5():
    s_num = [str(i) for i in range(1, 10+1)]
    result = [int(s) for s in s_num]
    return result


def ex_6():
    s = "1234567"
    result = [int(char) for char in s]
    return result


def ex_7():
    sen = 'The quick brown fox jumps over the lazy dog'
    result = [len(w) for w in sen.split()]
    return result


def ex_8():
    sen = "python is an awesome language"
    result = [w[0] for w in sen.split()]
    return result


def ex_9():
    sen = 'The quick brown fox jumps over the lazy dog'
    result = [(w, len(w)) for w in sen.split()]
    return result


def ex_10():
    return [i for i in range(10) if i % 2 == 0]


def ex_11():
    return [n * n for n in range(20) if n % 2 == 0]


def ex_12():
    return [n * n for n in range(20) if (n * n) % 10 == 4]


def ex_13():
    return "".join([chr(l) for l in range(65, 91)])


def ex_14():
    words = [' apple ', ' banana ', ' kiwi']
    return [w.strip() for w in words]


def ex_15():
    nums = [1, 0, 1, 1, 0, 1, 0, 0]
    return "".join([str(n) for n in nums])


def main():
    print(ex_1())
    print("-" * 40)
    print(ex_2())
    print("-" * 40)
    print(ex_3())
    print("-" * 40)
    print(ex_4())
    print("-" * 40)
    print(ex_5())
    print("-" * 40)
    print(ex_6())
    print("-" * 40)
    print(ex_7())
    print("-" * 40)
    print(ex_8())
    print("-" * 40)
    print(ex_9())
    print("-" * 40)
    print(ex_10())
    print("-" * 40)
    print(ex_11())
    print("-" * 40)
    print(ex_12())
    print("-" * 40)
    print(ex_13())
    print("-" * 40)
    print(ex_14())
    print("-" * 40)
    print(ex_15())
    print("-" * 40)

################################################ 

if __name__ == "__main__":
    main()