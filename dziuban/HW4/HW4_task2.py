import math


figure = int(input("Enter the number of figure you want to choose (rectangle - 1, triangle - 2, circle - 3):  "))

if figure == 1:

    rectangle_height = int(input("Enter the height of rectangle "))
    rectangle_width = int(input("Enter the width of rectangle "))

    area = rectangle_width * rectangle_height

    print(f"Area = {area}")

elif figure == 2:

    side_1 = int(input("Enter the base "))
    side_2 = int(input("Enter the height "))

    area = side_1 * side_2 * 0.5

    print(f"Area =  {area}")

elif figure == 3:

    circle_radius = int(input("Enter the radius of the circle "))

    area = math.pi * circle_radius ** 2

    print(f"Area = {area} a")

else:
    print("You can choose only 1-3 option")
