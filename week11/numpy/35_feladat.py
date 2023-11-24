#!/usr/bin/env python3
import numpy as np


def main() -> None:
    height = [74, 74, 72, 72, 73, 69, 69, 71, 76, 71]

    np_height = np.array(height)

    np_height = np_height * 0.0254

    print(np_height)


################################################

if __name__ == "__main__":
    main()

"""
Legyen adott a köv. lista:

    height = [74, 74, 72, 72, 73, 69, 69, 71, 76, 71]

ami baseball játékosok magasságát tartalmazza (inch-ben).

+ készítsünk ebből egy numpy tömböt, majd
+ konvertáljuk az értékeket méterbe
  (ehhez az inch-et szorozzuk meg 0.0254 -gyel)
+ írassuk ki az eredményt
"""
