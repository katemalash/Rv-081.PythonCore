stringa = 'Let assume that 22***78+22455---444/////11 equal to 3333.'
numbers_and_signs = '/*-+0123456789'
new_string = ''
printed = ''
i = 0 

while i < len(stringa):
    if stringa[i] not in numbers_and_signs:
        new_string += stringa[i]
        i += 1
    else:
        if stringa[i] != printed:
            new_string += stringa[i]
            printed = stringa[i]
            i += 1
        else:
            printed = stringa[i]    
            i += 1
print(new_string)            
