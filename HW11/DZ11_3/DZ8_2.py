def deposit(money, years):
    for i in range(years):
        money = money + money * 0.1
    return round(money, 2)


if __name__ == "main":
    moneyU = int(input())
    yearsU = int(input())
    print(deposit(moneyU, yearsU))
