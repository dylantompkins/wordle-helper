class State:
    def __init__(self, words: list) -> None:
        self.words = words
        print(words)

    def remove(self, word):
        self.words.remove(word)