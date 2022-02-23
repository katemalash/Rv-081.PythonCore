from Task5 import is_year_leap


def validation_date(day, month, year):
    """This function validation date and return 'True' or 'False'."""

    flag = False
    check_month = True if 1 <= month < 13 else False
    check_year = True if year >= 1 else False

    if 1 >= day <= 28 and month and year:
        flag = True

    elif month and 30 <= day <= 31 and \
            ((month < 6 and month % 2 == 0) or (month >= 6 and month % 2 == 1)):
        flag = True

    elif day == 29 and month == 2 and is_year_leap(year):
        flag = True

    return flag


date = [int(number) for number in (input('Enter date: ')).split('.')]

print(validation_date(date[0], date[1], date[2]))
