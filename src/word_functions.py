from src.word import Game_Word

def get_word_object_score(word_object):
    """Recebe um dicionário e retorna seu atributo score"""
    return ( word_object.get_score() )*100 - len( word_object.get_word() )

def can_get_word_from_input(word_input, word_from_list):
    """
    Recebe sequência de caracteres de entrada e uma palavra
    Retorna True se for possível formar essa palavra com os caracteres dados
    e False caso contrário
    """
    word_input = list(word_input)
    word_from_list = list(word_from_list)
    
    counter = len(word_from_list)
    
    for letter in word_from_list:
        if letter in word_input:
            word_input.remove(letter)
            counter -= 1
        if not counter:
            return True
    
    return False

def find_highest_value_word(word_input, word_list):
    """
    Recebe a entrada do usuário e a lista ordenada de palavras
    Retorna a palavra de maior valor que pode ser composta com a entrada
    """
    word_input = word_input.lower()
    for word_from_list in word_list:
        if can_get_word_from_input(word_input, word_from_list):
            return word_from_list
    return False

def remaining_input_letters(response, user_input):
    """
    Recebe a entrada a resposta e a entrada do usuário
    Retorna os caracteres da entrada que não foram usados na resposta
    """
    response = list(response)
    user_input = list(user_input)
    for letter in response:
        user_input.remove(letter)
    return user_input

def get_sorted_word_list( words_collection ):
    """
    Recebe uma coleção ordenada de objetos contendo palavra e pontuação
    Retorna uma lista ordenada de palavras
    """
    sorted_word_list = []
    for words_object in words_collection:
        # print( words_object.get_word() + ': ' + str(words_object.get_score()) )
        sorted_word_list.append( words_object.get_word() )
    return sorted_word_list

def get_sorted_words_collection( words, letter_score ):
    """
    Recebe o banco de palavras e o valor das letras
    Retorna uma coleção ordenada de objetos contendo palavra e valor
    """
    words_collection = []
    words.sort()
    for word in words:
        words_collection.append( Game_Word(word, letter_score) )
    words_collection.sort(key=get_word_object_score, reverse=True)
    return words_collection