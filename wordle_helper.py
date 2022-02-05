from reccomend_word import make_reccomendation
from remove import Remove

f = open('wordle-answers-alphabetical.txt', 'r')
words = []
for word in f:
    word = word[:5]
    words.append(word)
f.close()

remove = Remove(words.copy())

print("--- Welcome to Wordle Helper ---")
print("--- We reccomend your first guess be 'ROATE' ---")

while True:
    word = input('Enter the word you guessed: ')
    success = input('What color is each letter? (y)ellow, (g)reeen, or (n)one: ')

    remove.remove_words(word, success)

    if len(remove.words) == 1:
        break

    print(f'There are {len(remove.words)} words left.')
    display = input("Display them? y or n: ")
    if display == 'y':
        print(remove.words)

    # reccomendation = make_reccomendation(words)
    # print(f"--- We reccomend you guess {reccomendation} next ---")

print('You Won')
print(f'The word is {remove.words[0]}')