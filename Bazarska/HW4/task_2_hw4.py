
question = input('''Which figure area you would like to calculate?:
A) Triangle
B) Rectangle
C) Circle
[A/B/C]? : ''')

pi_number = 3.141592653589793

if question == 'A':
    len_a = int(input('Write the side a length '))
    len_b = int(input('Write the side b length '))
    trngl_area = (len_a*len_b) * 0.5
    print('Triangle area equals to ', trngl_area, 'cm')
elif question == 'B':
    side_a = int(input('Write the heigh length '))
    side_b = int(input('Write the width length '))
    rect_area = side_a * side_b
    print('Rectangle area equals to ', rect_area, 'cm²')
elif question == 'C':
    radius = int(input('Write the radius '))
    circle_area = pi_number * radius**2
    print('Circle area equals to', circle_area, 'cm²')
else:
    print('Invalid choice')









