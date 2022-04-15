def arithmetic_operation(first_num, second_num, ar_operation):
    """This function take two numbers and an arithmetic operation (/, *, +, -) and output result"""

    result = 'Unknown operation'
    if ar_operation == '+':
        result = first_num + second_num

    elif ar_operation == "-":
        result = first_num - second_num

    elif ar_operation == '*':
        result = first_num * second_num

    elif ar_operation == '/':

        try:

            result = first_number / second_num

        except ZeroDivisionError:
            result = 'zero'

    return result


try:

    first_number = int(input('Enter first number: '))
    second_number = int(input('Enter second number: '))

except TypeError:
    print('typeerror')

except ValueError:
    print('valueerror')


try:

    operation = input('Enter arithmetic operation (/, *, +, -): ')

    if operation not in ('/', '*', '+', '-'):

        raise Exception('THE OPERATION IS UNKNOWN')

except Exception:
    print('error')

try:

    print(f'\nResult: {arithmetic_operation(first_number, second_number, operation)}')

except NameError:
    print('nameerror')
