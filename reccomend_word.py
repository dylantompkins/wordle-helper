def make_reccomendation(words: list) -> str:
    """Simulate each guess/answer pair to determine the best word to guess.
       Statistically the best word based on avg number of words eliminated.

    Args:
        words (list): all the words remaining in the game

    Returns:
        str: the reccomendation
    """
    reccomendation = ''
    avg_words_removed = 0

    for guess in words:
        words_removed = []
        for answer in words:
            if answer == guess:
                continue

            # what color/letter combos would this guess/ans pair produce?
            colors = ''
            for i in range(5):
                letter = guess[i]
                if letter in answer:
                    if letter == answer[i]:
                        colors.append('g')
                    else:
                        colors.append('y')
                else:
                    colors.append('n')

            # how many words would be removed?

    return reccomendation