#Fill in one list with random numbers, another with numbers entered from the keyboard, and write the sums of the corresponding elements of the 
# first two lists in the third one. Display the contents of the lists on the screen.
import random


first_list = []
for i in range(1, 11):
    num = random.randint(1, 50)
    first_list.append(num)
print(first_list)

second_list = []
for i in range(1, 11):
    num2 = int(input('Enter 10 random numbers: '))
    second_list.append(num2)
print(second_list)

third_list = [x*y for x,y in zip(first_list, second_list)]
print(third_list)
