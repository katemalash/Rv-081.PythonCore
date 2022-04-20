def info_countries(city):
    countries_cites = {"Ukraine": ["Kiev", "Kharkiv", "Dnipro", "Lviv"],
                       "USA": ["Los Angeles", "New-York", "Washington"],
                       "China": ["Shanghai", "Beijing", "Guangzhou"], "Norway": ["Oslo", "Bergen", "Trondheim"]}
    for i in countries_cites:
        if city in countries_cites[i]:
            return i


if __name__ == "main":
    print(info_countries(input("Enter city: ")))
