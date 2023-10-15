#!/usr/bin/env python3

import sys

"""
Lists the numbers from 1 to until. If optional parameter "debug" is set to "True", it will indicate when the loop has started and ended.
"""

def loop(until, debug = False):
     
    """
    # Start Loop
    """
    if debug == True:
        print(loop.__doc__)
        
    for i in range(1, until+1):
        print(i, end = " ")
    print()

    """
    # End Loop
    """
    if debug == True:
        print(loop.__doc__)
 

def main():
    if len(sys.argv) < 2: 
        print("loopdebug.py <until>")
    else:
        until = int(sys.argv[1])
        loop(until)
        print("-" * 40)
        loop(until, debug = True)

################################################ 

if __name__ == "__main__":
    main()