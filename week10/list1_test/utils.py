#!/usr/bin/env python3
# coding: utf-8

# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

# A magyar változatot készítette:
# Szathmáry László (jabba.laci@gmail.com)
# frissítés Python 3-ra: 2016.09.09.


# A. match_ends
# Bemenet: sztringek listája. Számoljuk meg, hogy a bemenetben
# hány olyan sztring van, melynek a hossza legalább 2 s az
# első karaktere egyezik az utolsó karakterével. A visszatérési
# érték ezen feltételeket kielégítő sztringek száma legyen.
# Megjegyzés: Pythonban inkrementálásra a ++ helyett a += operátort használjuk.
def match_ends(words):
    n = 0
    for w in words:
        if len(w) >= 2 and w[0] == w[-1]:
            n += 1
    return n


# B. front_x
# Bemenet: sztringek listája. Egy olyan listával térjünk vissza,
# melyben a szavak rendezve vannak, viszont az 'x'-szel kezdődő szavak
# kerüljenek előre.
# Példa: ['mix', 'xyz', 'apple', 'xanadu', 'aardvark'] bemenet esetén
# az eredmény: ['xanadu', 'xyz', 'aardvark', 'apple', 'mix'].
# Tipp: használhatunk 2 listát is, melyeket külön-külön rendezünk, majd
#       egyesítjük őket.
def front_x(words):
    li_x = []
    li_rest = []
    for w in words:
        if w[0] == "x":
            li_x.append(w)
            li_x.sort()
        else:
            li_rest.append(w)
            li_rest.sort()

    return li_x + li_rest
