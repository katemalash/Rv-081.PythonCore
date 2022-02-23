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
        result = first_num / second_num

    return result


first_number = int(input('Enter first number: '))
second_number = int(input('Enter second number: '))
operation = input('Enter arithmetic operation (/, *, +, -): ')

print(f'\nResult: {arithmetic_operation(first_number, second_number, operation)}')
