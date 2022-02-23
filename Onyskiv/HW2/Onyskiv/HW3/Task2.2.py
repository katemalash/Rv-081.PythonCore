var_byte=int(input('Enter number in bytes:'))

var_Kb=var_byte/1028
var_Mb=var_Kb/1028

print('You entered ',var_byte,' bytes, which equals ',round(var_Kb,2),'Kb',' and ',round(var_Mb,2),'Mb')

