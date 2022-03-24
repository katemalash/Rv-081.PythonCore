'''
Find the maximum elements among the minimum elements of the matrix columns.
'''

import random

columns = 5
rows = 5

numberList = []
minList = []

for i in range(columns):

    numberList.append([])

    for x in range(rows):

        numberList[i].append(random.randint(10,99))

    print(numberList[i])

minList.append(min(numberList[0]))
minList.append(min(numberList[1]))
minList.append(min(numberList[2]))
minList.append(min(numberList[3]))
minList.append(min(numberList[4]))

max(minList)

print(f"\nFrom the minimal elements of all lists {minList}, the bigest one is {max(minList)}")


