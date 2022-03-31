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


number1 = int(input("Enter number1: "))
number2 = int(input("Enter number2: "))
user_input = int(input(">> "))
choice = calculator(user_input)
print(choice(number1, number2))
