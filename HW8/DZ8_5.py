def is_year_leap(year):
    if year % 4 == 0:
        if year % 100 !=0:
            return True
        else:
            return False
    else:
        return False


print(is_year_leap(2000))