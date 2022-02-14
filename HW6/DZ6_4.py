mix = (1, "A", 2, "andrey", "$", 2, 222, "84", "&", "Boy6", "@", 32,)
int_list = []
str_list = []
other_list = []

for i in mix:
    if type(i) == int or i.isdigit() == True:
        int_list.append(i)
    elif i.isalpha() == True:
        str_list.append(i)
    else:
        other_list.append(i)

print(int_list)
print(str_list)
print(other_list)
