#1
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

#2
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