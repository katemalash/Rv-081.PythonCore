'''
Enter a number, letter or special character from the keyboard and return the entry
index to the corresponding tuple accordingly.
'''

tuple_of_things = ('1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')

def indexing_check():
    
    print("-"*77)
    
    users_entry = input("Enter the item to determine the entry index of this value inside the tuple: ")

    if users_entry in tuple_of_things:
        
        print(f"\nThe item '{users_entry}' has index {tuple_of_things.index(users_entry)} in the tuple.")

    elif users_entry not in tuple_of_things:
        
        print("\nNo such item in the tuple")

    print("-"*77)


indexing_check()

while True:
    users_entry = input("Would you like to try again? Yes/No: ")
    
    if users_entry == "Yes":
        indexing_check()
        
    elif users_entry == "No":    
        break
