def calculator(arg):

    while True:
        try:
            a = int(input('Enter a: '))
            b = int(input('Enter b: '))
        except ValueError:
            print("It's not int")
        else:
            break

    def summ(a, b):
        print(a + b)

    def dif(a, b):
        print(a - b)

    def product(a, b):
        print(a * b)

    def fraction(a, b):
        try:
            print(a / b)
        except ZeroDivisionError:
            print('Division by zero')

    if arg == 1:
        return summ(a, b)

    elif arg == 2:
        return dif(a, b)

    elif arg == 3:
        return product(a, b)

    elif arg == 4:
        return fraction(a, b)

    else:
        print('Value error')


while True:
    try:
        calculator(int(input('Enter command from 1 to 4: ')))
    except ValueError:
        print("Command not found")
    else:
        break
