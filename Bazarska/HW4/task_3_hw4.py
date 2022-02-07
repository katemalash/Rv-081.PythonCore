number = int(input('Enter a number: '))

if number > 0:
    print('Your number is positive and has ', len(str(number)), 'digits')
elif number < 0:
    print('Your number is negative and has', len(str(number * (-1))), 'digits')
else:
    print('It is not a number')
