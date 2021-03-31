import json
import unicodedata

letters_filename = 'files/letters.txt'
words_filename = 'files/words.txt'
words_json_filename = 'files/words_db.json'
letters_json_filename = 'files/letters_db.json'

def strip_accents(s):
    """Remove acentos de uma string"""
    return ''.join(c for c in unicodedata.normalize('NFD', s)
                  if unicodedata.category(c) != 'Mn')

def write_words_json(words_filename, words_json_filename):
    words = read_words(words_filename)
    write_words(words_json_filename, words)

def write_letter_json(letters_filename, letters_json_filename):
    letter_score = read_words(letters_filename)
    write_words(letters_json_filename, letter_score)

def read_json(filename):
    try:
        with open(filename) as file_object:
            return json.load(file_object)
    except:
        return False

def read_letter_score(filename):
    """
    Le o arquivo de nome filename
    para cada linha cria um dicionario 
    em que a chave é a pontuação da letra
    e o valor é uma lista com as letras relacionadas a essa pontuação
    retorna uma lista desses dicionarios
    """
    letter_score = {}
    with open(filename) as file_object:
        contents = file_object.readlines()
        for line in contents:
            formated = line.lower().replace(',', '').strip().split()
            del formated[1]
            letter_score[formated[0]] = formated[1:]
        return letter_score

def read_words(filename):
    """
    Le o arquivo de nome filename
    transforma todas as palavras para letras minusculas sem acentos e outros caracteres
    retorna um vetor com essas palavras formatadas
    """
    with open(words_filename) as file_object:
        contents = strip_accents(file_object.read())
    words = contents.lower().replace('"', '').replace(',', '').replace('\n', ' ').split()
    return words

def write_letter_score(filename, letter_score):
    """
    Guarda a lista de dicionarios contendo os valores das letras em um arquivo json
    """
    with open(filename, 'w') as file_object:
        json.dump(letter_score, file_object)

def write_words(filename, words):
    """
    Guarda a lista de palavras em um arquivo json
    """
    with open(json_filename, 'w') as file_object:
        json.dump(words,file_object)

# def get_word_score(word, letter_score):
#     """
#     Recebe uma palavra e uma lista com os valores das letras
#     Para cada letra da palavra percorre a lista de dicionarios até encontrar
#     o valor daquela letra e incrementa esse valor.
#     A variável word_score é retornada contendo a pontuação daquela palavra.
#     """
#     list_word = list(word)
#     word_score = 0
#     for letter_word in list_word:
#         for score, letters in letter_score.items():
#             if letter_word in letters:
#                 word_score += int(score)
#                 break;
#     return word_score

def get_word_dict_score(word_dict):
    """Recebe um dicionário e retorna seu atributo score"""
    return ( word_dict.get_score() )*100 - len( word_dict.get_word() )

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
    word_input = word_input.lower()
    for word_from_list in word_list:
        if can_get_word_from_input(word_input, word_from_list):
            return word_from_list
    return False

def remaining_input_letters(response, user_input):
    response = list(response)
    user_input = list(user_input)
    for letter in response:
        user_input.remove(letter)
    return user_input
