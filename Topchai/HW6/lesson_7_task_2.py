'''
Calculate the sums of each row and each column of the matrix. Complete it with a 
column that contains the sums of the elements of the rows and a row whose
elements are the sums of the elements of the columns.
'''

import random


numberList = []
sumList = []
rows = 4
columns = 5

for i in range(rows+1):
    sumList.append(0)

for i in range(columns):

    numberList.append([])

    for x in range(rows):

        numberList[i].append(random.randint(10,99))
        sumList[x] += numberList[i][x]

    numberList[i].append(sum(numberList[i]))

    print(numberList[i])

numberList.append(sumList)

print(sumList)
