import math
year = int(input('Enter the year: '))
century = year / 100
century = math.ceil(century)

if year %4 == 0:
    print (f'It is the leap year of the {century} century')
else:
    print (f'It is the usual year of the {century} century')
