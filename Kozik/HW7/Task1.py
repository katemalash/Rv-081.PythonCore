user_string = input('Enter string: ')
new_string = ''

for index in range(len(user_string)):
    if user_string[index: index + 1] != user_string[index + 1: index + 2]:
        new_string += user_string[index]

print('Result: ', new_string)
