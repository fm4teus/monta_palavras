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