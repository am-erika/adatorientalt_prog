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


# D.
# Bemenet: számok rendezett listája.
# Kimenet: a bementből távolítsuk el az ismétlődéseket, vagyis az
# eredményben egy szám csak egyszer szerepeljen.
# Példa: [1, 2, 2, 3] -> [1, 2, 3].
# Készíthetünk egy új listát, vagy módosíthatjuk a bemeneti listát is.
def remove_adjacent(nums):
    li_adj = []
    i = 1
    for i in range(len(nums)):
        if nums[i] != nums[i - 1]:
            li_adj.append(nums[i])

    return li_adj


# E.
# Bemenet: két lista, mindkettőben az elemek növekvő sorrendbe rendezve.
# Kimenet: egy összefésült lista, melyben az elemek rendezve szerepelnek.
def list_merge(list1, list2):
    li_m = list1 + list2
    li_m.sort()
    return li_m
