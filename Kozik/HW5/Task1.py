import random

desired_number = random.randint(0, 100)

user_number = int(input('Your version number: '))
count_attempts = 1

while user_number != desired_number:

    if count_attempts == 10:

        print('Attempts are over. Hidden number {}'.format(desired_number))
        break

    if user_number < desired_number:

        user_number = int(input('Less than necessary. Try again: '))

    else:

        user_number = int(input('More than necessary. Try again: '))

    count_attempts += 1

else:

    print('Congratulations! You are a winner.')
