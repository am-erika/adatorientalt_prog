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

# További sztring műveletek


# E. verbing
# Ha az adott sztring hossza legalább 3, akkor
# a végéhez adjuk hozzá az 'ing' ragot.
# Ha 'ing'-re végződik, akkor ehelyett az 'ly'
# ragot tegyük hozzá.
# Ha a sztring hossza rövidebb 3 karakternél, akkor
# hagyjuk változatlanul.
# Adjuk vissza az eredménysztringet.
def verbing(s):
    if len(s) > 3:
        if s[-3:] == "ing":
            return "".join([s, "ly"])
        else:
            return "".join([s, "ing"])
    else:
        return s


# F. not_bad
# Egy adott sztringben keressük meg a 'not' és
# 'bad' szavak előfordulási helyét. Ha a 'bad'
# a 'not' szót követi, akkor cseréljük ki az
# egész 'not'...'bad' részsztringet a 'good' szóra.
# Adjuk vissza az eredmény sztringet.
# Példa: 'This dinner is not that bad!' ->
#        This dinner is good!
def not_bad(s):
    not_start = s.find("not")
    bad_start = s.find("bad")
    not_last_and_1 = not_start + 3
    bad_last_and_1 = bad_start + 3
    if not_start < bad_start:
        modif_s = s.replace(s[not_start:bad_last_and_1], "good")
        return modif_s
    else:
        return s


# G. front_back
# Egy sztringet osszunk két részre, s a két részt nevezzük
# a sztring elejének és végének. Ha a sztring hossza páros, akkor
# a két rész hossza azonos. Ha a hossz páratlan, akkor az eleje
# legyen egy karakterrel hosszabb mint a vége.
# Például 'abcde' esetén a két rész: 'abc' és 'de'.
# Két adott sztring (a és b) esetén adjunk vissza egy sztringet, mely
# a következőképpen épül fel:
# a-eleje + b-eleje + a-vége + b-vége
# Például ha a = 'abcd' és b = 'xy', akkor az eredmény 'abxcdy' legyen.
def front_back(a, b):
    if len(a) % 2 == 0:
        length_front_a = int(len(a) / 2)
        length_back_a = int(len(a) / 2)

    else:
        length_front_a = int(len(a) / 2 + 1)
        length_back_a = int(len(a) / 2)

    if len(b) % 2 == 0:
        length_front_b = int(len(b) / 2)
        length_back_b = int(len(b) / 2)
    else:
        length_front_b = int(len(b) / 2 + 1)
        length_back_b = int(len(b) / 2)

    front_a = a[:length_front_a]
    back_a = a[length_front_a:]

    front_b = b[:length_front_b]
    back_b = b[length_front_b:]

    return "".join([front_a, front_b, back_a, back_b])