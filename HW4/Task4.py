square_hall = int(input('Enter square hall: '))
radius_place = int(input('Enter radius place: '))
K = int(input('Enter K: '))
side_hall = square_hall / 2

if side_hall - radius_place*2 > K:
    print('Is it possible')
else:
    print('Is it imposible')
