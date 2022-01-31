a = float(input('Enter A: '))
b = float(input('Enter B: '))


results = dict()
results['Addition'] = a + b
results['Subtraction'] = a - b
results['Multiplication'] = a * b
results['Division'] = a / b
results['integer division'] = a // b
results['Remainder'] = a % b
results['Exponentiation'] = a ** b

for key in results.keys():
    print(f'{key}: {results[key]}')
