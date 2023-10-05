import unittest
from game.dictionary import Dictionary

class TestDictionary(unittest.TestCase):
    def test_simple_verify(self):
        dic = Dictionary()
        word = "Casa"
        self.assertEqual(dic.verify_word(word), True)
    def test_verify_false_word(self):
        dic = Dictionary()
        word = "Kadabra"
        self.assertEqual(dic.verify_word(word), False)
    def test_verify_word_with_accents(self):
        dic = Dictionary()
        word = "Café"
        self.assertEqual(dic.verify_word(word), True)
    def test_verify_word_with_dieresis(self):
        dic = Dictionary()
        word = "Cigüeña"
        self.assertEqual(dic.verify_word(word), True)