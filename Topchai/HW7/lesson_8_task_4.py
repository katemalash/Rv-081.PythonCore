"""
User enters the text. A word is a sequence of non-empty characters that follow in a
row, words are separated by one of more spaces.

Create a dictionary in which the keys are the words from the sentence, and the
values - the number of it's occurrences in the sentence.
"""

sentence = input('Enter your text: ')
sentence = sentence.split(' ')

words_count = {}

for i in sentence:
    if i not in words_count:
        words_count[i] = 1
    else:
        words_key = words_count[i]
        words_count[i] = words_key+1

for i, x in words_count.items():
    print(i, x)