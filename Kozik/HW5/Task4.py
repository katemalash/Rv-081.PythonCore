height = int(input('Enter height: '))
width = int(input('Enter width: '))

print()

for number_string in range(height):

    if number_string == 0 or number_string == height - 1:

        print('#' * width)

    else:

        print('#' + '.'*(width - 2) + '#')
