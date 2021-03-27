import json
import unicodedata

letters_filename = 'letters.txt'
words_filename = 'words.txt'
json_filename = 'words_db.json'
letters_json_filename = 'letters_db.json'

def strip_accents(s):
    """Remove acentos de uma string"""
    return ''.join(c for c in unicodedata.normalize('NFD', s)
                  if unicodedata.category(c) != 'Mn')

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

def get_word_score(word, letter_score):
    """
    Recebe uma palavra e uma lista com os valores das letras
    Para cada letra da palavra percorre a lista de dicionarios até encontrar
    o valor daquela letra e incrementa esse valor.
    A variável word_score é retornada contendo a pontuação daquela palavra.
    """
    list_word = list(word)
    word_score = 0
    for letter_word in list_word:
        for score, letters in letter_score.items():
            if letter_word in letters:
                word_score += int(score)
                break;
    return word_score

def get_word_dict_score(word_dict):
    """Recebe um dicionário e retorna seu atributo score"""
    return word_dict['score']

def can_get_word_from_input(word_input, word_from_list):
    """
    Recebe sequência de caracteres de entrada e uma palavra
    Retorna True se for possível formar essa palavra com os caracteres dados
    e False caso contrário
    """

    word_input = list(word_input)
    word_from_list = list(word_from_list)
    remaining_letters = word_input.copy()
    
    for letter in word_input:
        if letter in word_from_list:
            word_from_list.remove(letter)
            remaining_letters.remove(letter)
        # print('input: ' + str(remaining_letters))
        # print('from list: ' + str(word_from_list) + '\n')
    
    if not word_from_list:
        return True
    else:
        return False

def find_highest_value_word(word_input, word_list):
    for word_from_list in word_list:
        if can_get_word_from_input(word_input, word_from_list):
            return word_from_list
    return False