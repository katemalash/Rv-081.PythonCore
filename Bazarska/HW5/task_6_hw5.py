neg = 0
pos = 0

while True:

    number = int(input('Enter a number: '))

    if number > 0:
        pos += 1
    elif number < 0:
        neg += 1 
    else:
        break
print('There are ', pos * 100 / (pos + neg), '% of positive numbers')
print('There are ', neg * 100 / (neg + pos), '% of negative numbers')
