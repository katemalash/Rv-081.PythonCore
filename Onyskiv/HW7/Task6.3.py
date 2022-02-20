countryDict={'Ukraine':['Kyiv','Kharkiv','Dnipro'],'USA':['New York','Los Angeles','Dallas']}

city=input('Enter large city:')
errorSign=0

for key in countryDict.keys():
    value=countryDict[key]
    valueLen=len(value)
    
    for i in range(valueLen):
        if city==value[i]:
            errorSign=1
            print('This city is from', key)

if errorSign==0:
    print('You entered wrong city')

