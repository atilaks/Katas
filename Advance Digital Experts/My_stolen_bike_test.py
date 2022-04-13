import unittest
from My_stolen_bike import Bike


class TestStolenBike(unittest.TestCase):
    def test_record_incident(self):
        # Arrange
        incident = Bike()
        expected = "Se ha registrado un el incidente"

        # Act
        result = incident.recorded_incident()

        # Assert
        self.assertEqual(expected, result)

    def test_define_bike(self):
        # Arrange
        bike = Bike()
        bike_description = ["00001AAA", "rojo", "carretera", "desaparecida", "Jose García",
                            "19/03/2022", "sin descripción", "sin dirección"]
        expected = {"license": "00001AAA", "color": "rojo", "type": "carretera",
                    "status": "desaparecida", "owner": "Jose García", "date": "19/03/2022",
                    "description": "sin descripción", "address": "sin dirección"}
        bike.set_bike(bike_description)

        # Act
        result = bike.get_bike()

        # Assert
        self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()
