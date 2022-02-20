"""
Task 5
Enter a number, letter or special character from the keyboard and return the entry index to the corresponding tuple accordingly.
"""

my_tuple = ('!','#','$','%','&','(',')','*','+',',','-',',','/',':',';','<','=','>','?',
            '0','1','2','3','4','5','6','7','8','9',\
            'B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',\
            'b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'
)


print(my_tuple.index(input('Enter one character ')))