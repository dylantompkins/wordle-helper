class State:
    def __init__(self, words: list) -> None:
        self.words = words

    def remove_letter(self, letter):
        self.words = [word for word in self.words[:] if not letter in word]