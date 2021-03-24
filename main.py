import json

import unicodedata
def strip_accents(s):
   return ''.join(c for c in unicodedata.normalize('NFD', s)
                  if unicodedata.category(c) != 'Mn')

letters_filename = 'letters.txt'
words_filename = 'words.txt'
json_filename = 'words_db.json'
letters_json_filename = 'letters_db.json'

def read_letter_score(filename):
    letter_score = {}
    with open(filename) as file_object:
        contents = file_object.readlines()
        for line in contents:
            formated = line.lower().strip().split()
            del formated[1]
            letter_score[int(formated[0])] = formated[1:]
        return letter_score

def read_words(filename):
    with open(words_filename) as file_object:
        contents = strip_accents(file_object.read())
    words = contents.lower().replace('"', '').replace(',', '').replace('\n', ' ').split()
    return words

def write_letter_score(filename, letter_score):
    with open(filename, 'w') as file_object:
        json.dump(letter_score, file_object)

def write_words(filename, words):
    with open(json_filename, 'w') as file_object:
        json.dump(words,file_object)

letter_score = read_letter_score(letters_filename)
write_letter_score(letters_json_filename, letter_score)

words = read_words(words_filename)
write_words(json_filename, words)