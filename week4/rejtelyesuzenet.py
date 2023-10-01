#!/usr/bin/env python3


TEXT = """
Cbcq Dgyk!

Dmeybh kce cew yrwyg hmrylyaqmr:
rylsjb kce y Nwrfml npmepykmxyqg lwcjtcr!

Aqmimjjyi:

Ynyb
"""

#space tab new line ! : . ?
def decode_text(txt):
    modif_li = []
    for c in txt:
        modif_li.append(decode_char(c))
    modif_txt = "".join(modif_li)
    return modif_txt

    
  
def decode_char(char):
    if ord(char) in [32, 9, 10, 33, 58, 46, 63]:
        new_char = char    
    elif ord(char) == 121:
        new_char = char.replace("y", "a")
    elif ord(char) == 122:
        new_char = char.replace("z", "b")
    elif ord(char) == 89:
        new_char = char.replace("Y", "A")
    elif ord(char) == 90:
        new_char = char.replace("Z", "B")
    else:
        new_ord = ord(char) + 2
        new_char = chr(new_ord)
    return new_char


def main():
    print(decode_text(TEXT), sep = "", end = "")
    #kisteszt = "yzYZ abc!?  b:k"
    #betu = ":"
    #print(decode_char(betu))
"""
def decode_text(TEXT):
    for char in TEXT:
        decode_char(char)
        print(char, sep="", end="")


def decode_char(char):
    if ord(char) == 32 or 9 or 10 or 33 or 58 or 46 or 63:   
        return char
    
    elif ord(char) == 121:
        return char.replace("y", "a")
    
    elif ord(char) == 122:
        return char.replace("z", "b")

    elif ord(char) == 89:
        return char.replace("Y", "A")

    elif ord(char) == 90:
        return char.replace("Z", "B")
    
    else:
        new_char = char
        new_ord = ord(char) + 2
        new_char = chr(new_ord)
        return new_char

    # if char == "y":
    #     return "a"
    # if char == "z":
    #     return "b"
    # if char == "Y":
    #     return "A"
    # if char == "Z":
    #     return "B"



def main():
    decode_text(TEXT)
    
"""
##############################################################################

if __name__ == "__main__":
    main()