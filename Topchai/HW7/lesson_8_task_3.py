'''
Create a dictionary with the keys of which are the countries and the values of which
are a list the major cities of that country. When user enters the city, the program
should display the country in which it is located.
'''

citiesDict = {
    "Ukraine": ("Kyiv", "Kharkiv", "Odesa"),
    "USA": ("New york", "Los angeles", "Chicago"),
    "Germany": ("Berlin", "Hamburg", "Munich"),
    "Italy": ("Rome", "Milan", "Naples"),
    "Portuguese": ("Lisabon", "Porto", "Vila Nova de Gaia"),
    "France": ("Paris", "Marseille", "Lyon"),
    "Austria": ("Vienna","Graz","Linz"),
    "Finland": ("Helsinki","Tampere","Turku"),
    "Norway": ("Oslo","Bergen","Stavanger")
    }

print("""
This program will display the country of origin of the entered city.

To stop the program, enter "F". 
""")

while True:

    userInput = str(input("\nEnter name of the city: "))

    for country in citiesDict:

        if userInput in citiesDict[country]:
            print(f"\nThe {userInput} is a city of {country}\n")
    
    if userInput == "F":
        break

