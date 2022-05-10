"""
The user makes a deposit of n dollars for year at 10% per annum (each year the
amount of his deposit increases by 10%. This amount is added to the deposit amount,
and next year there will also be interest on it).

Create a bank function that takes the arguments n and years and returns the 
amount that will be in the user's account.
"""

def deposit_calc(amount, years, percent):
    """This function creates a bank function that takes the arguments amount, 
    years, percent and returns the amount that will be in the users's account"""

    counter = 1
    percent = percent / 100

    for i in range(years):
        amount = amount + amount * percent

        print(f"Year {counter} = {round(amount, 1)}$")

        counter += 1

    return (f"Year {years} = {round(amount, 1)}")

if __name__ == "__main__":
    print("-"*140)

    amount = int(input("Enter the amount of deposit: "))
    years = int(input("Enter the number of years: "))
    percent = int(input("Enter the interest per annum: "))

    print("-"*140)

    deposit_calc(amount, years, percent)

    print("-"*140)

    while True:
        users_entry = input("Would you like to try again? Yes/No: ").lower()
        
        if users_entry == "yes":
            print("-"*140)

            amount = int(input("Enter the amount of deposit: "))
            years = int(input("Enter the number of years: "))
            percent = int(input("Enter the interest per annum: "))
            
            print("-"*140)

            deposit_calc(amount, years, percent)

            print("-"*140)
            
        elif users_entry == "no":

            print("\nGLORY TO UKRAINE!")

            print("-"*140)

            break