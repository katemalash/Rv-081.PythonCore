import math

leg_a = float(input('Leg a: '))
leg_b = float(input('Leg b: '))

hypotenuse = math.hypot(leg_a, leg_b)

print(f'\nc = {hypotenuse}')
