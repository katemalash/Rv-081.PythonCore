print('''Please enter the number of shape:
1 rectangle
2 triangle
3 circle''')   
shape = int(input())

if shape == 1:
    a = int(input('Enter first side '))
    b = int(input('Enter second side '))
    s = a * b
elif shape == 2:
    a = int(input('Enter first side '))
    b = int(input('Enter second side '))
    c = int(input('Enter third side '))
    p = (a+b+c)/2
    s = (p * (p-a) * (p-b) * (p-c))**0.5 
elif shape == 3: 
    pi = 3.14
    r = int(input('Enter radius '))
    s = pi*r**2
else:
    print('You entered bad number')

print(f'The area of shape is {s}')
