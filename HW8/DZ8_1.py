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


num1 = int(input("Enter 1 number: "))
num2 = int(input("Enter 2 number: "))
operation = input("Enter operation: ")
print(arithmetic(num1, num2, operation))
