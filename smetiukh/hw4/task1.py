year = int(input("Enter the year"))
if year % 4 == 0:
    print("Високосний")
else:
    print("Невисокосний")
print("Belongs to ", (year//100) + 1, "Century")
