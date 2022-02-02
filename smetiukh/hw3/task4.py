import math


radius = int(input('Enter radius of the circle'))

area = math.pi * (radius ** 2)
perimeter = (2 * (math.pi * radius))

print('The area of the circle is', area, 'square centimeters.', '\n',
      'This is perimeter of the circle', perimeter, 'centimeters.')
