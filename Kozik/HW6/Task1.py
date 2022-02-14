import random


the_number_of_numbers_in_the_lists = 10

random_list = [random.randint(1, 10) for _ in range(the_number_of_numbers_in_the_lists)]
user_list = [int(input(f'Enter {i + 1} number: '))
             for i in range(the_number_of_numbers_in_the_lists)]

sum_list = [user_number + random_number
            for random_number,  user_number in zip(random_list, user_list)]

print(f'\nRandom list: {random_list}\n'
      f'User list: {user_list}\n'
      f'\nSum list: {sum_list}')
