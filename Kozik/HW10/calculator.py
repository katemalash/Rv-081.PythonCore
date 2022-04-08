def summ(a, b):
    result = a + b
    return result


def dif(a, b):
    result = a - b
    return result


def product(a, b):
    result = a * b
    return result


def fraction(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        return 'Division by zero'
    else:
        return result
