"""Task 4
Divide the tuple into several ones, each of which contains only numbers, only letters, etc."""

numbers_int = ()
numbers_float = ()
letters = ()
not_letters = ()

my_tuple = ('\n',5.3,'*',123,' ','color',-456,'A+','very',-2.487)

for item in my_tuple:
    item = (item,)
    if isinstance(item[0],str):
        if item[0].isalpha():
            letters += item
        else:
            not_letters += item   
    elif isinstance(item[0],int):
            numbers_int += item
    elif isinstance(item[0],float):
            numbers_float += item

print ('Letters',letters)
print('Not letters',not_letters)
print ('Int numbers',numbers_int)
print('Float numbers',numbers_float)
