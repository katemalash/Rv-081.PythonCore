#plowad i perimetr priamoygolnika

from turtle import width


height = float (input("введите высоту: "))
width = float (input ("введите ширину: "))
area = height * width
perimetr = height * 2 + width * 2
print ("площадь " + str (area))
print ("периметр " + str(perimetr))


