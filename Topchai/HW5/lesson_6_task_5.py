'''
Given the number P and the number H. The user enters a sequence of numbers. Determine: 
the sum of those numbers that are less than P; product of numbers greater than H; the number 
of numbers in the range of values from P to H. When entering a number equal to P or H, stop 
the calculation and display the result.
'''

numberP = 20
numberH = 75

sumNumbersLessP = 0
sumNumbersLessPList = []

numberProductGreaterH = 1
numberProductGreaterHList = []

numberCountFromPtoH = 0
numberCountFromPtoHList = []

while True:
    entryNumber = int(input("\n>>> "))
    
    if entryNumber < numberP:

        sumNumbersLessPList.append(entryNumber)
        sumNumbersLessP += entryNumber

    elif numberP < entryNumber < numberH:

        numberCountFromPtoHList.append(entryNumber)
        numberCountFromPtoH += 1

    elif entryNumber > numberH:
        
        numberProductGreaterHList.append(entryNumber)
        numberProductGreaterH = numberProductGreaterH * entryNumber

    elif entryNumber == numberP or entryNumber == numberH:
        break

    else:
        print("it`s not number")

print(f"""
{"-"*90}
The sum of numbers less than P is {sumNumbersLessP}, {sumNumbersLessPList}
The Multiplication of numbers that are greater than H is {numberProductGreaterH}, {numberProductGreaterHList}
The numbet of numberst beetween P and H is {numberCountFromPtoH}, {numberCountFromPtoHList}
{"-"*90}
""")
