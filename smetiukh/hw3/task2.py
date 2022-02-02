bytes = float(input('Enter Bytes'))

kilobytes = (bytes * 0.0009765625)  # 1 kilobyte = 1024 bytes
megabytes = (bytes * (9.537 * (10 ** -7)))  # 1 Megabyte = 1048576 bytes

print('Amount in kilobytes = ', kilobytes, '\n'
      'Amount in megabytes = ', megabytes)
