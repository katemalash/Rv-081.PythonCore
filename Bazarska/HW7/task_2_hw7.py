#There are two character strings of lowercase and uppercase Latin letters and numbers. Develop a program that builds and prints in alphabetical 
# order the set of letters that are in both arrays and the set of letters of the first and second arrays separately.
first_string = set(input('Enter a few words and/or numbers: '))
second_string = set(input('Enter a few words and/or numbers: '))

print(sorted(first_string))
print(sorted(second_string))
print(sorted(first_string.union(second_string)))
