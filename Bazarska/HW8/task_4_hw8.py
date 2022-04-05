#Create the function is_prime, which takes 1 argument - a number from 0 to 1000, and returns True if it is simple, 
# and False - otherwise.
def primeNumber(number):
    '''This function shows if the number is prime or not'''

    if number == 1:
        return True
    for i in range(2, number):
        if number % i == 0:
            return False 
    else:
        return True 

print(primeNumber(73))
