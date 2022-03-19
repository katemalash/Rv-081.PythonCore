'''
Divide the tuple into several ones, each of which contains only numbers, only letters, etc.
'''

items = ("f" , "98", "ff1", "%", "&", "Kyiv", "I", "RyskiVoennyKorablIdiNa", "40", "138", "2", "#", "@", "1", "asdd244", "sws65", "$", "-")

numbers = []
words = []
symbols = []
mix_int_str = []

for i in items:
    if i.isdigit() == True:
        numbers.append(i)

    elif i.isalpha() == True:
        words.append(i)

    elif i.isalnum() == False:
        symbols.append(i)
    
    else:
        mix_int_str.append(i)

print(f"""
{"-"*50}
Numbers:
{numbers}

Words or letters:
{words}

Special characters:
{symbols}

Mix of numbers and characters:
{mix_int_str}
{"-"*50}
""")
