def Rectangle():
    a = int(input('Please enter width of the rectangle: '))
    b = int(input('Please enter heigth of the rectangle: '))
    p = 2*(a+b)
    s = a*b
    print (f'Perimetrs of the rectangle: {p} ,\nArea of the rectangle: {s}')

def Triangle():
    import math
    a = int(input('Please enter katet 1: '))
    b = int(input('Please enter katet 2: '))
    hypo = math.sqrt(a**2 + b**2)
    print (f'Lenght of the hypotenuse: {hypo}.')

def Circle():
    r = int(input('Please enter radius: '))
    Pi = 3.14
    S = Pi * r ** 2
    P = 2 * Pi * r
    print (f'Area ofthe circle: {S} \nPerimetr of the circle: {P}')

def Task():
    task = input(('Please make your choice:\n"1" - launch Rectangle,\n"2" - launch Triangle,\n"3" - launch   Circle,\n'))
    
    if task == '1':
        Rectangle()

    if task == '2':
        Triangle()

    if task == '3':
        Circle()

Task()

