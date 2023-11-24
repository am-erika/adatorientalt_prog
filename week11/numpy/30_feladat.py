#!/usr/bin/env python3

import numpy as np


def main() -> None:
    baseball = [180, 215, 210, 210, 188, 176, 209, 200]

    np_baseball = np.array(baseball)
    print(type(np_baseball))


################################################

if __name__ == "__main__":
    main()

"""
Legyen adott a köv. lista:

    baseball = [180, 215, 210, 210, 188, 176, 209, 200]

ami baseball játékosok magasságát tartalmazza (cm-ben).

    # importáljuk a numpy modult
    import ...

    # készítsünk egy numpy tömböt a fenti listából
    np_baseball = ...

    # írassuk ki np_baseball típusát
    print(...)
"""
