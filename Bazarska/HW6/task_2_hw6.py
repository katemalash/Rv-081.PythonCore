#Calculate the sums of each row and each column of the matrix. Complete it with a column that 
# contains the sums of the elements of the rows 
# and a row whose elements are the sums of the elements of the columns.
x = int(input('Enter number of rows: '))
y = int(input('Enter number of columns: '))

a, sum = [], 0

print('Enter the numbers of the matrix: ')
for i in range(x):
    a.append([])
    for j in range(y):
        a[i].append(int(input()))
    print(end="\n")

for i in range (x):
    for j in range(y):
        sum = sum + a[i][j]
    print('Sum of the ', i, 'position row is ', sum)
    sum = 0

print(end='\n')
sum = 0

for j in range(y):
    for i in range(x):
        sum = sum + a[i][j]
    print('The sum of the ', j, 'position column is ', sum)
    sum = 0
