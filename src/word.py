class Game_Word:

    def __init__(self, word, letter_score):
        self.word = word
        self.score = self.set_score(letter_score)

    def set_score(self, letter_score):
        """
        Recebe uma palavra e uma lista com os valores das letras
        Para cada letra da palavra percorre a lista de dicionarios até encontrar
        o valor daquela letra e incrementa esse valor.
        A variável word_score é retornada contendo a pontuação daquela palavra.
        """
        list_word = list(self.word)
        word_score = 0
        for letter_word in list_word:
            for score, letters in letter_score.items():
                if letter_word in letters:
                    word_score += int(score)
                    break
        return word_score

    def get_word(self):
        return self.word
    
    def get_score(self):
        return self.score