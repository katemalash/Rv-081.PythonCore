reserved_number = int(input('Please enter reserved number '))
top_bottom = 'top' if reserved_number%2 else 'bottom'
plase_side = 'compartment' if reserved_number<=36 else 'side'
print(f'You have {top_bottom} {plase_side} plase in the carriage.')