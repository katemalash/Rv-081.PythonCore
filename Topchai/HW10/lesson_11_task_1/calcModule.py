"""
Create a module calculator that contains 4 functions: sum(a,b), dif(a,b), product(a,b) and fraction(a,b)
1. Import the entire module and use it's functions
2. Import only 2 functions and use them
3. Import all the functions and use them.
"""

def calcSum(a,b):
    """Calculate sum of a and b"""

    result = a + b
    return result

def calcDif(a,b):
    """Calculate dif of a and b"""
    
    result = a - b
    return result


def calcProduct(a,b):
    """Calculate product of a and b"""
    
    result = a * b            
    return result


def calcFraction(a,b):
    """Calculate fraction of a and b"""

    if b != 0:
        result = a / b            
        return result
    
    else:
        return "Division by zero"