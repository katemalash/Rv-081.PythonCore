def is_prime(number):
    if number == 1:
        return True
    for i in range(2, number-1):
        if number % i == 0:
            return False
    else:
        return True


print(is_prime(149))
