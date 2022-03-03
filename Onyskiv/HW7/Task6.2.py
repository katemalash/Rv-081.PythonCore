frstString=set(input('Enter first string (only letters and numbers:'))
secondString=set(input('Enter second string (only letters and numbers:'))

interSet=frstString.intersection(secondString)
print('intersection:',sorted(interSet))

differSet=frstString.difference(secondString)
print('difference1:',sorted(differSet))

differSet=secondString.difference(frstString)
print('difference2:',sorted(differSet))

