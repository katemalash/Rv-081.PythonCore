def type_definition(seq):
    seq = set(seq)
    reserve_set = set(seq)

    for element in reserve_set:

        if element.isdigit():
            seq.add(int(element))
            seq.remove(element)

    return seq


first_set = input('Enter set of elements #1: ')
second_set = input('Enter set of elements #2: ')

first_set = type_definition(first_set)
second_set = type_definition(second_set)

common_elements = first_set & second_set
different_elements = (first_set | second_set) - common_elements

print(f'\nCommon set: {common_elements}\n'
      f'Different set: {different_elements}')
