print("Enter the width and height to calculate the area and perimeter of the rectangle:")
rectangle_width = int(input("The width is "))
rectangle_height = int(input("The height is "))

rectangle_perimetr = 2 * (rectangle_width+rectangle_height)
print(f"The perimetr of rectangle is: {rectangle_perimetr}")

rectangle_area = rectangle_width * rectangle_height
print(f"The area of rectangle is: {rectangle_area}")