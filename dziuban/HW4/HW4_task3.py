number = int(input("Enter the number: "))

if number >= 0:
    print(f"The number is positive and has {len(str(number))} digits")
elif number < 0:
    print(f"The number is negative and has {len(str(number * (-1)))} digits")
