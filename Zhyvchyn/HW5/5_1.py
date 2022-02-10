from random import randint


guessed_number = randint(0,100)
print(guessed_number)
for i in range(10):
    number = int(input('Guess number\n'))
    if number == guessed_number:
        print(f'Yes, you guess  {guessed_number}')
        break
    elif number < guessed_number:
        print('Less then guessed')
    elif number > guessed_number:
        print('More then guessed')
else:
    print(f'Guessed number is {guessed_number}')   
