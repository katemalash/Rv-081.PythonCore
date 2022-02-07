seat = int(input('Enter the number of your seat: '))

if seat <= 36: 
    print('This seat is common')
elif seat <= 54:
    print('It is the side seat')
else:
    print('Error')

if seat % 2 == 0:
    print('Top seat')
elif seat % 2 == 1:
    print('Bottom seat')
else: 
    print('Try again')
    
