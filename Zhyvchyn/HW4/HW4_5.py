money_amount = int(input('Please enter amount of money '))
banknotes = {
    200:money_amount//200,
    100:(money_amount%200)//100,
    10:((money_amount%200)%100)//10,
    1:(money_amount%200)%10
}

print(banknotes)
