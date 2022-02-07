reserved_carriage = int(input("Enter your place"))
if (reserved_carriage % 2 == 0):
    print("Top")
else:
    print("Bottom")
if reserved_carriage <= 36:
    print("Compartment")
else:
    print("Side")
if reserved_carriage > 54:
    print("Seat doesn't exist")
