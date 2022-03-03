stringInput=input('Enter string:')

stringLength=len(stringInput)
newString=[]
stringOut=''

for i in range(stringLength):
    stringChar=stringInput[i]
    if stringChar!=stringInput[i-1]:
        newString.append(stringChar)
for i in newString:
    stringOut+=i

print('New string:',stringOut)

