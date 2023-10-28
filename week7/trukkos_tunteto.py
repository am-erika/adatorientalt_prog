#!/usr/bin/env python3

def decode(byte):
    
    total = 0
    step = 0
    for bit in range(len(byte)-1, -1, -1):
        total = total + int(byte[bit]) * (2 ** step)
        step += 1
    return chr(total)


def read_file(input_file, output_file):
    
    with open(input_file, "r") as file_from, open(output_file, "w") as file_to:
        for line in file_from:
            line = line.rstrip("\n")
            file_to.write(decode(line))

def main():
    input_file = "binaries.txt"
    output_file = "decode.txt"
    read_file(input_file, output_file)

#########################
if __name__ == "__main__":
    main()