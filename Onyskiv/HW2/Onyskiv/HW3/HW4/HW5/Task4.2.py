i=1
sum_5=0

while i<=10:
    nat_number=int(input('Enter natural number greater then 2:'))
    if nat_number%5==0:
      sum_5=sum_5+1

    i+=1

print('You put',sum_5,' numbers multiplies of 5')

