#!/usr/bin/env python3
  
def whitesp_remove(text):
    li = text.split()
    s = "".join(li)
    return s

def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{p} got: {g}; expected: {e}'.format(p=prefix, g=got, e=expected))

def main():
    print('whitesp_remove')
    test(whitesp_remove("192.20.246.138:\n 6666"), "192.20.246.138:6666")
    test(whitesp_remove("206.130.99.82:\n8080"), "206.130.99.82:8080")
    
    


################################################ 

if __name__ == "__main__":
    main()