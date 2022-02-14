import random


number =  random.randint(0, 100)

for i in range(1, 11):
    which_number = int(input('which_number the number from 1 to 100: '))
    
    if which_number == number:
        print('Well done!')
        break
    elif which_number < number:
        print('Try again, number is grater!')
    elif which_number > number:
        print('Try again, number is smaller!')
    else:
        print('Not a number')
print('The number was: ', number)
