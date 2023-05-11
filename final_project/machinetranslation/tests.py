import unittest
from translator import english_to_french, french_to_english

class TranslatorTestCase(unittest.TestCase):

    def test_englishToFrench_null_input(self):
        result = english_to_french("Hello")
        self.assertNotEqual(result, "")
        self.assertNotEqual(result, None)

    def test_englishToFrench_translation(self):
        result = english_to_french("Hello")
        self.assertNotEqual(result, "")
        self.assertNotEqual(result, None)
        self.assertNotEqual(result, "Hello")

    def test_frenchToEnglish_null_input(self):
        result = french_to_english("Bonjour")
        self.assertNotEqual(result, "")
        self.assertNotEqual(result, None)

    def test_frenchToEnglish_translation(self):
        result = french_to_english("Bonjour")
        self.assertNotEqual(result, "")
        self.assertNotEqual(result, None)
        self.assertNotEqual(result, "Bonjour")

if __name__ == '__main__':
    unittest.main()

