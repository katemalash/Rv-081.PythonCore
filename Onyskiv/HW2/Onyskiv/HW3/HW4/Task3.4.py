import math

square=int(input('Enter the area of square:'))
circle=int(input('Enter the area of the circle:'))
passage=int(input('Enter the passage between circle and wall:'))
radius=math.sqrt(circle/3.14)
side=math.sqrt(square)
if radius*2+passage<=side:
    print('This configuration is possible')
else:
    print ('It is inpossible')

