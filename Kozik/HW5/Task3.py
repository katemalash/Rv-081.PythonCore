for first_multiplier in range(1, 10):

    for second_multiplier in range(1, 10):

        multiplication = first_multiplier * second_multiplier

        if multiplication < 10:

            multiplication = str(multiplication) + ' '

        print('{} * {} = {}'.format(second_multiplier, first_multiplier,
                                    multiplication), end='\t'*2)
    print()
