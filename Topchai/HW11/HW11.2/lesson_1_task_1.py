while True:
    try:
        try:
            a = int(input("\nDefine numebr a "))
            b = int(input("Define number b "))
        except ValueError:
            print("a and b should be numbers.")
  

        addition = a + b
        subtraction = a - b
        multiplication = a * b
        
        try:
            division = a / b
        except ZeroDivisionError:
            print("\na can't devide by 0.")

        print ("a + b =", addition)
        print ("a - b =", subtraction)
        print ("a * b =", multiplication)
        print ("a / b =", division)
        
    except NameError:
        print("\na or b does not entered correctly.")
    
    new_try = input("\nWould you like to try again? Yes/No").lower()
    
    if new_try == "yes":
        pass
    
    elif new_try == "no":
        break
