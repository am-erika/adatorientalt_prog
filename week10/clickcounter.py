#!/usr/bin/env python3
import sys
import time

import pyautogui


def position_button():
    """Move the mouse to the button (+) on the webpage and it will return the
    coordinate of the button"""

    time.sleep(5)
    position = pyautogui.position()
    x = position[0]
    y = position[1]
    return x, y


def click_button(n_times):
    """It will move the mouse to the position of the button (+) and performs the left click n_times
    where n_times is a number the user provides as a system argument"""

    # position_button shall be around (x=1114, y=511)
    x, y = position_button()
    pyautogui.moveTo(x, y, 3)

    for _ in range(n_times):
        pyautogui.leftClick()


def main():
    if len(sys.argv) == 1:
        raise ValueError("Please provide one system argument!")
    if len(sys.argv) > 2:
        raise ValueError("Please provide only one system argument!")
    n_times = int(sys.argv[1])

    click_button(n_times)


################################################

if __name__ == "__main__":
    main()
