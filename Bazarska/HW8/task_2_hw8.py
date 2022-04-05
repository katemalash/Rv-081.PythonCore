#The user makes a deposit of n dollars for year at 10% per annum (each year the amount of his deposit increases by 10%. 
# This money is added to the deposit amount, and next year there will also be interest on it).
# Create a bank function that takes the arguments n and years and returns the amount that will be in the user's account
def deposit(dollars, years):
    '''This function calcuates the amount of money, which you can recieve, if you would make a deposit in bank'''

    for i in range(years):
        dollars = dollars + dollars * 0.1
    return (int(dollars), years)

print(deposit(400, 5))
