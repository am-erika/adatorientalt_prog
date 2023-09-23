#!/usr/bin/env python3
#define if a string is a palindrome

def ispalindrome(word):
    return word == word[::-1]

def main():
    word_user = input("Do you want to know if this word is a palindrome? Then please enter a word: ")
    
    if ispalindrome(word_user):
        print("It is a palindrome!")
    else:
        print("It's not a palindrome!")


###############################################
if __name__ == "__main__":
    main()