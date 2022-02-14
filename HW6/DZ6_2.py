import random


matrix = [[random.randint(1, 100) for a in range(3)],
          [random.randint(1, 100) for b in range(3)],
          [random.randint(1, 100) for c in range(3)]]
summa_row = [0 for d in range(4)]
matrix_index_drain = 0
summa_drains = 0
number_pillar = 0

for i in matrix:
     for j in i:
         summa_drains += j
         if j == i[2]:                                               # 2 is size str in matrix-1
             matrix[matrix_index_drain].append(summa_drains)
             summa_row[number_pillar] += j
             matrix_index_drain += 1
             summa_drains = 0
             number_pillar = 0
             break
         else:
             summa_row[number_pillar] += j
             number_pillar += 1
#Print
matrix.append(summa_row)
for i in matrix:
    for l in i:
        if l == i[3]:
            print(l)
            break
        else:
            print(l, end="\t")
