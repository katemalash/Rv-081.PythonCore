'''
Display a multiplication table (1 to 9).
'''

rows=10
columns=10
for i in range(1,rows+1):

    for x in range(1,columns+1):
        
        c=i*x

        print("{:3d} ".format(c),end=' ')

    print("\n")