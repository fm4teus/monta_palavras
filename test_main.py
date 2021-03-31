import unittest
from src.word_functions import *
from src.read_write_files import *


class FindWordTestCase(unittest.TestCase):
    """Realiza testes na função find_highest_value_word"""

    def setUp(self):
        """Inicializa valores importantes para realização dos testes"""
        letter_score = read_json(letters_json_filename)
        if not letter_score:
            write_letter_json(letters_filename, letters_json_filename)
            letter_score = read_json(letters_json_filename)

        words = read_json(words_json_filename)
        if not words:
            write_words_json(words_filename, words_json_filename)
            words = read_json(words_json_filename)

        words_collection = get_sorted_words_collection( words, letter_score )

        self.sorted_word_list = get_sorted_word_list( words_collection )



    def test_input_queijo(self):
        """Entrada com os caracteres com a palavra queijo (a mais valiosa)"""
        word_input = 'ABSQlamsiEluJaOas'
        response = find_highest_value_word(word_input, self.sorted_word_list)
        self.assertEqual(response, 'queijo')
    
    def test_input_dor(self):
        """Entrada com os caracteres com a palavra DOR"""
        word_input = 'AmenoDoriME'
        response = find_highest_value_word(word_input, self.sorted_word_list)
        self.assertEqual(response, 'dor')
    
    def test_input_empate_deixar(self):
        """Teste de desempate (deixar x montanha) escolhe menor"""
        word_input = 'MonXARtaNhadeI'
        response = find_highest_value_word(word_input, self.sorted_word_list)
        self.assertEqual(response, 'deixar')
    
    def test_input_empate_coisas(self):
        """Teste de desempate (coisas x drogas) escolha alfabetica"""
        word_input = 'aSDRogCoiS'
        response = find_highest_value_word(word_input, self.sorted_word_list)
        self.assertEqual(response, 'coisas')
    
    def test_input_sem_repetir(self):
        """Teste MANADA com apenas dois A's (verifica se o programa exige 3 ocorrencias da letra A)"""
        word_input = 'mndAA'
        response = find_highest_value_word(word_input, self.sorted_word_list)
        self.assertEqual(response, False)
    
    def test_input_falha(self):
        """Entrada com caracteres que não formam nenhuma palavra"""
        word_input = 'Putitrain'
        response = find_highest_value_word(word_input, self.sorted_word_list)
        self.assertEqual(response, False)
    
    def test_input_vazio(self):
        """Entrada vazia"""
        word_input = ''
        response = find_highest_value_word(word_input, self.sorted_word_list)
        self.assertEqual(response, False)

    
unittest.main()