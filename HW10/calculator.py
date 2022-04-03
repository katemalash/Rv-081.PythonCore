def calculator(arg):
    def sum(a, b):
        return a+b

    def dif(a, b):
        return a - b

    def product(a, b):
        return a * b

    def fraction(a, b):
        return a / b

    if arg == 1:
        return sum
    elif arg == 2:
        return dif
    elif arg == 3:
        return product
    elif arg == 4:
        return fraction


user_input = None
number1 = None
number2 = None
try:
    number1 = int(input("Enter number1: "))
    number2 = int(input("Enter number2: "))
    user_input = int(input(">> "))
    choice = calculator(user_input)
except ValueError:
    print("You enter no number")

