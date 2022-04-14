from exeptions import *

while True:

    try:

        number_p = int(input('Enter P: '))
        number_h = int(input('Enter H: '))

    except ValueError:
        print('Incorrect value. Please, enter numbers')

    else:
        break

sum_of_numbers_less_than_p = 0
multiplication_of_numbers_greater_than_h = 1
amount_of_numbers_between_p_and_h = 0

count_for_output = 1

while True:

    while True:

        try:
            user_number = int(input(f'\nEnter #{count_for_output}: '))

        except ValueError:
            print('Incorrect value. Please, enter numbers')

        else:
            break

    try:

        if user_number < number_p:
            raise LessP

        elif user_number > number_h:
            raise MoreH

        elif number_p < user_number < number_h:
            raise BetweenHandP

        else:
            raise EqualityPorH

    except LessP:
        sum_of_numbers_less_than_p += user_number

    except MoreH:
        multiplication_of_numbers_greater_than_h *= user_number

    except BetweenHandP:
        amount_of_numbers_between_p_and_h += 1

    except EqualityPorH:
        break

    finally:
        count_for_output += 1

print(f'\nSum of numbers less than P: {sum_of_numbers_less_than_p}\n'
      f'Multiplication of numbers greater than H: {multiplication_of_numbers_greater_than_h}\n'
      f'Amount of numbers between P and H: {amount_of_numbers_between_p_and_h}')
