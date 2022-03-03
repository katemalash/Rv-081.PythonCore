negativeNumber=0
positiveNumber=0

for i in range(1,20):
 userNumber=int(input('Enter the number:'))
 if userNumber<0:
      negativeNumber=negativeNumber+1
 elif userNumber>0:
      positiveNumber=positiveNumber+1
 else:
     print('Percentage of entered positive numbers to negative numbers=',round(positiveNumber/(negativeNumber+positiveNumber)*100,2))
print('Percentage of entered positive numbers to negative numbers=',round(positiveNumber/(negativeNumber+positiveNumber)*100,2))