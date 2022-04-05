#Character string is given. Develop a program that removes from this line all repeated occurrences of numbers and signs of arithmetic operations. 
main_list = [67, 7, 89, 7, 2, 7, 4, 4, 4, 22, 22, 22, 'p', 'p', 'q', 'q', '@', '@', '(', '(', ')', ')', 'U', 'U', 'o', '#', '#', '#', '$', '%', '=', '=']
newlist = []

for i in main_list: 
    if i not in newlist: 
        newlist.append(i)
print(newlist)
