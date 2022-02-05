words = []

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

def remove_words(word, colors, input_words) -> list:
    global words 
    words = input_words

    for i in range(5):
        letter = word[i]
        color = colors[i]
        slot = i+1

    if color == 'y':
        wrong_pos(letter, slot)
    elif color == 'g':
        correct_pos(letter, slot)
    else:
        remove_letter(letter)

    return words