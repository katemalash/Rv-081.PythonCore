import random


random_number = random.randint(0, 100)
attempts = 0

while attempts < 10:
    try:
        user_number = int(input("Enter your number: "))
    except ValueError:
        print("You didn't enter number")
        user_number = None
        attempts += 1
    if user_number != None:
        if user_number == random_number:
            print("You win ,good job")
            break
        elif user_number < random_number:
            print("your number less")
            attempts += 1
        elif user_number > random_number:
            print("your number more")
            attempts += 1

if attempts == 10:
    print("you lose")
    print("number = ", random_number)
