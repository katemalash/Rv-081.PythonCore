import math


promt = str(input("Square of Rectangle/Triangle/Circle"))

if promt == "Rectangle":
    width = int(input("Enter rectangle width"))
    height = int(input("Enter rectangle height"))
    area = width * height
    print('The area of rectangle is', area, 'square centimeters.')

elif promt == "Circle":
    radius = int(input('Enter radius of the circle'))
    area = math.pi * (radius ** 2)
    print('The area of the circle is', area, 'square centimeters.')

elif promt == "Triangle":
    a = int(input("Enter 1st Triangle Side"))
    b = int(input("Enter 2nd Triangle Side"))
    c = int(input("Enter 3d Triangle Side"))
    p = (a + b + c) / 2
    print("The area of triangle is", math.sqrt(p * (p - a) * (p - b) * (p - c)))

else:
    print("Please specify what you need to calculate, mind on upper case")
