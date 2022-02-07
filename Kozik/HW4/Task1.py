year = int(input('Enter year: '))
century = 100
number_of_centuries = year//century + 1

if year % 4 == 0:
    print('This year is a leap year.')

print(f'{number_of_centuries} century.')
