from math import sqrt


def is_prime(number):
    i = 1
    prime = True
    while i<sqrt(number):
        i += 1
        if number%i == 0:
            prime = False
            break    
    return prime

print(is_prime(17))