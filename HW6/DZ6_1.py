import random


user_list = []
random_list = []
sum_list = []

number = int(input("Enter size list: "))

for i in range(number):
    random_list.append(random.randint(0, 100))
    user_number = int(input("Enter your number: "))
    user_list.append(user_number)
    sum_list.append(user_list[i]+random_list[i])

print("Random list:", random_list)
print("Your list:", user_list)
print("Summa list:", sum_list)
