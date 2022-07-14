import unittest

from translator import english_to_french, french_to_english

class TestEnglishToFrench(unittest.TestCase):
    def test_english_to_french_isequal(self):
        self.assertEqual(english_to_french("Hello"), "Bonjour")
    def test_english_to_french_isnotequal(self):
        self.assertNotEqual(english_to_french("Hello"), "Hola")
    def test_english_to_french_isnone(self):
        self.assertIsNone(english_to_french(None))
    def test_english_to_french_isnone_wheninputempty(self):
        self.assertIsNone(english_to_french(''))

class TestFrenchToEnglish(unittest.TestCase):
    def test_french_to_english_isequal(self):
        self.assertEqual(french_to_english("Bonjour"), "Hello")
    def test_french_to_english_isnotequal(self):
        self.assertNotEqual(french_to_english("Bonjour"), "Hola")
    def test_french_to_english_isnone(self):
        self.assertIsNone(french_to_english(None))
    def test_french_to_english_isnone_wheninputempty(self):
        self.assertIsNone(french_to_english(''))


suite = unittest.TestLoader().loadTestsFromTestCase(TestEnglishToFrench)
unittest.TextTestRunner(verbosity=2).run(suite)
suite = unittest.TestLoader().loadTestsFromTestCase(TestFrenchToEnglish)
unittest.TextTestRunner(verbosity=2).run(suite)