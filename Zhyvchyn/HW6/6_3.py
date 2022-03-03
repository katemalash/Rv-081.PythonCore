"""Task 3
Find the maximum element among the minimum elements of the matrix columns. 
"""
from random import randint


matrix = [[randint(0,50) for i in range(0,5)] for i in range(0,5)]

max_min = max([min([row[i] for row in matrix]) for i in range(0,5)])

print(matrix)    
print(max_min)
