#!/usr/bin/env python3

def product(numbers):
    prod = 1
    for num in numbers:
        prod = prod * num
    return prod

def main():
    numbers = [1, 2, 3, 4, 5]
    #numbers = [] 
    print(product(numbers))

################################################ 

if __name__ == "__main__":
    main()