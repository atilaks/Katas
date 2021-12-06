import unittest
from KataKoan import *

class NombreDistinto(unittest.TestCase):
    def test_three_ones_roll(self):
        #Arrange
        player1 = Player()
        expected = "Tu puntuació es de: 1000"
        roll = [1, 1, 1, 2, 2]

        #Act
        result = player1.get_score(roll)

        #Assert
        self.assertEqual(expected, result)

    def test_three_six_roll(self):
        player1 = Player()
        expected = "Tu puntuació es de: 600"
        roll = [6, 6, 6, 2, 2]

        result = player1.get_score(roll)

        self.assertEqual(expected, result)

    def test_three_five_roll(self):
        player1 = Player()
        expected = "Tu puntuació es de: 500"
        roll = [5, 5, 5, 2, 2]

        result = player1.get_score(roll)

        self.assertEqual(expected, result)

    def test_three_four_roll(self):
        player1 = Player()
        expected = "Tu puntuació es de: 400"
        roll = [4, 4, 4, 2, 2]

        result = player1.get_score(roll)

        self.assertEqual(expected, result)

    def test_three_three_roll(self):
        player1 = Player()
        expected = "Tu puntuació es de: 300"
        roll = [3, 3, 3, 2, 2]

        result = player1.get_score(roll)

        self.assertEqual(expected, result)

    def test_two_three_roll(self):
        player1 = Player()
        expected = "Has terminado tu ronda. Tu puntuació es de: 0"
        roll = [2, 2, 2, 3, 3]

        result = player1.get_score(roll)

        self.assertEqual(expected, result)

    def test_one_one_on_roll(self):
        player1 = Player()
        expected = "Has terminado tu ronda. Tu puntuació es de: 0"
        roll = [1, 2, 2, 3, 3]

        result = player1.get_score(roll)

        self.assertEqual(expected, result)

    def test_one_five_on_roll(self):
        player1 = Player()
        expected = "Has terminado tu ronda. Tu puntuació es de: 0"
        roll = [5, 2, 2, 3, 3]

        result = player1.get_score(roll)

        self.assertEqual(expected, result)

    def test_multi_score_roll1(self):
        player1 = Player()
        expected = "Tu puntuació es de: 350"
        roll = [5, 2, 2, 2, 1]

        result = player1.get_score(roll)

        self.assertEqual(expected, result)

    def test_multi_score_roll2(self):
        player1 = Player()
        expected = "Tu puntuació es de: 1150"
        roll = [5, 1, 1, 1, 1]

        result = player1.get_score(roll)

        self.assertEqual(expected, result)

    def test_multi_score_roll3(self):
        player1 = Player()
        expected = "Tu puntuació es de: 650"
        roll = [5, 5, 5, 5, 1]

        result = player1.get_score(roll)

        self.assertEqual(expected, result)

    def test_second_roll_with_two_dice_reroled(self):
        player1 = Player()
        expected = "Has terminado tu ronda. Tu puntuació es de: 0"
        roll = [2, 2, 2, 6, 4]

        result = player1.get_score(roll)

        self.assertEqual(expected, result)

    def test_second_roll_more_ones(self):
        player1 = Player()
        expected = "Tu puntuació es de: 1150"
        roll = [1, 1, 1, 6, 4]
        roll2 = [1, 5]
        player1.get_score(roll)

        result = player1.get_score(roll2)

        self.assertEqual(expected, result)

    def test_second_roll_with_one_dice(self):
        player1 = Player()
        expected = "Tu puntuació es de: 1200"
        roll = [1, 1, 1, 1, 4]
        roll2 = [1]
        player1.get_score(roll)

        result = player1.get_score(roll2)

        self.assertEqual(expected, result)

    def test_without_score(self):
        player1 = Player()
        expected = "Has terminado tu ronda. Tu puntuació es de: 0"
        roll = [3, 2, 2, 6, 4]

        result = player1.get_score(roll)

        self.assertEqual(expected, result)

    def test_end_of_round_for_bad_roll(self):
        player1 = Player()
        expected = "Has terminado tu ronda. Tu puntuació es de: 0"
        roll1 = [1, 1, 1, 1, 4]
        roll2 = [3]
        player1.get_score(roll1)

        result = player1.get_score(roll2)

        self.assertEqual(expected, result)

    def test_save_high_score(self):
        player1 = Player()
        expected = "Tu puntuació es de: 1150"
        roll1 = [1, 1, 1, 6, 4]
        roll2 = [1, 5]
        player1.get_score(roll1)

        result = player1.get_score(roll2)

        self.assertEqual(expected, result)

    def test_save_high_score_and_end(self):
        player1 = Player()
        expected = "Has terminado tu ronda, tu puntuacion es de: 2250"
        roll1 = [1, 1, 1, 6, 4]
        roll2 = [1, 5]
        roll3 = [1, 1, 1, 1, 4]
        roll4 = [2, 2]
        player1.get_score(roll1)
        player1.get_score(roll2)
        player1.get_score(roll3)
        player1.get_score(roll4)

        result = player1.get_score()

        self.assertEqual(expected, result)

    def test_save_high_score_and_end(self):
        player1 = Player()
        expected = "Has terminado tu ronda. Tu puntuació es de: 0"
        roll1 = [1, 1, 1, 6, 4]
        roll2 = [1, 5]
        roll3 = [1, 1, 1, 1, 4]
        roll4 = [2, 2]
        player1.get_score(roll1)
        player1.get_score(roll2)
        player1.get_score(roll3)

        result = player1.get_score(roll4)

        self.assertEqual(expected, result)

    def test_detonation_of_last_game(self):
        player1 = Player()
        expected = "Has detonado el final de partida. Tu puntuación final es: 3100. El resto de jugadores tiene una última oportunidad de puntuar."
        roll1 = [1, 1, 1, 2, 2]
        roll2 = [1, 1, 1, 2, 2]
        roll3 = [1, 1, 1, 1, 2]
        player1.get_score(roll1)
        player1.get_score(roll2)

        result = player1.get_score(roll3)

        self.assertEqual(expected, result)

    def test_multiplayer_game(self):
        player1 = Player()
        player2 = Player()
        expected1 = "Tu puntuació es de: 1000"
        expected2 = "Tu puntuació es de: 500"
        roll1_p1 = [1, 1, 1, 2, 2]
        roll1_p2 = [5, 5, 5, 2, 2]

        result1 = player1.get_score(roll1_p1)
        result2 = player2.get_score(roll1_p2)

        self.assertEqual(expected1, result1)
        self.assertEqual(expected2, result2)

    def test_multiplayer_game(self):
        player1 = Player()
        player2 = Player()
        expected1 = "Tu puntuació es de: 1000"
        expected2 = "Tu puntuació es de: 500"
        roll1_p1 = [1, 1, 1, 2, 2]
        roll1_p2 = [5, 5, 5, 2, 2]

        result1 = player1.get_score(roll1_p1)
        result2 = player2.get_score(roll1_p2)

        self.assertEqual(expected1, result1)
        self.assertEqual(expected2, result2)

if __name__ == "__main__":
    unittest.main()
