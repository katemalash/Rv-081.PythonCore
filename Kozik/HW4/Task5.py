amount_of_money = float(input('Enter the amount of money: '))
two_hundred_denomination = 200
one_hundred_denomination = 100
ten_denomination = 10
one_denomination = 1

if amount_of_money % one_denomination == 0:
    print(f'\n200 banknotes - {int(amount_of_money // two_hundred_denomination)}')
    amount_of_money %= two_hundred_denomination
    print(f'100 banknotes - {int(amount_of_money // one_hundred_denomination)}')
    amount_of_money %= one_hundred_denomination
    print(f'10 banknotes - {int(amount_of_money // ten_denomination)}')
    amount_of_money %= ten_denomination
    print(f'1 banknotes - {int(amount_of_money // one_denomination)}')

else:
    print('\nNon-exchangeable amount')
