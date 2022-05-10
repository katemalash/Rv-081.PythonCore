'''
For user-entered numbers, determine the percentage of positive 
and negative numbers. When entering the number 0, finish the job.
'''

start = 1
numberCount = 0
positiveNumbers = 0
negativeNumbers = 0

while start == 1:
    try:
        enteredNumber = int(input(">>> "))
    
        if enteredNumber > 0:

            positiveNumbers += 1
            numberCount += 1
    
            print(f"\n     Postitive entries: {round((positiveNumbers/(numberCount/100)), 3)}%\n     Negative entries: {round((negativeNumbers/(numberCount/100)), 3)}%\n")

        elif enteredNumber < 0:
            
            negativeNumbers += 1
            numberCount += 1

            print(f"\n     Postitive entries: {round((positiveNumbers/(numberCount/100)), 3)}%\n     Negative entries: {round((negativeNumbers/(numberCount/100)), 3)}%\n")

        else:
            break
        
    except ValueError:
        print("ValueError: Please enter the number.")

print(f"""
Postitive entries: {round((positiveNumbers/(numberCount/100)), 3)}%
Negative entries: {round((negativeNumbers/(numberCount/100)), 3)}%
""")
