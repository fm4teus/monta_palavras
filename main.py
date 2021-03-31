from src.word_functions import *
from src.read_write_files import *
from src.word import Game_Word

letter_score = read_json(letters_json_filename)
if not letter_score:
    write_letter_json(letters_filename, letters_json_filename)
    letter_score = read_json(letters_json_filename)

words = read_json(words_json_filename)
if not words:
    write_words_json(words_filename, words_json_filename)
    words = read_json(words_json_filename)

words_collection = []

words.sort()

for word in words:
    words_collection.append( Game_Word(word, letter_score) )

words_collection.sort(key=get_word_dict_score, reverse=True)

sorted_word_list = []

for words_object in words_collection:
    print( words_object.get_word() + ': ' + str(words_object.get_score()) )
    sorted_word_list.append( words_object.get_word() )

while True:
    word_input = input("\n\nInsira uma sequencia de caracteres: ")
    if word_input == '-1':
        break
    response = find_highest_value_word(word_input, sorted_word_list)
    if response:
        response = Game_Word(response, letter_score)
        print("Palavra de maior valor: " + response.get_word().upper())
        print("Pontos: " + str( response.get_score() ))
        
        remaining = remaining_input_letters(response.get_word(), word_input.lower())
        if remaining:
            print("Sobraram as letras: " + str(remaining))
    else:
        print("Não foi possível encontrar nenhuma palavra!")