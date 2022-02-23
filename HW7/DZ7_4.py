str_user = input("Enter :")
list_user = []
repetition_words = dict()

list_user.extend(str_user.split(" "))

for i in list_user:
    if i not in repetition_words:
        repetition_words[i] = 1
    else:
        key_words = repetition_words[i]
        repetition_words[i] = key_words+1
        key_words = 0

print(repetition_words)
