in_bytes = int(input("Enter amount in bytes "))

in_kilobytes = in_bytes/1024
in_megabytes = (in_bytes/1024) / 1024

print(f"It will be {in_kilobytes} kilobytes, or {in_megabytes} megabytes")
