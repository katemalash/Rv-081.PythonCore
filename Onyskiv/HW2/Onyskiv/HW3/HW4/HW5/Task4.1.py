import random

print('Start game')

correct_answer=random.randint(1,100)

i=1
number_answer=int(input('input your number:'))

while number_answer!=correct_answer and i<=10:
    number_answer=int(input('input your number:'))
    i+=1
    print('You have next chance')
else:
    if number_answer!=correct_answer and i==10:
       print('Game over')
    print('You win, correct answer is',number_answer)

