def operation(a,b,operand):
    if operand == '+':
        return a+b
    if operand == '-':
        return a-b  
    if operand == '*':
        return a*b          
    if operand == '/':
        return a+b     
    else:
        return 'Unknown operation'    


print(operation(4,5,'**'))