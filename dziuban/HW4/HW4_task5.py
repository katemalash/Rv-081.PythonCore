money = int(input("Enter the sum you want to change: "))

print(money//200, "200")
money = money%200
print(money//100, "100")
money = money%100
print(money//10, "10")
money = money%10
print(money//1, "1")