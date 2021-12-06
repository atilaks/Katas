import unittest
from KataKoan import *

class NuevosTest(unittest.TestCase):
    def test_three_ones_roll(self):
        #Arrange
        game1 = Game()
        expected = 1000
        roll = [1, 1, 1, 2, 2]

        #Act
        result = game1.ramon(roll)

        #Assert
        self.assertEqual(expected, result)

if __name__ == "__main__":
    unittest.main()
