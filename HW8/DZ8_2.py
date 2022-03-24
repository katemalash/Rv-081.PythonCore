def deposit(money, years):
    for i in range(years):
        money = money + money * 0.1
    return round(money, 2)

print(deposit(20000, 15))
