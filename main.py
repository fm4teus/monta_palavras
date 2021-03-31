from src.word_functions import *
from src.word import Game_Word

letter_score = read_json(letters_json_filename)
# letter_score = read_letter_score(letters_filename)
# write_letter_score(letters_json_filename, letter_score)

words = read_words(words_json_filename)
if not words:
    write_words_json()
# words = read_words(words_filename)
# write_words(json_filename, words)

words_collection = []

words.sort()

for word in words:
    words_collection.append( Game_Word(word, letter_score) )

words_collection.sort(key=get_word_dict_score, reverse=True)

word_list = []

for words_object in words_collection:
    print( words_collectionget_word() + ': ' + str(words_collectionget_score()) )
    word_list.append( words_collectionget_word() )


while True:
    word_input = input("\n\nInsira uma sequencia de caracteres: ")
    if word_input == '-1':
        break
    response = find_highest_value_word(word_input, word_list)
    if response:
        response = Game_Word(response, letter_score)
        print("Palavra de maior valor: " + response.get_word().upper())
        print("Pontos: " + str( response.get_score() ))
        
        remaining = remaining_input_letters(response.get_word(), word_input.lower())
        if remaining:
            print("Sobraram as letras: " + str(remaining))
    else:
        print("Não foi possível encontrar nenhuma palavra!")