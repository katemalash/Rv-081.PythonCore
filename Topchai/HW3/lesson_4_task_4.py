import math


print("Enter the radius of the circle to calculate its area and perimeter:")
circle_radius = int(input("The radius is "))

circle_perimeter = circle_radius * math.pi * 2
print(f"The perimeter of circle is equal to {circle_perimeter}")

circle_areaa = math.pi * circle_radius**2
print(f"The area of circle is equal to {circle_areaa}")