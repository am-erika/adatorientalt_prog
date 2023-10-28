#!/usr/bin/env python3

def clean_file_2(input_file, output_file_2):

    with open(input_file, 'r') as file_from, open(output_file_2, 'w') as file_to:
        for line in file_from:
            position = line.find('#')
            if position == -1:
                file_to.write(line)

def clean_file_1(input_file, output_file_1):                

    with open(input_file, 'r') as file_from, open(output_file_1, 'w') as file_to:
        for line in file_from:
            if not line.startswith("#"): 
                file_to.write(line)




def main():
    input_file = "string1.py"
    output_file_2 = "string1_clean_2.py"
    clean_file_2(input_file, output_file_2)
    output_file_1 = "string1_clean_1.py"
    clean_file_1(input_file, output_file_1)


    


################################################ 

if __name__ == "__main__":
    main()