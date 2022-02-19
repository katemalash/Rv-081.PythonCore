import random

randomList=[]
userList=[]
listSum=[]

for i in range(1,10):
 listMember=random.randint(1,100)
 randomList.append(listMember)
 userlistMember=int(input('Enter the number:'))
 userList.append(userlistMember)

for i in range(0,9):
 listSumMember=randomList[i]+userList[i]
 listSum.append(listSumMember)

print('Random list:',randomList)
print('User list:',userList)
print('Sum:',listSum)


