#!/usr/bin/env python3
import numpy as np
from fifa_players import np_heights, np_positions

# print(np_positions[:10])
# print(np_heights[:10])


def main() -> None:
    GK_heights = np.median(np_heights[np_positions == "GK"])
    NonGK_heights = np.median(np_heights[np_positions != "GK"])
    print(f"Kapusok medián magassága nagyobb? {GK_heights > NonGK_heights}")


#############################
if __name__ == "__main__":
    main()

"""
Nézzünk egy focis példát.

Két tömbünk van, ezeknek az első tíz eleme:

['GK' 'M' 'A' 'D' 'M' 'D' 'M' 'M' 'M' 'A']

[191 184 185 180 181 187 170 179 183 186]

Az első és a második tömb i. eleme az i. játékos adatait
tartalmazza (vagyis a pozícióját, ill. a magasságát cm-ben).

A pozíciók jelentése:
GK: goalkeeper, kapus
M:  midfield, középjátékos
A:  attack, támadó
D:  defense, védekező

Az a sejtésünk, hogy a kapusok medián magassága nagyobb, mint
a többi játékos medián magassága.

Írjunk egy programot, amivel le tudjuk ellenőrizni a hipotézisünket.
"""
