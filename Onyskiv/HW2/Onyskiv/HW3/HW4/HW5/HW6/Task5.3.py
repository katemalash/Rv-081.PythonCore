matrix=[[1,2,3],[4,5,6],[7,8,9]]
minList=[]
minCol=[]

for i in range(3):
    for j in range(3):
     minNum=matrix[j][i]
     minList.append(minNum)
    minColnum=min(minList)
    minCol.append(minColnum)
    minList=[]

minMax=max(minCol)

print(minMax)

