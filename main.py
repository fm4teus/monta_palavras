# A lógica do programa se baseia em 

from src.word_functions import *
from src.read_write_files import *


letter_score = read_json(letters_json_filename)
if not letter_score:
    write_letter_json(letters_filename, letters_json_filename)
    letter_score = read_json(letters_json_filename)

words = read_json(words_json_filename)
if not words:
    write_words_json(words_filename, words_json_filename)
    words = read_json(words_json_filename)

words_collection = get_sorted_words_collection( words, letter_score )

sorted_word_list = get_sorted_word_list( words_collection )

while True:
    word_input = input("\n\nDigite as letras disponíveis nesta jogada: ")
    if word_input == '-1':
        break
    
    response = find_highest_value_word(word_input, sorted_word_list)

    if response:
        response = Game_Word(response, letter_score)
        print("\n" + response.get_word().upper() + ", palavra de " + str( response.get_score() ) + " pontos")
        
        remaining = remaining_input_letters(response.get_word(), word_input.lower())
        if remaining:
            str_remaining = ''
            for item in remaining:
                str_remaining += (item + ', ')

            print("Sobraram: " + str_remaining.upper())
    else:
        str_remaining = ''
        for item in word_input:
            str_remaining += (item + ', ')
        print("\nNenhuma palavra encontrada")
        print("Sobraram: " + str_remaining.upper())
