import math

print("rectangle or triangle or circle")
user_area = input("What area do you want to know?: ")

if user_area == "rectangle":
    user_data_a = int(input("Enter a: "))
    user_data_b = int(input("Enter b: "))
    print("Area rectangle = ",user_data_a*user_data_b)
elif user_area == "triangle":
    user_data_base = int(input("Enter base: "))
    user_data_height = int(input("Enter height: "))
    print("Area rectangle = ", user_data_base * user_data_height * 0.5)
elif user_area == "circle":
    user_data_radius = int(input("Enter radius: "))
    print("Area circle = ",math.pi * user_data_radius ** 2)
else:
    print("You pick nothing")