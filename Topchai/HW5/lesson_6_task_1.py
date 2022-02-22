'''
The program generates a random integer from 0 to 100. The user must guess 
it in no more than 10 attempts. After each unsuccessful attempt, program 
says if the number entered by user more or less than required number. If the 
number is not guessed for 10 attempts, then display the guessed number.
'''
import random


print("\nThe program will generate the random number from 0 to 100. Your task is to guess what number it is!\nLet's start!\n")

randomNumber = random.randint(0,100)
tryNumber = 10

#print(f"\nHINT: Random generated number is {randomNumber}\n")

for i in range(10):
    
    answerNumber = int(input("Please guess the number: "))

    if answerNumber > randomNumber:

        print("\nThe guessed number is lover. Please try again!")
        tryNumber -= 1
        print(f"Attempts left: {tryNumber}\n")
    
    elif answerNumber < randomNumber:

        print("\nThe guessed number is bigger. Please try again!")
        tryNumber -= 1        
        print(f"Attempts left: {tryNumber}\n")

    elif answerNumber == randomNumber:

        print(f"\nYou guessed it! The correct number is {randomNumber}!")
        break


print(f"The number was {randomNumber}!")