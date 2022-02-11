'''
The amount of money is known. Exchange it with 200, 100, 10 banknotes and 1 UAH coin, if possible.
'''
moneyAmount = int(input("\nPlease enter the amount: "))

banknote1 = 1
banknote10 = 10
banknote100 = 100
banknote200 = 200

if moneyAmount >= 1:
    count200 = moneyAmount // banknote200
    remnant200 = moneyAmount % banknote200

    print(f"You will get >>> {count200} banknotes of 200")

    count100 = remnant200 // banknote100
    remnant100 = remnant200 % banknote100

    print(f"You will get >>> {count100} banknotes of 100")

    count10 = remnant100 // banknote10
    remnant10 = remnant100 % banknote10

    print(f"You will get >>> {count10} banknotes of 10")

    count1 = remnant10 // banknote1

    print(f"You will get >>> {count1} banknotes of 1")

else:
    print("Not enough money.")