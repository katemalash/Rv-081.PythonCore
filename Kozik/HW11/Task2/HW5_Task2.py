from exeptions import LessTwoError

count_of_loop = 0
count_of_number = 0

while count_of_loop != 10:

    try:

        user_number = int(input(f'Enter a number greater than two #{count_of_loop + 1}: '))

        if user_number < 2:
            raise LessTwoError

    except ValueError:
        print('This is not number')

    except LessTwoError:
        print('Number less than two.')

    else:

        if user_number % 5 == 0:

            count_of_number += 1

        count_of_loop += 1


print(f'\nNumbers that are multiples of five: {count_of_number}')
