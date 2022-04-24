def date(day, month, year):
    monthThirtyOne = [1, 3, 5, 7, 8, 10, 12]
    monthThirty = [4, 6, 9, 11]
    if day <= 31 and month in monthThirtyOne:
        return True
    elif day <= 30 and month in monthThirty:
        return True
    elif month == 2:
        if year % 4 == 0:
            if year % 100 == 0 and day >= 29:
                return False
            else:
                return True
        elif day <= 28:
            return True
        else:
            return False
    else:
        return False


if __name__ == "main":
    dayU = int(input(">>"))
    monthU = int(input(">>"))
    yearU = int(input(">>"))
    print(date(dayU, monthU, yearU))
