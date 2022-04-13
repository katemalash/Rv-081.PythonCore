import random
from exeptions import *


desired_number = random.randint(0, 100)

while True:

    try:
        user_number = int(input('Your version number: '))
    except ValueError:
        print('Your number is not number')
    except Exception:
        print('Unknown error')
    else:
        break

count_attempts = 1

while user_number != desired_number:

    try:

        if count_attempts == 10:
            raise CountError

        if user_number < desired_number:
            raise ValueIsGreat

        else:
            raise ValueIsLittle

    except CountError:
        print('Attempts are over. Hidden number {}'.format(desired_number))
        break

    except ValueIsGreat:
        user_number = int(input('Less than necessary. Try again: '))

    except ValueIsLittle:
        user_number = int(input('More than necessary. Try again: '))

    count_attempts += 1

else:

    print('Congratulations! You are a winner.')