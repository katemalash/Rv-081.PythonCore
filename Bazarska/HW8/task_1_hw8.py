#Create an arithmetic function that takes 3 arguments: the first 2 are numbers, the third is the operation to be 
# performed on them. If the third argument is +, add them; if -, then subtract; * - multiply; / - divide (first to second). 
# In other cases, return the "Unknown operation" line.
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

arg1 = int(input('Enter the first number: '))
arg2 = int(input('Enter the second number: '))
operation = input('Which operation you would like to perform on them? ')
print(arithFunc(arg1, arg2, operation))
