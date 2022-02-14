plug = 1
positive_numbers = 0
negative_numbers = 0

while plug == 1:
    user_number = int(input())
    if user_number == 0:
        break
    elif user_number > 0:
        positive_numbers += 1
    else:
        negative_numbers += 1

sum_numbers = positive_numbers + negative_numbers

print("Positive : ", positive_numbers/(sum_numbers/100), "%")
print("Negative : ", negative_numbers/(sum_numbers/100), "%")
