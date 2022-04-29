#Create a function calculator(arg) that takes 1 argument: 1, 2, 3 or 4. This function should return function sum(a,b) 
# if arg = 1, dif(a,b) if arg = 2, product(a,b) if arg = 3 and fraction(a,b) if arg=4.
def calc(arg):

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

print('''You need to choose a number of the operation, which you would like to use, where:
1) Addition
2) Substraction 
3) Multiplication
4) Division''')
calc(int(input('Enter the number from 1 to 4: ')))
