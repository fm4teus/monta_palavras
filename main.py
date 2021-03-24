import json


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

def write_letter_score(filename, letter_score):
    with open(filename, 'w') as file_object:
        json.dump(letter_score, file_object)

letter_score = read_letter_score(letters_filename)
write_letter_score(letters_json_filename, letter_score)

with open(words_filename) as file_object:
    contents = file_object.read()

words = contents.lower().replace('"', '').replace(',', '').replace('\n', ' ').split()

with open(json_filename, 'w') as file_object:
    json.dump(words,file_object)

# dicionario = { 1: ['a','f'], 2: 'b'}
# print(dicionario[1])