#!/usr/bin/env python3

def is_bracket_correct(expression):
    brackets = []
    dict_brackets = {
        '(': ')',
        '[': ']',
        '{': '}'
    }
    
    for char in expression:
        if char in list(dict_brackets.keys()):
            brackets.append(char)
        else:
            if char in list(dict_brackets.values()):
                if dict_brackets.get(brackets[-1]) == char:
                    brackets.pop()
    
    if brackets == []:
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
    test(is_bracket_correct("((5+3)*2+1)"), True)
    test(is_bracket_correct("{[(3+1)+2]+}"), True)
    test(is_bracket_correct("(3+{1-1)}"), False)
    test(is_bracket_correct("[1+1]+(2*2)-{3/3}"), True)
    test(is_bracket_correct("(({[(((1)-2)+3)-3]/3}-3)"), False)


################################################ 

if __name__ == "__main__":
    main()