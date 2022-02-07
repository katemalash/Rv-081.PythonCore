import math
ticket = int(input('Please enter ticket number: '))
compartments = ticket / 4
compartments = math.ceil(compartments)

if ticket >= 37:
    if ticket % 2 == 0:
        print (f'You have a top side shelf')
    else:
        print (f'You have a lower side shelf')

elif ticket % 4 == 0:
    print (f'You have a top right shelf in {compartments} compartments')

elif ticket % 2 == 0:
    print (f'You have a top left shelf in {compartments} compartments')

elif ticket % 2 != 0 and (ticket+1) % 4 == 0:
    print (f'You have a lower right shelf in {compartments} compartments')
    
else:
    print (f'You have a lower left shelf in {compartments} compartments')
    
# У плацкартних вагонах 9 відкритих купе. Нумерація купейних місць починається з купе провідника, бокові починаються з 37-го місця, їхній відлік йде від туалету. Тобто, у першому купе будуть місця 1-4 та бокові 53, 54. У плацкартних та купейних вагонах непарні числа — це нижні полиці, а парні — верхні. 


