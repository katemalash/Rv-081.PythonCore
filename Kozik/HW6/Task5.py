import random


elements = tuple([chr(random.randint(33, 126)) for _ in range(10)])

search_element = str(input('Enter the required element: '))

while search_element not in elements:
    print('Try again.')
    search_element = str(input('Enter the required element: '))

list_of_index = []

for index in range(len(elements)):
    if elements[index] == search_element:
        list_of_index.append(str(index))

print(f"\nindexes: {','.join(list_of_index)}")
