from reccomend_word import make_reccomendation
from remove import remove_words

f = open('wordle-answers-alphabetical.txt', 'r')
words = []
for word in f:
    words.append(word)
f.close()

print("--- Welcome to Wordle Helper ---")
print("--- We reccomend your first guess be 'ROATE' ---")

while True:
    word = input('Enter the word you guessed: ')
    success = input('What color is each letter? (y)ellow, (g)reeen, or (n)one: ')

    words = remove_words(word, success, words.copy())

    if len(words) == 1:
        break

    print(f'There are {len(words)} words left.')
    display = input("Display them? y or n: ")
    if display == 'y':
        print(words)

    # reccomendation = make_reccomendation(words)
    # print(f"--- We reccomend you guess {reccomendation} next ---")

print('You Won')
print(f'The word is {words[0]}')