#!/usr/bin/env python3
#create a formatted summary table from a list of tuples containing students with their grades in math and history 

def main():
    students_grades = [("anne","A","A+"),("bennett","B", "E"), ("claire", "C", "A"), ("daniel", "D", "B"), ("edward", "E", "A")]
    print("{0:<12} {1:^20} {2:>20}".format("Name", "Grade_Math", "Grade_History"))
    print("-"*60)
    for element in students_grades:
        print("{0:<12} {1:^20} {2:>20}".format(element[0].capitalize(),element[1],element[2]))


################################################ 

if __name__ == "__main__":
    main()