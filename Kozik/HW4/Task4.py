import math


room_area = float(input('Enter the area of the room: '))
stage_radius = float(input('Enter the radius of the stage: '))
distance = float(input('Enter the distance to the walls: '))
room_side = math.sqrt(room_area)

if (room_side - distance) / 2 >= stage_radius:
    print('\nThe stage is suitable.')
else:
    print('\nThe stage is not suitable.')
