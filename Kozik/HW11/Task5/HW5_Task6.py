dict_of_user_numbers = {'Negative': 0, 'Positive': 0}
try:
    while True:

        while True:

            try:
                user_number = int(input('Enter number: '))

            except ValueError:
                print('Incorrect value')

            else:
                break

        if user_number < 0:

            dict_of_user_numbers['Negative'] += 1

        elif user_number > 0:

            dict_of_user_numbers['Positive'] += 1

        else:

            print('You have exited the program.')
            break

    summ = dict_of_user_numbers['Negative'] + dict_of_user_numbers['Positive']

    print(f"\nNegative - { dict_of_user_numbers['Negative'] / (summ/100)}%\n"
          f"Positive - {(dict_of_user_numbers['Positive'] / (summ/100))}%")

except Exception:
    print('Something extraordinary')
