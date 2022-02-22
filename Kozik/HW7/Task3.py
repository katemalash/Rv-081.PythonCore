countries_and_cities = {
    'Ukraine': ['odessa', 'kharkiv', 'kyiv', 'dnipro', 'zdolbuniv'],
    'Russia': ['moscow', 'vladivostok', 'ulan-ude'],
    'Somali': ['magadisho', 'meliorativnoe']
}

city_of_user = input('Enter your city: ').lower()

for country in countries_and_cities:

    if city_of_user in countries_and_cities[country]:
        print(f'Country: {country}')
