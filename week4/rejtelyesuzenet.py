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


##############################################################################

if __name__ == "__main__":
    main()