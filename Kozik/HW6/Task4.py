tuple_with_different_elements = (4, 'r', 8, '%', 7, 't', ')', 454, '&sdds8')

alphas = []
digits = []
symbols = []

for element in tuple_with_different_elements:
    element = str(element)

    if element.isalpha():
        alphas.append(element)

    elif element.isdigit():
        digits.append(element)

    else:
        symbols.append(element)

alphas = tuple(alphas)
digits = tuple(digits)
symbols = tuple(symbols)

print(f'Alphas: {alphas}\nDigits: {digits}\nSymbols: {symbols}')
