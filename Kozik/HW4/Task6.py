place_number = int(input('Enter place number: '))

if 1 <= place_number <= 36 and place_number % 2 == 0:
    print('Top shelf in compartment.')

elif 1 <= place_number <= 36 and place_number % 2 != 0:
    print('Bottom shelf in compartment.')

elif 37 <= place_number <= 54 and place_number % 2 == 0:
    print('Top shelf on the side.')

elif 37 <= place_number <= 54 and place_number % 2 != 0:
    print('Bottom shelf on the side.')

else:
    print('Place number is invalid.')
