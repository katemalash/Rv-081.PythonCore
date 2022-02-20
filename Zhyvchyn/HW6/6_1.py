from random import randint


NUMBER_OF_NUMBERS = 5

result_list =[]
random_list = [randint(0,50) for i in range(NUMBER_OF_NUMBERS)]
user_list = [int(x) for x in input(f'Enter {NUMBER_OF_NUMBERS} numbers ').split()]

for i in range(0,NUMBER_OF_NUMBERS):
    result_list.append(random_list[i]+user_list[i])

print(random_list)
print(user_list)
print(result_list)
