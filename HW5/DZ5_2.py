try_numbers = []
print("Enter 10 natural numbers > 2")

for i in range(10):
    user_number = int(input("Enter number: "))
    if user_number % 5 == 0 and user_number > 2:
        try_numbers.append(user_number)

print(try_numbers)
