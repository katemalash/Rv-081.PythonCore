P = 12
H = 20
sum = 0
product = 1
numbers = 0
while True:
    number = int(input('Enter number '))
    if (number == P) or (number == H):
        break
    else:
        if number < P:
            sum += number
        elif number > H:
            product *= number
        else:
            numbers += 1

product = product if product > 1 else 0            
print(f'Sum of less then {P} {sum},\
product of grater then {H} {product},\
number of numbers in range ({P},{H}) {numbers}')        