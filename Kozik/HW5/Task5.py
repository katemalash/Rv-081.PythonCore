number_p = int(input('Enter P: '))
number_h = int(input('Enter H: '))

sum_of_numbers_less_than_p = 0
multiplication_of_numbers_greater_than_h = 1
amount_of_numbers_between_p_and_h = 0

count_for_output = 1
user_number = int(input(f'\nEnter #{count_for_output}: '))

while user_number != number_h and user_number != number_p:

    if user_number < number_p:
        sum_of_numbers_less_than_p += user_number

    elif user_number > number_h:
        multiplication_of_numbers_greater_than_h *= user_number

    elif number_p < user_number < number_h:
        amount_of_numbers_between_p_and_h += 1

    count_for_output += 1
    user_number = int(input(f'Enter #{count_for_output}: '))

print(f'\nSum of numbers less than P: {sum_of_numbers_less_than_p}\n'
      f'Multiplication of numbers greater than H: {multiplication_of_numbers_greater_than_h}\n'
      f'Amount of numbers between P and H: {amount_of_numbers_between_p_and_h}')



