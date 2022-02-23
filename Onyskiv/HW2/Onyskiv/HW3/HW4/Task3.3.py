from num2words import num2words

num=float(input("Enter the number:"))
if num>=0: 
    sign='positive' 
    pnum=num
else: 
    sign='negative'
    pnum=-1*num
dig=len(str(pnum))-2
print(sign,' ',num2words(dig),'-digit')

