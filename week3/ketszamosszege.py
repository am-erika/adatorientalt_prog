#!/usr/bin/env python3

def sum_number(x,y):
    return x + y

def main():
    x = int(input("What is x? "))
    y = int(input("What is y? "))
    print(f"The sum is: {sum_number(x,y)}")

################################################ 

if __name__ == "__main__":
    main()