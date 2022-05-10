def add(a,b):
    addition = a + b
    return addition

def sub(a,b):
    subtraction = a - b
    return subtraction
    
def mul(a,b):
    multiplication = a * b
    return multiplication
    
def div(a,b):
    division = a / b
    return division

if __name__ == "__main__":
    try:
        a = int(input("\nDefine numebr a "))
        b = int(input("Define number b "))

        addition = add(a,b)
        subtraction = sub(a,b)
        multiplication = mul(a,b)
        try:
            division = div(a,b)
        except ZeroDivisionError:
            print("\n'a' can't be divided by 0")

        print (f"\na + b = {addition}")
        print (f"a - b = {subtraction}")
        print (f"a * b = {multiplication}")
        print (f"a / b = {round(division, 2)}\n")
    
    except: NameError