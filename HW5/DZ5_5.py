p = 15
h = 50
sum_fever_p = 0
multiplication_more_h = 1
gap = 0

while p < 100:
    user_number = input()
    if user_number == "H" or user_number == "P":
        break
    elif user_number.isdigit() == True:
        user_number = int(user_number)
        if user_number < p:
            sum_fever_p += user_number
        elif user_number > h:
            multiplication_more_h *= user_number
        else:
            gap += 1
    else:
        print("it`s not number")

print("Number all numbers < p:", sum_fever_p)
print("Multiplication all numbers > 5:", multiplication_more_h)
print("Gap p - h :", gap, "numbers")
