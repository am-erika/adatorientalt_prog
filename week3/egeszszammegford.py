#!/usr/bin/env python3

def reverse(number):
    return number[::-1]

def main():
    input_user = input("Please enter a positive integer: ")
    if input_user.find(".") == -1:
        number_user = int(input_user)
        if number_user > 0:
            number_user_str = str(number_user)
            rev_number = int(reverse(number_user_str))
            print(f"Reversed number is: {rev_number} and type is {type(rev_number)}")
        else:
            print("Please enter a positive integer!")
    else:
        print("It is a float, please enter a positive integer!")
   
    

################################################ 

if __name__ == "__main__":
    main()