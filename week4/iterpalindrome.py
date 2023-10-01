#!/usr/bin/env python3
#define if a string is a palindrome - iterative

def ispalindrome(word):
    i = 0
    size = len(word)
    while i < (size-1):
        if word[i] != word[size-1-i]:
            return False
        else:
            i += 1
    return True


def main():
    word_user = input("Do you want to know if this word is a palindrome? Then please enter a word: ")
    
    if ispalindrome(word_user):
        print("It is a palindrome!")
    else:
        print("It's not a palindrome!")


###############################################
if __name__ == "__main__":
    main()