numberP=10
numberH=100

start=1
stop=20
userNumber=0
sumNumber=0
productNumber=1
countNumber=0

while start<stop and userNumber!=numberP and userNumber!=numberH:

 userNumber=int(input('Enter the number:'))
 if userNumber<numberP:
   sumNumber=sumNumber+userNumber
 else:
   if userNumber>numberH:
    productNumber=productNumber*userNumber
   else: 
    if numberP<userNumber<numberH:
     countNumber=countNumber+1
 start=start+1

print('Sum of numbers less,then P =',sumNumber)
print('Product of numbers, greater, then H =',productNumber)
print('Number of numbers, which are between P and H =',countNumber)

