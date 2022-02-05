number = int(input('Please enter  number '))
 
if number>0:
    positive_negative = 'positive'
elif number<0: 
    positive_negative = 'negative'
else:
    positive_negative = ''
    number_of_digits = ''
    print('You entered zero')

number = abs(number)
if number // 100000 == 1:
    number_of_digits = 'six'
elif number // 10000 == 1:
    number_of_digits = 'five'
elif number // 1000 == 1:
    number_of_digits = 'four'
elif number // 100 == 1:
    number_of_digits = 'three'
elif number // 10 == 1:
    number_of_digits = 'two'
elif number<10 == 1:
    number_of_digits = 'one' 
else:
    number_of_digits = 'more then six'
  
print(f'You entered {positive_negative} {number_of_digits}-digits number')
