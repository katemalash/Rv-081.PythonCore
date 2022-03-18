def deposit(n,years):
    percent = 10
    return n*(1+percent/100)**years

print(deposit(100,7))