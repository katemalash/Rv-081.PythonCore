'''
Depending on the user's choice, ccalculate the square of either a rectangle, 
# or a triangle, or a circle. If a rectangle or triangle is selected, the lenghts 
# of the sides should be invited; if circle, its radius.
'''

import math


print("\nHello!\n")

print("Please choose the figure you want to calculate (Circle, Triangle, Rectangle):\n\n")

figure = ''

while figure not in ['circle', "triangle", "rectangle"]:
    figure = input("I want to calculate area of ")

if figure == "circle":
    print("Enter the radius of the circle to calculate its area and perimeter:\n")
    circle_radius = int(input("The radius is "))

    circle_perimeter = circle_radius * math.pi * 2
    circle_areaa = math.pi * circle_radius**2

    print(f"According to the circle radius, the perimeter of circle is equal to {circle_perimeter}. The area of circle is equal to {circle_areaa}.")

elif figure == "rectangle":
    print("Enter the width and height to calculate the area and perimeter of the rectangle:\n")
    rectangle_width = int(input("The width is "))
    rectangle_height = int(input("The height is "))

    rectangle_perimetr = 2 * (rectangle_width+rectangle_height)
    rectangle_area = rectangle_width * rectangle_height

    print(f"According to the width and height, the perimeter of ractangle is equal to {rectangle_perimetr}. The area of rectangle is equal to {rectangle_area}.")

elif figure == "triangle":
    print("Enter the two other sides of the right triangle to calculate the length of the hypotenuse:\n")
    side_a = float(input("Side A is "))
    side_b = float(input("Side B is "))
    side_c = float(input("Side C is "))

    semi_perimeter = (side_a + side_b + side_c) / 2
    triangle_area = math.sqrt(semi_perimeter*(semi_perimeter - side_a)*(semi_perimeter - side_b)*(semi_perimeter - side_b))

    print(f"According to the triagnle 3 sides lenght, the area is equal to {triangle_area}.")
