def arithFunc(arg1, arg2, operation):
    '''this function performs arithmetic operation between two numbers'''
    
    if operation == '+':
        return arg1 + arg2
    elif operation == '-':
        return arg1 - arg2
    elif operation == '*':
        return arg1 * arg2
    elif operation == '/':
        return arg1 / arg2
    else:
        return None

try:
    arg1 = int(input('Enter the first number: '))
    arg2 = int(input('Enter the second number: '))
    operation = input('Which operation you would like to perform on them? ')
    print(arithFunc(arg1, arg2, operation))
except ValueError:
    print('Something went wrong')
except TypeError:
    print('invalid value')
except ZeroDivisionError:
    print('The number can\'t be divided by zero')
else:
    print('There is no exceptions')
finally:
    print('The end of the process')