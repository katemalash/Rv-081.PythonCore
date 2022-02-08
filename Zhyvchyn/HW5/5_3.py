for i in range(1,10):
    row = ''
    for j in range(1,10):
        elem = f'{j}x{i}={i*(j)}'
        row += elem+' ' if len(elem)>5 else elem+'  '
                    
    print(row)