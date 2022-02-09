count_of_loop = 0
count_of_number = 0

while count_of_loop != 10:

    user_number = int(input(f'Enter a number greater than two #{count_of_loop + 1}: '))

    if user_number >= 2 or (user_number % 5 == 0 and user_number > 2):

        if user_number % 5 == 0:

            count_of_number += 1

        count_of_loop += 1

    else:

        print('Number less than two.')

print(f'\nNumbers that are multiples of five: {count_of_number}')
