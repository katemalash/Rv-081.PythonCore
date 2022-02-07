money = int(input("Enter sum of money you have"))
banknotes = {
    200:money//200,
    100:(money%200)//100,
    10:((money%200)%100)//10,
    1:(money%200)%10
}

print(banknotes)