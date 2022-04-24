def is_prime(number):
    if number == 1:
        return True
    for i in range(2, number-1):
        if number % i == 0:
            return False
    else:
        return True


if __name__ == "main":
    userInput = int(input(">>"))
    print(is_prime(userInput))
