#perevod v Kb i Mb

bytes = int(input("vvedite kolichestvo bayt "))
kilobytes = bytes // 2**10
print(str(kilobytes) + 'Kb')
megabytes = kilobytes // 2**10
print (str(megabytes) + 'Mb')
