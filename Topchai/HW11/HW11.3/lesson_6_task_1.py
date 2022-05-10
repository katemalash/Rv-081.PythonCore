'''
The program generates a random integer from 0 to 100. The user must guess 
it in no more than 10 attempts. After each unsuccessful attempt, program 
says if the number entered by user more or less than required number. If the 
number is not guessed for 10 attempts, then display the guessed number.
'''
import random
from CustomError import*


print("\nThe program will generate the random number from 0 to 100. Your task is to guess what number it is!\nLet's start!\n")

randomNumber = random.randint(0,100)
lives = 10
#print(f"\nHINT: Random generated number is {randomNumber}\n")

while lives != 0:
    try:
        try:
            answerNumber = int(input("Please guess the number: "))
        except ValueError:
            print("Wrong input.")

        if answerNumber < 0 or answerNumber > 100:
            raise CustomError("Input is our of range (0 - 100)")
        
        elif answerNumber > randomNumber:

            print("\nThe guessed number is lover. Please try again!")
            lives -= 1
            print(f"Attempts left: {lives}\n")
        
        elif answerNumber < randomNumber:

            print("\nThe guessed number is bigger. Please try again!")
            lives -= 1        
            print(f"Attempts left: {lives}\n")

        elif answerNumber == randomNumber:

            print(f"\nYou guessed it! The correct number is {randomNumber}!")
            break
        
        
    except CustomError as e:
        print("We obtain error:", e.data)
                    
print(f"The number was {randomNumber}!")