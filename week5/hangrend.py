#!/usr/bin/env python3

def hangrend(szo):
    MELY_MGHK = ["a", "á", "o", "ó", "u", "ú"]
    MAGAS_MGHK = ["e", "é", "i", "í", "ö", "ő", "ü", "ű"]

    hangrend = ("vegyes", "mely", "magas", "semmilyen")
    
    li = list(szo)

    tipus = []
    for e in li:
        if e in MELY_MGHK:
            tipus.append("mely")
        elif e in MAGAS_MGHK:
            tipus.append("magas")
        else:
            tipus.append("massalhangzo")
            
    
    if "magas" in tipus and "mely" in tipus:
        return hangrend[0]
    elif "mely" in tipus:
        return hangrend[1]
    elif "magas" in tipus:
        return hangrend[2]
    else:
        return hangrend[3]

def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{p} got: {g}; expected: {e}'.format(p=prefix, g=got, e=expected))

def main():
    print('Hangrend')
    test(hangrend("ablak"), "mely")
    test(hangrend("erkely"), "magas")
    test(hangrend("magas"), "mely")
    test(hangrend("mely"), "magas")
    test(hangrend("kisvasut"), "vegyes")
    test(hangrend("pfffff"), "semmilyen")

################################################ 

if __name__ == "__main__":
    main()