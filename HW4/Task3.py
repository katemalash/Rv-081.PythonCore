number = int(input('Please enter a one or two, positive or negative number'))
if number > 9:
    print('It is a positive two-digit number')
elif number < -9:
    print('It is a negative two-digit number')
elif number > 0 and number < 10:
    print('It is a positive one-digit number')
elif number < 0 and number > - 10:
    print('It is a negative one-digit number')
else:
    print('It is zero')
