"""
Create a module calculator that contains 4 functions: sum(a,b), product(a,b) and fraction(a,b)
1. Import the entire module and use it's functions
2. Import only 2 functions and use them
3. Import all the functions and use them.
"""

import calcModule


numberA = int(input("\nPlease enter A: "))
numberB = int(input("Please enter B: "))

print(f"\nSum A and B: {calcModule.calcSum(numberA, numberB)}")
print(f"Dif A and B: {calcModule.calcDif(numberA, numberB)}")
print(f"Product A and B: {calcModule.calcProduct(numberA, numberB)}")
print(f"Fraction A and B: {calcModule.calcFraction(numberA, numberB)}\n")
