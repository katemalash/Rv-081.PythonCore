'''
Fill in one list with random numbers, another with numbers entered from the 
keyboard, and write the sums of the corresponding elements of the first wto 
lists in the third one. Display the contents of the lists on the screen.
'''

import random
from operator import add


listWithNumbers = []
listWithRandomNumbers = []
counter = 10

for i in range(10):
    randomNumbers = random.randint(1,10)
    listWithRandomNumbers.append(randomNumbers)

for i in range(10):
    userEntry = int(input("Enetr numbers: "))
    listWithNumbers.append(userEntry)
    counter -= 1
    print(f"{counter} entries left.")

sumedList = listWithNumbers + listWithRandomNumbers

print(f"""
{"-"*60}

List with entered numbers: {listWithNumbers}

List with random numbers: {listWithRandomNumbers}

Sumed list: {[x + y for x, y in zip(listWithNumbers, listWithRandomNumbers)]}

{"-"*60}
""")