numbers = [int(input('Enter a natural number which > 2 : ')) for i in range(10)]

for num in numbers:
    if num % 5 == 0:
        print(num)
    else:
        break
print('Done')
