'''
For user-entered numbers, determine the percentage of positive 
and negative numbers. When entering the number 0, finish the job.
'''

start = 1
numberCount = 0
positiveNumbers = 0
negativeNumbers = 0

while start == 1:
    enteredNumber = int(input(">>> "))
   
    if enteredNumber > 0:

        positiveNumbers += 1
        numberCount += 1
   
        print(f"\n     Postitive entries: {positiveNumbers/(numberCount/100)}%\n     Negative entries: {negativeNumbers/(numberCount/100)}%\n")

    elif enteredNumber < 0:
        
        negativeNumbers += 1
        numberCount += 1

        print(f"\n     Postitive entries: {positiveNumbers/(numberCount/100)}%\n     Negative entries: {negativeNumbers/(numberCount/100)}%\n")

    else:
        break

print(f"""
Postitive entries: {positiveNumbers/(numberCount/100)}%
Negative entries: {negativeNumbers/(numberCount/100)}%
""")
