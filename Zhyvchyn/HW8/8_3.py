def date(*args):
    is_correct = False 
    months = {
        30:{4,6,9,11},
        31:{1,3,5,7,8,10,12},
        28:{2}
    }

    for day,month in months.items():
        if (args[1] in month) and (args[0] <= day) and(args[2] > 0):
            is_correct = True
    return is_correct

print(date(8,2,2022))   