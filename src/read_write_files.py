import json
import unicodedata
from src.word_functions import *

letters_filename = 'files/letters.txt'
words_filename = 'files/words.txt'
words_json_filename = 'files/words_db.json'
letters_json_filename = 'files/letters_db.json'

def strip_accents(s):
    """Remove acentos de uma string"""
    return ''.join(c for c in unicodedata.normalize('NFD', s)
                  if unicodedata.category(c) != 'Mn')

def write_words_json(words_filename, words_json_filename, letter_score):
    words = read_words(words_filename)
    words_collection = get_sorted_words_collection( words, letter_score )
    sorted_word_list = get_sorted_word_list( words_collection )
    write_words(words_json_filename, sorted_word_list)

def write_letter_json(letters_filename, letters_json_filename):
    letter_score = read_letter_score(letters_filename)
    write_letter_score(letters_json_filename, letter_score)

def read_json(filename):
    try:
        with open(filename) as file_object:
            return json.load(file_object)
    except:
        print("arquivo não encontrado!")
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
    with open(filename) as file_object:
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
    with open(filename, 'w') as file_object:
        json.dump(words,file_object)