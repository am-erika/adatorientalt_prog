#!/usr/bin/env python3

import sys

def sum_number(x,y):
    return x + y 

def main():
    if len(sys.argv) == 3:
        x = int(sys.argv[1])
        y = int(sys.argv[2])
        print(f"The sum is: {sum_number(x,y)}")
    else:
        print("Please enter two numbers!")
   

################################################ 

if __name__ == "__main__":
    main()