string1 = 'Lorem ipsuM dOlOr 456 sit amet, 78 consectetur Adipiscing elit'
list1 = list(string1.split(' '))
dict1 = {list1[i]: i  for i in range(10)} 
print(dict1)