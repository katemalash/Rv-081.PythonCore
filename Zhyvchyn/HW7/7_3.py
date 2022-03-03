countries  = {
    'Ukraine':{'Kyiv','Kharkiv','Dnipro','Lviv','Rivne','Lutsk'},
    'Poland':{'Warsaw','Lublin','Wroclaw'},
    'India':{'Delhi','Mumbai','Kolkata'},
    'Japan':{'Tokyo','Osaka','Nagoya','Fukuoka'},,
    'Unated States':{'New York','Los Angeles','Chicago','Housto','Dallas'}

}
city = input('Enter the city ')

for key in countries:
    if city in countries[key]:
        print(f'{city} located in {key}')
   