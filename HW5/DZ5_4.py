height = int(input("Enter height: "))
length = int(input("Enter length: "))

print(" * " * length)
for i in range(height-2):
    print(" * "+" . "*(length-2)+" * ")
print(" * " * length)
