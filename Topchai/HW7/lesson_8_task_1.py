'''
Character string is given. Develop a program that removes from this line all
repeated occurrences of numbers and signs of arithmetic operations.
'''

from os import dup


print("-"*140)

print("This program will remove all duplicated symbols from the line.")

def duplicate_check():
    
    print("-"*140)

    users_entry = input("Please enter the string: ")
    result = ''.join(sorted(set(users_entry), key=users_entry.index))

    print(f"\nCorrected line: {result}\n")    

duplicate_check()

while True:
    users_entry = input("Would you like to try again? Yes/No: ").lower()
    
    if users_entry == "yes":
        duplicate_check()
        
    elif users_entry == "no":
        print("-"*140)
        break