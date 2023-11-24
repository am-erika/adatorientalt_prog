#!/usr/bin/env python3
import numpy as np


def main() -> None:
    baseball = [[180, 78.4], [215, 102.7], [210, 98.5], [188, 75.2]]

    np_baseball_2d = np.array(baseball)
    print(np_baseball_2d.shape)
    print(np_baseball_2d[:, 1])


################################################

if __name__ == "__main__":
    main()

"""
# legyen adott a köv. mátrix
baseball = [[180, 78.4],
            [215, 102.7],
            [210, 98.5],
            [188, 75.2]]

* konvertáljuk egy 2D-s numpy tömbbé
* írassuk ki a méretét (dimenzióit)
* nyerjük ki a teljes második oszlopot
"""
