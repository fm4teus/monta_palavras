import unittest
from src.word_functions import *
from src.read_write_files import *
from src.word import Game_Word


class FindWordTestCase(unittest.TestCase):
    """Realiza testes na função find_highest_value_word"""

    def setUp(self):
        """Inicializa valores importantes para realização dos testes"""
        letter_score = read_json(letters_json_filename)
        words = read_json(words_json_filename)
        words.sort()
        words_dicts = []

        for word in words:
            words_dicts.append( Game_Word(word, letter_score) )

        words_dicts.sort(key=get_word_dict_score, reverse=True)
        self.word_list = []
        for words_dict in words_dicts:
            # print( words_dict.get_word() + ': ' + str(words_dict.get_score()) )
            self.word_list.append( words_dict.get_word() )


    def test_input_queijo(self):
        """Entrada com os caracteres com a palavra queijo (a mais valiosa)"""
        word_input = 'ABSQlamsiEluJaOas'
        response = find_highest_value_word(word_input, self.word_list)
        self.assertEqual(response, 'queijo')
    
    def test_input_dor(self):
        """Entrada com os caracteres com a palavra DOR"""
        word_input = 'AmenoDoriME'
        response = find_highest_value_word(word_input, self.word_list)
        self.assertEqual(response, 'dor')
    
    def test_input_empate_deixar(self):
        """Teste de desempate (deixar x montanha) escolhe menor"""
        word_input = 'MonXARtaNhadeI'
        response = find_highest_value_word(word_input, self.word_list)
        self.assertEqual(response, 'deixar')
    
    def test_input_empate_coisas(self):
        """Teste de desempate (coisas x drogas) escolha alfabetica"""
        word_input = 'aSDRogCoiS'
        response = find_highest_value_word(word_input, self.word_list)
        self.assertEqual(response, 'coisas')
    
    def test_input_sem_repetir(self):
        """Teste MANADA com apenas dois A's (verifica se o programa exige 3 ocorrencias da letra A)"""
        word_input = 'mndAA'
        response = find_highest_value_word(word_input, self.word_list)
        self.assertEqual(response, False)
    
    def test_input_falha(self):
        """Entrada com caracteres que não formam nenhuma palavra"""
        word_input = 'Putitrain'
        response = find_highest_value_word(word_input, self.word_list)
        self.assertEqual(response, False)
    
    def test_input_vazio(self):
        """Entrada vazia"""
        word_input = ''
        response = find_highest_value_word(word_input, self.word_list)
        self.assertEqual(response, False)

    
unittest.main()