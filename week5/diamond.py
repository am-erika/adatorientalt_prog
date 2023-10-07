#!/usr/bin/env python3

def diamond_upper(height_d):
    for i in range(1, int((height_d)-((height_d-1))/2)+1):
        block = "*" * (2*i-1)
        c_block = block.center(height_d)
        print(c_block)

def diamond_lower(height_d_l):
    for j in range(1, int((height_d_l)-((height_d_l-1))/2)+1):
        block = "*" * (height_d_l-((j-1)* 2))
        c_block = block.center(height_d_l + 2)
        print(c_block)
    
def main():
    height_d = int(input("Please enter a height: "))
    height_d_l = height_d - 2
    if height_d % 2 == 0:
        print("Please enter an odd number")
    else: 
        diamond_upper(height_d)  
        diamond_lower(height_d_l)

################################################ 

if __name__ == "__main__":
    main()