user_number = int(input('Enter number: '))
sign = 'Positive', 0

if user_number < 0:
    sign = 'Negative', 1

print(f'\n{sign[0]} {len(str(user_number)) - sign[1]}-digit')
