'''
The users enters a number, the program must display its description. 
For example, "positive one-digit", "negative two-digit", etc.
'''
input("\nThis program will determine if the entered number is positive or negative, and how many digits it contain.\n")
inputNumber = int(input("\nPlease enter the number:\n"))

if inputNumber > 0:
    positiveOrNegative = "postive"
elif inputNumber == 0:
    positiveOrNegative = "equal to zero"
else:
    positiveOrNegative = "negative"

if 0 < inputNumber < 10 or -10 < inputNumber < 0:
    digitCount = "1 digit"
elif 9 < inputNumber < 100 or -100 < inputNumber < -9:
    digitCount = "2 digits"
elif 99 < inputNumber < 1000 or -1000 < inputNumber < -99:
    digitCount = "3 digits"
elif 999 < inputNumber < 10000 or -10000 < inputNumber < -999:
    digitCount = "4 digits"
elif 9999 < inputNumber < 100000 or -100000 < inputNumber < -9999:
    digitCount = "5 digits"
elif 99999 < inputNumber < 1000000 or -1000000 < inputNumber < -99999:
    digitCount = "6 digits"
elif 999999 < inputNumber < 10000000 or -10000000 < inputNumber < -999999:
    digitCount = "7 digits"

print(f"\nThe number {inputNumber} is {positiveOrNegative} and contain {digitCount}\n")