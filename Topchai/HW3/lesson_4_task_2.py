bytes = int(input("Enter the amount in bytes: "))

kilobytes = bytes/1024
print (f"\n{bytes} bytes are equal to {kilobytes} Kilobytes")

megabytes = kilobytes/1024
print (f"\n{bytes} bytes are equal to {megabytes} Megabytes")

gigabytes = megabytes/1024
print (f"\n{bytes} bytes are equal to {gigabytes} Gigabytes")

terabytes = gigabytes/1024
print (f"\n{bytes} bytes are equal to {terabytes} Terabytes","\n")