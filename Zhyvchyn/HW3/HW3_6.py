#1 For each philatelist, I created a dictionary, where the name of the collection is the key and the name of  marks
#holding in tuples
philatelist_1 = {
    'cats':('grey', 'white','black','black-white'),
    'cars':('Opel','Mazda'),
    'elephants':('John','Alex')
}
philatelist_2 = {
    'cats':('foxy','grey'),
    'cars':('Skoda','BMW','Renault'),
    'elephants':('Alfred','Amelie','Cindy')
}

temp = philatelist_1['cars']
philatelist_1['cars'] = philatelist_2['cars']
philatelist_2['cars'] =temp
print(philatelist_1)
print(philatelist_2)

#2 If we need save information only about unique ones, then we hold items of marks in the set
philatelist_3 = {
    'cats':{'grey', 'white','black','black-white'},
    'cars':{'Opel','Mazda'},
    'elephants':{'John','Alex'}
}
philatelist_4 = {
    'cats':{'foxy','grey'},
    'cars':{'Skoda','BMW','Renault','BMW'},
    'elephants':{'Alfred','Alfred','Amelie','Cindy'}
}

print(philatelist_3)
print(philatelist_4)