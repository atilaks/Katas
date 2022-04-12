import unittest
#from Kata_procesador_texto import Ramon

TEXT = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."

class WordProcessor:
    def __init__(self, text):
        self.text = text

    def find_word(self, ramon):
        return True


class TestWordProcessor(unittest.TestCase):
    def test_find_the_word_on_text(self):
        #Arrange
        word_processor = WordProcessor(TEXT)

        #Act
        word_goal = "amet"
        result = word_processor.find_word(word_goal)

        #Assert
        expected = True
        self.assertEqual(result, expected)

    def test_when_not_find_the_word_return_false(self):
        #Arrange
        word_processor = WordProcessor(TEXT)

        #Act
        word_goal = "cachopo"
        result = word_processor.find_word(word_goal)

        #Assert
        expected = False
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main(verbosity=2)