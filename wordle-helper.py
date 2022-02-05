f = open('wordle-answers-alphabetical.txt', 'r')
words = []
for word in f:
    words.append(word)
f.close()

def remove_letter(letter):
    """If letter in word, remove word from possible answer list

    Args:
        letter ([type]): [description]
    """
    for word in words:
        if letter in word:
            words.remove(word)

def filter_letter(letter):
    """If letter not in word, remove word from possible answer list

    Args:
        letter ([type]): [description]
    """
    for word in words:
        if not letter in word:
            words.remove(word)

def wrong_pos(letter, pos):
    filter_letter(letter)
    
    for word in words:
        if word[pos-1] == letter:
            words.remove(word)

def correct_pos(letter, pos):
    filter_letter(letter)
    
    for word in words:
        if word[pos-1] != letter:
            words.remove(word)

print("--- Welcome to Wordle Helper ---")
print("--- We reccomend your first guess be 'ROATE' ---")

while True:
    word = input('Enter the word you guessed: ')
    success = input('What color is each letter? (y)ellow, (g)reeen, or (n)one: ')

    for i in range(5):
        letter = word[i]
        color = success[i]
        slot = i+1

        if color == 'y':
            wrong_pos(letter, slot)
        elif color == 'g':
            correct_pos(letter, slot)
        else:
            remove_letter(letter)

    if len(words) == 1:
        break

    print(f'There are {len(words)} words left.')
    display = input("Display them? y or n: ")
    if display == 'y':
        print(words)

print('You Won')
print(f'The word is {words[0]}')