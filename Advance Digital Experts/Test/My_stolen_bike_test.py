import unittest
from Advance Digital Experts import agente

from bike import Bike
from department import Department

bike_description = ["00001AAA", "rojo", "carretera", "desaparecida", "Jose García",
                    "19/03/2022", "sin descripción", "c/Francisco de Goya, 3"]


class TestStolenBike(unittest.TestCase):
    def test_record_incident(self):
        # Arrange
        incident = Bike()
        expected = "Se ha registrado un el incidente"

        # Act
        result = incident.recorded_incident()

        # Assert
        self.assertEqual(expected, result)

    def test_department_random_assignment(self):
        # Arrange
        department = Department()
        expected = "randomized"

        # Act
        result = department.set_department()
        if result in department._department:
            result = "randomized"

        # Assert
        self.assertEqual(expected, result)

    def test_unassigned_department(self):
        # Arrange
        bike = Bike()
        # Department().available_department = False
        # Department().set_department_availability()
        bike.set_bike(bike_description)
        expected = "not assigned"

        # Act
        result = bike.get_department()

        # Assert
        self.assertEqual(expected, result)

    def test_define_bike(self):
        # Arrange
        bike = Bike()
        bike.set_bike(bike_description)
        expected = {"license": "00001AAA", "color": "rojo", "type": "carretera",
                    "status": "desaparecida", "owner": "Jose García", "date": "19/03/2022",
                    "description": "sin descripción", "address": "c/Francisco de Goya, 3",
                    "department": "not assigned"}

        # Act
        result = bike.get_bike()

        # Assert
        self.assertEqual(expected, result)

    def test_bike_status(self):
        # Arrange
        status = Bike()
        expected = "desaparecida"
        status.set_bike(bike_description)

        # Act
        result = status.set_status()

        # Assert
        self.assertEqual(expected, result)

    def test_change_status(self):
        # Arrange
        status = Bike()
        expected = "encontrada"
        status.set_bike(bike_description)
        status.get_status()

        # Act
        result = status.set_status()

        # Assert
        self.assertEqual(expected, result)

    def test_bike_address(self):
        # Arrange
        bike = Bike()
        expected = "c/Francisco de Goya, 3"
        bike.set_bike(bike_description)

        # Act
        result = bike.get_address()

        # Assert
        self.assertEqual(expected, result)

    def test_bike_address(self):
        # Arrange
        bike = Bike()
        expected = "c/Francisco de Goya, 3"
        bike.set_bike(bike_description)

        # Act
        result = bike.get_address()

        # Assert
        self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()
