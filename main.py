from word_functions import *


letter_score = read_letter_score(letters_filename)
write_letter_score(letters_json_filename, letter_score)

words = read_words(words_filename)
write_words(json_filename, words)

words_dicts = []

for word in words:
    words_dicts.append({ 'word': word, 'score': get_word_score(word, letter_score) })

words_dicts.sort(key=get_word_dict_score, reverse=True)

word_list = []

for words_dict in words_dicts:
    print(words_dict['word'] + ': ' + str(words_dict['score']))
    word_list.append(words_dict['word'])


while True:
    word_input = input("\n\nInsira uma sequencia de caracteres: ")
    if word_input == 'quit':
        break
    response = find_highest_value_word(word_input, word_list)
    if response:
        print("Palavra de maior valor: " + response)
    else:
        print("Não foi possível encontrar nenhuma palavra!")