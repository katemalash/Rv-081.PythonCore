#Probably it's wrong, but at least it works :) 
hall = int(input('Enter the area of the hall in m²: '))
stage = int(input('Enter the radius of the stage in m: '))
passage = int(input('Enter the area of the passage in m²: '))

pi = 3.14159265359
stage_area = pi * stage**2
final = stage_area + passage #here we calculate how much m² will be ocuppied by stage and passage

if final == hall:
    print('It suits perfectly')
elif final < hall:
    print('There is enough place for stage, passage and something else')
elif final > hall:
    print('It can\'t be placed here')
else:
    print('You have missed something')