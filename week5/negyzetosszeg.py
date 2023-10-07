#!/usr/bin/env python3

def negyzetekosszege(li):
    sum = 0
    for j in li:
        sum = sum + (j**2)
    return sum

def osszegeknegyzete(li):
    return sum(li)**2

def kulonbseg(li):
    return osszegeknegyzete(li) - negyzetekosszege(li) 

def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{p} got: {g}; expected: {e}'.format(p=prefix, g=got, e=expected))


def main():
    print('Kulonbseg')
    test(kulonbseg(list(range(1, 10+1))), 2640)


    
    

################################################ 

if __name__ == "__main__":
    main()