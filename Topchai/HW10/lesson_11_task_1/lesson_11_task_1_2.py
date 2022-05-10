"""
Create a module calculator that contains 4 functions: sum(a,b), product(a,b) and fraction(a,b)
1. Import the entire module and use it's functions
2. Import only 2 functions and use them
3. Import all the functions and use them.
"""

from calcModule import calcDif, calcFraction


numberA = int(input("\nPlease enter A: "))
numberB = int(input("Please enter B: "))

print(f"\nDif A and B: {calcDif(numberA,numberB)}")
print(f"Fraction A and B: {calcFraction(numberA,numberB)}\n")
