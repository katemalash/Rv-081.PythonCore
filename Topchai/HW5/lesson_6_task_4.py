'''
Display a "rectangle" formed of two types of characters. The outline of the 
rectangle should consist of one character, and "fill" - of another.
'''

height = int(input("Enter height: "))
width = int(input("Enter width: "))

print()

print(" + " + " - " * (width-2) + " + ")

for i in range(height-2):
    print(" | " + " X " * (width-2) + " | ")

print(" + " + " - " * (width-2) + " + ")

print()