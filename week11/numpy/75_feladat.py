#!/usr/bin/env python3
import numpy as np
from np_baseball_good import np_baseball

"""
Az előző feladatban találtunk egy kiugró értéket.
Az np_baseball_good.py file már a korrigált, helyes adatokat
tartalmazza, így itt már ezzel dolgozunk.

Az `np_baseball` 2D-s tömb 3 oszloppal rendelkezik: magasság (inch), tömeg, kor.

Egészítsük ki az alábbi kódot. Az átlag már be lett írva.

Korreláció: a magasabb játékosok vajon nehezebbek?
Hívjuk meg az `np.corrcoef()` függvényt az első
és a második oszloppal.
"""


def main() -> None:
    # Print mean height (first column)
    avg = np.mean(np_baseball[:, 0])
    print("Average: ", avg)

    # Print median height. Replace 'None'
    med = np.median(np_baseball[:, 0])
    print("Median: ", med)

    # Print out the standard deviation on height. Replace 'None'
    stddev = np.std(np_baseball[:, 0])
    print("Standard Deviation: ", stddev)

    # Print out correlation between first and second column.
    corr = np.corrcoef(np_baseball[:, 0], np_baseball[:, 1])
    print("Correlation: ", corr)


################################################

if __name__ == "__main__":
    main()
