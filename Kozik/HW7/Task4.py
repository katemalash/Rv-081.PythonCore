text = input('Enter your text: ')
text = text.split(' ')

dict_of_words = {word: text.count(word) for word in text if '' != word}

for key, value in dict_of_words.items():
    print(key, value)
