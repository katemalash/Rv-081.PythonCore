from CustomError import*


while True:
    try:
        bytes = int(input("Enter the amount in bytes: "))
        
        if bytes < 0 or bytes > 100000000000000:
            raise CustomError("Enetred number of bytes is out of range (0 - 100000000000000)")
        
        else:
            kilobytes = bytes/1024
            print (f"\n{bytes} bytes are equal to {kilobytes} Kilobytes")

            megabytes = kilobytes/1024
            print (f"\n{bytes} bytes are equal to {megabytes} Megabytes")

            gigabytes = megabytes/1024
            print (f"\n{bytes} bytes are equal to {gigabytes} Gigabytes")

            terabytes = gigabytes/1024
            print (f"\n{bytes} bytes are equal to {terabytes} Terabytes","\n")
        
    except ValueError:
        print("Worng input. Please enter a number.")
        
    except CustomError as e:
        print("We obtain error:", e.data)