'''
User enters ten natural numbers greater than 2. Count how many of them are numbers that are multiples of 5.
'''

numberList = []

tryNumber = 10
numbers5 = 0

print("This program will determine whether the entered numbers are multiples of 5.")

for i in range(10):    
    
    try:
        naturalNumber = int(input("Please enter the number that is greater than 2: "))

        if naturalNumber > 2:

            if naturalNumber % 5 == 0:

                numberList.append(naturalNumber)
                numbers5 += 1

            tryNumber -= 1
            
            print(f"{tryNumber} entries left.\n")
        
        elif naturalNumber < 2:

            print("The entered number should be greater than 2. Please try again!")

            tryNumber -= 1

            print(f"{tryNumber} entries left.")
            
    except ValueError:
        print("ValueError: Please enter the number.")

print(f"\n{numbers5} ENTERED NUMBERS {numberList} ARE MULTIPLES OF 5.\n")
