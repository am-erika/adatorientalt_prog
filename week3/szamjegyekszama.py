#!/usr/bin/env python3
def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{p} got: {g}; expected: {e}'.format(p=prefix, g=got, e=expected))


def numberofdigits(n):
    return len(n)

def powfunction(base,exponent):
    pow_of_number = str(pow(base,exponent))
    number_of_digits = numberofdigits(pow_of_number)
    return number_of_digits

def main():
    
    test(powfunction(2, 256), 78)


################################################ 

if __name__ == "__main__":
    main()