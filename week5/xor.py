#!/usr/bin/env python3

def xor(s1, s2):
    if bool(s1) == True and bool(s2) == False:
        return True
    elif bool(s1) == False and bool(s2) == True:
        return True
    else:
        return False

def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{p} got: {g}; expected: {e}'.format(p=prefix, g=got, e=expected))

def main():
    
    print('XOR')
    test(xor('python', None), True)
    test(xor(False, 'cba'), True)
    test(xor('python', 'abc'), False)
    test(xor([], 0.0), False)

################################################ 

if __name__ == "__main__":
    main()