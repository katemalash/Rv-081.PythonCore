"""
Create an arithmetic function that takes 3 arguments: the first 2 are numbers, the
third is operation to be performed on them. If the third argument is +, add them;
if -, then substract; * - multiply; / - divide(first to second). In other case
the "Unknown operation" line.
"""

def calc_func(num1, num2, opp):
    """This function takes 3 arguments: the first 2 are numbers, the third is operation to be performed on them."""

    result = "Unknown operation"

    if opp == "+":
        result = num1 + num2
        
    elif opp == "-":
        result = num1 - num2

    elif opp == "*":
        result = num1 * num2

    elif opp == "/":
        result = num1 / num2

    return result

print("-"*140)

num1 = int(input("Please enter the first number: "))
num2 = int(input("Please enter the second number: "))
opp = input("Please enter the operation sign: ")

print(f"""{"-"*140}
Result: {calc_func(num1, num2, opp)}
{"-"*140}
""")
