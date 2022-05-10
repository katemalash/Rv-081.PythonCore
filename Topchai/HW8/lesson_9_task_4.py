"""
Create the function is_prime, which takes 1 argument - a number from 0 to 1000,
and returns True if it is simple, and False - otherwise.
"""


def is_prime(number):
    if number == 1:
        return True
    for n in range(2, int(number**0.5)+1):
        if number % n == 0:
            return False
    else:
        return True


while True:

    try:
        userInput = int(input("\nPlease enter the number from 0 to 1000: "))
        if 0 <= userInput <= 1000:
            if is_prime(userInput) == True:
                print(f"\nNumber {userInput} is prime.")
            else:
                print(f"\nNumber {userInput} is not prime.")
        else:
            print("\nWrong input.")

        action2 = input("\nWould your like to try again? yes/no >>> ").lower()

        if action2 == "yes":
            continue
        elif action2 == "no":
            break
        else:
            print("\nWrong input. Try again.")

    except ValueError:
        print("\nWrong input. Try again.")
