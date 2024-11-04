# Завдання 1
'''
text = input("Введіть текстовий рядок: ")

count_G = text.count('G')
count_g = text.count('g')

print("Кількість літер 'G':", count_G)
print("Кількість літер 'g':", count_g)

if count_G > count_g:
    print("Літера 'G' зустрічається більше разів.")
elif count_g > count_G:
    print("Літера 'g' зустрічається більше разів.")
else:
    print("Літери 'G' та 'g' зустрічаються однакову кількість разів.")
'''

# Завдання 2
'''
text = input("Введіть текстовий рядок: ")
words_list = text.split()
new_list = []

for word in words_list:
    if len(word) > 1: 
        new_word = word[-1] + word[:-1]  
    else:
        new_word = word  
    new_list.append(new_word)  

print("Слова з перенесеною останньою літерою:", ' '.join(new_list))
'''

# Завдання 3
'''
input_sentence = input("Введіть речення: ")

words_list = input_sentence.split()

unique_letter_words = []

for word in words_list:
    if len(set(word)) == len(word): 
        unique_letter_words.append(word)  

print("Слова з різними літерами:", unique_letter_words)
'''

# Завдання 4
''''''
input_text = input("Введіть текстовий рядок: ")
words_list = input_text.split()

same_lenght = {}

for word in words_list:
    word_length = len(word)
    if word_length in same_lenght:
        same_lenght[word_length].append(word)  
    else:
        same_lenght[word_length] = [word] 

for length, words in same_lenght.items():
    print(f"Слова довжини {length}:")
    for word in words:
        print(word)


