import math


print("Enter the two other sides of the right triangle to calculate the length of the hypotenuse:")
side_a = int(input("Side A is "))
side_b = int(input("Side B is "))

triangle_hypotenuse = math.sqrt(side_a**2 + side_b**2)
print(f"The hypotenuse is equal to {triangle_hypotenuse}")