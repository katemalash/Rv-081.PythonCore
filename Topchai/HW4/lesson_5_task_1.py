'''
The YEAR is known. Determine whether this year is intercalary and to what century this year belongs.
'''

print("\nPlease choose enter the year to determine whether this year is intercalary and to what century this year belongs\n")

inputYear = int(input("Enter the year: "))
yearsCentury = inputYear//100+1

if inputYear % 4 != 0:
    print(f"The {inputYear} year is regular and belong to {yearsCentury} century")

elif inputYear % 100 == 0:
    if inputYear % 400 == 0:
        print(f"The {inputYear} year is leap and belong to {yearsCentury} century")
    else:
        print(f"The {inputYear} year is regular and belong to {yearsCentury} century")

else:
    print(f"The {inputYear} year is regular and belong to {yearsCentury} century")
