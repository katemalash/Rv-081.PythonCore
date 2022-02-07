import math


user_choice = int(input('"1" - Triangle, "2" - Rectangle, "3" - Circle: '))
area = None

if user_choice == 1:
    side_a = float(input('\na = '))
    side_b = float(input('b = '))
    side_c = float(input('c = '))
    semi_perimeter = (side_a + side_b + side_c) / 2
    area = math.sqrt(semi_perimeter*(semi_perimeter - side_a)*(semi_perimeter - side_b)\
           *(semi_perimeter - side_c))

elif user_choice == 2:
    side_a = float(input('\na = '))
    side_b = float(input('b = '))
    area = side_a * side_b

elif user_choice == 3:
    radius = float(input('\nradius = '))
    area = math.pi * radius**2

else:
    print('Invalid input')

print(f'\nArea = {area}')
