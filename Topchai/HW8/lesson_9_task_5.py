"""
Create the function is_year_leap, that takes 1 argument - year,
and returns True if the year is high, and False otherwise.
"""


def is_year_leap(year):
    if year % 4 != 0:
        return False

    elif year % 100 == 0:
        if year % 400 == 0:
            return True
        else:
            return False
    else:
        return False


while True:
    try:
        userInput = int(input("\nPlease enter the year: "))
        if is_year_leap(userInput) == True:
            print(f"\nThe year - {userInput} is high.")
        else:
            print(f"\nThe year - {userInput} is regular.")

        action2 = input(
            "\nWould your like to chose another year? yes/no >>> ").lower()

        if action2 == "yes":
            continue
        elif action2 == "no":
            break
        else:
            print("\nWrong input. Try again.")

    except ValueError:
        print("\nWrong input. Try again.")
