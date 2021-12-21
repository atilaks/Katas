import unittest
from Scuba_Divers import *


class TestScubaDivers(unittest.TestCase):
    def test_initial_oxygen(self):
        # Arrange
        diver1 = Game()
        expected = "Oxígeno: 150"

        # Act
        result = diver1.get_oxygen()

        # Assert
        self.assertEqual(expected, result)

    def test_initial_depth(self):
        diver1 = Game()
        expected = "Profundidad: 0"

        result = diver1.get_depth()

        self.assertEqual(expected, result)

    def test_point_status(self):
        diver1 = Game()
        expected = "Puntos: 1"
        diver1.set_action("Down")

        result = diver1.get_points()

        self.assertEqual(expected, result)

    def test_action_down(self):
        diver1 = Game()
        expected = "Oxígeno: 148\nProfundidad: 1\nPuntos: 1"
        diver1.set_action("Down")

        result = diver1.get_status()

        self.assertEqual(expected, result)

    def test_action_up(self):
        diver1 = Game()
        expected = "Oxígeno: 143\nProfundidad: 1\nPuntos: 1"
        diver1.set_parameters(144, 2)
        diver1.set_action("Up")

        result = diver1.get_status()

        self.assertEqual(expected, result)

    def test_action_keep(self):
        diver1 = Game()
        expected = "Oxígeno: 143.5\nProfundidad: 2\nPuntos: 2"
        diver1.set_parameters(144, 2)
        diver1.set_action("Keep")

        result = diver1.get_status()

        self.assertEqual(expected, result)

    def test_sea_level(self):
        diver1 = Game()
        expected = "No puedes subir más"
        action = "Up"

        result = diver1.core_method(action)

        self.assertEqual(expected, result)

    def test_core_method(self):
        diver1 = Game()
        expected = "Oxígeno: 144\nProfundidad: 2\nPuntos: 2"
        diver1.set_parameters(148, 1)
        action = "Down"

        result = diver1.core_method(action)

        self.assertEqual(expected, result)

    def test_dead_end(self):
        diver1 = Game()
        expected = "Mueres. No puntúas"
        diver1.set_parameters(1, 3)
        action = "Up"

        result = diver1.core_method(action)

        self.assertEqual(expected, result)

    def test_end_game(self):
        diver1 = Game()
        expected = "Has terminado la partida.\nPuntos: 3"
        diver1.set_parameters(140, 3)
        diver1.set_action("Up")
        diver1.set_action("Up")
        action = "Up"

        result = diver1.core_method(action)

        self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()
