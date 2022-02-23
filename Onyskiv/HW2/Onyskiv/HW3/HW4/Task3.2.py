import math
from tkinter.messagebox import YES
answer1=answer2=answer3='no'
answer1=input("Do you prefer rectangle?")
if answer1=='yes':
    side1=float(input("Enter the first side of the rectangle:"))
    side2=float(input("Enter the second side of the rectangle:"))
    print("Square of the rectangle=",side1*side2)
else:
 answer2=input("Do you prefer triangle?")
 if answer2=='yes':
    side1=float(input("Enter the first side of the triangle:"))
    side2=float(input("Enter the second side of the triangle:"))
    side3=float(input("Enter the third side of the triangle:"))
    halfperimetr=(side1+side2+side3)/2
    trianglearea=math.sqrt(halfperimetr*(halfperimetr-side1)*(halfperimetr-side2)*(halfperimetr-side3))
    print("Square of the triangle=",trianglearea)
 else:
  answer3=input("Do you prefer circle?")
  if answer3=='yes':
    radius=float(input("Enter the radius of the circle:"))
    squarecircle=3.14*radius**2
    print("Square of the circle=",squarecircle)
print ("Thank you")

