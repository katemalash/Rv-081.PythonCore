sTuple='1','2','3','4','5','a','b','c','d','e','f','#','$','&'

listNumb=[]
listChars=[]
listSpec=[]


for i in range(14):
    if 48<ord(sTuple[i])<57:
        listNumb.append(sTuple[i])
    elif 96<ord(sTuple[i])<122:
            listChars.append(sTuple[i])
    elif 34<ord(sTuple[i])<39:
            listSpec.append(sTuple[i])

listNumb=tuple(listNumb)
listChars=tuple(listChars)
listSpec=tuple(listSpec)

print(sTuple)
print(listNumb)
print(listChars)
print(listSpec)



