year = int(input("Enter year: "))

if year % 4 == 0:
    print("Leap year")
else:
    print("No leap year")

print("Century ", (year//100)+1)
