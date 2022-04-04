from pond import Pond
from fish import *
import random


def output():

    answer = input('\nBack to menu (Press any kay): ')


def continue_loop():

    flag = input('\nMore?: (1 - Yeas, Any kay - No): ')

    if flag != '1':

        return True


my_pound = Pond()
fishes_in_a_bucket = []

print('Welcome to Game!')

while True:

    print('\nPress "1" - View capacity;\n'
          'Press "2" - View state of Pond;\n'
          'Press "3" - Add fish(Carp or Catfish);\n'
          'Press "4" - Catch fish(concrete instance);\n'
          'Press "5" - Create new fish(fill himself the creator);\n'
          'Press "6" - View bucket;\n'
          'Press "7" - Finish the game.\n')

    action = int(input('Enter action number: '))

    if action == 1:

        my_pound.show_capacity()
        output()

    elif action == 2:

        my_pound.show_state()
        output()

    elif action == 3:

        while True:

            if len(fishes_in_a_bucket) > 0:

                random_fish = random.randint(0, len(fishes_in_a_bucket) - 1)
                my_pound.obtain_fish(fishes_in_a_bucket[random_fish])
                fishes_in_a_bucket.remove(fishes_in_a_bucket[random_fish])

                print('\nFish is added to the pound\n')

            else:

                print('\nFish is over')

            if continue_loop():

                break

        output()

    elif action == 4:

        if len(my_pound.capacity) > 0:
            my_pound.lost_fish(my_pound.capacity[random.randint(0, len(my_pound.capacity))])

            print('\nFish lost\n')

        else:

            print('\nFish not found')

        output()

    elif action == 5:

        while True:

            user_fish = input('\nCarp or catfish? (1 or 2): ')

            if user_fish == '1':

                weight_of_fish = input('Weight: ')
                color = input('Color: ')

                user_fish = Carp(weight_of_fish, color)
                fishes_in_a_bucket.append(user_fish)

                print('\nYour carp is added to the bucket')

            elif user_fish == '2':

                weight_of_fish = input('Weight: ')
                length_of_whisker = input('Length of whisker: ')

                user_fish = Catfish(weight_of_fish, length_of_whisker)
                fishes_in_a_bucket.append(user_fish)

                print('\nYour catfish is added to the bucket')

            else:

                print("\nIt's not a fish\n")

            if continue_loop():

                break

    elif action == 6:

        print()

        for fish in fishes_in_a_bucket:
            print(fish)

        output()

    elif action == 7:

        break
