import unittest
from Potter_books import *


class PotterBooksTest(unittest.TestCase):
    def test_read_shopping_list(self):
        # Arrange
        article = ShoppingBasket()
        expected = [1]
        article.set_books(1)

        # Act
        result = article.get_books()

        # Assert
        self.assertEqual(result, expected)

    def test_read_shopping_list2(self):
        article = ShoppingBasket()
        expected = [1, 2, 3, 1, 3]
        article.set_books(1, 2, 3, 1, 3)

        result = article.get_books()

        self.assertEqual(result, expected)

    def test_regular_price(self):
        basket = ShoppingBasket()
        expected = [0, 2, 0, 1, 0]
        basket.set_books(4, 2, 2)
        basket.set_shopping_basket()

        result = basket.get_shopping_basket()

        self.assertEqual(result, expected)

    def test_one_book_for_8_euros(self):
        basket = ShoppingBasket()
        expected = 8
        basket.set_books(4)
        basket.set_shopping_basket()

        result = basket.get_shopping_basket()

        self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main()
