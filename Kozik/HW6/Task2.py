import random


matrix_size = 10
matrix = [[random.randint(1, 9) for i in range(matrix_size)]
          for i_for_string in range(matrix_size)]

for line in matrix:
    line.append(sum(line))

sums_of_columns = []
elements = []

for index in range(matrix_size + 1):

    for line in matrix:
        elements.append(line[index])

    sums_of_columns.append(list(elements))
    elements.clear()

matrix.append([sum(i) for i in sums_of_columns])

for line in matrix:

    for element in line:
        print(element, end='\t')

    print()

