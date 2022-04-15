def compound_interest_calculator(money, years):
    """This function calculates compound interest"""

    percent = 10

    while years != 0:
        money += round(money * (percent / 100), 2)
        years -= 1

    return round(money, 2)


if __name__ == "__main__":

    deposit = int(input('Enter a deposit: '))
    period = int(input('Enter period: '))
    income = compound_interest_calculator(deposit, period)

    print(f'\nResult: {income}')
