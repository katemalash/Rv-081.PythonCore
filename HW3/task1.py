a = int(input('Please enter value a: '))
b = int(input('Please enter value b: '))
tuple1 = a,b
b,a = tuple1
print(f'Swap the values: a - {a}, b - {b}')	
