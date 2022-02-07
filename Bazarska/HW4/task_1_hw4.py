
year = int(input('Enter the year '))
if year % 4 == 0 and year % 100 !=0:
    print('Leap year')
elif year % 400 == 0:
    print('Leap year')
else:
    print('Regular year')

if year % 100 > 0:
    century = int(year / 100 + 1)
    print('It reffers to ', century, 'century')
else:
    cent = int(year/100)
    print('It is ', cent, 'century')
