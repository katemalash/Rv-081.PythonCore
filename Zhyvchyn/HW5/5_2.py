list_number = [4,5,10,12,100,6,25,30,13,75]
i = 0
for number in list_number:
    if number%5 == 0:
        i += 1
print(f'We have {i} multiplaers of 5')        