import unittest
from Christmas_Party import SantaGestor


class TestChristmasParty(unittest.TestCase):
    def test_physical_product_generates_packing(self):
        # Arrange
        santa_gestor = SantaGestor()
        expected = "Se ha generado un albarán"
        product = {"Type": "Producto físico", "Description": "Juguete"}

        # Act
        result = santa_gestor.process_product(product)

        # Assert
        self.assertEqual(expected, result)

    def test_book_generates_packing(self):
        # Arrange
        santa_gestor = SantaGestor()
        expected = "Se han generado dos albaranes"
        product = {"Type": "Libro", "Description": "El Quijote"}

        # Act
        result = santa_gestor.process_product(product)

        # Assert
        self.assertEqual(expected, result)

    def test_netflix_activate_membership(self):
        # Arrange
        santa_gestor = SantaGestor()
        expected = "Se ha activado la subscripción"
        product = {"Type": "Netflix", "Description": "subscripción de Netflix"}

        # Act
        result = santa_gestor.process_product(product)

        # Assert
        self.assertEqual(expected, result)

    def test_default_error(self):
        # Arrange
        santa_gestor = SantaGestor()
        expected = "El producto no está en la lista"
        product = {"Type": "Objeto", "Description": "Nada"}

        # Act
        result = santa_gestor.process_product(product)

        # Assert
        self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()
