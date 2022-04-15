def is_prime(num):
    """This function determines the primality of a number."""

    for divider in range(2, num):

        if num % divider == 0:
            return False

    return True


if __name__ == "__main__":

    number = int(input('Enter number: '))
    print(is_prime(number))
