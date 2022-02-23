year=int(input("Enter the year:"))
century=int(1+year/100)

if year%400==0:
    print ("You entered a leap year in the",century,"century")
elif year%4==0:
    print ("You entered a leap year in the",century,"century")
else: print("You entered not a leap year")

