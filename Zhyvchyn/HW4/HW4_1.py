year = int(input('Please enter year ')) 

if (year%4 == 0):
    if year%100 == 0:
        if year%400 == 0:
            is_intercalary='intercalary'
        else:
            is_intercalary='not intercalary'  
    else:
        is_intercalary ='intercalary'
else:    
    is_intercalary='not intercalary'

print(f'{year} is {is_intercalary}, and belong to {(year//100)+1} century')           
