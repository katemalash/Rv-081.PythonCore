#Create a dictionary with the keys of which are the countries and the values ​​of which are a list of the major cities of that country. 
# When user enters the city, the program should display the country in which it is located.
while True:
    countries = {'Ukraine':['Kyiv', 'Kharkiw', 'Odesa', 'Dnipro', 'Donetsk'],
    'Canada':['Toronto', 'Montreal', 'Calgary', 'Vancouver', 'Edmont'],
    'England':['London', 'Manchester', 'Birmingham', 'Leeds', 'Glasgow'],
    'New_Zeland':['Auckland', 'Chirstchurch', 'Wellington', 'Hamilton', 'Tauranga'], 
    'Australia':['Sydney', 'Melbourne', 'Brisbane', 'Perth', 'Adelaide']}

    city = input('Enter the city: ')

    for i in countries:
        if city in countries[i]:
            print(i)
            