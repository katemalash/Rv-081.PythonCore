fill = input('Enter the character for fill rectangle ')
outline = input('Enter the character for outline rectangle ')
height = 10
width = 20
print(outline*width)
for i in range(1,height-1):
    print(outline+fill*(width-2)+outline)
print(outline*width)