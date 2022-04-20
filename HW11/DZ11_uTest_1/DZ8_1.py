from myZeroError import *


def arithmetic(num1, num2, operation):
    if operation == "*":
        return num1 * num2
    elif operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "/":
        return num1 / num2
    else:
        return "Unknown operation"


if __name__ == "__main__":
    try:
        num1 = int(input("Enter 1 number: "))
        num2 = int(input("Enter 2 number: "))
        operation = input("Enter operation: ")
        if operation == "/" and (num2 == 0 or num1 == 0):
            raise MyZeroError("You enter Zero")
        print(arithmetic(num1, num2, operation))
    except MyZeroError as error:
        print(error.data)
    except ValueError:
        print("You didn't enter number")
