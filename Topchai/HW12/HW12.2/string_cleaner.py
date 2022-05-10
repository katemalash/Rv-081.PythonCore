'''
Character string is given. Develop a program that removes from this line all
repeated occurrences of numbers and signs of arithmetic operations.
'''

from os import dup
from unittest import result


def duplicate_check(users_entry):
    result = ''.join(sorted(set(users_entry), key=users_entry.index))

    return(result)

if __name__ == "__main__":
    
    print("-"*140)

    print("This program will remove all duplicated symbols from the line.")
    
    users_entry = input("Please enter the string: ")

    edited_entry = duplicate_check(users_entry)
    
    print(edited_entry)

    while True:
        users_entry = input("Would you like to try again? Yes/No: ").lower()
        
        if users_entry == "yes":
            duplicate_check()
            
        elif users_entry == "no":
            print("-"*140)
            break