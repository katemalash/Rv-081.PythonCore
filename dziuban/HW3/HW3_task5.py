import math


side_1 = int(input("Enter the length of side one "))
side_2 = int(input("Enter the length of side two "))

hypotenuse = int(math.sqrt(side_1**2 + side_2**2))

print(f"The length of hypotenuse will be {hypotenuse}")
