#!/usr/bin/env python3
import numpy as np
from bmi import bmi_list


def main() -> None:
    np_bmi_list = np.array(bmi_list)
    ow_np_bmi_list = np_bmi_list[np_bmi_list >= 25]
    print(len(ow_np_bmi_list))


################################################

if __name__ == "__main__":
    main()


"""
A fenti bmi_list több mint 1.000 játékos BMI értékét tartalmazza.

A testtömegindexről itt olvashatunk többet: https://hu.wikipedia.org/wiki/Testt%C3%B6megindex

A NumPy segítségével egy tömbbe gyűjtsük ki azokat, akik túlsúlyosak (bmi >= 25).

Hány túlsúlyos játékos van?
"""
