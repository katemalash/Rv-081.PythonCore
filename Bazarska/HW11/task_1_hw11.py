def calc(arg):
    try:
        a = int(input('Enter the first number: '))
        b = int(input('Enter the second number: '))

        def addit(a, b):
            print(a+b) 
            
        def substr(a, b):
            print(a-b)
            
        def mult(a, b):
            print(a*b)

        def div(a, b):
            print(a/b)

        if arg == 1:
            return addit(a, b)
        elif arg == 2:
            return substr(a, b)
        elif arg == 3:
            return mult(a, b)
        elif arg == 4:
            return div(a, b)
        else:
            print('You entered an invalid number')
    except ValueError:
        print('Yoe have entered incorrect value')
    except TypeError:
        print('You have entered incorrect value')
    except ZeroDivisionError:
        print('The number cannot be divided by zero')
    else:
        print('There is no exceptions')
    finally:
        print('The end of the process')

print('''You need to choose a number of the operation, which you would like to use, where:
1) Addition
2) Substraction 
3) Multiplication
4) Division''')
calc(int(input('Enter the number from 1 to 4: ')))