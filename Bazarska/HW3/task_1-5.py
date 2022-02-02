import math

#Swap the values
first_number = input('Enter first number x ')
second_number = input('Enter second number y ')
first_number, second_number = second_number, first_number
print('x = ', first_number)
print('y = ', second_number)

#calculator
bytes_number = int(input('Enter value in bytes '))
kilobytes_number = bytes_number / 1024
megabytes_number = bytes_number / 1000000
print(bytes_number, 'is equal to ', kilobytes_number, 'kilobytes')
print(bytes_number, 'is equal to ', megabytes_number, 'megabytes')


#Calculate the area and the perimeter of the rectangle
rectangle_width = int(input('Enter the width of rectangle '))
rectangle_heigh = int(input('Enter the heigh of rectangle '))
perimeter = (rectangle_width * 2) + (rectangle_heigh * 2)
area = rectangle_width * rectangle_heigh
print('Perimeter equals to ', perimeter, 'cm')
print('Area equals to ', area, 'cm²')

#Calculate the area and the perimeter of the circle
circle_radius = int(input('Enter radius of the circle '))
circle_perimeter = 2 * math.pi * circle_radius
circle_area = math.pi * circle_radius**2
print('Circle perimeter is ', circle_perimeter, 'cm')
print('Circle area is ', circle_area, 'cm²')

#Calculate the length of the triangle's hypotenuse
first_side = int(input('Enter length of the side a '))
second_side = int(input('Enter length of the side b '))
hypothenuse = math.sqrt(first_side**2 + second_side**2)
print('Triangle\'s hypothenuse equals to ', hypothenuse, 'cm')

                    
