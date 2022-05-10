"""
Create a function calculator(arg) that takes 1 argument: 1, 2, 3 or 4. This function
should return function sum(a,b) if arg=1, dif(a,b) if arg = 2, product(a,b) if arg = 3
and fraction(a,b) if arg=4
"""


def calculator(arg):
    """Functions that return fuction depending on the entry"""

    def calcSum(a, b):
        """Calculate sum of a and b"""

        result = a + b
        return f"{a} + {b} = {result}"

    def calcDif(a, b):
        """Calculate dif of a and b"""
        result = a - b
        return f"{a} - {b} = {result}"

    def calcProduct(a, b):
        """Calculate product of a and b"""

        result = a * b
        return f"{a} * {b} = {result}"

    def calcFraction(a, b):
        """Calculate fraction of a and b"""

        result = a / b
        return f"{a} / {b} = {result}"

    if arg == 1:
        return calcSum

    elif arg == 2:
        return calcDif

    elif arg == 3:
        return calcProduct

    elif arg == 4:
        return calcFraction


stopper = 0

while True:
    action1 = int(input("\nChoose the action: "))
    callCalc = calculator(action1)
    argA = int(input("a = "))
    argB = int(input("b = "))

    print(callCalc(argA, argB))

    action2 = input("\nWould your like to try again? yes/no >>> ").lower()

    if action2 == "yes":
        continue
    elif action2 == "no":
        break
    else:
        print("\nWrong input. Try again.")
