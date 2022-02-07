from unittest import result


money = int(input('Enter the amount of money: '))

if money % 200 > 0:
    sum = int(money / 200)
    print('200: ', sum)
    sum2 = int((money%200)/100)
    print('100: ', sum2)
    sum3 = int(((money%200)%100)/10)
    print('10: ', sum3)
    sum4 = int((money%200)%10)
    print('1: ', sum4)
else:
    print('error')