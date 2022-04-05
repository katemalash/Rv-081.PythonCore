#Create the function is_year_leap, that takes 1 argument - year, and returns True if the year is high, 
# and False otherwise. 
def leapYear(year):
    '''This function shows if the year is leap or not'''

    if year % 4 == 0 and year % 100 != 0:
        return True
    elif year % 400 ==0:
        return True
    else:
        return False
print(leapYear(2000))
