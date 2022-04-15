def is_year_leap(year):
    """This function checks if the year is a leap year."""

    result = True if (year % 4 == 0 and year % 100 != 0 and year > 0) \
        or (year % 4 == 0 and year % 400 == 0 and year > 0) else False
    return result


def validation_date(day, month, year):
    """This function validation date and return 'True' or 'False'."""

    flag = False
    number_of_month = {1: 31, 2: 29 if is_year_leap(year) else 28, 3: 31, 4: 30, 5: 31, 6: 30,
                       7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}

    if month in number_of_month.keys() and day in range(1, number_of_month[month] + 1) and year >= 1:
        flag = True

    return flag


if __name__ == "__main__":

    date = [int(number) for number in (input('Enter date: ')).split('.')]
    print(validation_date(date[0], date[1], date[2]))
