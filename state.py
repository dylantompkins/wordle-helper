class State:
    def __init__(self, words: list) -> None:
        self.words = words

    def remove_letter(self, letter):
        self.words = [word for word in self.words[:] if not letter in word]

    def correct_pos(self, letter, pos):
        self.words = [word for word in self.words[:] if letter == word[pos]]

    def wrong_pos(self, letter, pos):
        # only words containing the letter
        self.words = [word for word in self.words[:] if letter in word]
        
        # eliminate the words that have letter at pos
        self.words = [word for word in self.words[:] if not letter == word[pos]]
