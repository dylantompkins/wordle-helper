import stat
from state import State

f = open('wordle-answers-alphabetical.txt', 'r')
words = []
for word in f:
    just_word = word[:5] # strip newline
    words.append(just_word)
f.close()

state = State(words[:])

print("--- Welcome to Wordle Helper ---")
print("--- We reccomend your first guess be 'ROATE' ---")

while True:
    guess = input("What word did you guess?: ")
    # colors = input("Colors (y g n): ")

print('You Won')
print(f'The word is {words[0]}')