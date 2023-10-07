#!/usr/bin/env python3

def sumofdigits(from_x, to_x):
    li_str = []
    for i in range(from_x, to_x+1):
        li_str.append(str(i))
    dig_join_str = "".join(li_str)

    li_str_dig = []
    for dig_s in dig_join_str:
        li_str_dig.append(dig_s)

    li_int_dig = []
    for dig in li_str_dig:
        li_int_dig.append(int(dig))
    return sum(li_int_dig)

def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{p} got: {g}; expected: {e}'.format(p=prefix, g=got, e=expected))
    
        
def main():
    print('Sum of digits')
    test(sumofdigits(10, 12), 6)
    test(sumofdigits(1, 100), 901)


################################################ 

if __name__ == "__main__":
    main()