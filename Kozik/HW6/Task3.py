import random


matrix_size = 10
matrix = [[random.randint(1, 9) for i in range(matrix_size)]
          for i_for_string in range(matrix_size)]


sums_of_columns = []
elements = []

for index in range(matrix_size):

    for line in matrix:
        elements.append(line[index])

    sums_of_columns.append(list(elements))
    elements.clear()

min_elements = [str(min(i)) for i in sums_of_columns]


for line in matrix:
    print(f'\t ', end='')

    for element in line:
        print(element, end='\t')

    print()

else:
    min_elements = '\t'.join(min_elements)
    print(f'\nMin: {min_elements}')
    print(f'\nMax from min: {max(min_elements)}')
