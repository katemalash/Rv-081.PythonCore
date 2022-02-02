Size_in_bytes = int(input('Enter size (bytes): '))

kilobytes = round(Size_in_bytes / 1024, 2)
megabytes = round(kilobytes / 1024, 2)

print(f'Kilobytes = {kilobytes}\nMegabytes = {megabytes}')
