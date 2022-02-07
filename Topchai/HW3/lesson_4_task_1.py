a = int(input("Enter A "))
b = int(input("Enter B "))

print ("Values:","A =", a, "B =", b)

a, b = b, a

print (f"Swapped values: A = {a}, B = {b}")