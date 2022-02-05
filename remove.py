class Remove:
    def __init__(self, words) -> None:
        self.words = words

    def remove_letter(self, letter):
        """If letter in word, remove word from possible answer list

        Args:
            letter ([type]): [description]
        """
        self.words = [word for word in self.words if not letter in word]

    def filter_letter(self, letter):
        """If letter not in word, remove word from possible answer list

        Args:
            letter ([type]): [description]
        """
        for word in self.words.copy():
            if not letter in word:
                self.words.remove(word)

    def wrong_pos(self, letter, pos):
        self.filter_letter(letter)
        
        for word in self.words.copy():
            if word[pos] == letter:
                self.words.remove(word)

    def correct_pos(self, letter, pos):        
        for word in self.words.copy():
            if word[pos] != letter:
                self.words.remove(word)

    def remove_words(self, word, colors):
        for i in range(5):
            letter = word[i]
            color = colors[i]

            if color == 'y':
                self.wrong_pos(letter, i)
            elif color == 'g':
                self.correct_pos(letter, i)
            else:
                self.remove_letter(letter)