import random


matrix = [[random.randint(1, 100) for a in range(3)],
          [random.randint(1, 100) for b in range(3)],
          [random.randint(1, 100) for c in range(3)]]
minimal_number =[]
element = 0

for i in range(3):
        minimal_number.append(min(matrix[0][element], matrix[1][element], matrix[2][element]))
        element += 1
print(matrix)
print(minimal_number)
print(max(minimal_number))
