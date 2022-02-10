negative = 0
positive = 0
while True:
    number = int(input('Enter number '))
    if number == 0:
        break
    else:
        if number<0:
            positive += 1
        else:
            negative += 1    
        print(f'Negative {negative/(negative+positive)*100}%')
        print(f'Positive {positive/(negative+positive)*100}%')

