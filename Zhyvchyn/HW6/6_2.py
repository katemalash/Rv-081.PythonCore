from random import randint


matrix = [[randint(0,10) for i in range(5)] for i in range(5)]
matrix.append([0]*5)

for i in range(5):#think about row[i]++
    suma = 0
    for j in range(5):
        suma += matrix[j][i]
    matrix[5][i] = suma 

for row in matrix:
   row.append(sum(row))

for row in matrix:
   print(row)

