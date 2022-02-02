#I think that the best solution for this task is dictionary.
#We can create 2 dictionaries which will refer to our collection and friend's one.

#my_collection
cats = {'Maine Coon': 'gentle', 'Bengal Cat': 'curious', 'Abyssinian Cat': 'highly intelligent'}
cars = {'Honda': 'Japan', 'Mercedes': 'Germany', 'Ford': 'USA'}
elephants = {'African savanna': '8,000kg', 'Asian': '5,500kg'}

#friend_collection
motorcycles = {'Suzuki': '1909', 'Yamaha': '1955', 'Kawasaki': '1896'}
dogs = {'Akita': 'fearless, loyal', 'Beagle': 'fun loving', 'Border Collie': 'endurant'}
cities = {'Toronto': 'Canada', 'Los Angeles': 'USA', 'London': 'UK'}
    
#In dictionaries we can save data because of key:value pairs

#We can refer to dictionary items by using the key name, for example:

print(cats['Maine Coon'])

#Also if we want to share our marks with someone we can use copy() method
cats = {'Maine Coon': 'gentle', 'Bengal Cat': 'curious', 'Abyssinian Cat': 'highly intelligent'}
fav_breeds = cats.copy()
print('My favourite breeds and their characteristic: ', fav_breeds)

#I don't think I know how to sort marks properly when we have the equal items
#in collection, it can be related to sort() method but I am not sure about it
