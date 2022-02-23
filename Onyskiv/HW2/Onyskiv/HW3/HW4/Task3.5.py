moneyamount=int(input('Enter amount of money:'))
if moneyamount>=200: 
    num200=int(moneyamount/200)
    num10=int((moneyamount-num200*200)/10)
    num1=moneyamount-num200*200-num10*10
    print('You can change your money to ',num200,' by 200 UAH, ',num10,' by 10 UAH, ',num1,' by 1 UAH')
elif moneyamount>=10:
    num10=int(moneyamount/10)
    num1=moneyamount-num10*10
    print('You can change your money to ',num10,' by 10 UAH, ',num1,' by 1 UAH')
else:
    print('You can change your money to ',moneyamount,' by 1 UAH')


