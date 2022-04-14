while True:

    try:
        height = int(input('Enter height: '))
        width = int(input('Enter width: '))

        if height <= 0 or width <= 0:
            raise ZeroDivisionError

    except (ValueError, ZeroDivisionError):
        print('Incorrect value (this is not number or less then 1')

    else:
        print()
        break

for number_string in range(height):

    if number_string == 0 or number_string == height - 1:

        print('#' * width)

    else:

        print('#' + '.'*(width - 2) + '#')
